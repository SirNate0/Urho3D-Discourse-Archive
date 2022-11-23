att | 2017-01-02 01:03:06 UTC | #1

:smiley:  
This week I released my new game Two Cars 3D, for now just android version. You can download and play it from following google play link.
[url]https://play.google.com/store/apps/details?id=com.kin9.att.twocars3d[/url]

updated:
iOS version added,
[url]https://itunes.apple.com/us/app/two-cars-3d/id963990088?mt=8[/url]

-------------------------

sabotage3d | 2017-01-02 01:03:19 UTC | #2

Nice ! How did you do the UI  ? Is it Urho's or something else ?

-------------------------

att | 2017-01-02 01:03:20 UTC | #3

The UI is just Urho's Sprite responding to touch events. :smiley:

-------------------------

thebluefish | 2017-01-02 01:03:20 UTC | #4

Is there a particular reason for the permissions?

[quote]
Version 1.0.1 can access:

Photos / Media / Files
- modify or delete the contents of your USB storage
- read the contents of your USB storage

Other
- full network access
- view network connections
[/quote]

Many people these days are wary about permissions that seem off, especially from a developer they don't know or haven't heard much about. Since my phone has corporate information, I personally can't install such apps.

Either way, good job getting something together and released! I bet it was certainly a learning experience :p

-------------------------

att | 2017-01-02 01:03:20 UTC | #5

[quote="thebluefish"]Is there a particular reason for the permissions?

[quote]
Version 1.0.1 can access:

Photos / Media / Files
- modify or delete the contents of your USB storage
- read the contents of your USB storage

Other
- full network access
- view network connections
[/quote]

Many people these days are wary about permissions that seem off, especially from a developer they don't know or haven't heard much about. Since my phone has corporate information, I personally can't install such apps.

Either way, good job getting something together and released! I bet it was certainly a learning experience :p[/quote]

There is no any particular reason for the permissions, just because google play services and admob need it. :stuck_out_tongue:

-------------------------

Stinkfist | 2017-01-02 01:03:20 UTC | #6

Nice! Tried, but this game seems to be way too difficult for my slow brain. Or the game is super hard. Or both.  :laughing: Any change to get a difficulty level (that alters the speed of cars) setting?

-------------------------

umen | 2017-01-02 01:03:33 UTC | #7

In which market did you release it in iOS ? 
i can't find it when i search "Two Cars 3D"

Can you tell us how was the development ? 
im looking into developing using this engine for iOS but there was ( don't know now ) some problems

-------------------------

att | 2017-01-02 01:03:35 UTC | #8

[quote="umen"]In which market did you release it in iOS ? 
i can't find it when i search "Two Cars 3D"

Can you tell us how was the development ? 
im looking into developing using this engine for iOS but there was ( don't know now ) some problems[/quote]

You can download android version from 
[url]https://play.google.com/store/apps/details?id=com.kin9.att.twocars3d[/url]

or iOS version form
[url]https://itunes.apple.com/us/app/two-cars-3d/id963990088?mt=8[/url]

If you have any problems when developing using this engine, I will do my best to help you.  :smiley: 
And [url]http://urho3d.prophpbb.com/forum8.html[/url] is a good place for help.

-------------------------

umen | 2017-01-02 01:03:36 UTC | #9

I send you email

-------------------------

sabotage3d | 2017-01-02 01:03:37 UTC | #10

Can you give us some tips for the IOS integration ? 
Do you have a sample on how to integrate Urho3D with the Game center ?
What did you use for the adds ? 
Did you run into problems with IOS 8 ?

-------------------------

att | 2017-01-02 01:03:37 UTC | #11

[quote="sabotage3d"]Can you give us some tips for the IOS integration ? 
Do you have a sample on how to integrate Urho3D with the Game center ?
What did you use for the adds ? 
Did you run into problems with IOS 8 ?[/quote]

"Do you have a sample on how to integrate Urho3D with the Game center?"
You can reference [url]http://novacreo.tumblr.com/post/65666085911/cocos2d-x-ios-gamecenter[/url]
unfortunately, the comments is chinese. :slight_smile: 

[url]What did you use for the adds ?[/url]
You can reference google integration instruction on [url]https://developers.google.com/mobile-ads-sdk/docs/admob/ios/quick-start[/url]

"Did you run into problems with IOS 8 ?"
There is no special problem with iOS 8.

-------------------------

sabotage3d | 2017-01-02 01:03:38 UTC | #12

Thanks a lot :slight_smile: 

Is there a way to use Game Center without objective-C  or Cocos-2d, just Urho3d and C++ ?

-------------------------

att | 2017-01-02 01:03:39 UTC | #13

[quote="sabotage3d"]Thanks a lot :slight_smile: 

Is there a way to use Game Center without objective-C  or Cocos-2d, just Urho3d and C++ ?[/quote]

You need't cocos2d support, just use the sample code to communicate with game center.  :smiley:

-------------------------

