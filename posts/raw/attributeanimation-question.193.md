alexrass | 2017-01-02 00:58:46 UTC | #1

Is it possible to change the shader options with AttributeAnimation?

-------------------------

cadaver | 2017-01-02 00:58:47 UTC | #2

At this point no, because there are no per-object shader parameters yet (it's always in the material) and materials don't have attributes as such.

Ideally we would have a generic mechanism for animating any Variant object, but in case of shader parameters it's a bit unsafe or would require hacks, because the parameters are stored inside a HashMap, and if you were to delete a parameter from the HashMap that was currently animating, how would that be safeguarded against?

-------------------------

alexrass | 2017-01-02 00:58:47 UTC | #3

Thanx for your engine. Simply amazing.

-------------------------

friesencr | 2017-01-02 00:58:48 UTC | #4

A method could be added to variant:  GetOrDefault<float>(key)

if the key doesn't exist then you get default

-------------------------

