TikariSakari | 2017-01-02 01:07:17 UTC | #1

Is there any kind of splash screen around for Urho3D? Something like Powered by: Urho3D with the fish picture?

-------------------------

cadaver | 2017-01-02 01:07:17 UTC | #2

Not one that specifically says "powered by", but the fish + Urho3D text in bin/Data/Textures/LogoLarge.png is closest we have to an official splash screen.

There are also bigger variants at:
[urho3d.github.io/assets/images/logo-big.jpg](http://urho3d.github.io/assets/images/logo-big.jpg)
[urho3d.github.io/assets/images/logo-big-bw.png](http://urho3d.github.io/assets/images/logo-big-bw.png)

-------------------------

Modanung | 2017-01-02 01:07:43 UTC | #3

I started working on a [url=http://luckeyproductions.nl/urho.html]3D Urho[/url] today. I intend to add more detail as well as a rig.
[url=http://luckeyproductions.nl/urho.blend][Blend][/url]

[size=85]NB: Blend4Web (used for the first linked-to file) doesn't seem to export bone constraints correctly.[/size]

-------------------------

TikariSakari | 2017-01-02 01:07:44 UTC | #4

That one looks really awesome

-------------------------

cadaver | 2017-01-02 01:07:44 UTC | #5

Very nice! I understand this to aim for a fairly low-tech aesthetic in which case the amount of vertices doesn't bother me.

-------------------------

Modanung | 2017-01-02 01:07:45 UTC | #6

Glad you like it. :smiley: All files are now updated with a quick and dirty (automatic weights) swim animation.
The [url=https://github.com/LucKeyProductions/Urho3DQtemplate]Urho3DQtemplate[/url] now features Urho swimming around.

-------------------------

Bananaft | 2017-01-02 01:07:46 UTC | #7

Very nice model. Nothing creepy for me. And yes, you could throw a bit more polys on the eyes, as it is the most important part of any character. Also, don't forget the false eye:
[img]http://i.imgur.com/nBlDLon.png[/img]

-------------------------

Modanung | 2017-01-02 01:07:46 UTC | #8

I won't forget the false eye: It's too awesome. So far the model is only coloured using vertex colors. I doubled the number of vertices in the eyes. Diffuse, specular and normal textures will add the rest of the detail.

-------------------------

urnenfeld | 2020-12-10 22:40:57 UTC | #9

Hello, Sorry bumping this old topic.

Has anyone yet ever done/used one? I think we need something more than just the logo, as proposed. Many people might not know that that logo is the engine that has been used to create the game... so I see important the **powered by** factor

So I would like to have one included in my game. I could create one, but I am not any kind of artist, so it would end up being unique and not used among others, therefore failing in its purpose.

Is there any interest in having an official one? 

I think just adding some text right bottom of the logo would be enough... but the most importand is that it must have some kind of standard status...

-------------------------

Modanung | 2020-12-10 20:17:16 UTC | #10

The [SVG](https://libregamewiki.org/images/f/fa/Urho3D.svg) can be exported to any size. There's also the [3D fish](https://opengameart.org/content/urho), but it may not be enough to make a splash. Having both _standard status_ and _uniqueness_ seem somewhat contradictory properties, btw.

-------------------------

urnenfeld | 2020-12-10 22:44:39 UTC | #11

[quote="Modanung, post:10, topic:1375"]
Having both *standard status* and *uniqueness* seem somewhat contradictory properties
[/quote]

Yep, I meant *unique* as for one for everybody, edited the reply to avoid confusion.

Is clear we have a logo, but not a way to spread the ***"Made with Urho3d engine"*** message

-------------------------

Modanung | 2020-12-11 09:59:59 UTC | #12

[quote="urnenfeld, post:11, topic:1375"]
Is clear we have a logo, but not a way to spread the ***"Made with Urho3d engine"*** message
[/quote]

Good luck finding a willing artist. Or a programmer able to appreciate the efforts of one, for that matter.

-------------------------

urnenfeld | 2020-12-13 14:22:06 UTC | #13

[quote="urnenfeld, post:9, topic:1375"]
I could create one, but I am not any kind of artist
[/quote]

Any artistic recommendation welcome:

https://github.com/urnenfeld/urho3d-splash-madewith

-------------------------

Modanung | 2020-12-13 15:09:04 UTC | #14

Background:
https://gitlab.com/Modanung/FlappyUrho
Lighting:
https://gitlab.com/luckeyproductions/games/AmazingUrho

You could make Urho swim through the logo (billboard with normal map) after fading in, add a little seafloor, weeds and [bubbles](https://gitlab.com/luckeyproductions/games/heXon/-/blob/master/Resources/Particles/TailBubbles.xml).

-------------------------

