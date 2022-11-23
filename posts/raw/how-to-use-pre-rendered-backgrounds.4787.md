Dave82 | 2019-01-01 16:01:51 UTC | #1

Hi , after struggling with SSAO and/or Rendering static lightmaps (which are extremely tedious work btw) and since PBR doesn't seem to gain any attention lately (i tried the sample from 1.7 but ran about 5-10 fps and my GPU fan go crazy although i have mounted a 2x larger fan on the heat sink) So i decided to dive into pre rendered backgrounds. I have 3 ideas so far but actually the best solutions would be the 1st or the 3rd if is even possible.

1.Since I already have the pre-rendered diffuse map and a 32 bit depth map rendered in 3ds max so i thought it would be the easiest soulution to use one texture unit for PreRenderedDepth and simply discard pixels which are behind depth at that point. This is most likely doable unfortunately engine wise i don't know how compicated would it be.

2. Render occluders to depth map is the easiest way to do this since the engine takes care of rendering orders and stuff but then it requires extreme ammount of work on modelling side sice i have to model everything twice. A low poly occluder mesh and the high poly scene. Doable but only if no other solution pops up

3. Is there any way of simply use a custom depth map ? Something like : 
   1. Render background 
   2. Set a custom depth map 
   3, Render scene objects

Any ideas appreciated.

-------------------------

Dave82 | 2019-01-03 02:40:37 UTC | #2

Ok it seems i am making progress. I am able to render backgrounds  and looks great but the depth still doesn't work...
I found out there is a TU_DEPTHBUFFER texture unit. What this does exactly ? I tried to bind my prerendered depth map to this unit but it seems it does nothing.

-------------------------

Dave82 | 2019-01-06 17:25:24 UTC | #3

Can't find a solution. I either render something on the screen including depth or render nothing.
Unfortunately to come up with some idea it would require a really good understanding of Urho's renderpath/technique/material structures. So for now i will just work without depth maps...
The most logical way would be :

1.Render the flat backround texture on a quad with a custom depth information (pre rendered depth)
2. Render everything else.

I just have no idea how to do this... I found some half informations , old documentations on the site which made the material system more confusing,
:(

-------------------------

