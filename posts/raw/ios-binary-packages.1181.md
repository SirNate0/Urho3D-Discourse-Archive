shadowphiar | 2017-01-02 01:05:55 UTC | #1

Hi,
I've downloaded the binary packages for iOS and iOS 64bit, with a view towards (possibly) migrating a project that I've been writing so far using GamePlay3D. I'm slightly confused by what I find in them; the libUrho3D.a appears to be built for x86 rather than ARM cpu architecture:

[quote][color=#808080]Dione:Urho3D-1.4-iOS-64bit-STATIC ascii$ [/color]file lib/Urho3D/libUrho3D.a 
lib/Urho3D/libUrho3D.a: Mach-O universal binary with 2 architectures
lib/Urho3D/libUrho3D.a (for architecture i386):	current ar archive random library
lib/Urho3D/libUrho3D.a (for architecture x86_64):	current ar archive random library
[/quote]

Are these only intended to run on the simulator, rather than devices? Do I in fact need to compile from source?

-------------------------

weitjong | 2017-01-02 01:05:55 UTC | #2

Welcome to our forum.

Our build system is capable to build Mac-O universal binary for iOS platform. So, for the Urho3D library, it could build for both 32-bit/64-bit iPhoneSimulator and ARM archs. Having said that, our build server is rather slow with a maximum of 50 minutes (limit for non-paying Travis-CI customers) to complete a build job or the job would be killed prematurely, and what makes the matter worse is the build server performance varies depending on the sever load through out the day. So, we have a set of build rules to avoid our build job to be killed in this manner by skipping some of non-critical build processes and universal binary build is one of those and as the result some of the iOS build artifacts only contains binary for iPhoneSimulator archs. It is also unfortunate that we realized we had a small glitch while we pushed 1.4 tag which prevented us from doing a universal binary build. The glitch has been fixed since then in our master branch, I believe.

You have two ways to solve your problem.

[ol]
[li] Clone from the master branch and build from source.[/li]
[li] If for some reason you don't want to build from source while evaluating Urho3D then you can download one of our latest snapshots artifacts after the 1.4 release. Choose one that have much bigger size than what you have at the moment. As explained above, we do not guarantee the iOS build artifacts will always contain the binary for all the archs.[/li][/ol]

-------------------------

shadowphiar | 2017-01-02 01:06:00 UTC | #3

OK, thanks for the info. I have built a library from source.

I've built a few of the sample programs. Some of them seem to look very different on my iPad Air compared running the OS X build on my desktop. Can any other iOS users confirm whether it behaves the same for them, or whether I have somehow screwed up my build?

For example, in the Water demo (23) I've noticed the following problems. Some of them are a bit hard to describe so I've uploaded a short video:
[video]https://dl.dropboxusercontent.com/s/b27g4xuig7h07gw/ipad_water_demo.mp4[/video]

[ul]
[li]The water texture 'jumps' discontinuously about twice per second[/li]
[li]Moving the camera distorts the reflection image randomly[/li]
[li]The reflected and refracted parts of partially-underwater objects don't seem to line up[/li]
[li]The blocks get weird diagonal textures which vary randomly when the camera moves. These disappear if shadows are disabled.[/li]
[li]The distance you can view objects (backplane culling?) is much shorter than on the desktop[/li][/ul]

Spec: iPad air 1, OS 8.4

-------------------------

weitjong | 2017-01-02 01:06:01 UTC | #4

I think one should not expect the sample apps would render similarly in desktop and mobile/tablet platforms. Urho3D engine uses different graphic back-end: OpenGL and OpenGL ES, respectively, for these platforms. Obviously the former has more capabilities than the latter. The provided sample apps, especially, the Water demo, may push the envelop of the latter. The issue with self-shadowing (weird diagonal) and no clipping plane (wrong reflection) have been explained by Lasse (the Author of Urho3D) already in other threads.

-------------------------

