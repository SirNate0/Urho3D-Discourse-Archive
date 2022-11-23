evolgames | 2020-11-30 00:17:08 UTC | #1

I recently tested one of my projects in Windows 10. I don't think this occurred with 7 but I got a security pop up saying that it was from an unknown publisher and potentially dangerous. I don't use windows as my daily OS. Clicking "run anyway" was fine and it ran like normal.
This isn't the first time windows (or an antivirus) gave false positives or a warning for stuff like this. Gmail will delete my email if I try to send the game zip to a friend (because it has an .exe in it).
Anyway, I don't want this security pop-up to be off-putting for users (the vast majority which are on windows).

Is there a way to "sign" the urho3dplayer.exe to at least put "Evol Games" as the publisher on this warning? (no idea where windows looks for that info)
Anyone else deal with this and figure something out as far as packaging? Do I need to do something different? Or just leave as is and promise the users it's safe? :slight_smile:

-------------------------

Modanung | 2020-11-30 00:36:03 UTC | #2

https://duckduckgo.com/?q=windows+10+unknown+publisher+fix&t=h_&ia=web

-------------------------

evolgames | 2020-11-30 00:50:34 UTC | #3

That's not issue or the point of this thread at all. I already said I have no problem running it. Most users will click run anyway and it's trivial to run it. The point is that it's not "signed" and shows up as an unknown publisher which is off-putting to users.
I don't need a workaround for the user end. I need it not to show up in the first place.

-------------------------

Modanung | 2020-11-30 01:01:38 UTC | #4

What IDE do you use?

I suspect it could be a way to motivate developers to spread M$ spyware by compiling in VS.

-------------------------

evolgames | 2020-11-30 01:02:24 UTC | #5

I don't compile. I write the scripts in lua and point the urho3dplayer to them via the commandline.text file. IDE is geany but I could just as easy use any text editor.

-------------------------

Modanung | 2020-11-30 01:03:36 UTC | #6

I don't think the pre-built player is compiled in VS either.

-------------------------

vmost | 2020-11-30 01:09:39 UTC | #7

Mac has a similar thing for downloaded executables, where third-party apps are 'soft-locked' and the only way to open them is with ctrl-click->'Open', then 'Open anyway' for the dialogue pop-up. It implies there is no easy way to get approval (at least on old OSes, which I use). Probably... only things distributed by the app store can be opened straight up. (not completely relevant I know)

-------------------------

Modanung | 2020-11-30 07:37:37 UTC | #8

[quote="vmost, post:7, topic:6583"]
(not completely relevant I know)
[/quote]

Probably similar brand-locking logic though; they crave [data](http://luckeyproductions.nl/images/PRISMslide.jpg).

-------------------------

JSandusky | 2020-11-30 20:26:23 UTC | #9

You either need to wait for MS to have received enough data (# of users) to clear your program or sign it with an EV cert.

EV certs are going to cost you, but if you sign your program with an EV cert it'll clear smart-screen (because they strongly identify you so if you do something heinous it comes back to you).

-------------------------

Modanung | 2020-11-30 07:37:33 UTC | #10

[quote="JSandusky, post:9, topic:6583"]
You either need to wait for MS to have received enough data [...]
[/quote]

And again with each update? M$ FOSS FUD [spoiler]:fu:[/spoiler]

-------------------------

evolgames | 2020-11-30 01:47:26 UTC | #11

Oh okay this is interesting. So what I take from this is after enough users have hit run anyway and MS has that data, it'll stop marking it like that.

This is curious though because how would MS distinguish between my project, which is just the Urho3DPlayer.exe running lua scripts VS. someone else's?
Or, maybe enough users running Urho programs in general I guess?
So I assume you all have similar errors?

Hm yeah, I'll do an EV cert only if I have a serious commercial product.

-------------------------

evolgames | 2020-11-30 01:51:52 UTC | #13

I should say, you all have similar errors for your users? The vast majority of my downloads are for Windows. I have data for 14,700 downloads since 2014 and it's probably 14k+ for Windows.

-------------------------

Modanung | 2020-11-30 01:56:44 UTC | #14

I don't provide binaries for Spy Systems either. I'd rather have one person try Linux than a 100 downloads.

-------------------------

evolgames | 2020-11-30 02:00:11 UTC | #15

Well to each their own

-------------------------

Modanung | 2020-11-30 02:07:08 UTC | #16

Own or be owned. :see_no_evil:

-------------------------

JSandusky | 2020-11-30 04:41:15 UTC | #17

[quote="evolgames, post:11, topic:6583"]
Oh okay this is interesting. So what I take from this is after enough users have hit run anyway and MS has that data, it’ll stop marking it like that.
[/quote]

Close enough. It's referred to as "organic reputation" if you need to google around to understand it. It's a giant confusing mess, but where they downloaded it from counts too. So if MS hypothetically gave itch.io a pass as trusted (doubt it due to no curation) *most* everything coming from there is probably going to pass.

You can use other certs to tie the reputation, otherwise the cert is against a "fingerprint" which could very well change between versions of your program, nixing your existing reputation - though it seems uncommon.

---

As long as you're not showing up as the red "malware" message. If it's the blue message that's not bad and to be expected. At the least complete **all** the metadata and sign against a generated cert to tie the reputation.

I don't think I've ever not had access to an EV to sign (if I didn't then it was something I had to tell IT to tie into the distro-script) outside of personal project junk. Of those I've never had a problem with things I write a WIX installer for with the UAC prompt being the only hoop, though others seem to have tons of problems. SmartScreen is weird.

-------------------------

throwawayerino | 2020-11-30 07:00:54 UTC | #18

Do you get the message, or your friend only? I have a little experiment: go to the exe's properties and see if it has a checkbox about it being "blocked".
And research self signing if you're looking for certs

-------------------------

evolgames | 2020-11-30 07:47:05 UTC | #19

There's no blocked properties. It's the exact same Urho3dplayer.exe that comes in the Urho1.8 release.
My win10 install also shows a warning (have to click more info and then run anyway).

-------------------------

Dave82 | 2020-12-02 15:58:32 UTC | #20

[quote="Modanung, post:12, topic:6583"]
Of course not; only a fool would use an SS instead of an OS
[/quote]

Wether you like it or not windows is the most popular OS in the world and DX is the most popular graphics API used by games. I understand your hate and delusional conspiracy theories about MS but calling 99%of developers , gamers , average users fools , is just unacceptable. Even [your poll](https://discourse.urho3d.io/t/os-poll/6461) clearly shows how popular is windows among open source developers (by which i was shocked btw i thought linux will win in a landslide...)

-------------------------

Modanung | 2020-11-30 13:01:26 UTC | #21

It is clear you are under-informed; a common trait of preoccupied proxy-cannibals. A quick glance at *history* should tell you popularity is by no means a measure of a wise "decision". Ever noticed how the SS comes preinstalled? And, where do you get this 99% from, btw? [Steam](https://spyware.neocities.org/articles/steam.html) statistics? :sheep:

> :musical_note: [It's all about the pentiums, baby](https://www.youtube.com/watch?v=qpMvS1Q1sos&disable_polymer=true) :penguin:

-------------------------

Eugene | 2020-11-30 13:27:28 UTC | #22

[quote="Modanung, post:21, topic:6583"]
And, where do you get this 99% from, btw? [Steam](https://spyware.neocities.org/articles/steam.html) statistics?
[/quote]
Well, it's the most reliable source of statistics that we have

[quote="Modanung, post:21, topic:6583"]
popularity is by no means a measure of a wise “decision”
[/quote]
If I create a game, my ultimate goal is to make it playable for the the biggest possible amount of players. If you have different goals, it's your personal choise.

-------------------------

throwawayerino | 2020-11-30 13:44:47 UTC | #23

Is the thing called "SmartScreen"? I'm not sure, but this page has directions at the bottom to submit a sample in case of false errors
https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-smartscreen/microsoft-defender-smartscreen-overview
And don't feed the troll

-------------------------

Modanung | 2020-11-30 13:52:39 UTC | #24

[quote="Eugene, post:22, topic:6583"]
Well, it’s the most reliable source of statistics that we have
[/quote]

It has the same *filter* as the SS user base: It is **spyware**, which means only the uncaring/ignorant run it.

@throwawayerino Now you're a propagandist. Congratulations. Ever read the EULA? Seen this [slide](https://luckeyproductions.nl/images/PRISMslide.jpg)?
Just truthin'. :trolleybus:

-------------------------

Modanung | 2020-11-30 14:28:23 UTC | #25

The best defense would be to start informing yourselves, and have a deep thought. :speak_no_evil:

-------------------------

Eugene | 2020-11-30 14:32:29 UTC | #26

[quote="Modanung, post:24, topic:6583"]
It has the same *filter* as the SS user base: It is **spyware** , which means only the uncaring/ignorant run it.
[/quote]
Sure, it has this filter. It doesn't change what I said. The majority of PC playerbase don't know or care about Steam being spyware. It's not like you have *better* statistics of OS use. We work with what we have. It's hard to tell, but I think at least 90% of people paying for games on PC have Steam.

Therefore, if one's untimate goal is to let people play the game, Windows support is wise decision.

If your goal is to make world clean of spyware, then you obviously shouldn't do it. But other people are not obliged to care about your goals.

-------------------------

Modanung | 2020-11-30 14:49:42 UTC | #27

[quote="Eugene, post:26, topic:6583"]
It’s not like you have *better* statistics of OS use. We work with what we have.
[/quote]

"We don't *know*" would be better when facing this level of obvious bias.

Enjoy your bugged machine.

-------------------------

Eugene | 2020-11-30 14:55:09 UTC | #28

[quote="Modanung, post:27, topic:6583"]
“We don’t *know* ” would be better when facing this level of obvious bias.
[/quote]
There are indirect ways to measure it.
E.g. compare GOG and Steam sales for the same game.

> On the big day-one releases, he says **GOG** typically sees about 15 percent the **sales** that **Steam** does

It's reliable to say that *at least* 85% of paying playerbase use Steam.
If you think these estimates are incorred, I'd like to see real data.

-------------------------

Modanung | 2020-11-30 14:59:30 UTC | #29

I thought you wanted as many people to *play* your games? Now you're comparing pay-walled releases....
of mostly spyware.

You really should give that deep thought a try some time.

-------------------------

1vanK | 2020-11-30 15:01:01 UTC | #30

Are you using your phone? Do you always go online through VPN? Do you publish information about yourself on the Internet?

-------------------------

vmost | 2020-11-30 15:08:30 UTC | #32

A support thread seems the wrong place to evangelize data-safe digital practices.

-------------------------

Modanung | 2020-11-30 15:09:24 UTC | #33

Well... it _does_ say "Windows" in the title.

-------------------------

1vanK | 2020-11-30 15:47:47 UTC | #34

[quote="Modanung, post:31, topic:6583"]
I keep wondering what brought some of you *here* ?
[/quote]

I came here because I found a good engine

-------------------------

evolgames | 2020-11-30 17:16:20 UTC | #35

Wow this did get off topic.
@throwawayerino I'll look into the link, thanks.
Yeah my goal is just for lots of people enjoy my projects. So that means windows 10 as a primary target. I use linux myself. It's my main OS. I have win10 on another drive for steam and other stuff.
@Modanung It doesn't make sense to argue against MS or Steam here. It simply is irrelevant to this topic. That's like if someone made a thread asking how to make a heightmap in photoshop and then suddenly there's a debate over photoshop vs. gimp. The whole point of the thread is support for the issue, whether you agree with it ideologically or not.

-------------------------

Modanung | 2020-11-30 17:58:11 UTC | #36

[quote="evolgames, post:35, topic:6583"]
It doesn’t make sense to argue against MS or Steam here.
[/quote]

I was responding to the misleading statistics that were thrown around by both @Dave82 and @Eugene. Indeed the topic veered somewhat off course, but it _is_ about Windows and security; they do not match.
It is designed to be insecure, both as part of M$'s business model as well as the global Stasi 2.0 situation that most people shrug off and/or deny to be taking part in. You call it ideology, I call it aware and moral.

-------------------------

Modanung | 2020-11-30 18:37:10 UTC | #37

https://en.wikipedia.org/wiki/Programming_ethics

-------------------------

Eugene | 2020-11-30 22:35:33 UTC | #39

[quote="Modanung, post:36, topic:6583"]
I was responding to the misleading statistics that were thrown around by both @Dave82 and @Eugene
[/quote]
It's not enough to point out the existence of bias. Literally all statistics are somehow biased.
Complaining that statistic is biased is like complaining that trees are made of wood.
To discard statistic as misleading it should be proven that the bias is sufficiently large.

There's no players unless proven otherwise.
Unless you can somehow *prove* that there are enough non-Steam PC players to make Steam statistics sufficiently biased, it's safe to assume that the percentage of non-Steam PC players in negligibly small and Steam statistics is reliable.

PS: Yes, I'm sorry for offtopic

-------------------------

evolgames | 2020-11-30 22:38:03 UTC | #40

Well, I don't think he's interested in selling games, anyway...
As far as off-topic, no big deal I guess now since the @JSandusky has pretty much answered everything I was asking about.

-------------------------

