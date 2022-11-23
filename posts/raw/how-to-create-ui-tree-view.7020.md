najak3d | 2021-10-25 07:06:40 UTC | #1

We're planning to use Urho's GUI system, but need a TreeView control, which does not exist natively.

What is the best way to create a Tree View from the existing native classes?  I'm guessing we'll need to create a new class, that derives from UIElement, and then manages the contents of this container manually.

But TreeView seems like a pretty common control - plus we see it in the Urho Editor too.   So we didn't want to re-invent the wheel, if it's already done.   Or, if we do need to "invent this wheel", we're looking for a few hints/pointers on how to best go about it.

-------------------------

Eugene | 2021-10-25 08:01:30 UTC | #2

`ListView` has some flags that let it be a tree. You can check editor scripts to see how exactly it's working.
https://github.com/urho3d/Urho3D/blob/9f968f3d24a97ee0619e1310522ebb6e89507363/bin/Data/Scripts/Editor/EditorHierarchyWindow.as#L26

-------------------------

najak3d | 2021-11-01 07:44:20 UTC | #3

OK - trying to make this work, but ListView is not acting very well, with two defects:
1. The Scrollbar is not working.  It shows, but doesn't reflect that there are 30 items in the ListView to be shown, and you cannot scroll down.
2. The click area for each item is cut too narrow by about 20 pixels (the final 2 characters "<=" are non-clickable).   Not a huge deal, but worth noting; should be fixed.

**Here is my code (inserted into the "HelloGUI" sample:**

			Urho.Gui.ListView treeView = new ListView();
                        treeView.Size = new IntVector2(w, 150);
			treeView.Position = new IntVector2(xmargin, y);
			treeView.HierarchyMode = true;
			treeView.LayoutMode = LayoutMode.Free;

			window.AddChild(treeView);
			treeView.SetStyleAuto();

			for (int i = 0; i < 30; i++)
			{
				Text item = new Text();
				item.Size = new IntVector2(w - 20, 15);
				item.Position = new IntVector2(5, i * 15);
				item.Name = "Item #" + i + ": not clickabled beyond here=>|<=";
				item.Value = item.Name;
				treeView.AddItem(item);
				item.SetStyleAuto();
			}

And here is the resulting output:

![image|496x224](upload://yUWfkFFFGEsfwaWkZ4DGTHGHgnj.png)

-------------------------

najak3d | 2021-11-01 08:12:59 UTC | #4

The Samples could really use a more GUI samples, to show at least one example of every GUI control type.  Currently, it only shows Window, Button, CheckBox, and LineEdit controls.  No others.

And the LineEdit control has the defect of no "ClipBorder"... so that the cursor starts out flush with the left border (no margin).   I finally figured a fix for this by adding a single line of code for each LineEdit instance:

			lineEdit.ClipBorder = new IntRect(7, 0, 7, 0);

(Which here provides 7 pixel margin on both left and right sides.)

Without this fix, it looks like this:

![image|390x59](upload://cOZbGXRAFw0OZ1xwAUCdcheP9ZR.png)


and with the fix, it looks like this:

![image|382x57](upload://ue4vdL8lL9IKPtkZ14gyTVJgFPf.png)

-------------------------

elix22 | 2021-11-01 11:34:21 UTC | #5

UI is tricky , but it is manageable once you know how to work with it .
I wrote a quick and basic example using my UIBuilder , it should also work on stock frameworks
https://github.com/Urho-Net/Samples/blob/main/UIBuilder/Source/HotReload/UI/TreeViewWindow.cs 
The items are expended/collapsing by double clicking them

![Screen Shot 2021-11-01 at 13.21.17|690x431](upload://iUZNjdM4UwhTQePY8xGX82PFY0u.jpeg)

-------------------------

najak3d | 2021-11-02 06:10:56 UTC | #6

We're stuck on UrhoSharp, which is over 3 years old now, and aging.  The GUI here seems to have some  bugs, such as I presented.   Looks like we'll hold off on the GUI work until we are able to switch to your Urho.NET, which we hope may be soon.   :)

-------------------------

