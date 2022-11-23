ucupumar | 2017-01-02 00:59:05 UTC | #1

Hi all.
It seems Urho material can only use five predefined texture types (diffuse, normal, specular, emissive, and environment).
Can I use non-predefined texture unit for my custom shader?
Or what if I want more than five textures in one material?

-------------------------

cadaver | 2017-01-02 00:59:05 UTC | #2

You are currently a bit limited. There's an active issue on this on the issue tracker but there's so far no pleasing solution. The problem comes from trying to be compatible with mobile devices which may not have more than 8 texture units, and we also need some for light shape/attenuation, so currently you get max. 5 material texture units.

You can refer to texture units also with numbers instead of names, but they just practically map into the same units as diffuse, normal etc. See the terrain material and TerrainBlend shader to see how that's done.

-------------------------

ucupumar | 2017-01-02 00:59:06 UTC | #3

Oh, thanks for the answer. I'll look into that. I hope this 'issue' will find some solution somedays  :smiley:

-------------------------

