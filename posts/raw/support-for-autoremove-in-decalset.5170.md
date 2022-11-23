Leith | 2019-05-22 05:03:17 UTC | #1

This seems like a fairly trivial request :slight_smile:

Can anyone think of a reason why DecalSet is not being treated like ParticleEmitter and SoundSource?

-------------------------

Leith | 2019-06-08 04:16:31 UTC | #2

Bump.

If we use DecalSet as per the sample, and we give our decals a fixed lifespan, the decals will automatically be removed when they expire - but we end up with empty DecalSet objects stuck to our drawables. For the static world, that's not horrible, but it is when we apply decals to things that can move.

-------------------------

Leith | 2019-08-03 09:22:35 UTC | #3

Here's a proposed patch for DecalSet to provide it with the same optional "AutoRemove" support as provided by ParticleEmitter. This patch has not been tested, but is a recreation of a recent implementation of the same solution, I'm fairly confident that the code is good.

DecalSet already has the capability for Decals to have a fixed lifespan - when they expire, they are automatically removed from the DecalSet. This is very similar to what happens with ParticleEmitter.
But DecalSet was missing the capability of itself being auto-removed when it "expires" (due to all its decals expiring / being removed). 

When the last Decal is removed from a DecalSet, these changes allow the empty component to optionally destroy itself, "just like ParticleEmitter", such that we don't end up with empty DecalSet objects attached to our drawables.

<https://www.dropbox.com/s/60fqo3kp761sxq7/DecalSet_AutoRemove.zip?dl=0>

-------------------------

Modanung | 2019-08-03 10:35:24 UTC | #4

Do you know [how git works](https://git-scm.com/book/en/v2)? It's easier reviewing the diff of squashed commits and to test a *whole* clone.

-------------------------

Leith | 2019-08-03 10:35:30 UTC | #5

In the past, I have offered PR, and found it to be a less than satisfactory route, as it is not transparent, it is not search-friendly, and there is no guarantee that my work would be seen again.
Times, as they say, are changing, and I'm happy when the community is happy.

-------------------------

Modanung | 2019-08-03 10:37:03 UTC | #6

Linking to commits does not require issuing PRs, it *does* however require having a public repository.

-------------------------

Leith | 2019-08-03 10:40:34 UTC | #7

I have a public fork, but I hate the fact that I have a fork, and I am not inclined to publish it as it implies, in my mind, that I have made substantial contributions to the codebase, and though I may be prolific, none of my changes :to date: are exactly ground-breaking...

-------------------------

Leith | 2019-08-04 08:36:49 UTC | #8

There is likely a tiny bug in the sourcecode I posted...
The "extern" statement should be "inside the urho namespace"... not slightly by a few lines outside of it.
Just move that statement down a few lines, past "using namespace Urho3D" and you're gold.

-------------------------

