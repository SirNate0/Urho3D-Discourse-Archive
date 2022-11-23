Virgo | 2018-05-06 14:18:21 UTC | #1

anyone got ideas about how to use QtCreator as the ide for developing urho3d games for mobile platforms?
Qt + Urho3D working great on Windows/Linux/Mac os, just required some adjustment in .pro file. but when i tried use them together on mobiles, lots of build errors come up :slight_smile:
i spent whole day trying to fix these issues, but just cant tackle last two.
for android:
**_how do i get rid of JAVAs, or how do i make them callable from a QAndroidJniObject so i can use QtCreator as the only ide and qmake as the build tool?_**
for ios:
**error: '/Users/user/Urho3D-1.7-iOS-64bit-STATIC/lib/Urho3D/libUrho3D.a(Quaternion.o)' does not contain bitcode. You must rebuild it with bitcode enabled (Xcode setting ENABLE_BITCODE), obtain an updated library from the vendor, or disable bitcode for this target. for architecture x86_64_**

-------------------------

Virgo | 2018-05-06 14:22:40 UTC | #2

im new to programming, and i know barely nothing about mobile development, especially the java language
so i wonder if i can use the same code to build for these platforms without introducing new language
(some modifications in .pro file is acceptable.)

-------------------------

weitjong | 2018-05-06 16:23:10 UTC | #3

I am not a fan of Qt, so I don't know the answer to your question. What I do know is that the Xcode's BITCODE option is always enabled in our build system, however, the option is only effective when you make an "install" or "archive" target. See https://github.com/urho3d/Urho3D/issues/2190.

-------------------------

Virgo | 2018-05-06 22:30:22 UTC | #4

do you mean by default Urho3D ios lib are built with bitcode enabled?
i were using the prebuilt lib downloaded from sourceforge and a sdl2 lib built by myself with bitcode enabled.
and thats how i got the **libUrho3D.a(Quaternion.o)’ does not contain bitcode.** error

i also tried to build Urho3D myself but encountered these errors 
**Urho3D-1.7/Source/ThirdParty/Lua/src/loslib.c:43:22: 'system' is unavailable: not available on iOS**
**Urho3D-1.7/Source/Urho3D/IO/FileSystem.cpp:94:16: Call to unavailable function 'system': not available on iOS**

-------------------------

weitjong | 2018-05-07 01:41:43 UTC | #5

I meant our build system does not explicitly disabled the bitcode option and so by default it should be enabled. However, that option is ignored by Xcode itself in “normal” build target, which is “ALL_BUILD” in our case. Xcode only honors that option when the build target is either install or archive.

The prebuilt binary is a build artifact from a normal build from our CI. So, it may not have bitcode. I haven’t verified this myself. 

You must build the Urho3D lib from source and then install it into file system as SDK. The lib in the build tree doesn’t have bitcode but the one in the installed SDK should have.

As for your last problem, it is a known issue. At the time we released 1.7 I believe we were not targeting iOS 11 yet. Later when it was made publicly available only then we realized this problem and we have a patch committed in master branch to fix it. In short when targeting iOS 11 you need to apply that patch on top of release 1.7. Do a search on our github repo.

-------------------------

Virgo | 2018-05-07 01:55:07 UTC | #6

ok i found the commit and complied "install"
but still have the same problem

-------------------------

weitjong | 2018-05-07 04:10:01 UTC | #7

Use the “lipo” and “otool” commands to verify. The last time I checked the bircode section is there.

-------------------------

Virgo | 2018-05-07 02:49:02 UTC | #8

actually i found your comment here https://github.com/urho3d/Urho3D/issues/2190#issuecomment-351424449

the outputs are

**Architectures in the fat file: libUrho3D.a are: x86_64 arm64**

**sectname __bitcode**
**segname __LLVM**
**segname __LLVM**
**sectname __bitcode**
**segname __LLVM**

-------------------------

weitjong | 2018-05-07 03:46:37 UTC | #9

Just in case, have you actually reconfigured your app to use the lib in the installed SDK instead of the Urho build tree?

-------------------------

Virgo | 2018-05-07 04:40:02 UTC | #10

yes.
but actually there is one error occurred in xcode, it tried to copy file into system directory and failed (no permission)
not sure if this matters? i still got the libUrho3D.a in _**/path/to/build-tree**_/lib 
or did i make some stupid mistakes i havent noticed? 
![Untitled|690x361](upload://f13NHeDCyWJyR346ZVgCnWVBr9H.png)

-------------------------

weitjong | 2018-05-07 05:11:14 UTC | #11

You need to either install it to a system-wide SDK location with account that has the permission or use CLI “sudo” command to escalate the privilege; or just install the SDK to a non system-wide location as normal user. There are a few ways to do so, your mileage may vary. See https://urho3d.github.io/documentation/HEAD/_building.html#Building_Library.

-------------------------

Virgo | 2018-05-07 05:53:10 UTC | #12

![macOS-2018-05-07-13-52-00|690x414](upload://uh62lJhBx0aRmpMtq02r0ZOJNIy.png)![macOS-2018-05-07-13-52-09|690x414](upload://vgAknVCE5szIElYaNtSzusOliFn.png)
same issue still xD

-------------------------

weitjong | 2018-05-07 06:47:25 UTC | #13

I am sorry to hear that. As I said I cannot provide any support nor comment for anything Qt-related.

Have you tried our CMake/Xcode generator? And then replicate the generated Xcode build setting to your Qt project, assuming the latter works correctly.

-------------------------

Virgo | 2018-05-07 08:50:46 UTC | #14

where is the generator :grinning:

-------------------------

Virgo | 2018-05-07 09:38:24 UTC | #15

do you have a prebuilt library with bitcode enabled?
can you upload it for me?

-------------------------

weitjong | 2018-05-07 16:19:50 UTC | #16

Now after a second thought, I believe those prebuilt binary from CI should have the bitcode as well. This is because in order to package the bits into a tarball, I think CPack must have invoked CMake Install to do the ground work. Personally I don’t have prebuilt binaries that I could share. Sorry.

About the generator, what I meant is using our provided cmake_xcode.sh script to generate a Xcode project, as per usual.

-------------------------

Virgo | 2018-05-07 10:40:37 UTC | #17

so it means thats all qt's fault?

i tried those cmake_*.* too, didnt figure out how to use them correctly xD
i followed this tutorial https://github.com/urho3d/Urho3D/wiki/Setting-up-a-Project-(CMake)
and stuck at step 2

-------------------------

Virgo | 2018-05-07 11:47:19 UTC | #18

oops i think i found the problem, i try to build examples in the xcode project generated by cmake_ios.sh
(yes stupid me forgot these examples)
everything went find when building ios-simulator targets
but as long as i switched to ios, one error occurred, says **"Code signing is required for product type 'Application' in SDK 'iOS 11.3'"**

-------------------------

johnnycable | 2018-05-07 12:42:12 UTC | #19

you need to codesign your apps before installing on a device; that is you need an apple id

-------------------------

Virgo | 2018-05-07 12:42:49 UTC | #20

so im leaving the ios platform for now xD

-------------------------

