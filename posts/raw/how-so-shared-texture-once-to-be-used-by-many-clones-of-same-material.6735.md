najak3d | 2021-03-01 07:06:46 UTC | #1

In our Map Tile application, there is one texture that will be universal and shared by all Tiles the same (it's like a static lookup table).

For efficiency-sake, we'd like to avoid having Urho3D set this Texture Unit individually for each Tile instance.   They will all be using a clone of the same Material, but each one will have some material settings that are specific to that instance, and some settings that are shared.  Each Tile will have one Texture that is unique to that Tile, but for ALL TILES, they will have one texture that is set the SAME for all Tile instances.

Is there a way to specify this ONE SHARED TEXTURE without having Urho3D thinking "it might be different" (we figure Urho has to do work in setting up the Draws for each Tile, and would like for it to "skip this logic" for that shared texture... just set it once, and then forget.

If not, then we'll just set this texture the same for each Tile instance, and accept the performance hit.  Likely the hit will be negligible, so this probably isn't a big deal.  It's just that if there is an easy way to optimize this, then we should probably optimize it, saving CPU cycles for Urho.

NOTE: We're not concerned about the time to call "SetShaderParameter", but rather are concerned with the Urho engine code that may have to keep setting this same texture for 100 Tiles, every render frame.  I hope I'm explaining this clear enough.

-------------------------

JSandusky | 2021-03-03 21:43:54 UTC | #2

[quote="najak3d, post:1, topic:6735"]
NOTE: We’re not concerned about the time to call “SetShaderParameter”, but rather are concerned with the Urho engine code that may have to keep setting this same texture for 100 Tiles, every render frame. I hope I’m explaining this clear enough.
[/quote]

During the batch loop material textures are set through the `Graphics` class which checks if a given texture is already bound before binding.

Setting the same texture won't happen every cloned material change unless other textures are changing. In GL you're entirely at driver mercy. In D3D11 you're at the mercy of the SRV binding being lowest-dirty-index to highest-dirty-index. Assuming those materials are activated one after other and batching doesn't do something else.

You're still at driver mercy there as to what really happens.

---

You can try using the render-order in the material to force your cloned-materials to be as contiguous as possible. That lets you fudge the order of things around. I've never used it for that kind of optimization though. It's more the sort of thing you use to draw the FPS-gun first, or alpha-tested/grass last where discard killing early-z won't hurt as bad --- and not so good for other sequencing issues (though usable with work).

Edit: you could setup a dedicated pass in Renderpath them to ensure their clustered but that'll almost certainly be slower than the render-order which is already considered in batch sorting anyways.

Best hope for driver luck is make sure the shared-texture is as low in the texture-units as you can go. Ideally unit-0.

-------------------------

