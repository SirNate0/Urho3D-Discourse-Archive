rogerdv | 2017-01-02 01:03:03 UTC | #1

I need to implement some way to notify NPCs that player or any other NPC entered its vision area (like a cone of X degrees in front), how can I do this?

-------------------------

thebluefish | 2017-01-02 01:03:04 UTC | #2

Easiest way to do this is to create a Frustum, like a camera. Then you can do OBB tests with any meshes that you want to check against.

Alternatively, you could create a collision shape that defines your cone of vision. Then you can use the physics system to run collision checks between your collision shape and any other collision shape in the scene.

No code as I'm writing this from my phone, but it's rather straight-forward. I've implemented something functionally similar with both methods, so I know it's possible with either way.

-------------------------

