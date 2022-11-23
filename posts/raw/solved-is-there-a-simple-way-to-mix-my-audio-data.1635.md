victorfence | 2017-01-02 01:09:08 UTC | #1

I'm trying to integrate video playing decoded by ffmpeg. I'v finished the task of display video by setting a texture data.

Then the task of audio:

At first, I found I can't open a SDL audio device, seems urho3d already opened one.

Then I realize I must mix my data in urho3d's audio.

I am feeling hard to do that. I noticed there's a SDL callback inside audio.cpp. I have no idea how to play with it.
Must I implement a custom SoudSource?

And I'm warry about the a/v syncing.

Is there some easier way? thanks for any hint.

-------------------------

friesencr | 2017-01-02 01:09:08 UTC | #2

Have you seen the sound synthesis demo? [github.com/urho3d/Urho3D/blob/m ... thesis.cpp](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/29_SoundSynthesis/SoundSynthesis.cpp)

-------------------------

victorfence | 2017-01-02 01:09:09 UTC | #3

[quote="friesencr"]Have you seen the sound synthesis demo? [github.com/urho3d/Urho3D/blob/m ... thesis.cpp](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/29_SoundSynthesis/SoundSynthesis.cpp)[/quote]

Hi Friesencr,

I's nice and sweet demo, I belive it's a rather easy idea, I am happy to found my task could be done.

-------------------------

