Sinoid | 2019-02-22 04:37:07 UTC | #1

UMDL2 Proposal

These are my notes (portions are complete but still), please rip them to pieces.

---

- Addition of `ResponseCurve` type
    - Functional curves defined by standard MKCB, shape, inverse-X, and inverse-Y
    - Will be part of variant
    - Aside from animation they're useful for AI weight functions
- Addition of key -> key interpolation parameters
    - Defined by response curves
- Addition of track blend parameters
    - Defined by response curves
- Addition of MorphTracks
    - Recorded morph-target weights in animation
- Addition of `Phases`
    - Similar to triggers but windows of time
    - Each phase has a name, start, end, and arbitrary Variants associated with start/end
    - Blends can specify phases to synchronize against
         - see **DOOM** talk for retargeting
- Root-motion as a first class citizen
    - Tied as well into phases
- Weighted push model for animation
    - Existing animation works as is superficially
        - new work can push over it
    - Facilitates pushing keys on demand rather than relying on existing animation
         - Futures are pushed, final blend reads the resulting futures for the given time
    - Provides correction that doesn't require sorting post-update bone correcting components
- Additional stock components for
    - Terrestrial navigation selection
    - Saccades and blink
    - IK assistance for strings of Look-at (see **DOOM** talk)

---

The biggest missing thing is selection-sets IMO, but those are not trivially reconcilable IMO.

-------------------------

Sinoid | 2019-02-25 04:57:29 UTC | #2

- Morph-tracks
     - Basically finished
     - Supported in the binary UMDL2 format and in the XML files already used for triggers, allowing their presence in the XML files
         - Assimp pretty is morph-idiotic, sxs XML support there provides a supplementary tool path lighter export from DCC tool
- Phases
    - Down to testing stage and verifying that the matching functions work as intended
        - for *naive* match to normalized position, not going to bother trying to do weighted sync in Urho3D's animation, it's all way off in the wrong direction for that - a silly amount of work
    - Phases can function as *loop portions* for looping animations, only exiting the phase when the animation is fading out
    - Also supported in either binary UMDL2 output or the sxs XML
- Root-motion
    - Not actually that serious, there's just no existing reasonable utility means to query the necessary information one actually wants to do root-motion from Animation resources
        - ie. grab the animation root transforms for the start and end of airborne phase, then retarget the root-motion on the fly to an arbitrary traversal
    - Dealing with the above is better than going for one-fix-for-all
- Weighted-push model
    - Not necessary
    - Just need to be able to push arbitrary `AnimationState` instances into an `AnimationController` and replicate those over network
        - ie. target-by-name transforms
    - `Animation` resource is also a bit *too* fixed, it's a jerk to work with and should be refined to be easier to work with and even use perpetually appended one-off *managed* resources
        - hence, focus on `AnimationState` instead - resources are network dumb

---

Fairly sure it doesn't actually belong in master, but just dropped elsewhere for utility. **DOOM** navigation wheel is largely functional now, only some dead-zone tuning to go and determining whether it should be controlling animation directly or signaling-events (right now it directly controls, which gets wonky with the dead-zone counter-rotation).

![motionwheel|400x300](upload://mgyMugffRy32OqKdaztZoiSoQIt.png)

-------------------------

SirNate0 | 2020-04-07 23:35:10 UTC | #4

Did you end up finishing this? I don't really have any comments as I don't have enough experience with animation to provide feedback, but I'm about to start the work of animating models for my game and some of these features seem very useful.

-------------------------

