weitjong | 2017-01-02 01:05:34 UTC | #1

It looks like you have well planned out everything. Does the ATF/WinForms run on Mono on Linux?

-------------------------

esak | 2017-01-02 01:05:34 UTC | #2

This sounds really interesting!
Unfortunately I don't have the time just now, maybe in the autumn...

Can you describe, from a high-level point, what the objective of the tool is? What areas will it cover?
Is it supposed to be a world/scene/level editor?

-------------------------

cadaver | 2017-01-02 01:05:34 UTC | #3

Looks like this could become the heavy-duty Urho3D Studio / Editor replacing the "example-grade" existing editor. Nice!

-------------------------

sabotage3d | 2017-01-02 01:05:35 UTC | #4

This looks like it won't be compatible with Linux and OSX or I am missing something ?

-------------------------

thebluefish | 2017-01-02 01:05:35 UTC | #5

Sinoid, I've actually be writing my own ATF-based editor based off of [url=https://github.com/SonyWWS/LevelEditor]the ATF Level Editor[/url] this past week and a half. Your project certainly looks interesting, and I think it would be sad if we worked on two independent projects with the same end-goal. Send me a PM with the details, and I'll get it ready for source control.

[quote="sabotage3d"]This looks like it won't be compatible with Linux and OSX or I am missing something ?[/quote]

Winforms hasn't seen much love with Mono, and ATF can't be compiled with Mono. Unity, which is based off winforms, has serious performance issues under Mono for this very reason. Unfortunately that's how these kind of tools work out.

-------------------------

Hevedy | 2017-01-02 01:06:02 UTC | #6

And why no use QT ? probably will be better for somethings.

-------------------------

rasteron | 2017-01-02 01:06:07 UTC | #7

As [b]Hevedy[/b] pointed out, Qt is really the way to go with crossplatform in mind but I'm still having hopes in using and expanding the built-in ui or editor.

-------------------------

weitjong | 2017-01-02 01:06:07 UTC | #8

Aster2013 has attempted to create one with Qt last year in local repository (not available publicly yet). I am not sure whether Aster2013  still pursuing it or not. Lasse and I received a copy of the early work. It was a skeleton framework for the Editor but the Scene Hierarchy and Attribute Inspector appear to be functional from a screenshot. If someone wants to go down this route, it may worth the trouble to write to Aster2013 to find out what is the latest status of this work.

I am not a fans of Qt, but considering the other proposed solutions mentioned in this thread, Qt looks like a lesser of two evils to me (on Linux). Personally I also hope the built-in UI could be improved further to support the Editor and of course our own apps can benefit from the improvement too.

-------------------------

christianclavet | 2017-01-02 01:06:21 UTC | #9

Hi, I'm still new to URHO3D, but the current provided GUI is almost good for creating applications. One of the thing I know it miss is a TAB component, and I still need to check out how I can create a variant of the input text GUI that support multi-lines. I was impressed by the current demos and the current editor abilities. (Drag&Drop is really nice!)

The current skin is a little pixely, but that can be changed by improving the skin (first thing I want to check out is creating an alternative skin)

What is missing to the current URHO3D GUI to be used in applications? (Editors).

I don't understand why putting efforts to make a editor restricted to the Windows environment because you use MFC. Qt or any other GUI addon that is multi platform would be preferable. Personally I would like to know what is missing from the current GUI system. 

I really like the idea that you have a EDITOR with URHO3D has this can be used to check for problems with features to the engine. If a feature is not working correctly, you can use the editor to test it and replicate the problem. When I was using Irrlicht, the devs were alway asking that you write them an application showing the problem. Creating something in the EDITOR that replicate a problem is MUCH EASIER and FASTER.

-------------------------

HeadClot | 2017-01-02 01:06:27 UTC | #10

So just thought I would chime in about QT as it is under the LGPL license and Urho3D is under the MIT license. 

They are not compatible with each other last I checked.

-------------------------

rasteron | 2017-01-02 01:06:28 UTC | #11

[quote="HeadClot"]So just thought I would chime in about QT as it is under the LGPL license and Urho3D is under the MIT license. 

They are not compatible with each other last I checked.[/quote]


It is somehow compatible by dynamic linking and an old issue, you should check here from Qt thread:

[forum.qt.io/topic/19358/qt-and- ... -license/3](https://forum.qt.io/topic/19358/qt-and-the-mit-license/3)

Then again, as the old saying goes "IANAL" so it will depend on your usage. :wink:

-------------------------

weitjong | 2017-01-02 01:06:28 UTC | #12

I am not a lawyer too and I am not trying to defend on Qt either as I have said before I am not a fan of it. But, I don't think using Qt framework for developing an "open source" Editor would be an issue. It is only when you want to make it a "closed source" tool then you need to call up your lawyer.

-------------------------

rasteron | 2017-01-02 01:06:28 UTC | #13

[quote="weitjong"]I am not a lawyer too and I am not trying to defend on Qt either as I have said before I am not a fan of it. But, I don't think using Qt framework for developing an "open source" Editor would be an issue. It is only when you want to make it a "closed source" tool then you need to call up your lawyer.[/quote]

Exactly, as long as you don't modify the actual Qt library and closed source your changes to it, everything is good to go. A clearer discussion here: 

[forum.qt.io/topic/6598/constrai ... l-of-qt/11](https://forum.qt.io/topic/6598/constrains-of-lgpl-of-qt/11)

...[quote]The commercial license allowes you to modify Qt without telling anybody about the changes, write closed code without giving anybody any source of anything :slight_smile:[/quote]

and more LGPL info [url=http://stackoverflow.com/questions/8534964/requirements-when-distributing-a-commercial-application-which-is-dynamically-lin/8540690#8540690]here.[/url]

-------------------------

cadaver | 2017-01-02 01:06:28 UTC | #14

License-wise Qt is not a problem, for example the realXtend project I've participated at work combines Qt, Ogre, and an Apache-licensed custom code base, and the whole combination is usable in commercial projects too, as long as Qt remains dynamically linked.

My suggestion would only be that Urho3D library itself remain Qt-agnostic, so it's always the editor application's build scripts that search for & link Qt. Conditional header-level compatibility (e.g. a URHO3D_QT_INTEROP define for things like allowing to construct Qt math objects from Urho objects and vice versa) would be OK though.

-------------------------

sabotage3d | 2017-01-02 01:06:28 UTC | #15

I am for Qt as well most of the VFX softwares are using it Maya, 3ds-max, Houdini, Nuke and so on. It looks like it is best suited for Editor. I am also using Qt Creator for C++ coding and I love it as it works on every possible platform.

-------------------------

Hevedy | 2017-01-02 01:08:02 UTC | #16

@Sinoid this is easier than the Urho3D editor ? Because to make the same scene in Unreal Engine 4 and Urho3D in UE4 I need about 4min and in Urho3D I need 8min that things of add nodes and subnodes are killing my time.

-------------------------

