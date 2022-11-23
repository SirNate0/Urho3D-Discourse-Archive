rku | 2017-10-17 14:00:48 UTC | #1

Does current `Terrain` component support cutting holes in it? Say for making cave entrance. API does not suggest anything obvious, but maybe there is some smart trick to achieve this?

-------------------------

Eugene | 2017-10-25 15:25:11 UTC | #2

Graphics is simple.
Physics is average.
Navigation etc - I don't know.

[quote="Eugene, post:2, topic:3538"]
Semi-transparent material for graphics.

Physics will require tweaking Bullet Physics, but that’s easy. I shall probably commit the change into Urho.

Navigation will also require some tweaking.

Thanks for reminding, I shall probably add some support of the holes in the Terrain. However, don’t expect this in the nearest future.
[/quote]

-------------------------

Eugene | 2017-10-17 15:30:05 UTC | #3

FYI: How to make Bullet work with holes in terrain:

1. Inherit from `btHeightfieldTerrainShape`
2. Override `processAllTriangles`
3. Somehow drop triangles: use mask array or sentinel height. I've just copy-pasted content of `processAllTriangles`.
4. Use your own height field shape.

-------------------------

Enhex | 2017-10-17 23:26:51 UTC | #4

Maybe you could use several terrains, leaving a gap between them?

-------------------------

rku | 2017-10-17 16:07:00 UTC | #5

I thought of that. It would likely be easiest approach, but then these two terrains would not be stitched together and lesser problem is gaps would be allowed only at terrain boundaries.


@Eugene thanks for pointers. Any idea if sentinel height value could be used with heightmap itself? I tried naive thing (discarding vertices [here](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Terrain.cpp#L706)) and it ended up being a royal mess because clearly i have no idea what im doing.

-------------------------

johnnycable | 2017-10-17 17:32:03 UTC | #6

Uhm, looking at terrain just these days...
I found, for instance, [BlenderGis](https://github.com/domlysz/BlenderGIS/wiki/Materials-node-setup-builder), which allows you to get multimapping; one could use heightmap as usual, and slope and aspect to get direction of movement for characters for recast/detour I think... or for intentional movement inside a cave...
Anyway terrain basically is a flat plane and doing st like cave sounds like voxels... the normal solution is using point of interests and teleporting somewhere else...
But of course this is not continuos movement like probably you're looking for...

-------------------------

Eugene | 2017-10-17 17:46:06 UTC | #7

It's hard to combine stable geometry discarding, sentinel heights and geomipmapping.
Even PhysX use material index instead of height to mask cells as gaps.
I recommend you to hold the idea about sentinel heights and revise it if it become important.

-------------------------

Enhex | 2017-10-17 23:39:21 UTC | #8

Another approach is to just use something other than heightmap terrain, like regular 3D models.
You can also mix it up with terrain, leaving a low height hole where you want to place your 3D model cave, so the terrain is below the cave.

a workaround with terrain is to have some sort of transition between the cave and the terrain, like a door.

-------------------------

rku | 2017-10-18 07:35:34 UTC | #9

@Enhex my primary reason why i looked at terrain component is that it handles stitching and all that. Using 3D model would probably be akin to making own terrain system.

On a closer look at terrain component i noticed these:

```cpp
void SetNorthNeighbor(Terrain* north);
void SetSouthNeighbor(Terrain* south);
void SetWestNeighbor(Terrain* west);
void SetEastNeighbor(Terrain* east);
```

Does terrain component handle stitching of multiple `Terrain` components together? Not just `TerrainPatch`es within `Terrain`? If so that brings me to your original suggestion.

Take a following picture as example:
![terrains|442x284](upload://hrloLpln9dvAdUofbtskd13x0xa.png)
Each rectangle represents `Terrain` component. Each green border represents neighbour relationship being set. Red border represents no neighbour relationship.

Am i right to think that in this setup terrain would not be stitched together at the red border? If so then adjacent tiles could have different height (which would be a very steep cliff if stitched together) and create a hole when no stitching is applied to that border.

-------------------------

Eugene | 2017-10-18 08:12:08 UTC | #10

AFAIK, terrain wouldn't be stiched unless you stich it manually. I mean, it depends on values in heightmap.
But I find this approach very limited to be useful.

-------------------------

rku | 2017-10-18 08:23:23 UTC | #11

What does `SetXXNeighbor(Terrain*)` do then?

-------------------------

Eugene | 2017-10-18 08:43:54 UTC | #12

Ensures that geomipmapping won't make any unexpected holes

-------------------------

rku | 2017-10-18 09:58:53 UTC | #13

[quote="Eugene, post:12, topic:3667"]
geomipmapping
[/quote]

Excuse my ignorance, but that sounds very much like stitching up terrains. Could you please elaborate?

-------------------------

Eugene | 2017-10-18 10:32:18 UTC | #14

Separate terrains don't have any shared data, so they couldn't stich themselves without explicit user intention.

Neigbors are used to ensure that terrain patches on the edges has valid topology and there won't be any gap caused by mismatching LODs.

-------------------------

Enhex | 2017-10-18 12:14:44 UTC | #15

You don't have to handle stitching with a 3D model, just let it intersect with the terrain and you won't have gaps.

-------------------------

rku | 2017-10-22 12:33:55 UTC | #16

I am experimenting with setting up multiple terrains. Docs are sparse on this topic and there seem to be hidden requirements for making entire thing work.

What is supposed to be a heightmap format? I noticed that terrain skips 1 pixel at the edges of heightmap, thus for creating 16x16 units terrain i need to use 17x17 heigthmap. Whats the purpose of skipped edge?

How exactly am i supposed to use `SetXXXNeighbor()`? My test code:

```cpp

        auto terrain = scene_->CreateChild()->CreateComponent<Terrain>();
        terrain->SetPatchSize(8);
        terrain->SetSpacing({1, 1.f / 255.f, 1.f});
        terrain->SetHeightMap(GetCache()->GetResource<Image>("Textures/heightmap.png"));

        auto terrain2 = scene_->CreateChild()->CreateComponent<Terrain>();
        terrain2->SetPatchSize(8);
        terrain2->SetSpacing({1, 1.f / 255.f, 1.f});
        terrain2->SetHeightMap(GetCache()->GetResource<Image>("Textures/heightmap.png"));
        terrain2->GetNode()->SetPosition({16, 0, 0});
        terrain->SetEastNeighbor(terrain2);
```
And a heightmap. I scaled it up by 800% for demo purposes. Actual image used by code is 17x17.
![heightmap|136x136](upload://fgkF33How0ftxdhexkzp48qYD1Y.png)

Test code aligns terrain tiles like so:
![heightmap|136x136](upload://fgkF33How0ftxdhexkzp48qYD1Y.png)![heightmap|136x136](upload://fgkF33How0ftxdhexkzp48qYD1Y.png)

On the right edge of terrain i expected to get seamless transition between terrains, however it looks like this:
![terrain|690x441](upload://eRAQXMpSym4qvfJ6sHlCOzFrDGv.png)

Notice crack between points painted in white on heightmap. Also neighbour terrains are not taken into account when calculating tiles.

So whats the right way to use terrain in this case?

-------------------------

Eugene | 2017-10-22 12:44:38 UTC | #17

[quote="rku, post:16, topic:3667"]
thus for creating 16x16 units terrain i need to use 17x17 heigthmap. Whats the purpose of skipped edge?
[/quote]

Do you mean 16x16 quads?

[quote="rku, post:16, topic:3667"]
How exactly am i supposed to use SetXXXNeighbor()?
[/quote]
If you want two terrains be seamlessly connected, you should set them as neighbors for each other.

-------------------------

rku | 2017-10-22 12:54:24 UTC | #18

[quote="Eugene, post:17, topic:3667"]
Do you mean 16x16 quads?
[/quote]

I mean entire terrain being 16x16 quad.

Edit: i suppose 1 pixel in heightmap means one vertex. In order to get 1x1 tile terrain i would need 2x2 heightmap, because one quad needs 4 vertices at the corners. So 16x16 terrain needx 17x17 pixels. Right?

[quote="Eugene, post:17, topic:3667"]
If you want two terrains be seamlessly connected, you should set them as neighbors for each other.
[/quote]

Like so?
```cpp
        terrain->SetEastNeighbor(terrain2);
        terrain2->SetWestNeighbor(terrain);
```
Because it produces exactly same visual result.

-------------------------

Eugene | 2017-10-22 13:06:33 UTC | #19

[quote="rku, post:18, topic:3667"]
i suppose 1 pixel in heightmap means one vertex. In order to get 1x1 tile terrain i would need 2x2 heightmap, because one quad needs 4 vertices at the corners. So 16x16 terrain needx 17x17 pixels. Right?
[/quote]

I think so.

[quote="rku, post:18, topic:3667"]
Because it produces exactly same visual result.
[/quote]
Well, that's strange. Maybe terrains have different scale?
They must have connected geometry. Could you check the grid?

-------------------------

rku | 2017-10-22 13:33:04 UTC | #20

[quote="Eugene, post:19, topic:3667"]
Could you check the grid?
[/quote]

Do you mean seeing debug geometry? Terrain does not have built in debug info rendering on purpose.  I added it myself bit it isnt exactly revealing.
![terrain|690x382](upload://cmWSq6mq0Ei0GsFzJjWAMs3ifE.png)

They are of exactly same scale. Snippet i pasted previously - its pretty much all the code setting up scene. Other stuff is just setting up viewport, camera and creating scene object. You can take a look at entire thing: [terrain.zip](https://drive.google.com/uc?id=0Bx2UNCIdLR4VazlwQnhObUcySG8)

Edit:
I just noticed that white pixel on the right was tiny bit darker than white pixel on the left. That caused height mismatch. But there is still normal issue which makes lighting look weird. Is terrain supposed to take into account neighbouring terrains when calculating normals?

![terrain|690x320](upload://xpRb4qeoyM2wCpPcuKOyk9jMfw5.png)

-------------------------

Eugene | 2017-10-22 13:37:50 UTC | #21

[quote="rku, post:20, topic:3667"]
I just noticed that white pixel on the right was tiny bit darker than white pixel on the left. That caused height mismatch.
[/quote]
I have just noticed too xD

[quote="rku, post:20, topic:3667"]
But there is still normal issue which makes lighting look weird. Is terrain supposed to take into account neighbouring terrains when calculating normals?
[/quote]
Yeah, I don't like this lighting. Terrain definetely _could_ pick neighbor's data when generating normal, but it doesn't do it for now... It could be hard, but must be possible.

-------------------------

Modanung | 2017-10-22 13:52:46 UTC | #22

Looking at the [code](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Terrain.cpp) it seems like neighbours should be set before creating the terrain geometry:
```
void Terrain::HandleNeighborTerrainCreated(StringHash eventType, VariantMap& eventData)
{
    UpdateEdgePatchNeighbors();
}
```

```
    // Send event only if new geometry was generated, or the old was cleared
    if (patches_.Size() || prevNumPatches)
    {
        using namespace TerrainCreated;

        VariantMap& eventData = GetEventDataMap();
        eventData[P_NODE] = node_;
        node_->SendEvent(E_TERRAINCREATED, eventData);
    }
```

-------------------------

Eugene | 2017-10-22 14:03:41 UTC | #23

Huh, just recalled...
If you want high-quality terrain lighting, use world-space normal maps.
Bake true normals of terrain into texture and use them in the shader _instead_ of vertex normals.
It has almost zero performance penalty, doesn't requre changes in Terrain and _has much much better quality_.
Vertex normals are badly corrupted by geomipmapping and look nasty. Texture is always nice.
(just a hint)

[quote="Modanung, post:22, topic:3667"]
Looking at the code it seems like neighbours should be set before creating the terrain geometry
[/quote]
I don't think that it's important because Terrain geometry is created via GetRawNormal/GetRawHeight that don't care about neighbors.

-------------------------

rku | 2017-10-22 15:04:57 UTC | #24

Tried setting neighbours before setting heightmap too. @Eugene guessed right - it had no effect.

Sounds like normals in a texture are easy way around the problem, going to do just that. Thanks ;)

-------------------------

JTippetts | 2017-10-22 22:22:07 UTC | #25

The cool part about using a normal map for normals is you can go higher resolution, to add detail that isn't there in the heightmap. Bake your normal map from a much higher resolution version of the heightmap, then downsample that heightmap for the actual heightmap, etc... It's a process I'm working on implementing in my terrain editor.

-------------------------

rku | 2017-10-25 10:09:46 UTC | #26

Back to original issue.. I found interesting idea on the internets: having depth mask object in a place where hole is supposed to be cut in the terrain. I created material that makes box transparent and all, tried ordering of box and terrain rendering but best i could get was a black or transparent box but no hole in the terrain. Any pointers would be greatly appreciated.

As for collisions one person on youtube mentioned using trigger objects disabling collision with the terrain when passing through masked area. This indeed sounds like perfect solution. Much simpler than altering collision/rendering meshes.

-------------------------

Eugene | 2017-10-25 12:00:58 UTC | #27

[quote="rku, post:26, topic:3667"]
I found interesting idea on the internets: having depth mask object in a place where hole is supposed to be cut in the terrain.
[/quote]
I don't understand the idea, may you elaborate?

BTW, I never liked solutions with stencil and other pipeline hacks because it makes many things broken and manual control is required..

[quote="rku, post:26, topic:3667"]
This indeed sounds like perfect solution
[/quote]
It is. If you could guarantee that:
1. All your holes have some "restricted area" around the hole edge that is never collided.
2. This restricted area is bigger that any dynamic object that could collide your hole.
![image|380x326](upload://o6n9LKjsagnEh93Cw50JkIgUYVM.png)

-------------------------

rku | 2017-10-25 12:12:33 UTC | #28

[quote="Eugene, post:27, topic:3667"]
I don’t understand the idea, may you elaborate?
[/quote]

As i understand rendering "mask" object is supposed to alter depth buffer making part of terrain covered by "mask" object transparent.

In video i mentioned mask object shader adds object to rendering queue at `Geometry+10`. [link](https://youtu.be/uxXEV91xsSc?t=173)
Same thing is done with terrain material, except its added to queue at `Geometry+100`. [link](https://youtu.be/uxXEV91xsSc?t=326)

I am not familiar with unity terms, but it seems this technique exploits rendering order.

Possibly:
1. Render mask object, depth buffer modification done here
2. Render terrain object, previous depth buffer modification prevents terrain from rendering at spot where mask object was visible.

Did i get it right?

-------------------------

Eugene | 2017-10-25 12:46:54 UTC | #29

I see. It must work if you set correct render order. Default is 128. Terrain hole and terrain itself should have bigger order than everything else. Hole technique must have depthwrite=true. Note that hole shader mustn't discard pixels with zero alpha.

If I understand correctly, this hack won't work if your Camera could move through the hole.

-------------------------

rku | 2017-10-25 12:59:04 UTC | #30

[quote="Eugene, post:29, topic:3667"]
If I understand correctly, this hack won’t work if your Camera could move through the hole.
[/quote]
Why not? Considering camera can see through that spot and collisions would be disabled upon moving through..

Could you take a peek at my technique and material?
```xml
 <technique vs="Unlit" ps="Unlit">
    <pass name="alpha" depthwrite="true" depthtest="lessequal" blend="replace" />
</technique>
```
```xml
<material>
    <technique name="Techniques/DepthMask.xml" />
    <parameter name="MatDiffColor" value="0 0 0 0" />
    <renderorder value="130" />
</material> 
```

They result in a black mask object. For terrain i am using original `Materials/Terrain.xml` material by the way.

-------------------------

Eugene | 2017-10-25 13:05:28 UTC | #31

[quote="rku, post:30, topic:3667"]
For terrain i am using original Materials/Terrain.xml material by the way.
[/quote]

What about Terrain render order?

[quote="rku, post:30, topic:3667"]
Why not? Considering camera can see through that spot and collisions would be disabled upon moving through…
[/quote]
Huh, it would be fine if you set front face culling for your mask object material.

-------------------------

rku | 2017-10-25 13:08:51 UTC | #32

[quote="Eugene, post:31, topic:3667"]
What about Terrain render order?
[/quote]

Terrain material does not set `renderorder` so it must be default value.

-------------------------

Eugene | 2017-10-25 13:11:17 UTC | #33

[quote="rku, post:32, topic:3667"]
Terrain material does not set renderorder so it must be default value.
[/quote]

So it won't work if you draw terrain before cutting the hole.

-------------------------

rku | 2017-10-25 13:22:23 UTC | #34

I tried changing `renderorder` of mask material to 0, 120, 130, 200. I also tried explicitly adding `renderorder` to terrain material and changing numbers so their order changes. Nothing has any effect which makes me think i messed up something else in material or technique.

-------------------------

Eugene | 2017-10-25 13:50:32 UTC | #35

[quote="rku, post:34, topic:3667"]
Nothing has any effect which makes me think i messed up something else in material or technique.
[/quote]
I don't know what could be wrong with materials.
The most important thing is that hole is rendered before terrain:

> I also tried explicitly adding renderorder to terrain material and changing numbers so their order changes.

The second important thing is that hole material writes depth.

> depthwrite="true"

You should be able to see hole if you set alpha = 0.1.
If you turn lighting on and make your terrain semi-transparend, you should be able to see the actual order of objects: maybe Urho doesn't handle render order properly.

-------------------------

rku | 2017-10-25 15:25:11 UTC | #36

Victory! This is how its done:

For depth mask object:
```xml
 <technique vs="Basic" ps="Basic">
    <pass name="alpha" depthwrite="true" blend="addalpha" />
</technique>
```
```xml
<material>
    <technique name="Techniques/DepthMask.xml" />
    <parameter name="MatDiffColor" value="0 0 0 0" />
    <renderorder value="129" />
</material> 
```
For terrain:
```xml
<material>
    <technique name="Techniques/DiffAlpha.xml" />
    <renderorder value="130" />
</material>
```
Important: terrain has to have technique supporting alpha. Result:

![2|320x255](upload://ZthkxULr2mC7fglvUIBuIHNvv5.gif)

Thank you everyone for the help!

-------------------------

Eugene | 2017-10-25 16:01:12 UTC | #37

[quote="Eugene, post:31, topic:3667"]
Huh, it would be fine if you set front face culling for your mask object material.
[/quote]
@rku Sorry, I was wrong twice. It won't work in common case.
This hack won't work if hole object is not rendered in front of terrain. E.g. if your camera is inside hole object.

PS. Rendering terrain after all other geometry will have negative performance impact due to overdraw.

PS2. Your terrain should also be rendered after semi-transparent things like particles.

-------------------------

rku | 2017-10-26 08:42:14 UTC | #39

@Eugene thank you for insights. Indeed this appears to be fitting for just some usecases. I tried making mask object as thin as possible, but even then camera passing through it results in a tiny few pixels strip across entire screen. That strip is terrain being no longer masked. And like you said, performance issues.. I guess they could be solved by replacing material of those terrain patches that have holes. Not much point in that considering previous issue.

Back to the drawing board i guess. I took a closer look at terrain code and seems like sentinel height values are off the table as well. Terrain component does a smart thing reusing index buffers between patches. Going to try to experiment by allowing unique index buffers for patches.

-------------------------

Eugene | 2017-10-26 10:09:57 UTC | #40

[quote="rku, post:39, topic:3667"]
Back to the drawing board i guess. I took a closer look at terrain code and seems like sentinel height values are off the table as well. Terrain component does a smart thing reusing index buffers between patches. Going to try to experiment by allowing unique index buffers for patches.
[/quote]

I don't think it's good solution if you want to use geomipmapping. There is no change to generate nice automatic LODs for terrain with corrupted geometry.

Heightfield use R or RG channels for height.
You could use B channel to mask holes for physics.
Of course, you'll need semi-transparent material for terrain.

-------------------------

rku | 2017-10-26 10:31:57 UTC | #41

[quote="Eugene, post:40, topic:3667"]
I don’t think it’s good solution if you want to use geomipmapping. There is no change to generate nice automatic LODs for terrain with corrupted geometry.
[/quote]

My idea was to allow it generate and process all vertices and only to not render triangles where at least one vertex is at zero height.

[quote="Eugene, post:40, topic:3667"]
Of course, you’ll need semi-transparent material for terrain.
[/quote]

But transparent objects are rendered after geometry, so it means overdraw like with previous approach, no?

-------------------------

Eugene | 2017-10-26 10:44:06 UTC | #42

[quote="rku, post:41, topic:3667"]
But transparent objects are rendered after geometry, so it means overdraw like with previous approach, no?
[/quote]

1-bit transparency is rendered like solid, so it's fine (ALPHAMASK pixel shared define in material).

[quote="rku, post:41, topic:3667"]
My idea was to allow it generate and process all vertices and only to not render triangles where at least one vertex is at zero height.
[/quote]
You will either have your holes disappearing (if hole is fully covered with low-quality LOD) or growing x2-x4-x8-etc (if it's not) as lod quality is decreased. Impossible to control, impossible to tune. The only way is to disable geomipmapping at all.

-------------------------

