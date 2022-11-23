devrich | 2017-01-02 01:02:37 UTC | #1

Hi,

As a new comer to Urho3D I am extremely excited to get developing on my game ideas right away  :smiley: 

I find the Urho3D Editor to be extremely impressive and it has just about everything at your finger tips.  I also find that with just starting out, it seems to be quite a lot more complicated than I had expected.  I like the Urho3D Editor and it's extremely awesome what it does particularly in real-time editing.

but I was wondering how to best get started with Urho3D using text editors like gedit?  I mean with all the files in the engine:

1:  How do I start with just a blank empty Urho3D project; where is function main or do I not use a funciton main?

2:  Do I just create my own .h/.cpp files and include them ( if so then where? ) ?

3:  How do I go about ( on Linux Mint 17.1 ubuntu 14.04 ) compiling and running my changes as I go along? For example: create box, change box scale, change box scale again, change box scale yet again.... and each change rebuild and run to see the changes.

4:  And last but not least, how do I tell Urho3D to build a debug Android App ( i have the SDK's and the NDK Dec 2014 r10d [url]https://developer.android.com/tools/sdk/ndk/index.html[/url] )?  Do I have to do something in particular to get Urho3Dto my Android tablet for "on-device" testing?

For example: create a Android Build folder somewhere then use terminal at that folder then run
*> ant debug clear
*> ant debug install
or is there another method to get my Urho3D game project to my tablet for "on-device" testing? ( i already have the tablet in developer mode )

Please bare with me if this seems like an "Read the manual" moment but I am just slightly unsure about how things work from reading up on everything.  I am certain that it's 'me' partially confusing myself and partially' coming from various other engines from over the years :blush:

-------------------------

Bluemoon | 2017-01-02 01:02:38 UTC | #2

[quote="devrich"]

1:  How do I start with just a blank empty Urho3D project; where is function main or do I not use a funciton main?

2:  Do I just create my own .h/.cpp files and include them ( if so then where? ) ?
[/quote]

Welcome to the Urho3D community :slight_smile: .
I believe this link [url]http://urho3d.github.io/documentation/1.32/_main_loop.html[/url] will answer the first two questions, this article is also contained in the doc of the distribution

-------------------------

JTippetts | 2017-01-02 01:02:38 UTC | #3

If you read the page [url=http://urho3d.github.io/documentation/1.32/_using_library.html]Using Urho3D as an external library[/url], it outlines a suggested project framework structure. It also details how to structure the CMake build. To start with, I recommend using the bootstrapping code provided by the Urho3D player application (in Source/Tools/Urho3DPlayer and Source/Urho3D/Engine/Application.h and .cpp) as a guide. The engine code defines a main() for you (using appropriate #ifdefs and macros to abstract away the details; see Source/Urho3D/Core/Main.h).

If you want to continually change and re-run things, I highly recommend you start with just the Urho3D pre-built player and write your application in either Lua or AngelScript. No recompilation necessary, just edit script and re-run the application. Once you get things nailed down, then you can start re-writing parts as C++ if necessary/desirable.

-------------------------

weitjong | 2017-01-02 01:02:38 UTC | #4

[quote="devrich"]3:  How do I go about ( on Linux Mint 17.1 ubuntu 14.04 ) compiling and running my changes as I go along? For example: create box, change box scale, change box scale again, change box scale yet again.... and each change rebuild and run to see the changes.[/quote]
You need an IDE. That's for sure if you are working on a serious or large project. GEDIT just won't cut it even when you have enabled all the developer-friendly plugins. Personally I use "vi" though (I am joking of course, but no, I am quite serious). The good IDE candidates are (not in any particular order): Code::Blocks, Eclipse (with CDT plugin), and Qt Creator. Both Mint and Ubuntu should have these IDE software packages available in their repository, so installing them is very easy. You should learn how to perform a debug run in the IDE of your choice. That should reduce the number of change/rebuild/run iterations considerably while ironing out any logic error. However, you should use the provided "Editor" app (not the text editor) to see the effect of changing the box size or other attributes. Use the right tool for the job.

[quote="devrich"]
4:  And last but not least, how do I tell Urho3D to build a debug Android App ( i have the SDK's and the NDK Dec 2014 r10d [url]https://developer.android.com/tools/sdk/ndk/index.html[/url] )?  Do I have to do something in particular to get Urho3Dto my Android tablet for "on-device" testing?[/quote]
This is not an easy question to answer. Urho3D Android project is Java project with C/C++ native code. With an Android IDE you should have no problem to debug into the Java side of the code. But it is another story to cross the border boundary to the C/C++ native side of the code. Let's not get ahead of yourself. I think you can find it on Google easy enough on how to deploy Android app into your Android device and those instructions should work on Urho3D app. But, I think you need to create your Android project first  :smiley:  . Alternatively, you can test out the sample apps provided by Urho3D project on your Android device first by following the instruction here ([urho3d.github.io/documentation/1 ... ng_Android](http://urho3d.github.io/documentation/1.32/_building.html#Building_Android)).

-------------------------

devrich | 2017-01-02 01:02:38 UTC | #5

I can't thank you guys enough!  All of your information and insights is exactly what I needed  :slight_smile:   I'm going over everything you all said and am going to get started on the samples to android first to see how my tablet handles them and then go for development along your suggestions.

Years ago I spent over 5 years being one of the top developers with another engine that's gone now and I got rusty.  I'm really eager to see what I can do with Urho3D and share/help where I can :smiley:

-------------------------

