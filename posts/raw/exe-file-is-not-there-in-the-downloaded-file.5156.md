gvnarendra | 2019-05-17 10:09:27 UTC | #1

Downloaded the Urho3D. after unpacking i do not see any exe file to execute it. How to proceed?

-------------------------

Leith | 2019-05-17 13:13:55 UTC | #2

Hi gvnarendra! Welcome to the Forum!

You have downloaded the sourcecode for Urho3D - for the sake of clarity, lets call that the "master" folder. The master sourcecode is meant to be "platform agnostic" - it's a blueprint that we can "unroll" for a specific target machine and compiler.. It's going to help us to create a project that targets our chosen compiler, so we can build urho3D using our compiler and target platform of choice.
One way to proceed is to use CMAKE to generate a "build folder" from your "master" - this is essentially a C++ Project for a compiler of your choice. You said "exe" - can I assume you're using Windows? Do you have Visual Studio installed? Choose it in CMAKE as your target compiler.
Once you have generated a "build folder", finally, you can build the Urho3D Project (in the build folder), which will generate a folder called "bin" (in the build folder), which contains your Executables. It will also create a folder called "lib", which contains the lib file for use in your own projects, assuming you choose not to use the "player app" (see bin folder).

-------------------------

gvnarendra | 2019-05-17 13:47:24 UTC | #3

Ok thank you
I will try the method. Yes I am using Windows 10

gvnarendra

-------------------------

S.L.C | 2019-05-17 14:03:59 UTC | #4

[quote="gvnarendra, post:1, topic:5156"]
Downloaded the Urho3D.
[/quote]

What did you actually download? The source code or the [pre-built binaries](https://sourceforge.net/projects/urho3d/files/Urho3D/)? Because you won't find any executables in the source code.

-------------------------

gvnarendra | 2019-05-17 14:25:34 UTC | #5

i down loaded from this link  [https://sourceforge.net/projects/urho3d/](https://sourceforge.net/projects/urho3d/)

is there any other link to down executable urho3D?

thank you

gvnarendra

-------------------------

Leith | 2019-05-17 14:43:44 UTC | #6

Give a man a fish, and he'll eat for a day.
Teach a man to fish, and he'll never go hungry!

-------------------------

gvnarendra | 2019-05-17 14:46:09 UTC | #7

I am not a game developer. But would like to make a 3d printable  from  2d photographs of persons. Please guide me for the free softwares

required. Thanks in advance.

gvnarendra

-------------------------

johnnycable | 2019-05-17 14:56:53 UTC | #8

Here.
https://blenderartists.org/t/autoface-create-rigged-and-textured-character-from-a-single-photograph/1154237

-------------------------

Leith | 2019-05-18 12:41:34 UTC | #9

I don't mind helping people with their projects, whether they be commercial or personal. But I do mind helping people to earn their degree when they don't deserve it. I will help you learn to fly - I will even push you out of the nest, but I will not give you a free ride.

-------------------------

Omid | 2022-09-08 11:49:53 UTC | #10

Do you think this is a right answer here???
When you go to a bakery and ask for a cake they give you a cake or how to bake a cake???? 
Do you like this example? I really do not understand what is happening to this project. Wrong decision after wrong decision. 
Why I have to spend lot of time to understand how to build it? I don't need to know. i only need binaries. static or shared library and that set. not prepare 3 different machine to cover all the builds for all platforms.

If you cannot help or do not have a correct answer for a question. I suggest you to do not write anything.

-------------------------

SirNate0 | 2022-09-08 17:14:38 UTC | #12

I am a bit confused as to your reply. I think helping users understand how to build the library (teaching to fish) is very useful, as users will have to build their game, which is generally a similar experience. I think a fairer analogy (unless you only intend to use scripts for your game) is that you can make a cake (your game) from a packaged mix and other ingredients, or you can skip the packaged mix and make that part as well (build Urho as well). The skills and tools needed between the two aren't very different, it's just a little more tedious to make your own mix (build Urho) than to get it prepackaged one, but you have more flexibility in what goes into it (e.g. disable unused engine components).

As to the builds, I think you only need 1 computer if you have a Mac. I'm pretty sure cross compiling for Windows and building for Android works from it, in addition to the obvious builds for OSX and iOS from it. I know it does from Linux at least. If you don't have a Mac, it's Apple that makes it difficult. I would welcome a solution to that as well.

If I'm wrong about that in the present feel free to correct me.

-------------------------

