Hideman | 2018-11-23 14:13:38 UTC | #1

Hello Urho's community,

I just started to develop some thing with Urho but I have some issues with TextureCube.

I just want to bind one texture by side on Box model so I try this:

        Urho3D::Model *boxModel = cache->GetResource<Urho3D::Model>("Models/Box.mdl");
        
        Urho3D::TextureCube *myCube = new Urho3D::TextureCube(context_);
        Urho3D::Texture2D *leftSide = cache->GetResource<Urho3D::Texture2D>("textures/left_side.png");
        Urho3D::Texture2D *rightSide = cache->GetResource<Urho3D::Texture2D>("textures/right_side.png");
        ...

        myCube->SetData(Urho3D::CubeMapFace::FACE_POSITIVE_Z, leftSide->GetImage());
        myCube->SetData(Urho3D::CubeMapFace::FACE_NEGATIVE_Z, rightSide->GetImage());
        ...


        Urho3D::Material *cubeMat = new Urho3D::Material(context_);
        cubeMat->SetTechnique(0, cache->GetResource<Urho3D::Technique>("Techniques/Diff.xml"));
        cubeMat->SetTexture(Urho3D::TU_DIFFUSE, myCube);


        Urho3D::Node *boxNode_ = m_scene->CreateChild("Box");
        boxNode_->SetPosition(Urho3D::Vector3(17, 34, 17));
        boxNode_->SetScale(Urho3D::Vector3(1, 1, 1));

        Urho3D::StaticModel *boxObject = boxNode_->CreateComponent<Urho3D::StaticModel>();
        boxObject->SetModel(boxModel);
        boxObject->SetMaterial(cubeMat);

But I just obtain a black box (and no error has been logged), so what am I doing bad ?

-------------------------

Modanung | 2018-11-10 23:00:15 UTC | #2

I don't think `TU_DIFFUSE` takes cube maps, try using `TU_ENVIRONMENT` instead.

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

Hideman | 2018-11-11 13:10:15 UTC | #3

Thanks ;)

Nop does not work.

I try cache->GetResource<Urho3D::Technique>("Techniques/DiffSkybox.xml") it's render but as skybox so always in backend and ignore near ligth.

So I think it need a specific tech and also shadder

-------------------------

Modanung | 2018-11-11 18:44:59 UTC | #4

Ah yes, the technique for the material should be one ending in `EnvCube`.

-------------------------

Hideman | 2018-11-12 14:06:16 UTC | #5

Envcube display me a pure reflecting geometry with no aspect of my texture.

-------------------------

Sinoid | 2018-11-12 17:57:20 UTC | #6

You can't, you can render to a specific face because targets have a *first-slice*, but shader resources do not.

Please explain what the end result you're trying to get is.

Why is your texture in a cubemap to begin with? A cubemap with texture-filtering is the most expensive thing you can sample so there's nothing clever enough you could be doing to justify having a regular texture in one.

They're also distorted so if it's a genuine cubemap and you intend to reuse the *ground* or something it's going to be warped - if that's what you need to do than if your cubemap is in a DDS file you can load it as an `Image` and construct the 2d texture chain for a specific face from that as `Image` will have the data for all of the faces and their mip-chain.

-------------------------

Hideman | 2018-11-12 18:16:01 UTC | #7

I have a collection of 2D textures and I just want to display a cube with each side have a specified texture and the texture in side can be changed during the game and texture ca be also use in other objects so that's why I don't want to use a unique texture with 6 sides texture. I used TextureCube because an object have a material and it's material have just one texture. Maybe I don't use the best way and maybe I don't need to use TextureCube (but it work like a dictionary with each side is affected to a texture so I tried to use it).

-------------------------

Sinoid | 2018-11-12 18:24:39 UTC | #8

What you describe is what Texture2DArray is for. You still need to create a shader to accept the index and the texture-array. The included shaders don't use it.

```
<texturearray> <!-- Texture2DArray::Load doesn't actually process the root element -->
    <layer name="Textures/Dirt.dds" />
    <layer name="Textures/Grass.dds" />
    <layer name="Textures/Stone.dds" />
    <layer name="Textures/Snow.dds" />
    <layer name="Textures/Gravel.dds" />
    ... repeat ad infinitum ...
</texturearray>
```

They have to be the exact same format (RGB/RGBA/etc).

-------------------------

Hideman | 2018-11-12 18:30:54 UTC | #9

Have you a example of the shader I need?

-------------------------

Modanung | 2018-11-12 20:36:16 UTC | #10

In that case you may want to make a cube with 6 geometries/materials after all, one for each side. You could clone the material and then set a different texture.
You can reuse the material by simply passing its pointer to the other objects

-------------------------

Sinoid | 2018-11-12 21:07:27 UTC | #11

[quote="Hideman, post:9, topic:4667, full:true"]
Have you a example of the shader I need?
[/quote]

Ask in a few days, if you can't work that out on your own you're in over your head.

~~You just add a `#define`, the sampler for the array, and an additional material variable for the texture-index. Where the desired texture is sampled you wrap it in a `#ifdef` and do the appropriate array lookup.~~ Brain filtered out that you're just mapping cube faces.

You're not going to see any substantial performance increase without C++ side engine changes unless you're just going to index off of the instance id (which you can only do on static models, and it won't be stable) - as you'll need a unique material per index in the array, which will batch-out to being almost the same as separate textures.

Edit: wait what?! A cube? You can use UDIM and just modulo the array index.

-------------------------

Hideman | 2018-11-12 20:43:32 UTC | #12

Thanks for your help, I will try and come back later if needed.

-------------------------

Hideman | 2018-11-23 14:13:27 UTC | #13

We proceed in an other way because of some optimization needed we split cubes into 6 textures and apply greedy meshing algorithm to downsize number of vertices.

But many thanks for your explanations.

-------------------------

