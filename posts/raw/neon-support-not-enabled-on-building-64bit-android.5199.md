rifai | 2019-05-29 23:37:57 UTC | #1

I want my android game built with 64 bit support because of google 64 bit policy. 

I compiled 1.7.1 with URHO3D_64BIT=1. But, I always getting this error.
"NEON support not enabled"
![neon|689x148](upload://t8QAChTqYJdQBYe5KgNNZt37H5n.png) 
Am I missing something?

Thanks

-------------------------

weitjong | 2019-05-30 01:32:12 UTC | #2

I recommend you switch to Gradle build system with master branch. Having said that, I think Android arm64 build was ok with 1.7 too. Check the online doc for version 1.7 for the correct build option to use.

-------------------------

rifai | 2019-05-30 06:08:06 UTC | #3

Finally, figure it out. 
I tried to change **ANDROID_ABI=arm64-v8a**, but got error

> Unrecognized 'arm64-v8a' specified in the ANDROID_ABI option, supported  values are: "armeabi-v7a", "armeabi-v6", "armeabi

Looked at android doc, changed **ANDROID_TOOLCHAIN_NAME=aarch64-linux-android-clang** and **ANDROID_NATIVE_API_LEVEL=android-21** (minimum version).
Compiled successfully. 

Thanks weitjong.

-------------------------

