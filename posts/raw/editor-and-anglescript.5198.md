UNDEFINED-BEHAVIOR | 2019-05-29 15:46:06 UTC | #1

Was there any particular reason to why the original editor was/has to be implemented in anglescript?

-------------------------

weitjong | 2019-05-30 01:36:30 UTC | #2

You asked the question too late. The original author has left the project. But the same question has been asked a few times in this forum and the old one. If you are lucky, Lasse may drop by to say a few words again.

-------------------------

S.L.C | 2019-05-30 04:09:19 UTC | #3

My guess is that it was easy to prototype. Make changes and additions quickly without much hassle.

-------------------------

Leith | 2019-05-30 04:59:20 UTC | #4

I guess is that it was an ideal way to "harden" the angelscript implementation, but the main benefit is that you can write entire games without ever going near a c++ compiler, taking advantage of hotloading for rapid development / reduced iteration times, in a way that completely just works across platforms. This means your "dev team" can be using entirely different operating systems, and still sharing a completely common codebase. The editor uses the "player" application as an execution shell at runtime, and so can your games.
Personally, I've barely started using scripting in Urho, however I can see advantages in going totally script-driven, and totally avoiding the mixed language approach (and the platform issues it can raise).
I like the idea that we can rapid-develop in script to get stuff working quickly, identify performance bottlenecks fairly easily, and promote the offending code to native c++, and that's coming from an oldschool asm and machine language programmer. Don't be a language purist, blind to the advantages of a slower but potentially more productive language - I avoided c++ for decades.

-------------------------

Modanung | 2019-05-30 06:51:25 UTC | #5

I think this message by @cadaver (Lasse) contains the answer to your question:
https://discourse.urho3d.io/t/new-urho3d-editor-update-from-2017-11-03/2407/2

-------------------------

QBkGames | 2019-05-30 09:14:43 UTC | #6

I think the essence of the question is why AngelScript as opposed to some other more commonly used scripting language such as Lua, Javascript, Python, etc. Because now, if you want to work on the editor, you have to learn a new scripting language which might not be useful anywhere else.

-------------------------

Leith | 2019-05-30 09:37:02 UTC | #7

Actually, the eventing system makes it reasonably easy to call into and out of the scripting system, so I don't know what lasse was driving at there - subsystems were i guess the focus he had at the time, but any object can be a sender or a receiver, so its not really anything to do with subsystems

-------------------------

Leith | 2019-05-30 09:38:39 UTC | #8

You can use lua no problems, and theres also a c# fork, why angelscript? because its close to c++ and very easy to upgrade and downgrade / promote and demote code between these langs

-------------------------

Modanung | 2019-05-30 09:46:15 UTC | #9

AngelScript is more similar to C++ than any of the other languages you mentioned. So the name may be different and unknown, but its syntax is not.

As @cadaver said repeatedly, it would probably be best to have an official editor written in C++ and developed in a *separate repo* at some point.

-------------------------

UNDEFINED-BEHAVIOR | 2019-05-30 15:41:58 UTC | #10

>You can use lua no problems

>My guess is that 

>I think this message by @cadaver
...
>Probably the ideal would be, if you wanted to improve the user experience at the same time, would be to use an actual native UI toolkit in the editor and rewrite it in C++. Otherwise you’re always going to be struggling with both the editor and game taking over Urho’s subsystems.
...
https://github.com/eugeneko/Urho3D-Editor
[Abandoned] 

lol

>AngelScript is more similar to C++ 

>it reasonably easy to call into and out of the scripting system, so I don’t know what lasse was driving at there

So according to responses it seems like angel script was more of a political decision. 
Kinda glad to hear that actually. I was thinking the author ran into some technical issue only angle script could solve or something..

---

>easy to prototype. Make changes and additions quickly without much hassle.

> without much hassle.

idk but a quick glance to the issue board's editor problems and most appears to be manifestation of angel script issue in some form or another..

-------------------------

Modanung | 2019-05-30 18:26:50 UTC | #11

I personally care little for non-specific editors and scripting. My birth sign may be snail, but I am of the conviction it saves times and effort to have (at least) your editor specialized for your project. Unnecessary features slow down content creation while features that may be deemed too specialized in a general purpose editor are exactly what your project needs for fast level fabrication.

-------------------------

Leith | 2019-06-03 08:14:42 UTC | #12

I'm surprised to hear you say that you advocate for in-game editing!
Personally, I am on the fence - I have worked both with proprietary closed-source engines and more public ones, and I have to admit that there are pros and cons for each side. Your in-game editor will NEVER be "fully-featured", but it WILL support exactly what you need, and WILL require basically a full rewrite for each new project. We can pick the flesh from previous projects to add to the next, but that is all. An editor that the user can extend at runtime is the right solution, and currently, our only option is to use scripting (lua, AS or dare I say it, C#) to do that. I am trying not to say anything about runtime reflection, as the costs are awful, and I know that a binary plugin system is not going to fly on all platforms.

I like that our editor can run game scripts, but I hate that our editor can't cope with user bindings.

-------------------------

Modanung | 2019-06-03 10:55:49 UTC | #13

[quote="Leith, post:12, topic:5198"]
I’m surprised to hear you say that you advocate for in-game editing!
[/quote]

Not at all. Although in-game editing has its place and can be neat, that is not what I meant. I *do* mean having a separate application to create levels. Just imagine making dozens of worlds like these using the default Urho, Unity or Unreal editors:
![WC3ed](//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/8d596db971b05d0a56f68adb4807d13fba47ba60.jpeg)

I think Dante Alighieri neatly described the mental state this would bring a person in.

-------------------------

Leith | 2019-06-03 09:05:58 UTC | #14

The conundrum for the time being, is that binary user code will not run in the editor, period.
Script will, even more than one kind, but not native plugin code, even if we provided code for script bindings, I could be wrong, please tell me I am wrong

-------------------------

Modanung | 2019-06-03 16:07:15 UTC | #15

Indeed (I think) this would require modifying the engine, but since Urho3D is open source that's perfectly possible. Although maybe not ideal.

...of course specific editors - like Warcraft III's World Editor - are almost always proprietary software and only suitable for modding. Open source world creation tools like Tiled and Edddy are attempts at filling these gaps. Aiming at a balance between specialization and versatility.

-------------------------

Leith | 2019-06-03 09:17:21 UTC | #16

It really detracts from the editor, that it cannot grok user binary code even though we are forced to provide rtti in our compiler settings

-------------------------

Leith | 2019-06-03 09:19:09 UTC | #17

basically, "my c++ zombies stand still" in the editor, and we could easily deal with this for common frame events, even with an "unknown" interface in play

-------------------------

JTippetts | 2019-06-03 14:15:17 UTC | #18

[quote="Leith, post:14, topic:5198, full:true"]
The conundrum for the time being, is that binary user code will not run in the editor, period.
Script will, even more than one kind, but not native plugin code, even if we provided code for script bindings, I could be wrong, please tell me I am wrong
[/quote]

If you write a custom component in C++, and link it with your player executable, it will be available in the editor. When you call RegisterFactory, provide a category name string and it will appear in the create component menu option. Any attributes registered as attributes will be reflected in the node attributes dialog, and it will receive the events that it registers for.

This actually caused me a tiny issue once, as at one point I made use of a TimedDeath component for certain entities, that would receive Update events and decrease a timer until 0, at which point it would remove the node it belonged to. In the editor, any time I added that component to a node, the whole node would disappear 1 second later (the default TTL).

-------------------------

Leith | 2019-06-04 05:43:01 UTC | #19

The problem there is, I don't rely on the player executable - my project has its own executable, whose source was derived from the sample application framework.
Merging my project with the player sourcecode would be a possible solution.
Linking unreferenced object code in the player clearly won't work.
What do I need to do to force the inclusion of my custom components in the player?

Oh I just realized!
I just need to register my new classes in the Player sourcecode, and all is well - the code is referenced and will be included by the linker (fingers crossed)

-------------------------

jmiller | 2019-06-04 05:44:54 UTC | #20

[quote="JTippetts, post:18, topic:5198"]
If you write a custom component in C++, and link it with your player executable, it will be available in the editor. When you call RegisterFactory, provide a category name string and it will appear in the create component menu option. Any attributes registered as attributes will be reflected in the node attributes dialog, and it will receive the events that it registers for.
[/quote]

Maybe a candidate for adding to docs somewhere?
[#EditorInstructions_Workflow](https://urho3d.github.io/documentation/HEAD/_editor_instructions.html#EditorInstructions_Workflow)

-------------------------

UNDEFINED-BEHAVIOR | 2019-06-04 13:45:47 UTC | #21

Most people here might have already been aware of this urho fork.
https://github.com/rokups/rbfx
Appears to have the most actively developed (and mostly functional) native editor, that I've came across thus far.

Just for reference.

-------------------------

