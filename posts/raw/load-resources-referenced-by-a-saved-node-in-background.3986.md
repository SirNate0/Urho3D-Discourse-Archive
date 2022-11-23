Alan | 2018-02-03 23:43:02 UTC | #1

Hello there.

I'm saving a Node using myNode->Save() and I want to load that at runtime, however, I would like to make sure the resources referenced in that Node are loaded/cached before instantiating it into the Scene, is there a way to do that or should I do it manually by looping the Components of the Node when I'm saving it and storing the Resources separately so I load them on the background before loading the actual Node?

Thanks

-------------------------

Alan | 2018-02-04 02:30:23 UTC | #2

OK, it was suggested on Gitter that `Scene->LoadAsync` in `LOAD_RESOURCES_ONLY` mode could do the trick, and apparently the PreloadResources calls `BackgroundLoadResource` so I guess I could simply use Scenes for that, before saving a Node I move it to another Scene and to load it back I could load the Scene using Async and wait for it to fully load before instantiating the Node in my main Scene.

-------------------------

