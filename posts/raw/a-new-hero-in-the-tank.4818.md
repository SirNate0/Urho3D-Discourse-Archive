Leith | 2019-01-14 08:50:38 UTC | #1

Hey guys, my name is Leith, I am a 43 year old coder who started as a kid, on low end platforms, and grew with the technology. By nine I was coding in machinecode, and by 14 I had owned my first network. I was a bad boy, with no rules. Things have changed a lot since then.

I spent a decade or so as admin on asmcommunity.net where I wrote under the pseudonym of Homer, mainly about games and physics.

At 19, I decided I needed a proper job, and went into precision metal.

I was a robotics programmer for the auto industry at large. I learned lots of funky math for transform hierarchies.
When the auto industry went into decline, I switched to video games.

After some more years, and frustration, I have my bachelor of games and virtual worlds degree.

I spent many years to attain qualifications that should have been handed to me.
Some years wasted on other game engines, but mostly wasted in engine dev.

Now I am here to make things better.
I hope to bring some positivity to this engine!

-------------------------

Modanung | 2019-01-14 10:51:55 UTC | #2

A glorious welcome to you, Leith! :confetti_ball: :smile:  

That's a nice set of credentials you got there. Your arrival is sure to bring hope to those familiar with Urho's stagnant development. You seem to know the ropes, but can you handle loose ends? :wink:

Try not to feel too much pressure, though. I think the community has gotten used to the little progress by now and would rather see developers stick around than exhaust themselves.

Bon appétit!

-------------------------

Kronix | 2019-01-14 17:57:23 UTC | #3

Just curious, what was your first computer and language?

-------------------------

Leith | 2019-01-19 05:46:11 UTC | #4

The first computer I owned was an Apple 2C. It was a GreenScreen.
I demanded to own that machine, based on the 3D (wireframe) tanks demo, the first ever 3D vector graphic demo, as far as I am aware. The machine was terrible to use and terrible to code for.

But the first computers I programmed included the VIC-20, TRS-80 and BBC Microbee (later Archimedes, C64, Amiga, and so on)

My first programming languages were native BASIC (although the VIC had none), rapidly followed by 8-bit machinecode (basically, 8-bit asm, written using a memory monitor, no assembler)

-------------------------

Leith | 2019-01-15 05:34:57 UTC | #5

I'll try to take my time, but I am something of a machine - I tend toward obsessive compulsive, and find it hard to stop doing what I love. Although I have a lot to learn, I already know a lot, and therefore the learn curve should be fairly flat. Still, I will probably ask some questions that may be considered as stupid (I believe that no question is stupid)

-------------------------

Modanung | 2019-01-15 08:17:58 UTC | #6

[quote="Leith, post:5, topic:4818"]
I am something of a machine
[/quote]

In that case steam ahead and let me know if you need some oil. ;P

-------------------------

dertom | 2019-01-15 14:14:38 UTC | #7

@Leith Welcome, hero. Make things better ;)

EDIT: TI99/4A,C64

-------------------------

johnnycable | 2019-01-15 13:28:11 UTC | #8

ZX81 and C64. Still have the red book for machine code.
Welcome

-------------------------

cadaver | 2019-01-15 15:41:31 UTC | #9

Good luck Leith!

My advice: due to realities of manpower, the engine can never be everything to everyone. Therefore, don't be afraid to be selfish. Work on your own goals / features you need the most. 

And if you come across something that impedes development (remember that the engine has a long history, all the way to DX9 / SM2) don't be afraid to suggest just ripping it away.

In my view, those who do the actual work have the final say.

Despite the legacy-ness, the good side of Urho is that the community is small and there's no hype really, so the engine doesn't have to bother with PR bullshit or trying to appear to be more than it is ... just make it work for you and those immediately around you.

-------------------------

Leith | 2019-01-19 05:41:56 UTC | #10

Thank you all for your kind welcome!

I am currently still in my first week of getting-to-know-you, both the codebase, and the people.
So far, the learn curve is fairly easy (given my background?) although there are still some curveballs.

I'm trying not to bother you guys too much, though I will certainly issue PR for anything that I think could help the community at large.

Please be patient with me while I find my sea legs on this ship!

-------------------------

bvanevery | 2019-01-21 16:56:41 UTC | #11

What a life journey.  Myself, a DEC Alpha assembly coder that didn't adapt well to change.  I've monitored Urho3D for a few years, haven't committed to it.

The best thing anyone could contribute at this point, would be the perception that the project has a direction.  Without visible stewards, the value proposition is endeavoring to understand the entire codebase oneself, and then determining whether one can completely maintain and improve the codebase oneself.  On the reasonable mid-term assumption that no one else will do so.

I know from previous experience that Weitjong will be doing an excellent job maintaining the CMake build system, but of course there's more to the engine than that.

-------------------------

Leith | 2019-01-22 04:42:10 UTC | #12

What I have learned so far, is that it is quite difficult to learn this engine in a vacuum, and that the samples alone are not enough to fill that void.

For things like physics and networking, you're expected to already be familiar with the underlying systems.
Documentation needs some love, including some annotation of headers, since we tend to rely on a mix of very old handwritten docs, and doxygen-generated stuff.

For anything specific, your best bet is this forum, as chances are good that your questions can and will be answered rapidly :slight_smile:

I've issued my first Pull Request, which is in regard to ordered network replication of node hierarchies.
But I'm still finding my way around, and asking lots of questions.

-------------------------

Leith | 2019-04-08 08:54:34 UTC | #13

After a few months on this ship, I found my sea legs, the codebase is mostly good... and can be improved, where we can show use-cases that fail due to Urho. I've found very few.
I did notice some redundant stuff in the engine source, I may notice it again when I remove the extra debug stuff I added recently

-------------------------

