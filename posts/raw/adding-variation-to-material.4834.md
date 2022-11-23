smellymumbler | 2019-01-18 20:44:18 UTC | #1

Does anyone have any idea on how to do something like this?

https://www.chrisalbeluhn.com/ut3-adding-variation-to-a-repeating-texture-pattern

-------------------------

JTippetts | 2019-01-18 21:55:38 UTC | #2

A quick overview indicates that they are doing the trick of sampling a texture twice, with different UV scales for each sample, then combining them together. It looks like they sample the floor texture at normal UV and at UV * 4, then multiply again by an arbitrarily-chosen color to try to correct the color which is altered by the multiplication. This technique was discussed somewhat in the old [Unreal Engine document](https://api.unrealengine.com/udk/Three/TerrainAdvancedTextures.html#Multi-UV%20Mixing:%20Reducing%20tiling%20through%20scalar%20mixing) about terrain texturing as the Multi-UV mixing technique.

After multi-UV mixing, they then sample another texture, multiply it against the previous result, then they mix this multiply result with the original UV-mixed sample with a mix factor of 0.5

Note that multiplying a texture sample by itself has a tendency to increase the saturation and can potentially reduce the brightness of a texture, hence the constant-color multiplication your linked article performs. Also, while UV-mixing can reduce the occurrence of local repeating patterns, repetition still exists at the level of the larger-scale UV sampling. One way of getting around the color-changing issue is to lerp/mix the multi-UV scale samples, rather than multiply them. For example, here is a texture mult-sampled at 1x and 4x scales then multiplied:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/b/b8105d03ea01fe6fa1a959f984b9d305217a24c3.png'>

Top left quarter is the base texture at UVx1, top right is UVx4, and bottom half is the result of multiplying them.

Now, here is the same texture with a 1/2 mix rather than a multiply:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/0/0b41d06ad1723d1ca3d0e4e2d3d93b8d355ade33.png'>

You can see that this method preserves the overall coloration of the source texture. This is the method that I perform in my terrain editor; you can see some of the results [here](https://discourse.urho3d.io/t/u3d-terrain-editor/765/81). If you choose the scale of your larger UV sample carefully, you can use this trick to hide repetition; just be aware that repetition still exists at that larger scale.

-------------------------

Leith | 2019-01-19 05:51:11 UTC | #3

[Repetition still exists at that larger scale] It sure does, I used similar tricks in a realtime terrain painting demo, where you could choose the weights and textures on your brush, but could not avoid the fact that I was still tiling textures in a regular way across the terrain

-------------------------

smellymumbler | 2019-01-21 16:36:49 UTC | #4

That was a very detailed answer, @JTippetts! Thank you so much for the attention and sharing the knowledge.

-------------------------

