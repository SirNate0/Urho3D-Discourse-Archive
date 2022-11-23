Hevedy | 2017-01-02 00:58:13 UTC | #1

I'm testing with "normal scene" sponza with a 3 directional lights over deferred shader and this is the result...

[img]https://dl.dropboxusercontent.com/u/28070491/URho3D/Light.png[/img]

Using the technique of id tech 4 for outdoors: [katsbits.com/tutorials/idtec ... niques.php](http://www.katsbits.com/tutorials/idtech/dynamic-outdoor-lighting-techniques.php)

This need a fix the shaders (looks like garage door in the faces with small light), and other walls looks dark.

-------------------------

Hevedy | 2017-01-02 00:58:13 UTC | #2

Test 2 with:
4 Ambient lights in 4 angles
1 Sun
1 Zone

No idea about how give more power to the light (only with color ??)
[img]https://dl.dropboxusercontent.com/u/28070491/URho3D/Demo2.png[/img]


Best but no good.

-------------------------

cadaver | 2017-01-02 00:58:14 UTC | #3

I have done testing with the zones and zone ambient gradient feature and there are some weird things going on which will need reviewing, and fixing. These are possibly due to over-optimizing the code that finds a zone for each visible drawable.

But, on the subject of lights, there is possibly a mismatch of expectations. Urho3D implements basic dynamic Blinn-Phong lights of 3 types (dir, spot, point) and never promised that they would look especially good. From the "Limitations" section of the About page at urho3d.github.io:

[quote]
Though Urho3D already contains several useful features and implements a framework for 3D games and applications, it is not yet a complete out-of-the-box game creation toolkit. Some things you can expect having to work on ...
- HLSL and GLSL shaders: the provided shaders give only basic examples of what is possible
[/quote]

This is a simple reality based on the current active development team size and available time. If there are actual bugs in the lighting implementation - sure, those should be fixed. Otherwise comparisons to commercial engines (even if 10 years old) are not very helpful and may actually give off an attitude that inspires others to ignore you.

I can say that I like the negative lights idea you posted at github; it would be a rather easy way to increase versatility of the lighting, at least in the deferred modes.

-------------------------

Hevedy | 2017-01-02 00:58:14 UTC | #4

[quote="cadaver"]I have done testing with the zones and zone ambient gradient feature and there are some weird things going on which will need reviewing, and fixing. These are possibly due to over-optimizing the code that finds a zone for each visible drawable.

But, on the subject of lights, there is possibly a mismatch of expectations. Urho3D implements basic dynamic Blinn-Phong lights of 3 types (dir, spot, point) and never promised that they would look especially good. From the "Limitations" section of the About page at urho3d.github.io:

[quote]
Though Urho3D already contains several useful features and implements a framework for 3D games and applications, it is not yet a complete out-of-the-box game creation toolkit. Some things you can expect having to work on ...
- HLSL and GLSL shaders: the provided shaders give only basic examples of what is possible
[/quote]

This is a simple reality based on the current active development team size and available time. If there are actual bugs in the lighting implementation - sure, those should be fixed. Otherwise comparisons to commercial engines (even if 10 years old) are not very helpful and may actually give off an attitude that inspires others to ignore you.

I can say that I like the negative lights idea you posted at github; it would be a rather easy way to increase versatility of the lighting, at least in the deferred modes.[/quote]

Ok. But i compared that because the technique is the same, in other engines you don't see the lights of the sun only vars to change. (Not for offend. I don't like offend to the community or people in general)
You some times compare with Unity (Please do not look in unity to create anything, not is a good example)

I need check the shaders, the light and the model, i going to upload some models to add to Urho (for examples or to test materials) and others to preview (lights, shaders...) like this.

[quote="cadaver"]
Otherwise comparisons to commercial engines (even if 10 years old) are not very helpful and may actually give off an attitude that inspires others to ignore you.[/quote]
Fixed, sorry.

-------------------------

cadaver | 2017-01-02 00:58:14 UTC | #5

Unity often is a good comparison, not because of graphics quality or specific implementations, but because it's very explicit that everything that's in the scene (well, almost) is in a gameobject or a component, there are no hidden processes.

Just as well I could compare to Ogre, which organizes things differently but it's the same idea. Everything is in the geometry entites, the materials and the inbuilt dynamic lights which are roughly same as Urho.

It's true that neither are state-of-the-art rendering engines.

-------------------------

Hevedy | 2017-01-02 00:58:14 UTC | #6

[quote="cadaver"]Unity often is a good comparison, not because of graphics quality or specific implementations, but because it's very explicit that everything that's in the scene (well, almost) is in a gameobject or a component, there are no hidden processes.

Just as well I could compare to Ogre, which organizes things differently but it's the same idea. Everything is in the geometry entites, the materials and the inbuilt dynamic lights which are roughly same as Urho.

It's true that neither are state-of-the-art rendering engines.[/quote]

Ogre is good but need implement the physics, audio, network... you, the docs of Ogre are outdated (in general), but have a some docs and codes about realtime god rays, gi...
I think Urho need a minimum of edit in the scene terrain (mesh and paint), and good idea is add some like bsp/gsc/or like in cryengine (no idea what is) because all people say the bsp give bad performance.

-------------------------

Hevedy | 2017-01-02 00:58:14 UTC | #7

Wow i testing with this scene with 1 zone and 6 point light with shadows and my 9800GTX+ going to explode by the shadows
[img]https://dl.dropboxusercontent.com/u/28070491/URho3D/Room.png[/img]

-------------------------

