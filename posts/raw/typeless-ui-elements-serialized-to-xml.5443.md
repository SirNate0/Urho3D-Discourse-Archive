Leith | 2019-08-10 04:24:57 UTC | #1

One of my test applications features a very simple UI consisting of a Window that contains a fistful of UI elements - its little more than a copy of the code from HelloGUI sample.

When I dump the UI root node to XML, I see that my Window element is buried in a fairly complex hierarchy of elements that all look like so:
[quote]
				<element>
					<attribute name="Size" value="1920 1080" />
					<attribute name="Pivot" value="0 0" />
				</element>
[/quote]

That's my app window resolution - 1920 x 1080.
There are literally dozens of these "typeless elements" in the resulting UI xml file (which incidentally, appears to load perfectly).
What are all these "typeless elements" for?

[EDIT]
When I use the Editor to examine the structure of the resulting XML file, I can see that the IDs for my Window and its children begins at 182.
There's literally over 180 elements in the hierarchy prior to my stuff, and they all appear to do not much to my untrained eye.

-------------------------

Leith | 2019-08-10 04:51:40 UTC | #2

Ahh! I was not "trashing the existing UI" correctly, when attempting to reload the dumpfile.
This was resulting in the UI root node being duplicated during serialization/deserialization.

[code]
uiRoot_->RemoveAllChildren(); // trash the ui system
uiRoot->AddChild(newRoot);    // attach what we loaded from xml
[/code]

-------------------------

Leith | 2019-08-10 05:06:04 UTC | #3

I ended up specifically omitting the UI root element when saving the UI - this is certainly not ideal, but I found no obvious way to replace the UI root node after reload.

-------------------------

Modanung | 2019-08-10 11:43:54 UTC | #4

Have you tried `GetSubsystem<UI>()->LoadLayout(...)`?

-------------------------

Leith | 2019-08-10 12:45:12 UTC | #5

[code]
        /// Format absolute filepath
        String fullpath=GetSubsystem<FileSystem>()->GetProgramDir ()+filepath ;

        /// Create a File object
        File file(context_);

        /// Use our File object to open a file
        file.Open(fullpath);
        if(file.IsOpen()){

            /// Load a UI Layout from file
            SharedPtr<UIElement> newRoot = GetSubsystem<UI>()->LoadLayout(file);
[/code]
yep

-------------------------

