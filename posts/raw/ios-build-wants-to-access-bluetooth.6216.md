jzpekarek | 2020-06-21 17:20:15 UTC | #1

After finally getting my iOS project building again after upgrading from Urho3D 1.5 to 1.8 alpha (Xcode 11.5 on macOS Catalina), I now get the message below, which implies that Urho3D wants access to Bluetooth?  My app certainly doesn't need to use Bluetooth for anything, but maybe there is a dependency in SDL for wireless joystick controllers? I can add the usage description as the message suggests, but I was concerned that it will now prompt the user to allow access to something I don't need.

Has anyone seen this before, or no how to disable the Bluetooth dependency?

`This app has crashed because it attempted to access privacy-sensitive data without a usage description. The app's Info.plist must contain an NSBluetoothAlwaysUsageDescription key with a string value explaining to the user how the app uses this data.`

-------------------------

elix22 | 2020-06-21 18:17:13 UTC | #2

Yes it's a known crash.
Check my fix 
https://github.com/elix22/Urho3D/blob/master/CMake/Modules/iOSBundleInfo.plist.template


My advice is to use my master branch for iOS  (includes more fixes, features and samples that are not part of the Urho3D master branch)

https://github.com/elix22/Urho3D

-------------------------

jzpekarek | 2020-06-21 22:24:57 UTC | #3

Thanks elix22, can you comment on the status and plans for your master branch versus the main master branch? Is your branch more focused on iOS? Are there many known issues with iOS support in the main branch? I have been struggling for the last few weeks trying to get my iOS build working again, and it seems like perhaps iOS support hasn't been well tested in the master branch. Any insight into this would be very helpful. I just got my app running again today, but it now has many new bugs in parts that worked fine in 1.5 Urho3D.

-------------------------

elix22 | 2020-06-22 16:40:49 UTC | #4

I don't have any specific plans .
At my spare time I am fixing bugs that I find on any platform (iOS , Android , Emscripten , desktop )

My Master branch contains a major feature for iOS & macOS , Angle->Metal support , basically it's OpenGL-ES running on top of a Metal backend (amazing implementation by @kakashidinho) .
It was Integrated by me into SDL2 & Urho3D  .
You can generate Xcode projects with Metal support , **script/cmake_ios_metal.sh ,** **script/cmake_xcode_metal.sh** 
All Samples were verified on numerous iOS devices.

It also contains additional samples that were written by talented community members and I thought are worth to be added  ,  all were verified on iOS and Android.

If you find any iOS issue that can be **reproduced** also **by me** on My Master branch and it's an issue that **bugs me**  , I will fix it  (when I have the time )

-------------------------

jzpekarek | 2020-06-23 05:32:04 UTC | #5

Thanks for the feedback. I tried your branch, and unfortunately, when I try to run any of the examples on my iPad Pro, the screen is black. I didn't use the metal version, so maybe that is now a requirement for your branch? Also, the original problem with wanting to use Bluetooth seems to persist (when I ran the example, it asked me if I was ok to allow the app to access Bluetooth, even though I'm pretty sure it isn't used). On the plus side, building for iOS actually worked (I gave up trying to build the 1.8 alpha and downloaded the pre-built library, I think the iOS build process is broken in that version), although I could not use the CMAKE GUI, and had to use the build scripts (had the same problem with 1.8 alpha).

-------------------------

elix22 | 2020-06-23 06:56:55 UTC | #6

> the examples on my iPad Pro, the screen is black

I don't see any issues on my iPad (iOS version 13.3) 
Both OpenGL-ES vanilla and Angle-Metal are running fine.
What iOS version are you running ?
Please note that Apple deprecated OpenGL-ES  , so they stopped supporting it , probably they
Will remove it entirely in the future , that's the reason/motivation of integrating the Metal support.
I would suggest to try the Metal version.


> Also, the original problem with wanting to use Bluetooth seems to persist.

That's not the original problem.
Originally the app was crashing all the time , now it asks you and continues to run.
Thats part of SDL2 , I prefer to keep it for now.

-------------------------

jzpekarek | 2020-06-24 04:38:35 UTC | #7

My iPad OS is 13.51. I verified that the metal build seems to work with the examples, whereas the non-metal build (cmake_ios.sh) displays a black screen for all the examples I tried on the iPad.

One other issue I'm having, is getting my own project (with my source files) created with the cmake_ios_metal.sh script, but maybe I'm not doing something correct. I was using the project scaffolding approach shown below, where I also copied the script folder from your branch, and used the CMakeList.txt template from the HEAD instructions, with the following line added to set the URHO3D_HOME directory to where I built your branch (out of source build).

`set(ENV{URHO3D_HOME} "/Users/jpekarek/Dev/Urho3D-E22-iOS-Mtl")`

The CMake folder also comes from your branch. 

I then cd to the script directory, and run sh cmake_ios_metal.sh /MyBuildDirectory, and the script runs for a while, but ends with errors.

    <PROJECT_ROOT>/
     ├ bin/
     │  ├ Data/
     │  └ CoreData/
     ├ CMake/
     │  ├ Modules/
     │  └ Toolchains/
     ├ CMakeLists.txt
      |- script
     ├ *.cpp and *.h
     └ *.bat or *.sh

I'm not for sure that copying the script folder into my local build directory and running from there is the right approach to building, but it was the only approach I tried that seemed to work when building from the master (or other more recent branches).

A sampling of the errors are shown below. I don't understand this build process well enough to have any idea what is going on here. I don't understand why the CMake script is trying to compile and link anything, I thought it's purpose was to make an Xcode project that took care of that. Any ideas on what I did wrong? 



       Undefined symbols for architecture arm64:        
       "_OBJC_CLASS_$_MTLTextureDescriptor", referenced from:
            objc-class-ref in libUrho3D.a(mtl_resources.o)
        "_OBJC_CLASS_$_MTLRenderPassDescriptor", referenced from:
            objc-class-ref in libUrho3D.a(mtl_command_buffer.o)
        "_OBJC_CLASS_$_MTLFunctionConstantValues", referenced from:
            objc-class-ref in libUrho3D.a(mtl_render_utils.o)
            objc-class-ref in libUrho3D.a(ProgramMtl.o)
        :
        :
       MANY LINES OF ERRORS
       :
       ld: symbol(s) not found for architecture arm64

      clang: error: linker command failed with exit code 1 (use -v to see
      invocation)

      Showing first 200 notices only

      ** BUILD FAILED **

      The following build commands failed:

      	Ld Debug/cmTC_04757.app/cmTC_04757 normal arm64

      (1 failure)

-------------------------

elix22 | 2020-06-24 07:52:51 UTC | #8

[quote="jzpekarek, post:7, topic:6216"]
project scaffolding
[/quote]

Yep , looks like an issue , I will look at it during the weekend.

In the meantime you can add your project  source into the Samples folder and build it as part of the samples. (don't forget to add your assets into bin/Data , bin/CoreData)

Regarding the black screen on vanilla OpenGL-ES , I will upgrade to 13.5.1 once Xcode 12 will go out of the beta phase.
But as I mentioned the right approach would be to start using the Metal solution (Apple abandoned OpenGL-ES) .

-------------------------

elix22 | 2020-06-24 16:45:24 UTC | #9

I had some free time today ,  fixed the project scaffolding error .
Part of my master branch
Doing the same procedure you described should work now

https://github.com/elix22/Urho3D

-------------------------

jzpekarek | 2020-06-25 06:12:49 UTC | #10

Thanks for the update, after rebuilding everything, I was able to create my own project (had to copy Default-568@2x.png into my textures directory to get rid of an error, but otherwise worked).

Now for the bad news. It appears that instancing doesn't work in my app in the metal build (I found the same problem in Urho1.7.1, that was fixed in the 1.8alpha and main branch). If I place more than one instance of the same model with the same material, then all instances disappear. I tried an example though (04_StaticScene) that does the same thing, and it worked fine, so  not sure what is going on.

The other issue, which I was hoping was fixed, is it seems something is wrong with the messaging system on iOS. This is a problem in 1.8alpha, the current Master branch, and your branch. It works fine on Windows, but some messages seem to be lost on  iOS, For example, I have a custom control that subscribes to E_DRAGBEGIN and E_DRAGEND as shown below. The handler function for E_DRAGBEGIN works, but the handler for E_DRAGEND doesn't get called when the touch event is released (this all worked fine in version 1.5, and it also works fine in all versions I tested in Windows). There are other UI events that are not working as well on iOS (wrong function called when a button is pressed, nothing happening when other buttons are pressed). Not sure if anyone else is seeing these issues in iOS. Maybe if I get some time I'll see if I can do a simple modification to one of the examples to see if I can get the problem to repeat on something I can share more easily.

    SubscribeToEvent(m_outer_circle, E_DRAGBEGIN, URHO3D_HANDLER(JZTouchCtrlWidget, HandleDragBegin));
    	SubscribeToEvent(m_outer_circle, E_DRAGEND, URHO3D_HANDLER(JZTouchCtrlWidget, HandleDragEnd));

-------------------------

elix22 | 2020-06-26 09:51:53 UTC | #11

I fixed the black screen issue on iOS OpenGL ES vanilla  , part of my master branch.

>  It appears that instancing doesn’t work

I would need more information to tackle it  , some kind of code snippet , models ,textures and materials used .
Did you try "20_HugeObjectCount" or "58_GeomReplicator" samples ?

> some messages seem to be lost on iOS

Yes I am aware of it  , in my todo list of fixes.

-------------------------

jzpekarek | 2020-06-27 04:57:50 UTC | #12

It might take me a few days, but I'll try to see if I can reproduce it in something that is easier to reproduce. When I saw the instancing issue previously (version 1.7.1), it also showed up in the examples that used instancing (like 04_StaticScene), but those same examples are working with your branch, so not sure what I'm doing that is different. 

As for the message problems, I'm trying to debug that as well. I have a working version on Windows where I have stepped through the same code as on the iOS side, and so far, it seems to be related to UI::ProcessClickEnd, where in the iOS build, that function is first called with cursorVisible==false, which removes the dragElements_ in the UI class, which causes the next call to the same function to fail. In the Windows build, the first call to UI::ProcessClickEnd doesn't have false set for curosrVisible, which ends up with the event being handled correctly. I may not get back to this for a few days, but thought what I found might be useful.

-------------------------

elix22 | 2020-06-27 13:21:40 UTC | #13

I fixed the iOS ui drag issue , part of my master branch
I used "37_UIDrag" sample to verify it.

-------------------------

jzpekarek | 2020-06-29 05:14:56 UTC | #14

I got your changes, but it didn't fix the problem in my application. I think there is something more fundamental wrong, as there are other problems related to touch events on iOS. For example, I have toolbar buttons that call the wrong functions, and the buttons on forms don't work anymore (like the cancel button, I have to kill the app as once a form is opened, none of the buttons work, and I can't exit). I was hoping to build against a previous stable version of Urho3D on iOS to see if I could figure out what changed, but I'm finding it very difficult to get older versions of Urho3D to build on the latest OS and Xcode. Since I was having troubles with 1.7.1, I decide to try to go back to 1.6, and was working through many compiler issues, but got stuck on the error message below in _size_t.h, maybe someone else has seen this and knows how to fix it (this occurs when trying to compile several SDL files). I'm guessing that all the changes in Apples OS and Xcode aren't compatible with older versions, but I don't know if there is some relatively easy fix. 

`Typedef redefinition with different types ('__darwin_size_t' (aka 'unsigned long') vs 'unsigned int')`

-------------------------

jzpekarek | 2020-07-05 01:03:42 UTC | #15

I figured out what was wrong with the touch events. Apparently in SDL2.0.4, iOS (and presumably Android), generate mouse messages for touch events by default (I don't think that was true in the earlier version of SDL that Urho3D 1.5 used). In my application, I run the same code on Windows and iOS, so I had both mouse and touch event handlers, and they started both getting called, which caused a lot of bad behavior. I found this link that talks about the problem.

https://stackoverflow.com/questions/34465681/sdl2-events-on-mobile

So for me, the fix was to call the following in my initialization code. Even though the hint appears to be specific to Android, it fixed my problem on iOS as well.

SDL_SetHint(SDL_HINT_ANDROID_SEPARATE_MOUSE_AND_TOUCH,"1");

I'll create a new post with a more accurate title in case someone else runs into this problem.

-------------------------

weitjong | 2020-07-05 04:27:23 UTC | #16

A post was merged into an existing topic: [Redundant handling of mouse and touch events on mobile platforms](/t/redundant-handling-of-mouse-and-touch-events-on-mobile-platforms/6242/2)

-------------------------

