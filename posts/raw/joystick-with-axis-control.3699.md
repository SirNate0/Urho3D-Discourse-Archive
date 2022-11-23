Lumak | 2017-10-31 03:27:53 UTC | #1

https://github.com/Lumak/Urho3D-Joystick

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/bf0a844ac5ce703257ab2502acf59dd8da014d2d.png[/img]

-------------------------

yushli1 | 2017-10-31 03:30:40 UTC | #2

That looks nice. Thank you for sharing it.

-------------------------

Lumak | 2017-10-31 14:25:45 UTC | #3

You're welcome. This repo should make mobile development more convenient.

Also updated the repo late last night, so you might want to grab the latest.

-------------------------

Lumak | 2017-11-01 18:59:37 UTC | #4

repo updated - refactored ScreenJoystick struct.

I'm considering adding d-pad button images to the Joystick.png and perhaps, resizing it to 256x256.  
Any thoughts?

-------------------------

Lumak | 2017-11-01 20:19:41 UTC | #5

Here's what I'm thinking:

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/00c42e17ec3561f7e943c046d9b5afc3f432416e.png[/img]

-------------------------

Miegamicis | 2017-11-21 09:18:14 UTC | #6

This was exactly what I needed. Managed to get it working with AngelScript by exposing GameController object to scripting. I can add a PR later with the AngelScript binding code, if needed. Script binding seems to be a hot topic lately.

-------------------------

Lumak | 2017-11-21 18:51:13 UTC | #7

That's good to hear. I don't support scripting language in my repo, but perhaps, you can contribute to Urho3D engine with your work.

-------------------------

Lumak | 2018-01-26 23:58:07 UTC | #8

I added PS4 controller mapping for Android.  I'm uncertain about how Android generates GUID but would like to verify that it's consistent across different API levels. API level that I tested is **Android 4.1.2, API 16**.

To enable the PS4 controller testing, uncomment the line 38, ```//#define TEST_PS4_CONTROLLER``` -- **edit:** in GameController.cpp.

I appreciate anyone with a PS4 controller and Android to verify that it works and mention your API lvl. Thanks.

----------------------------
Edit: Disregard. I got my answer.

-------------------------

