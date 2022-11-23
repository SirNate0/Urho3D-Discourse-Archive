georgeous | 2017-01-02 01:13:58 UTC | #1

I've been a lurker since I first heard about Urho3D a few weeks ago (getting back into 3D and looked up some OGRE reviews to get caught up). I just wanted to officially introduce myself so that you know who is/will be tweaking the wiki for Mint-specific instructions -- I'm running into a few obstacles getting everything up and running, and I'm enjoying the mental exercise as I get back into coding and 3D.

Many thanks to cadaver and everyone who has contributed to a such an exciting open source project.

-------------------------

weitjong | 2017-01-02 01:13:59 UTC | #2

Welcome to our forum. And thanks in advance for expressing your intention for updating the Wiki. You didn't say what kind of problem you are facing in your post but personally I don't think there are any major obstacles. To my knowledge, Mint is a derivative of Ubuntu/Debian which Urho3D supports well. One thing to note though, unlike our official online documentation, the Wiki's content is community-driven so it may get out-dated when the original content creator does not maintain it over time.

-------------------------

georgeous | 2017-01-24 15:28:05 UTC | #3

You're right, no major problems. Here's what I've come across so far:

For the 'quick start' wiki guide: Mint (and probably Ubuntu) doesn't come with the gcc compiler; you have to expressly install "build-essentials". Added [url=https://github.com/urho3d/Urho3D/wiki/Getting-started-in-Linux]here[/url]. If this is the case in Debian as well, someone please let me know and I'll format for the correction. I recently moved house and no longer have access to several desktops to play distro roulette.

For the build documentation:

On my system at least, when compiling Urho3D with ODBC support, unixodbc-dev is recommended, but only libiodbc2-dev seems to work. (I get "/usr/bin/ld: cannot find -libiodbc..." errors as per below when unixodbc-dev is installed)

Current issue _(EDIT: was installing in the home directory; installing via sudo in /usr/games seems to work. Left for posterity)_:

[code][ 72%] Linking CXX executable ../../../bin/tool/PackageTool
/usr/bin/ld: cannot find -linux-gnu
/usr/bin/ld: cannot find -linux-gnu
collect2: error: ld returned 1 exit status
Source/Tools/PackageTool/CMakeFiles/PackageTool.dir/build.make:96: recipe for target 'bin/tool/PackageTool' failed
make[2]: *** [bin/tool/PackageTool] Error 1
CMakeFiles/Makefile2:1880: recipe for target 'Source/Tools/PackageTool/CMakeFiles/PackageTool.dir/all' failed
make[1]: *** [Source/Tools/PackageTool/CMakeFiles/PackageTool.dir/all] Error 2
Makefile:160: recipe for target 'all' failed
make: *** [all] Error 2[/code]

...and a few "unused attribute" warnings that I assume aren't a big deal:

[code]/usr/games/Urho3D/Source/Urho3D/IO/FileSystem.cpp: In member function ?Urho3D::String Urho3D::FileSystem::GetCurrentDir() const?:
/usr/games/Urho3D/Source/Urho3D/IO/FileSystem.cpp:540:27: warning: ignoring return value of ?char* getcwd(char*, size_t)?, declared with attribute warn_unused_result [-Wunused-result]
     getcwd(path, MAX_PATH);
                           ^
/usr/games/Urho3D/Source/Urho3D/IO/FileSystem.cpp: In member function ?Urho3D::String Urho3D::FileSystem::GetProgramDir() const?:
/usr/games/Urho3D/Source/Urho3D/IO/FileSystem.cpp:717:48: warning: ignoring return value of ?ssize_t readlink(const char*, char*, size_t)?, declared with attribute warn_unused_result [-Wunused-result]
     readlink(link.CString(), exeName, MAX_PATH);
                                                ^[/code]

(running the downloaded .deb & compiling without ODBC support both seem to work fine)

-------------------------

weitjong | 2017-01-02 01:14:00 UTC | #4

I have already mentioned in my earlier comment that Wiki content tends to get out-dated over time, if not being maintained. The page that you are reading and editing exactly have this problem. The prerequisite packages listed in the page is evidently adapted from an older Urho3D "Building prerequisites" documentation page. That list is now expanded somewhat in release 1.6 after we have successfully integrated SDL CMake scripts into our own build system. The new prerequisite package list for Linux can be seen here [urho3d.github.io/documentation/ ... lding.html](https://urho3d.github.io/documentation/1.6/_building.html). Most notably is you may want to use PulseAudio instead of ALSA for sound server. This list is by no mean complete. It has intentionally left out those packages that are essential for any general 3D software development works, such as the native compiling toolchains (user has a choice between GCC and Clang) or OpenGL API implementation (user has a choice between open and proprietary one). That is, we only list what is specific to Urho.

As for building with URHO3D_DATABASE_ODBC enabled, I am afraid I was not able to reproduce your problem. I have both UnixODBC and iODBC installed but the build system still correctly configured my build tree to link against "libodbc.so" and not the "libiodbc.so". This is because our script gives higher precedence to UnixODBC. For what it worth, I am using Fedora 24. Those build scripts are mainly developed using Fedora but CI tested using Ubuntu, however, none of our CI jobs are setup to build with URHO3D_DATABASE_ODBC build option enabled at the moment. If you can reproduce your problem in a clean new build tree then you may log it as an issue in our issue tracker.

I have totally no idea how you could get "-linux-gnu" in your linking phase. For sure we don't have library called "inux-gnu".

-------------------------

Lumak | 2017-01-02 01:14:08 UTC | #5

I'd like to hear how's your Mint build is going.

Edit: what I wanted to know is the performance.  
[ul]
[li]I've installed Mint 17 on VMWare Player and was getting 4 fps on 19_VehicleDemo. I'm sure it's just a VMWare problem and nothing to do with Mint.[/li]
[li]Installed the same on VirtualBox and got 2 fps on 19_VehicleDemo.[/li][/ul]

I used Mint 17 in the past and it's actually quite good, but running a demo in a VM is shit.

-------------------------

