MrBushy | 2018-08-21 06:55:56 UTC | #1

Hi all,
I was wondering if anyone could help me with an issue building Urho3D on Windows 10. I'm using CMake GUI to generate a Visual Studio 2017 configuration. When building the resulting VS solution, I get the following error in the Urho3D project:

IOAPI.obj : fatal error LNK1179: invalid or corrupt file: duplicate COMDAT '??_9File@Urho3D@@$b7AE'

I'm using VS Community 2017 v15.8.1, latest download of Urho3D-1.7.zip from the website.

Default VS build configuration is Debug/Win32.

If anyone has come across this, any advice would be really appreciated!
Thanks.

-------------------------

Miegamicis | 2018-08-21 06:58:30 UTC | #2

Others have faced the same problem using latest Visual Studio 2017
Issue here: https://github.com/urho3d/Urho3D/issues/2362

-------------------------

MrBushy | 2018-08-21 07:03:50 UTC | #3

Ah, thanks for your quick reply!

-------------------------

