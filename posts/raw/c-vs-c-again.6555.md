vram32 | 2020-11-20 23:16:21 UTC | #1

Oh, they are moving towards C.
That is awesome. +1

-------------------------

johnnycable | 2020-11-20 23:16:21 UTC | #2

Why would that be awesome?
Are there somewhere some real world test showing real (and especially consistent) performance gains for using C instead of C++?
Or do I have to suppose the usual, tiresome "I'm an old C goon, simply I'm too lazy to learn C++?"

-------------------------

rku | 2020-11-20 23:16:21 UTC | #3

There will be no performance gains and code will be more verbose.

-------------------------

brokensoul | 2020-11-20 23:16:21 UTC | #5

[quote="johnnycable, post:2, topic:6555"]
’m an old C goo
[/quote]

C is much better than the shitstorm that C++ is, C++ is a huge clusterfuck. http://harmful.cat-v.org/software/c++/linus

-------------------------

Eugene | 2020-11-20 23:16:21 UTC | #6

Good luck writing server software in C.
I wonder how many crashes, leaks and security holes it would have comparing to modern C++, not mentioning more safe languages like python/Java/whatever they use now I don’t keep track.

-------------------------

brokensoul | 2020-11-20 23:16:21 UTC | #7

Who talked about writing servers?

-------------------------

brokensoul | 2020-11-20 23:16:21 UTC | #8

My point was that C++ is a clusterfuck, a bloated language that brings pain and suffering to the universe. for me C is much better because it is MUCH more simple, but also not my favorite language btw

-------------------------

Eugene | 2020-11-20 23:16:21 UTC | #9

Writing servers is just an exaggerated example. Server software pushes requirements to limits. It’s just when you write other apps you may ignore some issues. They are still there tho, just less relevant. 

Does C have ways to guarantee resource release? No. Does C have safe pointer management? Again no. So, given the same magnitude of the project, you can write more secure, safe and stable code in C++ comparing to C.

-------------------------

brokensoul | 2020-11-20 23:16:21 UTC | #10

oh dear god, nevermind

-------------------------

brokensoul | 2020-11-20 23:16:21 UTC | #11

Quoting Torvalds: 

" I've come to the conclusion that any programmer that would prefer the project to be 
in C++ over C is likely a programmer that I really *would* prefer to piss 
off, so that he doesn't come and screw up any project I'm involved with.

C++ leads to really really bad design choices. You invariably start using 
the "nice" library features of the language like STL and Boost and other 
total and utter crap, that may "help" you program " 

http://harmful.cat-v.org/software/c++/linus

-------------------------

vmost | 2020-11-20 23:16:21 UTC | #12

Can a mod move this stuff to an off topic thread? Thanks

-------------------------

1vanK | 2020-11-20 23:16:21 UTC | #13

[quote="Eugene, post:6, topic:6555"]
Good luck writing server software in C.
[/quote]

nginx, apache.

I agree that C ++ is a little safer than C, but it also requires very careful use.

-------------------------

George1 | 2020-11-21 00:05:44 UTC | #14

I think let C die in peace!

-------------------------

George1 | 2020-11-21 01:29:25 UTC | #16

Yes, but the majority of android apps are not create from C.
The reason why C is popular in research and development, and hardware driver interface is because there is not many alternative. Most hardware libraries are created in C. 
In terms of software application, there are many language variant.   Some people love pascal, fortran, C++, Java, C#...

-------------------------

JTippetts1 | 2020-11-21 02:37:07 UTC | #18

A C library can be wrapped and hidden away, as most of our third party libraries should be hidden away regardless of if they're C or C++. Unless someone is seriously considering re-writing Urho3D as a C library, then this isn't really a useful argument at all. There hasn't been a productive or interesting C vs C++ flame war in the history of the internet, so I don't know why anyone would assume now was the time to have one.

-------------------------

brokensoul | 2020-11-21 03:33:13 UTC | #20

https://www.youtube.com/watch?v=1S1fISh-pag

-------------------------

rku | 2020-11-21 09:06:53 UTC | #21

You can write great code in C++ and you can write garbage code in C. You can also write garbage code in C++ and great code in C. However it is much harder to do it in C. Quoting Torvalds is one thing. Thinking you could live up to his standards only by switching a language is laughable. Programming language is just a tool. If you cant wield C++ well, what makes you think you can do better with C? After all, C++ is a superset of C. If you like - write a conservative C++, using only good stuff. C-with-classes (which is basically C-with-RAII) is much easier than C already.

-------------------------

Modanung | 2020-11-21 09:52:57 UTC | #22

> _"Within C++, there is a much smaller and clearer language struggling to get out."_ -- **Bjarne Stroustrup**

-------------------------

brokensoul | 2020-11-21 10:01:13 UTC | #23

Good job attacking a strawman. My point still stands, C++ it is a bloated language, a huge clusterfuck

-------------------------

rku | 2020-11-21 11:15:14 UTC | #24

And? What of it? Are you saying it is impossible to write clean code in C++?

-------------------------

Stuur | 2020-11-21 14:03:09 UTC | #25

I hope that one day people like brokensoul will stop treating languages as anything else then tools that you pick for specific jobs, and other peoples opinions as something else then their subjective views on said tools due to their specific needs, and stop embarrassing themself by going to forums and starting "holy wars" like this thread.

-------------------------

brokensoul | 2020-11-21 13:29:38 UTC | #26

Oh god, i don't believe you asked this. Have you ever worked in legacy codebases ? Or in a team ? Or even in codebases that your team inherited from other team ? 

Life is not simple, you will have to deal with other's people code, and C++ is terrible in this kind of situations. C is also not the best in this case, but is not even close to being as bad as C++ in this regard.

I'm done with this discussion, you are obsviouly completly lost.

-------------------------

S.L.C | 2020-11-21 14:04:27 UTC | #27

Can someone please make me understand what is the point of this topic here? In relation to the engine itself. Are we looking into converting Urho to C? Is that why people here try to pitch the C language? I just don't get it. How did we get here and what's the point.

Are we really that dumb that we must debate performance of C vs C++? As if that's where the bottleneck actually is (*for a game/engine*).

By that logic. GNUC is made in C. Clang is made in C++. I wonder who has a reputation for being the fastest.

Is listing some libraries that were made in C somewhere between 90's and 2000's going to solve anything?

By that logic GTK was made in C, Qt and Wx were made in C++. I wonder who has a reputation for being easier to use or has a higher adoption outside of Linux where it's the default for last decade distributions. So you're kind of forced to use it.

Do you see the stupidity of trying to flex a few libraries made two decades ago and saying they're more widely adopted or faster.

First of all. Those are open source and the only thing you can flex with. Considering there are better closed source/proprietary software that overshadow either of the mentioned libraries/software. What makes you think that those closed source libraries/software are not made in C++. Thus, showing you can do better in C++.

But all of that is pointless. As it was already mentioned. A language is a tool. Stop treating it like a fking religion and trying to convert everyone to it. You are exhausting to everyone around you.

Man I hate what this forum has become.

-------------------------

1vanK | 2020-11-21 14:07:21 UTC | #28

[quote="S.L.C, post:27, topic:6555"]
Considering there are better closed source/proprietary software that overshadow either of the mentioned libraries/software.
[/quote]

I would like examples

-------------------------

S.L.C | 2020-11-21 14:12:41 UTC | #29

Actually I would like a C example to which I (*or someone else*) would come up with C++ counterpart. As pointless that may be.


Clearly I haven't made expressed my complete disinterest to such behavior. But oh well. Why not entertain ourselves :smiley:

-------------------------

1vanK | 2020-11-21 14:14:56 UTC | #30

> Actually I would like a C example to which I ( *or someone else* ) would come up with C++ counterpart. As pointless that may be.

openssl

-------------------------

S.L.C | 2020-11-21 14:23:57 UTC | #31

Can you actually mention an actual software? Something what wasn't meant to run on any and all possible platforms and architectures. Which includes the Linux kernel because you need a platform or openssl (*or any ssl*) to have a secure communication layer. These being the two main domains that aren't created in C++. Not for performance reasons. But simply because of where and how they have to be used.

Was that not implied?

-------------------------

1vanK | 2020-11-21 14:25:07 UTC | #32

Oh, now my example is wrong? First you made a statement, then I myself have to look for an example, and when I gave an example, it turned out to be wrong.

-------------------------

S.L.C | 2020-11-21 14:37:37 UTC | #33

It's not wrong in the way you think. It's simply that you mentioned a piece of code that needs to be available in absolutely every possible place and/or language. Thus C. Because of its simplicity. Therefore, no one bothers do one in C++. Just as no one bothers to do a Linux kernel in C++. One exists already and there is no market for another one to make it in C++.

Let me rephrase myself: Mention an actual software/application/game engine or something that doesn't have to act as the foundation to everything else. Rendering any duplicate as absolutely pointless or a simple curiosity.

The whole discussion seems to have stemmed from a rendering(?) library being converted to C. And the benefits of that.

You turned that into kernels or libraries that everyone (*must*) use. Therefore (*as mentioned already*) rendering any duplicate as absolutely pointless or a simple curiosity.

That was your goto because you had no other choice in terms of actual software.

Goddamnit this is already (*as mentioned*) getting exhausting.

-------------------------

1vanK | 2020-11-21 14:40:02 UTC | #34

You made a statement that I do not believe. Prove or admit you were wrong. Nobody has to prove your claim for you.

> Considering there are better closed source/proprietary software that overshadow either of the mentioned libraries/software.

-------------------------

S.L.C | 2020-11-21 14:50:58 UTC | #35

I actually refuse to admit to being wrong. Just because you're stubborn, trying to avoid the obvious and trying to further continue a pointless debate does not make that statement false or wrong.

You simply puled out a library that there was no need to be done in C++ (again). As I've mentioned. You knew that and that was your refuge. The refuge of every C fanboy trying to force a stalemate in an argument of C vs (*insert language*).

I wonder why Rust is trying to replace C. When C is absolute perfection.

As expected. Pointless and exhausting. Just leave it be.

-------------------------

1vanK | 2020-11-21 14:53:25 UTC | #36

My stubbornness lies only in the fact that for the third time I ask you to give examples that illustrate your words

> Considering there are better closed source/proprietary software that overshadow either of the mentioned libraries/software.

-------------------------

1vanK | 2020-11-21 14:55:19 UTC | #37

And why did you decide that I am a fan of С?

-------------------------

brokensoul | 2020-11-21 15:22:42 UTC | #38

Omg, another strawman argument, you people are getting really pathetic, basically you want him to give a example to confirm your believes. Listen to your own advice and go do something better with your time.

-------------------------

brokensoul | 2020-11-21 15:25:19 UTC | #39

Nobody is saying that C is perfect, and nobody said that we should convert Urho to C or anything like that. This whole discussion started because someone, from nowhere started a C flamewar. Just look in the second post, what @johnnycable said

-------------------------

rku | 2020-11-21 15:35:06 UTC | #40

So you are saying _other_ people write better code in C than C++?

-------------------------

1vanK | 2020-11-21 15:39:18 UTC | #41

Are you arguing that C ++ is easier to write good code?

-------------------------

rku | 2020-11-21 15:40:39 UTC | #42

Its at very least easier not to leak memory.

-------------------------

1vanK | 2020-11-21 15:50:01 UTC | #43

In a complex program, you will not be able to keep track of the hierarchy. And you have to use one smart pointer and weak refs. Or you will get circular references (memory leak). How this differs from using a raw pointer (except overhead)

-------------------------

rku | 2020-11-21 16:01:39 UTC | #44

It is different in a sense that you can not forget to free a smart pointer.

-------------------------

1vanK | 2020-11-21 16:06:24 UTC | #45

In both approaches, an object is created and destroyed in one place. The programmer may forget to destroy the object in this place. Such a programmer may forget many other basic things. And smart pointers won't save you from that. It's just going to be a bad programmer.

-------------------------

rku | 2020-11-21 16:14:21 UTC | #46

In real life its not that simple. You know that very well. This is why it is not uncommon to see `goto` in C because people go out of their way to try and not make mistakes because language just does not do enough.

-------------------------

1vanK | 2020-11-21 16:17:38 UTC | #47

You shouldn't have mentioned goto, because there is cases when it is needed. And if you try to avoid it, you get 15 nested loops.

-------------------------

rku | 2020-11-21 16:19:20 UTC | #48

Well it should not be needed. If it is - that is a lacking programming language. If i wanted to use `goto` i might as well write assembly.

-------------------------

1vanK | 2020-11-21 16:20:48 UTC | #49

What exactly is the difference between C ++ and C, which eliminates goto. I hope you don't mean an exceptions.

-------------------------

rku | 2020-11-21 16:24:27 UTC | #50

Once again RAII. Exceptions are also fine. People do misuse them, so what? On one side we have a powerhouse language loaded with complicate features that people often misuse. On the other side we have a language that has nothing beyond basics. It is impossible to misuse a nothing as it is impossible to use it. However having some options is always better than not having them.

-------------------------

1vanK | 2020-11-21 17:32:20 UTC | #51

I searched among the c++ libraries that the engine uses. `goto` is used in Bullet, SDL, PugiXml, SLikeNet, Assimp. 

> Exceptions are also fine

Where is `finally`? In C# I can. C ++ offers a stub that cannot be used.

-------------------------

throwawayerino | 2020-11-21 17:55:31 UTC | #52

Does this thread have any purpose? Unless you're planning to rewrite the entire engine in C, C++ is the language used and the structure chosen years ago by the author is class based. If it really bothers you, then you can use raw pointers and pointer arithmetic in your code and ignore all the features that come with classes and streams. Either way, the compiler will just output the same assembly and replace all your loops with jumps and gotos.
Oh my god this place reminds me of /g/

-------------------------

rku | 2020-11-21 18:47:53 UTC | #53

Clearly we have no better things to do than debate pointless stuff :)

-------------------------

Modanung | 2020-11-21 18:55:45 UTC | #54

Of course you do, you just don't **C** it. :wink:

-------------------------

George1 | 2020-11-22 02:00:22 UTC | #55

I think we need to look at big software application.  OpenSSL is just a small library.
e.g. CAD, Word processing, or design software
Solidworks, MS word etc...

Now people can develop in any language they wanted.  There are like more than 30 different types of languages out there.

-------------------------

JSandusky | 2020-11-22 02:06:13 UTC | #56

Only reason I can think of for C is that it's the only place the GNU compilers aren't falling behind and are actually staying ahead/on-time with standards/compliance, in which case it's just a "*give GNU hugs"* agenda.

We're a long long ways from the bad days of MSVC-2005 when compliance was so bad that STL-Port was mandatory to avoid heisenbugs with Boost.

---

Port it all to objective-C and use clang. 

Everyone loses. Problem solved.

-------------------------

Modanung | 2020-11-22 07:38:34 UTC | #57

I know, building those PiRMITs is a quite a daunting task. [![](https://gitlab.com/luckeyproductions/hantik/-/raw/master/pirmit/pirmit.svg)](https://gitlab.com/luckeyproductions/hantik/-/blob/master/pirmit/README.md)

-------------------------

1vanK | 2020-11-22 07:56:39 UTC | #58

[quote="George1, post:55, topic:6555"]
e.g. CAD, Word processing, or design software
Solidworks, MS word etc…
[/quote]

Thus, do you think that there are no open source analogues for this software?

-------------------------

George1 | 2020-11-22 10:15:56 UTC | #59

Not everyone is using opensource software, maybe Linux.  But most people at work probably are using Unix rather than Linux.
If windows is opensource, it can kill Linux.  But it is late in the game for that.

-------------------------

1vanK | 2020-11-22 10:16:23 UTC | #60

What statistics do you base your conclusions on?

-------------------------

1vanK | 2020-11-22 10:19:12 UTC | #61

Can I use open source software on Windows?

-------------------------

George1 | 2020-11-22 10:20:32 UTC | #62

Based on my experience.  I used other OS before Linux is created.

-------------------------

George1 | 2020-11-22 10:28:18 UTC | #63

Why not? you can use any opensource software on Windows if you want to.
Maybe we should keep on topic.  Haha.

C is ok,  but we should think it as a tool that solve certain problems. It is not a solution for everything.

-------------------------

1vanK | 2020-11-22 10:27:54 UTC | #64

Then I don’t understand at all what you’re trying to convince me of. How the above proves

> Considering there are better closed source/proprietary software that overshadow either of the mentioned libraries/software.

-------------------------

1vanK | 2020-11-22 10:29:21 UTC | #65

[quote="George1, post:63, topic:6555, full:true"]
Why not? you can use any opensource software on Windows if you want to.
Maybe we should keep on topic. Haha.

C is ok, but we should think it as a tool that solve certain problems. It is not a solution for everything.
[/quote]

And why does everyone think what I'm talking about C

-------------------------

George1 | 2020-11-22 10:34:10 UTC | #66

I don't know, someone started the holy C and C++ war.  
To me, I love pascal better than C. But don't really care.  They are just tools.
Maybe Op can just close the topic :slight_smile:

-------------------------

johnnycable | 2020-11-22 15:30:14 UTC | #67

[quote="vram32, post:15, topic:6555"]
EDIT: And apparently [C is still quite popular](https://www.tiobe.com/tiobe-index/) for some reason.
[/quote]



The reason is rewriting software is too costly.

-------------------------

johnnycable | 2020-11-22 15:34:35 UTC | #68

[quote="George1, post:16, topic:6555"]
The reason why C is popular in research and development, and hardware driver interface is because there is not many alternative. Most hardware libraries are created in C.
[/quote]

Indeed.
The reason for using C is is you're forced to because of hardware programming. No other sane use case.

-------------------------

johnnycable | 2020-11-22 15:58:42 UTC | #69

*goto* lol...
just a couple of weeks ago I was considering using one... :laughing: :laughing: :laughing:
that would've been very funny...
but it the end I've added a do while and kept my two-level recursion... :stuck_out_tongue_winking_eye:

-------------------------

Eugene | 2020-11-26 15:37:20 UTC | #70

[quote="johnnycable, post:69, topic:6555"]
*goto* lol…
just a couple of weeks ago I was considering using one… :laughing: :laughing: :laughing:
[/quote]
`goto` is great! `embree` has dozens of them, because it's software raytracer and it really _cares_ about performance.

-------------------------

