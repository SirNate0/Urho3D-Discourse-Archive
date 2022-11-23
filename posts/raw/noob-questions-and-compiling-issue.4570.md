primem0ver | 2018-09-27 00:01:55 UTC | #1

Hello.  I am new here.  I wanted to introduce myself, ask some basic questions, and get help with an issue.

I am "primem0ver".  My real name is Matthew.  I am working on a large prototyping project that makes use of 3d modeling.  The project currently uses the Irrlicht engine (http://irrlicht.sourceforge.net/) which in coding terms, is *almost* perfect for my purposes.  However, I want to expand the interface to allow use of OpenGL ES on tablets which is not currently supported by Irrlicht.  This was one of the first engines I found when doing a search on Google.  I wanted to make sure it will suit my needs so I have listed some requirements below.  I am also having a problem getting the project downloaded from your sight to compile so I describe that below as well.  Any insight and help would be greatly appreciated.  Thanks!

**Requirements:**

1. The ability to embed a 3d surface into a window, **specifically a Qt Widget** of any size.
2. The ability to develop a plugin for a web browser that will allow the interactive 3d surface to appear on a web page.
3. The ability to dynamically create a custom mesh using code that takes mesh shape parameters.
4. An ability to override the drawing cycle (chain) to allow for a custom type of lighting (directional lighting whose direction depends on an objects positional relationship to a point source (or another object))*.  
5. EDIT: Not required but would be very nice and helpful... I would prefer that the engine be able to import meshes of any commonly used format.  **Otherwise, it would need to be a common format that is easily convertible with other formats** (why I could not use Ogre3D).

*I have been told this can be done with shaders, but I have not been able to figure out how.

**Compiling Issue:**
I tried compiling the source "out of the box" on Visual Studio 2017 as described in the guide to get started.  I am getting a significant number of errors, including linking errors.  All of the compile errors are in one file: "chain_tree.c", specifically involving the type "ik_chain_t" which is undefined.

-------------------------

Sinoid | 2018-09-28 01:53:42 UTC | #3

1. Yes, you have to initialize the engine with your target window handle. In QT that means grabbing the handle from a plain QWidget to give to Urho3D. You cannot trivially do multiple viewports though.

    When I did that in the past I initialized multiple engine instances, which was nice since it kept stuff segregated, but had it's own share of weird issues.

2. Emscripten, see the online [web-samples](https://urho3d.github.io/samples/) for live demos

3. Yes, there's the `CustomGeometry` class for easily doing it, you can also build raw geometry and models at runtime if needed but that's ill-advised in the general case.

4. No, not as you describe it. Urho3D uses a multiple batching scheme (there are draw-batches, light-batches, and shadow-batches), this functionality is generally what you actually want and if you desire to touch it you really need to know what you're doing and why. It's not a newcomer project.

    Most likely you just want to tweak shaders or configure the scene such that it meets your criteria.

    You really need to explain what and why to get a real answer here.

5. This depends on if you mean at runtime or offline. There is an Assimp based importer that will cope with most everything except FBX beyond the 2013 SDK version. If you mean at runtime importing an FBX, MD5, or w/e file then the answer is "*not trivial enough to explain in 3 paragraphs*".

- Compiling issues: do you have error messages about `IK_REAL`? If so then CMake failed to generate the necessary file based on the configuration you gave it.
    - Which version of CMake did you use?
    - Did you run it from the GUI?
    - If you ran it from the commandline how did you run it?

> Geometry shader support, as far as I could search, is on the works.

Unless someone-else started something up, then nope. The completed code is available as a [source dump](https://github.com/JSandusky/Urho3D) but will not be getting a PR from me, like tools - shaders and lighting are a hot-button issue with me that I will never ever touch again, too much armchair gets involved - not touching those subjects with a ten-foot pole.

-------------------------

Virgo | 2018-09-28 04:08:41 UTC | #4

:rofl:to my knowledge, urho3d and qt both require to be main activity on android, which makes it impossible to use qt + urho3d on android at the same time?

-------------------------

Sinoid | 2018-09-28 04:21:26 UTC | #5

[quote="Virgo, post:4, topic:4570, full:true"]
to my knowledge, urho3d and qt both require to be main activity on android, which makes it impossible to use qt + urho3d on android at the same time?
[/quote]

That's because of SDL, that's trivially fixable in localized forks. SDL on android is giant heap of garbage. 

Particularly if you want to hit GearVR. Which pays my bills.

SDL as a whole is a library written by a bunch of incompetents ... and I'll just stop there, because that's a hot-button I forgot about. SDL is shit.

-------------------------

primem0ver | 2018-09-29 10:45:58 UTC | #6

I appreciate all the replies

@Sinoid (and anyone else curious about some specifics)

3.  Why ill-advised?  This is absolutely necessary for what I am doing.  For example, I seriously doubt that an ISEA grid is available for spheres; something I will eventually need to incorporate.  What kinds of shapes are already available?  I noticed spheres and cubes.  I need to be able to call up the generation of various shapes dynamically.  This is the primary reason for needing this feature.

4.  This is mainly to simulate a source of light that is larger than other objects in the same scene.  A simple example would be a sun and its planets.  Point source lighting doesn't light up an entire hemisphere and directional lighting is the same for all objects in the scene.  I need a directional light whose direction is different for each object in the scene (relative to the light source).

5.  I was implying at runtime,  I haven't been following all the available formats but I suppose I mean the most common ones like DirectX, Blender, Nif, Maya, and 3ds Max. 
 
I am using CMake 3.10.2.  I checked some options the first time, though I probably shouldn't have.  I am going to try it without changing the defaults and see what happens.

-------------------------

primem0ver | 2018-09-29 08:13:06 UTC | #7

Ok.  Yeah... it was my guess-checking that caused the compiling problem.  The default build worked fine.  I suppose I will need to learn about the additional options if and when I need them.

-------------------------

primem0ver | 2018-09-29 11:36:56 UTC | #8

Is Mac OS (OSX) fully supported?  As much as I dislike Apple, going without MacOS support is not an option for me because some of the consumer base for what I am building are loyal Apple folks; so if OSX isn't fully supported, I can't use it.

-------------------------

primem0ver | 2018-09-29 11:57:50 UTC | #9

Another potentially big "roadblock" to using this engine:

I noticed that Angelscript and Lua both seem to be packaged with this engine.  Scripting will be feature of the software I am building.  However, ALL objects in my software, including anything within the graphics engine MUST be tightly controlled.  Scripts cannot have access to any object in the graphics engine without express permission from my built in object manager.  Scripts themselves are managed objects which are assigned both a permission key and a permission level.  Anything without the correct key and/or with a permission level lower than the required permission level for an object must not be given access to that object.  Is this going to be a problem with the built in scripting?

EDIT: As an FYI, the tightly controlled permissions are not applicable in the context of a web page because the features which make the control necessary are not available through the web plugin.

-------------------------

Sinoid | 2018-10-05 02:54:56 UTC | #10

[quote="primem0ver, post:6, topic:4570"]
Why ill-advised? This is absolutely necessary for what I am doing. For example, I seriously doubt that an ISEA grid is available for spheres; something I will eventually need to incorporate. What kinds of shapes are already available? I noticed spheres and cubes. I need to be able to call up the generation of various shapes dynamically. This is the primary reason for needing this feature.
[/quote]

The *ill-advised* is because I'm referring to direct-manipulation of the underlying raw types (Geometry, VertexBuffer, IndexBuffer, etc) - for most custom shape needs the `CustomGeometry` component provides a cleaner and generally more friendly interface than working with raw vertex/index-data for creating basic procedural/etc geometry.

For most cases it's enough.

[quote="primem0ver, post:6, topic:4570"]
This is mainly to simulate a source of light that is larger than other objects in the same scene. A simple example would be a sun and its planets. Point source lighting doesn’t light up an entire hemisphere and directional lighting is the same for all objects in the scene. I need a directional light whose direction is different for each object in the scene (relative to the light source).
[/quote]

You might have to tweak the rendering core, you might not. It depends on how constant your source of light is. If I understand your issues correctly then I think you can just virtualize your lights such that you have a logical light source and instantiate the required light-sources as needed, not terribly unlike methods involving virtual-point-lights (VPLs).

-------------------------

