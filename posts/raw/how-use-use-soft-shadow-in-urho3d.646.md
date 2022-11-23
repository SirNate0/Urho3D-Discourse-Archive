abcjjy | 2017-01-02 01:01:51 UTC | #1

I didn't find any properties in Light class likely about soft shadow. In Unity, soft shadow can be set on light. 

Does Urho3d have this feature? If so, how to use it? If not, is there any reference on how to implement and integrate into Urho3d?

Thanks.

-------------------------

cadaver | 2017-01-02 01:01:51 UTC | #2

Welcome to the forums!

You will need to write improved light/shadowing shaders to get the effect you want. The shaders that come with Urho do a fairly basic 2x2 hardware PCF sampling of the shadow's depth texture. If you want something like variance shadow maps you will need to modify the engine code to allocate the shadowmap textures in a different format, right now they're depth textures (color texture not used at all.)

-------------------------

