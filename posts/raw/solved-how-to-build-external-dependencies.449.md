gwald | 2017-01-02 01:00:30 UTC | #1

Hi guys, Gwald here!
Firstly Very Impressive engine!  :sunglasses: 

So, I've been struggling lately with GP3D ( github.com / blackberry / GamePlay ) they're dropping 32bit desktop support  :angry: and I failed to get a build script for the external dependencies from the authors  :imp: - then I found you guys! wow!  :smiley: I love love love your you build system!!!

#1: So, I've searched but couldn't find any info on your external dependencies, build scripts or info on how it's done.
Is this public info?, do you guys know how to compile your own deps if you wanted/had to?

#2:  also, why is it a lightweight engine? That feature list is huge! and Raspberry Pi wow!


Cheers

-------------------------

weitjong | 2017-01-02 01:00:30 UTC | #2

Hi. Welcome to our forum.

I am not quite sure I understand your first question. If you are asking about "Urho3D" external dependencies then they are all neatly grouped under "ThirdParty" sub-directory. Each third-party dependencies is being built as static library. It has its own CMakeLists.txt that configures and generates what are necessary to build just one individual static library found in the same scope as this CMakeLists.txt. Urho3D then has a main CMakeLists.txt which includes all these sub CMakeLists.txt and basically makes Urho3D library target depends on all those static libraries. It should be quite easy to add any third party libraries into [b]your own project[/b] using CMake or not. But if you are asking how to add additional third party library into [b]Urho3D project[/b] itself then I think you will have to study closely the existing CMakeLists.txt(s) to see how it is done.

I will leave the second question to Lasse (the original author of Urho) to answer it. I can only guess the reason as the relative measurement of the actual binary size of the library or the feature set compared to other big boys game engine out there.

-------------------------

rasteron | 2017-01-02 01:00:30 UTC | #3

Hey gwald, Welcome to the forums and thank you for that youtube comment.  :slight_smile: 

As weitjong mentioned re external dependencies, you can just follow the process on how the third party libraries are built so you can get some idea to add your own. I remember I did an experimental sqlite bootstrap plugin one time and it worked straight out by following the existing libraries.

Cheers.

-------------------------

gwald | 2017-01-02 01:00:30 UTC | #4

Hi guys and thanks for the fast warm welcomes  :smiley: 
 
[quote="weitjong"] they are all neatly grouped under "ThirdParty" sub-directory. [/quote]

Thank you!  you're right under Urho3D/Source/ThirdParty/
Wow! wow! very impressive!
Now I see why it's lightweight!

Then what's the library on the home page  for? oh it's a binary package! all prebuilt.. and ready to go! again wow !
I thought these were just the third party libs, 
Thanks again... looking forward to having a read and a play!  :mrgreen:

Last question, I've noticed the binary package has a bunch of demo (car, ragdoll etc) but I've compiled from source can't find them are these a seprate download?

-------------------------

cadaver | 2017-01-02 01:00:30 UTC | #5

Urho is lightweight only comparatively, eg. it has less lines of code (excluding third party code) than Ogre3D, while Ogre3D is only a rendering engine, but very complex one. Or about 100x less code than Unreal Engine 4 :slight_smile:

At least on Windows the automatically built binary packages are likely *not* what you want for serious development, they're just provided for quick testing. The Windows version is compiled with MinGW so it's unusable for Visual Studios, and when we're talking about C++ code, the compiler should match exactly to prevent C++ ABI compatibility mismatches and crashes resulting from that. The preferable option is always to build Urho yourself with your own toolchain.

To enable build of the C++ examples, use the CMake option -DURHO3D_SAMPLES=1 when you configure your Urho build. This and other CMake options are documented in the readme and in the Doxygen documentation (see bottom of [urho3d.github.io/documentation/H ... lding.html](http://urho3d.github.io/documentation/HEAD/_building.html))

-------------------------

gwald | 2017-01-02 01:00:31 UTC | #6

[quote="cadaver"]At least on Windows the automatically built binary packages are likely *not* what you want for serious development, they're just provided for quick testing. [/quote]

Thanks for the tips and the great engine!
Got the samples working with no issues, I did a quick recording and I'll upload to youtube tomorrow.
Cheers

Edit: 
[youtube.com/watch?v=Xl8c79MGI6c](https://www.youtube.com/watch?v=Xl8c79MGI6c)  (linux openGL)
[youtube.com/watch?v=n8q1tDPKLko](https://www.youtube.com/watch?v=n8q1tDPKLko) (winXP DX9)

-------------------------

