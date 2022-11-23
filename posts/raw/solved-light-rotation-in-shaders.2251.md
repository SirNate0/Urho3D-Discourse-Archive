dragonCASTjosh | 2017-01-02 01:14:15 UTC | #1

Is there a light rotation value within the shaders or will i have to make my own uniform?

-------------------------

1vanK | 2017-01-02 01:14:15 UTC | #2

cLightDirPS ?

-------------------------

cadaver | 2017-01-02 01:14:15 UTC | #3

That's the forward dir of lights where applicable, don't think it applies to point lights. If you want a general transform matrix of the light node then make a new uniform.

-------------------------

dragonCASTjosh | 2017-01-02 01:14:16 UTC | #4

[quote="1vanK"]cLightDirPS ?[/quote]

Worked perfectly

-------------------------

