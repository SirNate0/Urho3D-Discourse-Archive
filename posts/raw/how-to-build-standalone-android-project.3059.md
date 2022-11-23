artgolf1000 | 2017-04-27 04:00:55 UTC | #1

Hi,

I never tried android project before, I can build and run Urho3D's samples on the android phone according to the document, but I don't know how to run my own standalone project on the android phone.

I simply copied the subdirectory of 'Android' to my own project, and generate project with cmake_android.sh, then built the project, there are no errors in the 'android update project' and 'make' steps, but when I run the last step 'ant debug', there are errors:

BUILD FAILED
/Users/nob/NVPACK/android-sdk-macosx/tools/ant/build.xml:649: The following error occurred while executing this line:
/Users/nob/NVPACK/android-sdk-macosx/tools/ant/build.xml:694: null returned: 1

By google search, it says that I need a clean project, so I deleted the whole project and tried again, this time the issue disappeared, I can get an apk file now.

But when I installed the apk file to the android phone with 'ant installed myown.apk', it always terminated immediately when launched.

I tried to delete all useful codes to let the app do nothing, but it still crashes.

Do I need to do something else?

-------------------------

SirNate0 | 2017-04-27 04:00:17 UTC | #2

Try debugging it and see what is happening. There is the possibility it is not actually added your game's .so to the apk, so it isn't finding it because of that and it is terminating because there is nothing for it to run. Alternatively, it could be crashing due to some other error, but you'd have to look at the log (possibly) or debug it (that should find it more reliably) to see.

-------------------------

artgolf1000 | 2017-04-27 05:11:26 UTC | #3

Thanks for your hint, it really because of the shared library, I renamed it to 'libUrho3DPlayer.so', everything is OK now!:relaxed:

-------------------------

