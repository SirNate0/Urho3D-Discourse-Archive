Lumak | 2017-01-02 01:14:54 UTC | #1

I'm at the initial stages of integrating NetSurf to Urho3D.  

[b]What is NetSurf[/b]
NetSurf is:
[quote]a multi-platform web browser for RISC OS, UNIX-like platforms (including Linux), Mac OS X, and more. Whether you want to check your webmail, read the news or post to discussion forums, NetSurf is your lightweight gateway to the world wide web. website: [url]http://www.netsurf-browser.org/[/url]
[/quote]

[b]How's it different than CEF[/b]
NetSurf in comparison to CEF is lightweight, has less source files to manage, you build every library, and easier to debug and troubleshoot.  If you were to build your own libcef.lib (not talking about libcef_dll.lib - the wrapper), the clone of chromiun folder to build it is ~22GB (at least on my PC), where as the NetSurf folder by itself is ~39MB, and everything including NetSurf, LibCurl, OpenSSL is ~101MB which also includes zlib and other misc. libs required for Windows build.
On Windows, my executable size increased by about 7MB adding NetSurf to it.

[b]WIP: [url]https://github.com/Lumak/Urho3D-NetSurf[/url][/b]
-completed browser for win32 build, tested with vs2013 and OpenGL.
-support for jpeg, png, bmp, gif, and ico formats
-issues: see the repo

Image:
[img]http://i.imgur.com/sAizLVI.jpg[/img]

Edit: corrected the byte size of the source and added a link to repo.

-------------------------

yushli | 2017-01-02 01:14:54 UTC | #2

I am quite interested in seeing it on github. CEF is too heavy way to manage. If NetSurf can be a lightway alternative that will be really good. I will try it once it is out.

-------------------------

weitjong | 2017-01-02 01:14:54 UTC | #3

Count me in.

-------------------------

Lumak | 2017-01-02 01:14:55 UTC | #4

All right then, I'll make some effort to clean up the code a bit before publishing.  Still debugging a lot of what doesn't work.

Disclaimer is probably due.  I'm creating a in-game browser similar to what I did for CEF port.  And this requires using framebuffer/sdl frontend, and with that the toolbar layout is nothing like a typical NetSurf browser - originators didn't give a lot of love to framebuffer interface :frowning:

However, it is possible to have a stand-alone browser, similar to how it's done for gtk and windows frontends.

-------------------------

Lumak | 2017-01-02 01:14:56 UTC | #5

Completed support for jpeg, png, gif, bmp, and ico image formats, and the browser runs in a background thread. But because there is no pthread in Win32 build, some sites tend to take more time loading compared to NetSurf's gtk frontend build on Linux.

Started working on compiling/testing on Linux and noticed that several CMakefiles are a mess and can't build.  It'll be sometime before I can upload to github.

-------------------------

Lumak | 2017-01-02 01:14:57 UTC | #6

Cleaned up the netsurf lib folder and is now ~39MB, the entire LibBrowser folder which contains all third party libs is now ~101MB.

-------------------------

yushli | 2017-01-02 01:14:57 UTC | #7

Thanks for the quick update. I will clone the repo and have a try.

-------------------------

Lumak | 2017-01-02 01:14:57 UTC | #8

@yushli, Try windows build. That works. Linux is still WIP.

-------------------------

Lumak | 2017-01-02 01:14:57 UTC | #9

Fixed Linux transparency  and browsing and problem.

-------------------------

S.L.C | 2017-01-02 01:14:58 UTC | #10

Also, considering you'd have to link the engine to libjpeg, libpng and zlib. You might as well use those to read images and discard stb_image and jo_jpeg. Not that they have any significance to the final executable but they feel kinda redundant.

-------------------------

Lumak | 2017-01-02 01:14:58 UTC | #11

[quote="S.L.C"]Also, considering you'd have to link the engine to libjpeg, libpng and zlib. You might as well use those to read images and discard stb_image and jo_jpeg. Not that they have any significance to the final executable but they feel kinda redundant.[/quote]

I agree. They are redundant. A better solution is to not link all those libraries in question but use STB lib and link with that instead. If you take a look at LibBrowser/netsurf folder, you'll also see that there are libnsgif and libnsbmp libraries. Instead of building those libraries where they are, they're brought local to 60_NetSurf/NetSurf folder.  In addition, all image wrapper classes needed for netsurf: i.e. bmp.c, gif.c, jpeg.c, etc., are also brought local for the purpose of being able to wrap them with STB for Urho3D.  But to do that, STB lib would have to be modified and that's something that I don't want to touch atm.  In any case, I brought the image wrapper classes local to make it flexible for anyone porting netsurf to, perhaps, stand-alone SDL or other rendering libs other than using Urho3D.

Another flexibility in this setup is that for a stand-alone browser using Urho3D, all those image wrapper classes can be wrapped with Urho3D::Image class and SDL_Surfaces with Urho3D::UI components. Choices are there for w/e someone wants to do with this port.

-------------------------

S.L.C | 2017-01-02 01:14:58 UTC | #12

There might be a small problem though. Considering there are sites out there that use progressive jpeg images. STB might not be able to handle those.

-------------------------

Lumak | 2017-01-02 01:14:58 UTC | #13

You're absolutely right. But still, I have no desire to rewrite Urho3D::Image class and replace STB with libjpeg and other libs. I'll use the libs integrated in this project as they are.  If someone wants to tackle this, they're more than welcome.

-------------------------

rku | 2017-01-02 01:14:58 UTC | #14

Browser itself supports only html 4 and css 2.1. I do not think lack of progressive jpeg support would be a major loss since browser is not suitable for casual web browsing anyhow.

-------------------------

Enhex | 2017-01-02 01:14:59 UTC | #15

Licese is GPL, big nope.
@Lumark IANAL, but you probably already violated GPL by releasing your project under MIT, which isn't copyleft, which is required by GPL.

-------------------------

Lumak | 2017-01-02 01:14:59 UTC | #16

Even though, I had this posted:
[quote]License
---
The MIT License (MIT)

See additional license infromation pertaining to NetSurf and other libraries in the subfolders.
[/quote]

due to so many different licenses, e.g. all subfolders prefixed with "lib" under libBrowser/netsurf/, e.g. libcss, libdom, libnsgif, etc., were all MIT license, duktape - MIT, and the only license which was GPL under the  libBrowser/netsurf/ folder was the netsurf subfolder.  The MIT license applied to my work which was in Urho3D-NetSurf\Source\Samples\60_NetSurf in .cpp and .h files, as indicated in the headers for those files.

But, you might be right that I might have violated the license for modifying the source files in libBrowser/netsurf/netsurf to be able to build with cmake and in Win32.

I've deleted the repo to avoid any complications.  Thanks for mentioning this.

-------------------------

Enhex | 2017-01-02 01:14:59 UTC | #17

Err I meant that GPL requires any software that links to it to be also copyleft, so you're forced to release things that link to it (source code counts as linking?) under copyleft license too.
Again IANAL and only read short summaries about what GPLs allows and restricts (the thing is a giant wall of text).

You don't have to remove your repo, worst case you get infected by the viral license and forced to use it too.

-------------------------

Lumak | 2017-01-02 01:14:59 UTC | #18

There were more MIT licenses than GPL under LibBrowser, though.  But I get it.  It does 'copy left' .

Anyway, I neglected to do this:
[quote]  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.
[/quote]

I changed many files in netsurf to be able to compile and run in Win32/MSVC and really don't want to deal with it. I hope everyone who was interested in this project got a copy :slight_smile:

-------------------------

