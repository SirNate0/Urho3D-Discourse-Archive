elix22 | 2020-03-30 11:28:22 UTC | #1

Unfortunately having some spare time during these uncertain days. 
I started a new thread on Metal support because the old one is too long and some of it is obsolete 

I have created a development branch in my GitHub repository
https://github.com/elix22/Urho3D/tree/dev

 With the following enhancements

* The amazing work done by @kakashidinho' , Angle-Metal backend implementation for Apple's devices .

* Samples created by @Lumak and @Modanung , please pay attention to the licensing terms of each sample, specifically @Modanung’s samples .

You can clone it : **git clone**  https://github.com/elix22/Urho3D.git **-b dev**

Creating XCode projects with Metal enabled use  the **-DURHO3D_ANGLE_METAL=1** switch 
In addition there are 2 new scripts in the script folder  that will create XCode with Metal enabled projects , **cmake_xcode_metal.sh** and  **cmake_ios_metal.sh**


Enjoy and take care

-------------------------

kakashidinho | 2020-03-31 10:49:58 UTC | #2

Just FYI,
I have implemented most of important features of OpenGL ES 3.0 on top of metal (uniform buffer, multiple render targets, depth sampler, etc). But I'm not sure when will the [OpenGL ES 3.0 PR](https://github.com/urho3d/Urho3D/pull/2536) be merged into master so that ES 3.0 Metal implementation could be used.

-------------------------

elix22 | 2020-04-10 12:26:33 UTC | #3

I merged @kakashidinho work on GLES 3.0 into my dev branch  .
Basically it's @orefkov  support for GLES 3.0 running on top of @kakashidinho Metal support for GLES 3.0

By default GLES 2.0 is enabled .
To enable GLES 3.0 use the build option **URHO3D_GLES3=1**
In addition if you wish to run it on top of Metal (**only Apple devices**)  , use the build option  **URHO3D_ANGLE_METAL=1**

Android : 
**URHO3D_GLES3=0 or nothing** => GLES 2.0 enabled
**URHO3D_GLES3=1** => GLES 3.0 enabled

iOS:
**URHO3D_GLES3=0 or nothing**  =>  GLES 2.0 vanilla enabled
**URHO3D_GLES3=1** => GLES 3.0 vanilla enabled
**URHO3D_GLES3=0 or nothing , URHO3D_ANGLE_METAL=1**  => GLES 2.0 on top of Metal
**URHO3D_GLES3=1 , URHO3D_ANGLE_METAL=1**  => GLES 3.0 on top of Metal
 
**Please note that it's experimental .**
**For production projects I would recommend to keep using GLES 2.0**

-------------------------

elix22 | 2020-04-21 13:56:03 UTC | #5

I added a new sample 65_SamplyGame ,  it's a small cool game , reminds me of  ShootySkies.
It's an interpretation (port)  of mine for a game that was originally written by Xamarin for UrhoSharp (in C#)

https://github.com/elix22/Urho3D/blob/dev/bin/Data/SamplyGame/Splashscreen.png?raw=true

I wrote the logic in Angelscript   and it runs nicely on mobile devices.
There was a screen orientation issue on iOS , portrait mode was not supported , fixed it.

A link to my dev branch 
https://github.com/elix22/Urho3D/tree/dev

In addition , if you want to try it  on your Android device.
I generated an Android APK with all the samples (including this one)
https://drive.google.com/open?id=19_feFQS18ePSScwtw-7ynj5XWuFLEtoS

-------------------------

elix22 | 2020-04-30 14:12:26 UTC | #6

I added a new demo sample , 66_SparkDemo , utilizing the SPARK particle engine.
Was originally written by @dakilla .
Verified on Windows , Android , macOS, iOS (OpenGL , Metal)

The source code can be found in my dev branch 
https://github.com/elix22/Urho3D/tree/dev
 
Android APK 
https://drive.google.com/file/d/19_feFQS18ePSScwtw-7ynj5XWuFLEtoS/view?usp=drive_open

-------------------------

elix22 | 2021-02-10 09:53:16 UTC | #7

I up-merged latest metal-angle branch  (from upstrem repo ,  @kakashidinho )
I enabled high DPI support for Metal  (both desktop and iOS) 
I made several  scaling fixes to support high DPI .

Can be found in my Master branch , you can read the wiki on how to compile .

https://github.com/elix22/Urho3D


https://github.com/elix22/Urho3D/wiki/Angle-using-Metal-backend

-------------------------

