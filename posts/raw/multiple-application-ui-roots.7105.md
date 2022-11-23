najak3d | 2021-12-20 08:58:17 UTC | #1

We're devising a Game Editor setup using Avalonia, with elix22's Urho.NET.

Here's the general scheme:
1. Urho App is the main app, and owns the Main Window.
2. In Game Editor mode, we're using Urho's UI system to render a full-screen sprite inside which Avalonia is rendering.
3. Inside of Avalonia's Dock Control sample, we have an Urho View 3D, which renders great.
4. ISSUE:  Since our Game UI is ALSO going to use Avalonia, we need for it to render inside the View3D game window.

But View3D doesn't sport it's own Urho UI.   We'd like a 2nd instance of Urho UI to place inside the View3D, and have it work the same as it does for the full screen now.

Perhaps I'm missing something; another/better way.

For now -- we have a work-around which is to simply use the SAME Urho.UI.Root to create the Sprite (which renders Avalonia), and place that Sprite overtop the View3D window, so that it appears to be a part of the View3D.

This seems to work fine, and performs well-enough - but the solution feels kludgy.   I think we'd prefer to have a separate UI.Root that runs inside the View3D itself.   (A UI inside the UI.)

Another idea that just popped into my head now is that maybe we can Parent the Game UI sprite to the View3D -- and maybe that resolves it, if there is relative-sizing/positioning -- so that if View3D resizes or moves -- the child Sprite inside it will move/resize in unison.   (OR... we can just manually do this math, and create the same effect in C#).

Here's a screenshot of our KLUDGE -- the UI sample we're using here is crap -- it's just a placeholder.   We have already figured out how to make this semi-transparent with click-through-to-scene.

![image|690x366](upload://gEiIlr1fbKLRsfx3FlBFt2J89u4.jpeg)

-------------------------

SirNate0 | 2021-12-21 16:28:20 UTC | #2

I've not tried it myself, but what happens if you just create another UI? You won't be able to make it a Subsystem in the Context, since there can only be one per type, but it might work.

Alternatively, could you just use the View3D or a UI element with the same size as it where you would otherwise use UI::GetRoot()?

-------------------------

najak3d | 2021-12-22 02:33:05 UTC | #3

We've resolved to making it work with just one UI.Root, as you have suggested.   We'll just do our own math (for position offsets/scale) and wrapper to make it *seem* like multiple independent UI systems.

This works just fine.  Feels like a kludge to us, but won't to our users, who will be able to treat this like two independent UI's -- Game Design Tools vs. the In-Game UI.

From Urho perspective, we simply map an Avalonia Window to an Urho.UI.Sprite, and it works efficiently and without issue (that we can see now).

-------------------------

