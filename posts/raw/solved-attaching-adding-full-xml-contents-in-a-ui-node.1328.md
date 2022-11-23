rasteron | 2017-01-02 01:06:51 UTC | #1

Hey guys,

I'm trying to figure out how to completely load and attach a layout content to a UI node/window. It looks like it only adds the first instance of the content

[code]UIElement@ MyWindow = ui.LoadLayout(cache.GetResource("XMLFile", "UI/MyWindow.xml"));
ui.root.AddChild(MyWindow);

UIElement@ listContainer = MyWindow.GetChild("ListContainer", true);
    
File loadFile(fileSystem.programDir + "Data/UI/Data.xml", FILE_READ);
listContainer.LoadXML(loadFile);[/code]

I also tried AddChild() and got the same results. The data is only composed of multiple custom UI elements with horizontal layout mode/style.

Appreciate any help.

-------------------------

cadaver | 2017-01-02 01:06:51 UTC | #2

Legal XML must have one root node. Therefore the XML layout you are instantiating also would need to have exactly one top-level element. It can be a bare UIElement that contains other elements.

-------------------------

rasteron | 2017-01-02 01:06:51 UTC | #3

Thanks Lasse. I got confused there for a bit and yes, works great now :smiley:

-------------------------

