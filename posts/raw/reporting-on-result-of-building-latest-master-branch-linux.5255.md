Leith | 2019-06-26 02:01:53 UTC | #1

On the bright side, I noticed that ScriptFile::Execute method now supports an optional ReturnValue! Very nice!

I still can't use the most recent Editor though - in an empty scene, it's crashing the moment I try to add my first component to my first node (it was a staticmodel, though I doubt its relevant).
Right before that happens, the editor complains loudly about not understanding the content of a number of xml files in my resource path which happen to be custom data files and not urho content files as such.
I close the error log popup, I add a node, I try to add a component, bang.

Perhaps the issue I am experiencing is somehow related to the failure to parse those custom xml files?

-------------------------

weitjong | 2019-06-26 04:04:59 UTC | #2

Like I said before in other thread, when you break the engine then you keep the pieces too. If you customize the engine or use the custom data format then you have to be clear with that or show us some code or otherwise no one will be able to reproduce.

-------------------------

SirNate0 | 2019-06-26 04:20:06 UTC | #3

I'm pretty sure you can ignore all the "Failed to parse XML" (or however it's phrased, I can't check right now) - I get a very large number of them as well, I think from the editor trying to guess the resource type of all the files in the directory so it can show them with the right icon.

One thing I've run into before when updating (I'm not sure it's your problem, since I don't know you would have been able to run the editor at all) - are you certain you updated the Data directory the editor scripts are being run from?

-------------------------

Leith | 2019-06-26 06:41:43 UTC | #4

This is a clean, full rebuild of master, pulled down 2 days ago... I also forked the repo - there are a few changes I have proposed recently (nothing too ground-breaking imho) ... I wanted to be sure that any PR I may issue will reflect a "clean codebase".
There's nothing of my modifications in the build - still the editor is crashing on me.
I'll try reverting the resource path...

-------------------------

Leith | 2019-06-26 06:24:30 UTC | #5

Yeah - I completely rebuilt Urho from scratch, overwriting my entire build folder, and recompiling the entire thing ... ahhh - the editor resource path is pointing at my project binfolder, and that contains old scripts... that could explain something. Yeah, I need to try resetting my resource path and see if the problem is indeed that the editor is picking up old scripts from my project resources folder.

-------------------------

