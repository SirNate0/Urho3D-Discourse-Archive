cap | 2017-01-02 01:06:54 UTC | #1

Trying to follow the suggestions given here

[urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html)

about creating a new C++ project that links to Urho3D as an external library (trying the first option, using Urho3D library directly from the Urho3D project build tree). I've set things up exactly as described there, and CMake does successfully build a Visual Studio project which appears to have all the correct dependencies.

But the C++ project I've made is intended to be a console application. When I build it, I get the error message:

"142 error LNK2019: unresolved external symbol _WinMain@16 referenced in function __tmainCRTStartup"

I think the problem is that, in my new project, I have copied the text (from the documentation linked above) into my CMakeLists.txt, which uses the macro setup_main_executable.

Any advice on how I could change the top level CMakeLists.txt in my new project, to still link to Urho3D as described in the documentation, but to just change the new project type to console application?

Or that doesn't have to be the fix, I am really just trying to avoid the "unresolved external symbol _WinMain@16...."

Thanks all!

-------------------------

thebluefish | 2017-01-02 01:06:54 UTC | #2

In Visual Studio (which I believe is the IDE you're using), the relevant option is shown here:

[url=http://i.imgur.com/oqe2Bye.png][img]http://i.imgur.com/oqe2Byem.png[/img][/url]

I've no idea how to bake this into CMake though.

-------------------------

weitjong | 2017-01-02 01:06:54 UTC | #3

Try to build with this build option "URHO3D_WIN32_CONSOLE" set.

-------------------------

rasteron | 2017-01-02 01:06:54 UTC | #4

[quote="cap"]
But the C++ project I've made is intended to be a console application. When I build it, I get the error message:
[/quote]

AFAIK, it looks like you are trying for something like a headless mode with a console or input.

[code]Headless (bool) Headless mode enable. Default false.[/code]

Are you trying to do the same?

-------------------------

cap | 2017-01-02 01:06:55 UTC | #5

@thebluefish -- thank you, yes I am using Visual Studio and changing that option solved the error

@weitjong -- I gave it a try, and the VS solution was successfully built, although I still had to change the System/SubSystem option as thebluefish suggested. I'm okay with that.

@rasteron -- yes what we're doing is quite similar to running an Application in headless mode. In fact that was an earlier variant of our project. At this point we're not even inheriting from Application, but using Scene, Octree and others by hand

Appreciate the responses!

-------------------------

cap | 2017-01-02 01:07:17 UTC | #6

Correction: I said weitjong's suggestion to set the build option "URHO3D_WIN32_CONSOLE" didn't work for me. Actually this definitely [i]does[/i] work and I must have done it wrong.

-------------------------

