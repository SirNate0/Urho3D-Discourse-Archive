Enhex | 2017-01-02 01:11:41 UTC | #1

A model vertex's elements need to be in a specific order?
Is it documented anywhere?

-------------------------

cadaver | 2017-01-02 01:11:42 UTC | #2

Yes, the order is in GraphicsDefs.h element enum (elements can be included or left out, but order must stay). You can also check the element offsets from VertexBuffer after you create it.

I'm currently working on freeform vertex declarations, after which this shouldn't be an issue anymore, but the API will break/change in some ways.

-------------------------

