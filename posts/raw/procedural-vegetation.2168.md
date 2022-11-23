Eugene | 2017-06-15 21:13:39 UTC | #1

I have started porting procedural vegetation from my engine onto Urho3D codebase.
Here are reference screenshots from my old demo.
[spoiler][img]https://pp.vk.me/c627619/v627619834/44b54/zOKErtRL4Vg.jpg[/img]
[img]https://pp.vk.me/c627619/v627619834/44b68/wuLBXGt1d-s.jpg[/img][/spoiler]

[b]cadaver[/b],
Do you need such functionality in Urho3D core?
If yes, I'll write code according to your code standard and inside Urho. And I'll have a lot of questions.
If no, it will be a separate C++11 library over Urho3D.

[b]Update:[/b]
This screenshot demonstrates editing of procedural tree.
[spoiler][img]https://pp.vk.me/c636316/v636316834/245e4/ckQkn3wwG20.jpg[/img][/spoiler]

**Update 2:**
All related code is stored here
https://github.com/eugeneko/Urho3D-Sandbox-Dirty

-------------------------

Enhex | 2017-01-02 01:13:37 UTC | #2

Procedural generation isn't in the scope of a game engine, so I think it should be external library.

-------------------------

yushli | 2017-01-02 01:13:37 UTC | #3

The trees look quite beautiful. Thank you for sharing this. Where can I find the sample project to try out?

-------------------------

Eugene | 2017-01-02 01:13:37 UTC | #4

[quote]Procedural generation isn't in the scope of a game engine, so I think it should be external library.[/quote]
Unity devs disagree with you.

[quote]The trees look quite beautiful. Thank you for sharing this. Where can I find the sample project to try out?[/quote]
I don't want to share my old demo and I haven't finished porting. I post here as soon as ready.

-------------------------

cadaver | 2017-01-02 01:13:38 UTC | #5

Looks like a beautiful feature. And I agree that it works best as an external library outside Urho.

-------------------------

hdunderscore | 2017-01-02 01:13:38 UTC | #6

Looks nice, I hope to see it shared in some form eventually !

-------------------------

Eugene | 2017-01-02 01:13:38 UTC | #7

[quote="cadaver"]Looks like a beautiful feature. And I agree that it works best as an external library outside Urho.[/quote]
It would be cool to have such external libraries that could be easily used by anybody (like assets in Unity).

I can easily create some library and player that wraps and extends Urho.
However, this way looks very limited in the context of extensibility.
I mean that several libraries could be only merged manually.
And matryoshka-like library design is not the best solution.

Do you have any ideas how it could be resolved?

-------------------------

cadaver | 2017-01-02 01:13:38 UTC | #8

I'd recommend just providing the code files and a CMakeLists if appropriate, and some kind of instructions how people can incorporate it in their application. I don't recommend actually wrapping and extending Urho.

-------------------------

Eugene | 2017-01-02 01:13:38 UTC | #9

[quote="cadaver"]I'd recommend just providing the code files and a CMakeLists if appropriate, and some kind of instructions how people can incorporate it in their application. I don't recommend actually wrapping and extending Urho.[/quote]
Does Urho have any codebase of such external add-ons?
It's quite hard to find and re-use code from forks... And from threads in 'Feature Request' too.

-------------------------

cadaver | 2017-01-02 01:13:38 UTC | #10

I'm not aware of a "god" repository, however what you (or anyone else) can do is to make a PR into Urho's documentation to the "external links" section to include a link to your project.

-------------------------

Eugene | 2017-06-16 16:29:37 UTC | #11

This screenshot demonstrates editing of procedural tree.
[spoiler]
[img]https://pp.vk.me/c636316/v636316834/245e4/ckQkn3wwG20.jpg[/img]
[/spoiler]

-------------------------

Eugene | 2017-06-15 21:15:22 UTC | #12

**Update**

All related code is stored here. The code is dirty and unsupported but may still be useful.
https://github.com/eugeneko/Urho3D-Sandbox-Dirty

-------------------------

yushli1 | 2017-06-16 03:26:01 UTC | #13

Thank you for sharing this. Those beautiful trees at least worth adding a sample demo to Urho3D.

-------------------------

Eugene | 2017-06-16 06:29:01 UTC | #14

It would be hard, but I'll think about it.

-------------------------

RCKraken | 2018-03-11 05:29:46 UTC | #16

@Eugene Hello, I watched your vegetation test, and I was wondering how you went about implementing the wind animations to the leaves of the trees. I have only had experience writing wind animation glsl shaders for grass animation. Thank you,

Orion

-------------------------

Eugene | 2018-03-11 08:14:48 UTC | #17

Check this
 https://github.com/eugeneko/Urho3D-Sandbox-Dirty/blob/master/Asset/Architect/Shaders/HLSL/StandardCommon.hlsl
and this
 https://github.com/eugeneko/Urho3D-Sandbox-Dirty/blob/master/Source/FlexEngine/Graphics/StaticModelEx.cpp
and this
 https://github.com/eugeneko/Urho3D-Sandbox-Dirty/blob/master/Source/FlexEngine/Graphics/Wind.cpp
and Unity manual about wind, cause I copypasted things from there.

-------------------------

RCKraken | 2018-03-11 08:28:56 UTC | #18

Thank you very much!

-------------------------

