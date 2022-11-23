sovereign313 | 2017-01-02 01:09:39 UTC | #1

so, our modeling guy is using blender and using some kind of method where he doesn't use textures at all (apparently, it's all 'materials' and shaders).  AssetImporter (and he has a Urho3d plugin for Blender that exports stuff) give a file like this:

[code]
<material>
        <technique name="Techniques/NoTexture.xml"/>
        <parameter name="MatDiffColor" value="0.64 0.64 0.64 1"/>
        <parameter name="MatSpecColor" value="0.5 0.5 0.5 50"/>
</material>
[/code]

Apparently, the MatDiffColor and MatSpecColor are supposed to be all that is required for this model to look like it does in Blender, but I'm thinking not.  Is it possible to load the model without a texture, using only shaders and 'materials', and have it look like it does in Blender?

-------------------------

TheComet | 2017-01-02 01:09:39 UTC | #2

[quote="sovereign313"]Is it possible to load the model without a texture, using only shaders and 'materials', and have it look like it does in Blender?[/quote]

It depends. Are you sure he's definitely not using a texture? "Materials" in blender can use textures as part of their material. Ask him if he's 100% certain he's not loading an external image.

If that is not the case then yes, it is possible to make it look like in blender without textures. From the sound of it, he's probably using vertex colours? I don't know enough about Urho3D yet to tell you how to enable those, but I can tell you from other experience that it requires a custom shader that reads the vertex colour property and applies it in the fragment shader.

It's possible Urho3D already ships with a shader with this capability. Hopefully someone else can confirm or deny this.

-------------------------

sovereign313 | 2017-01-02 01:09:41 UTC | #3

Thanks!

-------------------------

Dave82 | 2017-01-02 01:09:42 UTC | #4

By default materials does not use vertex colors. To use vertex colors your need to define VERTEXCOLOR in vertex and pixel shaders (for LitSolid), or by using techniques that already have these (techniques that have VCol in their names).But if you want some basic diffuse color , then you don't need vertex colors at all.

 [quote]Is it possible to load the model without a texture, using only shaders and 'materials', and have it look like it does in Blender?[/quote]
It depends.The material you provided is a simple colored mesh with some specular color.

Can you show us some examples how it looks in blender and in urho to make a comparison ?

-------------------------

