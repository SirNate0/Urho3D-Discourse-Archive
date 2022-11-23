mi3D | 2017-01-02 01:11:22 UTC | #1

Hello @all

first, thanks for this 3D framework.

I adapted one of the Samples to my needs, and till this everythings works fine. Finally i wanted to control one of the Pins from the RasPi. Therefor i installed wiringPi, included it in my code. It compiled fine, but when linking there were a lot of unknown errors.

I would like to know where to put the "-lwiringPi" 

thanks in advance

-------------------------

weitjong | 2017-01-02 01:11:23 UTC | #2

Welcome to our forum.

Presumably you are compiling wiringPi from its source code. If so, you will have "wiringPi" library target (in CMake speak) setup in your build. Then, it is a simple question of configure your final binary target to depend on this new wiringPi library target. You can use CMake target_link_dependencies() command directly for this purpose or if you use our custom macro so far then you can do exactly the same thing by initializing the LIBS CMake variable as appropriate before invoking the setup_executable() macro. CMake would take care of the rest of emitting the linker flag, handling the dependency, etc.

This is a basic CMake question. I think you will get more help if you ask the question in the CMake forum.

-------------------------

