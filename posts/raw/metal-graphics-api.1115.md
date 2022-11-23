sabotage3d | 2017-01-02 01:05:33 UTC | #1

Are there any plans for integration of the Metal API  in Urho3d ? It seems that Apple is moving forward with its integration into OSX.

-------------------------

cadaver | 2017-01-02 01:05:33 UTC | #2

I can only speak for myself, but at some point in the future (may be far away, so don't ask for any concrete timeframe) it will surely be interesting to play with the "to-the-metal" APIs. However I'm primarily a Windows guy instead of Apple, so I'd probably look at Direct3D12 first, or even Vulkan if it appears soon enough.

-------------------------

glebedev | 2018-06-12 14:21:38 UTC | #3

It is time :-) Metal is obligatiory on MacOS now

-------------------------

Sinoid | 2018-06-15 07:37:33 UTC | #4

Already done all of this. DX12 took 2 and a half weeks. Vulkan took 2 weeks. Metal took 3 days. If you want to buy the ports then PM me: 3k each.

Oculus mobile took 1 week (SDL had to go). Switch, PS4, XB each took 3 weeks a piece - 7k for those ports.

I had already worked with all of them professionally though (DX12 3x, Vulkan twice, and metal once). There is no LCD between them. Metal sucks at shading, extremely.

-------------------------

johnnycable | 2018-06-15 10:16:04 UTC | #5

[quote="Sinoid, post:4, topic:1115"]
Metal sucks at shading, extremely
[/quote]

Interesting. What exactly?

-------------------------

Sinoid | 2018-06-20 05:03:42 UTC | #6

@johnnycable

The whole pipe. Metal was mostly just VS/PS for quite a while and in general they've been pretty brutish about it all. The functions used for access of information are about as opposed as functions that return strings can be.

They also didn't solve a real problem. Like Vulkan, Metal on iPhone is different than Metal on Mac. Basically, it's just GLEW again.

The API is generally quite pleasant except with shaders. It's stupid easy to work with. I suspect someone better and more informed than I could do an Urho3D port to Metal in hours instead of the 2-3 days it took me. 

---

Offtopic: If Urho3D really really wants to live ... it needs to move to **premake**, cmake eats shit on consoles.

All of the above boasting and offering, premake only.

-------------------------

Eugene | 2018-06-20 08:11:58 UTC | #7

[quote="Sinoid, post:6, topic:1115"]
Offtopic: If Urho3D really really wants to live … it needs to move to **premake** , cmake eats shit on consoles.
[/quote]
I don’t consider it as the biggest obstacle since Urho upstream was never optimized and ported for consoles. I mean renderer and these optimizations.

-------------------------

cadaver | 2018-06-20 14:28:53 UTC | #8

Open source and consoles doesn't go together well anyway, because that'd mean maintaining a private / hidden repo for those who can prove to be valid developers with devkit access. Or else, it just means independent duplicated work.

-------------------------

