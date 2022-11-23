simonsch | 2018-03-02 13:10:00 UTC | #1

Greetings Community,

I am new to urho3d and want to use this engine in android via c++.

After i had some initial issues building urho3d for android 32 bit (armeabi-v7a) i was able to build everything as needed with the very easy to use shell scripts.

As a result i got 51 .so files (i assume for the examples), an additional libUrho3DPlayer.so and one static prebuilt lib libUrho3D.a. My first question is this libUrho3D.a + headers is that the engine? What do i need to develop for urho3d in c++?

I have an existing android project which exists out of some activites created with Java, JNI for connecting my c++ code and my c++ core which is responsible for some heavy calculations. Before urho3d i was using a GLSurfaceView which allowed me to dispatch the OpenGL Context via JNI through my c++ core. 

How can i create a similiar workflow with urho3D? Do i need an SDLActivity like in the examples? Can i then use urho3d in my c++ code. Sry if this is trivial but i searched a while and didn't find any information on this topic. 

The only related post i was able to find is this one:
https://discourse.urho3d.io/t/best-way-to-use-android-build/3126/3

Gradle, JDK and Android SDK/NDK are all available in my setup.

If you need any additional information, just ask and i am happy for every feedback i get :).

-------------------------

Lumak | 2018-03-02 16:39:24 UTC | #2

[quote="simonsch, post:1, topic:4066"]
My first question is this libUrho3D.a + headers is that the engine?
[/quote]

yes

[quote="simonsch, post:1, topic:4066"]
What do i need to develop for urho3d in c++?How can i create a similiar workflow with urho3D? Do i need an SDLActivity like in the examples? Can i then use urho3d in my c++ code.
[/quote]
The work flow run on android is all setup using SDL, SDLAcitivity, SDLSurface. You don't have to use your own GLSurfaceView. Caveat with the current work flow is that it requires Urho3DPlayer.so to exist to run any samples.  If you want to load your own specific C++ executable, I created a sample repo here, https://github.com/Lumak/Urho3D-Android-Project

-------------------------

simonsch | 2018-03-05 15:35:38 UTC | #4

Thy for the fast response, this helps me a lot. So i need the Urho3DPlayer.so only for the samples, okay. I looked up your helpful github project and i asked myself, why do you integrate sdl in c++ yourself. Can i also take the prebuilt version from urho3d? 

I see that you are even building the used joystick sample yourself, this would be the point for my custom code then? I ask because i miss the JNI glue, SDL dispatches events via JNI bindings through native c++ code, sorry if this is obvious.

It seems SDL doesn't find it's nativie c++ method, as i changed from '75_JoystickAndroid' to '01_HelloWorld' i was able to load this prebuilt .so sample but i get an 
java.lang.UnsatisfiedLinkError: No implementation found for int org.libsdl.app.SDLActivity.nativeInit

That's weird because i already integrate the prebuilt static libSDL.a. I looked up your SDL_android.c code and tried to integrate this into my app, as i saw that it is the needed c interface. Now i can't find any SDL header files from their and i saw th prebuilt libSDL.a file from urho doesn't have any of those headers. This static prebuilt is based only on object files it seems (.o). I am totally confused now.... i will try to include headers from sources now, but files like (../../video/android/SDL_androidkeyboard.h or ../../events/SDL_events_c.h) are still missing, they seem not be anywhere.

Edit:

After some experiments i was able to run your code and run the joystick .so sample from my application. But i found another example for SDL on android with version 2 it includes several other files (Sdl, SDLActivity, SDLAudioManager, SDLControllerManager), is this a newer one in comparison to your used version? And why you use urho3D 1.7 has this any specific reason? Also i still have problems trying to compile my own code, when using your SDL_Android.c interface. In the mentioned version 2 it is written that such an interface is not necessary anymore. Sry for bothering you with so many questions :smiley: .

-------------------------

Lumak | 2018-03-05 18:38:22 UTC | #5

Are you aware that Urho3D has its own SDL lib that it has integrated to the engine?  It's located in Urho3D/Source/ThirdParty/SDL folder and modified to work with Urho3D process.  You can't just bring sdl lib from sdl.org prebuild and make it work.

First let me say this, every sample that comes with Urho3D, excluding the PBR, will work on Android without any modification or addition of any external libs. Every ThirdParty libs that's already included and linked is all you need.

I specify Urho3D 1.7 tag as a reference because the head/master is constantly moving, and it's easier to specify a stable tag to guarantee that everyone who uses the repo can build it.

-------------------------

slapin | 2018-03-06 07:59:00 UTC | #6

Hi, all!
To clean things up - the only supported way to build for Android now is using Visual Studio, right?
Thanks!

-------------------------

simonsch | 2018-03-06 08:39:38 UTC | #7

> Hi, all!
To clean things up - the only supported way to build for Android now is using Visual Studio, right?
Thanks!

Why? I did build it with cmake via console and the supported shell aka batch files.

> Are you aware that Urho3D has its own SDL lib that it has integrated to the engine? It’s located in Urho3D/Source/ThirdParty/SDL folder and modified to work with Urho3D process. You can’t just bring sdl lib from sdl.org prebuild and make it work.
First let me say this, every sample that comes with Urho3D, excluding the PBR, will work on Android without any modification or addition of any external libs. Every ThirdParty libs that’s already included and linked is all you need.
I specify Urho3D 1.7 tag as a reference because the head/master is constantly moving, and it’s easier to specify a stable tag to guarantee that everyone who uses the repo can build it.

Thy i was not aware of this fact related to SDL, the samples are fine but i want to start coding myself ;). And ok i understand using a stable release. But i still have problems understanding how you use the source code with your native interface. I have a prebuilt urho3d library, i have an Android Studio project, with running java as well as c++ code. I controll my c++ core via JNI and the build results in one shared object which is then loaded. For the sdl activity i need a separate .so file, so far so good. But i want to build this .so file from my source code.
So when i look at your repository:
`Urho3D-Android-Project/Source/Samples/75_JoystickAndroid/`
contains the c++ source code for the sample you build, and additionally there is
`Urho3D-Android-Project/Source/ThirdParty/SDL`
but it contains not the SDL library just the glue but reference, headers which are not present in the project setup. Sry if i missed something, but i don't see where this project loads the SDL prebuilt.

-------------------------

slapin | 2018-03-06 10:03:08 UTC | #8

well, for me when I build with cmake on Linux, the resulting .so libraries miss SDL_main symbol. Which prevents any example from starting.

People building under Windows with VS do not see and never seen such problem,
so I ask.

-------------------------

simonsch | 2018-03-06 10:16:38 UTC | #9

> well, for me when I build with cmake on Linux, the resulting .so libraries miss SDL_main symbol. Which prevents any example from starting.
People building under Windows with VS do not see and never seen such problem,
so I ask.

I can't reproduce your problem i build it via a debian base image in a docker container. And this thread has nothing to do with building urho3d itself. Please create a new thread or contribute to the described problem.

-------------------------

johnnycable | 2018-03-06 11:02:16 UTC | #10

Let's try to add some more chaos. 
My gradle app file:

    apply plugin: 'com.android.application'

    android {
        compileSdkVersion 23
        buildToolsVersion '26.0.2'
        defaultConfig {
            applicationId "com.github.urho3d"
            minSdkVersion 12
            targetSdkVersion 23
            versionCode 1
            versionName "1.0"
            testInstrumentationRunner "android.support.test.runner.AndroidJUnitRunner"
            externalNativeBuild {
                cmake {
                    arguments "-DANDROID_TOOLCHAIN=clang"
                    arguments "-DANDROID_STL=c++_static"
                    arguments "-DCMAKE_BUILD_TYPE=Debug"
                    arguments "-DCMAKE_CXX_FLAGS=-std=c++11"
                    arguments "-DANDROID_CPP_FEATURES=exceptions rtti"
                    abiFilters "armeabi-v7a"
                }
            }
        }
        buildTypes {
            release {
                minifyEnabled false
                proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
            }
        }
        externalNativeBuild {
            cmake {
                path "CMakeLists.txt"
                // prefer local.properties cmake path setup
                // version "3.6.4111459"
            }
        }
        compileOptions {
            sourceCompatibility JavaVersion.VERSION_1_8
            targetCompatibility JavaVersion.VERSION_1_8
        }
        dexOptions { 
            javaMaxHeapSize "4g"
        }    
    }

    dependencies {
        implementation fileTree(include: ['*.jar'], dir: 'libs')
        implementation 'com.android.support:appcompat-v7:23.0.1'
        implementation 'com.android.support.constraint:constraint-layout:1.0.1'
    }

The CMakelist.txt file:

    # For more information about using CMake with Android Studio, read the
    # documentation: https://d.android.com/studio/projects/add-native-code.html

    # Sets the minimum version of CMake required to build the native library.
    cmake_minimum_required(VERSION 3.4.1)

    # Creates and names a library, sets it as either STATIC
    # or SHARED, and provides the relative paths to its source code.
    # You can define multiple libraries, and CMake builds them for you.
    # Gradle automatically packages shared libraries with your APK.
    set (CMAKE_VERBOSE_MAKEFILE "ON")

    # set values from environment
    set (URHO_DISTRO $ENV{URHO_DISTRO}) #usr/local/Urho/Urho3D
    set (URHO_BUILD $ENV{URHO_BUILD}) #usr/local/Urho/Urho3D/build

    # set values from gradle
    # set by gradle in app/build.gradle file "abiFilters"
    set (URHO_ABI ${ANDROID_ABI})

    # as ANDROID_ABI comes from gradle build script, so it'd be ANDROID_BUILDTYPE (the flavor) but as 2.3 I wasn't able to
    # find anything about that. Stackoverflow question here https://stackoverflow.com/questions/43395768/how-to-get-android-build-type-debug-release-as-a-variable-in-a-cmakelists-txt
    # went unanswered.
    # FIXME: take URHO_FLAVOR from gradle.build
    set (URHO_FLAVOR $ENV{URHO_FLAVOR}) # Debug or Release

    # log used vars. HAS FU*(&%$)IN CMAKE A BETTER LOG SYSTEM?
    # TODO: human-readable log
    set (VARS ${URHO_DISTRO} ${URHO_BUILD} ${URHO_FLAVOR} ${URHO_ABI})
    file (WRITE VARS.txt)
    file (WRITE VARS.txt ${VARS})

    # creates sources list
    file (GLOB_RECURSE HEADERS ${CMAKE_SOURCE_DIR}/src/main/cpp/src FOLLOW_SYMLINKS ${CMAKE_SOURCE_DIR}/src/main/cpp/src/*.h )
    file (GLOB_RECURSE BASESOURCES ${CMAKE_SOURCE_DIR}/src/main/cpp/src FOLLOW_SYMLINKS ${CMAKE_SOURCE_DIR}/src/main/cpp/src/*.cpp )
    file (GLOB_RECURSE EXAMPLES ${CMAKE_SOURCE_DIR}/src/main/cpp/src FOLLOW_SYMLINKS ${CMAKE_SOURCE_DIR}/src/main/cpp/src/*.inl )
    # it seems it needs c library with JNI objs to avoid linking problems (android native_app_glue) 
    # when build single app with static libs
    set (TARGET ${URHO_DISTRO}/Source/ThirdParty/SDL/src/main/android/SDL_android_main.c)
    set (SOURCES ${HEADERS} ${BASESOURCES} ${EXAMPLES} ${TARGET})

    # log used sources
    file (WRITE SOURCES.txt)
    file (WRITE SOURCES.txt ${SOURCES})

    # URHO3D_HOME is Urho3D library dir
    set (URHO3D_HOME ${URHO_BUILD}/android/${URHO_FLAVOR}/${URHO_ABI})

    include_directories (BEFORE ${URHO3D_HOME}/include/
                         BEFORE ${URHO3D_HOME}/include/Urho3D/ThirdParty
                         BEFORE ${URHO3D_HOME}/include/Urho3D/ThirdParty/Bullet
                         BEFORE ${URHO3D_HOME}/include/Urho3D/ThirdParty/SDL
    )

    # create our app lib
    add_library( # Sets the name of the library.
                 native-lib

                 # Sets the library as a shared library.
                 SHARED

                 # Provides a relative path to your source file(s).
                 ${SOURCES}
                 )

    # add Urho3D static lib             
    add_library ( Urho3D
                  STATIC
                  IMPORTED
                  )

    set_target_properties( # Specifies the target library.
                           Urho3D

                           # Specifies the parameter you want to define.
                           PROPERTIES IMPORTED_LOCATION

                           # Provides the path to the library you want to import.
                           # this hack is horrible...
                           # urho3d home must be redefined as library/android/debug_OR_release/abi
                           # to account for gradle managing both flavors
                           # URHO3D_HOME=$URHO_BUILD/$URHO_PLATFORM/$URHO_FLAVOR/$URHO_ABI
                           ${URHO3D_HOME}/libs/${URHO_ABI}/libUrho3D.a
                           )

    # Searches for a specified prebuilt library and stores the path as a
    # variable. Because CMake includes system libraries in the search path by
    # default, you only need to specify the name of the public NDK library
    # you want to add. CMake verifies that the library exists before
    # completing its build.

    # log
    find_library( # Sets the name of the path variable.
                  log-lib

                  # Specifies the name of the NDK library that
                  # you want CMake to locate.
                  log )

    # this is needed if you want to change the build tipe to a specific opengl version
    # opengl2 (level9)
    find_library( gl2-lib
                  GLESv2
    )

    #native-window (sdl2) (level9)
    find_library( android-lib
                  android
    )

    # collect libraries
    set (LIBRARIES ${Urho3D} ${native-lib} ${log-lib} ${android-lib} ${gl2-lib})

    # log used libraries
    file (WRITE LIBRARIES.txt)
    file (WRITE LIBRARIES.txt ${LIBRARIES})

    # Specifies libraries CMake should link to your target library. You
    # can link multiple libraries, such as libraries you define in this
    # build script, prebuilt third-party libraries, or system libraries.

    target_link_libraries( # Specifies the target library.
                           native-lib

                           # Links the target library to the log library
                           # included in the NDK.
                           ${log-lib}
                           ${gl2-lib}
                           ${android-lib}
                           Urho3D
                           )

At line 39 is the point where I link to the sdl c++ native glue file which is contained into the Urho sources.
Problem is this setup tries to load a static Urho3d library and it won't start if you don't patch a line in app/src/main/java/com/github/urho3d/Urho3D.java like this:

    // All shared shared libraries must always be loaded if available, so exclude it from return result and all list operations below
    int startIndex = libraryNames.indexOf("Urho3DPlayer");

    // check for third-party libraries/runners different from Urho3D Player whose name we don't know,
    // so taking the first element. This way, an empty library list is going to throw an exception anyway

    if (startIndex==-1 && !libraryNames.isEmpty()) startIndex = 0;

    // Determine the intention
        Intent intent = getIntent();
        String pickedLibrary = intent.getStringExtra(SampleLauncher.PICKED_LIBRARY);

_(fu*%/&%in markup)_

But if you use a shared Urho library, it _probably_ starts without this last patch...

-------------------------

simonsch | 2018-03-07 09:00:28 UTC | #11

@johnnycable you are absolut right about everything, it was my fault not seeing you presented me basically the solution of all. For your problem you can simply use the SDLActivity of @Lumak which i used to load one certain executable. 
https://github.com/Lumak/Urho3D-Android-Project/

-------------------------

Lumak | 2018-03-07 17:24:23 UTC | #12

[quote="simonsch, post:7, topic:4066"]
Urho3D-Android-Project/Source/Samples/75_JoystickAndroid/

contains the c++ source code for the sample you build, and additionally there is

Urho3D-Android-Project/Source/ThirdParty/SDL

but it contains not the SDL library just the glue but reference, headers which are not present in the project setup. Sry if i missed something, but i don’t see where this project loads the SDL prebuilt.
[/quote]

My mistake for misleading you. I said I have a repo demonstrating how to create your own C++ executable, but should've specified that it does not link with prebuilt libraries.  You've seen the *build steps* and my repo gets added on top of Urho3D 1.7 tag -- *build step 3*.  And you do end up building the repo, which also means every library, i.e. Urho3d lib, SDL lib, etc.

edit: let me add -- the changes to SDL_android.c is request/callback process to/from SDLActiviiy to C++ which is a foundation to integrate Admob and Google Play Services. I have another thread on discourse from about two and half years ago which goes into detail on how to do that, but didn't add anything to the repo yet or not sure if I'll add them because I'm sure the API and the execution sequence has changed with the current Android SDK.

edit2: in addition, there is no prebuild Urho3D libraries that work with Android NDK as far as I know. When releasing an Android app/game you'll have to include multiple architecture support, e.g. Arm, x86, Mips, etc. Which means you'll have to build the libraries on your own, but my repo demonstrates that.

-------------------------

simonsch | 2018-03-07 09:31:56 UTC | #13

Thank you again for your support, after some hours yesterday i was finally able to get my setup working :). I think it was not misleading you me, more i wanted to work it as i want not realizing i had to manage libs and code a little bit different.

So first all prebuilts with cmake for android are complied successfully. I tried building all for armeabi-v7a and as far as i can say everything works very well, i will even try to build everything for 64 bit -> arm64-v8a. Those both are sufficient for a very large range of devices. 
(Very old architectures are not part of my development process)

Even iOS should not be a huge problem, keep in mind that the cross plattform framework Xamarin already has a official support for Urho3D via its C# wrapper. 

So for everybody who wants to get a running setup on android, i will describe the process of creating a running setup. I would recommend you using a docker container, so you can share your build crossplatform. I use a windows host which is not that good for building c++ :D.
- First, download or clone urho3d with latest stable tag (e.g 1.7) 
- Then use cmake_android shell or bat file like described, or call your own CMAKE. An overview of all available tags is given on the urho3d page;
https://urho3d.github.io/documentation/1.7/_building.html#Build_Options
- After this you can enter your build path and simply call 'make' which will create all your prebuilt static urho3d library.
- I assume now you have an already running Android Setup with SDK, NDK, JNI and that you use also CMAKE here not ndk-build.
- So the only thing you have to do take headers and the library prebuilt, copy it to the 'wherever you have your prebuilts folder', add the static library via CMAKE
- Now you also need the mentioned SDLActivity which you can copy from the Urho3D-1.7\Android\src\org\libsdl\app folder. Keep in mind you have to copy the whole path to your java src org\libsdl\app
- This activity includes your glue via JNI you will have to extend your own activity from it.
- As the SDLActivity wants an executable, you should now add a shared library in cmake based on your source code (E.g. you have a folder in your cpp/renderstuff), name it e.g. 'render.so'
- Set that name in the activity to be loaded (<-Make sure you have the right SDLActivity, @Lumak has a good SDLActivity for loading one certain .so)
- In your setup c++ source code add some urho3d example source code like the hello_gui example
- Now go to the SOURCE of SDL through SDL\src\main\android and copy the SDL_android_main.c <- this are the native callbacks which connects the SDLActivity to your c++ code. 
- Copy this into your cpp/renderstuff and add the file via cmake to render.so
- Include headers for urho3d itself and for sdl under include/Urho3D/ThirdParty/ for the SDL_android_main.c file
- In CMake you now have to link urho3d into your render.so

> target_link_libraries(render
urho3D
android
log
GLESv2
z
${ROOT_LIBRARIES})

This is it, running the app and starting the activity should load your on the fly compiled render.so. I know that are a lot of steps, i know i rushed over it, but i wanted to share my working stuff fast. If you have any questions feel free to ask.

Thx to @johnnycable which opened my eyes with his post :D.

-------------------------

simonsch | 2018-03-07 08:57:23 UTC | #14

You could try to compile the source code of the samples yourself like described by me you maybe just need the SDL_android_main.c in the source code of the samples as the needed glue for JNI.

-------------------------

