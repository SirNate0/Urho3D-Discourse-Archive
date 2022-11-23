TheComet | 2017-03-19 18:00:12 UTC | #1

How would you create a spline that does the following?

After I saw this topic: http://discourse.urho3d.io/t/splines-in-urho/2928/1 I wanted to try and create a spline which describes a foot setting down and lifting off of the ground. Basically, something that looks like this:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/03c03e99ae2d587b8effa8b019120c5c50dd1a3b.png" width="640" height="400">

I determined these key times by looking at a walk animation in the editor. I figure I could spline between Vector2's, so I created the spline like this:
```cpp
Spline sp;
sp.AddKnot(Variant(Vector2(0.29, 0.0))); // foot down
sp.AddKnot(Variant(Vector2(0.39, 1.0))); // foot on ground
sp.AddKnot(Variant(Vector2(0.81, 1.0))); // foot still on ground
sp.AddKnot(Variant(Vector2(0.91, 0.0))); // foot lift
```

Then I use this code to calculate the weight:

```cpp
float norm = animState_.time / animState_.length;
float weight = sp.GetPoint(norm).GetVector2().y;
```

When I look at the `weight` value I'm getting something that looks like a sine wave and not the expected figure. What am I doing wrong?

-------------------------

Lumak | 2017-03-19 18:21:54 UTC | #2

I think by definition, you will not get a square wave function out of spline. You may just have to clamp the y output:
> float weight = Clamp(sp.GetPoint(norm).GetVector2().y, 0.0f, 1.0f);

-------------------------

slapin | 2017-03-19 20:22:52 UTC | #3

Yep, you can't get square wave form. You can use more knots to get closer though,
and use Clamp as proposed above.

-------------------------

TheComet | 2017-03-20 05:53:04 UTC | #4

Alright, got it to work with clamp by adding more points. Thanks!

-------------------------

johnnycable | 2017-03-20 09:47:09 UTC | #5

Have you tried this? http://cubic-bezier.com/

-------------------------

