GoldenThumbs | 2018-12-10 23:17:23 UTC | #1

Anyone have a C++ explanation/tutorial/whatever else for someone like me who is an artist that pretty much only knows very basic C# and Angel Script? I want to do some VERY minor mods to the engine and in order to do that I need to be able to understand what it is I'm doing.

-------------------------

Sinoid | 2018-12-11 00:13:27 UTC | #2

It's like C# with `unsafe` 100% of the time. You'll need to get used to having to use both `.` and `->` depending on how something was allocated and depending on what you're working with. Access control (protected private) is *sticky* instead of attached to each declaration and you've now got the joy of header files.

If you're using a new version of VS with the type search (default CTRL+T) that super helpful to new people and people new to a project - lets you easily track anything down by name.

What are the minor mods you're looking to do?

-------------------------

GoldenThumbs | 2018-12-11 00:43:58 UTC | #3

Not sure it really counts as a modification, but I'm wanting to make a character controller component and also add Ambient Occlusion to the renderer (pretty sure that would really be a shader though).

-------------------------

GoldenThumbs | 2018-12-11 00:44:59 UTC | #4

I've made an angel script character controller but I want to see if I can do it with C++ and make something more streamlined.

-------------------------

Sinoid | 2018-12-11 01:09:08 UTC | #5

> I’ve made an angel script character controller but I want to see if I can do it with C++ and make something more streamlined.

There are also C++ examples that are mostly all implemented to match the general structure of the angelscript/lua examples. Those should be useful for you to be able to reference what something in angelscript looks like in C++ for first porting (then improving) your AS controller to C++.

I believe there's a version of the NinjaSnowWar demo rewritten in C++ floating around somewhere that you might be able to track down, that should be similar to the examples as well.

**Edit:** [Ninja snow war C++ is over in this thread](https://discourse.urho3d.io/t/ninja-snow-war-c-version/2729), it does look to be a little behind the times though.

Unfortunately you have to pretty much just muscle through, read a few C++ crash courses (if you can find any you can stand to read, most I've seen are terrible), and ask when you're jammed up.

> add Ambient Occlusion to the renderer (pretty sure that would really be a shader though).

Yes, that's a shader (unless wanting bent-normals from vertex data - not likely you want that though).

-------------------------

