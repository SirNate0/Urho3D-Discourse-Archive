Moe | 2018-09-19 17:31:43 UTC | #1

Hey everybody, first off let me wave friendly and all - 'cause i'm new around here ... Hey!

So i started checking out Urho3D today - Got it on Win10, using CodeBlocks and MinGW.(wanna use it for the SBCs)

As stated the Samples work fine - can edit them, rebuild and all that cool stuff. However, i went to set up a project from scratch with Urho3D as libraries ... it said i think... https://www.youtube.com/watch?v=jRYO3F--KM8 <- Like that, followed that...

I got no build errors and input works proper, yet the Screen is Blank. I went with the minimal thing from the Docs (the one that is supposed to be Black) _main_loop Doc Stuff.
I then added "Hello World"-Stuff referencing the Samples source.
The screen remains Black - GUI is rendered even without Camera, right? (got a camera though)
And i also tried this one: https://github.com/urho3d/Urho3D/wiki/First-Project

Last time i worked outside of an Dev Environment like Unity or Unreal was ... idTech2 or 3 quite sometime ago. So I'm not super comfortable around building stuff from scratch. Pretty good at learning though ;)

Has anybody encountered something like that or maybe a tip?
Thanks yo!

-------------------------

Modanung | 2018-09-19 21:13:40 UTC | #2

Hi @Moe and welcome to the forums! :confetti_ball: :slight_smile:

Could you maybe share some of your code you've written so far to provide insight into what may be missing?

-------------------------

Moe | 2018-09-19 22:27:09 UTC | #3

Thanks a lot @Modanung, both for the welcome and the reply! :smiley:

The reason i did not supply any code is that i literally copy-pasted from the docs and the wiki. Then later took the minimal example from the doc and tried to add UI and other elements to be rendered.

That's why i though, in theory, copy-pasting directly from the wiki would have the same effect as me posting it here and you copying that. I can do that though - will do, after i slept and had another go.

Considering copy-pasted code is pretty hard to be faulty, is there anything else i could provide that might affect how it is (not)rendered? The build log doesn't show any warnings nor errors - says all be fine :confused: 
I mentioned, that i used that "Urho3D as Library" project setup tutorial. Maybe that is why i get weird results...

Anyways - i gonna sleep over the problem, see if some hints i can check turned up and/or try to go about it again fresh, in the morning.

-------------------------

JTippetts | 2018-09-20 06:29:46 UTC | #4

Run with logging, and see what kind of output gets put into the log. If you are building correctly, then problems like this typically occur because the application isn't finding the data and coredata folders. If this is the case, the logfile should indicate it.

-------------------------

Moe | 2018-09-20 06:29:36 UTC | #5

Oooh, @JTippetts i just had my first coffee and checked what you said - did it! Thanks a bunch!

I remember contemplating if something like that could be the problem but i dismissed it, thinking it would crash the executable or something if data was missing...

_I re-copied the "Data" and "CoreData" folders from the engines source archive and now it works as expected._:white_check_mark:

-------------------------

