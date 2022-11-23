evolgames | 2020-10-17 01:30:21 UTC | #1

What's a good way to make a realistic chain? As in this:
![10237598-close-up-of-a-curled-up-metal-chain|690x475, 50%](upload://9BQoVU0EFd2e3VzQbLIPyAyjPNg.jpeg) 
Performance is not an issue here. I assumed that if I made each link a separate node (with rigidbody) it would be more realistic. I added a traingle mesh shape to each and rotated 90 degrees every other link. Because the collider forms a torus-like shape, it *should* allow these to interlock without constraint joints, correct? The way a real chain is connected? Is it *possible* to connect bodies physically like this, just by spawning them inside each other? I feel like this solution would be the realist but I suppose joints are necessary here. Has anyone needed to make a physically-based chain or rope-like iterated object?

So far I haven't figured it out. I tried the real-world approach and also with hinge/point constraints and I got spastic results. I also tried descending the mass which helped but takes away from realistic movement.

Here is the setup (0 mass rigidbodies in this screenshot)
![Screenshot_2020-10-16_21-23-32|690x388, 75%](upload://ax8m41mVg8Fl9NWBd53Dzl2QwUK.jpeg) 

And here with descending mass (first link has 0 to connect to ceiling) and point constraints they spin through each other and are easily pulled apart, even though they should be colliding with each other. I started messing with angular and linear factors too. But, come to think of it, each link *should* be able to wiggle every which way.
![Screenshot_2020-10-16_21-26-56|690x388, 75%](upload://dY6QJAdhzVcNBj9iGn0PvwZ6V7v.jpeg)

-------------------------

vmost | 2020-10-17 02:08:31 UTC | #2

I saw a blender demo for creating chains... looking at google there are a bunch of resources available.

-------------------------

evolgames | 2020-10-17 02:16:53 UTC | #3

I don't have any issue creating the chain model. See above. I've made the link. Making Rigidbody simulations on blender will not work for realtime urho application.

-------------------------

vmost | 2020-10-17 02:31:38 UTC | #4

Oh I see what you were saying. The method of spawning links inside each other seems like it should work, what exactly were the problems you encountered?

-------------------------

evolgames | 2020-10-17 02:54:04 UTC | #5

>The method of spawning links inside each other seems like it should work

I hope so.
The problem is they immediately explode. Now I'm wondering if adding them one at a time, with some frames in between for bullet to settle the above link, might work better.
I'm going to test with hoolihoops and see if absolutely no contact before starting changes anything. Because a chain has the links very close by design, so maybe that's the issue.

EDIT: Tried with large rings and they absolutely were 100% separated. Still falls apart. Maybe triangle meshes can't hold objects this way? It's weird. The only way to have a hole in the mesh is to use a triangle mesh shape because otherwise it's covered. For regular collisions, that works, but you can't do that for rings. I can see the shape in debug geometry to be correct, but they pass through each other.

This is an interesting problem.

-------------------------

SirNate0 | 2020-10-17 03:01:13 UTC | #6

I'm not certain, but I think the triangle mesh shape is meant for static objects. Though you may want to double check the Urho/Bullet documentation on that. You could try a set of capsule shapes arranged in a rectangle and see if that works at first, and if it does go for a more rounded edge using more capsules later.

But my personal recommendation would actually be too use bullets softbody physics to make a rope and use the chain as the model.

-------------------------

evolgames | 2020-10-17 03:05:33 UTC | #7

Oh okay, that's interesting. I'll try out multiple slim capsules and see what happens. That sounds possible.

Hmm alright. I know there are collision chains for 2d but in the urho docs I don't see any soft body/rope entries. I'm also doing each link as it's own model currently but I can imagine how it'd behave as one large chain with rope mechanics behind it.

-------------------------

vmost | 2020-10-17 03:15:28 UTC | #8

Yeah sorry, when I said Blender earlier I meant Bullet [see this video](https://www.youtube.com/watch?v=BGAwRKPlpCw).

-------------------------

evolgames | 2020-10-17 03:22:42 UTC | #9

No worries. This is cool, thanks for the link.
@SirNate0 I tried the capsules. It works but it's rough. I'll try a soft body next.

-------------------------

Modanung | 2020-10-17 09:03:51 UTC | #10

Did you have a look at sample 13? It uses `Constraint::SetDisableCollisions(true)`.

-------------------------

evolgames | 2020-10-17 12:58:07 UTC | #11

Yeah that didn't affect it. It works with multiple capsules, though not very gracefully.

-------------------------

Modanung | 2020-10-17 15:47:55 UTC | #12

You may want to write some custom rope-IK-like component to save on resources anyway.
Unless there's only one big heavy chain in your world.

-------------------------

evolgames | 2020-10-18 17:19:07 UTC | #13

That sounds smart. I was considering having multiple small chains as part of the environment to add to the mood of the rooms. But only a few would exist at any given time.

-------------------------

