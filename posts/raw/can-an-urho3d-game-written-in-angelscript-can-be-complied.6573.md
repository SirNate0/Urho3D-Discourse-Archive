Thysta | 2020-11-28 21:44:52 UTC | #1

Can an Urho3D game written in AngelScript can be complied into an EXE or only if I use C++? I mean, do I have to use a .BAT and Urho3DPlayer.Exe and have my source code open or there is a way to do it?

Or, can a whole game be written in an AngelScript and just have the CPP load it?

Thank you!

-------------------------

Pencheff | 2020-11-27 02:15:19 UTC | #2

You can modify the Urho3DPlayer.exe source code to load an AngelScript file of your choice, without having to call a .bat file.

-------------------------

evolgames | 2020-11-27 02:51:03 UTC | #3

I dont believe you understood what he was asking. I'm also curious on this but I'm not sure.

-------------------------

Eugene | 2020-11-27 08:20:26 UTC | #5

You can do it in the same way as for any other resource.
There are 3rdparty tools to compile binary resources as part of exe. Urho is not integrated with such tools, but nothing stops you from doing so.

So, you can alter Urho in a way that let you “compile” AS. You cannot do it with Urho as is.

-------------------------

Modanung | 2020-11-27 23:23:53 UTC | #6

[quote="Thysta, post:1, topic:6573"]
[...] can a whole game be written in an AngelScript and just have the CPP load it?
[/quote]

Yes.

Also, welcome! :confetti_ball:

Also also, the *developer* category is for engine development. Please ask your questions in _support_.

-------------------------

Thysta | 2020-11-28 17:30:38 UTC | #7

Thank you for everyone for the answers it helped at least in that I don't miss something completely. Sorry for using the wrong forum I just saw "Developers" and thought it is the place sorry guys.

-------------------------

Modanung | 2020-11-28 17:45:24 UTC | #8

No worries, you're not the first to be confused. You *can* still move a thread after posting, btw.

-------------------------

