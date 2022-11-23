cin | 2017-01-02 00:57:31 UTC | #1

I generated new textures for skybox. May be used in Urho3D examples?

[img]http://i.imgur.com/TDe7eVH.jpg[/img]

[b][url=http://ogre3d.su/brightday.rar]Download[/url][/b]

-------------------------

cadaver | 2017-01-02 00:57:31 UTC | #2

These are quite useful, as you can make the fog color almost white and the terrain will fade nicely.

Can you make a double resolution (1024x1024) version? I'd say it's worth it to bump the quality at the same time.

-------------------------

cin | 2017-01-02 00:57:31 UTC | #3

Done. Now fog is white. 1024x1024 px.
Link in first post.
[img]http://i.imgur.com/YFQhB3R.jpg[/img]

-------------------------

cadaver | 2017-01-02 00:57:31 UTC | #4

Has been pushed. I adjusted red & green curves slightly downward to make it more blue and reduce brightness a bit to match the scenes.

-------------------------

globus | 2017-01-02 00:57:42 UTC | #5

Idea for next step:
Realization multilayer skybox with animating texture layer.
For designer this give best tool for making variations of skybox.

It like in Torque3D:
"Three separate cloud layers will be rendering and moving across the sky slowly"

Its clouds not volumetric or generated in real-time (could be best for performance)

[b]Without layers[/b]
[img]http://docs.garagegames.com/torque-3d/official/content/documentation/World%20Editor/Tutorials/images/SkyNoClouds.jpg[/img]
[b]With layers[/b]
[img]http://docs.garagegames.com/torque-3d/official/content/documentation/World%20Editor/Tutorials/images/CloudFastSpeed.jpg[/img]
Torque 3D skybox tutorial
[url]http://docs.garagegames.com/torque-3d/official/content/documentation/World%20Editor/Tutorials/CreatingSky.html[/url]

-------------------------

globus | 2017-01-02 00:57:42 UTC | #6

I know about bad optimization and hard code in Torque 3D.
I like ingame tools in this engine.
Also skybox, 3D water waves, and seamless indoor-autdoor scene managment based on zones and portals.

-------------------------

