umen | 2017-01-02 01:14:07 UTC | #1

Hello all
i try to compile the hello world example using xcode 7.3 on ios 8.2 
every thing is compiled fine but on run time im getting exception 
im using real device not simulator . 
i had this problem befor  but never seamed to fixed it .
any body got over this ?
[img]http://i.imgur.com/a9xvErf.png[/img]

-------------------------

sabotage3d | 2017-01-02 01:14:07 UTC | #2

this looks like SDL issue. I would check for possible solutions in their mailing list.

-------------------------

umen | 2017-01-02 01:14:07 UTC | #3

On simulator with 9.3 iOS it is working 
What is the minimum ? For the engine?

-------------------------

umen | 2017-01-02 01:14:07 UTC | #4

The problem is that Urho3d doesn't support iOS 8 
i upgraded my iphone to 9.3 and all is working ( im testing all the examples now ) on device , iphone 5 works fast!

-------------------------

weitjong | 2017-01-02 01:14:07 UTC | #5

Have you set the "IPHONEOS_DEPLOYMENT_TARGET" build option? If not set explicitly, the build will target latest installed iOS SDK which may or may not be what you want.

-------------------------

umen | 2017-01-02 01:14:07 UTC | #6

Yes did every thing it's just don't work on iOS 8 
Never mind this as it has less then 5% market share

-------------------------

