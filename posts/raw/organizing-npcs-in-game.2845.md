slapin | 2017-03-03 12:56:21 UTC | #1

Hi, all!

I know there are some experienced game devs here, so I'd like to have some idea.
I watched some GDC videos trying to grasp the subject, but it did not help. I don't have
much experience with such game structures so I'd like to get some insight.

In GDC videos they say about some characters not having something like Entity and some don't,
so I wonder, is this related...

The particular presentation I speak about is http://www.gdcvault.com/play/1022411/Massive-Crowd-on-Assassin-s there is also video on Youtube, but it is much less detailed.

About my problems:
I have somewhat working NPCs, but the level of scripts skyrocketed to  unmaintainable,
and for last 2 months I try to grasp manageable paradigm, but I seem to miss a lot.

In each character I have the following things:

**Visuals** - looks, so the code which copes with actual graphics (models, etc.).
**Controls** - the low-level part of how character moves and some character animation tweaks
(like walk step sync with motion speed). Also some state machinery stuff which is close to controls.
**AI** - the behavior logic with state machinery.

This looks not very good as some parts are here and there with hacks here and there. Also it is very slow,
really struggling around 60fps on i7.
From Volition videos (usually some random devs chit-chat) I've learned that it is usually done differently,
so AI is priority-queued. So I want that so close characters have higher priority and react faster than distant ones. But this doesn't fit into model I have. Also the above presentation lead me to idea that I need several types of AI which should be switcheable on runtime.
In addition I need to add AI-LODS and physics-LODS and animation-LODs to save on distant characters.
Doing all of the above requires me to completely rewrite logic, especially object model. As I'm prototyping I use AngelScript for that. Any ideas how can I organize my object model so I have enough flexibility to extend farther?
Any suggestions on where to go and what to read?

-------------------------

slapin | 2017-03-05 13:14:17 UTC | #2

Well, I found that to make things extremely better I just need to implement Behavior Trees.
This flexible construct makes things much easier to understand and extend.

-------------------------

