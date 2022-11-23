aster2013 | 2017-01-02 00:59:33 UTC | #1

Hi, all

Current Urho3D have StringHash and ShortStringHash, ShortStringHash is use for VariantMap and object type. I prefer to remove it. 

Here is Lasse's options

[quote]Ok, I have profiled the network byte usage of ShortStringHash. It's very minimal (only in effect when new components are being created into the scene) so from that sense the refactoring, which would cause that byte amount to be doubled, would be ok.

However, it's still a rather major change and it will break old binary scenes for everyone so maybe you should bring it up on the development subforum first.[/quote]

-------------------------

friesencr | 2017-01-02 00:59:33 UTC | #2

Aster can you please explain why you would like to remove it?

-------------------------

aster2013 | 2017-01-02 00:59:33 UTC | #3

I don't like it, and I think StringHash is enought.

-------------------------

thebluefish | 2017-01-02 00:59:43 UTC | #4

What benefits would this provide? Is there any compelling reason to remove it outside of personal preference? It seems like there was a reason it was put in in the first place.

-------------------------

aster2013 | 2017-01-02 00:59:43 UTC | #5

Not personal preference. ShortStringHash is excessive design.

-------------------------

cadaver | 2017-01-02 00:59:46 UTC | #6

Basically ShortStringHash was a micro-optimization for reducing the memory size (16bits vs 32bits) used by object type IDs and VariantMap keys (event parameters, node custom vars) Now that its removal has been applied I tend to agree with Aster that it wasn't really necessary, and had its disadvantages: confusion to newcomers for whether it or StringHash should be used, and greater potential for hash collisions.

-------------------------

friesencr | 2017-01-02 00:59:46 UTC | #7

Over engineering is slightly contextual to the people writing the code.  I am very greatful Urho has been as aggressive with performance and optimization as it historically.  So you killed a few bees with a bazooka!

-------------------------

