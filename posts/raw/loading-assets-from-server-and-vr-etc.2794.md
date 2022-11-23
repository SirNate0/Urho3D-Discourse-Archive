arpo | 2017-02-14 08:44:02 UTC | #1

**Can Uhro do what I need?**
I have developed a web app that you can use to develop 3D environments. The app is using Three.js an consists of 3D objects, created with the tool, Sky Cubes, particles to simulate rain, snow etc and sound. Since JavaScript in the browser is a bit limited I now would like to create an app where you can view the place you created and I have started to look att Uhro.

So...

Is it possible to import 3D objects from a server together with it's materials? The objects are in obj format and can be altered in any way since my web app controls all of that. Three.js can also export in many other formats if that is needed.

Load sounds from a server?

Load images from a server to use as a skybox, or similar?

Is there a stereoscopic camera to use for VR?

-------------------------

cadaver | 2017-02-14 09:22:55 UTC | #2

You can do all of those by expending a little work yourself, but Urho does not have support for per-asset network streaming built-in. Typically you would stream data in from a server, then create an in-memory asset for use by Urho.

In the realXtend Tundra VR client/server project, we did this at first with Ogre (using a similar method, since Ogre doesn't load data directly from network either), then a lightweight version with Urho. 

http://github.com/realxtend/tundra-urho3d

-------------------------

arpo | 2017-02-14 09:52:38 UTC | #3

Thanks for your response, I asked the same question in the Unity forum a week ago and have still not got any replies. 
Since I'm a JavaScript developer I might ask a stupid question but: does "Urho does not have support for per-asset network streaming built-in" mean that you can't load files from a server?

The data for the places is stored in JSON and OBJ-files. So I want to load the JSON-from the server and based on that info create in-memory assets. The last part I understand works. 

My plane is to build mobile apps using Xamarina/Urhosharp so I guess Xamarina adds a lot of download-stuff-from-a-server-functionality I can use.

Any thoughts about this?

-------------------------

cadaver | 2017-02-14 10:20:32 UTC | #4

Take a look at the built-in HttpRequest class and see what its API can do, it's somewhat low-level.
(In UrhoSharp you can probably also use the .Net network functionality, since HttpRequest is quite simple / limited)

What I mean that you can't e.g. call into the ResourceCache directly and ask it to load a resource over http.

-------------------------

arpo | 2017-02-14 10:25:54 UTC | #5

Tack Lasse! 
I'll take a deeper look.

-------------------------

