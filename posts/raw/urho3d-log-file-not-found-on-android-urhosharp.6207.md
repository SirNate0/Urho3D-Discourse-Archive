najak3d | 2020-06-16 17:30:26 UTC | #1

We are using UrhoSharp.  When we deploy to Android, we currently cannot find the Urho3D.log file anywhere (we're programatically traversing all folder paths looking for it).   I thought this file was supposed to be written to the application folder itself -- but it's not (nor any folders beneath it).

UrhoSharp does not expose any of the Logging API.

Our main issue is that when Urho is malfunctioning or having issues - we currently have no way of reading this Urho3D.log file.

-------------------------

Pencheff | 2020-06-16 20:49:23 UTC | #2

Android logging is done using __android_log_print https://developer.android.com/ndk/reference/group/logging, so you can view the log using logcat.

-------------------------

najak3d | 2020-06-17 05:36:38 UTC | #3

THANK YOU!  This helped a lot.   It's not perfect, because the info shown in this Logcat seems less informative than what I found in the Urho3D.log.   Namely, when I have shader compiler errors, it doesn't tell me the Line# now, which makes for unnecessary extra guesswork.

-------------------------

