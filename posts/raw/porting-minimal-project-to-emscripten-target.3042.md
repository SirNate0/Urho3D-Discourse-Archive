napard | 2017-04-24 15:41:55 UTC | #1

Hi, I've managed to compile Urho3D for Emscripten target, now I'd like to port a minimal working project to compile against that build, and run it inside the browser. What are the basic steps to achieve this? As I said, I have a working Urho3D build with Emscripten as target...

Thanks!

-------------------------

weitjong | 2017-04-25 07:28:48 UTC | #2

It makes no difference whether you are targeting Web platform or other platforms when you are reusing the build system from Urho3D for your own project. See https://urho3d.github.io/documentation/HEAD/_using_library.html.

-------------------------

