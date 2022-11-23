Leith | 2019-08-03 07:49:28 UTC | #1

Here's a proposed (and tiny) patch to deal with root motion in character animations.

I chose not to interfere with the AnimationState blending implementation - I wanted the solution to work with layered animation blending... the changes are not intrusive and don't appear to break existing code.

There's a new boolean switch in AnimationController which, if enabled, will prevent the controller from translating the model's root bone - AT ALL. 
Instead, the change in (world) position due to the sum effect of the animation system is measured and recorded, the velocity implied by that position delta is also noted, and it is "left to the user" to apply position changes to their character as they see fit (example: perhaps they want to hand the extracted velocity to a navmesh agent, who applies position changes that match the animation as well as the agent's navpath ...)

I kept this simple, since my needs are generally simple - but character root motion is certainly something I want to have at least some control over.

< https://www.dropbox.com/s/tqqfxvu85ofs73o/RootMotion.zip?dl=0 >

-------------------------

