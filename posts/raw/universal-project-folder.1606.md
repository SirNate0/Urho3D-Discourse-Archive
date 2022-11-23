greenhouse | 2017-01-02 01:08:52 UTC | #1

I want to have game project folder that will contain iOS-folder, Android-folder and shared-folder of C++ code for both of them.

Something similar to how Cocos2d-x newly created project folder looks like. I think it's very convenient.

How can I achieve this with Urho3D?

-------------------------

jmiller | 2017-01-02 01:08:56 UTC | #2

Hi greenhouse,

I've found Urho to be accommodating. I have a few Desktop+Android projects structured something like this:

./Android-src : a copy of Urho/Android folder, with the various files edited to fit the project, added ant.properties file, etc.
[b]edit:[/b] Before building, I have a "scaffolding" script that makes a copy of this for the actual build tree (like build-android-debug), and inside that an 'assets' folder with links to (or copies of) CoreData/Data folders.
./build (debug)
./build-android-debug
[etc]
./CMake (symbolic link ->Urho/CMake)
./CoreData (symbolic link ->Urho/bin/CoreData)
./Data
./Data2 (example of additional data tree, which I can quickly add to Urho engine's ResourcePath)
./src (C++)
./{project files, cmake-[platform] and other scripts, CMakeLists.txt, binaries..}

I'm unfamiliar with iOS particulars, maybe others have more advice.
Think you will find something comfortable and convenient to you.

-------------------------

weitjong | 2017-01-02 01:08:56 UTC | #3

A few releases ago we did have something similar whereby our build system would decide where the "standard" build tree location for each target platform should be on user behalf. All the build trees were inside the Urho3D project folder. However, some of you said that was not a true out-of-source build system should be and we (finally) agree. Now the build system has changed to not make that decision anymore. User is the one responsible to tell where his/her build tree should be generated in the file system.

-------------------------

greenhouse | 2017-01-02 01:08:58 UTC | #4

[quote="weitjong"]A few releases ago we did have something similar whereby our build system would decide where the "standard" build tree location for each target platform should be on user behalf. All the build trees were inside the Urho3D project folder. However, some of you said that was not a true out-of-source build system should be and we (finally) agree. Now the build system has changed to not make that decision anymore. User is the one responsible to tell where his/her build tree should be generated in the file system.[/quote]
I can understand the reason behind this decision but for newcomers like me, it's quite hard to create a universal project structure as I have little knowledge of cmake...  :confused: 
It will be very helpful to leave an option of such tree generation (maybe with some parameters, for example which platform to support in project and etc.) for newcomers.
Can someone please share a steps to recreate simple universal project structure?  :slight_smile:

-------------------------

greenhouse | 2017-01-02 01:08:58 UTC | #5

[quote="carnalis"]Hi greenhouse,

I've found Urho to be accommodating. I have a few Desktop+Android projects structured something like this:

./Android (a copy of Urho/Android folder, with the various files edited to fit the project, added ant.properties file, etc.)
./build (debug)
./build-android-debug
[etc]
./CMake (symbolic link ->Urho/CMake)
./CoreData (symbolic link ->Urho/bin/CoreData)
./Data
./Data2 (example of additional data tree, which I can quickly add to Urho engine's ResourcePath)
./src (C++)
./{project files, cmake-[platform] and other scripts, CMakeLists.txt, binaries..}

I'm unfamiliar with iOS particulars, maybe others have more advice.
Think you will find something comfortable and convenient to you.[/quote]
Hi carnalis,
I'll need some time to understand the structure you are using, but it looks nice, only iOS platform is missing :slight_smile:
By the way, do you use Android Studio for developing?

-------------------------

weitjong | 2017-01-02 01:08:59 UTC | #6

Well, it cannot keep everyone happy all the time. I already mentioned in my previous comment that user can generate the build tree(s) anywhere they like. It does not specifically prevent you from generating those inside the Urho3D project directory. So one can just as easily have this "universal" structure manually:

[code]Urho3D:
   - Android
   - CMake
   - etc from the Urho3D upstream
   then followed by generated build trees:
   - native-Build
   - android-Build
   - mingw-Build
   - rpi-Build
   - etc
[/code]

Just invoke the CMake as many time as you like via our convenient scripts or via cmake-gui and alternate the new build tree location and the build options as appropriate. You do need to have all the compiler toolchains properly configured in your host system before you can target multiple platforms. As iOS buid tree needs xcodebuild, one can only have this build tree generated when the host system is Mac with Xcode installed.

-------------------------

greenhouse | 2017-01-02 01:08:59 UTC | #7

Thanks for clarifications! 

Which IDEs supported for Android development? Android Studio?

-------------------------

weitjong | 2017-01-02 01:08:59 UTC | #8

I don't know about other users. But personally I use Eclipse/CDT/ADT for Android development. If you look carefully in our build system configuration then you can see it goes that little extra mile to support Eclipse IDE.  :wink:

-------------------------

greenhouse | 2017-01-02 01:09:00 UTC | #9

[quote="weitjong"]I don't know about other users. But personally I use Eclipse/CDT/ADT for Android development. If you look carefully in our build system configuration then you can see it goes that little extra mile to support Eclipse IDE.  :wink:[/quote]
Ok, thanks! 

I've recently encountered [url=https://www.cevelop.com/]Cevelop IDE[/url]. Someone tried it?

-------------------------

AReichl | 2017-01-02 01:09:03 UTC | #10

Cevelop is nice. It's basically Eclipse with all ( at least all that make sense ) addons/plugins for C++.

-------------------------

jmiller | 2017-01-02 01:09:07 UTC | #11

[quote="greenhouse"]I'll need some time to understand the structure you are using, but it looks nice, only iOS platform is missing :slight_smile:
By the way, do you use Android Studio for developing?[/quote]

I use CodeLite, which has good support for [url=http://mingw-w64.org/]MinGW-w64[/url]
As Alex showed, it can also do syntax + code completion for AngelScript: [topic45.html](http://discourse.urho3d.io/t/configuring-codelite-for-editing-as-scripts/68/1)

(and slight edit to my post to describe android scaffolding)

-------------------------

