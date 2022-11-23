yiown | 2017-01-02 01:09:52 UTC | #1

Hi, i have been trying to build my project for android without luck.
I have already build it for native windows, native linux, and emscripten but for android i am lost.
Plus the docs are obscure and misleading.
I have tried with rake, cmake, followed several tutorials and remade my Urho3D setup countless times.

NOT WORKING Steps i tried:
1. properly install NDK, SDK, JDK, with latest API (23) and properly env vars.
2. git clone urho3d
3. cmake it for android
4. compile it for android
--- if i run ant release it creates an apk at this point, but not my project's apk ---
5. rake scaffolding my project
6. go to my project's scaffolding
8. symlink my sources, modify CMakeLists.txt to include my sources
7. rake cmake it for android
8. rake make it for android
--- at this point it seems compiled, i see .o files for my sources, but "ant release" will fail and even "android update" since neither have the required xml files.

Can you clarify how to compile a user's project based on Urho3D ?
Thanks

-------------------------

Lumak | 2017-01-02 01:09:53 UTC | #2

I found the developers suggested method of building for Android some what cumbersome and used an alternative method, as described here [url]http://discourse.urho3d.io/t/deploying-urho3d-to-android-studio-in-windows/1107/1[/url].

Try it at your own risk, as the suggested method might be better for you.

Edit: oh wait, its Linux.  I didn't test the procedure that I describe on Linux, sry.

-------------------------

yiown | 2017-01-02 01:09:53 UTC | #3

yeah, i am looking for a command line solution, i can automate into a script.

i haven't tried it through android studio... nice to know. thanks.

-------------------------

weitjong | 2017-01-02 01:09:53 UTC | #4

In the documentation for the rake scaffolding task, there is a note/warning that at the moment it does not work well to scaffold for Android platform yet. This has been discussed before. It requires some undocumented post steps manually. But someone has posted the steps that worked for him in the forum. I don't have the link ready with me but it should be searchable.

-------------------------

Sir_Nate | 2017-01-02 01:09:56 UTC | #5

I didn't use rake but I got mine to work decently through the command line. I'm not sure how well it handles symlinked files though -- I seem to recall that it wouldn't include my assets if they were symlinked instead of actual files). It's been a while, but I think my steps were something like:
Clone Urho Source and build for Android, setting the NDK variables as required,
Copy my project so that stuff didn't get potentially messed up by CMake
Set the URHO_HOME variable to the build location of Urho from above ( I think you can do this in the CMakeLists.txt file -- 
[code]
set (URHO3D_HOME H:/Projects/Urho/UrhoRepo/builds/android-samples)
set (ANDROID_NDK H:/Tools/Android/android-ndk-r10e)
[/code]
but I'm not certain if it still works like that, as that was old stuff from my last computer, and now I just export URHO3D_HOME, so...)
[code]
android update project -p . -t [target form android list targets]
make -j8
ant debug
ant installd # while the device is connected
[/code]

You may have to play around with directory structure some, especially with assets, but I get a libs/armeabi-v7a/lib[Project].so file.
Also note that you can open the apk as an archive (as a jar, I think), and then you can explore what is/isn't included.
And note that I have an in-source build with the CMake Source and Build directories the same for my project.

-------------------------

weitjong | 2017-01-02 01:09:56 UTC | #6

I did a search just now and it came out as the first result. [topic378.html](http://discourse.urho3d.io/t/solved-using-scripting-with-android/386/1). The link is kind of dated, so YMMV.

-------------------------

