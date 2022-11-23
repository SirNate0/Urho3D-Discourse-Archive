skymaker | 2017-01-02 00:58:14 UTC | #1

Hey all!

I'm a starting Urho3D dev who is trying to create some apps for the iPhone and other iOS devices.  I've been having a lot of trouble figuring out how to get Urho3D working such that I can take a project built in it and compile it for use in the iOS Simulator program on my OSX machine, however; can someone clarify how I need to set that up?

Currently I have an iOS-targeted Urho3D.xcodeproj file that, when opened, allows me to build the individual demos ("01_HelloWorld", etc) and run them directly in the Simulator once built.  And, with the help of a friend (and a lot of confusion), we were able to install the OSX native libraries in /usr/local/share/Urho3D/CMake/Modules, and build/run our test project natively in OSX, so I have that much working via the commandline (cmake -> make -> run binary).  Trying to use the "install" build target for the iOS XCode project seemed only to result in .app compiled binaries at that same location, so that didn't seem to be what was needed...

(Incidentally, is there a reason why Urho3D-CMake-magic was not installed as part of the "install" build target for the OSX version of the Urho3D XCode project?  We had to copy it in manually before anything would build...)

The problem now, though, is that we're still thoroughly confused as to how we can compile our own stand-alone Urho3D project file for iPhone.  I'm under the impression that we're supposed to somehow generate a new XCode project by referencing the iOS version of the Urho3D.xcodeproj file as a library?

Long story short, can someone with more insight or experience explain just how this iOS build pipeline is supposed to work?

Thanks!


P.S. - I should add that I'm pretty new to OSX and Apple products in general, but that said, I have a decent amount of experience working with both Linux and Windows systems in the past.  I know my way around a terminal well enough.  If there is a way to do more of the build process for iOS via terminal commands, I'd be interested to know how that is done.

-------------------------

skymaker | 2017-01-02 00:58:15 UTC | #2

Hey again,

Sorry to bump my post, but after looking over my bleary 2am first post, I thought I'd do better to clean up my questions a bit. /:I

Basically, I want to understand how an iOS build is done using Urho3D:

From what I can gather from the documentation, and from experimenting myself, I basically need to use the Urho3D.xcodeproj file that is generated using the "cmake_ios.sh" build script.

I've run that script, and I can load the resulting project in XCode, and can build/run the demo projects fine from there.  

Next, referencing this part of the documentation:

[quote]iOS build process
-----------------

Run cmake_ios.sh. This generates an Xcode project named Urho3D.xcodeproj.

Open the Xcode project and check the properties for the Urho3D project (topmost
in the Project Navigator.) In Architectures -> Base SDK, choose your iOS SDK
(CMake would automatically select latest iOS when generating the Xcode project).
In Code Signing, enter your developer identity as necessary.

The Urho3DPlayer target will actually build the application bundle and copy
resources from Bin/Data and Bin/CoreData directories. Edit its build scheme to
choose debug or release mode.

To run from Xcode on iPhone/iPad Simulator, edit the Product Scheme to set "Run"
destination setting to "iPhone Simulator" or "iPad Simulator", and executable
to "Urho3DPlayer.app".[/quote]

...I am left with the impression that I'm basically expected to dump my own app's "Build", "Source", and maybe also "Bin" folders and files into the "Urho3D.xcodeproj" (or associated directories in the OS filesystem) such that, when I build the "Unity3DPlayer.app" target, it uses my own project's resources for that build.

But having tried to do this in a few different ways (copy files in via the Finder, trying to import the files into what seem like relevant parts of the XCode project itself, etc...), I'm still unclear on how I'm supposed to do this import properly, if indeed that's the right understanding of how this setup is intended to work.  (I know this build target does build successfully by default because it happily runs the "snowninja" demo in the iOS Simulator before I try to change anything...)

Can someone please clarify this step of the process for me?  How do I get the "Urho3DPlayer" target to integrate with and build my own app, for iOS?  (And if that's not how it works, what am I missing?)

Any insight into this is much appreciated; thanks in advance. :slight_smile:

-------------------------

weitjong | 2017-01-02 00:58:15 UTC | #3

Welcome to our forum.

Have you read the documentation, more specifically this one? [urho3d.github.io/documentation/a00004.html](http://urho3d.github.io/documentation/a00004.html). Admittedly, our current build process is more Urho3D centric, although we now support building Urho3D engine as external library which can be linked by standalone project outside of Urho3D project. I haven't tried to reference the Urho3D.xcodeproj directly inside a new Xcode project. Let us know your setup if you could make it work that way. Currently though, we have two ways to use Urho3D library as documented in above link.

In the latest v1.31 release, we have already renamed our CMake module from Urho3D-CMake-magic to Urho3D-CMake-common. So, if you choose to the second way which install the Urho3D SDK into your filesystem then that module should be installed in this location: /usr/local/share/Urho3D/CMake/Modules/. I have just verified that.

In short, if you follow our current "limited" documented approach then you first create a new CMake project (that references Urho3D lib as external library). Use CMake to configure and generate your new Xcode project. Open that Xcode project and build. CMake should have configured everything for you already.

However, if all you intend to do is, to use the AngelScript or Lua to create your application script and let it played using the Urho3DPlayer, then you don't need to create a new project just for that. You could create the new scripts and simply replace the content of CommandLine.txt to point to your new script.

-------------------------

skymaker | 2017-01-02 00:58:17 UTC | #4

[quote="weitjong"]
...Use CMake to configure and generate your new Xcode project. Open that Xcode project and build....
[/quote]

Hi weitjong, 

Thanks a lot for your reply.  Since reading through your post, and revisiting the problem, I believe I now have Urho3D updated and installed on my system as it should be for use as a linked library (I see "Urho3D-CMake-common" in "/usr/local/share/Urho3D/CMake/Modules" as you mention).  So far so good.

However, when I run "cmake CMakeList.txt ../Source", and then use "make" on the resulting build files, the result is an OSX binary that I can run locally.  How do I tell CMake to build an iOS XCode project instead?  I've looked through the documentation you've linked, but I seem to be missing how that is done...


EDIT: Nevermind.  I finally figured out that CMake has a "-G xcode" flag. [/facepalm]   I seem to have this working now; thanks again for your help.

EDIT2: Well, seems I've traded one problem for another.  When I run the amended command, I get an XCode project, which is good; but it's set to use the OSX architecture, which is not.  Then, when I go to change the architecture to ARM/iPhone, I get the following build error:

[code]dependency issue: 
target specifies product type 'com.apple.product-type.tool', but there's no such product type for the 'iphonesimulator' platform[/code]

I've looked around and tried to figure out how to resolve this - I believe I'm somehow referencing a library that I shouldn't be for the iPhone platform, presumably one that is automatically assigned when the XCode project is first built with the OSX default architecture - but I'm drawing a blank on how to fix it.  Any advice on a solution for this problem?

-------------------------

cadaver | 2017-01-02 00:58:17 UTC | #5

The Urho CMakes scripts use the variable IOS to determine the intent of compiling either for OSX or iOS. Try calling CMake with the following command line option appended, similar to cmake_ios.sh: -DIOS=1

-------------------------

skymaker | 2017-01-02 00:58:19 UTC | #6

Hi cadaver;

That worked perfectly, thank you!  I have just now got my test app working in the iOS Simulator program.  Problem solved~

For my future reference, if these details of the XCode and iOS building/toolchain process with CMake are documented somewhere, where would that be?  I've looked around a lot online for articles and documentation (for Urho or otherwise) in trying to figure these (apparently simple) details out, but either I just completely missed my mark or they're more obscure than I would have expected.  I'm embarrassed to say it really threw me for a loop. /:I

In summary, for anyone else who is as confused as I was in the future, the build process for iOS is simply:

[ul]
[*]Download the source code for, and install, Urho using the relevant cmake script as seen in the documentation here: [url]http://urho3d.github.io/documentation/a00001.html[/url] (in the case of an OSX system the script would be "cmake_macosx.sh")[/*]

[*]Code your Urho project (this reference may help with code-side preparations: [url]http://urho3d.github.io/documentation/a00004.html[/url])[/*]

[*]Compile the source via the command line using CMake from the "[myproject]/Build" directory using the command: "cmake -DIOS=1 -G Xcode CMakeLists.txt ../Source" (where the "-G Xcode" flag requests an XCode project file be built, and the "-DIOS=1" variable ensures that this XCode project is put together for the iOS architecture specifically, rather than OSX)[/*]

[*]Load up the resulting "[myproject].xcodeproj" file placed in "Build" in XCode[/*]

[*]Set the project's "Scheme" hardware target (top-left of XCode GUI) to the desired build target (in my case the iOS Simulator, or a dev-registered iPhone), and also in the Scheme, choose "[myproject]" as the desired build target[/*]

[*]Build the application via XCode[/*]

[*]At this point, it should run without problems (unless something is horribly broken, in which case...hit the Urho or CMake forums /:U )[/*]
[/ul]

-------------------------

weitjong | 2017-01-02 00:58:19 UTC | #7

The documentation in [urho3d.github.io/documentation/a00001.html](http://urho3d.github.io/documentation/a00001.html). Most of the build options that are applicable for Urho3D project, are also applicable for your project. The cross-platform capability of Urho3D project, is also available for your project for free.

In short, if you structure your new project as instructed then you just need to cd to your project root directory and invoke ./cmake_ios.sh and passing in whatever build options you like, such as: -DENABLE_LUA=1 etc.

-------------------------

