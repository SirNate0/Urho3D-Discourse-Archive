Dave82 | 2017-01-02 01:11:53 UTC | #1

Hi ! I if understand correctly , to have proper shadows casted on transparent meshes we can't reuse shadow maps.Thats odd since some parts of my levels use 6 lights + a flashlight and a muzzle flash light. Thats 8 lights with resolution of 2048 each...so far i didn't experienced big slowdowns but i think thats way too much texture usage. I could limit the max shadow maps but that's makes it even worst the engine tries to use the closest lights and cull the other , so as you move in the scene the lights keep popping in and out.

Are there any ideas/plans to optimize this ?

-------------------------

cadaver | 2017-01-02 01:11:53 UTC | #2

The relevant function is Renderer::GetShadowMap().

Checking its implementation, it's quite crude. It simply tries to get a shadowmap of the light's requested resolution, and if it can't (because allocation count is exceeded) it returns 0, which converts the light to unshadowed. So it doesn't fallback to smaller resolutions, which it probably should do. Also the number of shadowmaps per resolution is one variable, while it should rather allow more of smaller shadowmaps.

The light shadowmaps are allocated in camera distance order (nearest first.)

If you want to improve the logic and make a PR, it would be most welcome. I will probably get to this at some point too.

-------------------------

Dave82 | 2017-01-02 01:11:55 UTC | #3

Thanks cadaver ! Well , for now i will go with smaller shadow maps (perhaps 1024's) , and will try to find a solution in the meantime

-------------------------

