gawag | 2017-01-02 01:03:24 UTC | #1

I made a simple mesh, with a diffuse texture and a normal texture, and exported it to Urho3D:

[img]http://vignette1.wikia.nocookie.net/urho3d/images/d/d8/Blender_urho3d-0.png/revision/latest?cb=20150213181337[/img]
[img]http://vignette2.wikia.nocookie.net/urho3d/images/d/dd/Blender_model_in_urho3d.jpg/revision/latest?cb=20150213182427[/img]

The model in Urho3D (1.32, OpenGL on Windows7) has no working normal map (as you can see) though the material looks fine:
[code]
<material>
	<technique name="Techniques/Diff.xml"/>
	<texture name="models/testmesh.png" unit="diffuse"/>
	<texture name="models/testmesh2.png" unit="normal"/>
	<parameter name="MatDiffColor" value="0.64 0.64 0.64 1"/>
	<parameter name="MatSpecColor" value="0.5 0.5 0.5 50"/>
</material>
[/code]
I also tried <technique name="Techniques/DiffNormal.xml"/> which made no difference.

The textures are both there.
Did I miss something or is a setting wrong or should this work?
Texture units are not described in the manual. Wrong techn

-------------------------

Mike | 2017-01-02 01:03:25 UTC | #2

Settings seem good, DiffNormal technique should be what you get at export.
As you don't use "Files overwrite", maybe your model file didn't update.
Did you check the log for potential clues?

-------------------------

gawag | 2017-01-02 01:03:25 UTC | #3

Ah wat...
Just exported again and this time moved textures and materials into the Textures and Materials subfolders. Had them in the Models folder before (though adapted all paths). That should have worked too (and had no error messages).
Now it's suddenly working! Wow great, and weird.
I also had the problem of Urho at first not finding this DiffNormal technique and thought the exporter used a wrong name. Now the material file worked without any change.

Is still remember programming a normal map shader for Ogre. That was so much more complicated.

-------------------------

gawag | 2017-01-02 01:03:30 UTC | #4

Found out that this issue was depending on the build mode. When build in debug mode everything worked. When building in release mode it couldn't find the techniques and other files as well.

At that time I used a custom CodeBlocks project where I had manually set up every library for linking and every include path. Now I'm using the CMake way and let it generate the CodeBlocks-Project. There everything is working in both versions and the water issue, that I mentioned here [post4794.html#p4794](http://discourse.urho3d.io/t/my-first-experience-and-problems-with-urho3d/838/10), is also working with that CMake build. Still weird though.

-------------------------

