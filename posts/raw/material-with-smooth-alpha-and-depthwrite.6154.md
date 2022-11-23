Askhento | 2020-05-14 12:42:47 UTC | #1

Hi guys!
I want to make a 3d face with smooth edges. I made a material with DiffUnlitAlpha.xml technique with modified **depthwrite=True.** It was good, until faces (yes many of them) overlapped. Places without texture still write to buffer which cause occlusion.

After searching answered questions I've found this => **psdefine="ALPHAMASK"** which I guess  makes object **"transparent"**. Cool, but what about the edges? Can I make them smooooth? If these options are incompatible, then I need to know that!

tl;dr : is it possible to combine **depthwrite** and **smooth alpha** transition without occlusion?

-------------------------

Eugene | 2020-05-15 13:49:04 UTC | #2

**depthwrite** means that you don't have any guarantees about the data behind the surface of the geometry. Therefore, it is physically impossible to reliably use any form of blending with background for **depthwrite** Material.

> is it possible to combine  **depthwrite**  and  **smooth alpha**  transition without occlusion?

Generally spearking? Yes. In practice? Nope.

**Order-Independent Transparency** requires custom geometry/compute shader that utilizes multiple depth buffers. Urho suports neither.

The only possible workaround for you is Alpha-to-Coverage + MSAA.
If you both enable MSAA xN (globally) and A2C (for material), you can use up to N-1 shades of transparency (excluding 0 and 1) with perfectly working occlusion.

Note that MSAA is not always supported.

-------------------------

Askhento | 2020-05-15 13:48:58 UTC | #3

Ok I see, this is really expensive in my case. I want the edge to be really wide. 
Found [this article](https://medium.com/@bgolus/anti-aliased-alpha-test-the-esoteric-alpha-to-coverage-8b177335ae4f), just in case someone will need info about A2C.
Thank you.

-------------------------

