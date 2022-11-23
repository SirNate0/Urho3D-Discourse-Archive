umen | 2017-01-02 00:58:48 UTC | #1

Hello all
i successfully compiled the engine without script support both windows and mac , in mac I'm targeting to iOS 
and the example do run on iOS fine , but the problem is the examples are for desktop so no event handling or any thing like that ,
my question is , is there any example that are adjusted for mobile ( iOS) ? ( finger touch and multi touch and orientation)
Thanks Allot!

-------------------------

Mike | 2017-01-02 00:58:49 UTC | #2

Currently only example 18_CharacterDemo and NinjaSnowWar are "designed" for mobiles.
02_HelloGUI and 14_SoundEffects are mobile-friendly either.
There's a discussion here: [url]https://github.com/urho3d/Urho3D/issues/264[/url]

-------------------------

weitjong | 2017-01-02 00:58:49 UTC | #3

I have just submitted the first working concept of the screen joystick to address this issue. Currently I have only refactored NinjaSnowWar to take advantage of this new feature. It will be rolled out subsequently to the rest of the sample apps.

-------------------------

Mike | 2017-01-02 00:58:49 UTC | #4

Awesome work, thanks weitjong  :stuck_out_tongue:

-------------------------

umen | 2017-01-02 00:58:49 UTC | #5

How do i deploy the NinjaSnowWar ( that is using the player ) to iOS ?
thanks for the fast help

-------------------------

weitjong | 2017-01-02 00:58:49 UTC | #6

Not sure I have understood your question correctly. Like you said, NinjaSnowWar is implemented using Urho3D's AngelScript API. It is played with Urho3DPlayer. So, you need to deploy Urho3DPlayer.app. By default, on mobile platforms Urho3DPlayer will play NinjaSnowWar. That could be changed by replacing the content of "CommandLine.txt" before building and deploying.

As all the sample apps including Urho3DPlayer.app are not signed. You cannot deploy them to actual iOS device. As they are, you can only deploy them to iPhoneSimulator.

HTH.

-------------------------

umen | 2017-01-02 00:58:50 UTC | #7

Thanks for the fast replay , i did deploy to iOS device i have signed as developer

-------------------------

