xujingsy | 2017-01-02 00:59:43 UTC | #1

there are two main steps:
one is use cmake_android.bat to generate project file,this step is ok!
the other step:
android update project -p .-t 1 ----- ok!
make -j4 ---- error!
--------------------------------
make: Interrupt/Exception caught (code = 0xc00000fd, addr = 0x420942)
make[1]: *** [ThirdParty/Box2D/CMakeFiles/Box2D.dir/all] Error 255
make: *** [all] Error 2

why?thanks!

-------------------------

