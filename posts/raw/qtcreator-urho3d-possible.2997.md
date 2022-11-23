slapin | 2017-04-09 15:06:17 UTC | #1

Hi, all!

I never used QTCreater before and find it very unfriendly and hard to use.
It seems to import CMakeLists.txt, but shows no other project files.
Also whatever options I add to CMake configuration it ignores them, so I can't compile.
Also it can't complete any files from Urho directory (and labels all #includes red.
Not that I really want to use it, but I don't want to use Eclipse because that is
really heavy and unpredictable monster. Otherwise I will not be able to cope with urho coding style
and C++ stuff as it just can't fit the brain, and working without autocompletion is not possible
because everything is so complicated and verbose.
I wonder will Kdevelop work instead? Or is it possible to make QtCreator work
without spending too much time configuring it?
I'm too used to vim + C / python for 10 years and I really doubt now that using IDE is efficient at all.
The problem is that C++ is just not designed to be used with simple tools :(

-------------------------

KonstantTom | 2017-04-09 16:11:38 UTC | #2

I use QtCreator 3.5.1 on Windows 7 and all works perfect. Maybe you mistake something in CMake scripts? You can see my project CMake scripts (they are below), QtCreator imports it successfully.
There is executable target:
https://github.com/KonstantinTomashevich/colonization/blob/master/sources/Launcher/CMakeLists.txt
There is library target:
https://github.com/KonstantinTomashevich/colonization/blob/master/sources/Colonization/CMakeLists.txt
There is main cmake script (cutted):
https://github.com/KonstantinTomashevich/colonization/blob/master/CMakeLists.txt#L54

-------------------------

slapin | 2017-04-09 16:15:12 UTC | #3

Thanks a lot for your info, I've sloved the problem by using KDevelop which is great.
Probably your solution helps somebody else.
My CMakeList .txt works fine with command line and with KDevelop, so I think this is something in QtCreator.
As I'm fine with KDevelop, I think this topic is solved.

-------------------------

