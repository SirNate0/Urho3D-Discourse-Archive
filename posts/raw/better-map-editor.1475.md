Hevedy | 2017-01-02 01:08:02 UTC | #1

The current map editor is bad designed to make real maps and i don't get that of need create subnodes and nodes in nodes to add a simple mesh to the level, and location and rotation properties texbox should be more responsive and show the whole number and select the whole number when you click in one textbox of that. And the nodes should be hidden or something in the editor, the editor make that changes in the background no you in the editor, that no make sense.

Take ages create the same created in other game engine.

-------------------------

cin | 2017-01-02 01:08:03 UTC | #2

[quote="Hevedy"]i don't get that of need create subnodes and nodes in nodes to add a simple mesh to the level,[/quote]

You can create prefab - set of nodes with required components. Save node to xml-file and just drag and drop from Resource Browser windows to parent node.
If you want to make many copies of this node in scene. you can use Spawn Editor to make copies of node in picked by mouse position in scene.

[quote="Hevedy"] location and rotation properties texbox should be more responsive and show the whole number and select the whole number when you click in one textbox of that.[/quote]
Explain more specifically what you mean by "should be more responsive".

[quote="Hevedy"] and select the whole number[/quote] 
You can double click in field to select value.

[quote="Hevedy"] And the nodes should be hidden or something in the editor, the editor make that changes in the background no you in the editor, that no make sense.[/quote]
Explained more specifically with example.

-------------------------

codingmonkey | 2017-01-02 01:08:03 UTC | #3

The main problem i think what the Urho3D presented as "tiny library", and not something huge with every time growing up abilities from "box".
After all the main growing up mechanics of Urho3D is commits from contributors. In this situation the main principle  - if you needed some kind of extended functionality? Do it! And if it working properly, please do PR into master for others :slight_smile:

-------------------------

boberfly | 2017-01-02 01:08:03 UTC | #4

Yeah Urho3D has always been (IMO) the right balance between just enough engine but leaving the door open for your own stuff to work with it without being a monster of a codebase to deal with. Plus the excellent and easy to use CMake build system is a huge huge win.

-------------------------

Hevedy | 2017-01-02 01:08:04 UTC | #5

My idea at the first is support the UE4 and Urho3D but with the map editor I can't support then my next project for Unreal Engine 4 and Urho3D atm.
It's too hard try to do the same with this tools.

-------------------------

bukkits | 2017-01-02 01:08:15 UTC | #6

I'm also a little confused at these complaints, but I would like there to be more documentation on using the editor as many of the features are still a mystery to me.
Most of what I've learned has been through trial and error

-------------------------

cadaver | 2017-01-02 01:08:15 UTC | #7

Sometimes people contribute features but don't update the editor documentation, and when merging those PR's we don't always catch this. And the instructions were quite sparse to begin with. The absolutely best editor documentation is the source code.

-------------------------

christianclavet | 2017-01-02 01:08:16 UTC | #8

Hi, 
Some GUIs might need to be improved first before the editor can be improved. They are linked together. A better gui will have a better editor. The current GUI is really good for creating games or demos, but would need improvement to make editors.

I see some parts in the editor that could need to be worked on first:
- Inpector window (Should allow to edit lots of item and don't scale but have content that can be scrolled), 
- Each element (component) of the inspector windows, should have a fixed size but can be collapsed.
- Main 3D background is too dark, Should be like gray when editing and use the defined color when playing back. It's logical that the 3D background be black since it's not defined but make it harder to place stuff when editing.

For the moment, I can't do this, as I'm still really noob with Urho. I've just learned how to compile it properly with the feature I need and generate the docs. (Linux and Windows) I'm still reading how the examples are done.

-------------------------

christianclavet | 2017-01-02 01:08:17 UTC | #9

Hi, Thanks for the hints about the background. By that I was meaning, as other editors out there a neutral background color (not the sky or the ground) that would be used in "editing" mode. But not used in "playback" mode (would use the world information in light, fog, sky)
As an example in this screen, the background is a neutral gray. Easier to place stuff, when doing level editing. We could have "preview/play" mode button that show the scene after if the button is pressed to see what the environment is really looking with the light, and environment settings. But start with this as default. This would allow people to start placing stuff faster, easier, then when wanting to deal with the lighting details would press the preview button to toggle to the environment lighting / background.

Here is a exemple that would be in "default" edit mode with a neutral background: (Images references taken from Maya and Unreal editor, but could have been taken from others also)
[img]https://i.ytimg.com/vi/tU1TvTveFfQ/maxresdefault.jpg[/img]
In this mode the lighting could be a simple light setup that follow the editing camera. All other lights would be off.

Here is a exemple that would be in preview mode with full lighting enabled:
[img]https://de45xmedrsdbp.cloudfront.net/blog/46Release/Updated/image23-1600x900-1570981615.png[/img]
The editing mode light would be disabled and the light setup that was defined would be enabled.

[quote]Would videos be useful to people that have trouble with the workflow? As in organized lesson-plan style ones?[/quote]
Any video would be great!

-------------------------

bukkits | 2017-01-02 01:08:20 UTC | #10

[quote="Sinoid"]

Would videos be useful to people that have trouble with the workflow? As in organized lesson-plan style ones?[/quote]


Absolutely. The biggest complaint I have with the editor right now is that there's very little direction in finding a workflow in the editor. It looks like it already has some power behind it, I just don't know where to begin.

-------------------------

pqftgs | 2017-01-02 01:08:21 UTC | #11

[quote="bukkits"][quote="Sinoid"]
Would videos be useful to people that have trouble with the workflow? As in organized lesson-plan style ones?[/quote]
Absolutely. The biggest complaint I have with the editor right now is that there's very little direction in finding a workflow in the editor. It looks like it already has some power behind it, I just don't know where to begin.[/quote]
I second this

-------------------------

Modanung | 2017-01-02 01:08:35 UTC | #12

What I really like about the editor is how the controls seem to aim at mimicking those of Blender, which is the obvious choice of modelling software for any Urho3D developer.
I understand it's a work in progress, but here's a list of things I ran into about the Blender controls in the Urho3D editor that were found not to be as in Blender (yet):
[spoiler]Ctrl+G should show a naming dialog and parent the selection to a new node with that name.
Numpad 4, 2, 6 and 8 should rotate the camera, Num[+] and num[-] and Ctrl+mmb should move forward and backward
Num[.] should center view on selection
Delete should also delete, not only X
Select/Deselect all should done with A instead of Ctrl+A
Shift+A should bring up the create menu under the cursor
P should pause/play the game
pop-up menus should appear under cursor and move the cursor out of them should close them
arrows should navigate pop-up menus
enter/return should confirm pop-up menus
Ctrl+N should load default scene instead Ctrl+Shift+N
G/R/S should activate the action instead of selecting it
	(Shift+)X/Y/Z should lock the manipulation to an axis or plane
	Escape should cancel the manipulation, lmb/Space/Enter should comfirm it
Ctrl+Space should hide the manipulator
Shift+D should initiante a grab operation on the duplicate

Fly mode:
	Tab to enable/disable gravity
	Teleporting using space or mmb
	Escape/rmb should return to previous position
	Shift/Alt/scroll speed up/down
	lmb/enter should apply view change

3D cursor:
	Missing yet which is an awesome Blender feature. In the Urho3D Editor it would be awesome for array-like placement of duplicate objects.
	. , Ctr+. Ctrl+, for changing pivot mode
	Shift+S for the snapping menu
Arithmatic should be allowed in number fields that are applied on enter.
Having an 'active' member of the selection is important for certain operations:
- Parenting
- Alignment

Enable/Disable Lock/Unlock Nodes and Components in the hiearchy as well[/spoiler]
Thought it might be a useful reference. It is very likely that this list is not complete (and outdated).

-------------------------

