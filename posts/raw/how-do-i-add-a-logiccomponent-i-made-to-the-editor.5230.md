throwawayerino | 2019-06-14 23:46:36 UTC | #1

I made a standard LogicComponent and would like to be able to place it using the editor. How do I add it?

-------------------------

Leith | 2019-06-15 22:39:23 UTC | #2

Hi, throwawayerino!
I would welcome you to this forum, but I sense your username is temporary?
I asked this exact question very recently...

Urho's editor is entirely written in AngelScript, on top of the Urho3DPlayer application...

You need to modify the sourcecode for Urho3DPlayer... make it include your component, and add a line of code (to Urho3DPlayer.cpp) to register your component class with Urho3D - that will force the compiler and linker to include your component directly in the Player..  now rebuild the Urho3DPlayer application, and your component should now work in the editor.

The reason we need to hack the player app is simply that Urho does not provide a mechanism for "binary plugins" (such as dynamically linked libraries) and the reason for that, I believe, is that some of the target platforms do not support the concept.

-------------------------

throwawayerino | 2019-06-15 15:21:42 UTC | #3

Thanks for the explanation. Can I register objects using angelscript and simply edit a script called at runtime?
Also my name isn't really temporary, I just like it like that

-------------------------

throwawayerino | 2019-06-15 20:51:00 UTC | #4

I added my component and recompiled the editor, but now it complains at startup about AttributeInfo and no matching signatures to load and loadXML

-------------------------

throwawayerino | 2019-06-15 22:39:19 UTC | #5

Nevermind I was being dumb and my editor was out of date. All I had to do was set a category when registering factory

-------------------------

Leith | 2019-06-16 10:15:00 UTC | #6

In that case, welcome to the forum! :four_leaf_clover:
Glad to hear you solved your problem :slight_smile:

-------------------------

Leith | 2019-06-16 10:15:59 UTC | #7

I am stuck using the out of date editor, until/unless some bugs are resolved in the linux build. Ugh.

-------------------------

weitjong | 2019-06-16 11:22:22 UTC | #8

Ahem. I have noticed you always spread the misinformation  about the editor segfaulting bug. That bug you mentioned has been fixed weeks ago. Also that bug did not always manifest itself as it depends on the compiler used, the cosmic alignment and the user luck.

-------------------------

Leith | 2019-06-16 11:31:39 UTC | #9

Thanks for verifying the issue is resolved, i will pull down the changes and confirm.
I would not like to spread false information! Thanks man.
I just got comfortable using the old version of the editor on the new codebase, hopefully all is well!

-------------------------

weitjong | 2019-06-16 16:10:53 UTC | #10

You were clearly in this thread.

https://discourse.urho3d.io/t/urho3d-editor-crashes-on-component-creation/5143

-------------------------

Leith | 2019-06-17 10:12:25 UTC | #11

I was clearly spreading false information? If that is what you meant by "clearly" then please point out at which I point I did so. Certainly not my intent!

-------------------------

weitjong | 2019-06-17 10:13:44 UTC | #12

I meant to say you were clearly In the thread where the bug was announced to be fixed already. So, I totally don’t understand why you keep barking on the editor. We have bug and fixes all the time and we move on.

-------------------------

weitjong | 2019-06-17 10:18:40 UTC | #14

As this is going off topic now and the question has been answered, I am closing this thread.

-------------------------

weitjong | 2019-06-17 10:51:24 UTC | #17



-------------------------

weitjong | 2019-06-21 16:28:32 UTC | #18

I just close the thread and I have deleted all your other nonsense posts in the thread.

-------------------------

