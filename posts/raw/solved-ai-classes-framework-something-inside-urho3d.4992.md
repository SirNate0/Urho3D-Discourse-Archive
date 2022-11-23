urnenfeld | 2019-03-04 16:59:13 UTC | #1

Hello,

I almost have the logics/physics skeleton of my game in place:

![Screenshot_20190228_154051|643x500,50%](upload://4apZanHyUiC8hMsbhybSv0AOPOv.png) 
(the absence of any artistic skills are evident)

But as it is a 2 players game... To start playing myself, either I start planning how is going to be playing in network or I need to think about an AI for the game.

So I have decided going for the second for now.

**Something in our engine that I have missed that would help in the design of the AI?**

-------------------------

Modanung | 2019-03-02 17:38:03 UTC | #2

What AIs - or maybe rather AP[spoiler]layer[/spoiler]s - need to be capable of greatly depends on the game at hand. In short I think it generally (when dealing with opponents) comes down to writing functions that calculate the meaning of winning after which you find places to inject seemingly human-like error to keep your game fun to play. :slight_smile:
In case of a paddle game you could simply calculate a target position and have the AP move his paddle in that direction. If this calculation is accurate it may become unbeatable, so you could add something akin to a visual-spatial disability to the calculation that increases with the speed of the ball. You could maybe even add some virtual eye and have its position and angle relative to the ball effect the errors as based on your own experience playing the game.

-------------------------

Leith | 2019-03-04 08:12:04 UTC | #3

It's not a lot of work to knock up a basic BehaviourTree or even a simple FSM to deal with AI behaviours - purely functional solutions quickly get out of hand with all the conditional logic.
Whether or not Urho should provide these things is another question - currently I'm still working with functional control logic for my AI, even though there is a FSM for gamestates (intro, menu, gameplay, etc.)

-------------------------

urnenfeld | 2019-03-04 16:58:59 UTC | #4

Yep there is something already in place, I implemented a grid representing the wall where each elements represent the danger on the staying there, yet it is only needed to avoid them.

The fact is in some cases, that the simplest AI algorithm could make your game unbeateable, but if you don't polish your algorithm enough then remains beateable, and you get were you wanted :slight_smile:

-------------------------

Leith | 2019-03-11 04:01:23 UTC | #5

Its true - example? when an AI aims a gun at your player and shoots a bullet at you, we add some randomness to the direction vector, so that the AI can "miss"... we tweak the random factor (or range) to determine how accurate the AI will be, and in turn, how difficult the gameplay is.

-------------------------

Modanung | 2019-03-11 06:10:43 UTC | #6

Note that [normal distributions](https://en.wikipedia.org/wiki/Normal_distribution) make for more human-like error than ordinary random numbers.

-------------------------

Leith | 2019-03-11 06:23:26 UTC | #7

I wrote a white paper on random number distributions, doubt its easily available, but a good random seed always helps

-------------------------

weitjong | 2019-03-11 06:39:37 UTC | #8

An extraordinary claim requires an extraordinary evidence.

-------------------------

Leith | 2019-03-11 06:50:58 UTC | #9

would you like to look at my old super random on asmcommunity, or something more recent? I blended park-miller with mersenne twister B, it works lovely, and is deterministic based on the seed
The combination of these algos gave me a far superior numerical distribution in the keyrange, which I plotted and evaluated ;)

-------------------------

