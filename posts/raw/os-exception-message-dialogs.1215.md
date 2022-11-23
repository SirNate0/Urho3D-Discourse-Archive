rasteron | 2017-01-02 01:06:07 UTC | #1

Hi,

So I was wondering if a feature already exist with the latest build in handling OS specific exception messages. Take for example a Checksum Error Scene where in Android it just automatically exits without any clue on what just happened. It would be nice to have a way to handle these type of messages so that users are aware of some fatal or exit errors and put out some custom messages or suggestions. ie. "Game requires the latest update to run"

Perhaps maybe an option and something to using 'SDL_ShowSimpleMessageBox'??

Thanks.

-------------------------

thebluefish | 2017-01-02 01:06:09 UTC | #2

It shouldn't be difficult to add it to the Log system, though probably be better to put it in an Assert. This is something I need, so I'll look into it.

-------------------------

rasteron | 2017-01-02 01:06:09 UTC | #3

Hey bluefish. Yes, looks like it and would be cool to have as an option. BTW, I already discussed this with Lasse here:

[github.com/urho3d/Urho3D/issues/795](https://github.com/urho3d/Urho3D/issues/795)

..for reference. Looking forward to your progress, thanks.

-------------------------

thebluefish | 2017-01-02 01:06:10 UTC | #4

Well that's beyond me then. I tested it in Windows and was going to test in OS X and Linux, but I haven't compiled Urho3D for Android before. Hopefully Lasse will figure something out :wink:

-------------------------

rasteron | 2017-01-02 01:06:10 UTC | #5

no worries and thanks again. yeah I really think something like this needs to happen on cross-platform.  :slight_smile:

-------------------------

