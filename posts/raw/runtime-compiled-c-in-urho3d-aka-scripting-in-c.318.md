Pablo | 2019-05-12 19:07:21 UTC | #1

I've been working in this a few weeks in my spare time after work. I took the idea of using C++ as a scripting language from [url]http://molecularmusings.wordpress.com/2013/08/27/using-runtime-compiled-c-code-as-a-scripting-language/[/url] and [url]http://runtimecompiledcplusplus.blogspot.com[/url]. This is technically called "Runtime-compiled C++", which I'll call RCCpp from now on.

Obviously, C++ is not a real scripting language, nor it tends to be. The main goal is to shrink iterations' time while having a quick preview of what you're trying to accomplish while using a well-known language such as C++. You have the power of C++ with trusted IDEs, autocompletion, debugger and everything you'd need to work already, so you don't need either to learn other language nor look for new tools to work with Lua or AngelScript. Of course, you can still shoot yourself in the foot, and have to be very careful about memory leaks, as the idea is to have Urho3DPlayer always running while it loads dynamically a recent compiled version of what you're trying to do. Ok, enough chit-chat. This is what it looks like:

Enable HD to be able to read the code
http://youtu.be/uRf0LXjZWO0

To put it simple those are the steps that Urho3D's RCCpp follows:

1) If a .cpp is passed as an argument (instead of a .lua or .as), a Makefile is generated on the fly (only GCC/MinGW is supported for now) with all the .cpp's within that same folder and compiles everything into a shared library. So let's say we run "Urho3DPlayer RCCpp/Game.cpp". This will try to compile Game.cpp and all the cpp's within RCCpp into a shared library called Game.dll (or Game.so if we're on a Unix system). If instead we pass an already compiled library (.dll or .so), step 2 applies inmediately.

2) If the compilation succeeds, it will load at runtime the shared library and will execute its "Start" method, the same way it's done with Lua or AngelScript.

3) Every time there's a change in any .cpp being watched (within RCCpp folder, in this case), it will compile again and if it was successful, it will call the "Stop" method of Game, destroy the old Game object, unload the old library, load the new one and call its "Start" method. This has been done this way to avoid freezing the update loop so that the game plays as smoothly as possible. Please note that a total different object is created, so if you would like to have exactly the same state as before, you'll have to serialize and unserialize it by yourself.


So, right now everything is compiled into a single library. This has pros and cons, but I ended up doing it like that because if I wanted to have a different library for each class (which is desirable in terms of extensibility and speed, so that I don't have to unload and load all the classes at the same time, just the ones that need to be replaced) I'd have to use a fixed interface (usually Update and Render methods) and have somehow a list of dependencies among classes so that if I change one class, all of its dependant classes are also compiled or at least reloaded. This was quite painful at the end, so having everything in a single library eases things up and avoids some other problems.

I've tried to follow the rules that I've read in the documentation so that RCCpp is only used if a define is passed via CMake (URHO3D_RCCPP) and so on. I use the FileWatcher to know when a file has changed and needs to be recompiled. I also send useful events when a library/class is going to be unloaded or loaded, when the compilation has started or finished and so. It's been tested it on Mac and Windows (with MinGW, no Visual Studio support yet) and it should work on Linux too. The only thing you need to make it work is adding your toolchain binary folder in your path so that "make" and "g++" can be called and define an environment variable called URHO3D_HOME pointing to your Urho3D's main folder so that the include and library paths can be found in order to compile. You could also create a "PreMakefile" that will be included at the very beginning of the Makefile to pass to the compiler/linker your own flags. Take a look into the content of the Makefile generated to find the name of the variables to set.

Lastly, I'd like to hear your thoughts about this. Do you think is useful, do you think is a waste of time, what would you improve, do you have any suggestions? I've easily ported all the examples so that the same file and the same code works for the C++ samples as well as for RCCpp using a couple macros. The code is not the cleanest nor the most commented thing right now, but if people are interested, we could clean things up together and polish the bugs that may arise: [github.com/pamarcos/Urho3D/tree/RCCpp](https://github.com/pamarcos/Urho3D/tree/RCCpp)

-------------------------

thebluefish | 2017-01-02 00:59:35 UTC | #2

Interesting idea. Is there any performance boost by scripting this way? Any possible metrics?

Excuse me if I'm being ignorant, but doesn't this also require the header files to be available? I would probably have to pass on this idea if that was the case, but cool idea none-the-less!

-------------------------

Pablo | 2017-01-02 00:59:35 UTC | #3

[quote="thebluefish"]Interesting idea. Is there any performance boost by scripting this way? Any possible metrics?[/quote]
I haven't run any benchmark myself, but the performance boost would be the same as C++ over AngelScript or Lua. Have a look at [codeplea.com/game-scripting-languages](http://codeplea.com/game-scripting-languages). Anyway, a game bottleneck is usually its core (which in this case is already in C++, so no problem here) rather than the game logic. One of the advantages of using C++ directly is that you have the full API 100% available but with RCCpp, you don't need to worry about large compilation times and closing and opening the game again and again.

[quote="thebluefish"]Excuse me if I'm being ignorant, but doesn't this also require the header files to be available? I would probably have to pass on this idea if that was the case, but cool idea none-the-less![/quote]
Regarding the headers, you don't really need to pass any header files as that's taken care of by the Makefile. It adds to the include path every Urho3D folder as well as the same path of the cpp you're passing. So, you just have to create a class (i.e. Game) that inherits from RCCppMainObject and reimplement its Start and Stop methods. If you wanted to use more classes, create as many as you like that inherit from RCCppObject and then you can use it from your Game class.

-------------------------

friesencr | 2017-01-02 00:59:35 UTC | #4

I really like the idea of doing this.  I build my code around angelscripts hot swapping so doing it in c++ sounds radicool.  I don't have any wisdom to know whether it is a good idea or not.  I looked at your code.  It looks really good!  I will definitely try out your fork sometime this week.  Thanks for sharing!!

-------------------------

alexrass | 2017-01-02 00:59:36 UTC | #5

Super! Going to try.

[after try]
This is awesome!!! Works perfect!!!
Once compiled, you can run the library. [code]Urho3DPlayer.exe Modules/Test.dll -w[/code] This should be in the Urho3D!

-------------------------

cadaver | 2017-01-02 00:59:36 UTC | #6

This is certainly very cool. For inclusion into the official Urho3D repo, I'm not sure. We'd have to think carefully of what application / execution model we want to impose (currently Urho3D doesn't really impose one for C++), and if reloading the whole "game" is enough, or should we need per-component reloading?

-------------------------

rasteron | 2017-01-02 00:59:36 UTC | #7

Very nice addition here for direct C++ coders in the engine! I've been watching this framework for some time now and its really cool to change C++ code in run-time for development/testing. I would recommend though having this as a build option or "add on" if the core team decides to add this to the repo.

-------------------------

AGreatFish | 2017-01-02 00:59:36 UTC | #8

This is extremely cool :slight_smile:

I think it could be extremely helpful for us C++ developers in some situations.

Of course, the ability to use Urho3D as an external library needs to be preserved, but that seems to be the case (?).

So..as long as it is optional, I am definitely in favour of this.

PS:
I am having some trouble getting it to work on Linux, though (though, that might just be me...). It detects the changes properly and compiles successfully and seems to "restart" the application but it doesn't display the effects of the changes.
I can only see those once I restart Urho3DPlayer itself (even if I pass the library itself as an argument, so it appears to compile correctly).

I believe that there might be an issue with loading the new library.

-------------------------

Pablo | 2017-01-02 00:59:36 UTC | #9

[quote="rasteron"]I would recommend though having this as a build option or "add on" if the core team decides to add this to the repo.[/quote]
RCCpp is compiled as a separte module the same way as AngelScript, Lua or some others by defining something during the CMake process. In this case, URHO3D_RCCPP needs to be set.

[quote="AGreatFish"]Of course, the ability to use Urho3D as an external library needs to be preserved, but that seems to be the case (?).[/quote]
Yes, in fact if RCCpp is enabled Urho3D is compiled as a shared library so that your game library is linked against it.

[quote="AGreatFish"]I am having some trouble getting it to work on Linux, though (though, that might just be me...). It detects the changes properly and compiles successfully and seems to "restart" the application but it doesn't display the effects of the changes.
I can only see those once I restart Urho3DPlayer itself (even if I pass the library itself as an argument, so it appears to compile correctly).[/quote]
Sorry about that, I didn't have time to test it on Linux (because I didn't have a Linux partition working at the moment). Have you compiled the debug version to see what RCCpp outputs through stdout? There's also a Build.log to check that the compilation worked, although a compilation error doesn't seem to be your issue the way you described it. Take a look at RCCppUnix.cpp and try to write some logs in case dlopen failed. Something like this:

[code]bool RCCppUnix::LoadLib(const String& libraryPath)
{
    library_ = dlopen(libraryPath.CString(), RTLD_LAZY);
    if (library_ != NULL)
    {
        String name = GetFileName(libraryPath);
        createObject_ = (PCreateRCCppObject)dlsym(library_, String("create" + name).CString());
        destroyObject_ = (PDestroyRCCppObject)dlsym(library_, String("destroy" + name).CString());
    }
    else
    {
        LOGDEBUG("Error opening library " + libraryPath);
    }

    if (library_ == NULL)
    {
        return false;
    }
    else
    {
        return true;
    }
}[/code]

Anyway, I'll try to set a VM with a Linux version to test it out. If you take a look at RCCppWin you'll notice that I have to do some kind of hack in order to hot-swap the library. The compilation fails to create the library because it's still being used (which doesn't happen un Mac). Funny thing is that whereas you cannot change the content of the library itself, you can change the name. So what it's done is: change the old library name (let's say from Game.dll to Game.dll.old), compile the new code to Game.dll, unload the old library and load the new one. Once this is done, the .old version is removed. However, this doesn't seem to be your issue, as if this was the case, the compilation would fail during the linking process.

Thanks everyone for checking this out. There's still some work to do for a perfect integration with Urho3D, but I think we're heading in the right direction.

-------------------------

AGreatFish | 2017-01-02 00:59:37 UTC | #10

According to the log, the compilation is successful.

I also don't think that dlopen is the problem. I set debug messages to confirm this and I set a breakpoint and inspected the values of library_.

-------------------------

Pablo | 2017-01-02 00:59:37 UTC | #11

[quote="AGreatFish"]According to the log, the compilation is successful.

I also don't think that dlopen is the problem. I set debug messages to confirm this and I set a breakpoint and inspected the values of library_.[/quote]

At the end Urho3DPlayer wasn't working well on my VM so I installed Linux in a brand new partition. I've had exactly the same problem that you described. It's been a while until I've found the issue. It seems dlclose is not closing properly the library and so, every time dlopen is called it returns exactly the same handler (which is the handler to the very first version of the library compiled) so nothing really changes in the game apart from destroying the main object and creating it again. If you take a look at the documentation at [linux.die.net/man/3/dlclose](http://linux.die.net/man/3/dlclose) it says:

[quote]If the same library is loaded again with dlopen(), the same file handle is returned. The dl library maintains reference counts for library handles, so a dynamic library is not deallocated until dlclose() has been called on it as many times as dlopen() has succeeded on it. The _init() routine, if present, is only called once. But a subsequent call with RTLD_NOW may force symbol resolution for a library earlier loaded with RTLD_LAZY.[/quote]

As far as I understand, it seems that the reference count system is not working as it should or something I can't understand is happening. In Mac is working well, though (which makes sense, because there's only one dlopen-dlclose pair). I'm not very proud of what I've done to make it work, but it's working and I think that's enough for a day. I hope it works for you as well. 
Give it a try: [github.com/pamarcos/Urho3D/comm ... 9ec3c09a5c](https://github.com/pamarcos/Urho3D/commit/2ae5db35b0da3eb947b066185a99219ec3c09a5c)

-------------------------

friesencr | 2017-01-02 00:59:37 UTC | #12

i don't know if this helps... but sdl has stuffs

[wiki.libsdl.org/SDL_LoadObject](https://wiki.libsdl.org/SDL_LoadObject)
[wiki.libsdl.org/SDL_LoadFunction](https://wiki.libsdl.org/SDL_LoadFunction)

-------------------------

AGreatFish | 2017-01-02 00:59:37 UTC | #13

I just did a quick test before going to sleep and it works now :slight_smile:

And it seems even cooler after actually having used it !

Will take a closer look at it tomorrow :wink:

-------------------------

DougBinks | 2017-01-02 00:59:37 UTC | #14

Doug here Runtime-Compiled C++.

In our RCC++ implementation we only compile changed files, so load these as new modules with a temp name to avoid name clashing and so we can keep the old modules open (as they may contain code still being used). The solution you're using for Linux looks the same as the one I'm using.

Let me know if you have any further problems, and I'll see if I can help - though I'm travelling for work atm, so there may be some delay.

-------------------------

AGreatFish | 2017-01-02 00:59:37 UTC | #15

I noticed a funny effect:
Since Urho3D is still running it appears that some things persist after recompiling. 
E.g. when I change the position of UI Elements, the elements appear two times. Once in the old position and once in the new position.

-------------------------

Pablo | 2017-01-02 00:59:37 UTC | #16

[quote="AGreatFish"]I noticed a funny effect:
Since Urho3D is still running it appears that some things persist after recompiling. 
E.g. when I change the position of UI Elements, the elements appear two times. Once in the old position and once in the new position.[/quote]

That's right. RCCpp only cares about compiling, destroying the object, reloading the new lib and creating the new object. So, you have to take care of everything else by yourself. If you added something to the UI's root, you'll have to remove it either in the Stop method or in the destructor of your RCCppMainObject so that when the new one is created, you don't have duplicates. I thought about cleaning the whole UI after every time your lib is unloaded, but that would clean absolutely everything and there may be cases where that's not the desired behavior (e.g. in the samples the Urho3D logo would be removed also).

The easiest solution for the UI is adding everything as children of a UiElement that you remove in the Stop method so that the next time the lib is loaded, only the new UI-related stuff is shown. This is what I did in the video with the Urho2DSprite example.

Summarizing, using RCCpp is cool and useful, but there are times where it requires an exta step where you have to make sure that everything you have created/added etc, is removed in your Stop or destructor so that the next time the lib is loaded you don't have duplicates.

-------------------------

friesencr | 2017-01-02 00:59:37 UTC | #17

I wonder if instead of firing of the Start event we could create a virtual method OnReload and publish an event that could cancel the reload,  the OnReload would just call Start likely but it could allow the logic to grow.  I am guessing there are too many things that could happen after initialization for urho to gracefully handle object reloading.  We could set up some conventions with the vars/attributes but its hard to know if those would work.

-------------------------

DougBinks | 2017-01-02 00:59:38 UTC | #18

Our [url=https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus]RCC++ framework[/url] has an object initialization where we pass in a boolean demarking whether the init is being called on a new object or on one being re-loaded. I'd be tempted to go for three separate functions in future, one for first time init, one for reload init (object hasn't been recreated or had code changed) and one for recreated object.

-------------------------

Pablo | 2017-01-02 00:59:39 UTC | #19

[quote="friesencr"]I wonder if instead of firing of the Start event we could create a virtual method OnReload and publish an event that could cancel the reload,  the OnReload would just call Start likely but it could allow the logic to grow.  I am guessing there are too many things that could happen after initialization for urho to gracefully handle object reloading.  We could set up some conventions with the vars/attributes but its hard to know if those would work.[/quote]

Right now the Start is always called. Adding an option to avoid reloading everything by RCCpp and leaving you to do it whenever you want should not be difficult. Having said that, there are 6 different events that RCCpp is already firing to give you the possibility to clean things up your way. Those are: E_RCCPP_COMPILATION_STARTED, E_RCCPP_COMPILATION_FINISHED, E_RCCPP_LIBRARY_PRELOADED, E_RCCPP_LIBRARY_POSTLOADED, E_RCCPP_CLASS_PRELOADED, E_RCCPP_CLASS_POSTLOADED. So, you can still set up a listener to any of those methods in order to do something before the library is really reloaded. What you can't do right now is stopping the process to reload it whenever you want. I'll give it some thoughts of how that could be done in an easy way.

[quote="DougBinks"]Doug here Runtime-Compiled C++.

In our RCC++ implementation we only compile changed files, so load these as new modules with a temp name to avoid name clashing and so we can keep the old modules open (as they may contain code still being used). The solution you're using for Linux looks the same as the one I'm using.

Let me know if you have any further problems, and I'll see if I can help - though I'm travelling for work atm, so there may be some delay.[/quote]

Good to see you here, Doug  :slight_smile:. I was mind-blown the first time I visited your webpage. It's quite impressive to see C++ compiled and loaded at runtime. I mean, when you think about it you realize it's technically feasible to do it, but still impressive. I tested the samples and so, but unfortunately I haven't had much spare time to look at the code to know how everything works.
For the very first version of RCCpp in Urho3D, instead of using a Makefile system that would compile everything into a single library, I thought of having a different shared library for every class. That in terms of modularity is desirable, but the "one-single library" approach won in terms of simplicity. The overhead of loading the whole library for a single class is still there, but I avoided the following issues:

[ul]
1) Compiling everything the very first time. Makefile does the work compiling only the necessary files, because otherwise I'd have to implement some kind of file date checking to see if the libraries are up-to-date and compile only the files needed.
2) How do you solve dependencies among libraries? You have to specify one way or another what other libraries you depend on so that when some of that libraries is compiled, you create a new oject of that kind. I thought of having a Class.rcpp file with that kind of information, or embedding some commented code into any class' cpp file (yeah, that would be specially ugly) specifying that and parsing it from RCCpp. Another option would be to parse every file and recompile everything including Class.h. I didn't like any of the solutions, though.
3) By compiling everything, destroying everything and creating it again I ensure that every object is an up-to-date version.
[/ul]

I get that by creating temporary names for the libraries you can still use the old ones. But why would you want to use an older version of the library/module? Shouldn't every class reload the new version of the class? Or you simply let the coder choose whether he wants to reload a new version or not? Another question I have is how do you handle exceptions in Mac and Linux where you don't really have SEH.

Thanks in advance. Cheers.

-------------------------

DougBinks | 2017-01-02 00:59:39 UTC | #20

@Pablo - glad you like the demos! Our objective with the RCC++ project was to change people's minds about how C and C++ can be used, and it seems we're getting there. I've added Urho3d to a [url=https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus/wiki/Alternatives]list I keep of projects using RCC++[/url].

You'll find answers to some questions on [url=https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus/wiki]our wiki[/url], and there's a chapter on RCC++ in the book Game AI Pro if you can get hold of it.

1) Our RCC++ implementation is designed to be used to re-compile code as fast as possible. We avoid needing makefiles etc. as the developer uses their existing infrastructure to compile the code in any way they like, and RCC++ simply handles re-compilation at runtime when a source file is changed.

2) We solve dependencies by embedding the information in the compiled code. See the wiki on [url=https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus/wiki/Specifying-include-directories]includes[/url], [url=https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus/wiki/Using-libraries-from-runtime-modifiable-classes]libraries[/url], [url=https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus/wiki/Runtime-modifiable-header-files]modifiable headers[/url] and [url=https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus/wiki/Runtime-source-dependencies]source dependencies[/url]. Recently people have [url=https://groups.google.com/forum/#!topic/runtimecompiledcplusplus/2_I-kewQgvc]started to use RCC++ for scripting[/url], where they want to compile new code and I'm looking into ways to make this easier. Personally I prefer using my normal tool chain and just using RCC++ for changes.

3) We still perform a full data reload (in memory), but keep the compiled and linked code as small as possible. Linkage is often a rate-determining step so this helps considerably. Recently I'm finding the full-reload can be more lengthy that it needs to be so I'm considering adding support for only reloading data for modified files.

4) We need to keep old libraries around as our implementation compiles changes and dependencies into a single dll per [url=https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus/wiki/Using-ProjectIds-and-Projects]'project'[/url] (most users only need one project). So a library may contain code from a.cpp and b.cpp, then when b.cpp changes we get a new library only containing the code from b.cpp, so need to keep the old library for the code from a.cpp. In many cases, the original code is compiled into the executable, so obviously that needs to be kept around.

5) For error protection outside of windows we use signals. Take a look at [url=https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus/wiki/Error-protection]the wiki page on error protection[/url] and code for [url=https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus/blob/master/Aurora/RuntimeObjectSystem/RuntimeProtector.h]RuntimeProtector.h[/url] and implementation in [url=https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus/blob/master/Aurora/RuntimeObjectSystem/RuntimeObjectSystem_PlatformPosix.cpp]RuntimeObjectSystem_PlatformPosix.cpp[/url]

Remember that since our RCC++ implementation uses a liberal license, you can borrow as much or as little of the code as you need for Urho3d. I'm travelling atm, so may be a bit slow with replies but please continue asking questions as you need!

-------------------------

scorvi | 2017-01-02 01:00:47 UTC | #21

hey,

i have some problems integrating this into my game framework. 

i am using Visual studio and i followed the RCC++ project's integration but somehow the dll which is created has no exposed functions. i used dumpbin /EXPORTS HelloWorld.dll  to check it. 

so i replaced 
[code]// Expands to this example's entry-point
//DEFINE_APPLICATION(HelloWorld)
extern "C"  __declspec(dllexport)   RCCppObject* createHelloWorld(Context* context) { return(RCCppObject*) new HelloWorld(context); }
extern "C"   __declspec(dllexport)  void  destroyHelloWorld(RCCppObject* object) { delete object; }
[/code]

and now it has exposed functions:
[code]C:\....\Bin\Data\RCCpp\01_HelloWorld>dumpbin /EXPORTS HelloWorld.dll
Microsoft (R) COFF/PE Dumper Version 12.00.21005.1
Copyright (C) Microsoft Corporation.  All rights reserved.

Dump of file HelloWorld.dll

File Type: DLL
  Section contains the following exports for HelloWorld.dll

    00000000 characteristics
    543E2EEC time date stamp Wed Oct 15 10:23:08 2014
        0.00 version
           1 ordinal base
           2 number of functions
           2 number of names

    ordinal hint RVA      name

          1    0 000033A0 createHelloWorld
          2    1 000033F0 destroyHelloWorld

  Summary

        1000 .data
        5000 .rdata
        1000 .reloc
        5000 .text[/code]

my cmd call line is this :
[code] call "C:\Program Files\Microsoft Visual Studio 12.0\VC\Vcvarsall.bat" x86 && cl /Od /DRCCPP /D_WINDOWS /DWIN32 /D_DEBUG /DURHO3D_SSE /DURHO3D_MINIDUMPS /DURHO3D_FILEWATCHER /DURHO3D_PROFILING /DURHO3D_LOGGING /DURHO3D_OPENGL /DURHO3D_ANGELSCRIPT /DURHO3D_RCCPP /I%URHO3D_HOME% /I%URHO3D_HOME%/Build/Engine /I%URHO3D_HOME%/Source/Engine/RCCpp /I%URHO3D_HOME%/Source/Engine /I%URHO3D_HOME%/Source/Engine/Audio /I%URHO3D_HOME%/Source/Engine/Container /I%URHO3D_HOME%/Source/Engine/Core /I%URHO3D_HOME%/Source/Engine/Engine /I%URHO3D_HOME%/Source/Engine/Graphics /I%URHO3D_HOME%/Source/Engine/Input /I%URHO3D_HOME%/Source/Engine/IO /I%URHO3D_HOME%/Source/Engine/Math /I%URHO3D_HOME%/Source/Engine/Navigation /I%URHO3D_HOME%/Source/Engine/Network /I%URHO3D_HOME%/Source/Engine/Physics /I%URHO3D_HOME%/Source/Engine/Resource /I%URHO3D_HOME%/Source/Engine/Scene /I%URHO3D_HOME%/Source/Engine/UI /I%URHO3D_HOME%/Source/Engine/Script /I$%URHO3D_HOME%/Source/Engine/Urho2D /I%URHO3D_HOME%/Source/ThirdParty/Box2D /I%URHO3D_HOME%/Source/ThirdParty/Bullet/src /I%URHO3D_HOME%/Source/ThirdParty/kNet/include /I%URHO3D_HOME%/Source/ThirdParty/SDL/include  /IC:/Users/.../GitHub/Urho3DGame/Bin/Data/RCCpp/01_HelloWorld/ /IC:/Users/.../GitHub/Urho3DGame/Bin/Data/RCCpp/01_HelloWorld/../ /FdC:/Users/.../Coding/GitHub/Urho3DGame/Bin/Data/RCCpp/01_HelloWorld/ /FeC:/Users/.../GitHub/Urho3DGame/Bin/Data/RCCpp/01_HelloWorld/ /FoC:/Users/.../GitHub/Urho3DGame/Bin/Data/RCCpp/01_HelloWorld/ /FpC:/Users/.../Urho3DGame/Bin/Data/RCCpp/01_HelloWorld/ C:/Users/.../Urho3DGame/Bin/Data/RCCpp/01_HelloWorld/HelloWorld.cpp /MDd /LDd /link %URHO3D_HOME%/Lib/Urho3D_d.lib [/code]

did i forget to define a konstant in the cmd call ?

-------------------------

Pablo | 2017-01-02 01:00:49 UTC | #22

Sorry for the late reply, but I was on holidays traveling and I didn't have access to Internet.

Indeed, as MSVC was not supported, you'll definitely need some tweaks to make it work. One of which is exporting the methods properly as you did. I would recommend you to overwrite the DEFINE_APPLICATION macro of Sample.h or the RCCP_OPBJECT of RCCppObject.h so that it works for every class and not just this one.

After having a quick look at your cmd line call seems that everything is as it should (I'm not a MSVC pro, though). Could you explain deeper what's your current issue, the steps that you do and the logs that you get? If I understood correctly, RCCpp should be complaining about not finding the createHelloWorld and destroyHelloWorld methods. It should print a log line such as "Could not load library HelloWorld". Is that what's actually happening to you? I understand that it woudn't work if symbols are not exported, but I don't really understand what's happening to you right now if you've properly exported the symbols as you did.

-------------------------

scorvi | 2017-01-02 01:00:50 UTC | #23

[quote="Pablo"]Sorry for the late reply, but I was on holidays traveling and I didn't have access to Internet.

Indeed, as MSVC was not supported, you'll definitely need some tweaks to make it work. One of which is exporting the methods properly as you did. I would recommend you to overwrite the DEFINE_APPLICATION macro of Sample.h or the RCCP_OPBJECT of RCCppObject.h so that it works for every class and not just this one.

After having a quick look at your cmd line call seems that everything is as it should (I'm not a MSVC pro, though). Could you explain deeper what's your current issue, the steps that you do and the logs that you get? If I understood correctly, RCCpp should be complaining about not finding the createHelloWorld and destroyHelloWorld methods. It should print a log line such as "Could not load library HelloWorld". Is that what's actually happening to you? I understand that it woudn't work if symbols are not exported, but I don't really understand what's happening to you right now if you've properly exported the symbols as you did.[/quote]

np.

i just wanted to know if using __declspec(dllexport) was the right way to do it. Because i did not see somthing like that in your implementation, so i thought i did something wrong. And i did not find this approach in the RuntimeCompiledCPlusPlus code, too... so i asked here ...

Yes it works with __declspec(dllexport). 
thx for your reply.

how would i start creating c++ scripting for components ? or replace the scriptcomponent with a scriptcpluspluscomponent ?

-------------------------

Pablo | 2017-01-02 01:00:50 UTC | #24

Ok, I thought that after using __declspec(dllexport) you were still having some issues, that's why I asked :smiley:.

The thing is that I did this implementation only for gcc-based compilers (in Windows that would be MinGW). By default, those compilers export every symbol unless specified otherwise. The approach of Visual Studio is exactly the other way around. Unless specified, it does not export anything, so you have to use __declspec(dllexport) yourself to every method that you want to export. That's the reason people normally use some macro that they use in every class containing something different depending on the OS (take a look at [github.com/LaurentGomila/SFML/b ... Config.hpp](https://github.com/LaurentGomila/SFML/blob/master/include/SFML/Config.hpp), for instance).

[code]////////////////////////////////////////////////////////////
// Define helpers to create portable import / export macros for each module
////////////////////////////////////////////////////////////
#if !defined(SFML_STATIC)

    #if defined(SFML_SYSTEM_WINDOWS)

        // Windows compilers need specific (and different) keywords for export and import
        #define SFML_API_EXPORT __declspec(dllexport)
        #define SFML_API_IMPORT __declspec(dllimport)

        // For Visual C++ compilers, we also need to turn off this annoying C4251 warning
        #ifdef _MSC_VER

            #pragma warning(disable: 4251)

        #endif

    #else // Linux, FreeBSD, Mac OS X

        #if __GNUC__ >= 4

            // GCC 4 has special keywords for showing/hidding symbols,
            // the same keyword is used for both importing and exporting
            #define SFML_API_EXPORT __attribute__ ((__visibility__ ("default")))
            #define SFML_API_IMPORT __attribute__ ((__visibility__ ("default")))

        #else

            // GCC < 4 has no mechanism to explicitely hide symbols, everything's exported
            #define SFML_API_EXPORT
            #define SFML_API_IMPORT

        #endif

    #endif

#else

    // Static build doesn't need import/export macros
    #define SFML_API_EXPORT
    #define SFML_API_IMPORT

#endif[/code]

[quote]how would i start creating c++ scripting for components ? or replace the scriptcomponent with a scriptcpluspluscomponent ?[/quote]

The easiest way to start using RCC++ within Urho3D is creating a folder within the Bin/Data folder called as you wish. Then, inside you have to create a class that inherits from RCCppMainObject and reimplement their Start and Stop methods, which will be the ones that Urho3D will call at the beginning and end, respectively. Then, you just have to call "Urho3dPlayer.exe MyMainClass.cpp" (as in any AngelScript or Lua script, besides any other parameters you may need). For any other component that you want to use, just remember that you have to inherit from RCCppObject and that you have to place the cpp file within the same folder as the RCCppMainObject's file. You can also reimplement the Start/Stop methods of those additional components, but it's not mandatory. To use the components from RCCppMainObject you just have to include its header as you would do normally and that's all. RCC++ should be smart enough and create the proper Makefile to include every cpp within the folder of the project. 

Having said that, you may need some work to make Visual Studio compile the Makefile succesfully. Take a look at [github.com/pamarcos/Urho3D/blob ... mpiler.cpp](https://github.com/pamarcos/Urho3D/blob/RCCpp/Source/Engine/RCCpp/RCCppGppCompiler.cpp). You'll have to use nmake instead of make. I'm not sure the original Makefile created will be ok for MSVC, but you can create a RCCppMsvcCompiler.cpp that does something similar but for Visual Studio.

[code]
#ifdef __MINGW32__
    SYSTEM_INFO sysinfo;
    GetSystemInfo(&sysinfo);
    int cores_ = sysinfo.dwNumberOfProcessors;
    makeCommand_ = "mingw32-make -j" + String(cores_);
#else
    int cores_ = sysconf(_SC_NPROCESSORS_ONLN);
    makeCommand_ = "make -j" + String(cores_);
#endif
[/code]

I hope it helps. Good luck, buddy!

-------------------------

sabotage3d | 2017-01-02 01:00:53 UTC | #25

Any chance this could work on IOS using Xcode ? It could be with some hackery I have seen workaround that allow the use of shared libraries for IOS. Although it might work only on the simulator and not on the device, but still could be quite useful.

-------------------------

Pablo | 2017-01-02 01:00:53 UTC | #26

[quote="sabotage3d"]Any chance this could work on IOS using Xcode ? It could be with some hackery I have seen workaround that allow the use of shared libraries for IOS. Although it might work only on the simulator and not on the device, but still could be quite useful.[/quote]

I don't think this would work easily on iOS. I'm not very familiar with the installation process of apps for iOS, but my guess is that you'd like to have the game running on the device and be able to change the code in your machine, compile it and upload the new library to the device so that it changes the behavior of the game instance running at the moment. As far as you're able to load a library at runtime, you should be able to load another library and start using it. What I'm concerned is that you should either have a button to know when to reload the library, or implement by your own something like Urho3D has to detect file changes (take also a look at [code.google.com/p/simplefilewatcher/](https://code.google.com/p/simplefilewatcher/)), but I'm not sure you'll be able to do that in iOS. The other hard thing would be to upload a file to some place within iOS where your app would have access to read, and I'm not sure the OS would allow you to do that (without reinstalling the whole application) either. On the other hand, I do think this could be done in Android, as you have access to push files to different locations and in Java as far as I know you can unload and load native libraries again.

If anyone's got expertice about this, please post your thoughts.

-------------------------

sabotage3d | 2017-01-02 01:00:54 UTC | #27

I think this could work with the simulator and it would be more useful anyway. The simulator is using the same compiler as OSX it is just clang and the files are pushed to local folder. If shared library is needed it could be with some modifications of Xcode configs but it could work. Can just Cmake be used to track if files is changed ? Can you provide a simple OSX example with Urho3D I think I can get the IOS version to work ?

-------------------------

Enhex | 2017-01-02 01:06:28 UTC | #28

I wonder if it's possible to make RCCpp secure and viable for modding.

From security perspective:
- side effects only though the scripting API.
- bound checking
- sandboxing
- Compile at runtime to make sure the shared library doesn't come modified.
Using a different compiler may create incompatible library.
If VS is used, does it mean the user needs to install VS to be able to use mods?

From viability perspective:
- it should be easy to use. Having to deal with build systems isn't good enough.
- Most commercial games want to protect their source code. Maybe if it's possible to only include the headers relevant to the scripting API.

To conclude it seems like too much trouble for a moddable scripting option.

-------------------------

cadaver | 2017-01-02 01:06:28 UTC | #29

Yes, if the game was built with VS users would need the exact same VS version as the main game was compiled in, due to C++'s lack of stable ABI.

Maybe you could settle with using MinGW (a fixed version) and make the game installer bundle it together. But still it would bloat the installation and cause security concerns, compared to the usual approach of having moddable scripts.

-------------------------

Pablo | 2017-01-02 01:06:29 UTC | #30

You could make RCCpp viable for modding, but I agree with cadaver, you'd need to make sure the user has the same version of the compiler to make it work. The safest solution would be to deploy also the compiler itself to make sure the user uses exactly the same version. Once you have coped with that, you can deploy your API libraries compiled and expose only the headers so that it can be used. Of course, you'll also have to make sure the user links against these libraries. You could also add some security for every method the user creates catching the exceptions and signals to avoid crashing the application/game itself.

In any case, for the purpose of modding using a scripting language such as Lua or AngelScript seems like the way to go. They have been made thinking about all these concerns and are far more easier than C++ itself. I'd say RCCpp is thought as a tool to be able to iterate faster in your prototypes or your own libraries.

-------------------------

sabotage3d | 2017-01-02 01:06:38 UTC | #31

For the Runtime-compiled C++ Is there a simple example on how to use it ? Does it need engine modification ?

-------------------------

Pablo | 2017-01-02 01:06:38 UTC | #32

[quote="sabotage3d"]For the Runtime-compiled C++ Is there a simple example on how to use it ? Does it need engine modification ?[/quote]
It needs an engine modification that you can find in the following branch: [github.com/pamarcos/Urho3D/tree/RCCpp](https://github.com/pamarcos/Urho3D/tree/RCCpp)
You have to checkout that branch and compile Urho3D defining URHO3D_RCCPP in CMake. I run the following in the root folder to compile everything from scratch in Unix:

[code]
rm -rf Build
rm Lib/*
./cmake_clean.sh
mkdir Build
./cmake_gcc.sh -DURHO3D_RCCPP=1 -DURHO3D_64BIT=1 -DURHO3D_OPENGL=1 -DCMAKE_BUILD_TYPE=Debug ..
make -j8
[/code]
Apart from that, you need a GCC-compatible compiler. In Windows, that would be MinGW.

I made all the examples in C++ work with RCCpp. The way RCCpp is used is similar to the AngelScript and Lua script examples within Bin/Data, being the RCCpp examples in Bin/Data/RCCpp. So, in order to use it you have to run:

[code]./Urho3DPlayer -w Data/RCCpp/02_HelloGUI/HelloGUI.cpp[/code]
This should compile the code for you into a shared library and load it at runtime. Then, you can change HelloGUI.cpp code (or any other file within its folder) and RCCpp will detect the change, compile, unload the old library and load the new one.

It's more deeply explained in the first post, but it's true that there is no step-by-step guide. Please note that the code of every example within the RCCpp folder is exactly the same as the original examples in C++ that Urho3D has, except for Sample.h and Sample.inl which are slightly different in case RCCpp is activated. Basically, the difference is that you have to inherit from [i]RCCppMainObject[/i] instead of Application for tour main class (RCCppObject for any other class) and use the [i]RCCPP_OBJECT[/i] macro over every RCppObject class so that it exposes the create and destroy methods.

-------------------------

sabotage3d | 2017-01-02 01:06:39 UTC | #33

Thank you for the thorough explanation. Is there a way to be made as a patch or a module, as I am keen on trying it with the latest build ?

-------------------------

Pablo | 2017-01-02 01:06:39 UTC | #34

[quote="sabotage3d"]Thank you for the thorough explanation. Is there a way to be made as a patch or a module, as I am keen on trying it with the latest build ?[/quote]
I have merged the current master branch in my RCCpp one to update it to the latest version. Unfortunately, I am not currently able to compile Urho3D in Mac. It gives me too many errors in Yosemite with clang 6.1.0. So, even though I have changed all the RCCpp files as needed after they changed quite a bit the CMake files and the source structure, I cannot really test it to make sure it's working.

I'll try to search over there how to fix the compilation and will update the change.

-------------------------

Pablo | 2017-01-02 01:06:42 UTC | #35

Ok, finally got everything compiling with latest version of Urho3D. I have only tested it on Mac, though. Please checkout the latest commit at [github.com/pamarcos/Urho3D/commits/RCCpp](https://github.com/pamarcos/Urho3D/commits/RCCpp) and tell me whether it works or not.
Please note that you have to configure Urho3D with CMake adding: -DURHO3D_RCCPP=1 -DURHO3D_LIB_TYPE=SHARED plus whatever you want.

If I have time tomorrow, I will write some Readme in the repo explaining with a step-by-step example how to use it.

-------------------------

sabotage3d | 2017-01-02 01:06:42 UTC | #36

Awesome ! I will try it out :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:06:44 UTC | #37

I am having problems enabling RCPP. When I run the Urho3d Player it says RCCpp is not enabled. I compiled with RCCpp.sh under OSX.

-------------------------

Pablo | 2017-01-02 01:06:44 UTC | #38

[quote="sabotage3d"]I am having problems enabling RCPP. When I run the Urho3d Player it says RCCpp is not enabled. I compiled with RCCpp.sh under OSX.[/quote]

I have pushed new changes to ensure that URHO3D_RCPP is enabled. Please also make sure that you don't have any CMake files cached and if using the RCCpp.sh script you are compiling the "Build" folder it generates.
Also remember to set URHO3D_HOME to your Urho3D's compiled folder (where your lib and include folders are). If you are using the RCCpp.sh script, that's the Build folder.
Apart from that, now Samples are all copied properly to the Data/RCCpp folder as it was they were in the previous version.

I hope this time you can make it work :smiley:

-------------------------

sabotage3d | 2017-01-02 01:06:45 UTC | #39

It worked with 02_HelloGUI without problems but it errored with 01_HelloWorld .
These are the errors: [codepad.org/VWjsczg2](http://codepad.org/VWjsczg2) .
I also noticed I cannot maintain the state of the application when I change the text for example it also resets the whole application to the default.

-------------------------

Pablo | 2017-01-02 01:06:45 UTC | #40

[quote="sabotage3d"]It worked with 02_HelloGUI without problems but it errored with 01_HelloWorld .
These are the errors: [codepad.org/VWjsczg2](http://codepad.org/VWjsczg2) .[/quote]
Sorry about the error in the HelloWorld example, that was my fault. I have been quite busy at work and didn't have much time to fix this and test every single sample. Fortunately, we both have similar systems and I was able to fix it quite easily. Please checkout the newest version.

[quote="sabotage3d"]I also noticed I cannot maintain the state of the application when I change the text for example it also resets the whole application to the default.[/quote]
Yep, there is no state saving right now in RCCpp as it was intended to be a PoC for fast prototyping. I am thinking about making this a lightweight runtime-compiled C++ library and do the integration with Urho3D as I have done. In there, I could implement some state saving to restore the state between different compilations. I have been taking a look at [url]http://uscilab.github.io/cereal/index.html[/url] and it looks quite promising.
However, it's up to the developer to know whether it should save and load something or not. Also, depending on what you're trying to do and how, the class may have weird behavior or even crash when reloading it. One has to take into account that not everything is destructed and constructed again, but only the classes you are working with. This means that for instance if you took the UI root node and draw something within it, if you don't remove it in your Stop (or destructor), when Start (or constructor) draws again over the UI root, you will have the same thing drawn twice.

-------------------------

sabotage3d | 2017-01-02 01:06:45 UTC | #41

Thanks a lot. Any plans for merging this with Urho3d ?

-------------------------

Pablo | 2017-01-02 01:07:00 UTC | #42

[quote="sabotage3d"]Thanks a lot. Any plans for merging this with Urho3d ?[/quote]
Sorry for the late reply, I was waiting if someone else within the Urho3D dev team answered. Actually, that's not on me but on the devs so it's for them to decide whether this is worth it or not.
On my side, I'm still thinking about the best way to take out RCCpp from within Urho3D into a lightweight 3rd-party library adding features such as serialization to save and restore the state of the scene.

-------------------------

sabotage3d | 2017-01-02 01:07:00 UTC | #43

Yeah that would be quite cool. This one looks really fast and it preserves the state: [youtube.com/watch?v=FHwJUGhXDUQ](https://www.youtube.com/watch?v=FHwJUGhXDUQ) .  Is it based on different techniuqe ? 
There are some updates here as well: [runtimecompiledcplusplus.blogspot.co.uk/](http://runtimecompiledcplusplus.blogspot.co.uk/)

-------------------------

Pablo | 2017-01-02 01:07:00 UTC | #44

[quote="sabotage3d"]This one looks really fast and it preserves the state: [youtube.com/watch?v=FHwJUGhXDUQ](https://www.youtube.com/watch?v=FHwJUGhXDUQ) .  Is it based on different techniuqe ?[/quote]
As far as I know for the posts that he did it's the same technique, but he did a very good work preserving the state. Regarding RCC++ it's been recently updated, but what I don't like too much about it is that it's not that easy to understand and use for a newcomer.

-------------------------

sabotage3d | 2017-01-02 01:07:20 UTC | #45

I also found this in-depth article for implementing Runtime-compiled C++in a game engine : [blog.molecular-matters.com/2014/ ... -the-hood/](http://blog.molecular-matters.com/2014/05/10/using-runtime-compiled-c-code-as-a-scripting-language-under-the-hood/)

-------------------------

rasteron | 2017-01-02 01:07:21 UTC | #46

[quote="Pablo"]
Sorry for the late reply, I was waiting if someone else within the Urho3D dev team answered. Actually, that's not on me but on the devs so it's for them to decide whether this is worth it or not.
On my side, I'm still thinking about the best way to take out RCCpp from within Urho3D into a lightweight 3rd-party library adding features such as serialization to save and restore the state of the scene.[/quote]

I agree with the guys here, it is a great idea and an added C++ feature. One way to find out is to update your repo, a sample demo and send your changes for PR review.  :wink: 

[b]+1000[/b] keep it up!

-------------------------

