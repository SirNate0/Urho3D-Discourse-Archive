greyWiz | 2017-07-11 18:20:13 UTC | #1

Hi, I'm trying to set up Urho3D as a submodule inside my own application according to this link:

https://urho3d.github.io/documentation/HEAD/_using_library.html

I've copied CMake/Modules to the root folder and added the code to CMakeLists.txt exactly as shown there, but when I try to configure the project through cmake-gui I receive this error:

> CMake Error at CMake/Modules/FindUrho3D.cmake:347 (message):
  Could NOT find compatible Urho3D library in Urho3D SDK installation or
  build tree.  Use URHO3D_HOME environment variable or build option to
  specify the location of the non-default SDK installation or build tree.
  Ensure the specified location contains the Urho3D library of the requested
  library type.
Call Stack (most recent call first):
  CMake/Modules/UrhoCommon.cmake:230 (find_package)
  CMakeLists.txt:22 (include)

I have already set URHO3D_HOME inside cmake_gui pointing to the Urho3D folder (inside Dependencies/Urho3D), but it keeps complaining that can't find the library or SDK installation. What am I missing here?


Thanks in advance!

-------------------------

Eugene | 2017-07-11 18:48:26 UTC | #2

This is known issue.
https://github.com/urho3d/Urho3D/issues/1167

-------------------------

greyWiz | 2017-07-11 19:02:31 UTC | #3

Hi Eugene, thanks for the reply. I've read that linked topic yesterday and it says

>  In the mean time though, unless you are familiar with how CMake works, I advice to stay within the currently supported use case as documented in the https://urho3d.github.io/documentation/HEAD/_using_library.html in order not to waste your time.

Since I was following the "currently supported use case", I thought this method was actually working and that it was my fault in messing it up... so there's no way of making it work for now? :disappointed:

-------------------------

Eugene | 2017-07-11 19:09:18 UTC | #4

Sorry, I misunderstood the topic because you actually don't need to _submodule_ Urho despite the title.
Then...

Make sure that URHO3D_HOME is set to _built_ CMake project, you shan't set the variable to Urho's sources. However, in this case you don't need (or even mustn't) store Urho inside your project)

-------------------------

greyWiz | 2017-07-11 20:55:02 UTC | #5

Ok, I guess I've got it... The scenario described is one of adding a dependency to the SDK, this is why there's no need to submodule it.

Well, I guess there's nothing that could be done for now. I will build Urho3D inside its own folder and maybe think about a workaround in the future.

Thanks!

-------------------------

weitjong | 2017-07-12 00:26:40 UTC | #6

Sorry for the delay. Personally I have not given that issue enough priority. I intentionally discourage the submodule usage with the current state of our build system to casual CMake users. However, if you are a CMake expert then that advise doesn't apply to you. And you are welcome to submit a PR to contribute your changes if you have cracked it yourself.

-------------------------

greyWiz | 2017-07-12 16:02:23 UTC | #7

Hi weitjong, thanks for the reply. It is my intention fixing it so it works as a submodule, but right now my priority is finishing my Master's project, which is using Urho3D as its main dependency. Anyway, I guess I'll keep studying Urho's CMake code in my spare time during the Master's, let's see if I'll be able to crack it in the meantime. :-)

-------------------------

