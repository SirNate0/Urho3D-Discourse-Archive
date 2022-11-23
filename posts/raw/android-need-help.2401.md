enelex | 2017-01-02 01:15:13 UTC | #1

Hi !
I have proble, pliss help. I create game.
My scene is big single mesh hall of 1600 tris and 10 materials
No gui, no light (only ambient) and while I look at our room in frame my fps down from 47/47 to 20/47. But if I look at big mesh with 10 000 tris my fps max. What the problem ? Maby that I dont use material texture tile and scale UV ?

-------------------------

rasteron | 2017-01-02 01:15:27 UTC | #2

Hi there, maybe check first with a desktop build of your scene but technically 1.6k tris is relatively light for Urho3D and android build. That's around the size of a single low/mid poly character. :slight_smile:

What's your device spec btw?

-------------------------

enelex | 2017-01-02 01:15:41 UTC | #3

My device in android 4.2, 1.3gzh, 4 core, mali-400mp2 video card,1280x800 screen)

-------------------------

rasteron | 2017-01-02 01:15:41 UTC | #4

You should probably post your model or apk for testing, are you using the latest engine release?

-------------------------

