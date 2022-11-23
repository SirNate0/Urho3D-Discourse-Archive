Miegamicis | 2020-05-22 18:56:17 UTC | #1

For the past few months have kept myself busy working with the Urho's web port. One thing that bothered me alot was the lack of networking in the web builds. With that being said today I'm proud to present to you my proof-of-concept for the networking in the web builds.

I've tried to implement https://github.com/HumbleNet/humblenet/ library in the way that it was supposed to be implemented. Sadly it didn't quite work that well and the networking was usable on half of the computers that we tested (thanks to other members in the community!). So I had to get rid of WebRTC support and do a plain server-client implementation using websockets. 

HumbleNet already has built in support for websockets, but not in the way that is needed for true server-client mode. So I did quite few hacks here and there, bunch of workarounds, bad code practices etc. 

So with that all being said here's the actual demo of if: 
https://playground-sample.frameskippers.com/

Everything that you see in the game is controlled by the server, you will see the replicated state of it.

Just open the link, press "New Game" and click on the "Flatland" image to start the sample. Sample is based on this project: https://github.com/ArnisLielturks/Urho3D-Project-Template

If you notice any problems or crashes (or typos), please provide the stack trace from the dev console so I could keep improving it and hopefully make a PR to make it a part of the engine.

The codebase with the HumbleNet implementation will be shared a bit later, have to make it MIT friendly first since the new networking library depends on a lot of other stuff.

-------------------------

Miegamicis | 2020-05-22 18:57:18 UTC | #2

Also if the server crashes for some weird reason it should restart in few seconds so you could keep checking it out!

-------------------------

George1 | 2020-05-23 02:55:38 UTC | #3

In the example, the camera is not mounted on the ball.

-------------------------

Miegamicis | 2020-05-23 04:34:06 UTC | #4

Got it. There's only 1 attempt to mount the camera, might need to improve it since it could happen when the initial scene state loads a bit slower from the server.

-------------------------

dertom | 2020-05-23 09:52:21 UTC | #5

Wow, very cool! Good job :+1:

Edit: If you need more people for testing or such, count me in.

-------------------------

George1 | 2020-05-23 15:16:39 UTC | #6

I'm not sure if the graphic options have been enable yet.  
e.g. SSAO option shown a black screen.

-------------------------

johnnycable | 2020-05-23 15:34:04 UTC | #7

Works pretty well.

![Screenshot 2020-05-23 at 17.29.29|690x394](upload://81gWXthEIZZIEN1tVgyFZguWjKA.png) 

Everything is snappy and fluid. No hiccups.
Tried it on my mac both Chrome and Safari. Only strange thing I saw is on Safari, you cannot look around 360°; when mouse pointer hits the left/right screen border, look around stops, limiting the view.
Really good job. Networking on web always been a sore point in Urho.

-------------------------

Miegamicis | 2020-05-23 16:03:08 UTC | #8

I haven't got to that yet, but some options are not really ment for the web and other platforms. Will disable them in the future to avoid confusion.

-------------------------

Miegamicis | 2020-05-23 16:03:51 UTC | #9

That's a know bug in my latest emscripten shell implementation, plan to fix that in the upcomming weeks.

-------------------------

Rook | 2020-05-24 07:08:18 UTC | #10

Nice work. The only things I noticed were the following: -
System: i7920, GTX 750ti, 6Gb RAM, Ubuntu 20.04, Firefox

1) F2 did not activate a console
2) SSAO mode in graphics options opens a grey screen
3) The mouse does not fully rotate the camera about the ball
4) When the mouse is captured there is no cursor on screen even when a UI is displayed
5) When moving back to the menu from a game after switching to fullscreen, I needed to press escape which escaped fullscreen too there after the GUI even when reentering fullscreen was partially off screen.
6) While I 'think' there was some shadowing in objects there was none on the ground making it difficult to assess whether any options were working.

Hope this helps, good luck.

-------------------------

Miegamicis | 2020-05-24 21:58:13 UTC | #11

Thanks for the feedback!

1. Have a typo there, console opens with F1
2. SSAO doesn't work in web and probably never will
3. Mouse pointer issues might be fixed in the latest release, just did a patch and submitted a PR with fixes

Regarding the lighthing I just remembered that all the scenes use ambient light. You can tweak the values in console by typing 
`ambient_light 0 0 0`

-------------------------

Rook | 2020-06-01 20:46:02 UTC | #12

The showing of the mouse pointer does appear to be correct now however it still does not capture the mouse in windowed mode and when the menu is called fullscreen is still exited thereafter even upon returning to fullscreen the mouse will not fully rotate the ball.

Regards.

-------------------------

yiown | 2020-09-02 09:16:57 UTC | #13

Just a heads up, the link https://playground-sample.frameskippers.com/ is not working anymore.

Having humblenet would be nice but overkill.
I just need raw websockets, like simple "em++ -lwebsocket.js" how can I do this in Urho3D ?!

-------------------------

Miegamicis | 2020-09-02 09:55:02 UTC | #14

> Just a heads up, the link https://playground-sample.frameskippers.com/ is not working anymore.
> Having humblenet would be nice but overkill.
> I just need raw websockets, like simple “em++ -lwebsocket.js” how can I do this in Urho3D ?!

Sample was moved here: https://playground-sample.arnis.dev/
But seems like I forgot to update the server url which is used to actually connect to the server, will update it sometime this week.

---

I would say that the easiest way to use websockets would be trough C++ <--> JS bindings since the network library currently used by Urho does not have emscripten port. But that would mean that you would not be able to code the actual server inside Urho without heavy modification.

My unpolished Humblenet integration can be found here: https://github.com/ArnisLielturks/Urho3D-Humblenet-Integration - it has 2 branches:
1. master - the hublenet integration as it's meant to be used
2. websockets-only - which is heavily modified humblenet library to allow direct server-client connections using websockets and does not require you to set up humblenets peer-server

Web networking is still a WIP and I'm still trying to figure out the best solution to make it a reality.

-------------------------

yiown | 2020-09-02 18:57:59 UTC | #15

Amazing !!! thanks for the quick reply !

In a normal scenario we will use Urho3D for the client side game rendering and interactions, taking advantage of a single code base being deployed to multiple platforms, where "web" will be the most usable one (i.e. no installation required).
So the server part is not needed in Urho3D. Actually, most games and applications would have a cloud headless processing unit, dispensing world updates to the connected clients, probably implemented in slender and fast "C++, bullet, linux" solutions.
So, the only missing component to be able to use Urho3D, is a working raw websocket connection. Much like the MakeHttpRequest() we finally have.

Do you think this could be quickly added to the engine ?

-------------------------

Miegamicis | 2020-09-03 13:28:31 UTC | #17

> Do you think this could be quickly added to the engine ?

Probably not. But you are more than welcome to try out the humblenet port, the `websockets-only` branch supports creating both server and client urho applications.

-------------------------

yiown | 2020-09-04 03:50:55 UTC | #18

Excellent ! I'll try it out right now and report back :cowboy_hat_face:

-------------------------

yiown | 2020-09-04 05:27:34 UTC | #19

Sorry no luck, here is the console log:
>     $ ./script/cmake_emscripten.sh .            
>     -- AAA ETCPACK
>     -- AAA FreeType
>     -- AAA LZ4
>     -- AAA PugiXml
>     -- AAA SDL
>     -- AAA StanHull
>     -- AAA AngelScript
>     -- AAA Lua
>     -- AAA toluapp
>     -- Exporting variables to parent scope
>     CMake Deprecation Warning at Source/ThirdParty/HumbleNet/cmake/UtilityFunctions.cmake:4 (cmake_policy):
>     The OLD behavior for policy CMP0025 will be removed from a future version
>       of CMake.
>     The cmake-policies(7) manual explains that the OLD behaviors of all
>     policies are deprecated and that a policy should be set to OLD only under
>     specific short-term circumstances.  Projects should be ported to the NEW
>     behavior and not rely on setting a policy to OLD.
>       Call Stack (most recent call first):
>     Source/ThirdParty/HumbleNet/CMakeLists.txt:19 (include)
>     -- results 1  1  1 1
>     -- results 1.1
>     -- results 2 OFF OFF 1 1
>     CMake Error: failed to create symbolic link '/Urho3D/include/Urho3D/ThirdParty/HumbleNet/src': no such file or directory
>     CMake Error: failed to create symbolic link '/Urho3D/include/Urho3D/ThirdParty/HumbleNet/lib': no such file or directory
>     -- AAA ik
>     -- AAA Detour
>     -- AAA DetourCrowd
>     -- AAA DetourTileCache
>     -- AAA Recast
>     -- AAA Box2D
>     -- AAA WebP
>     -- AAA Bullet
>     CMake Error at /usr/share/cmake/Modules/GenerateExportHeader.cmake:399 (get_property):
>       get_property could not find TARGET Urho3D.  Perhaps it has not yet been
>       created.
>     Call Stack (most recent call first):
>     Source/Urho3D/CMakeLists.txt:274 (generate_export_header)
>     Error copying file (if different) from "/Urho3D/Source/Urho3D/Urho3D.h.new" to "/Urho3D/Source/Urho3D/Urho3D.h".
>     -- AAA Urho3D
>     clang-12: warning: argument unused during compilation: '-mno-sse' [-Wunused-command-line-argument]
>     -- AAA Urho3DPlayer
>     -- Configuring incomplete, errors occurred!
>     See also "/Urho3D/CMakeFiles/CMakeOutput.log".
>     See also "/Urho3D/CMakeFiles/CMakeError.log".

Also, I see you have made extensive modifications to support some MSVC feature, and then more changes for the customized console. And when I tried to fix the building problem, I just got lost in confusion.

In any case, I see this is all to support network replication, and suddenly I understand why you need the **server** also working... BUT this is assuming *we want* network replication, and under this particular data model. So it's either all or nothing, self dependent, like a serpent biting its own tail.

And all I need is access to the websockets transport which is readily available in every platform...

Good thing is, your code gave me an idea where to include the emscripten websocket lib, so I'll fiddle with that a bit more, and if all fails, I'll just default to the HTTP pooling. So thanks @Miegamicis !!!

-------------------------

Miegamicis | 2020-09-06 19:17:30 UTC | #20

ah, crap.

Probably forgot to copy something from the main branch where I did all the testing. I had complete urho lib there and I tried to copy out all the necessary stuff for humblenet and it seems that I failed. But I have published the complete urho engine with humblenet here: https://gitlab.com/ArnisLielturks/urho3d-websockets

-------------------------

