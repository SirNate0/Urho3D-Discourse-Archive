Alan | 2018-02-04 12:26:55 UTC | #1

Hello there.

I'm trying to use Scene->LoadAsync() to load data without affecting framerate too much, but I can't get it to work properly, it always seem to load it all in a single frame anyway and I want it to load a little bit per frame, code is very simple:
```
		scene->SetAsyncLoadingMs(1);
		scene->LoadAsync(f);
```
I think that should pause loading when it reaches 1ms at a given frame, allow the frame to continue and resume loading on the next frame, but that's not what happens, it locks the game. I'm loading 8 resources and although each of them takes more than 1ms to load, there's no reason it shouldn't spread the load across many frames, loading say 1 per frame.

-------------------------

Alan | 2018-02-04 22:45:12 UTC | #2

I figured out that the problem is loading resources... it's not working very well, when it's preloading the resources it goes through all nodes and passes all the referenced assets to the preloader what could be optimized by discarding duplicates. Also, string sanitization is extremely slow.
Using LOAD_SCENE mode helps a lot but there's no real solution to this. Also the Scene loader works based on direct child nodes.

-------------------------

