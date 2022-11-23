JTippetts | 2017-01-02 01:03:05 UTC | #1

I've been working on a [url=http://discourse.urho3d.io/t/terrain-editor/765/1]terrain editor[/url] in my spare time, and I've been noticing a bit of a performance snag. I've implemented the ability to script certain filters that can modify the heightmap or the blend texture, including filters to randomly locate terrain blending based on noise fractals, filters to place roads etc... But I have noticed that the more I use filters that modify the blend map, the worse my performance degrades. For example, when I first start the application, I get decent performance: [url=http://i.imgur.com/XFJi03P.jpg]screenshot[/url].

When I run a [url=https://github.com/JTippetts/U3DTerrainEditor/blob/master/Bin/TerrainEditFilters/dirtgrass.lua]fractal filter[/url] that iterates the blend image and sets the pixels of the blend, then calls [b]blendtex:SetData(blend)[/b] to upload the edited texture, the framerate drops noticeably: [url=http://i.imgur.com/EoXEHwY.jpg]screenshot[/url]. Doing further operations such as building an elevation map and adding a road drop it even further: [url=http://i.imgur.com/9XJOUDy.jpg]screenshot[/url]. (Note that the heightmap, while it has a miniscule effect, is nowhere near as drastic as modifying the blend map.) If I quicksave the heightmap and blendmap, exit the application and restart, then load the quicksaves, I get a lot of performance back: [url=http://i.imgur.com/6E4E6H0.jpg]screenshot[/url].

So I'm wondering if I'm handling the process of modifying and updating the blend texture sub-optimally. My standard technique is to modify the texture, or part of a texture, directly into the image then upload the image via Texture2D::SetData(). But I wonder if I somehow miss a crucial step, perhaps related to detail levels or to discarding old texture data or something of that nature.

Possibly related, when I create the texture for the blend map I initially call SetSize(0,0,0,TEXTURE_DYNAMIC) in order to specify dynamic usage, as I did not see anywhere to specify the usage otherwise. However, according to the comments, using sizes of 0 causes the texture size to follow the application window size. Then, when SetData is called, the texture is resized again.

I am using a 64-bit Mingw-w64 build with LuaJIT and Direct3D.

-------------------------

cadaver | 2017-01-02 01:03:05 UTC | #2

Looking at the profiling blocks it doesn't seem like anything in Urho's native view update & rendering is slowing down, but there's something outside it that is taking a huge chunk of time. Maybe Lua garbage collection?

-------------------------

JTippetts | 2017-01-02 01:03:05 UTC | #3

I thought it might be the garbage collector, but inserting a [b]collectgarbage()[/b] call for a full gc cycle at the end of the filter doesn't help. However, after you pointed out that it doesn't seem to be in the render code, I started to dig deeper. I've built a dummy filter as a minimal example that demonstrates the slowdown:

[code]
return
{
	name="Dummy Loop",
	description="Create a mottled dirt/grass terrain.",
	options=
	{
		{name="Frequency", type="value", value=8},
		{name="Num Octaves", type="value", value=6},
		{name="Gain", type="value", value=0.8},
		{name="Seed", type="value", value=12345},
		{name="Use Mask?", type="flag", value=false},
	},
	
	execute=function(self)
		local hw,hh=blend:GetWidth(),blend:GetHeight()
		local x,y
		
		for x=0,hw-1,1 do
			for y=0,hh-1,1 do
				local nx=x/hw
				local ny=y/hh
				local val=0.5
				local col=Color(1,0,0,0):Lerp(Color(0,1,0,0), val)
			end
		end
		collectgarbage()
	end,
}
[/code]

Given that all of the texture manipulation stuff is stripped out, the error is definitely not in the texture stuff. This minimal example makes me believe that it does, in fact, lie in how Lua generates and collects garbage, specifically user data such as Color. The newly-added call to collectgarbage() should execute a full GC cycle, but has zero effect on the issue.

For clarification, the slowdown is not a temporary condition. It doesn't go slow for a few seconds or minutes until some internal state has caught up; it slows down for the entire further duration of the program. ie, it never catches up. When the degradation is extreme (such as after I execute a terrain filter followed by a road filter, or if I do numerous executions of the minimal example) the application becomes quite nearly unusable, with very exaggerated input delay.

Now, when I execute the above minimal example, the execution time is about 4 seconds, after which the frame count drops from 100 to 17 and stays there. However, if I remove the line that interpolates colors, then the execution time becomes nearly instantaneous, and no permanent slowdown is observed after execution. If I change the filter so that no Color garbage is generated in the inner loop:

[code]
for x=0,hw-1,1 do
			for y=0,hh-1,1 do
				local nx=x/hw
				local ny=y/hh
				local val=0.5
				--local col=c1:Lerp(c2, val)
				c3.r=c1.r+val*(c2.r-c1.r)
				c3.g=c1.g+val*(c2.g-c1.g)
				c3.b=c1.b+val*(c2.b-c1.b)
				c3.a=c1.a+val*(c2.a-c1.a)
			end
		end
		collectgarbage()
[/code]

Then the permanent slowdown is also eliminated.

I find this... odd. Admittedly, though I use Lua a lot, I am no expert on its internals. But the problem seems to be a result of a lot of locally-generated Color garbage and the collectgarbage() call effectively does nothing to ameliorate it.

-------------------------

JTippetts | 2017-01-02 01:03:07 UTC | #4

I'm wondering if there is a problem with how tolua garbage collection works. I created a filter script that all it does is loop 1000000 times and create a local Color() value. Using collectgarbage("count") to display used memory, I get a used mem count of 2437 before the loop and 27692 after the loop. However, calling collectgarbage() for a full gc cycle then displaying the used mem count again I get 22434, meaning that a whole lot of those locals that were created inside the loop are not being garbage collected. Continuous reporting of used memory shows that the used memory is never freed up, regardless of garbage collection. This results in an ever increasing amount of garbage that never gets taken out.

This test triggered a little bit of a memory for me. I haven't worked on my game project in many months, but I remembered having performance issues with it and having a general unwillingness to try to deal with it helped me to stop working on it. So I went back and did some memory tracking, and it looks like I am getting gradually accumulating garbage there that never gets collected either. Not in chunks as large as a loop iterating on a 1024x1024 image generates, but over time it adds up. I think this gc problem might be the root cause of the slowdown.

I've spent quite a few hours googling for potential leaks and problems with tolua++, but I don't really find much outside of some old unanswered posts on various forums and one discussion back in 2001 regarding earlier versions of Lua and tolua being unable to collect userdata objects returned by value, but nothing recent. I think that tolua++'s growing obsolescence might be starting to catch up to it, at least so far as lack of internet discussion about it goes.

At this point, I'm kind of stymied. I could possibly switch over to AngelScript, but that doesn't really solve the long term problem I have regarding my poor, neglected game. Guess I'll do some more digging into the source code to see if I can figure out what's going on.

-------------------------

cadaver | 2017-01-02 01:03:07 UTC | #5

You can also log an issue to raise awareness of this problem. Either it's a bug within tolua or we're somehow using / exposing the value-type classes incorrectly.

EDIT: searched a bit on gamedev.net, one possibility is that our Lua function calls executed from C++ side are not restoring the stack position, leading Lua to believe everything created inside the function is still in use.

EDIT 2: doesn't look to be that, as creating ordinary float value garbage *is* cleaned up correctly.

-------------------------

JTippetts | 2017-01-02 01:03:07 UTC | #6

I feel a little bit like Ouroboros on this, because I'm certain this is something I've tackled in the past. Side effect of going for months or years between programming binges is that you forget a lot of stuff and end up retreading old ground.

The local version of Color:new looks like this (with the conditional compilation stuff for non-release builds removed for clarity):

[code]
static int tolua_MathLuaAPI_Color_new00_local(lua_State* tolua_S)
{
 Color* tolua_ret = (Color*)  Mtolua_new((Color)());
 tolua_pushusertype(tolua_S,(void*)tolua_ret,"Color");
 tolua_register_gc(tolua_S,lua_gettop(tolua_S));
 return 1;
}
[/code]

I believe this is the one called when performing a statement as [b]local c=Color(1,1,1,1)[/b]. So I'm not certain that it's necessarily anything that we are doing wrong. The color is allocated, registered with tolua's garbage collector, and pushed onto the stack. On Lua side, obtaining the userdata and storing it in a local does the appropriate stack popping. When I get back from grocery shopping, though, I'm going to start tracing things more exactly to see if I can figure this out.

-------------------------

cadaver | 2017-01-02 01:03:07 UTC | #7

I made a stupid test in 04_StaticScene.lua where it generates a large number of Color objects each frame you keep the W key pressed. The observation was that it does collect (delete) the color objects, but creating a very large number of them (100000+) in one frame results in a permanent slowdown. It's as if it leaves the table (?) that held the objects permanently large even after deleting them, so on subsequent frames the GC walks through a large empty table, incurring a performance loss. This is probably a tolua++ architectural issue.

-------------------------

OvermindDL1 | 2017-01-02 01:03:15 UTC | #8

What were the reasons why luajit are not used exclusively compared to including lua?  Luajit's ffi interfaces handle these things far better, as well as the binding code is on the lua side.  Even if the JIT part is not used the normal execution (for iOS or so forth) is still of decent speed and the ffi bindings are still far far better to use than the C bindings.

Perhaps instead of luajit just being a subpart of the lua build, maybe it would be better to have it be a whole ScriptLuajit system so it could be used with the full ffi interfaces and other features, which would supply substantial performance benefits when the JIT is enabled compared to using the exceedingly slow lua C binding layer.

-------------------------

weitjong | 2017-01-02 01:03:16 UTC | #9

Completely agree with all you said above about FFI. I think most of us know that already. The question is, will someone come forward to rewrite the binding and contribute it?

-------------------------

OvermindDL1 | 2017-01-02 01:03:17 UTC | #10

[quote="weitjong"]Completely agree with all you said above about FFI. I think most of us know that already. The question is, will someone come forward to rewrite the binding and contribute it?[/quote]
I would in a heartbeat if I had time, I have done so a few times in the past on fairly large systems.  If I get time in the future and it remains undone then I might.  With the FFI binding layer and some well made wrappers you could fix all of the shared pointer issues that the current lua bindings have as well.

-------------------------

