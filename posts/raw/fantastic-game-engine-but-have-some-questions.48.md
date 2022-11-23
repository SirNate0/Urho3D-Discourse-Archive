Jace | 2017-01-02 00:57:35 UTC | #1

Hello my fellow Urho3D users :slight_smile: 

First let me give a huge thanks to all the developers who have donated their time and hard work to create this magnificent game engine.

I've been keeping up with the progress of Urho3D for a few months now and I am very impressed. It literally is the most complete open source c++ game engine out there with a viable and realistic license (in my opinion). All the other actual free C++ based engines I've encountered are very fragmented and missing most of the functionality Urho3D has. They also require the user to hunt down many libraries and implement them themselves, making these engines nearly out of the question for all novice programmers. Then we have the commercial alternatives. Almost all of these have heavily crippled free versions and do not allow any source access unless you pay an insane amount of funds which is virtually impossible for indi devs who aren't millionaires. So there you have it; could Urho3D possibly be the greatest indi game engine of all time? I sure think so!

I have all but decided to use this engine for a serious game project I've been conceptualizing for over a year now. I'd also love to contribute whatever improvements I make to help further the cause of Urho3D which I think seems to be making an actual complete, multi-platform game engine of commercial quality that doesn't have an overly restrictive viral license available to the public for the first time (correct me if I'm wrong here but I really don't think there is anything even close to comparable out there at the moment).  The engine looks nearly perfect for my indi game endeavor but I have a few quick questions regarding the engine's core structure/api for the devs.

[b]1.[/b]
Would it be feasible (not insanely difficult) to create an in-game level editing system in c++ by using the same calls made to the angel script editor within the Urho3D player?
 Does the engine's code structure allow for this or would it simply be out of the question?  I'm asking because my second engine choice was actually Cube 2(aka Sauerbraten) or the improved version known as "Tesseract" which has one of the best level editing systems I've seen in any game/engine, not just open source. I'd even  considered porting some of it's functionality over to Urho3d as they both have a very permissive license

[b]2. [/b]
Can the engine be compiled with LUA only  and exclude the angelscript library/add-on since I do not intend to use angel script?

[b]3. [/b]
Is the networking system currently fully integrated with all the supported platforms?

The last two are both requests and questions I suppose. 

[b]4. [/b]
Now that asm.js can run at only 1.5x slower than native code (as of 12-21-13) will the devs consider targeting browsers as a viable platform using emscripten, which I'm sure most are aware is capable of compiling c++ code  and even open gl es   2.0 graphic programming straight to  javascript with little to no modification/cleanup required in the code. Epic games has made full use of this and now there is even an actual full fledged commercial 
released  called "Monster Madness" that uses this technology. It's also worth pointing out that the entire LUA vm has already been fully compiled to java script using emscripten and runs at near native speed.    

[b]5.[/b]
 Do you plan to implement support for Oculus Rift VR in the future?

Thank you very much,
Jace

-------------------------

weitjong | 2017-01-02 00:57:35 UTC | #2

Welcome to our new forum.

I decided to stick around with Urho3D after observing how stable it is compared to Ogre3D and after learning how clean the source codes are compared with others. It turns out to be a good decision for me.

Allow me to answer some of your questions.
[ol]
[li] I think it should be possible. If I recall correctly I have seen comment or commit log somewhere that indicates the Editor was once written in native C++ language before being rewritten using AngelScript (Lasse would know better). Although it was quite sometime ago before Editor acquires much of improvements recently. The underlying interfaces being used by the Editor scripts via AngelScript API are available also in native C++, so I would say it is feasible. Having said that, I know at least one construct in the Editor scripts that uses AngelScript special features like "funcdef" (it is almost like a closure but not quite the same) for implementing menu callbacks. You will have to replace those AngelScript special constructs in C++.[/li]
[li] Yes, it can. Both AngelScript and Lua subsystems can be enabled or disabled using their respective build option. The difference is only AngelScript subsystem is enabled by default. Note that you can also enable both at the same time (just for testing).[/li]
[li] I believe so, it works on all the supported desktop platforms. For mobile platforms, I am not sure it is possible though.[/li]
[li] There is already a discussion on this specific topic on our old forum. [groups.google.com/forum/#!searc ... d7OCNfcKgJ](https://groups.google.com/forum/#!searchin/urho3d/emscripten/urho3d/K05m3Y795gU/8ad7OCNfcKgJ). There is no update since then.[/li][/ol]

-------------------------

Mike | 2017-01-02 00:57:35 UTC | #3

For question #2, you have to build using the -DENABLE_ANGELSCRIPT=0 option.
See [url]http://urho3d.github.io/documentation/a00001.html[/url] for references.

-------------------------

Jace | 2017-01-02 00:57:35 UTC | #4

Thank you for the prompt responses guys, very much appreciated.  Your answers are quite auspicious.

I'm glad to know that an in game editor is doable. I'll have to take a look at those constructs; I'm hoping it won't be too difficult to port to lua or c++ and all I have to worry about is making my gui.
Also, full networking support huh; that is terrific.

About emiscripten, I see it doesn't support sdl2 yet. I guess until Mozilla implement the ability to compile SDL2 code to javascript it isn't very practical for any SDL2 based engines. I may try stripping Urho3D down to a bare minimum and just use GLES 2.0 code to see if I can get it to compile over. I know the author of emscripten successfully converted the entire cube2 engine but that used the old SDL standard that came before 2.

Mike, I actually do remember seeing that compile flag before but I wasn't sure if it still existed or rather how tightly integrated angel script had become in the engine since then.
I'm very relieved to hear it isn't mandatory. I have to say I love the fact that Urho3D is so modular. 

I am pleased to announce that I've chosen Urho3D for my game and will gladly make any useful contributions I can.
Now let's not let Unity buy us out eh? I think Urho3d is likely to become what Blender 3D of open source game engines, in other words the best option available, well, at least if it keeps going in the direction it is now.

-------------------------

Azalrion | 2017-01-02 00:57:35 UTC | #5

[quote]The underlying interfaces being used by the Editor scripts via AngelScript API are available also in native C++, so I would say it is feasible. Having said that, I know at least one construct in the Editor scripts that uses AngelScript special features like "funcdef" (it is almost like a closure but not quite the same) for implementing menu callbacks. You will have to replace those AngelScript special constructs in C++.[/quote]

Could be a case there for writing Callback functionality for the C++ side of Urho, although C++11 semantics using function and bind pretty much provide that already.

-------------------------

cadaver | 2017-01-02 00:57:35 UTC | #6

Hi and welcome from me as well.

About the networking: the mobile platforms also support BSD sockets so technically the networking compiles in and should work, but I've not tested it in a real-world scenario. The problem with the networking is that it implements a very generic sync of attributes, where the server is 100% authoritative and performs the players' move logic, so there will be lag felt on the client machines. Client prediction would need the ability to "rewind" the player, but as all current examples do player movement with general rigidbody physics, it's hard to do. So what I'm saying is that networking will likely need game-specific modifications to be truly usable.

About emscripten: the way to go would be to leave the actual SDL2 library out of the compilation and see how much the SDL calls need to be modified to be compatible with emscripten's implementation.

Btw. it was NinjaSnowWar which originally had a C++ implementation, it was long ago when the scripting was not there at all. The editor (in script) was started after creating the initial AngelScript bindings. It was only few months after that, in spring of 2011, when I rewrote almost the entire codebase to become V1.1 which is the base of things up to today :wink:

-------------------------

weitjong | 2017-01-02 00:57:36 UTC | #7

[quote="cadaver"]Btw. it was NinjaSnowWar which originally had a C++ implementation, it was long ago when the scripting was not there at all. The editor (in script) was started after creating the initial AngelScript bindings. It was only few months after that, in spring of 2011, when I rewrote almost the entire codebase to become V1.1 which is the base of things up to today :wink:[/quote]

Thanks for the correction. So it was the NinjaSnowWar, not Editor  :laughing:.

-------------------------

Jace | 2017-01-02 00:57:37 UTC | #8

[quote="cadaver"]Hi and welcome from me as well.

About the networking: the mobile platforms also support BSD sockets so technically the networking compiles in and should work, but I've not tested it in a real-world scenario. The problem with the networking is that it implements a very generic sync of attributes, where the server is 100% authoritative and performs the players' move logic, so there will be lag felt on the client machines. Client prediction would need the ability to "rewind" the player, but as all current examples do player movement with general rigidbody physics, it's hard to do. So what I'm saying is that networking will likely need game-specific modifications to be truly usable.

About emscripten: the way to go would be to leave the actual SDL2 library out of the compilation and see how much the SDL calls need to be modified to be compatible with emscripten's implementation.

Btw. it was NinjaSnowWar which originally had a C++ implementation, it was long ago when the scripting was not there at all. The editor (in script) was started after creating the initial AngelScript bindings. It was only few months after that, in spring of 2011, when I rewrote almost the entire codebase to become V1.1 which is the base of things up to today :wink:[/quote]

I see, so no client-side prediction code is contained in the Urho3D networking library as of yet; that is unfortunate. If only Urho3D used enet instead of knet, then I could just cnp some prediction code from Tesseract and replace Tesseract physics with bullet  :smiling_imp: 

However, in light of this I think what I may end up doing is using some combination of both Urho3D and the Tesseract engine to achieve my goals. Implementing highly complex player prediction algorithms is a little bit beyond my ability (currently  :wink: ) and the scope of what I want to do to create a prototype for my game,though, I suppose I could figure it out eventually after studying the prediction code in some other engines beforehand.  

Regarding the editor functions, It shouldn't be a problem to call them from within the Urho3D player (in game) if I use the original c++ code the angel script bindings are calling into right?

-------------------------

Azalrion | 2017-01-02 00:57:37 UTC | #9

[quote]Regarding the editor functions, It shouldn't be a problem to call them from within the Urho3D player (in game) if I use the original c++ code the angel script bindings are calling into right?[/quote]

Not at all, thats how you go about using urho when not fully depending on the scripting languages. There are some changes though because the angelscript bindings need a slight work around but thats mostly to do with being able to listen to events and other aspects that need access to the context, just derive your control classes from Object and you'll have access to what you need.

-------------------------

GIMB4L | 2017-01-02 00:57:37 UTC | #10

No one has addressed the fifth point, and I'd like to take a crack at it.

I have experience developing for the Oculus Rift, not just through unity but also in C++. I'd like to take a crack at implementing this in the core of the engine as a component.

-------------------------

Jace | 2017-01-02 00:57:37 UTC | #11

[quote="GIMB4L"]No one has addressed the fifth point, and I'd like to take a crack at it.

I have experience developing for the Oculus Rift, not just through unity but also in C++. I'd like to take a crack at implementing this in the core of the engine as a component.[/quote]

I'm sure many would appreciate this; an announcement that support for it was being implemented would probably garner Urho3D a lot more popularity due to the fact that there aren't really many FOS engines out there besides Tesseract and Torque3D supporting it. Neither of those engines are multi-platform either, but there is work being done by one guy to get Torque3D compiled for the other platforms with crowd funding. Torque3D appears to be the only real competitor Urho3D has.

Since both of the other aforementioned engines have full support for Occuls VR already and use the Sdl2 for graphics (wip linux port of Torque3D only) it would probably make things a lot easier to see how they implemented it. Actually, you may even be able to get some compensation for your time and work by starting a donation Paypal. Torque3D seems to be gaining a lot of new functionality that way so why not Urho3D as well? I guess the core devs would have to approve something like that, though, as I don't know how they stand on donations since there really isn't any info about it on the site that I could see.

Back to the subject of networking, by looking at the classes it seems the Knet library is very tightly integrated with the scene system of Urho3D. I had hoped it would be less difficult to use an alternative network library in the engine but that 
definitely doesn't seem to be the case :frowning: I guess the only viable option for someone who has no prior experience with network programming is to compare the api of knet and the api of the network library used by the engine that supports client prediction and then try and remap that prediction code over to knet. What have I gotten myself into  :astonished:

- Edit - 
Thought I might as well post a [url=http://www.garagegames.com/community/blog/view/22557/2#comments]link[/url] to that post about Torque3D receiving full multi-platform support. It seems Torque3D may be trying to steal the show for best FOS game engine :laughing:

@ GIMB4L
And [url=http://svn.tuxfamily.org/viewvc.cgi/tesseract_main/src/engine/ovr.cpp?revision=1126&view=markup]here's[/url] a link to the OVR code contained in Tesseract in case you do want to see it.

-------------------------

cadaver | 2017-01-02 00:57:38 UTC | #12

The kNet library is just used for raw transport of messages that are either reliable or unreliable, which is quite the same for what eNet would be used.

For example, you could implement a Quake3-like protocol just as well with kNet, but Urho consciously avoids that currently, because the Quake3 model needs more processing power & memory on the server for each client, as you're basically storing each state you've sent to each client so that you know what kind of delta to send next (and erase the states as acks arrive from clients.)

Instead, we have basically 2 categories of attributes sent in a way that tracking client's "last acked state" is unnecessary:
- Reliable attributes. These are things which rarely change, for example model's material refs
- Latest data attributes (transform, rigidbody velocities, animation state). These are sent as unreliable and old values don't matter to the client. For these we use kNet's "content ID" feature so we know, on both server & client, to discard old messages that either weren't sent yet, or arrived out of order.

The first step for supporting prediction would be to add a frame number to the client controls message, and server sending the "last seen client's framenumber" back to the client. From this it would know what inputs it would need to replay and estimate the latency.

On the subject of donations: Urho3D project does not generate costs just by existing, so that would mean donations would go toward development. And I'm not sure that would be a good idea. Our license says "the software is provided 'as is' without warranty of any kind..." and if we were taking money, that shouldn't / couldn't be strictly true any more, and could open up possibilities of ugly situations. In my personal opinion the most precious resource in Urho development is available time, of which there isn't enough. :wink:

-------------------------

