lazypanda | 2017-01-02 01:03:30 UTC | #1

Hey again!

Could some one tell me about vegetation systems and how they're implemented in games. I've been studying pagedgeometry from ogre3d. The general notion seems to be to divide the terrain into batches and load grass around the camera in a cache-friendly way (using vectors?). 

My questions are:
 - Can I use the octree in Urho3d for spatial partioning, or is it better to write my own grid classes?
 - What is the most performance friendly way to load and unload meshes in Urho?
 - Can I use the inbuilt instancing with alpha (grass)? I read in some thread that this wasn't possible in Urho. 

Thanks  :smiley:

-------------------------

cadaver | 2017-01-02 01:03:31 UTC | #2

The octree should be perfectly fine for creating grass objects dynamically, and in fact you would certainly want to use it so that the grass objects can interact normally with the rest of the rendering (ie. lights and shadows).

If the grass patches use ordinary model resources loaded through the ResourceCache, instantiating more copies of them is fairly fast (ie. create a scene node and a drawable component, SetModel to it), as well as deleting them (just remove the scene node). ResourceCache takes care of keeping the model resource(s) in memory for fast access.

If you need to create model resources dynamically, there is not a real "fast" or a "slow" path either to it. Create model, create vertex/index buffers, fill them with data. Refer to the 34_DynamicGeometry C++ sample.

Most FPS / TPS games seem to use alpha-tested opaque vegetation, which means that it's not an actual alpha object as far as the Urho's renderer would be concerned, but writes to the Z-buffer normally. In this case the renderer can instance your objects. If you need actual alpha blending, the grass patches will need to be distance-sorted and that will tax the CPU and not allow instancing. In that case I'd recommend to use as large patches as possible, so that you only need a few of them.

-------------------------

lazypanda | 2017-01-02 01:03:31 UTC | #3

Thanks cadaver! So I've thought  about StaticModels close to the camera and billboards further back. Are lots of billboards performance hungry in Urho? Also is a cache system needed like the one in pagedgeometry or should add/removing nodes be enough?

-------------------------

cadaver | 2017-01-02 01:03:31 UTC | #4

One BillboardSet component is one drawcall. These will not be instanced because each sends unique shader constants for the camera orientation. So gather as many billboards as you can into one BillboardSet. About the cache system I cannot answer, as I haven't studied Ogre PagedGeometry code and don't know what it exactly does, so you should profile yourself: start with the simplest code you can and see if the performance is already OK.

-------------------------

franck22000 | 2017-01-02 01:03:31 UTC | #5

Here is an image of my day/night cycle with my vegetation system in uhro. My system is made by using a custom grid class and some billboard textures that are automatically generated from the tree models. Tree in front are regular meshes and of course trees in distance are billboards.

So yes urho can handle this easilly but you need to do some of the work yourself :slight_smile: 

[url=http://tof.canardpc.com/view/fd79006c-3ec2-4812-ab53-de30b3dd5e6f.jpg][img]http://tof.canardpc.com/preview2/fd79006c-3ec2-4812-ab53-de30b3dd5e6f.jpg[/img][/url]

-------------------------

gawag | 2017-01-02 01:03:32 UTC | #6

Oh that looks really great!

I've used PagedGeometry with Ogre before and I would / we could really need something like that for Urho3D as well.
I've also used two different Day/Night/Weather things with Ogre, one was called SkyX I think. Those systems also changed models and the terrain by adding a shader phase to it, to influence them with the current lighting.

Could you release your work regarding those things in some way? Even it's unfinished/buggy. They could be expanded to be general and easily usable as PagedGeometry was.
Can it also do grass? PagedGeometry used two triangles per grass "billboard", which were deformed depending on terrain shape. Paged Geometry also automatically created images of objects to have billboard of them from different angles.
Are your systems used in any game project?

-------------------------

