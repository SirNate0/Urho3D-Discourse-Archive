Sehlit | 2018-05-23 14:28:02 UTC | #1

Hello.

I'm considering using Urho for moibile games, they are simple 2d games and I don't need physics or network, just basic input/sounds/sprites, can i strip out the features I don't need and if I do what's the expected APK size for a hello world application?

Thank you al help is appreciated.

-------------------------

S.L.C | 2018-05-23 14:41:18 UTC | #2

Yes, you can disable what you don't need. That is perfectly safe.

What takes a bunch of memory is and will always be the scripting components. Lua for example has to generate wrappers for every exposed API and AngelScript also has to generate a ton of function calls for registering the API.

Second would be disabling the Database component if you don't need it. No reason to include SQLite or ODBC(?) into your code if you don't need it. Followed by the web-server if you don't need that too.

IK component can also be disabled since I'm guessing you won't be using that either.

The NavigationSystem can probably be disabled too if you don't need it.

Not sure if the WebP image library can be disabled if you can live with just the standard DDS/PNG/JPEG/BMP/PSD etc. formats. I'll have to look into that to say for sure.

Network and Physics can probably be disabled too without any effects. The network can definitely be disabled if you don't need it.

Not sure if the 3D physics can be omitted if you only need 2D scene and physics. A more experienced used 
can tell you that for sure. Or how it can be achieved. I only know you can omit the 2D component entirely.

Disabling most of these can significantly reduce the size of your executable. Especially the script components.

-------------------------

Sehlit | 2018-05-23 15:08:23 UTC | #3

Thank you for your detailed reply.

I'm going to use C++ directly so I don't need the script interpretors too. When you say i can *disable* what i don't need is that done on cmake or something like that?
Also, yeah i don't need physics not even 2D so i could disable that too.

Do you have however any rough idea on the apk size after disabling all of that? I ask because the apk size for unreal engine is like hundred MBs while unity about 10MB so that varies a lot

-------------------------

Eugene | 2018-05-23 15:07:53 UTC | #4

[quote="Sehlit, post:3, topic:4258"]
When you say i can *disable* what i don’t need is that done on cmake or something like that?
[/quote]
Just open generated Urho3D build folder with CMake GUI, go through items and disable whatever you don't need.

-------------------------

S.L.C | 2018-05-23 16:15:06 UTC | #5

I have not created any APK so far. So I can't say for sure how large it would be. But if I hope it to be close an x86 executable, then it should be roughly the same as Unity. Excluding any game resources, like textures/models/sounds etc.

As for disabling 2D physics. I haven't looked whether you can. I can only remember you can disabled the whole 2D subsystem.

-------------------------

SirNate0 | 2018-05-24 02:41:24 UTC | #6

From playing around with it about a year ago, without stripping out all of the extra things, I ended up with a debug apk of about 40 MB, but almost all of that was from ~50MB of assets -- the actual .so that is the built game is about 10 MB uncompressed. Since I did not strip out all of the extra features, and I'm pretty sure the library is a debug build, I'd say you're looking at something a decent amount smaller, though you'll probably need to go ahead and build it to find out, unless someone with more experience with it than I have can help.

-------------------------

johnnycable | 2018-05-24 08:40:16 UTC | #7

It's 35,8 Mb on my morning build for armeabi-v7a in debug mode, without scripting (I don't use that) and without assets of any kind. All the rest included.
I cannot tell you about release right now, my build facility is not configured for that. But you can figure it will be lower, of course.
HTH

-------------------------

