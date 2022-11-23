rogerdv | 2017-01-02 01:02:47 UTC | #1

Im trying to use a couple of DropDownList widgets, but in the actual game they look different from UI editor. In editor, I can click and they deploy a list, empty and short, but a list. In the code, I tried to add an item
[code]race = step1.GetChild("race", true);
		Text@ glist = Text();
		glist.text = "Male";
		race.AddItem(glist);[/code] 

But it doesnt responds to clicks.

-------------------------

Mike | 2017-01-02 01:02:47 UTC | #2

You have to subscribe race to the "ItemSelected" event.

Also set size, style, resize popup...

-------------------------

rogerdv | 2017-01-02 01:02:47 UTC | #3

nop, that didnt solved the problem. The dropdowns are just boxes that doesnt do anything.

-------------------------

weitjong | 2017-01-02 01:02:48 UTC | #4

You can see how it is done in C++ code in the engine's Console class. Hope this help.

-------------------------

rogerdv | 2017-01-02 01:02:49 UTC | #5

I switched to default style and now they work. I was trying to implement my own look for UI, but seems that it needed fixes to work.

-------------------------

