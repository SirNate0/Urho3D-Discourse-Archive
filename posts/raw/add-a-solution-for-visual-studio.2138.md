Sasha7b9o | 2017-01-02 01:13:24 UTC | #1

Hi.
From time to time I hear from newcomers that they retreat when compiling engine.
Since most of them use the studio, maybe add a studio solution in the .zip?
This allows beginners to start examples with a minimum of effort and familiarize the engine.
O_o.

-------------------------

Eugene | 2017-01-02 01:13:24 UTC | #2

Flooding main repo with garbage files is not very good idea...

-------------------------

Sasha7b9o | 2017-01-02 01:13:24 UTC | #3

Oh yeah.
However, it added just one "build" directory in the "root" directory.
At the same time fewer newcomers will leave aside Unity without trying Urho3D.

-------------------------

rasteron | 2017-01-02 01:13:25 UTC | #4

Another problem with this is the configuration option that you need to bundle with the Visual Studio solution, that is why you need to use CMake to choose from the available build options. Then again I guess the default option will do fine for newcomers.

At least this could be feasible as a separate project repo because I don't see it making it to main repo.

-------------------------

rku | 2017-01-02 01:13:25 UTC | #5

For building engine this is completely unnecessary, but for working on engine i can see it coming in handy. Last time i checked visual studio projects produced by cmake werent of best quality. But then again not like newcommer has business developing engine if he has a problem with cmake.. I would rather suggest cleaning up all those many files in main engine dir and replacing them with cmake.sh / cmake.bat that are supposed to be run with some parameters..

-------------------------

Enhex | 2017-01-02 01:13:25 UTC | #6

Using CMake GUI is just picking 2 directories and pressing 2 buttons.
Urho3D has excellent CMake build system, works out of the box, unlike some projects low quality CMakes that will keep you debugging their broken mess for hours.

Also the CMake build system can be configured in many ways. A single VS solution is fixed to a single configuration.
And it would probably have mismatching include paths, which means it will be broken and users need to manually fix the solution.

It's just a bad idea.

[quote="rku"]Last time i checked visual studio projects produced by cmake werent of best quality.[/quote]
They create solution without any compile errors, that's flawless quality in my book.

-------------------------

Sasha7b9o | 2017-01-02 01:13:25 UTC | #7

[quote="Enhex"]Also the CMake build system can be configured in many ways. A single VS solution is fixed to a single configuration.
And it would probably have mismatching include paths, which means it will be broken and users need to manually fix the solution.
It's just a bad idea.[/quote]
I agree with you completely.
Build system engine is simple, functional and perfect.
However, some inexperienced novice she scares (

-------------------------

rku | 2017-01-02 01:13:25 UTC | #8

[quote="Enhex"]
They create solution without any compile errors, that's flawless quality in my book.[/quote]

Yes, but all code is in one place, no separation no nothing. Sure one can work with that but.. I rather prefer neat solutions with things in their places, not one giant pile of files. It just gets tedious.. Not sure if it improved now. Would be real great if cmake created solution filters based on subdirectories source files are in. Does it do that? It didnt in the past.

-------------------------

Egorbo | 2017-01-02 01:13:25 UTC | #9

[quote="Sasha7b9o"]However, some inexperienced novice she scares ([/quote]
Those who are inexperienced can use UrhoSharp  :smiley:  :smiley:  I've created an [b]online[/b] solution template so it takes a few seconds to create a simple game:
[img]https://habrastorage.org/files/f22/b49/ded/f22b49dedc264396a47015784bd9b35f.gif[/img]
and it allows you to launch/debug Urho3D for Android, iOS and Windows from the same solution.
PS: and you can debug C# and the original Urho3D C++ code together if it's needed (sometimes it is) - I mean to jump from C# breakpoint to C++ one and see locals.

-------------------------

weitjong | 2017-01-02 01:13:26 UTC | #10

The problem with having a pre-generated project file, be it VS solution or Xcode xcodeproj or what have you, in the repository is that it would "bake" all the build options into the project settings and take the freedom away from users and so it forces users to modify the project settings manually via the IDE should they decide to make any changes at all to the build. The problem with the latter is those changes are not "sticked" to your "project". They are just settings in the VS/Xcode project file, and so if users ever have to perform an upgrade from Urho upstream, say migrating to newer release or applying bug fixes/enhancements in the Urho3D build system, etc, then users would have to redo their changes all over again in the newly downloaded pre-generated project file. CMake build system does not have this problem. As long as the users don't lose their CMake caches in the build tree, they could simply rerun CMake to reapply those manual changes back automatically, i.e. CMake reads the new changes in the build scripts, reads the newly added/removed source files in the upgraded codebase, and reads the build options in the caches and generates a new project file just the way each of us want it each time. Besides the point of avoiding product lockup.

-------------------------

Sasha7b9o | 2017-01-02 01:13:26 UTC | #11

Well thank you.

-------------------------

