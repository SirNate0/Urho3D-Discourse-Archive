theslimde | 2017-01-02 00:58:46 UTC | #1

Hi guys,

I have a principal question about networking in Urho3D. Let's assume I would want to create a typical Server, Client setup, where the Server is the authority. A easy way to do this seems to just use scene replication and just add (almost) everything to the scene on the server. However that seems strange, especially since the server should run in headless mode. 

So I thought I could do this: Just add the Nodes to the Scene on the server and no Materails, Models, Lights etc. The client would than copy the scene (via scene replication) and add those things to the existing nodes.

Is this a way that makes sense? If so, how would you tag the Nodes so the client knows which Models need to go on which Nodes? Or would you send a big list 
of Events to the client that explain what Models go on what Nodes?

Am I on the right way?

Thanks in advance!

-------------------------

cadaver | 2017-01-02 00:58:46 UTC | #2

The NinjaSnowWar game in server mode should already run also headlessly.

The idea is that you are able to load just the same objects on the client and server, a light for example exists in the scene and can change its parameters (which will be replicated to clients) but it doesn't actually render. Meshes are loaded into CPU-side memory also on headless mode, so that physics can handle per-triangle collisions correctly. Materials and textures, on the other hand, won't be loaded for real (the loading function just returns immediate success without doing anything), the components like StaticModel just refer to the materials so that the material information is correctly transmitted to the client.

In other words everything you describe should already work without any extra effort needed, and without the server consuming unnecessary resources. Or if it doesn't, it's a bug and you can file an issue :slight_smile:

-------------------------

theslimde | 2017-01-02 00:58:46 UTC | #3

Thanks for the quick response!

One quick follow up question: Am I supposed to add a octree component to the (headless) server? 
To me it seems unecessay, but if I don't, I get a console full of ERROR: No Octree component in scene,...
(even though it seems to work nonetheless).

-------------------------

cadaver | 2017-01-02 00:58:46 UTC | #4

Yes, you need the Octree, as in addition to culling it does things like animation updates. Also, you can still do graphical raycasts in a headless system.

-------------------------

