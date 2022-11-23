GoldenThumbs | 2019-07-20 23:13:34 UTC | #1

I have decided that I need to learn C++ in order to properly use Urho3D. Until now I've done mostly shader work, and the small amount of code I needed to get those to display was in Angelscript. I checked out a book on C++ at my local library so I can understand the basics. Every time I've tried learning C++ prior I was on my own, no guide or anything. I never got far. I'm hoping this book will at least let me wrap my head around the language. Any other resources that you guys would recomend for learning C++? Just general C++, I am learning this to use Urho3D but it doesn't have to directly relate to Urho. Any good websites or books that I can get easily? If you have any good tutorials please post a link to them here. Thank you for the help. :slight_smile:

-------------------------

SirNate0 | 2019-07-20 23:28:14 UTC | #2

This is what I learned from, but it is pre-c++11, so it won't be complete. Basically, I used this to get an understanding of how c++ works (syntax, pointers, etc.) but it was only through actually using it in a small- to mid-sized project and debugging all the mistakes I made that I actually learned the language.
[http://www.cplusplus.com/files/tutorial.pdf](http://www.cplusplus.com/files/tutorial.pdf)

They also have [http://www.cplusplus.com/doc/tutorial/](http://www.cplusplus.com/doc/tutorial/) which does include c++11 features, though I haven't actually used these.

-------------------------

GoldenThumbs | 2019-07-21 00:01:20 UTC | #3

Thanks! I will check it out!

-------------------------

Leith | 2019-07-21 06:32:53 UTC | #4

The great thing about C++ is that you can pretty much learn it as you need it (kinda like guitar).

When you look at other people's work, you'll occasionally see new things that you don't fully understand.
This gives you a chance to play with that new feature in isolation and understand it completely, before adding it to your ever-growing "tool box" of techniques and language features.

If you ever "get stuck", there's literally millions of programmers around the world who are more than willing to help you - maybe not do your work/homework for you, but definitely willing to explain things and generally point you in the direction of the answer.

That being said, and even though Urho3D is exceptionally well-written and clean sourcecode, the engine codebase is quite large, and daunting for a new C++ programmer to attempt to understand.
Be patient with yourself, learning anything new has a "learning curve" which is always steepest at the beginning, and which always eases over time.

I'm currently struggling with Angelscript/C++ interop dramas.
One would think it would be trivial to call from one language to the other and back again, but there are some hurdles and pitfalls and I'm still working them all out...

-------------------------

jmiller | 2019-07-21 13:36:35 UTC | #5

 **Bjarne**'s style in code and as an instructor appeal to me. He brings out the elegance in the rather complex language of C++.
On his site is a wealth of resources (and he will not do our homework too :) ).
http://www.stroustrup.com/C++.html

Books? His *The C++ Programming Language* does cover the entire language exhaustively but other books come as recommended, some as primers or for different backgrounds. This list appears to be maintained.
  https://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list

A fairly complete online C++ reference.
https://cppreference.com/

-------------------------

Modanung | 2019-07-21 16:41:43 UTC | #6

I think Bjarne's [_Tour of C++_](https://isocpp.org/tour) strikes a good balance between being concise and informative.
A good IDE also helps great deals. Personally I'm quite fond of [Qt Creator](https://www.qt.io/download).

-------------------------

SirNate0 | 2019-07-21 17:09:39 UTC | #7

Seconded about a good IDE and about Qt Creator as a suggestion. Letting the IDE deal with the exact spelling and capitalization (yay autocomplete) is nice when trying to figure out a language (except for the rare occasions when it tries to correct something incorrectly). To me, even more important are the nice debugging features that most IDEs provide - debugging from the console is doable, but not something I enjoy.

-------------------------

johnnycable | 2019-07-22 15:07:42 UTC | #8

Welcome to the club. Think about it: finally you get away with those pimplebones of angelscript or lua (yuch), javascript or pisqueakscript (bleahrg), czharp (pouh), and python (ok, save python), to finally appraise pure power.
In the beginning you will cough your blood out, praise the gods and grimace people away. But in the end (1 to 5-10 years) you'll be feeling proud.
But fear not. Over those lonely nights, coredump after coredump, think you're not alone.

Starting book:
A Tour of C++, Bjarne Stroustrup, C11
Online references:
http://www.cplusplus.com/
https://en.cppreference.com/w/
a more neat reference:
https://devdocs.io/cpp/
some more when you beef up
exercises: use Urho3d

Of course, don't lose your time with pre C11. C11 is here to stay. C before, just dying dizzy old programmers use that

(p.s. forgot about java. Die!)

-------------------------

TheComet | 2019-07-23 16:20:20 UTC | #12

Along with all of the suggestions, I cannot stress enough how important it is to learn to use a debugger. printf() is NOT an adequate debugging tool in C++, especially when your code crashes or malfunctions in bizarre ways.

You should be using breakpoints, stepping through your code and looking at stack trace/variable watches/etc.

-------------------------

Modanung | 2019-07-23 22:45:50 UTC | #13

`assert()` and `Log::Write()` are also handy (temporary) diagnosis tools.

-------------------------

codexhound | 2019-08-06 03:06:37 UTC | #15

Wish you luck. IMO anyone who wants to program should start with the basics first, C and C++ as by learning them you get an understanding of how software works in general. C is a very low level language by itself. Myself, I've been coding in C++ for awhile and there are still things I sometimes find in examples that I didn't know you could do or just have never needed before, for example, being able to make your program more dynamic by mapping actual function pointers as variables. I know sounds crazy but that's why C++ is one of the best because you are allowed to do manual manipulation of memory at the lowest levels.

-------------------------

codexhound | 2019-08-06 03:05:43 UTC | #16

C and C++ are all part of the same language. You should learn the latest C++ methodology though, as it makes things much simpler. QT is also a great library to start off with by compiling it. download the source and learn how to compile the source-code yourself.

Learn the standard STD library. Maps are all important for pretty much everything you do.

-------------------------

Leith | 2019-08-06 06:21:53 UTC | #17

Given the learner already had a background in several script languages that feature OOP, I felt that only a "crash course" in C++ features and syntax was warranted - a total of 17 single-file examples was provided, using STL as an imposter, and we're now ready to explore Urho - we may not be an expert C++ coder, but we now know enough to get by in Urho projects, and besides, Urho itself does not tend to use "new" features of the language, so only what was relevant was covered. Some low-level concepts, including binary enums and bitshifting and the common binary logic operators, but not much of the very top end stuff was included.

-------------------------

Sinoid | 2019-08-06 07:33:47 UTC | #18

@Leith

It's impossible to compile Urho3D to a straight C++03 target, being the oldest *clean* target in K&R purist eyes. You just saw this with the `using` usage for shadowmap blurs, which is a C++11 feature.

It's 2019, please use texture arrays for fucks sake.

-------------------------

Leith | 2019-08-06 07:34:33 UTC | #19

I have indicated at every step, that learning c++ can take up to ten years, and that there is more to explore on your own - I aimed for the sweet spot, and so does Urho in terms of what parts of c++ are used - particularly, I drew attention to common containers, and how Urho has a version of every container we touched on in the 17 lessons

-------------------------

Leith | 2019-08-06 07:35:22 UTC | #20

early examples included an abstract value container...

-------------------------

Leith | 2019-08-06 07:38:40 UTC | #21

I've not even touched on render tech yet, except for custom debug drawing, but I promise to use texture arrays appropriately, if or when it comes up :love_you_gesture:

-------------------------

Sinoid | 2019-08-06 07:57:51 UTC | #22

Texture arrays are my personal crusade. They are glory and they are versatile. They're also more than a decade old and still under used.

-------------------------

GoldenThumbs | 2019-08-06 22:35:43 UTC | #23

An array of textures sounds useful AF to me, but something tells me it's a bit more complex than that. Is it kinda like a megatexture in the ID tech engines?

-------------------------

Leith | 2019-08-07 05:35:15 UTC | #25

The learner has indicated that they can already code shaders, at which point I was happy to condense the learning material to suit the needs of the learner
I have not touched on any rendering stuff yet, but some undisclosed lessons do touch on some basics - we'll get there rapidly, once we are done playing catch-up

-------------------------

TheComet | 2019-08-07 08:14:02 UTC | #26

This whole thread has become so weird :confused:

-------------------------

Leith | 2019-08-07 11:03:54 UTC | #27

I don't know what you can see, but I work with the OP, I agreed to rapid accelerate the OP

-------------------------

Lumak | 2019-08-07 19:41:59 UTC | #30

We currently have no texture array example, not even the terrain shader uses it. It's all texture 2D.
The minimum requirement for OpenGL is shader version ES 3.0 and something yet supported by Urho3D. 
You can find more info -- https://discourse.urho3d.io/search?q=texture%20array

-------------------------

TheComet | 2019-08-08 06:45:18 UTC | #31

We are all here to help. As you said yourself, you aren't more qualified, in fact, I'd say the Urho3D developers and frequent users are the most qualified.

It's become weird because you've transformed this thread into a situation where we (the community) are talking through a middle man instead of talking with the OP directly.

If OP has questions OP is fully capable of asking them himself on this forum. He doesn't need you to ask them for him.

-------------------------

GoldenThumbs | 2019-08-08 06:49:51 UTC | #32

Wait what's going on? I'm very confused. I'm not even getting every notification from this topic and everyone is fighting.

-------------------------

TheComet | 2019-08-08 06:54:14 UTC | #33

You are the learner and @Leith is the master. I hear your powers have doubled the last time we met?

-------------------------

GoldenThumbs | 2019-08-08 07:02:12 UTC | #34

[quote="TheComet, post:33, topic:5316, full:true"]
You are the learner and @Leith is the master. I hear your powers have doubled the last time we met?
[/quote]


I wouldn't say that, I can just kinda undertand C++ code and write some basic stuff. I feel like I'm not really taking full advantage of having a tutor and I'm not asking enough questions. I've always found it easier to have things explained to me the first time and then have time to absorb the information on my own and untangle the coiled strands of information at my own pace. @Leith has a teaching style that more relies on the student asking more questions instead of giving all that information at once and having them figure out most of it on their own. Or I'm just an idiot and I'm reading too fast. Either or really.

-------------------------

Leith | 2019-08-08 13:58:17 UTC | #35

First there are 17 rapid acceleration lessons in c++ aimed at people who can already code oop, then there are, to date, 6 elementary lessons in urho, which are deliberately geared to lead toward the samples... The intent is to provide a baseline set of knowledge and skills, and ease the learner into discovering the samples, rather than having the samples thrust upon them. If it turns out to prove useful to one, I will offer it to others, post it on the wiki, whatever. I just want to give back.

-------------------------

GoldenThumbs | 2019-11-03 23:16:33 UTC | #36

I haven't been able to do any coding lately because my PC died, but I really want to start working on a custom fork of Urho3D. Just experiment with various ideas until I have something that's worth giving back. Something that I just found out about and kinda want to play with is "Moment Shadow Maps", but I still have a lot of research to do before I could ever work on implementing it.

-------------------------

