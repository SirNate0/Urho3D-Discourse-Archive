Miegamicis | 2019-01-31 11:42:24 UTC | #1

Does the engine support multiple sound listeners at once? I think I already know the answer but maybe there is a reason why there isn't such support for it at the moment. The problem is with the splitscreen local multiplayer, since there could be only 1 sound listener, sounds will be generated only for one player and the rest of them will be playing in the "quiet" mode.

-------------------------

Leith | 2019-02-01 03:28:17 UTC | #2

Currently the Audio class only supports one SoundListener.

[code]void Audio::SetListener(SoundListener* listener)
{
    listener_ = listener;
}[/code]

You should only require one sound listener, as there is no association between players and the audio system - simply put, the soundlistener is not owned by any player, it is owned by the application, and so can play any sound sources, regardless of 'who made the sound happen'.

-------------------------

Dave82 | 2019-02-01 07:34:36 UTC | #3

Well i don't think the problem could be solved by more than one sound listeners. Just imagine a scenario of an explosion sound and two players. How would you handle the 3d sound if you have two listeners but your hardware has only ONE output (speakers) ? Some games achieve this by using the adventages of the stereo output and simply split the audio into L and R. But to be honest i don't think there is any simple solution for this.
I would simply avoid using 3d sounds altogether in a split screen game...

-------------------------

Miegamicis | 2019-02-01 07:36:20 UTC | #4

Thanks for the explanation. That makes a lot of sense. Will try to avoid using 3D sounds altogether in my splitscreen project.

-------------------------

Leith | 2019-02-01 11:02:01 UTC | #6

one 3d listener, the computer, can hear sounds from both players

-------------------------

Leith | 2019-02-01 11:03:05 UTC | #7

please do not avoid 3d sound, its super easy and works in your bubble

-------------------------

Dave82 | 2019-02-01 11:33:20 UTC | #8

It can't... A listener is attached to a player (or camera) and the gain is calculated from a distance between a listener (player) and a sound source. It is impossble to hear the same sound from two different positions if you have only one speaker.
How would you play an explosion sound if one player stands closer and the other is far away ?

-------------------------

Leith | 2019-02-01 11:50:02 UTC | #9

there are always ways to cheat the system, in this example, we could feed two sound streams into a mixer under sdl2 audio

-------------------------

Leith | 2019-02-01 11:55:57 UTC | #10

most things worth doing are not easy, but thats what makes them interesting

-------------------------

Leith | 2019-02-01 11:58:15 UTC | #11

nothing i know of, is impossible, except theoretical shit that doesnt fly yet

-------------------------

Dave82 | 2019-02-01 12:01:03 UTC | #12

Yes there are some workarounds. The same issue is mentioned here : 
https://answers.unity.com/questions/1030856/in-a-split-screen-game-how-to-deliver-different-3d.html

[quote]we could feed two sound streams into a mixer under sdl2 audio"[/quote]
But wouldn't that mean playing the same sound twice ? I don't see a point of doing this.

-------------------------

Leith | 2019-02-01 12:01:59 UTC | #13

no, it means the same audio inputs are mixed, into a final output hardware buffer player to the speaker(s)

-------------------------

Leith | 2019-02-01 12:02:51 UTC | #14

we're able to mix sounds before we play it

-------------------------

Leith | 2019-02-01 12:03:32 UTC | #15

think like a DJ, with a mixing bench

-------------------------

Miegamicis | 2019-02-01 12:36:02 UTC | #16

What about using multiple sound listeners but only use the nearest listener to the sound source to calculate the volume of the actual sound + disabling the stereo effect?

-------------------------

Leith | 2019-02-01 22:49:03 UTC | #17

When you're working with 3D sound sources, you don't need stereo sounds - all your 3D sounds should be mono! As for switching between Listeners, what's the difference between that, and just moving the one Listener on demand?

-------------------------

I3DB | 2019-02-02 15:40:52 UTC | #18

[Progression of legacy 3D into spatial sound](https://docs.microsoft.com/en-us/windows/mixed-reality/spatial-sound) ...

-------------------------

Leith | 2019-02-02 15:52:14 UTC | #19

Pretty sure I have 3D sound worked out, been doing this stuff for a while.
A 3D sound source comes from a place, so we don't need two channels of audio information, we just need a mono sound, coming from some 3D place.

2D sounds on the other hand, like background music, can and should be stereo.

The implication is that 3D sounds exist in a virtual 3D space, while the more boring 2D sounds exist in the application space. It is fairly easy to make decisions about which space sounds should live in.

-------------------------

