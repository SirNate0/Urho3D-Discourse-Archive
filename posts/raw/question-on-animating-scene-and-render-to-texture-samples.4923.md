I3DB | 2019-02-14 15:49:33 UTC | #1

In the render to texture samples, the floating cubes are only visible in the rendered texture but otherwise not visible.

I converted that sample and in my conversion the cubes are always visible, outside the rendered texture and also in the rendered texture.

In comparing what I've done with the code in the sample, not seeing the reason why the render to texture sample only shows cubes in the rendered texture.  One difference, which may explain it, is I only use a single scene, and the sample uses two scenes.

How is it done that cubes are only visible in the rendered texture?

The title includes the sample animating scene, because the cubes are visible both in the sample code and in my conversion. I create the cubes the same way in my converted code, for both samples.

-------------------------

I3DB | 2019-02-14 15:39:34 UTC | #2

![MCS_Photo10-33-00|690x388](upload://cElghg9y8Fg963UbTtSqiMk7oK3.jpeg) 

The sample:
![NOCubes|666x500](upload://kYA3wLlPQNDoXjoMxbTprRTw7D6.png)

-------------------------

I3DB | 2019-02-14 16:56:15 UTC | #3

Yes, the issue was the scene. In the samples. there is a second scene that holds just the cubes and a camera to view them. That scene is rendered to the texture. 

In my sample conversion, I missed that and used a single scene, so all is visible.

Verified, by adding the second scene and then it all works as per the original sample.

The real issue here is my lack of comprehension of scenes. But getting better.

-------------------------

