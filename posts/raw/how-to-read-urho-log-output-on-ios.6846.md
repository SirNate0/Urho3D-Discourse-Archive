najak3d | 2021-05-15 09:02:18 UTC | #1

On WPF/Windows, I can just read the Urho3D.log.
On Android emulator, I can read it from the logcat /  DeviceLog.

But on iOS Emulator, I don't know where to read the log?   Urho3D is failing miserably for us on iOS, and I have no log output to tell what has gone wrong.

Note, it would be awesome if Urho3D established a LogEvent that we could subscribe to, so that we could read the log messages via code directly, and collate the Urho logs messages with our App log messages (so you can see them in context).

As is - getting the Urho log is awkward, and varies by platform.   For iOS right now, on the emulator, we appear unable to get this log at all (i.e. VStudio for Mac doesn't provide a way to "View System Log" for emulators).

-------------------------

Eugene | 2021-05-15 18:11:48 UTC | #2

[quote="najak3d, post:1, topic:6846"]
it would be awesome if Urho3D established a LogEvent that we could subscribe to
[/quote]

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/IO/Log.cpp#L216-L219

-------------------------

najak3d | 2021-05-15 18:13:44 UTC | #3

Awesome.  That's a good solution for the Urho3D users.  Since we're on UrhoSharp, and nobody seems to be able to rebuild it (to allow modifcations), we do not have access to subscribe to this event.

I'm glad to see it in Urho3D.  Now it's just a matter of figuring out if UrhoSharp will ever be resurrected, or if RbfxSharp (aka Urho3DNet) will become a viable product.

-------------------------

JTippetts1 | 2021-05-15 22:16:27 UTC | #4

I feel like you could have built your own tech stack in the time you've spent agonizing about a dead C# engine port you deliberately chose to use in spite of all advice against it. UrhoSharp will almost certainly never be resurrected. If you've put money on the line with this, then you have bet it on the wrong horse. Urho3DNet might get there eventually, I don't know because I kind of don't care about C#, but it just baffles me why you would deliberately choose the dead port in the first place over vanilla, knowing even at the time that it was borderline unusable, then constantly pester people here, most of whom equally don't care about C#, about when it will be fixed for your particular edge case.

-------------------------

najak3d | 2021-05-16 01:54:56 UTC | #5

When we chose UrhoSharp, it was the Microsoft recommended solution for 3D presentation in Xamarin forms.  And the UrhoSamples worked out-of-box for all 4 platforms, very nicely.   It's still working great, with a few caveats.   No other solutions on the internet provided a solution this good (even with it's flaws).

We only have a few gripes with UrhoSharp, and most are easy-to-solve, if only it were resurrected.

UrhoSharp is not for AAA games, and maybe not even AA games - but it's still a solid solution for rendering elaborate packed 3D scenes, with most all of the benefit of Urho3D.  It's still a good solution for us.

RbfxSharp is a new hope for us to resolve the nuances that are hurting us with UrhoSharp.  We're getting some support there now.

@Egorbo, the author of UrhoSharp, has been semi-active on the Rbfx dev feed.  We're hoping this gains traction and becomes a completed, semi-supported (i.e. non-dead) platform, good for use by Xamarin/.NET devs everywhere.   A good solution doesn't exist for us; the gap is waiting to be filled.

Also to note -- RbfxSharp *does* expose the Log messages as an event that we can subscribe to, so they've already resolved this for us.  We may soon be in process of jumping over to RbfxSharp, and will be out of your hair. :slight_smile:

-------------------------

Batch | 2021-05-16 03:01:02 UTC | #6

Urho is weird. I myself have been using rbfx, but with C# disabled. Anything that breathes life back into these projects would be a good thing!

-------------------------

Modanung | 2021-05-16 09:47:54 UTC | #7

[quote="najak3d, post:5, topic:6846"]
When we chose UrhoSharp, it was the Microsoft recommended solution [...]
[/quote]

Computerland Rule #1: Never trust Microsoft

-------------------------

