setzer22 | 2017-01-02 01:00:10 UTC | #1

Quoting from the Documentation:

[quote]Material shader parameters can be floats or vectors up to 4 components, or matrices.[/quote]

I think this limits what can be done with shaders. For example one might like to pass a long array of floats representing a set of data that the shader might want to randomly sample. Of course this can be achieved with textures manually checking texels, but it feels rather inaccurate.

AFAIK this is possible with OpenGL (I don't know about DirectX). Could urho3d support this? It doesn't look like the engine needs a lot of refactoring for such a feature and it would surely allow interesting shader behaviour.

For now I'll go into using textures myself, but this feels like a limitation compared to raw OpenGL so I think it's a nice feature to add! I'd work on this if I had the knowledge but sadly this is way over me, so I'll leave it as a request.

Thank you!

-------------------------

vivienneanthony | 2017-01-02 01:00:10 UTC | #2

[quote="setzer22"]Quoting from the Documentation:

[quote]Material shader parameters can be floats or vectors up to 4 components, or matrices.[/quote]

I think this limits what can be done with shaders. For example one might like to pass a long array of floats representing a set of data that the shader might want to randomly sample. Of course this can be achieved with textures manually checking texels, but it feels rather inaccurate.

AFAIK this is possible with OpenGL (I don't know about DirectX). Could urho3d support this? It doesn't look like the engine needs a lot of refactoring for such a feature and it would surely allow interesting shader behaviour.

For now I'll go into using textures myself, but this feels like a limitation compared to raw OpenGL so I think it's a nice feature to add! I'd work on this if I had the knowledge but sadly this is way over me, so I'll leave it as a request.

Thank you![/quote]

Something that could be utilized for procedural terrain ?

-------------------------

cadaver | 2017-01-02 01:00:10 UTC | #3

Generally, using an engine with a multi-API abstraction is always going to be less flexible than coding directly to the rendering API.

For the case of custom (float) arrays, they would need to be stored inside the material, and serialized/deserialized. This would mean adding a new datatype (float array) to Variant, so that the data could be efficiently accessed when loading the array uniform to OpenGL.

However, consider that uploading large amounts of uniform data is going to hurt performance (if you need it for a lot of different objects / materials) and the uniform space isn't limitless either, so for large amounts of data accessed by a pixel shader textures are likely a better option.

-------------------------

setzer22 | 2017-01-02 01:00:10 UTC | #4

[quote="vivienneanthony"]Something that could be utilized for procedural terrain ?[/quote]

Possibly, that could be a thing, yes. I'm working on a shader that projects a grid over any kind of surface myself and I found textures to be like hack-ish for that purpose, in the sense that a texture is not meant to store the kind of custom data that I'm using, and it tends to get screwed easily with image editors when you're treating the binary data as anything else but colors. Even so, I'm using textures and they're working perfectly so I guess I don't need to worry as much. At least with Urho3D I can sample texels instead of normalized coordinates, so floating point precision is not going to be an issue anyway.

[quote="cadaver"]Generally, using an engine with a multi-API abstraction is always going to be less flexible than coding directly to the rendering API.

For the case of custom (float) arrays, they would need to be stored inside the material, and serialized/deserialized. This would mean adding a new datatype (float array) to Variant, so that the data could be efficiently accessed when loading the array uniform to OpenGL.[/quote]

This looks like some non-trivial work. And I guess it's not a priority. I might take a look at the source myself and if I can figure out how it works I'll do it.

[quote="cadaver"]However, consider that uploading large amounts of uniform data is going to hurt performance (if you need it for a lot of different objects / materials) and the uniform space isn't limitless either, so for large amounts of data accessed by a pixel shader textures are likely a better option.[/quote]

So you're telling me that the texture uploads only once to the GPU and all the materials use the same shared texture data by default? Is there any way I could trigger this behaviour otherwise? I'm interested. I know this is not the support forum, but I had to ask.

-------------------------

cadaver | 2017-01-02 01:00:10 UTC | #5

I'm not completely sure what you're asking, but yes, when several materials refer to the same texture (usually by referring with a filename, which is resolved and loaded through ResourceCache) the texture is only loaded once. Materials can't share shader parameters similarly, so each time when the shaders are changed, or the material being used is changed, the material uniforms are reuploaded. The Renderer / View classes try to limit overhead from this by sorting objects with same shader or same material to be rendered one after another.

-------------------------

boberfly | 2017-01-02 01:00:11 UTC | #6

Hi setzer22,

Reading from a texture as an array of data in the shader is the best way for GL2.x/ES2.0/DX9 compatibility, just bear in mind vertex texture fetches will limit your hardware support, particularly on mobile hardware. What you're after are Uniform Buffer Objects or preferably Texture Buffer Objects which would need GL3.x/ES3.x/DX10 at least. I've got a branch of Urho3D where I'm upgrading the GL level and I've made a GPUBuffer class which basically just wraps these extra BOs as GL can bind any kind of buffer to a type so it makes sense to keep it in one class, but I'm still testing it and needs some work to bind it to shaders.

[url]https://github.com/boberfly/Urho3D/tree/moderngl[/url]

I don't think I've pushed the GPUBuffer stuff yet, I've separated it from the existing VertexBuffer/IndexBuffer classes rather than making them use the one class so I don't need to change the whole codebase. :slight_smile:

-------------------------

friesencr | 2017-01-02 01:00:11 UTC | #7

[quote="boberfly"]Hi setzer22,

Reading from a texture as an array of data in the shader is the best way for GL2.x/ES2.0/DX9 compatibility, just bear in mind vertex texture fetches will limit your hardware support, particularly on mobile hardware. What you're after are Uniform Buffer Objects or preferably Texture Buffer Objects which would need GL3.x/ES3.x/DX10 at least. I've got a branch of Urho3D where I'm upgrading the GL level and I've made a GPUBuffer class which basically just wraps these extra BOs as GL can bind any kind of buffer to a type so it makes sense to keep it in one class, but I'm still testing it and needs some work to bind it to shaders.

[url]https://github.com/boberfly/Urho3D/tree/moderngl[/url]

I don't think I've pushed the GPUBuffer stuff yet, I've separated it from the existing VertexBuffer/IndexBuffer classes rather than making them use the one class so I don't need to change the whole codebase. :slight_smile:[/quote]

That implimentation looks really clean.  With only slight modifcations to urho it could be moved into Graphics/OpenGL3 and be distributed with Urho3D.  I wish I was more knowlegable.

-------------------------

boberfly | 2017-01-02 01:00:11 UTC | #8

Probably not friesencr as I completely break DX9 support in the process or at least I disregard it currently. :slight_smile: The debug callback stuff could be merged however, which makes debugging GL stuff a LOT easier, and it is only compiled in when doing a debug build.

Also abstracting enough for DX11 support down the track I'm not really looking into so closely, but OpenSubdiv's codebase kind of gives some good assumptions as to how the equivalent buffer objects are handled (as my current goal is to support OpenSubdiv in some form or another, which heavily uses Texture Buffer Objects and the Tessellation stages).

-------------------------

