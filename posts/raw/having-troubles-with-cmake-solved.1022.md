Bananaft | 2017-01-02 01:04:52 UTC | #1

I've pulled current version from git, and having hard time building it. Win 7 64, VS 2013. I'm noob.

[code]CMake Error at ThirdParty/FreeType/CMakeLists.txt:80 (setup_library):
  Unknown CMake command "setup_library".


CMake Warning (dev) in CMakeLists.txt:
  No cmake_minimum_required command is present.  A line of code such as

    cmake_minimum_required(VERSION 3.2)

  should be added at the top of the file.  The version specified may be lower
  if you wish to support older CMake versions for this project.  For more
  information run "cmake --help-policy CMP0000".
This warning is for project developers.  Use -Wno-dev to suppress it.[/code]

I've tried to update FreeType, it started to stumble on another third party component - JO.
I also tried older CMake version - 2.8.12 vith same result.

-------------------------

GoogleBot42 | 2017-01-02 01:04:52 UTC | #2

What command did you use?  Are you using 1.32 or the latest unstable version of Urho3d?  Is the folder that Urho3D is in clean?  (Did you change anything other than running the command?)

-------------------------

weitjong | 2017-01-02 01:04:52 UTC | #3

I think you have hit a common pitfall of migrating from release 1.32 to the yet-to-be-released master branch. The build system in the latest master branch has been refactored heavily. You should read about it here [topic729.html](http://discourse.urho3d.io/t/new-build-system/715/1) (at least read the first post). I believe you have used cmake-gui instead of one of the provided build script. Using cmake-gui is actually just as fine, but then you have to take care yourself the difference between 1.32 and latest master branch due to the build system refactoring. In the 1.32 the main CMakeLists.txt is in the Source/ subdirectory while in the latest master branch it is in the top directory (project root where you have checked out the repo). So, you have to select the correct main CMakeLists.txt in the cmake-gui window.

-------------------------

Bananaft | 2017-01-02 01:04:52 UTC | #4

Yeah, I'm using gui(last unstable, no local changes.), because .bat files did nothing either, and I don't know how to get their log.

Thank you for reply, I'll make another approach later today.

-------------------------

Bananaft | 2017-01-02 01:04:54 UTC | #5

Ah, all I needed was, is to specify folder name. It's really that simple. That's why .bat files didn't worked.
[code]cmake_generic.bat my_build -VS=12[/code]

Didn't found how to setup cmake_guy to another CMakeLists.txt, but hey, I did built the thing.

-------------------------

