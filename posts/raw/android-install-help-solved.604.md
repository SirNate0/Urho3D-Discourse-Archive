practicing01 | 2017-01-02 01:01:38 UTC | #1

Hello, I followed the documentation build process (ran cmake_eclipse.sh) and am trying to 'Import "Existing Android Code into Workspace"' but eclipse isn't finding a project within the /Build directory.  It is finding something within the /Source directory but when I try to "Run As" -> "Android Project" that imported project, it just crashes on my phone (I don't think it's even creating a debug apk).  Any links to information that might help would be greatly appreciated.  Thanks for your time.

Edit: Solved, missed the environment variable step -.-', my apologies.

-------------------------

weitjong | 2017-01-02 01:01:38 UTC | #2

The cmake_eclipse.sh relies on the cmake_gcc.sh to do the actual work. In the normal case calling the cmake_gcc.sh (and so also cmake_eclipse.sh) configures and generates a Unix Makefile project file for native platform. In order to make it to configure/generate project file for Android platform, you need to export ANDROID_NDK environment variable pointing to where you have actually installed the Android NDK. The build tree for Android platform is currently defaulted to "android-Build" and not "Build" directory (which is for native platform). If you cannot find the "android-Build" directory then you have done something wrong with the ANDROID_NDK environment variable setting.

-------------------------

