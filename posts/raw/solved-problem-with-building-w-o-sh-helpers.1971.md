artemutin | 2017-01-02 01:11:58 UTC | #1

Hello.

I've successfully built engine, and my own project for Android with Urho3D as standalone library using cmake_android.sh script. But, in order to properly work with IDE (Qt Creator or Clion), it needs bare cmake to be run and generate build files.
And here is the cmake error -  while i trying to import my project into QtCreator - [spoiler]~/Build/Urho3D-Android-Build/"aa"
CMake Error at CMake/Modules/FindUrho3D.cmake:356 (message):
  Could NOT find compatible Urho3D library in Urho3D SDK installation or
  build tree.  Use URHO3D_HOME environment variable or build option to
  specify the location of the non-default SDK installation or build tree.
  For Android platform, double check if you have specified to use the same
  ANDROID_ABI as the Urho3D library in the build tree or SDK.
Call Stack (most recent call first):
  CMake/Modules/Urho3D-CMake-common.cmake:195 (find_package)
  CMakeLists.txt:36 (include)[/spoiler] 
I can read error messages, and the point is that $URHO3D_HOME variable is set to correct path! I can echo it in terminal, I can even display it within cmake script itself - here it is, on a first line of log(with redundant "aa"  :slight_smile:  to indicate empty var)
Here is my CMakeLists.txt:[spoiler][pastebin]K2pTyagv[/pastebin][/spoiler]
I had also tried to pass it as argument -still had no luck.

Any suggestions, please? I want to use IDE features, like easy navigating through code of Open Source Engine :smiley: !

-------------------------

weitjong | 2017-01-02 01:11:58 UTC | #2

IMHO, this is the problem of the IDEs themselves. Those IDE rely on CMake to generate the project but yet they do not provide a way to select which CMake generator and which CMake toolchain files to use. They just assume and use the native generator/toolchain. To make the matter worse, CMake is also inflexible in this matter. Once a generator is chosen and the project file is generated initially then it does not allow it to be changed. Not unless you reset its cache and regenerate the project from scratch again. I have not tried it with Qt Creator yet, but at least in CLion the IDE provides a way to reset the cache and reload project (more like regenerate the project actually) with a single click of a button. So, I have no problem to use CLion with Android NDK compiler toolchain.

Step 1. Open the project. Clion uses the native generator and toolchain. In my Linux host system, the native generator is Unix Makefile, so that's good and no need to be changed for my case. We will change the toolchain in the next step though.
Step 2. Go to CMake view then click on the "CMake Settings" button. Change the CMake options to include "-DCMAKE_TOOLCHAIN_FILE=CMake/Toolchains/android.toolchain.cmake". Click OK. You can see CLion tries to invoke CMake to reload (regenerate) the project again, but nothing really change due to CMake change inertia that I explained earlier.
Step 3. Still in the CMake view, click on the "Reset Cache and Reload Project" button. This button is on the "Cache" tab. After the regeneration then you should be able to build correctly.

-------------------------

artemutin | 2017-01-02 01:11:58 UTC | #3

[quote="weitjong"]IMHO, this is the problem of the IDEs themselves. Those IDE rely on CMake to generate the project but yet they do not provide a way to select which CMake generator and which CMake toolchain files to use. They just assume and use the native generator/toolchain. To make the matter worse, CMake is also inflexible in this matter. Once a generator is chosen and the project file is generated initially then it does not allow it to be changed. Not unless you reset its cache and regenerate the project from scratch again. I have not tried it with Qt Creator yet, but at least in CLion the IDE provides a way to reset the cache and reload project (more like regenerate the project actually) with a single click of a button. So, I have no problem to use CLion with Android NDK compiler toolchain.

Step 1. Open the project. Clion uses the native generator and toolchain. In my Linux host system, the native generator is Unix Makefile, so that's good and no need to be changed for my case. We will change the toolchain in the next step though.
Step 2. Go to CMake view then click on the "CMake Settings" button. Change the CMake options to include "-DCMAKE_TOOLCHAIN_FILE=CMake/Toolchains/android.toolchain.cmake". Click OK. You can see CLion tries to invoke CMake to reload (regenerate) the project again, but nothing really change due to CMake change inertia that I explained earlier.
Step 3. Still in the CMake view, click on the "Reset Cache and Reload Project" button. This button is on the "Cache" tab. After the regeneration then you should be able to build correctly.[/quote]
Thanks for the reply! It has worked both with Clion and QtCreator(just manually delete cache in build folder, and voila!)

-------------------------

