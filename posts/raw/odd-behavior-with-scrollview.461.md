thebluefish | 2017-01-02 01:00:37 UTC | #1

I want to confirm if this is a bug or if I'm just doing something wrong. There's two issues here actually.

Here's how I'm setting up my ScrollView:
[code]
_scrollview_chat = chatContainer->CreateChild<Urho3D::ScrollView>();
_scrollview_chat->SetStyleAuto();
_scrollview_chat->SetFocusMode(Urho3D::FM_NOTFOCUSABLE);
_scrollview_chat->SetEditable(false);
_scrollview_chat->SetSize(chatContainer->GetWidth(), chatContainer->GetHeight() - 24);
_scrollview_chat->SetPosition(0, 0);

Urho3D::UIElement* chatContentElement = _scrollview_chat->CreateChild<Urho3D::UIElement>();
_scrollview_chat->SetContentElement(chatContentElement);
chatContentElement->SetLayoutMode(Urho3D::LM_VERTICAL);
chatContentElement->SetStyleAuto();
chatContentElement->SetPosition(0, -12);
chatContentElement->SetAlignment(Urho3D::HA_LEFT, Urho3D::VA_BOTTOM);
[/code]

Here's how I add a message:
[code]
Urho3D::Text* text = _scrollview_chat->GetContentElement()->CreateChild<Urho3D::Text>();
//text->SetWordwrap(true);
text->SetFont(font, 12);
text->SetText(sender + ": " +message);
[/code]

The first issue that I'm experiencing is that the scrollbar doesn't properly work with the alignment VA_BOTTOM. Elements populate bottom-to-top as they should, but the scrollbar still expands from the top instead of the bottom.

I've included some screenshots showing the behavior here: [imgur.com/a/ywDZn](http://imgur.com/a/ywDZn)

My second issue is that word wrap does not work properly. In the above code, I've uncommented the following:
[code]
text->SetWordwrap(true);
[/code]

However what this does is cause the text not to appear entirely. The length of the text causes the height of the scrollview content element to become very tall, indicating that it is likely wrapping the text to be 1 character wide.

-------------------------

cadaver | 2017-01-02 01:00:37 UTC | #2

The ScrollView's content element should be left at 0,0, alignment HA_LEFT, VA_TOP; think of it as a canvas extending from the top-left edge of the ScrollView.

You can also use ListView which allows you to add child items directly (it handles the content container for you). Two examples of adding chat-like text elements to a list are Console.cpp and the Chat sample application.

However everything doable with ListView should also be doable with ScrollView, it just takes more effort. I'll try to cook up a basic code example below.

-------------------------

cadaver | 2017-01-02 01:00:37 UTC | #3

Here is a minimal example. It's in AngelScript but should be quite easily translatable to C++. While writing it I uncovered something weird related to use of wordwrap and vertical layout: the content element should resize itself to the children's combined height, but is instead left too large if I don't call UpdateLayout manually in the end. I'll make an issue of that.

[code]
UIElement@ content;

void CreateUI()
{
    XMLFile@ uiStyle = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
    // Set style to the UI root so that elements will inherit it
    ui.root.defaultStyle = uiStyle;

    Window@ window = ui.root.CreateChild("Window");
    window.size = IntVector2(400, 300);
    window.position = IntVector2(100, 100);
    window.movable = true;
    window.SetStyleAuto();
    
    ScrollView@ view = window.CreateChild("ScrollView");
    view.position = IntVector2(10, 10);
    view.size = IntVector2(380, 280);
    view.SetStyleAuto();
    
    content = UIElement();
    view.contentElement = content;
    content.SetLayout(LM_VERTICAL);
    content.SetFixedWidth(376); // Scrollview has a small border around the edges, account for that

    for (int i = 0; i < 10; ++i)
    {
        Text@ text = content.CreateChild("Text");
        text.SetStyleAuto();
        text.wordwrap = true;
        text.text = "Longcat and Tacgnol fought the battle of Catnarok. No-one survived";
    }
    // There is currently a bug which requires calling this manually after manipulating children.
    // It shouldn't be necessary. Otherwise content element is left too big. This has to do with
    // wordwrap, as the bug doesn't appear if wordwrap in the children is left false
    content.UpdateLayout();
}
[/code]

-------------------------

cadaver | 2017-01-02 01:00:38 UTC | #4

Another example doing the same with ListView, this time with a resizable window. ListView actually behaves more robustly when used with wordwrap text elements and dynamic resizing, and is easier to use when all you need is to just stack the items vertically:

[code]
void CreateUI()
{
    XMLFile@ uiStyle = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
    // Set style to the UI root so that elements will inherit it
    ui.root.defaultStyle = uiStyle;

    Window@ window = ui.root.CreateChild("Window");
    window.size = IntVector2(400, 300);
    window.position = IntVector2(100, 100);
    window.movable = true;
    window.SetStyleAuto();
    window.resizable = true;
    window.SetLayout(LM_VERTICAL);
    window.layoutBorder = IntRect(20,20,20,20);

    ListView@ view = window.CreateChild("ListView");
    view.minSize = IntVector2(300, 200);
    view.SetStyleAuto();

    for (int i = 0; i < 10; ++i)
    {
        Text@ text = Text();
        text.defaultStyle = uiStyle;
        text.SetStyleAuto();
        text.text = "Longcat and Tacgnol fought the battle of Catnarok. No-one survived";
        text.wordwrap = true;
        view.AddItem(text);
    }
    SubscribeToEvent("Update", "HandleUpdate");
}
[/code]

-------------------------

thebluefish | 2017-01-02 01:00:38 UTC | #5

For the chat box bit I went ahead with a ListView since that is probably better in this case. I did figure out that there is some odd behavior with the scrollbar when I created my items as a child of the listbox (scrollview has same odd behavior) and then add it to the listview items. However as in your examples, creating it separately then adding it does just fine. I think that's a big part of where my confusion came from as well. However it is all working good for now, thanks again.

-------------------------

