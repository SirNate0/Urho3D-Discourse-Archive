vivienneanthony | 2017-01-02 01:05:33 UTC | #1

Hi

How does Async loading works? So far I used the code and getting segfault when the async finishes specifically file->getname in urho?  I have feeling need to make the File a shared pointer in the class header.

Now I'm l lost on individual static and animated model, and terrain Async loading. I don't see the info in the docs. I need to load other resources async for the loading, progress, slash transition 

Viv

-------------------------

cadaver | 2017-01-02 01:05:36 UTC | #2

Scene async loading simply means the scene will load a part of itself every frame to ensure the framerate does not get bogged down or so that there isn't a long pause.

During async loading the scene will hold onto the scene file with a SharedPtr. You should not need to hold onto the file yourself at all, and certainly not for example delete it manually.

You can also make the resource cache manually background preload individual resources, which is normally part of the async scene loading. See ResourceCache::BackgroundLoadResource(). Note that if you start a resource background loading, but then call GetResource() for it in the main thread before it has finished loading, the main thread will stall to wait for completion, so it's only advantageous when you do it early enough in advance.

-------------------------

