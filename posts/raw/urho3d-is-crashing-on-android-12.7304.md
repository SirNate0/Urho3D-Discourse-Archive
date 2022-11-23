elix22 | 2022-07-28 10:39:00 UTC | #1

This is just some information for anyone that is planing to submit a game/app to Google play.

I recently uploaded a game to Google Play Console.
During its review it failed and crashed  on an Android 12 device (Pixel 6).
After short investigation , long story short , there are some Android 12 related fixes there were introduced into SDL.
https://github.com/libsdl-org/SDL/commit/97c71371f21187f146872d41f94a5593c0a374ba

For now I downgraded my targetSdkVersion to 30 (Android 11) .
Google is still allowing it but not for long ,targetSdkVersion 31 (Android 12) will become mandatory very soon.
I plan to integrate the fix (maybe the entire latest SDL)  into one of my  branches

-------------------------

