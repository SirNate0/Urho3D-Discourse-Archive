cftvgybhu549 | 2017-01-02 01:15:25 UTC | #1

when running app on iphone, the resolution is so low which is always 480*320. But it's normal on ipad.
when I debug, I found that the function "Graphic::SetMode" is invalid in iphone.
after run this function, the width and height I get is always 480 * 320.
I don't know how to solve this problem, help me plz~

-------------------------

rasteron | 2017-01-02 01:15:28 UTC | #2

Hello there, I think this issue is related to your problem:

[github.com/urho3d/Urho3D/issues ... -222401779](https://github.com/urho3d/Urho3D/issues/1371#issuecomment-222401779)

as suggested there, try setting the engine's [b]HighDPI[/b] parameter, or simply use [b]-hd[/b] if you're using Urho3D Player.

-------------------------

cftvgybhu549 | 2017-01-02 01:15:44 UTC | #3

[quote="rasteron"]Hello there, I think this issue is related to your problem:

[github.com/urho3d/Urho3D/issues ... -222401779](https://github.com/urho3d/Urho3D/issues/1371#issuecomment-222401779)

as suggested there, try setting the engine's [b]HighDPI[/b] parameter, or simply use [b]-hd[/b] if you're using Urho3D Player.[/quote]


thx man

-------------------------

