Autian | 2017-01-02 01:04:39 UTC | #1

Hello,
I get heavy lags after creating a big table in Lua. During the lags, nothing is editing the table in any way, at least in the lua code. The table is created and then it is left alone, until I press "R", which creates objects and links them in that array. "T" will delete that table (for testing!). When deleting the table, the lags are away.

Something is doing stuff with that big table in every frame update. So, what is going on and how can I eliminate these lags?

The table is created that way.
[code]local function initChunk(_c)
	if _c.d == nil then
		_c.d = {}
	end
	for bx = 1, 8, 1 do
		if _c.d[bx] == nil then
			_c.d[bx] = {}
		end
		local a = _c.d[bx]
		for by = 1, 8, 1 do
			if a[by] == nil then
				a[by] = {}
			end
			local b = a[by]
			for bz = 1, 8, 1 do
				if b[bz] == nil then
					b[bz] = {id = 0, obj = nil}
				end
			end
		end
	end
end
local function worldInit(_w)
	local cxmax = 4;
	local cymax = 4;
	local czmax = 4;
	for cx = 1, cxmax, 1 do
		if _w[cx] == nil then
			_w[cx] = {}
		end
		local a = _w[cx]
		for cy = 1, cymax, 1 do
			if a[cy] == nil then
				a[cy] = {}
			end
			local b = a[cy]
			for cz = 1, czmax, 1 do
				if b[cz] == nil then
					b[cz] = {}
					initChunk(b[cz])
				end
			end
		end
	end
end[/code]

Edit: reworked the code, but has the same functionality as before.

-------------------------

GoogleBot42 | 2017-01-02 01:04:40 UTC | #2

I think I should say something first... are you making a minecraft clone?  Writing the core logic in lua is a *really bad* idea.  There is a lot of wasted memory and it will perform slower (if you are using luaJIT that will help with speed).

Second thing, are you having one cube model for each block in the world?  If so, you will get horrible performance.  You will need to have groups of blocks share a single mesh (or maybe all blocks in the world share a single mesh).

The lag isn't from your huge table.  That is just data that is managed strictly by lua.  The objects referenced by different parts of you lua table aren't the source of lag either.  It is that you are drawing the terrain of the world in one of the least efficient was you could.

I think you should do some research or you will just get really frustrated, give up, and have wasted you time.  :frowning:  :confused: 

IDK how good this is but his might help some: [url]http://www.teamavolition.com/topic/4130-just-how-easy-is-it-to-make-a-game-like-minecraft/[/url]

-------------------------

Autian | 2017-01-02 01:04:41 UTC | #3

[quote]I think I should say something first... are you making a minecraft clone?[/quote]
Yup, kind of. Now everybody think "another one making minecraft crap". But I want some more things in it. All that with a nice GUI unlike other clones.

[quote]Writing the core logic in lua is a *really bad* idea.[/quote]
Yeah, I thought that too, but not that it is too bad.

[quote]You will need to have groups of blocks share a single mesh (or maybe all blocks in the world share a single mesh).[/quote]
I wanted to do that, but later I saw that this is not possible in Lua only. So I thought more about resizing these cubes.

[quote]It is that you are drawing the terrain of the world in one of the least efficient was you could.[/quote]
When the table is created, there is nothing in there except integers. So there are no objects created yet. Just a black background. The table is created and is in the memory. Then I have around 30 FPS. When I empty the table, it jumps up to 180+ FPS. In each frame update (except for the very first update), there is nothing in the Lua code that does use the table, only if a specified key is pressed.
My Idea was to reuse these chunks. So if the player moves forward, the last chunks very behind of the player are moved to the front where new chunks are required.
Nevermind, I'll do something different, getting inspired by that link you gave me.
I'm still new to that 3D stuff.
Thanks!

-------------------------

cadaver | 2017-01-02 01:04:41 UTC | #4

This may be the same or similar slowdown as discussed in [github.com/urho3d/Urho3D/issues/649](https://github.com/urho3d/Urho3D/issues/649)

Basically, the LuaScript subsystem runs the GC on each frame. When you have large tables (or even the GC's table itself) significant amount of time can be taken just by the GC going through them, looking for objects to delete.

One option is to switch to AngelScript. In AngelScript we have disabled GC and only rely on reference counting.

-------------------------

Autian | 2017-01-02 01:04:41 UTC | #5

I did also some experiments before. Creating objects and then removing them properly. (also checked the exported xml, where all objects are shown, the objects are removed properly but the counter, shown in the code below, is very high)
[i.imgur.com/Mzm7j9N.png](http://i.imgur.com/Mzm7j9N.png)
(don't look at the size of the swap :smiley: I set it way too high)
Part of scene.xml:
[code]	<attribute name="Next Local Node ID" value="16777216" />
	<attribute name="Next Local Component ID" value="16777216" />[/code]
complete scene:
[code]<?xml version="1.0"?>
<scene id="1">
	<attribute name="Name" value="" />
	<attribute name="Time Scale" value="0.1" />
	<attribute name="Smoothing Constant" value="50" />
	<attribute name="Snap Threshold" value="5" />
	<attribute name="Elapsed Time" value="0" />
	<attribute name="Next Replicated Node ID" value="4" />
	<attribute name="Next Replicated Component ID" value="4" />
	<attribute name="Next Local Node ID" value="16777216" />
	<attribute name="Next Local Component ID" value="16777216" />
	<attribute name="Variables" />
	<attribute name="Variable Names" value="" />
	<component type="Octree" id="1" />
	<node id="2">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Zone" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="Zone" id="2">
			<attribute name="Bounding Box Min" value="-1000 -1000 -1000" />
			<attribute name="Bounding Box Max" value="1000 1000 1000" />
			<attribute name="Ambient Color" value="0.15 0.15 0.15 1" />
			<attribute name="Fog Start" value="500" />
			<attribute name="Fog End" value="750" />
		</component>
	</node>
	<node id="3">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="DirectionalLight" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="0.884784 0.399593 0.239756 -0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="Light" id="3">
			<attribute name="Light Type" value="Directional" />
			<attribute name="Color" value="1.2 1.2 1.2 1" />
			<attribute name="Specular Intensity" value="0.5" />
			<attribute name="Cast Shadows" value="true" />
			<attribute name="CSM Splits" value="10 50 200 0" />
			<attribute name="Depth Constant Bias" value="0.00025" />
		</component>
	</node>
</scene>[/code]
That memory usage increase is interesting. Also I think that when creating a new node/component, the new smallest possible ID that the node/component gets should be found first if it is wished. (or this feature exists already but I may not found it)

-------------------------

cadaver | 2017-01-02 01:04:42 UTC | #6

The node ID's have nothing to do with memory use. Smaller ID's are not reused to avoid possible mismatches in network replication. 16777216 is the first local (non-replicated) ID number.

-------------------------

