glebedev | 2021-04-01 08:24:34 UTC | #1

I would like to implement something like this in Urho3D:
https://www.youtube.com/watch?v=KLjTU0yKS00

I see that I should trigger solver manually and it seems to be quite expensive if I do it sequentially for each character as they could be ran in parallel.

What would be the best way to implement full body IK rig with minimal changes to Urho3D? What would be an ideal way to do it?

-------------------------

Modanung | 2021-04-01 11:42:33 UTC | #2

That sounds a bit like my blue PiRMIT concept, in terms of rig-agnostic animations. It's core idea is setting transform ranges for bones, mapping them to tendons and using normalized values to control these. This should allow for clenching a fist or posing the spine with a handful of characters, as well as sign language. The range and tendon mappings would be in red PiRMIT, which should also be able to define/generate the rig and mesh. That's where my quest for a better curve started, from which I'm working my way back up. Red PiRMIT will basically function as a `Cyberplasm` markup language.
:hole:

-------------------------

SirNate0 | 2021-04-01 15:18:37 UTC | #3

Honestly I had issues with Urho's IK, specifically it didn't interact well with physics, though I don't remember what exactly didn't work at this point. As such, I just rolled my own - a two bone IK setup is fairly easy to implement, one bone is even easier (look at), and something like following a curve is reasonably simple as well. If you want, I could share some of what I've done with you (at least the two bone one), though don't expect it to be particularly polished. If you look at my [procedural animation project](https://discourse.urho3d.io/t/procedural-animation-project/6497) it's basically a full body IK setup, though without any MoCap features.

I wouldn't bother with trying to make it parallel until you know it's an issue. Though as long as you don't interact with the scene nodes (e.g. just stick to computing transform matrices) it should be relatively straightforward to parallelize.

-------------------------

Modanung | 2021-04-01 18:00:26 UTC | #4

I think _witches_ might also be able to work as a non-iterative IK solver; coupling the normals to ~bone-Y.

-------------------------

glebedev | 2021-04-01 19:27:25 UTC | #5

What do you think of this one? https://github.com/kobli/ikSolver/blob/master/solver/src/solver.cpp

-------------------------

SirNate0 | 2021-04-02 04:20:13 UTC | #6

I'm not really sure. I think Urho already implements FABRIK, I think it's just how exactly the physics and the IK solver tried to set transformations that ended up not working together. In general I'm slightly skeptical that it would give you results that are better than individually combining a series of 1 and 2 bone IK solvers (arms/legs would be two bone, hands and maybe hips one bone) and something special for the spine. I certainly can't call myself an expert though.

That said. It's probably possibly to get a FABRIK solver to give you good results, provided it does support constraints on the joints. Though that also applies to the 1 and 2 bone solvers - you don't want your knees bending backwards or sideways.

-------------------------

