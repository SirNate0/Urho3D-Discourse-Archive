majhong | 2021-02-14 07:58:21 UTC | #1

* What went wrong:
Execution failed for task ':android:launcher-app:externalNativeBuildDebug'.
> Build command failed.
  Error while executing process ninja with arguments {-C /root/Urho3D/android/launcher-app/.cxx/cmake/debug/armeabi-v7a Urho3DPlayer}
  ninja: Entering directory `/root/Urho3D/android/launcher-app/.cxx/cmake/debug/armeabi-v7a'

  ninja: error: '/root/Urho3D/android/urho3d-lib/.cxx/cmake/debug/armeabi-v7a/lib/libUrho3D.so', needed by '../../../../build/intermediates/cmake/debug/obj/armeabi-v7a/libUrho3DPlayer.so', missing and no known rule to make it

-------------------------

WangKai | 2021-02-14 08:23:07 UTC | #3

Please see - https://discourse.urho3d.io/t/build-system-broken/6653/9

-------------------------

majhong | 2021-02-14 08:29:39 UTC | #4

Compiled successfully, I made a mistake on " URHO3D_LIB_TYPE=SHARED"

The correct way is URHO3D_LIB_TYPE="SHARED"

thanks!

-------------------------

