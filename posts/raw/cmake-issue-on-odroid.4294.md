capelenglish | 2018-06-07 13:48:56 UTC | #1

I have developed a simple Urho3D application using C++ on my Windows PC. Now I want to port this over to run on a ARM based Odroid single board computer running Ubuntu. I have installed Urho3D on the Odroid, run cmake and make. The samples run fine. Now I want to install and complile my Urho3D application. Here is where I installed Urho3D:

    /home/odroid/Urho3D
and built it using

   ./cmake_arm.sh ./build

then I ran make in the ./build directory. As stated, the samples run fine in ./build/bin directory. 
My question is how do I setup my project directory correctly. Here is what I've tried:
1) create project root folder in /home/odroid/game1
2) cd game1 and create bin folder 
3) copy Data and CoreData folders from the SDK install into bin 
5) copy CMake folder from the SDK install to the project directory
6) can add the Urho3D project root directory into the PATH environment
	- edit the ~/.bashrc file and add the following line
	- export PATH=$PATH:/home/odroid/game1
	- export URHO3D_HOME=/home/odroid/Urho3D/build
	- reboot
7) create a source folder /home/odroid/game1/source
8) Copy my .cpp and .h files into the source directory
9) in the source folder copy the sample CMakeLists.txt file (replace MyProjectName and MyExecutableName with my project name)
10) run cmake ./source

I get a cmake error saying it can't find UrhoCommon. I've tried differnt things and gotten differnt errors. Obviously, I'm doing something wrong and would appreciate some guidance on how to accomplish my objective.

-------------------------

weitjong | 2018-06-07 20:29:47 UTC | #2

It looks like the last step was wrong. After setting up your own project similar to how Urho3D project is setup, you should be able to reuse its build system for your own project, so the last step should be something like:

9. ```cd /home/odroid/game1 && ./cmake_arm.sh ./build```

Probably you need to copy/symlink those Urho3D provided shell scripts first, if you haven't done so. HTH.

-------------------------

capelenglish | 2018-06-07 15:08:26 UTC | #3

I left out the step where I created a symlink to Urho3D. I edited the CMakeLists.txt and hard coded

    set (CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake/Modules)
to 

    set (CMAKE_MODULE_PATH /home/odroid/game1/CMake/Modules)
and I got it to work. I'm not sure where CMAKE_SOURCE_DIR gets defined...

-------------------------

weitjong | 2018-06-07 15:11:47 UTC | #4

That is one of the built-in variable from CMake. Its value should automatically point to where your project "source tree" is, which in this case, should be exactly "/home/odroid/game1". Provided your main ```CMakeLists.txt``` file is correctly resided in that path.

-------------------------

