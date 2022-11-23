codefive | 2021-09-04 17:13:13 UTC | #1

I have installed Urho3D with DBE, and i have created a project for Web, Linux, and Windows, everything fine, but when i modify the project and run rake build it throws a error make: Makefile the file or directory doesnt exist and There is no rule to build 'Makefile' objective. And also if i want to use a ide (codelite) when i run GENERATOR=codelite rake cmake i get another error CMake Error at cmake/Modules/FindUrho3D.cmake Could not find compatible Urho3D library in Urho3D SDK installation or build tree. Thank you in advance BTW im on Linux

-------------------------

codefive | 2021-09-04 19:15:25 UTC | #2

I have managed to do it, i have added a enviromental variable to my .bashrc file named export URHO3D_HOME="path here to your urho3d install dir" from there i could build with IDE

-------------------------

weitjong | 2021-09-05 02:37:45 UTC | #3

Glad you got it figured out. The new pages on our online doc have explained the steps in detail.

The DBE is just providing a virtual environment that calls the rake tasks. The rake tasks are just wrapper on top of the existing old shell scripts, which in turn just invoke the existing old CMake build scripts. So, ultimately we are all still dealing with the same o’ same o’ Urho3D CMake build scripts. The requirement for “URHO3D_HOME” env-var is evidence of the age. In short, those CMake build scripts are very old and need upgrading badly, although they still work for now.

-------------------------

codefive | 2021-09-05 17:08:31 UTC | #4

Yes thank you !! I have opened another thread, yes a lot of improvements in Urho3d, i have not been around for a while i was bussy, but now im back

-------------------------

