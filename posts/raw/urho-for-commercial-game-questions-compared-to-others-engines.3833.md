Elendil | 2017-12-10 18:57:33 UTC | #1

I want start learn some 3D engine and I want the "freedom" with engine. This means, I can create any game with it. For me, Ogre and Urho looks good for it. I know Ogre is only rendering engine, I describe it later why I mention it.

1. Is possible now create with Urho some game as commercial? Is Urho stable? It is good idea? I am asking because under info there are some limitations mentioned:

> Though Urho3D already contains several useful features and implements a framework for 3D games and applications, it is not yet a complete out-of-the-box game creation toolkit. Some things you can expect having to work on, or to require skills for: (contributions to the project are naturally welcome)
> 
> * C++ for performance-critical code and improving existing subsystems such as networking, physics and animation, depending on your needs

This is not clear to me. That means Urho is not optimized and networking, physics and etc.. it is my responsibility to integrate in to engine? (I am sorry, my english is not so good as it maybe looks :))

2. How would you compare Urho with other engines? I mean overall usage of engine, not in displaying nice graphics.
I have interest in Unreal Engine, CryEngine, both are free, because there is lot of done, like nice editor. Big down are system requirements. I dont know if I can create more low level graphic game running in old hardware, but with Urho (I played with samples and run smoothly) or Ogre I am sure I can. Another area is programing. With Ogre or Urho, it looks like you have everything under control, on UE or CE, I am not sure.

 I mention Ogre, mainly because Urho is inspired with this rendering engine. But Ogre have advantage that there are some commercial games created with it. I played Torchlight 2, and it looks and run very good even on my old notebook with integrated graphic card.

-------------------------

1vanK | 2017-12-10 19:30:41 UTC | #2

[quote="Elendil, post:1, topic:3833"]
Is possible now create with Urho some game as commercial?
[/quote]

yes

> How would you compare Urho with other engines?

this is the best engine, if you are ready to write everything you need on your own, but not just combine components to application

-------------------------

Eugene | 2017-12-10 20:08:01 UTC | #3

[quote="Elendil, post:1, topic:3833"]
Is possible now create with Urho some game as commercial?
[/quote]

It is possible. Well, there are a lot of possible things in the world... You could create commerical game with plain C++, so you could do the same with Urho. With much less effort.

[quote="Elendil, post:1, topic:3833"]
Is Urho stable?
[/quote]
Very flexible question. Yes. For me, it never crashed with well-formed code. But I suggest you to avoid DLL version of Urho just for case.

[quote="Elendil, post:1, topic:3833"]
It is good idea?
[/quote]
Who knows? E.g. Unity power has been proven by thousands of people, including commerical companies. Urho has much smaller community.

[quote="Elendil, post:1, topic:3833"]
That means Urho is not optimized and networking, physics and etc… it is my responsibility to integrate in to engine?
[/quote]
It means that Urho gives you set of features, but you shouldn't rely only on them. It's not end-user toolkit like Unity, it is open-source confugurable C++ framework.

This is both advantage and disadvantage.
If you miss some feature, you could always implement it on your own with best performance ever possible (unlike Unity etc)
If you miss some feature, you would probably have to implement it on your own, because there is no paid full-time team to work on requests.

There are several _important_ things are missing in Urho now:
- Good native Editor (work in progress, there is developing version of Editor)
- Compute shaders. There is BGFX port WIP, compute shaders would probably be implemented when it finished.
- Asset pipeline. There is _something_ like asset pipeline, but much less user-friendly than in the Unity.

-------------------------

1vanK | 2017-12-10 20:11:59 UTC | #4

[quote="Eugene, post:3, topic:3833"]
It is possible. Well, there are a lot of possible things in the world… You could create commerical game with plain C++, so you could do the same with Urho. With much less effort.
[/quote]

I think question about license

-------------------------

Elendil | 2017-12-10 20:53:30 UTC | #5

No, it is more open question. Each point is one complex question and for better understand I use more questions inside point. You can answer each one question or to the point, or as you wish.

Thanks 1vanK and Eugene for the answers.

-------------------------

Elendil | 2017-12-10 20:58:33 UTC | #6

[quote="Eugene, post:3, topic:3833"]
Very flexible question. Yes. For me, it never crashed with well-formed code. But I suggest you to avoid DLL version of Urho just for case.
[/quote]

You mean dynamically linked Urho or something other?

-------------------------

Eugene | 2017-12-10 21:29:44 UTC | #7

[quote="Elendil, post:6, topic:3833"]
You mean dynamically linked Urho
[/quote]
Exactly. Theoretically, Urho should work fine when linked as DLL.
Practically, several people reported crashes due to memory sharing problems...
So, I suggest you to avoid DLLs in C++ entirely and in Urho partuculary.

-------------------------

artgolf1000 | 2017-12-11 00:51:54 UTC | #8

If you can write shaders, and fine tune the physics system, Urho3D is a good choice, for you can control everything.
But it is lack of some important features, such as global illumination, which is cool for outstanding games.

-------------------------

jmiller | 2017-12-11 21:29:43 UTC | #9

I would re-iterate most things Eugene and others have said. :slight_smile:

[quote="Eugene, post:7, topic:3833"]
Theoretically, Urho should work fine when linked as DLL.
[/quote]

My own anecdote: I almost always link to Urho as shared library (so/dll) as it is less resource-intensive by an order of magnitude (compare link times).. but with C++ one should be aware of the ABI hazards that currently stand (which C++17 appears to be addressing with 'Modules'. :cool:). One could use static for distribution or particular case..

BTW:  https://discourse.urho3d.io/t/torchlight-2-ish-occlusion-ghosting/109 in Urho

-------------------------

