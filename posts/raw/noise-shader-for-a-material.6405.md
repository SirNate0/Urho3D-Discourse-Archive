evolgames | 2020-09-29 18:42:54 UTC | #1

So I have a low poly scene. I created a simple texture in gimp using a flat color + rgb noise. Super easy to do. In game it looks great, exactly how I wanted.
![road|128x128](upload://tGXDkJepLFX06l3qoNSnRnYKKsH.jpeg) 
Is it smarter to just use a noise shader for the materials (over top of the diffuse color) instead? Would that be faster or slower than texturing everything (no spec or normal)?
I looked around online but I can't figure out how to set up a noise shader for a material. Is it worth it in terms of performance? If it is, how could I achieve simple rgb noise in .glsl?

Here is the greyscale shader I use (faded in in-game for a certain effect):
```void PS()
{
    vec3 rgb = texture2D(sDiffMap, vScreenPos).rgb;
    float intensity = GetIntensity(rgb)*(1-cGreyness.x);
    vec3 rgb2 = rgb*cGreyness;
    gl_FragColor = vec4(vec3(rgb2+intensity),1);
}
```
For rgb noise, I suppose it would be something similar? Taking a function of gaussian or perlin and passing that output to the fragcolor? Anyone ever do something similar? Also, how can I tell a specific material to use a specific shader?

Of course, if it's better to just use textures I'll do that, but it'd be nice to know how to do this with shaders. Could be useful for things like paper effects.

-------------------------

jmiller | 2020-09-30 03:17:49 UTC | #2

[quote="evolgames, post:1, topic:6405"]
Also, how can I tell a specific material to use a specific shader?
[/quote]

Shaders are specified by the Technique which [Materials](https://urho3d.github.io/documentation/HEAD/_materials.html) (in docs [Related Pages](https://urho3d.github.io/documentation/HEAD/pages.html)) use.

-------------------------

Eugene | 2020-09-30 09:10:28 UTC | #3

[quote="evolgames, post:1, topic:6405"]
Is it smarter to just use a noise shader for the materials (over top of the diffuse color) instead? Would that be faster or slower than texturing everything (no spec or normal)?
[/quote]
The answer depends on your exact implementation, texture sizes and target platforms.
I would cache noise in texture unless I have a good reason not to.

[quote="evolgames, post:1, topic:6405"]
If it is, how could I achieve simple rgb noise in .glsl?
[/quote]
1) Copy-paste existing shader(s) for geometry (LitSolid? Unlit? whatever you use now).
2) Copy-paste noise function from stackoverflow/shadertoy or write your own. Watch for performance!  Noise may be expensive to generate, depending on algorithm and options.
3) Apply noise function somewhere in pixel shader.

-------------------------

evolgames | 2020-09-30 15:45:58 UTC | #4

> I would cache noise in texture unless I have a good reason not to.
> Noise may be expensive to generate, depending on algorithm and options.

Hmm, okay. I definitely don't want to hamper performance if textures work fine for this. They'd be smaller textures too. I'll play around with it though

-------------------------

