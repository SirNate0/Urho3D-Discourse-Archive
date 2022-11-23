walker | 2017-01-02 01:10:39 UTC | #1

I'm working on an app (not a game) which shows both 3d and 2d vector contents. Basically it should support popular desktop and moblie platforms. 
I found Urho3d is the best open-source one available which has clean code structure and good cross-platform support. (Ogre3d's code is too complex. OSG's license is bad)
The special requirement is the app can be released as a control, so the users can use it like an android view or qt widget. 

After some study of Urho3d code, I found the window/input system is done by SDL. Changing SDL looks too complicated to me. I tried to removed all the SDL code(window/ogl context management) in the graphics and finally rendered an Urho sample in a QGLWidget. But the code is really ugly, and not easy to port to other platforms. So, is there a better way to do it?

Another question is is it possible to render multiple Urho view simultaneously? This can be useful when user creates multiple controls.

-------------------------

cadaver | 2017-01-02 01:10:39 UTC | #2

Welcome to the forums.

Like you have noticed you are working against Urho's own usecase, which is to run a game-like app in its own window, and which SDL allows to accomplish on all supported platforms. But if you go outside of that, and rip out SDL, I'm sorry to say you're on your own.

We support an "external window handle" usecase in which the Urho window is to be embedded e.g. in an editor application's native window, but this is still working within SDL. I don't think that can be expanded to mobiles ("run as a control") without modifications to SDL.

As of the current version multiple window rendering from within the same application isn't supported.

-------------------------

walker | 2017-01-02 01:10:39 UTC | #3

[quote="cadaver"]Welcome to the forums.

Like you have noticed you are working against Urho's own usecase, which is to run a game-like app in its own window, and which SDL allows to accomplish on all supported platforms. But if you go outside of that, and rip out SDL, I'm sorry to say you're on your own.

We support an "external window handle" usecase in which the Urho window is to be embedded e.g. in an editor application's native window, but this is still working within SDL. I don't think that can be expanded to mobiles ("run as a control") without modifications to SDL.

As of the current version multiple window rendering from within the same application isn't supported.[/quote]

Thanks for your reply :slight_smile:
I'll try to replace SDL first, then see if I can write new backends for SDL.
Since there're only several files using SDL(graphics/input/audio/file), the change work should be acceptable.

-------------------------

gawag | 2017-01-02 01:10:41 UTC | #4

Would it be possible to let Urho render to textures and display these textures in different widgets? Render to texture seems to be possible, the texture data has to be only accessible. I could be copied by CPU or maybe displayed in different OpenGL contexts?
Qt's QImage with ARGB32 (pixel directly in one continuous "array") could be used or one of the Qt OpenGL possibilities to display OpenGL textures. (Qt is also available on Android but I haven't used that, but the same thing may work with typical Android applications)

-------------------------

