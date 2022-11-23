xalinou | 2017-01-02 01:12:44 UTC | #1

I've noticed that Urho has pretty good Emscripten support and i was curious if anyone tested networking. Is it supported without any changes? Or it hasn't been tested yet?

-------------------------

Enhex | 2017-01-02 01:12:44 UTC | #2

I've been looking into this topic.

AFAIK the libraries that urho uses for networking don't compile with emscripten out of the box.

Emscripten provides libc networking (Brekeley socket API), which it uses JavaScript networking to emulate, which means only asynchronous operations should be used ([kripken.github.io/emscripten-si ... networking](https://kripken.github.io/emscripten-site/docs/porting/guidelines/api_limitations.html#networking)).
This is low level work, and I wouldn't recommend it.

There's a better approach. Emscripten lets you execute JS code directly, so you could use that to use JS networking directly which is so much simpler and elegant.
[kripken.github.io/emscripten-si ... javascript](https://kripken.github.io/emscripten-site/docs/api_reference/emscripten.h.html?highlight=asm#inline-assembly-javascript)

AFAIK JS only has 2 networking systems: HTTP requests and websockets.
There are C++ libraries for both.
It should be possible to make a library that conditionally uses a JS or C++ implementation so there'll be a single API for both regular and emscripten builds, similar to how Urho uses Direct3D/OpenGL.
It makes sense because if you're using JS networking directly you'll need HTTP/websocket servers, so you need to use the same networking system for the regular build.

-------------------------

rasteron | 2017-01-02 01:12:44 UTC | #3

There's WebRTC and it's also P2P. Checking the changelog, I'm not sure about the status of this feature, but I think they already fixed it with v1.34.

[quote]v1.34.2: 7/14/2015
------------------
 - Upgrade to new SIMD.js polyfill version and improved SIMD support.
 - Improved WebGL support in --proxy-to-worker mode (#3569)
 - Removed warning on unimplemented JS library functions
 - Fix WebGL 2 support with closure compiler
[b] - Fixed an issue with WebRTC support (#3574)[/b]
 - Fixed emcc to return a correct error process exit code when invoked with no input files
 - Fixed a compiler problem where global data might not get aligned correctly for SIMD.
 - Fixed a LLVM backend problem which caused recursive stack behavior when linking large codebases, which was seen to cause a stack overflow crash on Windows.
 - Full list of changes:
    - Emscripten: [github.com/kripken/emscripten/c ... 1...1.34.2](https://github.com/kripken/emscripten/compare/1.34.1...1.34.2)
    - Emscripten-LLVM: [github.com/kripken/emscripten-f ... 1...1.34.2](https://github.com/kripken/emscripten-fastcomp/compare/1.34.1...1.34.2)
    - Emscripten-Clang: no changes.
[/quote]

[webrtc.github.io/samples/](https://webrtc.github.io/samples/)

Check also with BananaBread project (Cube2 port)
[github.com/kripken/bananabread](https://github.com/kripken/bananabread)

-------------------------

xalinou | 2017-01-02 01:12:45 UTC | #4

BananaBread used to have WebRTC support, but that has been broken for a long time. There's a PR with fixes, but apparently, it's heaavily outdated and wasn't merged by the authors: [github.com/kripken/BananaBread/pull/38](https://github.com/kripken/BananaBread/pull/38)

The way they used to do networking was by relaying websocket connections: [github.com/kripken/BananaBread/ ... /server.py](https://github.com/kripken/BananaBread/blob/master/cube2/server.py)

Very crappy.  :frowning:

-------------------------

Sir_Nate | 2017-01-02 01:12:48 UTC | #5

There are a couple of paragraphs about some people's experience porting Networking code here if anyone's interested:
[url]https://hacks.mozilla.org/2013/12/monster-madness-creating-games-on-the-web-with-emscripten/[/url]

-------------------------

rasteron | 2017-01-02 01:12:49 UTC | #6

[quote="xalinou"]BananaBread used to have WebRTC support, but that has been broken for a long time. There's a PR with fixes, but apparently, it's heaavily outdated and wasn't merged by the authors: [github.com/kripken/BananaBread/pull/38](https://github.com/kripken/BananaBread/pull/38)

The way they used to do networking was by relaying websocket connections: [github.com/kripken/BananaBread/ ... /server.py](https://github.com/kripken/BananaBread/blob/master/cube2/server.py)

Very crappy.  :frowning:[/quote]

You can check [b]luser[/b]'s activity and fork branch here 'webrtc-sockets'. I think he got this working again at some point and the possible support again..

[github.com/luser/emscripten/com ... tc-sockets](https://github.com/luser/emscripten/commits/webrtc-sockets)
[github.com/kripken/emscripten/i ... -184876966](https://github.com/kripken/emscripten/issues/3773#issuecomment-184876966)

-------------------------

dprandle | 2022-10-01 20:07:11 UTC | #7

Hi - I know this thread is way old..

I'm trying to build a UI for a ROS robot control - using urho cause part of the UI is a visualization of mapping data and I am comfortable with both urho UI and renderer, and well I hate JavaScript/typescript 

Before I invest time figuring it out myself - was wondering if anyone knew if it's still the case that socket connections and the networking system don't directly work in emscripten build

Thanks!

-------------------------

rku | 2022-11-03 07:41:50 UTC | #8

Yes, but it is way worse than that. There is an experimental unfinished [branch](https://github.com/urho3d/Urho3D/tree/websockets-implementation) by @Miegamicis which uses websockets. However scene synchronization is so bad that anything beyond simplest game will not scale. @Eugene reworked networking system to eliminate scaling limitations and i am working on implementing networking using webrtc (in rbfx of course).

-------------------------

dprandle | 2022-11-03 17:56:00 UTC | #9

Thanks for the reply

Luckily for me, I don't need replication using emscripten - my use case is very simple.

For anyone else wondering about this - if you use posix sockets and compile with emscripten, they will be converted to web sockets in the browser, but, they seem to work.

Keep in mind on your server, if you plan to support desktop and web build, it works more smoothly (at least for me using nodejs server) to open separate servers - one for the web socket connections and one for the bare system posix socket connections.

Also, since the web sockets must be created on top of http connection, some handshaking is involved which means you need to use your posix sockets (which will be converted to web sockets in the browser) in non-blocking mode and poll the socket for read/write ready state on the fd before use.

I could see this not being a viable way to do replication, as requiring all data to go through http protocol could be high in overhead. But, for people like me who are just sending/receiving fairly simple command/info packets, the emscripten compiler conversion to web sockets for posix sockets works. Also, I use linux for this - I would imagine mac would be the same deal but windows totally different.

Thanks

-------------------------

