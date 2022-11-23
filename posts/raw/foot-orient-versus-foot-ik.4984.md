Leith | 2019-03-02 03:10:22 UTC | #1

[quote]
asking for help on the foot orient issue - I can turn off JOINT_ROTATIONS and the feet orient correctly, but theres distortion at the knees. If I turn it on the knees are good, but now the feet are always pointing in the same worldspace direction... if the character turns 180 degrees to face you, his feet will point backwards and his legs are munted all the way to the hips, the torso is twisted, the ik chains are not being solved in character space
[/quote]

-------------------------

Modanung | 2019-03-02 09:45:28 UTC | #2

Are you aware of these functions?

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Node.h#L488-L499

-------------------------

Leith | 2019-03-02 11:52:31 UTC | #3

yeah man, I am well aware of spatial shit, thanks though, i appreciate any efforts
I coded seven axes for the car companies, not two, not three, seven, for articulated robots

-------------------------

Leith | 2019-03-02 11:47:53 UTC | #4

apparently the ik solver is not so aware, it ignores its parent transform and solves in world space
for the sample, that works, because we dont ever rotate the sample character in that worldspace, so we never noticed this issue - man please dont ask me to post video, its embarrassing for us both

-------------------------

Modanung | 2019-03-02 12:01:50 UTC | #5

I know about your expertise with programming specialized hardware and dealing with spatial orientation stacks. This doesn't mean Urho works the same. It could even make _you_ have certain expectations or habits that simply not apply in this new environment.  

It can also mean you know better. But I think you're well aware of that option. ;)

-------------------------

Leith | 2019-03-02 12:13:55 UTC | #6

I've just spent three days on this, its not good-i can fix it
Man I have two options - figure it out myself because i get almost no help here, or make an urho fixes website in the morning, and let my dad run it - seriously, im easier to get along with

-------------------------

Leith | 2019-03-02 12:37:37 UTC | #7

tomorrow i will set up independent branch, and a hail fuck u, so long dickheads, and thanks for all the fish - dad wanted a new chat site, but its going to become a new home for the urho who still believe. You are mostly useless, not even familiar with the source, see you around

-------------------------

Modanung | 2019-03-02 12:51:20 UTC | #8

[quote="Leith, post:7, topic:4984"]
You are mostly useless, not even familiar with the source, see you around
[/quote]

Don't blame life-support for not taking you anywhere. I hope to see you return when you're feeling useful.

-------------------------

Leith | 2019-03-02 12:52:44 UTC | #9

dude, I solved it without you, and you are about as useful as tits on a bull, so thanks for chiming in, on this one.

-------------------------

Modanung | 2019-03-02 12:55:47 UTC | #10

I guess you're having a bad day. Maybe take a walk?

-------------------------

Leith | 2019-03-02 12:57:36 UTC | #11

im having a bad week, but your certainly were not part of my healing process, still calling you a friend, but not there for me when I needed u

-------------------------

Leith | 2019-03-02 13:00:48 UTC | #12

i still love u man, im not writing you off yet, it would be nice if you gave me the same k

-------------------------

Modanung | 2019-03-02 13:02:37 UTC | #13

Digital social contact is a strained reduction of what most people need on a regular basis. One cannot expect the same of it, only hope that others too are doing their best given _their_ circumstances.

If you'd like to chat, add me on [Wire](https://wire.com/en/download/).

-------------------------

Leith | 2019-03-02 13:07:30 UTC | #14

no, i wont add you on wire, i dont even know what it is or care
sorry, just no
tomorrow i write a replacement for mplayer and paltalk

-------------------------

Modanung | 2019-03-02 13:08:58 UTC | #15

Not before I save the world! ;P

-------------------------

Leith | 2019-03-02 13:09:41 UTC | #16

you need to beat me to it, tomorrow i save the world

-------------------------

Modanung | 2019-03-02 13:10:11 UTC | #17

Seems like a healthy competition to have.

-------------------------

weitjong | 2019-03-02 13:10:31 UTC | #18



-------------------------

