devrich | 2017-01-02 01:03:29 UTC | #1

How do we play ogg, ogv, mp4,or avi like a movie on a plane?

I don't recall reading anything about that and I would like to consider this approach for cutscenes for one of my game ideas :slight_smile:

-------------------------

cadaver | 2017-01-02 01:03:29 UTC | #2

By integrating your video player library of choice, feeding the video data to a Texture2D that's being shown, and the audio to your custom SoundStream. (See the sound synthesis C++ example.) Urho itself does not contain a ready integration as of now.

-------------------------

devrich | 2017-01-02 01:03:29 UTC | #3

ohh.. ok then umm.... where to read up on how to integrate a third-party library into Urho3D?

-------------------------

sabotage3d | 2017-01-02 01:03:29 UTC | #4

You don't have to integrate third-party libs into Urho3D. You can just link them against your main app.

-------------------------

cadaver | 2017-01-02 01:03:29 UTC | #5

There is no tutorial to this as such, basically you would examine the build system (CMakeLists.txt files) on how the existing libraries are integrated. There are some instructions related to eg. script bindings in the "contribution checklist" [urho3d.github.io/documentation/H ... klist.html](http://urho3d.github.io/documentation/HEAD/_contribution_checklist.html) but that's more about the things you have to remember for getting a pull request accepted.

That said, if you're only interested in getting video playback running in your own program and not contributing it to be a part of Urho3D, then the question is reduced to "how to integrate a third-party library in your own program." In any case this will involve C++ interaction with the video player library and Urho3D, so a pure script application would be out of the question.

-------------------------

devrich | 2017-01-02 01:03:29 UTC | #6

Thanks guys; my main target platform is Android 4.2 ~ 5.x including Android tv tablets and phones.

C++11 would end up being the way for me to go then when I find a good library...  I guess I'm just a little worried about getting the linked library(ies) to work on Android as this would be my first time linking a library to Urho3D....

Can you give me any hints/tips on making sure that the libraries I link would work on Android devices when I get them ready to test?

[i]Edit:[/i] I just don't want to screw up Urho3D

-------------------------

jmiller | 2017-01-02 01:03:29 UTC | #7

I would take a good look at [url=http://ffmpeg.org/]FFMpeg[/url]
it is probably the most complete decoder, cross-platform, LGPL, few dependencies, popular enough that there is a lot of information out there.
like [stackoverflow.com/questions/9605 ... ndroid-ndk](http://stackoverflow.com/questions/9605757/using-ffmpeg-with-android-ndk)

I don't think you can screw up Urho unless you really get naughty  :slight_smile:

-------------------------

friesencr | 2017-01-02 01:03:29 UTC | #8

IMHO TheoraPlay is a good candidate for Urho3D:

[icculus.org/theoraplay/](http://icculus.org/theoraplay/)

Pending mobile compatibility.

-------------------------

devrich | 2017-01-02 01:03:30 UTC | #9

many thanks guys, i'm going to look into both of those and see what I can achieve :slight_smile:

Also I don't 'plan' to do anything to screw up Urho3D but you never know when messing around with various libraries :wink:

-------------------------

