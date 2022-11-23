Jens | 2022-10-27 17:25:15 UTC | #1

Hi,

I'm a bit confused by Zones, specifically how the AmbientColor LightMask is supposed to work. The code is UrhoSharp, but I think the principles should be the same as Urho3D. According to the Urho documentation it is just the object's and zone's lightmasks that matter. According to the metadata it is the scene light's and zone's lightmask. From a day's experimenting it seems to me the scene light's + object's lightmasks work as expected. As soon as a Zone is added nothing seems to work as expected. 

> Urho Doc - Zones
Like lights, zones also define a lightmask (with all bits set by default.) An object's final lightmask for light culling is determined by ANDing the object lightmask and the zone lightmask. 

> Drawable MetaData:
        //     Return light mask. Or Set light mask. Is and'ed with light's and zone's light
        //     mask to see if the object should be lit.

Another thing I found strange is that the scene with no lights and no Zone is close to black. If a Zone is added, yet the lightmask set to zero, the scene is a grey colour. I would expect it to still be black. No doubt I've misunderstood something here.

-------------------------

Eugene | 2022-10-28 09:52:55 UTC | #2

Okay, so we have a lot of masks going on.

Ignore `ViewMask` for now, it's irrelevant.

`LightMask` and `ShadowMask` affect **only** `Light` components and how they shade geometry.
These masks are checked like `object_geometry.LightOrShadowMask & ligth_source.LightOrShadowMask & zone_of_the_object.LightOrShadowMask`.

So, basically, mask of the `Light` component is used as is, and mask of the geometry is modulated by the `Zone` containing the geometry. The common use case is to e.g. disable sun for indoor zone and all objects that belong to it, without manually setting mask for every single object.

`ZoneMask` is used only to determine whether the object belongs to `Zone` or not.
`AmbientColor` and all other properties of `Zone` are applied based on the containing Zone only. So, only object position and ZoneMask intersection between object and Zone matters here.
`LightMask` and `ShadowMask` are irrelevant there.

-------------------------

Jens | 2022-10-28 17:16:58 UTC | #3

Thanks for the detailed reply. 
I've come to realise this is going to take some time to get it right. Bit of a shock, up until now I've used diffuse materials, and the scene lighting was perfect with a single directional light and Zone set at 0.5 ambient colour. So, I thought lighting, at least, is not gonna be a problem. Now I'm using diffuse + normals (procedural plaster material), and it's got a whole lot more difficult.
Thanks again.

-------------------------

