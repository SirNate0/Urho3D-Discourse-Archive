TheComet | 2017-01-02 01:14:32 UTC | #1

I noticed that pressing the "e" key on Windows causes all UI elements to disappear in the editor. This is extremely annoying when trying to enter a node name that contains "e". This doesn't happen on Linux.

I can't find any reason why this would happen (after searching for KEY_E in the editor code). Any ideas?

-------------------------

cadaver | 2017-01-02 01:14:33 UTC | #2

Can't reproduce right now. Pressing the movement keys while not in any UI element focus should dim the UI, but not hide. Make sure you're actually running the editor scripts of the newest master. In theory defining a resource directory with outdated editor scripts included could cause those to be used instead. In case of doubt, try deleting the editor config from

C:\Users\<username>\AppData\Roaming\urho3d\Editor

-------------------------

TheComet | 2017-01-02 01:14:34 UTC | #3

I'm on commit hash [url=https://github.com/urho3d/Urho3D/commit/ca263bef55b6bcb18dd6c9e3f7291db27430e4e8]ca263be[/url], the issue still occurs.

I can reproduce the issue when doing a clean build on Windows 7 using msvc2010, and I can reproduce the issue if I do a cross compile on linux (i686-pc-mingw32), install urho to [b]/usr/urho3d[/b] and run [b]wine /usr/urho3d/bin/Urho3DPlayer.exe Scripts/Editor.as[/b]

Deleting Config.xml didn't have any effect.

-------------------------

cadaver | 2017-01-02 01:14:34 UTC | #4

The key F12 is supposed to hide the editor. You can see the code for it in EditorUI.as. Maybe it's some weird key code / mapping thing?

-------------------------

