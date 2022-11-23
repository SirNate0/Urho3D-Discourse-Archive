godan | 2017-01-02 01:14:38 UTC | #1

When I use Urho as lib, I generally use

[code]
setup_main_executable()
setup_library()
[/code]

to create my projects. However, this always copies the resouce dirs (Data, CoreData) in to my build folder (full copy on Windows VS, linked on other). Is it possible to turn this off?

-------------------------

weitjong | 2017-01-02 01:14:38 UTC | #2

The purpose of the setup_main_executable() macro is to setup a main executable target with resource copying. If you don't want to perform the latter then you can try to call its counterpart setup_executable() macro instead. This may or may not work depends on the nature of the target you want to setup. The other way is, populating the "RESOURCE_DIRS" CMake variable to represent your own resources directory structure (it could be empty var as long as it is defined, I think) before calling the setup_main_executable() macro.

-------------------------

godan | 2017-01-02 01:14:40 UTC | #3

K, great. I think setting the RESOURCE_DIRS variable is the way to go for me. Thanks!

-------------------------

