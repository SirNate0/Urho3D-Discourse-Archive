darkirk | 2017-06-16 18:43:39 UTC | #1

I'm trying to use the PBR pipeline in Urho but i'm a little confused about the current implementation. It seems that the Skybox lighting information is not used at all. Do i have to create it in a special way? 

I'm trying to use this HDRI skies: https://www.viz-people.com/portfolio/free-hdri-maps/

I've created a Skydome, but i don't think that Urho supports reading info from that since it acts just like a normal mesh. Then i converted my panoramic HDRI to a cubemap and applied that to the skybox, but no lighting information at all. Can someone help me with this?

-------------------------

dragonCASTjosh | 2017-06-16 01:20:00 UTC | #2

You will need to place down a zone in the level. This works like a reflection probe, once you generate a cubemap it should work. I recommend you filter the cubemap in something like CMFT before using it so it samples correctly at higher roughness values

-------------------------

darkirk | 2017-06-16 01:52:03 UTC | #3

Like a postprocessing zone covering whatever is inside the skydome? Does it need a special name or something?

-------------------------

Modanung | 2017-06-19 14:02:50 UTC | #4

In case of the PBRExample this `Zone` component is loaded with the scene:
https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scenes/PBRExample.xml#L731-L744

-------------------------

darkirk | 2017-06-16 19:47:16 UTC | #5

What are the possible values of the zone texture? Always a cubemap?

-------------------------

dragonCASTjosh | 2017-06-17 02:11:48 UTC | #6

Currently it has to be a cubemap to work with PBR

-------------------------

darkirk | 2017-06-18 18:32:31 UTC | #7

Thank you for the info!

-------------------------

