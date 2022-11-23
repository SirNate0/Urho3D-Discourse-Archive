Enhex | 2018-08-08 22:04:52 UTC | #1

https://conan.io/

Using Conan will allow us to:
- move the dependencies outside of Urho's repo, and easily upgrade them.
- Easily use several builds of Urho3D at the same time (different build options, 32/64, ...), without having to manually rebuild or manage several copies.
- Easily consume Urho3D as a library, without having to manually generate a template project and maintain it.
- Speed up Urho build time by caching and reusing build results for dependencies
- Will allow easier consumption of libraries built on top of Urho3D

It's a bit tricky to move to Conan because the CMake script has a lot of logic and some of it has to be exposed in the Conan recipe, such as build options. Also all the dependencies logic needs to be moved from the CMake script to the Conan recipe.

I started making a recipe. It doesn't have all the options yet, and didn't move the dependencies logic from CMake to Conan:
https://github.com/Enhex/conan-Urho3D

Urho modifies few of the libs it uses, which will require creating a fork and a Conan recipe for it, so it isn't a big deal.

-------------------------

Enhex | 2018-08-09 18:24:36 UTC | #2

By the way I'd like to know if people are in favor of using Conan, Especially @weitjong. If so I'll put effort into it and make a PR.

-------------------------

weitjong | 2018-08-10 05:47:09 UTC | #3

This topic has been raised in the past. See:

https://github.com/urho3d/Urho3D/issues/2234

You don’t need my blessing for it. As long as you intend to maintain it long term then we will be glad to accept your contribution.

-------------------------

weitjong | 2020-12-25 08:53:40 UTC | #4

Two years have passed since I last commented on this thread. These days if you do any ML stuffs then you just cannot avoid to learn Python. Anyway I have now enough Python knowledge to get me started with Conan and I have time to play around with it recently. But to cut the long story short, I quickly have my doubt on Conan after my short evaluation. First of all I don't think I would like the idea to have Conan to download prebuilt binary into my system for security reason. All binaries in my system are GPG signed from my system official repo only. PERIOD. Ok, let's just say in future the prebuilt binary can be signed and verified just like those system packages from RPM/Deb repositories, I just don't see how that would scale up for Conan, considering some projects like Urho3D and SDL2 do not have a canonical way to build the binary from source. The combination of build options from Urho3D and SDL2 alone would already create a huge matrix, not to mention the variants due to different settings from compiler, build type, os, arch, etc. So, the idea of having someone specify a requirement in `conanfile.txt` and getting the signed binary installed ready for usage that actually meeting the specific project use case and need just sounds like a miracle, at least to me.

In my short evaluation, I already having issue to "just" attempting to bring in SDL2 (from bincrafters) as one of the dependencies. Understandably the SDL2 recipe would transitively bring in its own dependencies. However, I don't like the way the recipe draws the line between what should be system provided and what should be installed/built from source using the Conan recipe of the dependencies. And, there is no easy way to override that. For example, I cannot ask Conan to exclude `alsa`, it keeps tries to insist to build `libalsa` from source[?]. Some of CMake auto-detection magic from original SDL2 CMake build system is lost or hindered by Conan. I then attempted to create my own recipe for SDL using the recipe from bincrafters as baseline, but soon I realize if I have to write a Python script to get CMake to build SDL2 the way I like it by myself then I might as well do it without Python at all.

The only time I see it to be useful is when I specify the header-only library as dependencies, like `entt` or `doctest`. No binary, just a single header file that works for all settings and options. But even then, I find it to be a little bit intrusive to let the Conan's generators to "pepper" the conan-specific macros to the CMakeLists.txt build script in order to allow the two integrate together. I have tried "cmake", "cmake_paths", and "cmake_find_packages" generators.

This is just my personal opinion. What do others think about Conan?

-------------------------

Enhex | 2020-12-25 11:42:22 UTC | #5

[quote="weitjong, post:4, topic:4444"]
First of all I don’t think I would like the idea to have Conan to download prebuilt binary into my system for security reason.
[/quote]

You can control that. You can setup your own Conan server and manually add recipes/packages to it after auditing them, and configure your Conan client to only use your server (you can add/remove remotes).

[quote="weitjong, post:4, topic:4444"]
The combination of build options from Urho3D and SDL2 alone would already create a huge matrix, not to mention the variants due to different settings from compiler, build type, os, arch, etc.
[/quote]

That's an inherit complexity independent of any specific tool.
Unlike most other tools Conan doesn't ignore it and gives you a way to automatically manage the variation.
The consumer of a package doesn't have to specify all the options, each package defines its defaults which can be overriden.
It isn't a miracle, it's finally a tool that get things right.

[quote="weitjong, post:4, topic:4444"]
For example, I cannot ask Conan to exclude `alsa` , it keeps tries to insist to build `libalsa` from source[?]. Some of CMake auto-detection magic from original SDL2 CMake build system is lost or hindered by Conan.
[/quote]

Not all C++ libraries lend themselves easily for packaging, and it's usually because they're doing
questionable things with their build setup.
I'd say that using OS package manager for C/C++ dependencies is a bad solution, because (AFAIK) you don't have control over the build (for example if you need to compile with PIE or change some options).
The second part of "CMake magic" is also bad, CMake is not a package manager and it's awful attempt of its detection hacks (which are just looking up hardcoded paths AFAIK) are not something to look up to or try to preserve, my reaction would be "good riddance".
(and in general CMake is an abomination design wise)

Personally as of now I got [16 FOSS Conan packages I wrote on Github](https://github.com/Enhex?tab=repositories&q=conan&type=source), and more private ones.
Most of them were trivial to make - just provide the include path and lib name.
sometimes the libs do stuff that make them less packagable like adding a "d" suffix to their debug build library, which requires special handling in the recipe.
There's nothing special about Conan recipes, it's just a python script that specifies how to download, configure, build, and include/link a library. Same as you'd to manually.

[quote="weitjong, post:4, topic:4444"]
I find it to be a little bit intrusive to let the Conan’s generators to “pepper” the conan-specific macros to the CMakeLists.txt build script in order to allow the two integrate together
[/quote]

How can it be any less intrusive than generating an external script to include and call a single function from it?

<br>
I can say that about a week ago I wanted to rebuild Hellbreaker and the hassle of having to re-learn how to setup Urho3D projects, and manually re-create a new Visual Studio solution with all the linking and includes (need to add other libs too) is so tedious I couldn't bother.
If Urho3D had a Conan package it would be a matter of re-running a single command.
Also it would make creating a Linux build virtually zero effort.

-------------------------

weitjong | 2020-12-25 13:06:20 UTC | #6

Instead of replying you point by point, I would say this. All the "good things" that you mentioned above I already known or read about them before deciding to start evaluation Conan. In theory on paper it all sounds very good. But, the devil is in detail. Have you ever try to use SDL2 Conan recipe in your project so far, specifically on Linux. For me, there are nothing wrong to use some packages built by distro maintainers, especially for those packages that deal with lower level stuffs. Bullets and SDL and Alsa and PulseAudio are all available in the system repo. But I would choose to customize and build from source only for the first two, but leave the lower level packages to the one who knows the system better than me. The point is I have the option to choose where the line is drawn and not by someone else who writes the recipe.

To me the jury is still out whether Conan will be the C++ package manager. So to have my CMake build script committed to the one package manager now  is risky. Take the Android plugin for Gradle, for example, it actually just wraps around the CMake build script and not a single line in the CMake build script needs to be altered for the plugin to work. The rakefile in the GitHub Action workflow that I did also just wraps and invoke CMake. With Conan, this is not the case. The CMakeLists.txt needs to be made aware of Conan existence someway or another.

At least I agree with you on one thing. It is not easy to write a recipe for a more complex library with many options. If it was easy, I think by now there will be a few people bragging to have Conan recipe for Urho3D by now. Where are they? Even the experts in the bincrafters could not come up with SDL2 recipe that meets my taste :slight_smile:

-------------------------

Enhex | 2020-12-25 12:50:50 UTC | #7

btw just to clarify the choice between source and OS package is Bincrafter's.
There's nothing stopping you from installing OS packages from the Conan recipe, but note it's not portable, not only between Linux and Windows/etc but also between Linux distros, each using a different OS package manager.
So it's either single line Conan dependency to install from source, or maintaining different solution for windows/*BSD/MacOS/apt/pacman/rpm/dnf/zypper/apk/portage/... , and on top of that you have no guarantee all the OS packages build the lib the same way so that's more potential artificial complexity branching to manage the differences, and perhaps bugs or things break with specific ones, or some of them have more outdated versions than others holding you back.

it's simply a wrong model for userland library dependency management.

-------------------------

weitjong | 2020-12-25 12:57:25 UTC | #8

If that is true then the same should be true too for the default options to work equally well across all the platforms you just mentioned.

-------------------------

Enhex | 2020-12-25 13:04:00 UTC | #9

not really because Conan controls the options + the build settings, so it isn't affected by where it runs.
so you have a "single source of truth" which you control directly, instead of hoping that all these OS package managers build it the same way.

-------------------------

weitjong | 2020-12-26 15:16:55 UTC | #10

I know what are you saying. This is one of the Conan selling point. But I just not buying it for now. Don't get me wrong. I am not stopping anybody to adopting it. C++20 module is coming. So, not sure how the landscape will change after that.

-------------------------

Enhex | 2020-12-25 13:23:26 UTC | #11

Modules improve things regarding consuming libraries, but not getting/building/including/linking them AFAIK.

I think giving Conan a test run in small personal project can demonstrate the value better, but with packages which aren't troublesome :slight_smile:
Maybe trying to port such existing project to use Conan and measuring how much work it saves when setting up the project from scratch (i.e. fresh git clone).

-------------------------

