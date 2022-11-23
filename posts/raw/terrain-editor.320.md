jorbuedo | 2017-01-02 00:59:35 UTC | #1

Hi, I'm working on a terrain editor, basically heightmap modification and texturing in real time. For now I'm starting with the heightmap, but I think I'll have to modify  the Terrain source code.
The approach I was using was to modify the heightmap  image, the problem is that reloading the whole geometry with the new image takes almost a second, so it can't be used efficiently as a brush to paint height.

Looking at the source, I think it requires something to modify the geometry on the fly, and another function to update the heightmap image to the new geometry. 

Also, to speed things up, the vertex buffer should be modified using shaders. That would also make easier creating new brushes, just create a shader and pass it as argument to the modify geometry function.


I think I can make it, but I'm not sure how long it will take, I'm not familiarised with the code and I never used shaders.



What are your thoughts about it?


[img]http://i61.tinypic.com/nbeqzb.jpg[/img]

-------------------------

friesencr | 2017-01-02 00:59:35 UTC | #2

I am very interested.  I have a hard time believing anything would take a second in urho.  Are you will to show the code how you are modifying the terrain?

-------------------------

jorbuedo | 2017-01-02 00:59:36 UTC | #3

Sure. It's in lua.
The code for creating the Terrain is almost the same as in the examples, but storing the image in a variable.
[code]    -- Create heightmap terrain
    terrainNode = scene_:CreateChild("Terrain")
    terrainNode.position = Vector3(0.0, 0.0, 0.0)
    local terrain = terrainNode:CreateComponent("Terrain")
    terrain.patchSize = 64
    terrain.spacing = Vector3(2.0, 0.5, 2.0) -- Spacing between vertices and vertical resolution of the height map
    terrain.smoothing = true
    heightMapImage = cache:GetResource("Image", "Textures/HeightMap.png")

    terrain.heightMap = heightMapImage
    terrain.material = cache:GetResource("Material", "Materials/Terrain.xml")
    -- The terrain consists of large triangles, which fits well for occlusion rendering, as a hill can occlude all
    -- terrain patches and other objects behind it
    terrain.occluder = true[/code]

Then the painting itself. This is just an example, not a real brush, it increases +10% the height on each point. 

[code]function PaintBrush(center, radius)
    radius = radius or 80.0
    center = center or Vector3(.0,.0,.0)
    local terrain = terrainNode:GetComponent("Terrain")
    
    center.x = (center.x + heightMapImage.width) / terrain.spacing.x
    center.z = (center.z - heightMapImage.height)/ terrain.spacing.z * (-1.0)
    radius = radius / terrain.spacing.x
    radiusSquare = radius * radius or 400.0
    
    local x_min = center.x - radius
    
    local y_min = center.z - radius
    
    local x_max = center.x + radius
    
    local y_max = center.z + radius
    
    for i=x_min, x_max do
        for j=y_min, y_max do
            if ((i - center.x) * (i - center.x) + (j - center.z) * (j - center.z)) <= radiusSquare then
                heightMapImage:SetPixel(i,j, heightMapImage:GetPixel(i,j) * 1.1)
            end
        end
    end
    terrain.heightMap = heightMapImage
end[/code]

You should be able to add that to the water or vehicle example and execute the paint through console, both arguments are optional, it will paint a 80 radius circle on the centre of the map. 


I don't think it's weird that it takes a second, it's reconstructing all the vertex in the terrain from scratch, instead of just the ones being modified.

-------------------------

cadaver | 2017-01-02 00:59:36 UTC | #4

There are some modifications in the master branch now which make partial updates take less time. It basically checks for which terrain patches the heightmap image has actually changed. I tested it in the vehicledemo by constantly updating the terrain under the vehicle (1 pixel only) and it seemed to work at a nice framerate.

The slow parts are (among other things) the heightmap smoothing, calculating LOD errors for all LOD levels, and generating normals for the vertex buffer data.

-------------------------

jorbuedo | 2017-01-02 00:59:36 UTC | #5

I'll try to disable those things and see if it goes fast enough.

-------------------------

jorbuedo | 2017-01-02 00:59:36 UTC | #6

Ok, it seems fast enough now. I'll give it a try and make the brushes just with lua.

-------------------------

christianclavet | 2017-01-02 01:06:17 UTC | #7

HI, I'm an thinking about creating the geometry directly in URHO (A simple plane with vertices of the resolution of the height map), then manipulating the vertices directly. Once the edit is done of the terrain mesh, convert the vertices values to a height map and replace it with a terrain mesh.
My old editor use a similar method and refreshes are quite fast. There are methods to create a mesh and modify all the attributes of the meshbuffers in URHO3D?

-------------------------

codingmonkey | 2017-01-02 01:06:17 UTC | #8

>There are methods to create a mesh and modify all the attributes of the meshbuffers in URHO3D?

Yes, you need create your new class based on Drawable

class URHO3D_API YourNewDrawableClass : public Drawable {}

then resize batches and fill geometry for each batch as you wish

geometry_->SetVertexBuffer(0, vertexBuffer_, MASK_POSITION | MASK_COLOR | MASK_TEXCOORD1);
geometry_->SetIndexBuffer(indexBuffer_);
batches_.Resize(1);
batches_[0].geometry_ = geometry_;

for more info see thread about creating tail-component [topic828.html](http://discourse.urho3d.io/t/solved-own-component-based-on-drawable-dont-work/809/1) there a lot code examples

-------------------------

