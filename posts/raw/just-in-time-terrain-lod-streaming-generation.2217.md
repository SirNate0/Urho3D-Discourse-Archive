krstefan42 | 2017-01-02 01:14:00 UTC | #1

Hi. I want to create a procedural terrain with a 10km draw distance and detail down to a few centimeters. I can't feasibly generate a heightmap for the entire terrain (it would consume too much memory anyway). So I thought I could generate patches of the terrain at the appropriate LOD level on an as-needed basis. It seems like the terrain API allows for connecting multiple sub-terrains with the neighbor terrain functionality. Could this be used to do what I want? If not, I'd be willing to roll my own solution, but would appreciate some pointers on how to do so (i'd rather do it by extending the engine than some bolted-on solution, but I wouldn't know where to begin).

-------------------------

cadaver | 2017-01-02 01:14:00 UTC | #2

You can instantiate new terrains into the scene (with suitable size) and join them as neighbors to ensure the LOD transitions at edges don't bug, but every terrain "piece" you create this way has to be in the same resolution, practically the highest resolution, for the neighbor transition to work properly. If you need to instantiate far away terrain pieces with a lower heightmap resolution (because highest resolution would be too much memory) then you need a custom system or to modify the existing engine code.

-------------------------

horvatha4 | 2017-01-02 01:14:00 UTC | #3

@krstefan42 Welcome to the "Club"!   :smiley: 

Here are a few topic for you:
[url]http://discourse.urho3d.io/t/question-super-large-worlds/1870/1[/url]
[url]http://discourse.urho3d.io/t/managing-large-scenes/1346/1[/url]
[url]http://discourse.urho3d.io/t/infinite-world/1993/1[/url]

Arpi

-------------------------

Dal | 2017-01-02 01:14:05 UTC | #4

I'd like to do this as well... has anyone got anything working yet? Can it be done with Urho's built in workqueue in a cross-platform way?

-------------------------

cadaver | 2017-01-02 01:14:05 UTC | #5

You cannot safely manipulate the scene from outside the main thread, or perform the actual GPU upload of new terrain patches outside main thread, but you can background load heightmap images in advance.

-------------------------

Lumak | 2017-01-02 01:14:05 UTC | #6

[quote="Dal"]I'd like to do this as well... has anyone got anything working yet? Can it be done with Urho's built in workqueue in a cross-platform way?[/quote]

Using the Workqueue class won't work but the Thread class will allow you to do this. Terrain loading can be split into multiple stages. Horvatha4 and I were discussing this on this thread [url]http://discourse.urho3d.io/t/infinite-world/1993/1[/url].

-------------------------

Dal | 2017-01-02 01:14:06 UTC | #7

@Lumak that thread looks interesting.

Does the Thread class still work cross-platform? I guess the most expensive part would be calculating noise or reading heightmap image data for each vertex, so we should be able to do that part in another thread?

-------------------------

Lumak | 2017-01-02 01:14:06 UTC | #8

As far as I know, the Thread class is cross-platform, although, terrain loading will probably not work very well w/o multiple CPU cores or multiple HW threads.

Any loading that happens on the GPU must be done in the main thread, and the most expensive part of the terrain loading is CreatePatchGeometry(), which should be split into two parts: the construction in the background and vertex/index assignment (GPU access) in the main thread.

Edit: just to note that my PC is not the greatest, it's nearly 10 yrs. old so you'll probably get a better performance with whatever you got  :wink:

-------------------------

