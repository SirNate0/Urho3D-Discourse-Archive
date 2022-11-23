jeezs | 2019-06-27 10:04:25 UTC | #1

Hello, 
Is it possible to create 2D rounded shapes then animate the point's shape.
or if possible to morph a polygon into another.
Also does it support boolean operation on 2D shapes.
if not can Is possible to achieve this in 3D with 2D shapes.

Thanks.

-------------------------

weitjong | 2019-06-28 00:45:22 UTC | #2

I think you need other library instead of Urho, if you want to achieve your goal faster.

-------------------------

guk_alex | 2019-06-28 07:55:52 UTC | #3

To create rounded shapes I guess you need some kind of Bézier curves, or a some kind of polygon with a lot of vertices to make it rounded (a lot of workaround could be used to achieve that).
And yes, you can morph a polygon into another with help of custom geometry / morph animations.
Can you describe what do you want to achieve, may be there is others method to do what you want?

-------------------------

jeezs | 2019-06-28 14:13:41 UTC | #4

Thanks for your replies.
My goal is to create an open source and cross platform 2D & 3D design app with Urho3D.
Dunno if it's possible

-------------------------

Leith | 2019-06-28 14:52:30 UTC | #5

Look into CSG - definitely possible on the 3D/ Bullet physics side, and I have done similar things under Box2D as well.

-------------------------

