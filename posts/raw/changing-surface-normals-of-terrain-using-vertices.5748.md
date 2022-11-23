spenland | 2019-12-04 15:06:23 UTC | #1

Is there a way to tap into a terrains vertices and re-calculate the triangle/quad normal in my own way? Basically, I am wanting to make the terrain appear flat shaded instead of smooth - in order to give it a low-poly look.

I've looked at the terrain [reference page](https://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_terrain.html) and see SetSmoothing() but that doesn't appear to do anything...and I'm not sure it would do what I want anyway... I do see a vertex count but I need the Vector3 of each vertex, how they are ordered (in an array or something), and then the ability to change the vertex normal of each vertex...I'm new to Urho3D and also just 3D in general...

Is this possible, is there an easier way...any help would be awesome.

-------------------------

JTippetts | 2019-12-06 12:23:07 UTC | #2

I believe that smooth normal calculation is baked into the Terrain, see https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Terrain.cpp#L1342 for where the normal is calculated. The good news for you, though, is that it also calculates tangents which means you can use a tangent-space normalmap (with a small modification to the terrain shader; just use the vTexCoord varying parameter to sample a normalmap texture, and use that for the normal) and bake your flat-shading normals into the normal map. I personally recommend using a normal map for terrain shading anyway, due to the more consistent lightning at distance.

The SetSmoothing method doesn't have anything to do with normals, but instead has to do with smoothing out the stair-steps that can be created by using an 8-bit heightmap image, due to the low vertical resolution. If you use 16-bit heightmaps (encoding a fractional part in the green channel and the 'standard' elevation in red) then you don't need SetSmoothing, since that gives you plenty of vertical resolution.

-------------------------

spenland | 2019-12-06 18:53:18 UTC | #3

Is there a way to change the code in the GetRawNormal function without editing Urho source?

I tried making something like this:

    class FlatShadedTerrain : public Terrain
    {
        public:
        private:
            virtual Vector3 GetRawNormal(int x, int z) const;
    }

and overriding the function with my own code but it seems there are private functions and variables that I cannot access from inside that override function...I'm new to c++ and not sure how to alter the code without changing it in Urho source which I'd like to not do.

-------------------------

SirNate0 | 2019-12-06 19:24:49 UTC | #4

Terrain is just a component, you can always copy the code and create you're own FlatShadedTerrain, and then register and use that component instead. I've taken that approach when I needed a bit of extra functionality in the particle emitter. Just copy the Terrain.cpp and .h files and then replace every occurrence of Terrain with FlatShadedTerrain in those files and change the normal function as you want then.

-------------------------

spenland | 2019-12-06 21:14:36 UTC | #5

I copied the h and cpp files but have a few errors that I can't figure out.

![flat_terrain|690x413](upload://eNqbGR8BvfuCyJFzB3bM6KSxcws.png)

-------------------------

SirNate0 | 2019-12-06 22:19:48 UTC | #6

URHO3D_ATTRIBUTE_EX should be #defined in Serializable.h. Where there any errors about missing includes or the like, or perhaps do you also have an older copy of the library without that macro?

It mostly worked for me, though I didn't fully make it work (A FlatTerrainPatch would need to be created as well, not just a Terrain, but I just commented out the setOwner line that was breaking rather than actually fixing it). I also had to change the #include to use the copied file and not the original. None of those seem to be the error that you're getting. Could you perhaps copy the whole error log and/or upload the files that you used so I can see if they work for me (I'm not using Visual Studio, so that could also influence it).

Also, if you do go this route, I'm pretty sure you'll have to change how the vertices are defined as well, as you'll end up with 4 (6?) different normals at every point in the grid rather than just the one normal (and thus re-usable vertex) situation it is now. JTippets' solution to bake a flat shaded normal map (and then probably use nearest filtering) may be a much better approach.

-------------------------

Modanung | 2019-12-07 00:26:30 UTC | #7

Another option might be using a shader with a [`flat`](https://www.khronos.org/opengl/wiki/Type_Qualifier_(GLSL)#Interpolation_qualifiers) (GLSL) or [`nointerpolation`](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-struct?redirectedfrom=MSDN#interpolation-modifiers-introduced-in-shader-model-4) (HLSL) specifier.
Although you might still want to calculate the normals differently, the vertices could then remain shared.

-------------------------

Modanung | 2019-12-07 00:59:24 UTC | #8

In the case of GLSL that would mean changing...

`varying vec3 vNormal;`

...to...

`flat varying vec3 vNormal;`

...in your project's LitSolid.glsl.

-------------------------

spenland | 2019-12-07 16:03:57 UTC | #9

I'm not sure I can bake the normal as I'm going to be generating a perlin noise image, use it for the heightmap, then make it flat shaded. Or at least that's my hopes...

I got everything made: the FlatTerrain and the FlatTerrainPatch files but I get a runtime error.

![error|567x500](upload://odrkqMq6NKGP1OvPxsu7DHg4nLQ.png) 

I'm a little lost on the error, not sure what is going on. The patchSize_ is null. I'd think just copying the files that I'd be able to recreate the same functionality...then from there start working on playing with calculations.

-------------------------

SirNate0 | 2019-12-07 17:44:52 UTC | #10

It's not the patchSize_ that's bull, it's the pointer `this`, that is, the FlatTerrain that had the function SetPatchSize called. Step back up the stack to the function that called SetPatchSize (and higher if needed) until you find where something has a nullptr for a FlatTerrain*

-------------------------

