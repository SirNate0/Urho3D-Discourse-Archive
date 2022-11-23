xarpus | 2017-07-06 14:26:39 UTC | #1

Hello,
I am trying to generate Android build on Linux, but I keep getting this error
"include android/native_window_jni.h ": No such file or directory
I believe that there is some step that I keep missing.
This is what I am doing so far:
1. cloned urho3d from repository
2. open cloned directory and make directory called "Android_Build"
3. open new directory in terminal
4. run cmake .. -DANDROID=1 from terminal
5. make -j2

I do have latest Android SDK and NDK on my computer , and I've exported them as environment variables.
Their locations are "/home/user/Android/Sdk/" and "/home/user/Android/Sdk/ndk-bundle".
I've also tried to add "-DANDROID_ABI=arm64-v8a" flag , but CMake throws warning that it is not used by project.

-------------------------

kostik1337 | 2017-07-06 15:01:41 UTC | #2

Did you set environment variable ANDROID_NDK? It should point to directory with NDK

-------------------------

xarpus | 2017-07-06 16:43:30 UTC | #3

Yes , ANDROID_NDK points to /home/user/Android/Sdk/ndk-bundle.

-------------------------

weitjong | 2017-07-07 06:28:45 UTC | #4

[quote="xarpus, post:1, topic:3326"]
I've also tried to add "-DANDROID_ABI=arm64-v8a" flag , but CMake throws warning that it is not used by project.
[/quote]

That error indicates to me that you did not use CMake/Android toolchain file. Use the provided "cmake_android.sh" script to fix this or pass the ```-DCMAKE_TOOLCHAIN_FILE=$TOOLCHAINS/Android.cmake``` on your own when you want to invoke the vanilla "cmake" CLI command.

-------------------------

