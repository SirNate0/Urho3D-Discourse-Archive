glhrmfrts | 2018-08-30 18:41:26 UTC | #1

Hello, I'm making most of my game using lua, including my map generator, which takes some time and right now it's blocking the main thread. I want to run it in the background and display a loading screen while it generates the map, so is it possible to run a lua script in a background thread? I'm using a customized version of the Urho3DPlayer and I have some experience with C++, I'm just not sure how I would approach this using the LuaScript subsystem.

Thank you

-------------------------

JTippetts | 2018-08-31 02:36:02 UTC | #2

I'm not sure how you would do that. The Lua script system just isn't really designed that way. However, while someone more clever than me might be able to devise a solution, my recommendation is to move your map generation stuff into C++. The reason for this is tolua++. The Lua system uses tolua++ to generate the bindings, and as I've discovered [in the past](https://github.com/urho3d/Urho3D/issues/649) it creates some tables behind the scenes to help it with management (tracking which classes are subclasses of others, etc....) that can grow pretty large. The bad part is, these tables don't ever get compacted or resized, so as they grow they begin to bog down things like garbage collection.

Usage patterns that really trigger this behavior cropped up in my own map generation code. When I was generating tile map chunks, I would iterate a chunk on X and Y, and inside I would do Magic(TM). However, if any of that Magic created any Urho3D objects that were to be managed by tolua++ (things such as Color or Vector3 returned by value from bound functions/methods or created inside the nested loops as locals) then those internal tables would grow huge, and cause nearly immediate performance problems. For that reason (as well as other general performance reasons) I moved all of my map generation logic into C++ routines, and reserved Lua for other, less garbage-intensive tasks.

-------------------------

