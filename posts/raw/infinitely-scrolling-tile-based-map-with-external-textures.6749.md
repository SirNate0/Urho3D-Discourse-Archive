nickwebha | 2021-03-08 16:31:45 UTC | #1

Morning all!

I am building a tile-based infinitely scrolling map. I already have an idea on how I am going to do that bouncing around in my head. My question is as follows: How can dynamically generated run-time textures? In other words, when a new tile is created at the edge of the scene, how can I `node->SetMaterial()` with a resource grabbed from an HTTP or WebSocket request?

The HTTP and WebSocket servers are already built and functioning just fine (I use them in another project); I am not asking about those. Just how, in Urho3D, to dynamically get those tile images onto a node.

**Edit**
The tiles are 256px by 256px PNGs.

-------------------------

SirNate0 | 2021-03-08 17:18:29 UTC | #2

Without knowing what you have from an HTTP or WebSocket request it's kind of hard to know how to do it. If you have the png "file" stored in memory somewhere, you can construct a [MemoryBuffer](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_memory_buffer.html) from the data, which you can then create an [Image](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_image.html) that you will call `Load(memoryBuffer)` to do the actual PNG loading. You can then use [`Texture2D::SetData(img,withAlpha)`](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_texture2_d.html#ab49167ad05742f9610fd938c2f9f29ce) to set it as a texture. At the very least, I would suggest storing the texture in the ResourceCache as a manual resource.

I'm not certain, but I think it should also be possible to skip handling the Image yourself in the middle by just calling `Texture2D::Load(memoryBuffer)`.

-------------------------

nickwebha | 2021-03-08 17:34:21 UTC | #3

Awesome! Thanks. I will look into all of that. Looking forward to showing this thing off when I am finished.

We are literally talking about 2.345624806x10^13 tiles here. I can still use the ResourceCache for buffering but I will be adding and removing a lot of tiles in doing so. I will have to experiment with it.

-------------------------

nickwebha | 2021-03-08 17:37:57 UTC | #4

Wait a second, I just realized I made an assumption that might affect the answer: *This is a 3D game.* When I said "tile" what I should have said was "PNG image." I am looking to map these "tiles" onto block shapes to build out the world.

-------------------------

SirNate0 | 2021-03-08 18:13:23 UTC | #5

How many different images do you have? And are you asking how to get them onto models in the world, or do you have that figured out already?

-------------------------

nickwebha | 2021-03-08 19:07:58 UTC | #6

2.345624806x10^13 possible images (there will be a lot of dynamically loading and unloading of images). I am asking how to get them onto models from memory (IE not from disk). Right now I am using Box.mdl as a test model.

-------------------------

SirNate0 | 2021-03-08 22:42:47 UTC | #7

Then my first answer is basically correct. You will also need to create `Material`s for each of the different images, by using `void Material::SetTexture(TextureUnit unit, Texture* texture)`. You probably want `TU_DIFFUSE` as your unit. You then assign the box Static/AnimatedModel that material, and you should see your image.

-------------------------

glebedev | 2021-03-10 08:13:00 UTC | #8

If I get this right @nickwebha is going to stream in and stream out tiles so I would recommend to reuse material and texture objects when possible instead of creating new one every time.

-------------------------

nickwebha | 2021-03-12 14:29:07 UTC | #9

The documentation does not say what a `TextureUnit` is. For example, the signature of `SetTexture` is `SetTexture(TextureUnit unit, *texture)`. Also based on the [documentation](https://urho3d.github.io/documentation/1.7.1/class_urho3_d_1_1_texture.html) for `*texture` I do not see a way to get an image on there.

Is there a sample you can point me to doing something similar? I have looked but did not find what I was looking for.

Thanks.

-------------------------

JTippetts1 | 2021-03-12 14:37:23 UTC | #10

TextureUnit is an enum defined at https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/GraphicsDefs.h#L321 which just gives enum name handles to the various commonly-used texture types in the default shaders. The awkward part of this scheme is that if you are not using the default shaders, or you are using heavily-edited shaders, you still need to use a member of TextureUnit to designate which slot they're bound to, even if the name doesn't match up to your usage. So to bind to texture slot 0, you'd call SetTexture with TU_DIFFUSE, for example.

You don't pass an image to SetTexture, you pass a Texture. @SirNate0 already mentioned how to get the Image data into the Texture2D, by way of Texture2D::SetData which, when passed an Image, will construct the texture from the image. Your job will be to create the Image, pass it to a Texture2D by SetData, and bind that texture to the appropriate texture slot in the shader.

-------------------------

nickwebha | 2021-03-19 13:11:11 UTC | #11

I am a little stuck. I have gotten this far:
>     auto tile = GetSubsystem< Tile >();
>     std::string tileString = tile->GetTile( 0, 0, 0 );
>     const char* tileData = tileString.c_str();
>     MemoryBuffer tileMemoryBuffer( (void*)tileData, tileString.size() );
>     Image* tileImage = new Image( context_ );
>     tileImage->SetData( tileMemoryBuffer.GetData() );
>     Texture2D* tileTexture2D = new Texture2D( context_ );
>     tileTexture2D->SetData( tileImage );

Seems `tileData` contains a null terminating character and that might be throwing it off?

I have confirm `GetTile()` is returning the PNG image. Urho3D spits out the error
> ERROR: Zero or negative texture dimensions

to the console.

**Edit**
I have not gotten to the part where I stick it on the node yet.

-------------------------

SirNate0 | 2021-03-12 20:27:39 UTC | #12

You need to set the Image size, it can't determine it from the data. You may also need to set it on the texture, but I think using an Image for SetData takes care of that automatically (hopefully).

Also, I would avoid the conversation to string, as you will probably end up with issues if there are any 0 values in the data.

-------------------------

JSandusky | 2021-03-12 23:19:39 UTC | #13

If your memory contains an PNG file in its entirety and not just the pixels extracted from one then you need to load it from the memory buffer:

```
tileImage->Load(tileMemoryBuffer);
```

not `Image::SetData`. 

**Edit:** If the above is the case than you can just do this with your texture too, `tileTexture2D->Load(tileMemoryBuffer);`

-------------------------

nickwebha | 2021-03-15 20:59:57 UTC | #14

Is it just me or is there a dearth of documentation on materials and using materials?

Right now I have
>     auto tile = GetSubsystem< Tile >();
>     std::string tileString = tile->GetTile( 0, 0, 0 );
>     const char* tileData = tileString.c_str();
>     MemoryBuffer tileMemoryBuffer( (void*)tileData, tileString.size() );
>     Image* tileImage = new Image( context_ );
>     tileImage->SetSize( MAP_TILE_SIZE, MAP_TILE_SIZE, 3 );
>     tileImage->Load( tileMemoryBuffer );
>     Texture2D* tileTexture2D = new Texture2D( context_ );
>     tileTexture2D->SetData( tileImage );
> 
>     SharedPtr< Node > tileNode_;
>     tileNode_ = scene_->CreateChild( "tile" );
>     tileNode_->SetPosition( Vector3( 0, 3, 0 ) );
>     tileNode_->SetScale( Vector3( 1, 1, 1 ) );
>     StaticModel* tileObject = tileNode_->CreateComponent< StaticModel >();
>     tileObject->SetModel( cache->GetResource< Model >( "Models/Box.mdl" ) );
>     tileObject->SetMaterial( TU_DIFFUSE, tileTexture2D );
(Of course that last line throws an error because it expects an XML or JSON document instead of a 2D texture.)

It seems to me Urho3D demands a file be loaded from disk. I can create all the `MemoryBuffer`s I like but it is always going to ask for a material? I read all your guys responses (thanks again!) and I do not see how the code ends. How do I create a material on the fly at runtime?

@SirNate0
I could not find a way around using the C-style string so I used the constructor that lets you specify size instead. I think that should fix that issue (if I was even seeing that).

@JSandusky
Thanks for the heads up. When I get this working I will shorten the code.

**Edit**
Re-reading your replies again I feel like I am overlooking something here. What am I glossing over?

-------------------------

JTippetts1 | 2021-03-15 22:03:37 UTC | #15

SetMaterial requires just a pointer to a material. TU_DIFFUSE is a texture unit specifier used for binding a texture to a specific slot inside a material. You could either manually create a material using new, and manually set up the techniques and passes, or just load an xml material definition, then manually bind your texture to the slot using Material::SetTexture(TU_DIFFUSE, tileTexture2d). But yes, a model is always going to need a Material, since a material specifies the techniques to use and shaders to use to render.

-------------------------

nickwebha | 2021-03-19 13:15:47 UTC | #16

This is not right, either:
>     const char* tileData = tileString.c_str();
>     Urho3D::MemoryBuffer tileMemoryBuffer( (void*)tileData, tileString.size() );
>     Urho3D::Image* tileImage = new Urho3D::Image( context_ );
>     tileImage->SetSize( MAP_TILE_SIZE, MAP_TILE_SIZE, 3 );
>     tileImage->Load( tileMemoryBuffer );
>     Urho3D::Texture2D* tileTexture2D = new Urho3D::Texture2D( context_ );
>     tileTexture2D->SetData( tileImage );
> 
>     Urho3D::SharedPtr< Urho3D::Node > tileNode_;
>     tileNode_ = scene_->CreateChild( "tile" );
>     tileNode_->SetPosition( Urho3D::Vector3( 0, 3, 0 ) );
>     tileNode_->SetScale( Urho3D::Vector3( 2, 1, 2 ) );
>     Urho3D::StaticModel* tileObject = tileNode_->CreateComponent< Urho3D::StaticModel >();
>     Urho3D::Material* tileMaterial = new Urho3D::Material( context_ );
>     tileObject->SetModel( cache->GetResource< Urho3D::Model >( "Models/Box.mdl" ) );
>     tileMaterial->SetTexture( Urho3D::TU_DIFFUSE, tileTexture2D );
>     tileObject->SetMaterial( tileMaterial );

No errors from the compiler so there is that.

**Edit**
I checked the return values and they all came back as `1`. Where as before it was complaining about an unrecognised image format when I was accidently loading the wrong thing. So I know that the error catcher works.

-------------------------

JTippetts1 | 2021-03-19 13:19:56 UTC | #17

Well, it's not going to work just creating a blank material. If you read the [documentation](https://urho3d.github.io/documentation/HEAD/_materials.html) for Materials, you can see that the XML format provides a lot of different tags for passes, techniques, cull settings, etc... If you elect to not define your material via XML, then you need to duplicate those necessary setups in code. For example, if you don't provide a technique, it will fall-back to a default which is a NoTexture technique, meaning no textures will be applied. You can see what the Material defaults look like [here](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Material.cpp#L1246). You need to define your material so that it renders your object exactly as you need it, including technique which is pretty important. The easiest way to do it is to define the material XML, load it from the resource cache and assign it to the object. Then you can bind your texture to the material texture slot it needs to go. But if you really can't/won't do that for some reason, you can manually create a Technique that does what you need it to do.

-------------------------

nickwebha | 2021-03-19 13:23:16 UTC | #18

I think I understand something now I did not before. It also sounds like I can use a single XML file for all 2.345624806x10^13 tiles, too.

Thank you. Hopefully I will not be back. :slight_smile:

-------------------------

JTippetts1 | 2021-03-19 13:42:06 UTC | #19

As an aside, doing something like `Urho3D::Material* tileMaterial = new Urho3D::Material( context_ );` is rather a bad practice, since it could potentially leak. Instead, you should explicitly assign it to a SharedPtr<Material> during the allocation. Of course, this means you need to be mindful about keeping it alive for as long as is needed, since inside Batch (which is used by StaticModel) the Material pointers are stored as raw pointers, meaning if your SharedPtr dies from going out of scope, those raw pointers now point to dead memory. Some parts of Urho store SharedPtr internally, but some don't. In the case of Materials, the usual use case is that ResourceCache manages its lifetime, so if you bypass ResourceCache and allocate Material directly, you need to be mindful of keeping it alive for as long as needed and freeing it when no longer needed.

-------------------------

nickwebha | 2021-03-19 14:11:50 UTC | #20

I am experimenting with creating a single Materials XML file that will be used with all tiles and then supplying the image via `std::string.c_str()` instead of using `<texture />`. I am trying to do things within the framework (defining my material via XML, for example) but mixing that with the `MemoryBuffer` is tricky (at least to someone like me who is still learning).

Normally I pick apart the Samples-- which are a great resource-- but there is not one that does this. For example, how do I set
`tileObject->SetMaterial( cache->GetResource< Urho3D::Material >( "Materials/Tile.xml" ) );`
(without `<texture />` in it) and
`tileObject->SetMaterial( tileMaterial );`
at the same time to set everything via XML except the image itself? The obvious answer is you do not but I do not know of any alternatives. `SetMaterial` is how you set a material so mixing XML files with buffered data seems impossible from where I am sitting. I know you have explained a lot but the more I look the less is clicking for me without the code sample (not that I am asking you to provide one).

**Edit**
The `Material` in the XML file defines a lot of things besides the image itself. How do you get the image on there while still using the XML file? My brain is just two stones rubbing together it feels like.

-------------------------

JTippetts1 | 2021-03-19 14:13:11 UTC | #21

You only have to define a texture tag inside the material definition if you want a texture to be bound to a slot automatically when the resource is loaded. You can still call Material::SetTexture to explicitly bind a texture to a material, even one you created by loading an XML definition. Even if you *do* assign a texture inside the material XML, you can still override/overwrite it using SetTexture.

You setup your XML so that it specifies all the settings you need: cull mode, technique, passes, etc.... Load it via ResourceCache::GetResource, then with the returned pointer you call SetTexture to set your texture to the appropriate slot. Then you can assign that Material pointer to as many models as you need.

Since ResourceCache is now managing the lifetime of your Material, you can call GetResource with the name of your material at any time to obtain another pointer to the same material instance. Then you can call Material::SetTexture on this pointer to change the bound texture for all instances of that material, meaning that you can perform whatever Tile initialization and construction you need to do simply by calling tileObject->SetMaterial, then after the fact or during runtime you can change the bound texture by obtaining another pointer to the Material from the cache.

Note that in this pattern, since all Tiles share a material instance, changing the texture bound to one will change the texture bound to all. If you do have Tiles that need a different texture, you will have to create separate Material instances for each texture.

-------------------------

nickwebha | 2021-03-19 14:21:04 UTC | #22

> @JTippetts1
> Note that in this pattern, since all Tiles share a material instance, changing the texture bound to one will change the texture bound to all. If you do have Tiles that need a different texture, you will have to create separate Material instances for each texture.

Now that throws a wrench in the works. Since there are *sssooo* many tiles that is not practical for a number of reasons. Looks like I might have to define everything in code after all and just make sure I manage the memory properly. If I am understanding you. I do not think that was covered in the [documentation](https://urho3d.github.io/documentation/HEAD/_materials.html).

-------------------------

JTippetts1 | 2021-03-19 14:25:23 UTC | #23

Yeah, if you need different textures for tiles, you might need to manage them differently. ResourceCache keeps a map of Filename->Material pointer so that when you request a given XML material def, it will return the one already loaded.

However, you can still make use of the ResourceCache to load your initial material, if you don't want to construct a Material by hand. Material provides a method called Clone which will return a SharedPtr to a Material that is an exact copy of the material. You can load your XML def (without a bound texture) using ResourceCache, then for every unique instance of the material you need, call Clone and store the returned SharedPtr in your own cache of some sort, ie a vector or somesuch.

-------------------------

nickwebha | 2021-03-19 16:36:02 UTC | #24

I managed to figure it out!

For anyone looking in the future here is my code:
>     const char* tileData = tileString.c_str();
>     Urho3D::MemoryBuffer tileMemoryBuffer( (void*)tileData, tileString.size() );
>     Urho3D::Image* tileImage = new Urho3D::Image( context_ );
>     tileImage->SetSize( MAP_TILE_SIZE, MAP_TILE_SIZE, 3 );
>     tileImage->Load( tileMemoryBuffer );
>     Urho3D::Texture2D* tileTexture2D = new Urho3D::Texture2D( context_ );
>     tileTexture2D->SetData( tileImage );
> 
>     Urho3D::SharedPtr< Urho3D::Node > tileNode_;
>     tileNode_ = scene_->CreateChild( "tile" );
>     tileNode_->SetPosition( Urho3D::Vector3( 0, 3, 0 ) );
>     tileNode_->SetScale( Urho3D::Vector3( 2, 1, 2 ) );
>     Urho3D::StaticModel* tileObject = tileNode_->CreateComponent< Urho3D::StaticModel >();
>     Urho3D::Material* tileMaterial = cache->GetResource< Urho3D::Material >( "Materials/Tile.xml" );
>     tileObject->SetModel( cache->GetResource< Urho3D::Model >( "Models/Box.mdl" ) );
>     tileMaterial->SetTexture( Urho3D::TU_DIFFUSE, tileTexture2D );
>     tileObject->SetMaterial( tileMaterial );
The variable names should all be pretty self-explanatory. Note this is using "regular" pointers so that could be done better with smart pointers.

`Tile.xml` (based off `Stone.xml`):
>     <material>
>     	<technique name="Techniques/Diff.xml" quality="0" />
>     	<shader psdefines="PACKEDNORMAL" />
>     	<parameter name="MatSpecColor" value="0.3 0.3 0.3 16" />
>     </material>
Do not quote me on the XML part. Still learning about that. But it works.

Thank you, thank you, thank you guys for your help! Can not wait to stick this in the showcase when it is ready!

-------------------------

nickwebha | 2021-03-25 17:04:54 UTC | #25

I wrote a Bash script to generate an XML file for each tile. They (of course) all have different file paths (`Materials/Tile.xml`, `Materials/6/0/0.xml`, `Materials/6/0/1.xml`, etc).

`Tile.xml`, `0.xml`, `1.xml`, etc:
>     <material>
>         <technique name="Techniques/Diff.xml" quality="0" />
>     </material>

I create the grid of tiles, each using a different XML file (`Materials/6/0/0.xml`, `Materials/6/0/1.xml`, etc). I then create a test floating block using `Materials/Tile.xml` and programmatically assign it a texture. *They all change to that texture.*

Here is my "floating test block":
>     auto cache = GetSubsystem< Urho3D::ResourceCache >();
> 
>     const char* tileData = tileString.c_str();
>     Urho3D::MemoryBuffer tileMemoryBuffer( (void*)tileData, tileString.size() );
>     Urho3D::SharedPtr< Urho3D::Texture2D > tileTexture2D;
>     tileTexture2D = new Urho3D::Texture2D( context_ );
>     tileTexture2D->Load( tileMemoryBuffer );
> 
>     Urho3D::SharedPtr< Urho3D::Node > tileNode_;
>     Urho3D::SharedPtr< Urho3D::StaticModel > tileObject;
>     Urho3D::SharedPtr< Urho3D::Material > tileMaterial;
>     tileNode_ = scene_->CreateChild( "tile" );
>     tileNode_->SetPosition( Urho3D::Vector3( 0, 4, 0 ) );
>     tileNode_->SetRotation( Urho3D::Quaternion( 0, 90, 0 ) );
>     tileNode_->SetScale( Urho3D::Vector3( MAP_TILE_MULTIPLIER, 1, MAP_TILE_MULTIPLIER ) );
>     tileObject = tileNode_->CreateComponent< Urho3D::StaticModel >();
>     tileObject->SetModel( cache->GetResource< Urho3D::Model >( "Models/Box.mdl" ) );
>     tileMaterial = cache->GetResource< Urho3D::Material >( "Materials/6/0/0.xml" );
>     tileMaterial->SetTexture( Urho3D::TU_DIFFUSE, tileTexture2D );
>     tileObject->SetMaterial( tileMaterial );

It is my understanding that `ResourceCache` caches based on file hashes/file paths. Does it instead cache on something else and that is why they are all changing, not just the "floating test block"?

-------------------------

SirNate0 | 2021-03-25 15:08:25 UTC | #26

Did you actually assign the textures to the tiles? If you use a technique that expects a texture but don't supply one you can send up with it reusing the texture from random other objects (it depends on the render order I'm pretty sure).

-------------------------

nickwebha | 2021-03-25 17:02:20 UTC | #27

That was it. Now that I think about it that makes sense.

Regenerated the XML to include an image and it works in tandem with the programmatic one. I will give it a dummy/loading image and stream the tile images in from the web.

Thank you.

**Fun Fact**
If I stream in an image I need to rotate it by 90° on the Y axis. If the image comes from disk no rotation required.

-------------------------

nickwebha | 2021-03-26 13:54:31 UTC | #28

*Man, I wish there was a wiki or something. It would help a lot with the lack of documentation.*

For anyone interested I got individual materials from the ResourceCache without the repeating problem (sorry to make you read through the entire thread but I am not re-typing all of that):
>     auto cache = GetSubsystem< Urho3D::ResourceCache >();
> 
>     Urho3D::SharedPtr< Urho3D::Technique > tileTechnique;
>     tileTechnique = cache->GetResource< Urho3D::Technique >( "Techniques/Diff.xml" )->Clone();
> 
>     const char* tileData = tileString.c_str();
>     Urho3D::MemoryBuffer tileMemoryBuffer( (void*)tileData, tileString.size() );
>     Urho3D::SharedPtr< Urho3D::Texture2D > tileTexture2D;
>     tileTexture2D = new Urho3D::Texture2D( context_ );
>     tileTexture2D->Load( tileMemoryBuffer );
> 
>     Urho3D::SharedPtr< Urho3D::Node > tileNode_;
>     Urho3D::SharedPtr< Urho3D::StaticModel > tileObject;
>     Urho3D::SharedPtr< Urho3D::Material > tileMaterial;
>     tileNode_ = scene_->CreateChild( "tile" );
>     tileNode_->SetPosition( Urho3D::Vector3( 0, 4, 0 ) );
>     tileNode_->SetRotation( Urho3D::Quaternion( 0, 90, 0 ) );
>     tileNode_->SetScale( Urho3D::Vector3( MAP_TILE_MULTIPLIER, 1, MAP_TILE_MULTIPLIER ) );
>     tileObject = tileNode_->CreateComponent< Urho3D::StaticModel >();
>     tileObject->SetModel( cache->GetResource< Urho3D::Model >( "Models/Box.mdl" ) );
>     tileMaterial = cache->GetResource< Urho3D::Material >( "Materials/Tile.xml" )->Clone();
>     tileMaterial->SetTechnique( 0, tileTechnique );
>     tileMaterial->SetTexture( Urho3D::TU_DIFFUSE, tileTexture2D );
>     tileObject->SetMaterial( tileMaterial );

Note the `Clone()` on the material and the technique. I was driving myself crazy cloning one or the other but it turns out you need to clone both. Now you can assign arbitrary textures to materials without one changing the others or a ton of boilerplate code. Nor a need to generate a million (in my case much more than that) XML files for each tile. Plus this will save a lot of resource cache loading times.

Remember to keep an eye on the allocated memory. It would be very easy to have leaks all over the place.

-------------------------

Modanung | 2021-03-26 14:34:45 UTC | #29

[quote="nickwebha, post:28, topic:6749"]
Man, I wish there was a wiki or something.
[/quote]

:sparkles:

https://github.com/urho3d/Urho3D/wiki

-------------------------

