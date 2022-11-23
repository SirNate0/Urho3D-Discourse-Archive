Sehlit | 2018-05-23 14:39:32 UTC | #1

Hello.

Is there any kind of official support for 3rd party game libraries like:
Ads (like AdMob and Mediation services)
IAPs (Google/Apple/Amazon/Facebook)
Social (Sharing/Posts on Facebook/Twitter)
Game Services (Scoreboards/Multiplayer/Achievements - Google/Apple/Steam)

If there is no support is it possible and easy to add these libraries in a Urho game?

Thank you

-------------------------

johnnycable | 2018-05-23 19:57:47 UTC | #2

No, all those services you have to integrate them yourself the usual way; by binding to the various systems...

-------------------------

Alan | 2018-06-15 01:59:54 UTC | #3

General question on this subject: Not a single for these 3rd party service middleware like [sdkbox](http://www.sdkbox.com/) or [enhance](https://enhance.co) work in Urho3D or just C++? How hard would it be to get something that works in Cocos2D-X working in Urho? Can't you call the Xamarin plugins for example?

-------------------------

