Bluemoon | 2019-11-22 09:31:50 UTC | #1

Seriously I wish the above subject exists. 

I've really been finding it very difficult building Urho3D for Android on my system, I've tried the normal process and also tried using DBE all to no avail. My last resort is the official Urho3D builds hosted on sourceforge, unfortunately the last android build I can see there is that of v1.7, there is none for v1.7.1 nor for v1.8-alpha. And the snapshot  has not really been including android builds.

I just want to get the libs and do some work on android.

Urho3D would really excel in android game development, focus needs to be channeled that areas. 
Equally, making it a little bit easier to obtain the android build and startup work with it will immensely help alot

-------------------------

orefkov | 2019-11-22 11:53:14 UTC | #2

What problem with android builds?
Install android sdk and ndk. I create domake.cmd file in root folder with this content

    set JAVA_HOME=c:\Program Files\Java\jdk1.8.0_181
    set ANDROID_HOME=e:\Users\orefkov\AppData\Local\Android\Sdk
    call gradlew.bat -PURHO3D_GLES3=1 -PURHO3D_ANGELSCRIPT=1 -PURHO3D_LUA=0 -PURHO3D_DATABASE_SQLITE=1 -PURHO3D_LIB_TYPE=STATIC -PURHO3D_SAMPLES=0 -PANDROID_ABI=armeabi-v7a,arm64-v8a assembleRelease

and run it. You wil got android\urho3d-lib\build\intermediates\cmake\release\obj\arm64-v8a\libUrho3D.a and android\urho3d-lib\build\intermediates\cmake\release\obj\armeabi-v7a\libUrho3D.a, use it on own android project.

You must write your pathes and can choice different options in build command, of course.

-------------------------

johnnycable | 2019-11-22 16:17:24 UTC | #3

Android is the most convoluted pipeline of them all. Linux over Java over c++. Dumbasses. No surprise you don't get it simply. Forum are full of questions about it...
Try again, you'll win in the end.

-------------------------

Bluemoon | 2019-12-06 13:35:33 UTC | #4

Thanks alot this works. I was finally able to build for android without any issue.

However I'm more of proposing for a simple out of box Urho3D SDK for android, more like collection of built libs and docs that any newbie can grab and start doing some stuff with. 

The prospect of having to go through the build process and figuring out how to put the moving parts together inorder to create a simple "Hello World" for android can be such a daunting task for some.

-------------------------

drohen | 2020-10-11 21:28:04 UTC | #5

Hi Bluemoon, care to share what you did to get it to work?

-------------------------

Bluemoon | 2020-10-12 17:36:50 UTC | #6

Hello @drohen welcome to our community. 

This really helped:

https://discourse.urho3d.io/t/urho3d-android-sdk/5734/2?u=bluemoon

Also it would be nice to know which area you are having difficulty so I can help out better

-------------------------

