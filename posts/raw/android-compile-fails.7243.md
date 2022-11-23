feresmu | 2022-04-25 08:46:08 UTC | #1

Hi.
I tried to compile urho3d for Android.
I use docker like https://urho3d.io/docs/getting-started/quick-start:
git clone https://github.com/urho3d/Urho3D.git
cd Urho3D
script/dockerized.sh android rake build install

But it fails:
> Task :android:launcher-app:externalNativeBuildDebug FAILED

Build Urho3DPlayer_armeabi-v7a

ninja: error: '/home/user/Urho3D/android/urho3d-lib/.cxx/cmake/debug/armeabi-v7a/lib/libUrho3D.so', needed by '../../../../build/intermediates/cmake/debug/obj/armeabi-v7a/libUrho3DPlayer.so', missing and no known rule to make it

seems that it need libUrho3D.so but I think that is libUrho3D.a what is needed.

I have follow the instructions of https://urho3d.io/docs/getting-started/quick-start
Is there something wrong in the docker file or I do someting wrong?
Someone can compile urho3d for Android?

-------------------------

SirNate0 | 2022-04-25 19:15:10 UTC | #2

I don't use docker, I just installed it to try and debug this. As such, I have no idea how to fix the issue (I also encountered it), but doing a shared build instead I got it to build successfully. Just add  URHO3D_LIB_TYPE=SHARED to the end of the dockerised.sh call.

I hope that helps.

-------------------------

feresmu | 2022-04-26 20:04:54 UTC | #3

Hi.
It works, thank u.

I tried to do the same with Android Studio (it fails the same way) but with URHO3D_LIB_TYPE=SHARED in grandle.properties file or -PURHO3D_LIB_TYPE=SHARED in File/Settings/Command-Line Options doesn't works.

The only way it works was changed all libUrho3D.so with libUrho3D.a in all files, but is a bad idea.

 Where I must set URHO3D_LIB_TYPE=SHARED in Android Studio?

-------------------------

weitjong | 2022-05-02 14:43:21 UTC | #4

It has been awhile since I last checked the CI/CD workflow in our project GitHub action. But based on these logs from the last build against the main branch, I am sure both STATIC and SHARED lib type are still working fine.

 https://github.com/urho3d/Urho3D/runs/6225610854?check_suite_focus=true#step:8:8763
 https://github.com/urho3d/Urho3D/runs/6225610954?check_suite_focus=true#step:8:9319

The difference between these two jobs are one of them got the "URHO3D_LIB_TYPE" env-var defined to "SHARED". Urho3D prefers "STATIC" by default.

[quote="feresmu, post:3, topic:7243"]
Where I must set URHO3D_LIB_TYPE=SHARED in Android Studio?
[/quote]
Try this. Export this env-var in your ~/.bash_profile, relogin, and launch the IDE again.

Or with CLI.

```
URHO3D_LIB_TYPE=SHARED script/dockerized.sh android rake build install
```

-------------------------

feresmu | 2022-05-06 08:24:25 UTC | #5

Hi.
It works.
I run a command window and do:
set URHO3D_LIB_TYPE=STATIC (I prefer static)
\Program Files\Android\Android Studio\bin\studio64.exe

Perhaps it must to be in https://urho3d.io/documentation/HEAD/_building.html

-------------------------

