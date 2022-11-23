Askhento | 2021-10-30 14:01:38 UTC | #1

Is it possible to use viewport as texture unit in material?

```
<material>
    <technique name="Techniques/myTechinque" quality="0" loddistance="0" />
    <texture unit="diffuse" name="viewport" />
</material>
```

-------------------------

throwawayerino | 2021-10-31 08:13:45 UTC | #2

I guess you could render viewport to a separate texture in the renderpath, and reference that texture in here.

-------------------------

Askhento | 2021-10-31 15:01:50 UTC | #3

Do you have an example ?

-------------------------

Eugene | 2021-10-31 18:45:17 UTC | #4

I believe we have found quite elegant solution for this if you _really_ want to reference Render Target texture in Material w/o any material-related code.

1) Create empty placeholder texture in resource folder
2) Now you can load it and keep it in ResourceCache with built-in tools
3) Use it in Materials, etc
4) Instead of creating new texture for Viewport, load this texture and call `SetSize` with `TEXTURE_RENDERTARGET` to make it render target.

This way you can have 100% dynamic resource natively accessible by components and other resources.

`AddManualResource` will work too, but you will have to synchronize access in order not to access resource before its creation.

However, you **must** have explicit render target creation for this to work.

-------------------------

Askhento | 2021-11-01 10:27:16 UTC | #5

I know that I can create Texture2d class like this :
```
myTexture  = Texture2D();
myTexture(int(size.x), int(size.y), GetRGBAFormat(), TEXTURE_RENDERTARGET);
myTexture.name = "myTexture";
cache.AddManualResource(myTexture);
```

This way I can use it like : 
```
<texture unit="diffuse" name="myTexture" />
```

So your method seems to be similar. But I am confused.
1) I need to add texture file with any data in it? For example "Textures/empty.png"?
2) Should I use GetResource() ?
3) How do I reference this texture in material?
4) Do I need to add commands (with CopyFrameBuffer)  to renderPath to fill it with viewport data?

-------------------------

Eugene | 2021-11-01 15:49:37 UTC | #6

Unfortunatelly, my solution cannot work neither for your main window viewport (but I think you don't need it, right?), nor for internal renderpath textures (like gbuffer textures in deferred render path).

However, I assume that you have some custom render target and non-main viewport (like in sample `10_RenderToTexture`). In this scenario, all you need to do is to use texture from Resource Cache instead of new texture in [this line](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/10_RenderToTexture/RenderToTexture.cpp#L183)

In this context, answers to your questions:

1) Yes, any texture file will do, just make sure it's valid and loads
2) Yes, you have to use `cache->GetResource`
3) Like any other texture on the disk: by name (e.g. “Textures/empty.png”, although you will want more specific name)
4) N/A, given my comments above. This trick works only for main output texture of render-to-texture viewport.

-------------------------

Askhento | 2021-11-04 14:33:20 UTC | #7

Ok, I confirm that this method is working,

-------------------------

