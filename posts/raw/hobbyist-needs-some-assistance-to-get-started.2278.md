conducto | 2017-01-02 01:14:28 UTC | #1

Hello Urho-Community!

First I'd like to introduce myself, as this is my first post in this forum, though i've been hanging around on Urho's website for quite some time. I'm a technical enthusiast who likes to tinker with programming and especially game development. Over the last decade I've developed several small games with different languages (loved the simplicity of game orientated languages like BlitzBasic) and also used my games for teaching purposes (my profession is media education).
When I was still a kid, my father had a book about c++ programming laying around in his office. I tried to figure out how to write programms or even games but never got used to the language's complexity (I guess I was lacking in programming experience :wink:). About a year ago I came back to cpp, did some online courses and messed around with librarys like SDL and GLEW. Really liked to dive in to this rather low level technical stuff and so I found out about Urho3D and got really excited about all the possibilities when I saw the samples.

But: As I told you, i am not a professional programmer and just a hobbyist. And that's why I am having a really hard time to get my own first project with Urho3D on its own feet. I was able to build Urho3D with the samples on Linux using CodeLite. Now that I want to set up my own project I run into problems. As mentioned in the tutorial (Setting up a Project (CMake)) I create a new folder "~/game" for my project and copy the folders bin and cmake from Urho3D, create a .cpp and .h file, create CMakeLists.txt and the scripts cmake_generic.sh and cmake_codelite.sh. But everytime I try to run the cmake script (~/game/cmake_codelite.sh ~/gameBuild/) it says that it could not find a compatible Urho3D lib:

CMake Error at CMake/Modules/FindUrho3D.cmake:352 (message):
  Could NOT find compatible Urho3D library in Urho3D SDK installation or
  build tree.  Use URHO3D_HOME environment variable or build option to
  specify the location of the non-default SDK installation or build tree.
Call Stack (most recent call first):
  CMake/Modules/Urho3D-CMake-common.cmake:193 (find_package)
  CMakeLists.txt:30 (include)


What am I doing wrong? I just can't figure it out...

-------------------------

1vanK | 2017-01-02 01:14:28 UTC | #2

You can set path to compiled engine in your CMakeLists.txt

For example [github.com/1vanK/PuddleSimulato ... eLists.txt](https://github.com/1vanK/PuddleSimulator/blob/master/GameSrc/CMakeLists.txt)
[code]
set (ENV{URHO3D_HOME} d:/MyGames/PuddleSimulator/Engine/Build)[/code]

-------------------------

conducto | 2017-01-02 01:14:28 UTC | #3

Thank you! That worked like a charm :slight_smile:

-------------------------

