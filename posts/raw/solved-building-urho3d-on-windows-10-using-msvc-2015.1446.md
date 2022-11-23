christianclavet | 2017-01-02 01:07:46 UTC | #1

Hi.

I'm trying to build Urho3D on Windows 10, using MSVC Community 2015.

It build correctly if I use the command line. But I would like to activate options like 64bit, LUA, Examples, etc.
I used the CMAKE GUI to activate theses options and tried to rebuild. 

I am able to activate and build with most options, but for some unknow reason there is no way my MSVC project will build in 64bit. The project will display Win32 and will fail to compile. If I remove the 64bit option, I can build and compile. Can you help?
What do I type when I want to add options from the command line?

-------------------------

rasteron | 2017-01-02 01:07:46 UTC | #2

So the [b]-DURHO3D_64BIT=1[/b] option does not work? You should file an issue then. :slight_smile:

-------------------------

weitjong | 2017-01-02 01:07:46 UTC | #3

It happens on any Visual Studio versions on any Windows versions. This is a known problem that is specific to the CMake/Visual Studio generators. Unlike other generators where you can change the already configured/generated build tree from 32-bit to 64-bit and vice versa, the VS generators come in two different flavors: "vanilla" and "Win64" that once the build tree has been generated with one of these, it must stay to use the initially configured 32-bit or 64-bit (not changeable). You have to use two different build trees to manage both separately. Or if you really have to use just one build tree then probably you can use the cmake_clean.bat to clean all the CMake caches first before switching (not tested).

-------------------------

christianclavet | 2017-01-02 01:07:46 UTC | #4

Hi! Thanks for the inputs! 

Using the GUI to set the option work. But as Weitjong said, the configuration cache must be made directly for 64bit.

So done this:
cmakeVS2015 ../Urho3d  -DURHO3D_64BIT=1

This created a first configuration of Urho directly in 64bit but no other options. I then used the GUI to select others options and regenerated again. Since the generator was set the first time as 64bit. When I opened the MSVC project it was created as "X64" this time and not "Win32".

I'll modify the .bat file to include the option all the time since I need 64bits builds for all my projects.

I read what CMAKE was asking for the documentation and installed the missing parts. I'm now able to create the builds the way I need them and have the documentation generated! :smiley: 
Thank a lot for your help! I had issues since the beginning with this.  :slight_smile: 

Note: For the CLEAN. I tried that from the CMAKE GUI but did not seem to changed anything. Doing the command line with the option make it work all the time.

-------------------------

