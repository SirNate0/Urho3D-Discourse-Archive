slapin | 2017-05-09 01:04:44 UTC | #1

Hi, all!

As I told a lot lately I have showstopper kind of trouble with UI elements which generate popup window.
These are Menu and DropDownList. Both do display original widget but fail to display popup menu.
Today I was able to  display Menu popup for some time but after some minimal change it stopped working again
and then I was not able to repeat the result. Struggling for 20+ hours for nothing again, I decided to
debug the thing properly, so to find out why it is so brittle. Could somebody point me out somewhere in Urho code
so I look for the culprits?
Please don't point me to editor, I know everything works there, but it is not possible to repeat.
Probably there are some not obvious magic happens.
I found that popup window defaultStyle needs to be set to style XML otherwise it will display
white (root window style do not apply), but that happened before. Now I see nothing at all,
like nothing is drawn and the click is ignored. I tried to display popup window manually and it works fine,
so it is something with menu itself which is wrong. I will probably replace it with separate button and menu
if debugging will take too long, but I'd prefer to finally make such widgets work and solve this puzzle...

-------------------------

SirNate0 | 2017-05-09 04:00:51 UTC | #2

Can't offer advice on debugging the GUI, but here's the code I use to make a dropdown list for a simple in-game editor I have (if you need any more of the code let me know, I tried to just pull out whatever was needed for the DropDownList):

```cpp
SharedPtr<UIElement> me_;
	static SharedPtr<XMLFile> Style;

void EditorGroup::SetPosition(UIElement* child)
{
	if (!child)
		return;
	IntVector2 size = child->GetMinSize();
	child->SetPosition(position_);
	if (useColumns_)
	{
		position_.y_ += size.y_;
		breakOffset_ = Max(size.x_, breakOffset_);
		me_->SetMinSize(position_.x_ + breakOffset_, position_.y_);
	}
	else
	{
		position_.x_ += size.x_;
		breakOffset_ = Max(size.y_, breakOffset_);
		me_->SetMinSize(position_.x_, position_.y_ + breakOffset_);
	}
	child->SetStyleAuto(Style);
}

EditorGroup* EditorGroup::CreateDropdown(String label, Vector<Variant> values, int val)
{

	DropDownList* l = me_->CreateChild<DropDownList>(label);
	int height = 0; int width = 0;
	for (int i = 0; i < values.Size(); ++i)
	{
		width = Max(width, 8*values[i].GetString().Length());
		height = Max(height, 16);
	}
	l->SetPlaceholderText(label);
	l->SetResizePopup(true);
	l->SetSelection(0);
	EditorGroup* c = new EditorGroup(l);
	l->SetMinSize(width, height);
	SetPosition(l);

	for (int i = 0; i < values.Size(); ++i)
	{
		Text* item = new Text(l->GetContext());
		item->SetText(values[i].ToString());
		item->SetName(values[i].ToString());
		item->SetMinSize(8*values[i].GetString().Length(),16);

		item->SetStyle("EditorEnumAttributeText");
		l->AddItem(item);
	}
	children_.Push(SharedPtr<EditorGroup>(c));
	c->type_ = DROPDOWN;
	c->defaultValue_ = val;
	c->extendedValue_ = values;
	c->SubscribeToEvent(l, E_ITEMSELECTED, HANDLER(EditorGroup, HandleEvent));
	return c;
}
```

-------------------------

slapin | 2017-05-09 11:25:01 UTC | #3

Well, debugging the GUI I found that in both cases I have zero-sized window.
While I set window min sizes, it looks like it was resized to zero so not displaying.
Need to check this some meore...

-------------------------

lezak | 2017-05-09 15:23:33 UTC | #4

I'm unable to reproduce Your problems. Can You show problematic parts of Your code or at least describe layout setup (parent-child structure, aligment etc.)?

You can also check this functions (ie copy and run in hello gui sample), both are working:

    void CreateDropDown()
    {
        DropDownList@ dropDown = ui.root.CreateChild("DropDownList", "List");
        dropDown.SetSize(128, 64);
        dropDown.SetPosition((graphics.width / 6), (graphics.height / 2));
        dropDown.SetStyleAuto();
        
        dropDown.resizePopup = true;
        
        for(int i = 0; i < 5; i++)
        {
            Text@ item = Text();
            item.text = "Item" + String(i);
            item.SetStyleAuto();
            dropDown.AddItem(item);
        }
    }

    void CreatePopupMenu()
    {
        Menu@ menu = ui.root.CreateChild("Menu", "menu");
        menu.SetSize(128,64);
        menu.SetPosition((graphics.width * 0.7), (graphics.height /2));
        menu.SetStyleAuto();
        
        Window@ popup = Window();
        popup.SetSize(128,128);
        popup.SetStyle("Window", cache.GetResource("XMLFile", "UI/DefaultStyle.xml"));
        menu.popup = popup;
        menu.SetPopupOffset(20,10);
        
        Text@ label = popup.CreateChild("Text", "label");
        label.SetStyleAuto();
        label.text = "Popup Menu";
        label.textAlignment = HA_CENTER;
        
        label.enableAnchor = true;
        label.SetMinAnchor(0, 0);
        label.SetMaxAnchor(1, 0.15);
        label.SetPivot(0.0, 0.0);
        
        UIElement@ btnHolder = popup.CreateChild("UIElement", "btnHolder");
        btnHolder.enableAnchor = true;
        btnHolder.SetMinAnchor(0, 0.15);
        btnHolder.SetMaxAnchor(1, 1);
        
        btnHolder.SetLayout(LM_VERTICAL, 0, IntRect(0, 0, 0, 0));
        for(int i = 0; i < 3; i++)
        {
            Button@ btn = btnHolder.CreateChild("Button", "btn");
            btn.SetStyleAuto();
        }
    }

-------------------------

slapin | 2017-05-09 15:43:58 UTC | #5

I'm still in process of debugging. Somehow popup window size is set to 0, I currently debug why this happens.

-------------------------

slapin | 2017-05-09 15:44:32 UTC | #6

I don't want to repeat some magic passes, I want to understand what is really needed.

-------------------------

slapin | 2017-05-09 18:55:37 UTC | #7

OK I now found the solution to my problem.

1. Thou shalt set default style (defaultStyle) for all popup windows.
2. Thou shalt SetLayout(LM_VERTICAL/LM_HRIZONTAL) on popup window.
if LM_FREE is wanted add additional UIElement.
3. ThouShalt SetMinSize after SetLayout.

I'm not sure about 3. but that fixed my problem. Then I removed it and there is no problem.
To be safe I set it back. It looks like it depends on what widgets are in the window.
I have Window->ScrollView->UIElement->{Lots of UIElement->{Checkbox, Text}}
When I did not have ScrollView it worked with 1 + 2, but as I added ScrollView it broke.
While fixing this I also did lots of reordering of operations, so the fix might be reordering + SetMinSize.
I don't know but it works now. I will leave debugging code in there just in case it will break again.

-------------------------

