NessEngine | 2020-04-12 22:23:28 UTC | #1

Hi all,
This post seems long but its mostly pics :) Also you can skip to the end tl;dr, 

**I need a real transparent background, ie actually discarding pixels which are transparent.**

I've seen this topic https://discourse.urho3d.io/t/png-transparent-zones-filled-in-black/503
and I know about the Alpha materials.

But, correct me if I'm wrong, all the alpha materials disable depth write and relay on sorting based on distance from camera. This means that if I try to do a texture fan technique for trees and bushes (putting two sprites on the same position rotated 90 degrees to each other), I get this:
![image|333x500](upload://A1KycnKZ92eYRmQAc0RYtz5ugEU.png) 

In the pic above I recolored one of the sprites so it will be more clear - the more green tree is fully shown, but its supposed to be cut in the middle where the other sprite merge with it. However because they don't depth-write, and that sprite is nearer, I get this weird result. What I want to see, is this:
![image|271x500](upload://lHTlAV4lt5vjlR7IQijJSPjV321.png) 

See how the two tree sprites properly hide each other? This is because I enabled depth write. Looks good on this angle, however, now I'm facing this problem:
![image|271x500](upload://4vNr62aHOVNvdq7ZAFKJcJ6g3ce.png) 

The transparent background of one of the sprites also writes to depth buffer, and hide the other part of the tree (and background). I tried adding alphatest="true", but it didn't work. Here's the technique:

    <technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
        <pass name="alpha" depthwrite="true" alphatest="true" blend="alpha" />
        <pass name="litalpha" depthwrite="true" alphatest="true" blend="addalpha" />
        <pass name="shadow" vs="Shadow" ps="Shadow" />
    </technique>

But it doesn't work for some reason.

**tl;dr** I need a technique that actually discard transparent pixels, so they won't go into the depth buffer when I enable depth write. How?

Thanks!

-------------------------

Eugene | 2020-04-12 22:53:17 UTC | #2

Alpha-techniques are used for *translucency*, not transparency.
If you need only *transparency*, you should use `ALPHAMASK` shader define with standard techniques instead.

-------------------------

NessEngine | 2020-04-12 22:43:08 UTC | #3

Edit: nevermind, found this: https://discourse.urho3d.io/t/problem-on-material-with-alpha-channel/4014

Now it works. Thanks!

-------------------------

