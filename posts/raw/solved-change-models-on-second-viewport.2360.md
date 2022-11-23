Marcin | 2017-01-02 01:14:58 UTC | #1

Hey all!
I just starting to know Urho3d. I have a problem. Could You please help me - how to modify the example code No. 9 (09_MultipleViewports) so that the rearViewport have:
- Mushrooms not visible (not rendered);
- The light had different parameters (example other direction, more brightness);
- Cubes (boxes) have a different material;
Of course, the main viewport should be unchanged. Please help me and give an example of how to do it.

Thanks in advance!
Marcin

-------------------------

1vanK | 2017-01-02 01:14:58 UTC | #2

> Mushrooms not visible (not rendered);
viewMask

> The light had different parameters (example other direction, more brightness);
> Cubes (boxes) have a different material;

make another scene

-------------------------

jmiller | 2017-01-02 01:14:58 UTC | #3

Hi Marcin, and welcome to the forums.  :slight_smile: 

To make the sample work like that should be some minor changes as [b]1vank[/b] describes.
As you work through the code (either AngelScript or C++ version) and check the comments, you should get a picture of how things fit together.

We can find a scattering of related posts..
[google.com/search?q=viewmas ... ophpbb.com](https://www.google.com/search?q=viewmask+site%3Aurho3d.prophpbb.com)
[discourse.urho3d.io/t/how-to-layer-scenes/740/1](http://discourse.urho3d.io/t/how-to-layer-scenes/740/1)

Let us know how it's working out.

-------------------------

Marcin | 2017-01-02 01:14:59 UTC | #4

Tank You very much. For now I checked viewmask, it works correctly. Using the viewmask I can even turn off the light and turn on the other light for the second viewport. 
Is there a documentation for 'renderpath' how does it work and what parameters can I set?

I have another question, I noticed that if I use the material without Emissive techniques (eg. DiffNormalSpec.xml), but I set parameter Emissive in this material (eg. <Parameter name = "MatEmissiveColor" value = "1.0 0 0 1" />) then anyway the object emits Glow / Bloom. Is this a correct action?

-------------------------

Eugene | 2017-01-02 01:14:59 UTC | #5

[quote="Marcin"]
I have another question, I noticed that if I use the material without Emissive techniques (eg. DiffNormalSpec.xml), but I set parameter Emissive in this material (eg. <Parameter name = "MatEmissiveColor" value = "1.0 0 0 1" />) then anyway the object emits Glow / Bloom. Is this a correct action?[/quote]
EMISSIVE shader define (and correspondingly tagged techniques) have the same idea as DIFFMAP, NORMALMAP or SPECMAP tags: they turn on/off input textures.

-------------------------

jmiller | 2017-01-02 01:15:00 UTC | #6

[quote="Marcin"]Tank You very much. For now I checked viewmask, it works correctly. Using the viewmask I can even turn off the light and turn on the other light for the second viewport. 
Is there a documentation for 'renderpath' how does it work and what parameters can I set?[/quote]

For HEAD revision of Urho3D:
[urho3d.github.io/documentation/ ... paths.html](https://urho3d.github.io/documentation/HEAD/_render_paths.html)

This is found in the "Related Pages" section from the index page at [urho3d.github.io/documentation/HEAD/index.html](https://urho3d.github.io/documentation/HEAD/index.html)

-------------------------

