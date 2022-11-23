projector | 2017-09-24 17:30:26 UTC | #1

All Urho3D iOS apps(as well as the Urho3d examples) shows the blank screen with battery status at the top right corner after showing launch image and before the loading/initialisation is completed. The duration of showing battery status depends on how long the device takes to finish the initialisation/loading, it could be fraction of second or sometimes few seconds.

I couldn't find a way to hide the battery status while loading, "hide status bar" is already ticked in xcode, I'm at the middle of my mobile game development, I should start thinking about possible polishing work, anyone here knows how to make Urho3d app not to show battery status?

-------------------------

weitjong | 2017-09-24 13:38:24 UTC | #2

There is one thing in my todo list that I haven't got time to do it. You may want to try to sync the `CMake/Modules/iOSBundleInfo.plist.template` file in Urho3D project with the latest version from CMake itself. Do not just replace as our version contains Urho-specific stuff in there. HTH.

-------------------------

projector | 2017-09-26 13:37:36 UTC | #3

I just checked with the AppleInfo.plist template from latest Cmake, in fact it's pretty much the same(except for some settings I believe are Urho-specific). 

However I managed to hide the battery status by comparing the .plist file with my previous iOS game. I have modified iOSBundleInfo.plist.template and tested it( you can download from http://windigig.com/file_temp/iOSBundleInfo.plist.template ), the following are the added lines :

    <key>UIViewControllerBasedStatusBarAppearance</key>
    <false/> 

I hope you can consider to upload this to Urho3D main branch as in general it makes more sense for mobile games to hide the battery status.

-------------------------

weitjong | 2017-09-26 00:02:17 UTC | #4

Yes, I think that makes sense.

-------------------------

