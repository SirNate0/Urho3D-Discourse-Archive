rasteron | 2017-01-02 01:06:10 UTC | #1

I have tried this before with older versions and I don't see any issues, might worth checking it out again..

-------------------------

rasteron | 2017-01-02 01:06:11 UTC | #2

So far, yes it does look like a main concern there. Well, In my case I'm trying to move away with the VS compilation but one thing I like about in VS is its smaller file size with the output.

-------------------------

thebluefish | 2017-01-02 01:06:11 UTC | #3

I'm genuinely confused. Is there some problem with OpenGL in Visual Studio? I've not had any issues myself with the latest master branch in VS2013.

-------------------------

friesencr | 2017-01-02 01:06:11 UTC | #4

I run opengl in visual studio everyday.  Run ./cmake_vs20XX.bat -DURHO3D_OPENGL=1 on build.  There are no problems here.

-------------------------

jamies | 2020-05-01 12:57:51 UTC | #5

A bit late to the party: Can I disable directx in cmake? Can I disable SDL too? Does urho require SDL for mouse/keyboard inputs?

-------------------------

Eugene | 2020-05-01 13:26:19 UTC | #6

[quote="jamies, post:5, topic:1221"]
Does urho require SDL for mouse/keyboard inputs?
[/quote]
Yes, it does.
All communication with platform, including input and window management, is done via SDL.
I guess Urho can tecnhically run in headless mode w/o SDL after adjustments in the code, but you will not get any graphics.

-------------------------

