Lumak | 2017-01-02 01:06:14 UTC | #1

I feel that I needed to write this game dev post mortem after completing my very first mobile game.  Why?  Well, your first is always exciting :slight_smile:  You can see it here [url]http://discourse.urho3d.io/t/lumaks-wraptiles/1231/1[/url].   My game is only 2D but it should say a lot about how good the engine is if someone can just pick it up can make a game in less than 2 months (barely).

Actually, this post is not so much about my game, but more about this engine.

This is my first open source engine that I've ever used. I did evaluate Epic's game engine and Unity engine prior to looking at Urho3D, but I decided against them for a few reasons.  I wanted something light weight and not too overly architected (code bloat) yet optimized, supported latest graphics capabilities, free to develop on multiple platforms, and that I could write my code once for multiple platforms with very little changes on my end.   Needless to say, it was very difficult to find such engine.

Then I discovered Urho3D.  I've been learning this engine for less than 2 months and feel as though I've only scratched the surface.  There's so much to this engine.  When I first started looking at it I was excited and couldn't wait to write a game with it.  As it turns out, I found that this engine gave me more than what I had expected.  From well architected classes, to well designed message event system, to mem dumps that helped me detect memory leaks that I wasn't freeing properly early on, to cmake build process which you don't have to bother learning because devs/contributors done all that for you, I can't say enough about how awesome this engine is.  

So here's to you originators/devs/contributors, kudos!

;tldr - this is an awesome engine!

-------------------------

Lumak | 2017-01-02 01:06:14 UTC | #2

Alright, maybe I'll write a bit of post mortem about my game development and how it went if anyone is curious.  Albeit, it's not a 3D game, some might be curious about Android development anyways.

As you saw from my comments above, the least of my worries about my game development was using Urho3D.  If anything, that was easiest part of my development due to lots of great features already built into it.  More time was spent working on other stuff.  

I'm no artist, so I spent/wasted lots of time trying to create art assets and probably created several iterations on what looked about right - AND it looks like that!  What you see in the game is probably typical of what a programmer would call a polished mock up art :slight_smile:

Another time sink was learning Android development and how to implement Google Play Services.  I spent more time reading posts on Stack Overflow to get answers that I didn't know.

I used the engine as it was with very, very minimal changes to things like creating a grouped check boxes (which I posted in the code exchange) and having a fixed knob size on the slider.  Majority of new code that I added was on the Java side to support Google Play Services and Interstitial AdMob.  If anyone is interested in those, I can probably post them on the code exchange.

-------------------------

esak | 2017-01-02 01:06:15 UTC | #3

Congrats for finishing your game!
It's good to hear your experience and that you are positive to Urho3D, since I'm in the process of making my first game with Urho3D (I have previously used libGDX).
I must say that my experince with the engine is the same as yours. It's very nice!

-------------------------

Lumak | 2017-01-02 01:06:15 UTC | #4

Ty esak and good luck in your development.  Yeah, I really like this engine and I want to do a lot more with it than just create 2D games.  I'm curious as to what it can do in a 3D space.

-------------------------

weitjong | 2017-01-02 01:06:15 UTC | #5

[quote="Lumak"]I used the engine as it was with very, very minimal changes to things like creating a grouped check boxes (which I posted in the code exchange) and having a fixed knob size on the slider.  Majority of new code that I added was on the Java side to support Google Play Services and Interstitial AdMob.  If anyone is interested in those, I can probably post them on the code exchange.[/quote]
Please do share your code. I am always interested to see how others do things from their code.

-------------------------

Lumak | 2017-01-02 01:06:16 UTC | #6

K, I'll post the java code on the code exchange, but it'll be a couple of days, though.  I just digested AdMob reports on how I'm getting paid from ad activities, and I think I'll have to change my strategy a bit and rewrite some parts of the code.  I'll post it once I've done that.

-------------------------

Lumak | 2017-01-02 01:06:19 UTC | #7

I posted the java code and other stuff here [url]http://discourse.urho3d.io/t/android-googleplay-admob-and-licensing-code/1238/1[/url]

-------------------------

