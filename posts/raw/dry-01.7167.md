Modanung | 2022-01-29 10:14:41 UTC | #1

I'm not sure if that's a version number, but you can find it here:

https://gitlab.com/luckeyproductions/dry

Too many changes to mention, not enough to get excited - or worked up - about.
*Unless you need Lua or Direct3D,* then you're out of luck, as they say.

Chat's on Matrix!

https://matrix.to/#/#dry:matrix.org

Mainly:

1. Shorter engine macros and namespace names, free of numbers
1. Consistent `IsNull()`/`IsEmpty()` method names
1. More `IntVector2`-friendly UI
1. Quadratic approximation of sines and cosines
1. Harmonics and polynomial classes
1. Dice rolls

-------------------------

1vanK | 2022-01-29 07:25:54 UTC | #2

Oh, githlab already unbanned you for stealing?

-------------------------

Modanung | 2022-01-29 07:44:18 UTC | #3

Clarification:
I changed `Urho3D Project` to `LucKey Productions`, without removing anyone from the list of contributors. This was a reason for @Eugene to file a DMCA request. The issue has been resolved.

Apparently it made the news.

-------------------------

1vanK | 2022-01-29 07:55:53 UTC | #4

> I changed `Urho3D Project` to `LucKey Productions`

It sounded like you just changed the name of the project. But it was a little different, wasn't it?

-------------------------

Modanung | 2022-01-29 07:59:26 UTC | #5

I hope this line from Urho3D's _contribution checklist_ will make you see this nonissue for what it is:
> Note here that "Urho3D project" is not an actual legal entity, but just shorthand to avoid listing all the contributors.

Could you please stop hijacking my thread with what are effectively baseless smears?

-------------------------

1vanK | 2022-01-29 08:00:42 UTC | #6

[quote="Modanung, post:5, topic:7167"]
Could you please stop hijacking my thread with what are effectively baseless smears?
[/quote]

Firstly, your topic is offtopic for this forum. Second, what exactly is "baseless smears"?

-------------------------

Eugene | 2022-01-29 08:14:48 UTC | #7

[quote="1vanK, post:4, topic:7167"]
But it was a little different, wasn’t it?
[/quote]
The original issue was caused by a direct violation of MIT license by Dry, which I found unethical and asked to fix.
Now this issue is fixed. I don't really see what's there to discuss anymore.

[quote="1vanK, post:6, topic:7167"]
Firstly, your topic is offtopic for this forum
[/quote]

This forum is about Urho and all the things made with Urho. Forks are made with Urho as well. We had Atomic thread, we had iogram thread, we had rbfx-related threads, now we have Dry thread. Why not?..

-------------------------

1vanK | 2022-01-29 08:15:51 UTC | #8

We just have a very tolerant forum. Everything for the community

-------------------------

Modanung | 2022-01-29 08:27:48 UTC | #9

[quote="Eugene, post:7, topic:7167"]
The original issue was caused by a direct violation of MIT license by Dry, which I found unethical and asked to fix.
[/quote]

Which did not differ in any way from my description of it. Only in perceived intent, it seems, and/or the ignorance of the line I referred to earlier from the _contribution checklist_.
But I may be misinterpreting that. I'm fine with a two-liner if that makes you happy.

Actually, it was an easier *replace all* at the time; not an attempt at stealing credit. I wanted to make it a two-liner and failed. Basically hadn't gotten to it yet.

-------------------------

1vanK | 2022-01-29 08:40:29 UTC | #10

[quote="Eugene, post:7, topic:7167"]
This forum is about Urho and all the things made with Urho. Forks are made with Urho as well. We had Atomic thread, we had iogram thread, we had rbfx-related threads, now we have Dry thread. Why not?..
[/quote]

I'll just leave it here  
![1|690x227](upload://cebaQKeAOdmSkbOtU5peQJnt8WB.png)

-------------------------

Modanung | 2022-01-29 08:48:59 UTC | #11

I provided a link to a chatroom. Should I post it again? Or would that be spam?

Also, you're pulling another statement out of context again.

-------------------------

GoldenThumbs | 2022-01-29 08:49:04 UTC | #12

What are "dice rolls" in the context of a game engine?

-------------------------

Modanung | 2022-01-29 13:48:34 UTC | #13

In `Mathdefs.h`:
```
/// Return the result of a dice roll.
inline int DiceRoll(int dice, int sides = 6)
{
    if (sides == 0 || dice == 0)
        return 0;
    else if (sides == 1)
        return dice;

    int diceSign{ Sign(dice) };
    dice = Abs(dice);
    sides = Max(0, sides);
    int result{ 0 };

    for (int i{ 0 }; i < dice; ++i)
        result += Random(1, sides + 1);;

    return result * diceSign;
}
```

Ever played an RPG? :)
There's a less-than-slight chance at least one of them used dice rolls instead of just `rand()`.

-------------------------

Eugene | 2022-01-29 08:55:10 UTC | #14

[quote="Modanung, post:9, topic:7167"]
Actually, it was an easier *replace all* at the time; not an attempt at stealing credit. I wanted to make it a two-liner and failed. Basically hadn’t gotten to it yet.
[/quote]
I don't think and I never thought that you wanted to actually steal the credit. Never used the word "steal" too.
I am looking at it from different angle.

The people who contribute to MIT project already surrender almost all their rights.
They retain only one right: to keep their copyright intact. They contributed their code using their own name, or alias, or legal name, or some generic banner. And they know that no matter what happens with the code, their name, or alias, or legal name, or banner, will stay as they put it.

Imagine that I have a copyright in my project:
`// Copyright (c) 1994-2022 Eugene Kozlov.`
And someone takes my code, puts my name into the list somewhere else, and changes copyright to this:
`// Copyright (c) 1994-2022 third party.`
It wouldn't be ethical, right? That's why MIT doesn't allow removing copyrights, no matter what exactly is put after (c).

PS: Also, if you replace copyrights, it would be impossible to tell which files come from original project and which files were created in scope of the derived project without Git history and deep investigation.

-------------------------

Modanung | 2022-01-29 08:56:33 UTC | #15

You have a point which I'm not trying to dispute.

-------------------------

Modanung | 2022-01-29 08:59:33 UTC | #16

In Roguelikes it would be notated as - for instance - `2d6`: Equivalent to `DiceRoll(2, 6)`

-------------------------

GoldenThumbs | 2022-01-29 09:00:22 UTC | #17

Seems kind of useless if you were to make anything outside of an rpg that relies on dice rolls. Also, why are you still using SDL? That lib is kind of overkill when you only target one platform with one graphics API.

-------------------------

Modanung | 2022-01-29 09:06:57 UTC | #18

Yes, I don't expect to use dice rolls much either. I just thought it made a nice anticlimactic punchline.
...and it seemed like a game engine had to have it.

[quote="GoldenThumbs, post:17, topic:7167"]
Also, why are you still using SDL? That lib is kind of overkill when you only target one platform with one graphics API.
[/quote]

Noted. I have different priorities, but if you're up for it... :slight_smile:

-------------------------

1vanK | 2022-01-29 09:07:12 UTC | #19

Let's not be too strict. Modanung violated the license by accident, out of ignorance. And no one warned him: https://discourse.urho3d.io/t/best-fork-to-start-learning-with/6848/6?u=1vank

-------------------------

Modanung | 2022-01-29 09:48:02 UTC | #20

Great idea; dragging that heated discussion in here like some history book.
But thanks for setting the same atmosphere to go with it.

-------------------------

Modanung | 2022-01-29 09:09:44 UTC | #21

It wasn't an accident: I was n00b. And lazy, like you:

https://discourse.urho3d.io/t/removing-lua-bindings/7149/55

-------------------------

GoldenThumbs | 2022-01-29 09:10:24 UTC | #22

I'm on Windows. I guess you could say I'm "out of luck", heh.

-------------------------

Modanung | 2022-01-29 09:10:56 UTC | #23

Windows supports OpenGL. What's the problem?

-------------------------

GoldenThumbs | 2022-01-29 09:11:28 UTC | #24

I thought you removed Windows support in general? I thought I read that in your repo somewhere.

-------------------------

1vanK | 2022-01-29 09:12:00 UTC | #25

[quote="Modanung, post:20, topic:7167, full:true"]
Great idea; dragging that heated discussion in here like some history book.
[/quote]

I'm just trying to support you

-------------------------

Modanung | 2022-01-29 09:14:24 UTC | #26

No, just Direct3D. Although I'm not _testing_ for Windows.

So would that be a reason to keep SDL? Or still overkill?

-------------------------

GoldenThumbs | 2022-01-29 09:15:04 UTC | #27

I don't think so. There are OpenGL specific windowing libraries that are also cross platform (GLFW for instance). It's probably not worth the effort to remove it though.

-------------------------

Modanung | 2022-01-29 09:15:39 UTC | #28

Well, I'm no pipeline wizard, and it works for me. But that doesn't mean it should stay like it is.

-------------------------

GoldenThumbs | 2022-01-29 09:20:03 UTC | #29

Well, neither am I. I just thought you only wished to support Linux, so SDL seemed like a fairly large lib for that scope. It *could* wind up being worth it to replace SDL with GLFW (or something similar) but I doubt it. End user of engine doesn't mess with the windowing lib directly so it probably doesn't make any difference in the end.

-------------------------

Modanung | 2022-01-29 09:53:45 UTC | #30

If I had to specify one, I'd say _more tools_ is my main priority for the engine.

Working on a particle system which overlaps with (also new) audio synthesis components as well.

-------------------------

Modanung | 2022-01-29 10:56:15 UTC | #31

The name may sound like a bit of a rip-off from the Cry Engine. But - dry your eyes - the way I got to it was more driven by a set of interlingual puns: A bit of Dry humor, if you like.
Dry is a homophone of both Dutch _draai_ - which means to spin/turn or to run (a machine or program) - and German _drei_, meaning 3. Furthermore _dry_ is Old English for wizard/sorcerer (pronounced more like _druid_), and of course there's just something about things "running dry".

[spoiler]How many times did *you* hear someone say *"it uses your ho"* instead of *Urho*?[/spoiler]

-------------------------

Modanung | 2022-01-29 11:09:43 UTC | #32

Dice rolls _do_ give you a unique distribution of integers which sometimes simply might be preferable:

https://i.stack.imgur.com/DNhaf.png

With [more dice](https://qph.fs.quoracdn.net/main-qimg-583e2e40b3efcec586aded53c167255e) it approaches a normal distribution.

-------------------------

1vanK | 2022-01-29 14:06:28 UTC | #33



-------------------------

