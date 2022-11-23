Mike | 2017-01-02 01:14:13 UTC | #1

I need to retrieve a Constraint2D component, which can be any type (Constraint2DRevolute, Constraint2DRope...), from a node.
Is it possible to get theConstraint2D component without having to check each possibility (HasComponent<Constraint2DRevolute>, ...) ?

-------------------------

cadaver | 2017-01-02 01:14:13 UTC | #2

In C++ you should be able to use GetDerivedComponent().

This was before the basetypes were included into the custom RTTI system, so a script version taking e.g. a string typename should be doable too, but isn't implemented at the moment.

-------------------------

Mike | 2017-01-02 01:14:14 UTC | #3

Many thanks, that should be exactly what I need  :stuck_out_tongue:

-------------------------

