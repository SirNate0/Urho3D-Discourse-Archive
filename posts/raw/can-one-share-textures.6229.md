Haukinger | 2020-06-28 16:31:50 UTC | #1

I create tiles and each gets nine 256x256x256 volume textures (one for the tile itself, 8 for potentially overlapping neighbours). I don't want to create each texture 9 times, so I keep them around in a lookup table.
When a tile gets off screen, I remove its node.
Now, when a tile comes back, the texture (that it had before) in the lookup table has been deleted. What do I have to do so that my textures survive when one of the nodes using them gets removed?

-------------------------

Lys0gen | 2020-06-28 21:20:36 UTC | #2

What do you use for that lookup table? Keeping the texture alive by saving a SharedPtr reference to it should work fine.

-------------------------

Haukinger | 2020-06-29 15:50:09 UTC | #3

I keep an array of the textures, but I should add that I don't use Urho3D directly but through the managed wrapper (urhosharp).

I think I see the problem - when I create the managed wrapper Texture object, it does not create something like a SharedPtr of itself. So when I add the texture to the material, the material is the sole owner of the texture (together with other materials that use it), and if the last such material goes away, Urho3D deletes the texture, because it cannot know that there's a managed wrapper around that might want to use it. I guess, I'll file a bug report with urhosharp.

My solution is to create dummy materials together with the textures (that I don't ever use, so they never get deleted).

-------------------------

SirNate0 | 2020-06-29 18:35:37 UTC | #4

If you never want them to be deleted you should be able to just add them as a manual resource to the reasource cache (you could still remove them, it may be a bit more difficult than having just a vector of them, however).

-------------------------

