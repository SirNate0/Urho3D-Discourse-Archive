SirNate0 | 2017-07-18 17:33:31 UTC | #1

What is the proper way to setup reading the depth buffer in a shader? Searching a little I found this https://discourse.urho3d.io/t/how-xml-rendering-framework-works-to-get-depth/80, so is using another render path required, or is it something that can be set up with just the material, technique a and shader?

-------------------------

Eugene | 2017-07-18 17:46:40 UTC | #2

You mustn't read from and write into buffer simultaneously, this is internal limitation of any hardware.
On the other hand, switching buffer from write to read means two passes in the Urho because depth buffer is something that can't be changed during the pass. I doubt that you can achieve this in any other way.

-------------------------

