evolgames | 2020-09-17 20:13:51 UTC | #1

TL;DR: Who is doing multiplayer and what did you use for a solution? Has anyone actually used the implementation of p2p from the replication sample? Are there any thirdparty solutions that save the headaches? I don't even care about having a dedicated server. I just want a way for friends to connect and host (even if they have to tell each other their ip over the phone or something). Is there a viable commercial solution to make this work better?

Farthest I got using the sample was:
Client Connected
and then immediately after: Client Disconnected
etc
(with a bunch of tries before failing totally)
This is based off the Sample with the ball thing running a server with digital ocean.

If I just do two pcs, seperate networks, and I run an unmodified SceneReplication sample, it just won't ever connect. I know there is a p2p multiplayer helper project by Arnis which I'm grateful for but unfortunately the setup is way over my head. Also, I don't see why the sample method doesn't work. I've spent far too many hours messing with digital ocean trying to get two applications to connect. One person can connect, but not a second one. I've tried everything I could think of as far as opening ports and all that. I don't have networking issues with other p2p games though (alien-arena, for example just works without issues). I'm worried something about the way urho does it is the problem. No idea how to troubleshoot this.

Localhost works (running the application multiple times on the same pc always replicates and allows all clients in). I can run it multiple times and with the networking sample I'll have multiple "player" balls. Trying this with two computers on the same wifi doesnt work, though.

Is there an easy way or should I just stick to single player projects?

-------------------------

Modanung | 2020-09-17 20:35:13 UTC | #2

[quote="evolgames, post:1, topic:6395"]
I just want a way for friends to connect and host (even if they have to tell each other their ip over the phone or something)
[/quote]

For that, I think sample 17 should provide all the information you need.

-------------------------

evolgames | 2020-09-17 20:36:25 UTC | #3

I agree that it *should*. No idea why it fails to connect though. Everything in the sample makes sense, and should work but it just doesn't.
I wish there was more information with "Failed to connect."
Maybe I'm still too noob for networking

-------------------------

Miegamicis | 2020-09-18 02:28:51 UTC | #4

> Client Connected
and then immediately after: Client Disconnected

Check the logs, maybe there is some sort of scene mismatch failure which triggers the disconnect.

> If I just do two pcs, seperate networks, and I run an unmodified SceneReplication sample, it just won’t ever connect. 

That's probably because both of your computers are behind a wifi, so they are not directly exposed to the outside world. In that case there are 2 solutions:
1. Use port forwarding in your router settings
2. Use the NAT punchthrough solution which solves issues like this


I have tested the networking part of the engine quite extensively and the problems that occurred were mostly caused by server misconfiguration (firewall, port forwarding). Care to share your Digital Ocean servers address?

If you need NAT punchthrough master server, feel free to use this for testing purposes: 

address: `nat.arnis.dev`
port : `30123`

-------------------------

evolgames | 2020-09-17 21:33:18 UTC | #5

Thanks a lot for the quick and helpful response.
Okay looks like I have to tell the sample to log since no file is generated. All the console says is that the connection failed so maybe the log will say more.

Hm that's weird because I've done everything I've found online about opening ports. Maybe there is an issue with both my router and the additional one I tested on (a friend's). All networking (gigabit) in my apartment building goes through the IT room (idk why or what for), though everyone has their own router. I was under the impression that Digital Ocean would circumvent any router issues.

Ahh I deleted my droplet out of frustration a few weeks ago. Since there's other simple games working with p2p I probably will try to get things to work without DO in the future. I don't know much about NAT punchthrough but I guess that's what the other p2p games that work for me must be using then.

[quote="Miegamicis, post:4, topic:6395"]
I have tested the networking part of the engine quite extensively and the problems that occurred were mostly caused by server misconfiguration (firewall, port forwarding).
[/quote]
This is very useful. I guess if I have an issue with port forwarding on my router then that could be the reason behind this.

Cool, appreciate the testing server. I will take another careful look at your Urho3D-P2P-Multiplayer project. Maybe NAT is what I need to make this work.

Oh wow, I recently rebuilt urho via git. I didn't know there was a Sample 52_NATPunchthrough now. I'm a dummy. Looks like it wasn't in the 1.7 release that I had initially. I guess I will try this first!

-------------------------

evolgames | 2020-09-18 03:03:08 UTC | #6

Ok confirmed working for me now with the 52_NATPunchthrough sample. I connected my two pcs to your testing master server, ran one as a server and the other I connected as a client. Worked perfectly. I feel really dumb now for not knowing about this sample before. But, I'm happy it works and that it solves the issues I was having with Scene Replication and possibly restrictive connections. I have plenty to play around with now. Going to try out that docker set up in DO. And I'll spend some time learning more about this technique.

Thanks so much for all your awesome work on Urho. I'm only getting more obsessed with the engine as I learn more. It's really an amazing piece of software. Is there an Urho buy-a-dev-a-beer url?

-------------------------

Miegamicis | 2020-09-18 04:37:00 UTC | #7

Glad to hear that it worked. The 1.7 version actually contains different networking library - kNet, it was replaced with different one a while ago. The new lib has the NAT punchtrough support, that's why there was no samples for that in 1.7 release.

-------------------------

evolgames | 2020-09-18 04:58:00 UTC | #8

Ah I see. Good to know. Is there a reason 1.8 isn't [here](https://urho3d.github.io/news-categories.html#releases-ref)?
Edit: nvm I see 1.8 says alpha. Cool

-------------------------

Miegamicis | 2020-09-18 07:36:48 UTC | #9

I guess the main reason is that there are few open issues that we wanted to resolve prior 1.8.

-------------------------

coldev | 2020-09-20 14:25:55 UTC | #10

Photon network
realtime is very fast , and sdk is easy to learn,
include free forever 20 concurrent connections

https://www.photonengine.com/sdks#realtime-cpp

https://www.photonengine.com/en-US/Realtime

-------------------------

evolgames | 2020-09-20 14:58:34 UTC | #11

Interesting! I'm going to check this out too

-------------------------

Miegamicis | 2020-09-20 15:25:58 UTC | #12

Haven't checked Photon, but I'm currently experimenting with this one: https://heroiclabs.com/

Good thing is that it can be fully self hosted and by the look of it provides the same stuff that photon does.

-------------------------

Modanung | 2020-09-21 19:55:53 UTC | #13

Soon it will just be a matter of passing a few pixels around, but more about that later. :slightly_smiling_face:

-------------------------

JTippetts1 | 2020-09-21 22:05:05 UTC | #14

Ugh, my crappy rural internet connection cringes at the thought.

-------------------------

Modanung | 2020-09-23 21:44:47 UTC | #15

:dark_sunglasses: You think that's air you're receiving now?

Do you have any idea how many ASCII indixes fit into a single pixel?

[spoiler]8.5 [![](https://gitlab.com/luckeyproductions/hantik/-/raw/master/images/antiq.svg)](https://gitlab.com/luckeyproductions/hantik/-/blob/master/antiq.md)[/spoiler]

Communicate an abbreviated entity mapping and one pixel should be enough for small changes when using glyph mirroring instead of separators and octal numbers together with any leftover bits. Only one pixel could contain a property identifier, a normalized 3D vector and its scalar.

It would be nice if graphics cards had direct glass fiber lattice interfaces though.

-------------------------

JTippetts1 | 2020-09-21 22:46:44 UTC | #16

Yeah, you're talking about something entirely different than what I thought.

-------------------------

Modanung | 2020-09-22 10:29:24 UTC | #17

Yea no, not the renderbuffer-by-plane model: I mean syncing by means of mutual fairy dust and gravel.

-------------------------

Enhex | 2020-09-25 00:02:46 UTC | #18

There's also the client side prediction Urho subsystem I wrote back in the day:
https://github.com/Enhex/Urho3D-CSP

Works directly with Urho's networking so it's probably the quickest solution to integrate, but it's basic (no lag compensation) and possibly needs to be patched up to work with latest Urho version.

-------------------------

lebrewer | 2020-09-25 22:36:15 UTC | #19

Now that's actually useful. Thank you!

-------------------------

