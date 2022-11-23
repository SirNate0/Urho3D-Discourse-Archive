chenjie199234 | 2018-08-04 11:36:10 UTC | #1

i copy the code in the Water example,NO.23
but there is something strange in my object,like a white shadow~
how to fix it~
it will show when the angle between camera direction and horizontal plane is small.
this is the screen shoot
![123|690x375](upload://1g8z81NMg5GAeNRXfGu9ZUQMVYC.PNG) ![456|690x390](upload://fQNVRbjb3SClpTJjQ3G0c9V0qma.jpg)

-------------------------

JTippetts | 2018-08-04 13:29:28 UTC | #2

That's the reflection on the surface of the water. In the sample, reflectionCamera is a camera set up to take a picture of the scene from a different viewpoint, and render that shot to a texture. In the water shader, a Fresnel term is used to mix between the refracted background color (your rendered scene from the standard camera viewpoint) and the reflection color. The Fresnel effect means that the shallower your viewing angle becomes, the more the reflected image will dominate over the refracted image.

If you don't want reflections, you can modify the shader to only use the refracted color. This should get rid of the "shadow", but also means there will be no surface reflections.

-------------------------

chenjie199234 | 2018-08-04 14:21:04 UTC | #3

got it.I didnt copy all the code in the example.thx for the explain.

-------------------------

Bananaft | 2018-08-04 16:24:17 UTC | #4

Are you using orthographic camera? Some features may not work with it.

-------------------------

chenjie199234 | 2018-08-05 04:43:13 UTC | #5

yes im using orthograghic camera.what feature not work with it.
do u know how to modify the shader.i dont know how towrite shader.
can we add a technique named WaterWithoutReflect.xml

-------------------------

Bananaft | 2018-08-05 21:01:33 UTC | #6

[quote="chenjie199234, post:5, topic:4435"]
do u know how to modify the shader.i dont know how towrite shader.
[/quote]
look into water.glsl, it's pretty simple actually. You can replace reflectColor texture read with plain blue color and fresnel calculation with static number. Also disable all reflection related code from water example (which is almost all of it. :) )

Good luck!

-------------------------

