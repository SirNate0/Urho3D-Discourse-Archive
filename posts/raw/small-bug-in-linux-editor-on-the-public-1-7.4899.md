Leith | 2019-02-06 05:44:21 UTC | #1

Today I decided that I can't work with the broken editor on the master branch on Linux, and rebuilt the public 1.7 version, which appears stable. When loading my current project scene from XML into the editor, I immediately noticed something weird - the camera aspect ratio was completely awful - I mean in the editor, not the game camera / preview. Everything was skewed, like stretching out from the middle of the window. I had the window expanded to my desktop resolution, and it looked awful, so I tried reducing the window size, and this fixed the problem, until I played with the zoom factor (mouse wheel). Zoom does not play well with aspect ratio. Still a lot more usable for me than the head branch version, just wanted to bring it up incase there is a known solution, and wondered if it affects other platforms.

-------------------------

Modanung | 2019-02-06 10:06:36 UTC | #2

Cannot reproduce; works fine on my (Linux) machine.

-------------------------

Leith | 2019-02-06 10:09:58 UTC | #3

play with scroll wheel, see if the aspect ratio goes haywire
I can live with it, but its looks wrong
at least the editor isnt crashing on the old build, so we can get some eyes on whats changed

-------------------------

Modanung | 2019-02-06 10:09:57 UTC | #4

[quote="Leith, post:3, topic:4899"]
play with scroll wheel, see if the aspect ratio goes haywire
[/quote]

Nothing of that nature. Could you be more specific and maybe provide an image or video?

-------------------------

Leith | 2019-02-06 10:13:32 UTC | #5

k, but im done for now, tomorrow ok? i will drop a couple of screen shots and show what i see here
my eyeballs are hanging out, courtesy of that nameless fruit company, wearing glasses is letting me see, but gives me headaches
It's odd that I could stare at oldschool screens, absorbing all that beta radiation for all these years for hours on end, but just a few months of staring at a screen for the fruit company stole my eyesight

-------------------------

Modanung | 2019-02-06 10:18:15 UTC | #6

My eyes are a big fan of `redshift-gtk`, makes you sleep better too.

-------------------------

Leith | 2019-02-06 10:19:56 UTC | #7

I have it built into my dualscreens, but it doesnt stop my nightmares or make me sleep well

-------------------------

Modanung | 2019-02-07 20:36:04 UTC | #8

[details=Nightmare remedies you could try:]
* Lucid dreaming (facing the monsters)
* Cannabis (less dreams)
* Meditation (serenity training)
[/details]

-------------------------

Leith | 2019-02-06 10:47:31 UTC | #9

In all seriousness, I suffer from PTSD, a dog bit off and swallowed most of my top lip - I spent a month with my lips sewn together, while the lower lip was used as a donor to replace the top one, now I have scars on my face, which I try to ignore in public settings
The nightmares about having my face eaten still happen

-------------------------

lezak | 2019-02-06 13:06:40 UTC | #11

Back to Your problem, I don't think it's a bug. There have been some improvements in editor controls after 1.7 was released and before that zoom was handled by changing camera FOV or something like that. If I remember correctly it can be changed in editor settings or preferences, look for something like move/change camera position on mouse wheel, it should make camera behave similar to current state.

-------------------------

Leith | 2019-02-08 04:35:50 UTC | #13

Unfortunately, I can't use any recent editor builds on Linux (app is highly unstable) - I'm stuck with the 1.7 editor for now, though I've had no problem using it with assets from the development head branch.

-------------------------

