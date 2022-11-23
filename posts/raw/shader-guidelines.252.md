carlomaker | 2017-01-02 00:59:09 UTC | #1

Hi , 
Soon I will concentrate on shaders, so I would understand if there is any guideline, because I found it  a bit complex compared to what we saw in Ogre3D.
thanks

-------------------------

friesencr | 2017-01-02 00:59:09 UTC | #2

Are you caught up on the somewhat recent changes to shaders?  A ton of "complexity/verbosity" was removed by putting a more smarts c++ side.

-------------------------

cadaver | 2017-01-02 00:59:10 UTC | #3

I recommend to read the material & shader documentation pages first ([urho3d.github.io/documentation/a00022.html](http://urho3d.github.io/documentation/a00022.html)), study the simplest shaders first, like Unlit and Shadow, then come back here with questions, which can be used to improve the documentation for the future.

Indeed, like Chris said, in V1.31 onward shader authoring is simplified and improved compared to the past, due to not requiring to write "shader XML description files" any more. Now you basically have shader compilation defines coming either from the technique's or post process effect's pass definition, or from the engine itself. The engine's inbuilt defines take care of things like skinned or instanced geometry, or shadows / no shadows. Ogre's shaders are simpler on the surface in the sense that the engine only supplies you some ready-to-use uniforms like camera view/projection matrices, but handling eg. skinned/unskinned geometry is completely up to you.

Another thing that makes Urho3D's example materials and shaders complex is that they support all of forward, deferred and light pre-pass rendering. Due to not wanting to repeat some common code these are not put into separate files. In your own project you likely decide which lighting pipeline to use and need to write the materials / shaders only for that.

-------------------------

