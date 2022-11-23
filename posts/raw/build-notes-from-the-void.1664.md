dvan | 2017-01-02 01:09:21 UTC | #1

After a month or so of trying various things, I seem to have the basics of Urho3D tool chaining setup in some useful ways. Thought I'd put some notes out here, and see if I should be doing things differently before I get too busy with this.

Environment:  Running Win7 as a core, but using Urho in VMware Win8.1 environment (primarily). Also have a VM Linux Mint Xfce environment, but Windows is faster for me (also, have not gotten OpenGL builds to work (just won't display anything) in either of these VM environments). So these notes are Win8.1 DX9 based.

One of the attractions of Urho is X-Building for different environments. I wanted to be able to "target anything" in an efficient way and this has a good start at that, though some environments don't get a lot of attention (as it will probably always be). I wanted to build tool chains to easily switch between them for any build I'm interested in.

VS Community 2015:  Started with this, but have abandoned it for now. It "appears" it can only target 64bit applications (though, might just be how Urho is defaulting). Also seem not to be able to produce a "real static runtime" like I can with my VS 2010 environment. Perhaps it's a limit of the "Free" version, or just some flags that need setting, but I've found using mingw easier/cleaner for now.

CodeBlocks: Using v15.12 of this w/mingw-w64-install.exe (5.2.0) ran twice... Once for the default 32bit build, and again for a separate 64bit build directory. Urho seems to like whatever "default" environment is current, so I switch a few things to point to the ones I want at the time (path in environment and settings/compiler in CodeBlocks).

Directories Layouts:  Suppose because I spent a few years working in Unix (before linux existed). I prefer to keep various builds/sources separated, I ended up with this basic layout to illustrate:

C:\Dev\
    ----> mingw32     // 32bit mingw tools
    ----> mingw64     // 64bit mingw tools
    ----> Urho3D\               // Urho Generated buld environments
    ---->----> v1.5-Android19                  // Eclipse API-19 target
    ---->----> v1.5-CBWin                  // CodeBlocks 64bit
    ---->----> v1.5-CBWin32              // CodeBlocks 32bit
    ----> Urho3D-1.5    // Urho3D Origonal source to build from

C:Src\Urho3D\      // Urho individual project stuff

In my Src directories I've followed similar practice, having separate build directories for CMake to deposit generated CodeBlocks builds like "Build32" or "Build64", etc.

To switch / build the different environments, I mostly just need to change the "URHO3D_HOME=" environment variable and run visual Cmake to generate the build. If I'm switching between 32/64 bit also need to change a few other things.

This works for me, but am always looking for faster/better alternatives!

-------------------------

