LiamM32 | 2017-07-30 00:26:30 UTC | #1

I am quite inexperienced in programming.  I have compiled Urho3D and I completed the _[Setting up a Project](https://github.com/urho3d/Urho3D/wiki/Setting-up-a-Project-(CMake))_ tutorial, but I don't know what to do next.  I just don't know how a program should be structured.  Even the _[First Project](https://github.com/urho3d/Urho3D/wiki/First-Project)_ tutorial appears to be too much for me at the moment.

What should I do to gain programming experience before I'm ready to start a project in Urho?  Is there any theory I should read, or guides I should read about making the base of a C++ application?

My goal is to remake [Lips of Suna](https://gitlab.com/electric-gecko/lipsofsuna) in Urho3D, with a combination of Angelscript and C++.  Lips of Suna is a game project abandoned by it's creator.  I'm trying to pick it up, but the codebase is too much of a mess even for more skilled programmers, which seems to be stopping potential contributors.  There's also some performance issues that would likely get resolved with Urho3D.  It uses a custom game engine written in C/C++ using OGRE & Bullet, and scripts are written in Lua in a rather incomprehensible style.  So far, I've been getting it to work with OGRE 1.10 and Bullet 2.86.  I've pretty much just replaced deprecated functions with new equivalents though, as I couldn't figure out how make more complex changes to take advantage of new OGRE features.

I think I'll start with recreating the main menu before writing the game itself, likely using Urho's UI features.  This must be the easy part, and it's also what first appears when starting the game.

The only programming that I can currently do comfortably is with Arduino.  However, I have _sometimes_ managed to make little edits to open-source C++ projects, most notably when I tried to [add a retuning feature to QSynth](https://github.com/LiamM32/qsynth) (MIDI synthesizer), which didn't get finished though I got pretty far given my general lack of skills.  I learned Arduino through a high-school class, but the C++ I learned is from online tutorials I have taken since.  I have _never_ managed to fix a segmentation fault.  I hope that gives you an idea of where my skills are.

What I think I need to know now is what the codebase is required to have to make the application to run.  So far I've only been modifying existing programs which already had the main() loop or whatever's needed written, so I don't know how those parts work.  Although I have a good understanding of math and (sometimes) logic, my struggles in programming come from syntax and the low-level stuff.

-------------------------

slapin | 2017-07-21 03:21:39 UTC | #2

Be inspired, read docs and ask questions.

Start simple with small feature code with small things you want to add.
After you finish with that and feel stronger with code, plan architecture and ddesign engine for game
(Consider Urho as building blocks for your game engine, not complete engine like UE4).
Implement features from top to bottom one by one. Share your progress and ask questions.

-------------------------

Alex-Doc | 2017-07-21 04:24:46 UTC | #4

I'm not sure if I can post links to commercial websites, but I'd suggest this book:
 "A Tour of C++ (C++ In-Depth)" from Bjarne Stroustrup, you can figure out where you can find it though your favorite search engine. :) 

The website learncpp.com also has some good resources and is free.

It's also very important to keep practicing and read a lot of code, pretty much as then others said.

-------------------------

LiamM32 | 2017-07-21 06:32:29 UTC | #5

Thank you, but I think I need to further clarify where my capabilities are at.

I have read C++ tutorials.  I can easily write programs that do things such as calculating some numbers from input variables and spitting out results.  The programs that I have written from scratch before are mostly one file.  None of them had a GUI, or took any input, or output anything other than the "cout" from the iostream library.

What I need to learn is how to start making bigger, more advanced programs.  I need to know how to make a main function that connects all the .cpp files together (if that's how it works).  It would also be handy to learn how to set-up the build systems.

[quote="Alex-Doc, post:4, topic:3373, full:true"]
The website learncpp.com also has some good resources and is free.
[/quote]
Thank you.  I have read individual pages of this website that showed up on Google searches, but I never tried reading it all from the beginning.  I didn't think I needed to, as I had already read the [Tutorials Point C++ tutorials](https://www.tutorialspoint.com/cplusplus/), but I like the extra detail provided on this website.  I have already read up to lesson 1.1, and I will get back to it.

The IDE that I've been using so far is Netbeans, although I'm using Code::Blocks for those tutorials.

-------------------------

rasteron | 2017-07-21 07:37:16 UTC | #6

Start with a small game with Urho, either 2D or 3D. Have a checklist on the features of what needs to be done. Try also porting well known small games or platformers and see if you can manage to get it done. You can get an idea on some Engine API functions by checking out the examples. There's also some demos and completed games that you can pull some reference from, check out the showcase section.

The only way I see that you can start doing something with the engine is having a problem presented to you and take it from there.

Good Luck and Happy Coding!

-------------------------

DrAlta | 2017-07-26 23:29:19 UTC | #7

Are you using 0.5 or 0.8 version of Lips of Suna? I had an idea to port the the 0.5 over to Urho3D but no one seemed interested in working on LoS so I put it lower on my priority list.

-------------------------

slapin | 2017-07-27 02:14:31 UTC | #8

LoS 0.5 and 0.8 are completely different games, and I like both. If anybody actully starts porting either of them, I'd be interested to follow...

-------------------------

LiamM32 | 2017-07-29 22:43:23 UTC | #9

Unfortunately, none of the tasks that have been suggested to me are very good. They're all either too basic (like tutorials for the basic syntax of C++, which I'm already past), or just telling me to "make something with Urho", which is exactly what I'm struggling to do.  Currently, I can write a simple terminal program in C++ (using the internet for reference) that asks the user to input text and prints out a result.  However, I don't understand how more complex programs work.  I need to learn about how a more complex program is initialized, and how the main loop works.  But I'm really struggling to make even the most basic thing in Urho, so I think I should find something easier to do first just for the learning experience.

I have found tutorials on the syntax of C++, but not a more "practical guide" that teaches how to use it.

-------------------------

slapin | 2017-07-29 22:52:39 UTC | #10

What do you want us to suggest? The programming is learned 99% as self-learning - you see examples,
modify them, understand how they work, ask questions. Everything depends on you, nobody can get
experience for you. You should learn how the programming craft works. Otherwise the only way for you is to get
entry-level job in some huge company so your collegues will teach you and you will get a lot of experience quickly.
It is not easy either way.

-------------------------

LiamM32 | 2017-07-29 23:13:03 UTC | #11

[quote="slapin, post:10, topic:3373, full:true"]
What do you want us to suggest?
[/quote]
Well, it would be nice if I could see an example of a very simple GUI program that uses a main loop, with an explanation of how it works.  Maybe also point me to something that I can read on program initialization and main loops.

[quote="slapin, post:10, topic:3373, full:true"]
The programming is learned 99% as self-learning
[/quote]
Are most programmers actually self-taught?  I find that hard to believe, given how hard it is to figure it out.

-------------------------

slapin | 2017-07-29 23:37:39 UTC | #12

Well, you won't go very far with this attitude. There are examples and documentation and source code. If that is not enough to get you started, you better think a bit if your career choice is right. If you're sure, just seat and learn. It is slow process.

-------------------------

LiamM32 | 2017-07-29 23:56:56 UTC | #13

[quote="slapin, post:12, topic:3373, full:true"]
If that is not enough to get you started, you better think a bit if your career choice is right.
[/quote]
I don't think I'm naturally good enough at programming to do it as a career, but only as a hobby.  Engineering is what I plan to be my career, but I might be able to take jobs that involve small amounts of programming down the road if I manage to get better at it.

I should mention that I actually have been _trying_ to get an Urho3D program running by imitating the code in the included HelloGUI example, and also what's in [this tutorial](https://github.com/urho3d/Urho3D/wiki/First-Project).

I'm just hoping that someone could point me to a simpler example of a program with a main loop, just so I can get prepared.  That's not to say I'm not trying with what I have.

-------------------------

LiamM32 | 2017-07-30 00:42:25 UTC | #14

[quote="DrAlta, post:7, topic:3373, full:true"]
Are you using 0.5 or 0.8 version of Lips of Suna? I had an idea to port the the 0.5 over to Urho3D but no one seemed interested in working on LoS so I put it lower on my priority list.
[/quote]
Nice to see that there are _two_ people on this forum interested in Lips of Suna

My vision for the future Lips of Suna is something between 0.5.0 and 0.8.0.  I was thinking that 0.8.0 would be our main design reference when remaking it, but there's definitely some aspects of 0.5.0 that should go in there (such as the menu's).  However, 0.5.0 may be used more as a reference for the beginning of the project due to having a simpler codebase.  I was also thinking that the final project can have a "classic mode", which is a recreation of Lips of Suna 0.5.0 with new graphics.

I never got to play 0.5.0, as I couldn't get it to compile even on Ubuntu 12.04 (which I was using at the time I discovered it, but it was written for an older Ubuntu version).  However, I have seen two videos of it.  When I first saw the video of 0.5.0 (about a month after I began playing 0.8.0), [I was shocked](https://forum.freegamedev.net/viewtopic.php?f=63&t=5661), as it looked better in so many ways.  In fact, it looked very much like my vision at the time of what I wanted Lips of Suna to develop into.

It's nice to hear that you were actually thinking of porting Lips of Suna to Urho3D yourself.  I have started [this topic](https://discourse.urho3d.io/t/help-remaking-lips-of-suna-engine-with-urho3d/3396) about remaking Lips of Suna.  It would be very nice if you could help me in remaking the engine.

By the way, when you said "port 0.5 over to Urho3D", were you thinking of keeping the Lua codebase and getting it to work with Urho?  I think it should be rewritten in Angelscript with a better coding style, but I suppose that the existing Lua codebase can be a placeholder if it isn't difficult.

-------------------------

slapin | 2017-07-30 01:10:03 UTC | #15

I think it is really hard to hit many moving targets. I'd start with using existing assets (including scripts)
but with Urho as engine, and only after that I would work on script rewrites.

-------------------------

DrAlta | 2017-07-30 02:53:34 UTC | #16

Ya. 0.5.0 had a lot more polish than 0.8.0. I was going to keep the Lua codebase.

-------------------------

LiamM32 | 2017-07-30 06:43:11 UTC | #17

@DrAlta So, do you think that you will help out with the engine remake?
You can talk about it on the thread that I linked to.

It would be nice that I will finally get to try 0.5.0 myself if you actually do it.

-------------------------

