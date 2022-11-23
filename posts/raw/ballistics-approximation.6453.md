lebrewer | 2020-10-22 00:52:42 UTC | #1

Not for Urho, but might help people working with projectiles in their projects: https://www.patrykgalach.com/2020/03/23/drawing-ballistic-trajectory-in-unity/

Helped me a lot in my game! :D

-------------------------

Modanung | 2020-10-22 10:12:57 UTC | #2

Since you're basically drawing a parabola, it might be useful to have a `Plotter` struct that generates a vector of `Vector3D`s which could then be used to generate the desired geometry through a `RibbonTrail` subclass. This approach would extend the applicability of your classes while providing more control by separating the shape and resolution of the curve from how it is displayed (if at all).

-------------------------

