franck22000 | 2017-01-02 01:04:31 UTC | #1

Hello guys ! 

What is the best way to get the material pointer of a geometry surface hit by a raycast ? The procedure is unclear for me at the moment.

I would like to do such thing for example to know a surface type (written as a property in material) and then for example play different footsteps sound according to that.

Thanks

-------------------------

cadaver | 2017-01-02 01:04:31 UTC | #2

Previously you couldn't, but if you grab the very latest master branch, a triangle-level raycast to StaticModel will return the hit submesh (batch) index in the subObject_ variable of the raycast result. You can use this index in StaticModel's GetMaterial() to get the material. Note that you can't assign arbitrary properties to materials, so you rather need to have some external lookup map between e.g. materials and sounds to play.

-------------------------

franck22000 | 2017-01-02 01:04:31 UTC | #3

Thanks you ! I will grab the last branch right now.

[quote]Note that you can't assign arbitrary properties to materials[/quote]

Would it be possible to add this possibility in the master branch ? I think it could be usefull for a lot of developer.

-------------------------

cadaver | 2017-01-02 01:04:32 UTC | #4

Urho's material is strictly tied to rendering. It doesn't contain physics properties or anything else unrelated. Therefore I'm not terribly in favor of adding anything extra to it.

If you really wanted, you probably could abuse the shader parameters (they're Variants) to contain parameters that no shader actually uses, but are used for external purposes.

-------------------------

