davidpox | 2018-01-10 17:26:42 UTC | #1

Hi all, 

Looking for more clarification towards the StaticModelGroup -
Am I able to effectively update the position of the node constantly with Rigidbodies?
Currently, when testing my project, I can display 1024 nodes as a test perfectly fine but when I give each of them a random linear velocity and set their mass to 1.0f, the performance tanks completely.

Am I wrong in thinking that SMG's work like this? Are they designed to be static, or am I doing something wrong?

-------------------------

Eugene | 2018-01-11 06:18:56 UTC | #2

[quote="davidpox, post:1, topic:3936"]
Are they designed to be static, or am I doing something wrong?
[/quote]

They are.
Just use `StaticModel` by default and don't touch `StaticModelGroup` unless you really need it.

-------------------------

davidpox | 2018-01-10 18:08:07 UTC | #3

Gotcha.
Recommend any optimisation tips for ~1k moving objects? Would only updating the objects in the view be the way to go or is there something clever that I can do with Urho?

-------------------------

Eugene | 2018-01-10 18:13:49 UTC | #4

[quote="davidpox, post:3, topic:3936"]
Recommend any optimisation tips for ~1k moving objects?
[/quote]

Are you talking about 1k _simultaneously_ moving physical objects?

-------------------------

davidpox | 2018-01-10 18:16:51 UTC | #5


Yep, All going different directions, different speeds. Not much in terms of collision except 4 walls and a floor/ceiling.

-------------------------

Eugene | 2018-01-10 18:46:36 UTC | #6

1k of awake dynamic objects will always be relatively slow.
Physics calculations are quite complex on their own, so you will probably have bottleneck there and only tests on the target hardware could give you information.
Prefer simple dynamic shapes (spheres and cylinders are the best), don't know other advices.

-------------------------

Modanung | 2018-01-10 19:29:01 UTC | #7

Doesn't the _static_ in `StaticModelGroup` simply refer to them not being usable for `AnimatedModel` situations? I think the nodes can be transformed all you like.

-------------------------

Eugene | 2018-01-10 19:57:33 UTC | #8

[quote="Modanung, post:7, topic:3936"]
I think the nodes can be transformed all you like.
[/quote]
They can.
It doesn’t mean that this is better or faster than simple separate nodes.

-------------------------

cadaver | 2018-01-11 09:37:01 UTC | #9

Yeah the StaticModelGroup will LOD as one big drawable, and receive light and cull as one big drawable, which will in some cases be exactly not what you want. It's not worth using before you run into a severe rendering CPU bottleneck, and confirm it is the case.

-------------------------

