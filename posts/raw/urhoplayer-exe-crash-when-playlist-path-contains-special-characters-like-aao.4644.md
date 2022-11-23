lahiruzz | 2018-11-06 04:17:09 UTC | #1

 I need to render the movie. So I'm passing arguments for example (urhoplayer.exe \"D:\\Projects\\övrigt\\playlists\\20181105--103658--b2995b35-5383-466e-bdec-58625370912f\" -x 600 -y 800 -WindowPositionX 7 -WindowPositionY 29) to uhro player. but it crash the urhoplayer. This is due to special characters in my playlist path. Is there any solution available for this ?

-------------------------

weitjong | 2018-11-06 01:28:07 UTC | #2

FWIW, it looks like it is Windows-specific problem. I could not reproduce it locally on Linux host, at least on my Fedora system.

```
[weitjong@igloo bin]$ pwd
/tmp/övrigt/build/native/bin
[weitjong@igloo bin]$ ./Urho3DPlayer /tmp/övrigt/build/native/bin/Data/Scripts/01_HelloWorld.as
[Mon Nov  5 21:53:00 2018] INFO: Opened log file /home/weitjong/.local/share/urho3d/logs/01_HelloWorld.as.log
[Mon Nov  5 21:53:00 2018] INFO: Created 3 worker threads
[Mon Nov  5 21:53:00 2018] INFO: Added resource path /tmp/övrigt/build/native/bin/Data/
[Mon Nov  5 21:53:00 2018] INFO: Added resource path /tmp/övrigt/build/native/bin/CoreData/
[Mon Nov  5 21:53:00 2018] INFO: Adapter used nouveau NVC8
[Mon Nov  5 21:53:00 2018] INFO: Set screen mode 1920x1200 fullscreen monitor 0
[Mon Nov  5 21:53:00 2018] INFO: Initialized input
[Mon Nov  5 21:53:00 2018] INFO: Initialized user interface
[Mon Nov  5 21:53:00 2018] INFO: Initialized renderer
[Mon Nov  5 21:53:00 2018] INFO: Set audio mode 44100 Hz stereo interpolated
[Mon Nov  5 21:53:00 2018] INFO: Initialized engine
[Mon Nov  5 21:53:00 2018] INFO: Compiled script module Scripts/01_HelloWorld.as
```

-------------------------

lahiruzz | 2018-11-06 04:20:01 UTC | #3

I'm running on this Windows 10.

-------------------------

Sinoid | 2018-11-06 05:23:53 UTC | #4

Anything in the log? `Users/__YourUserName__/AppData/Roaming/Urho3D/logs/__ProgramYouRan___.txt`

-------------------------

lahiruzz | 2018-11-06 07:42:51 UTC | #5

No logs. I'm just passing command line arguments to urho player.

urhoplayer.exe “D:\Projects\övrigt\playlists\20181105–103658–b2995b35-5383-466e-bdec-58625370912f” -x 600 -y 800 -WindowPositionX 7 -WindowPositionY 29

-------------------------

lahiruzz | 2018-11-13 14:31:07 UTC | #6

I found why this is happen on windows.
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/IO/FileSystem.cpp (`bool FileSystem::FileExists(const String& fileName) const`) 
here we have this check statement 
```
#ifdef WIN32
    DWORD attributes = GetFileAttributesW(WString(fixedName).CString());
    if (attributes == INVALID_FILE_ATTRIBUTES || !(attributes & FILE_ATTRIBUTE_DIRECTORY))
        return false;
```
 and it returns null if path with contains letters like ÅÄÖ

-------------------------

Sinoid | 2018-11-13 23:20:39 UTC | #7

What's your system codepage?

Switching to using the correct OS functions (`MultiByteToWideChar`) in the WString consversion will most likely fix it. The current EncodeUTF16 functions are codepage ignorant.

-------------------------

