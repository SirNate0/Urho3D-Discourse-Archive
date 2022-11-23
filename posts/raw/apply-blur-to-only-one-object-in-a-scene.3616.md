stark7 | 2017-09-28 21:22:38 UTC | #1

Hello -

I am looking into applying effects to specific objects only, like blur and autofocus.

Can someone please tell me what is the simplest and/or most efficient way to blur only one Node + Model Component in a scene?

I was looking at the Outline.as example, only I can't run it locally for some reason - and that method seems may not take depth into account and I definitely want that a blurred object to be rendered behind a regular one.

-------------------------

Bananaft | 2017-09-28 21:36:11 UTC | #2

What renderPath are you are planning to use? You better to provide some more info or reference picture on what exactly you want to achieve.

-------------------------

stark7 | 2019-05-23 13:20:02 UTC | #3

Here is an example - (clearly not my game :) ) - basically I have a scene and I only want one of the enemies to be blurred like that. I did this one in gimp.
https://imgur.com/qbxL3ML

[edit, it too me longer than what is reasonable to figure out how to embed images]

![cq8irNx|690x431](upload://8fgZjJ6UmBIiXsHcPDEAXuuvVpI.jpg)

-------------------------

1vanK | 2017-09-29 02:00:17 UTC | #4

use masks https://github.com/1vanK/Urho3DMotionBlur

-------------------------

Bananaft | 2017-09-28 22:17:01 UTC | #5

I see two solutions:
1) You render the shape of blurred area into stencil buffer(or whole texture channel), then blur post effect shader will read it  to apply itself only on this area.

2) If the number of blurred areas is limited (one or few) and shape is always sphere, you can pass its position and radius as shader parameters, then do a spherical projection and manual depth compare in shader.

http://iquilezles.org/www/articles/sphereproj/sphereproj.htm

-------------------------

stark7 | 2017-09-29 02:11:19 UTC | #6

Would this work with a partially blurred object in view?

-------------------------

