KamiGrave | 2018-03-18 14:28:00 UTC | #1

I've just pulled the latest ~17 commits and rebuilt the Urho3D library, but now my application just boots into the Ninja Snowball demo and not into my game.

I had previously build my game with the scaffolding project. I was having issues with physics and thought I'd best update to make sure I had latest, and now I'm not entirely sure how to get my version of the Urho3DPlayer in my project to run. There appears to be no calls into my code at all.

Any help is appreciated.

-------------------------

KamiGrave | 2018-03-18 23:35:59 UTC | #2

False alarm.

It turns out Visual Studio messed up some include directories, so Urho3D wasn't to blame. Just some side effect from having compiled the library and having the original scaffolding Urho3DPlayer still around in the default location (I had moved it to tidy it up a bit but looks like I didn't delete the originals).

-------------------------

