Lumak | 2017-08-05 23:43:17 UTC | #1

I'm sure this has been discussed, but what is the shadow settings to remove the lines shown in the image?  And shouldn't the default setting be set so that such thing is not shown?


[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/c027662709ed7fd3dee8e54e4fdda742e26ca03a.jpg[/img]

-------------------------

Lumak | 2017-08-05 22:31:35 UTC | #2

Nvm, solved. *twenty chars*

-------------------------

Alex-Doc | 2017-08-06 06:30:37 UTC | #3

Can you please tell how you solved?

-------------------------

Eugene | 2017-08-06 07:49:44 UTC | #4

Tweaking biases and distances, probably... That's classic solution.

-------------------------

Bananaft | 2017-08-06 08:54:08 UTC | #5

[quote="Lumak, post:1, topic:3424"]
And shouldn’t the default setting be set so that such thing is not shown?
[/quote]

There is no basic setting that will cover all cases. This shadow acne artifact is very dependent on scene scale, geometry shape, light angle, and ways to fight it will vary too.

-------------------------

slapin | 2017-08-06 12:05:26 UTC | #6

Could you please elaborate? I'd like to know what handles I'm to tweak with stuff like this...

-------------------------

Eugene | 2017-08-06 12:31:04 UTC | #7

Huh, let me recall...

- Tweak _Depth Constant Bias_, _Depth Slope Bias_ and _Normal Offset_ parameters of `Light` component.

- Make shadow distance smaller or use more cascades;

- Increase depth buffer precision or resolution;

- Use back face culling for shadow pass or vice versa.

This usually helps to reduce artifacts (bias artifacts and peter panning)

-------------------------

Lumak | 2017-08-06 13:42:00 UTC | #8

https://discourse.urho3d.io/t/shadow-map-normal-offset-bias/1904

-------------------------

slapin | 2017-08-06 17:01:51 UTC | #9

Thanks so much for the help!

-------------------------

