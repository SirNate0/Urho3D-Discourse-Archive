Alex-Doc | 2017-07-12 18:37:53 UTC | #1

Hi everyone,
I was unsuccessfully trying to export an environment cube map with DOF and got frustrated,
so I made a Blender add-on to do that.

[You can find it here](https://github.com/Alex-doc/blenderExportSkybox)

I don't give instructions because the UI is pretty self-explanatory but if you have any doubt, feel free to ask.

I hope it will be useful to you too!

-------------------------

slapin | 2017-07-13 10:48:26 UTC | #2

Thank you for your great work!

Could you pleas provide screenshot of your scene setup? I never made skybox before
so I'm quite clueless there... :( I'm interested in sizes and what mesh types are used and overall layout...

-------------------------

Alex-Doc | 2017-07-13 12:25:38 UTC | #3

For this particular game, I'm just making a landscape in blender and [this is the setup](http://imgur.com/a/fI2aO).

My scene uses a couple of planes and the particle system to place the props on them.

For actual Skydome and using actual photographs, [you could try this](https://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro/Build_a_skybox).
If you use the second link's tutorial, keep in mind that you can replace the "Render the environment map" step with my Add-On.

Basically, once you get a scene you like to see from location 0,0,0 you can call my Add-On to get a 360° view to use in a Skybox.

EDIT:
A good way to make some without using a skydome and photographs, could be to setup some nice clouds by using the Blender's cloud/smoke simulator.

-------------------------

