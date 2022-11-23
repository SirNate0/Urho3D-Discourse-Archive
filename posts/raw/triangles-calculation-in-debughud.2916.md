Marcin | 2017-03-17 13:07:12 UTC | #1

Hi,
How triangles are counted in DebugHud? I see that I have counted about 8 times more than it is in models. What could be the reason for this surplus?

-------------------------

Eugene | 2017-03-17 13:28:35 UTC | #2

More info, plz. Shadows, viewports, text, anything.
E.g. screenshot of Uhro window.

-------------------------

KonstantTom | 2017-03-17 16:13:04 UTC | #3

I found same problem some time ago. DebugHud always add its text triangles to summary triangles count. It adds about 10000 triangles if DebugHud is in DEBUGHUD_SHOW_ALL mode.

-------------------------

UrhoIsTheBest | 2020-06-12 05:58:59 UTC | #5

Sorry to reply this old post.
I am having the same question.

I have two terrains, each is constructed by a 65*65 heightmap.
So for each terrain, I expect 64 * 64 * 2 = 8192 triangles. Total would be **~16,000 triangles.**
But I am seeing **61,559 triangles instead,** about **4 times more**!

Attached two screenshots.

Overview
![image|663x500](upload://oWipRPX44cWHbVsPTRGQX8YJ1gx.png) 

Zoom In (you can count the size manually)
![image|663x500](upload://u1uY7MV1TFL4GVF7Hq4DO3y2h1z.png)

-------------------------

Valdar | 2020-06-15 01:23:10 UTC | #6

It looks to me that you have 64 x 64 **quads** per height map, so 128 x 128 triangles x 2. That puts you at ~33k. The rest is apparently taken up by the HUD text and logo.

-------------------------

UrhoIsTheBest | 2020-06-15 05:55:03 UTC | #7

Correct me if I am wrong, but **1 quad = 2 triangles**, so 64 x 64 **quads** = 64 * 64 * 2 = 8192 triangles. Two terrains make it into **~16k**. I think you double counted it.
Even by your calculation, the logo and HUD is making up the rest ~30k triangles which does not make any sense to me?

-------------------------

UrhoIsTheBest | 2020-06-15 06:10:43 UTC | #8

I did a simple test, just rotate the camera to the background and no terrain showing.
The base count of triangles **~11k**.
This agrees with @ [KonstantTom](/u/KonstantTom)'s result
![image|661x500](upload://YJl5FNkKzO4kSFNJ2yXwFqrSLc.png)

-------------------------

Valdar | 2020-06-15 06:32:27 UTC | #9

My bad. I misread your post and didn't see that you multiplied by 2 before doubling (and yeah, if counting the triangles across, my formula should have been 128 x **64** x 2 = ~16K).

So, I did a test with an empty scene and got ~12k tris. Then I threw a model in and got 97k tris. However, that model in Blender is only 28k Tris... So, it looks like something **is** wrong. I never questioned it before :)

-------------------------

UrhoIsTheBest | 2020-06-15 06:55:19 UTC | #10

That's interesting.
So basically for my case, 
*the display triangles / real triagnels = (62k - 12k) / 16k ~ 3 times;* 
For your case, 
*the display triangles / real triagnels = (97k - 12k) / 28k ~ 3 times;* 

A quick guess would be the calculation counted **vertices** instead of **triangles**.

But I took a quick look at the source code, could not find anything suspicious. For example, in ```D3D11Graphics.cpp``` or ```OGLGraphics.cpp```, we can get the ```primitiveCount``` number.
```
static void GetD3DPrimitiveType(unsigned elementCount, PrimitiveType type, unsigned& primitiveCount,
    D3D_PRIMITIVE_TOPOLOGY& d3dPrimitiveType)
{
    switch (type)
    {
    case TRIANGLE_LIST:
        primitiveCount = elementCount / 3;
        d3dPrimitiveType = D3D_PRIMITIVE_TOPOLOGY_TRIANGLELIST;
        break;

    ...
    }
}
```

Anyway, I believe it should be just a mis-count somewhere, not mistakenly rendering more triangles than we need. So it should not impact the performance.

-------------------------

cadaver | 2020-06-15 09:03:45 UTC | #11

Note that in forward rendering, each per-pixel light will re-render the affected geometry. If you have an unlit scene there should be just a single pass.

For shadowed lights, there will be also shadow map pass, which renders even more triangles.

-------------------------

UrhoIsTheBest | 2020-06-19 00:12:35 UTC | #12

Ah! That explains it!
I do have 3 lights in the scene.
When I leave only one light there, the total triangle count is ~28k, exactly 16k + base 12k.
![image|657x500](upload://4va4atkk5QsPYfVq7UWacn95jBq.jpeg) 

Thanks so much for pointing this out ! Lasse!
I am still learning all those computer graphics rendering techniques. I am writing a custom terrain class to dynamically create/destroy patches for a super large world.

-------------------------

