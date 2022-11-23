Rook | 2019-12-06 11:03:44 UTC | #1

Hello,
This is just a quick tip for something that held me up for a day when I switched from Windows to Ubuntu.

**Problem**: Fullscreen applications in linux Ubuntu 19.04 only show a black screen.

**Description**: I had very few issues building Urho in linux once I had the requisite packages installed and all of the samples worked well until I tried to run the PBRDemo.sh and NinjaSnowWar.sh which are both fullscreen apps. The display went completely black although you could hear the Ninja demo clearly running in the background. Alt Tabbing to a window created a display and exiting the application showed the last rendered frame before the application terminated.

**Solution**: The problem was resolved when I did a 'sudo apt-get install libgles2-mesa-dev libxt-dev libxaw7-dev' 'sudo apt-get install nvidia-cg-toolkit libsdl2-dev doxygen' (steps found on an Ogre3D build guide website), ran cmake_generic.sh and ran make again. I suspect it was the libsdl2-dev that actually corrected the issue.

I don't know if this will help anyone out, if you have this issue though perhaps it will.

Rook

-------------------------

