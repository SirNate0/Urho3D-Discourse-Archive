shipiz | 2017-05-20 23:43:37 UTC | #1

So how would i add platform specific classes? i.e in generated xcode project for iOS i would like to add analytics/ads integration written in objC/swift, or maybe i would like to have additional library only for iOS only.

-------------------------

weitjong | 2017-05-21 00:54:27 UTC | #2

You can get the inspiration from reading the code from SDL library. HTH.

-------------------------

shipiz | 2017-05-21 08:48:39 UTC | #3

yeah i can see the iOS specific code in SDL, but is there any way to access it from my project without modifying engine code ?

Platform specific code should be exposed in game project.

-------------------------

weitjong | 2017-05-21 10:30:33 UTC | #4

Perhaps you got me wrong. Your new classes should still be in your own project. You can have them in a separate subdir with a separate CMakeLists.txt for instance. Then in your main CMakeLists.txt you can decide whether to include that subdir or not based on certain condition is true. This is not the only way, for sure. You can also just mix the Objective-C code with C/C++ code in a same directory if there are only a few classes to warrant for a new subdir. See how Urho implements its FileWatcher for example.

-------------------------

