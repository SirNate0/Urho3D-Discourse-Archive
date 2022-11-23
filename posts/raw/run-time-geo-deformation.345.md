ghidra | 2017-01-02 00:59:45 UTC | #1

Along the lines of my later post [url]http://discourse.urho3d.io/t/runtime-geometry-creation/337/1[/url], what about deformation, on generated geo or even imported geo...

Do you have access to the verts of imported geo?

For example, if I wanted to do some fake softbody type deformations on collision, are there methods that will let me get and set the point positions? What about velocities of points? can i get those? and if not, would I be able to grab the verts at a previous time step and potentially calculate them myself?

I'm apologize for all the hypotheticals. I am just curious how far and how easily I can do data manipulation at the vert level..

-------------------------

cadaver | 2017-01-02 00:59:45 UTC | #2

You don't have efficient access to geometry in scripting languages, as they can't safely expose a "freeform" data layout such as a vertex buffer. I don't recommend the use of CustomGeometry for heavy use cases (continuous modification of many vertices on many objects). But in C++ you could access the vertex/index buffers of a model directly and that's what I recommend for manipulating geometry data efficiently.

-------------------------

jmiller | 2017-01-02 00:59:46 UTC | #3

The Bullet physics library has nice softbody dynamics (see videos out there). This is not wrapped by the Urho3D API at this time, but assuming there are no conflicts, one might use Bullet separately or simultaneously. Urho3D and parts of its code might be useful, e.g. in getting geometry in or out. I'm not sure about your requirements or how practical.

-------------------------

ghidra | 2017-01-02 00:59:46 UTC | #4

This might give me a reason to peel into C++ if i can understand this correctly..
Are there any examples that might point me in the right direction?

If I were to just make a class, that say, loads a Sphere; There should be methods that exposes the vert data that I can then manipulate and set back?

You recommended not using customGeometry for large number of object. However, I noticed the getVetices() but not a setter on CustomGeometry. I quickly dug around the other inherited classes, but didnt see anything for getting verts. I'm not being very thorough in my searching at the moment, I am still in the hypothetical stages, but still curious the best methods here.

-------------------------

cadaver | 2017-01-02 00:59:47 UTC | #5

CustomGeometry is based on always rebuilding the whole object when you want to change something, so when animating it you'd be doing the same as defining it the first time.

Because there can be varying vertex buffer layouts (such as 0-n UV channels, tangents or not etc.) and it would be hard to do efficiently, the vertex buffers don't provide an API for modifying single vertices. Instead you either Lock() a data range to acquire a pointer to it, after which you can manipulate it, then Unlock() to apply to the actual GPU vertex buffer. Alternatively you can use the buffer's SetData() operation. In both cases you'll have to understand the data layout and manipulate the underlying raw data, eg. position would be 3 consecutive floats, followed by other vertex elements. Use GetElementMask() on the buffer to know which vertex elements it contains.

When using models and vertex buffers for runtime geometry manipulation, what will come to bite you next is that manipulating a Model affects all drawable objects which are using it. Therefore there needs to be a clone operation in Model to make unique copies. I've submitted an issue on this so that I remember it. :slight_smile: I'll hope to add an example of C++ dynamic geometry manipulation after I implement that.

-------------------------

friesencr | 2017-01-02 00:59:47 UTC | #6

That would be a nice tutorial!

Since I don't know graphics well but my business programming background has lots of batching / grouping I have made arrays of custom geometries and split my mesh into smaller patches so i can get reliable modification times and occlusion.

-------------------------

cadaver | 2017-01-02 00:59:47 UTC | #7

The clone operation for Model & the dynamic geometry sample are now in the master branch.

-------------------------

friesencr | 2017-01-02 00:59:47 UTC | #8

thx Lasse \m/

-------------------------

ghidra | 2017-01-02 00:59:47 UTC | #9

That was fast!

-------------------------

