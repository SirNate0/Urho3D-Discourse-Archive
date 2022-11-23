evolgames | 2022-11-08 02:33:56 UTC | #1

I'm always learning something new here. Sometimes I'm not sure if it's a lua thing or an Urho thing. For context, I'm scripting with lua. I'm curious about script objects. I've been using them in projects for a while now, after seeing them in the samples. They seem to be very convenient. I can store data easily self.x self.health etc. I can instantiate a bunch of npcs and create a script object when I do so, and they will automatically run the NPC:Update() function, without me having to cycle through a list and do so manually. If you look at the samples, like the character sample, it's easy to take that script object and make multiple player characters in the same manner. In fact, I did so for an online multiplayer game.

However, I've noticed that with large numbers (in this case, 4000) that performance is hurting from these. Maybe I'm using them wrong. I was attaching a script object to each tile in a topdown 2d game. The script object functions would handle animations of the sprites (I don't use spriter animations) and disable the nodes at certain points and other stuff. Basically, manipulate the static sprites and check things each frame. I'm getting very bad frame rates doing this. And it's not a matter of culling because I need certain things, like entities and items, to update offscreen and was planning on keeping this. So like 40-60 fps. For example, each water tile has a script object to handle waves and animations, grass tiles have them for certain spawn points and triggers, and so on.

I took out the script objects and tried putting each tile in a table and running:

```
function UpdateTiles()
	for i=1,#animTiles do
		animTiles[i].tile:GetComponent("StaticSprite2D").color = Color(Random(1),Random(1),Random(1),1)
	end
end
```
Just as a test manipulation of all 4000 tiles every frame. And to my surprise the fps is 900-1200. I just always assumed the script objects were not that much different from some kind of list that runs certain functions in the program loop. I also assume Nodes are similar?

How are script objects handled in Urho? Any reason they would be slower than just cycling through a table every frame? I don't really need a solution since the above works great for anything I'd need to do to or with a tile, just really curious why that works better.

-------------------------

SirNate0 | 2022-11-08 04:00:34 UTC | #2

I'm not certain about this, but I think crossing from C++ to script may be the bottleneck with the ScriptObject approach. Your for loop remains within the Lua interpreter (well, it calls the functions to set the values and all) and so there's greater possibility for the interpreter to optimize it, especially if you are using LuaJIT.

Take Python as an extreme example - starting the python interpreter can take a significant portion of a second, while running a line in a for loop can be only a few times slower than the comparable machine code, taking only microseconds.

Possibly you made some sort of other mistake with the script objects, which didn't occur with the for loop, but the above would be my first guess.

-------------------------

evolgames | 2022-11-08 14:46:09 UTC | #3

Ah okay that makes sense. Thanks for the example. I noticed it also depends on what operation I do, but it does seem that the script objects are bottlenecked. It's no big deal to do it the other way, fortunately.

-------------------------

