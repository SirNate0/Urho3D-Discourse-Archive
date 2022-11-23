Batch | 2021-04-20 00:36:44 UTC | #1

I have a Component that has a member of type set<unsigned int<j>> which holds a bunch of Component IDs from the scene. I'm trying to serialize this such that I can use the Scene's SaveXML() and LoadXML() functions, but I'm not having any luck figuring out how to get the macros to work. It seems that they rely on Variant having an operator=(const set<unsigned int<j>>& rhs) which it doesn't, and I can't figure out how to add it.

How do I serialize attributes that are of a type Variant wont accept? Thanks.

-------------------------

SirNate0 | 2021-04-20 02:06:33 UTC | #2

Hello, welcome to the forum!

I'm not certain there is a way to serialize other types directly that aren't supported by Variant. It might be possible now with the addition of support for user types in Variant, but I haven't done anything with that so I'm not sure.

In any case, since node IDs can change when loading the scene (refer to the Scene resolver class for how this works) you may need to convert to a VariantVector containing a series of unsigned integers for your serialization. I think it is possible to write an accessor that would do the conversion for you. Make sure you mark the attribute as AM_NODEIDVECTOR so the IDs are converted properly though.

If you need more help feel free to ask, though I'm not sure I specifically could provide that much more assistance.

-------------------------

Batch | 2021-04-20 02:37:19 UTC | #3

There doesn't seem to be any way to add custom types to Variant that can be serialized, but I think I can just edit the Variant.h/Variant.cpp files to support my types. It should be easy enough to add support for any type to the Variant interface, then behind the scenes just use json to turn it into a string.

I'm really surprised there's no standard way of serializing a list of references to Nodes. It seems like a common task people would want to do in a game world that can be saved and loaded.

-------------------------

SirNate0 | 2021-04-20 04:30:31 UTC | #4

There is an existing way of serializing such a list of Node IDs. It's used by Spline and StaticModelGroup, so I guess you could call it standardized? I certainly wouldn't call it particularly user friendly, though. That aspect can certainly be improved.

In any case, I think your approach of adding it to Variant is suitable. It should be more efficient in the end implementation than copying to a VariantVector, though I will warn you that it might take slightly longer to write the code (by my own very tentative estimate). That's one of the best advantages of having an open source engine, though - being able to modify it as is convenient to you.

-------------------------

Batch | 2021-04-20 04:48:08 UTC | #5

Thanks, I'll take a look, although what I put together so far is working very well so far. Now that I have a bunch of new types working with Variant, everything else fell together nicely.

Linking Nodes/Components together is a big part of my designs, so being able to reliably do that across saves is important, but I'm sure it'll be relatively easy in the end. So far the IDs of Components and Nodes have remained the same after saving/loading. Overall the engine has been fantastic so far.

-------------------------

