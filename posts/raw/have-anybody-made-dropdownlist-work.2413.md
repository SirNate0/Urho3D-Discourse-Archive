slapin | 2017-01-02 01:15:16 UTC | #1

Hi all!

I have the following code:
[code]
UIElement@ CreateShapeType()
{
    UIElement@ uie = UIElement();
    uie.SetFixedHeight(30);
    Text@ item = Text();
    item.style = "PropertyText";
    item.size = IntVector2(100, 30);
    item.text = "Shape";
    DropDownList@ lv = DropDownList();
    lv.style = "PropertyListView";
    lv.SetStyleAuto();
    Text@ item1 = Text();
    item1.style = "PropertyText";
    item1.size = IntVector2(60, 30);
    item1.text = "CAPSULE";
    lv.AddItem(item1);
    Text@ item2 = Text();
    item2.style = "PropertyText";
    item2.size = IntVector2(60, 30);
    item2.text = "BOX";
    lv.AddItem(item2);
    lv.position = IntVector2(70, 0);
    lv.size = IntVector2(90, 36);
    lv.minHeight = 30;
    lv.selection = 1;
    lv.resizePopup = true;
    lv.getPopup().SetStyleAuto();
    uie.AddChild(item);
    uie.AddChild(lv);
    uie.SetStyleAuto();
    return uie;
}
[/code]

This displays empty DropDownList, if I click it displays empty popup. So this behaves like it is empty.
The decoration is fine.
Styles:
[code]
    <element type="PropertyText">
        <attribute name="Font" value="Font;Fonts/Anonymous Pro.ttf" />
        <attribute name="Font Size" value="18" />
        <attribute name="Color" value="0.3 0.2 0.2" />
    </element>
    <element type="PropertyListView" style="HierarchyListView">
        <attribute name="Hierarchy Mode" value="true" />
        <attribute name="Base Indent" value="1" />  <!-- Allocate space for overlay icon at the first level -->
        <element type="BorderImage" internal="true">
            <element type="HierarchyContainer" internal="true">
                <attribute name="Layout Mode" value="Vertical" />
            </element>
        </element>
        <element type="UIElement" internal="true">
        </element>
    </element>
[/code]

-------------------------

rasteron | 2017-01-02 01:15:28 UTC | #2

Hey slapin, you should probably take a look at some of the Editor code. There's a lot of dropdown elements there to check out. Here's one:

[github.com/urho3d/Urho3D/blob/m ... erences.as](https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/Editor/EditorPreferences.as)

-------------------------

Miegamicis | 2017-01-02 01:15:28 UTC | #3

I managed to create it after looking at the Console code. C++ code looks like this:

[code]
dropdown = static_cast<DropDownList*>(viewElement->GetChild("dropdownElement", true));
Vector<String> elements;
elements.Push("item1");
elements.Push("item2");
elements.Push("item3");
elements.Push("item4");

for (auto it = elements.Begin(); it != elements.End(); ++it) {
	Text* text = new Text(context_);
	text->SetStyle("ConsoleText");
	text->SetText((*it));
	dropdown->AddItem(text);
}
[/code]

Hope this may help!

-------------------------

