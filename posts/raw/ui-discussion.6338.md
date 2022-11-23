vmost | 2020-08-21 13:56:35 UTC | #1

"I see a lot of people complain about the current Urho UI, perhaps we can evaluate the idea of either overhauling or replacing the UI functionality." I learned about Turbo Badger today, and it looks pretty amazing. If the UI should be overhauled, then I hope it aims for that kind of quality. There have been several efforts to integrate Turbo Badger with Urho.

-------------------------

Eugene | 2020-08-21 13:56:35 UTC | #2

[quote="vmost, post:1, topic:6338"]
I learned about Turbo Badger today
[/quote]
I thought it is dead? Last time I checked it was not being developed.
I have my hopes regarding [RmlUi](https://github.com/mikke89/RmlUi), it has exactly this kind of flexibility one needs from game UI. Where you can animate whatever you want without writing any code.

-------------------------

vmost | 2020-08-21 13:56:35 UTC | #3

Maybe it's my own naivete... the aesthetic demo'd in RmIUi is frustrating.
1. It feels very 'digital'... as if it was just temporarily loaded onto a screen (which is literally true of course). There is a lack of immersion, as if the portal we use to look into a game is a commodity (which is literally true) that could just as easily peer into a different game, and not native to the game itself. This concept only makes sense for sci-fi environments where all the in-game tools are commodities.
2. It has been done to death. Where is the essence of inspiring game UI design? Probably, unique solutions for each game.

My concern is the fundamental design philosophy of RmIUi precludes unique or native-feeling UI.

Well, it's not like TurboBadger is a great solution either. EDIT: it looks like the fork [HastyBadger](https://github.com/tesch1/turbobadger) is actively maintained, and plans to integrate updates from the original TurboBadger author who is too busy.

-------------------------

rku | 2020-08-21 13:56:35 UTC | #4

We consider a UI system not for it's looks but for it's functionality. You want good looks? You develop assets and it can look like anything you want.

-------------------------

vmost | 2020-08-21 13:56:35 UTC | #5

My point is function is the foundation of aesthetic. Is the functional design philosophy supportive of native UI design?

-------------------------

Eugene | 2020-08-21 13:56:35 UTC | #6

How would you measure UI aesthetic?

I know only one measurable criteria: capacity of being animated. Abrupt transitions are unnatural, even "instant" changes look better when they are not actually instant, just very quick. Every function and its first derivative shall be continuous. If framework supports smoothness, it is capable of making more natural picture.

-------------------------

vmost | 2020-08-21 13:56:35 UTC | #7

I would say the criteria for 'native' UI design is almost the opposite of animatableness, namely permanence. A UI element feels like it belongs there if it feels like it has always been there and isn't going anywhere. Rather than summoning elements out of the ether, moving between visible UI elements should be like looking at things that were already there before our eyes turned to them. In the case of sci-fi settings, this usually means activating in-world devices and interfaces which embody the permanence concept.

Transitions between UI elements are mostly ancillary quality-of-life effects.

-------------------------

GoldenThumbs | 2020-08-21 13:56:35 UTC | #8

Well, couldn't one do a lerp/tween with their UI to make it animate better?

-------------------------

GoldenThumbs | 2020-08-21 13:56:35 UTC | #9

Are you looking for a good UI lib for tools or games? Because if you want a native-looking UI you are probably working on a tool of some sort, and probably need to look in the direction of something like QT.

-------------------------

GoldenThumbs | 2020-08-21 13:56:35 UTC | #10

I'm going to be honest here in saying I don't see anything wrong with the current UI tooling, was just noting that quite a few people seem to take issue with it. I think it's more than functional for games and things like that. I personally see things like more fancy UI transitions as something the current UI lib is more than able to do as long as you are familiar with some basic math functions. Perhaps I'm not understanding what you mean...

-------------------------

vmost | 2020-08-21 13:56:35 UTC | #11

My thoughts are focused on a very UI-centric game concept.

-------------------------

Eugene | 2020-08-21 13:56:35 UTC | #12

I have used Urho UI for actual game once and I spent obscene amount of time in order to get very simple UI. Quality/Time ratio with Urho UI is extremely low

-------------------------

rku | 2020-08-24 13:33:01 UTC | #13

Min/Max Anchor/Offset is just impossible to use. I can feel brain cells dying trying to randomly tweak values to do what i want. Animating stuff is very verbose and done in code. Defining layouts is hard and due to tight data/layout coupling it can be quite problematic to reload UI as you would lose state. Styling without dedicated tools is also very complicated. Basically current UI system needs a lot of love to be viable and nobody is going to give that.

What i personally would like to see is UI system that:
* Where layouts can be easily defined with a text editor alone
* Has styling independent of layout
* Has ability to switch between styles for elements
* Has predefined functionality composing animations, without a need of writing c++ code
* Has data separated from UI
* Is easily reloadable at runtime
* Has support for rendering custom graphics for certain elements
* Has support for defining resolution-independent layouts

Look i just wrote feature list of RmlUi :eyes:

-------------------------

jmiller | 2020-08-25 18:25:00 UTC | #14

[quote="Eugene, post:2, topic:6338"]
I thought it is dead?
[/quote]
Or basically complete. :) though there are merits to an active project. There is one active [fork](https://github.com/tesch1/turbobadger). [TurboBadger](https://github.com/fruxo/turbobadger) does appear to be one of the most complete (including animation, resource files, languages, see link for full list), with Urho-compatible deps and numerous backend options, and is retained-mode (perhaps more easily avoiding the "tacked on" feel some have noted of some immediate-mode UIs)... FWIW

-------------------------

JimMarlowe | 2020-08-25 15:36:21 UTC | #15

If you want to try Turbobadger, or the superset of Turbobadger in the Atomic Game engine UI, and already integrated into urho3D, with both Angelscript and Lua support, and converted samples, and a cross platform sample launcher, then [AUI (Atomic Game Engine + Turbo Badger)](https://discourse.urho3d.io/t/aui-the-ui-of-the-atomic-game-engine-in-urho3d/5152) still applies. It's something you can compile and operate and examine to see if it is as good as it's suppose to be.

-------------------------

