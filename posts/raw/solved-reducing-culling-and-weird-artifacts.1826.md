vivienneanthony | 2017-01-02 01:10:28 UTC | #1

Hi

I'm trying to improve the quality. I'm noticing a few issues with the scene in the client. As you see in the editor the station shows up fine and okay in the game camera view. Now when its loaded in the client which uses the game camera.

It seems the plating mesh is mixed with the station mesh in calculation creating weird artifacts. The culling is set at CWW. I even tried it as max. [imgur.com/a/cdwkT](http://imgur.com/a/cdwkT)

The quality is set at Simple 24bit
Texture and material quality at 2.
Also CCW or CCW for the materials and camera.

Viv

-------------------------

vivienneanthony | 2017-01-02 01:10:33 UTC | #2

Solution was simple, thanks for the help.

[youtube.com/watch?v=ihlQi-27Ud0](https://www.youtube.com/watch?v=ihlQi-27Ud0)

-------------------------

yushli | 2017-01-02 01:10:34 UTC | #3

Would you like to share the solution? I didn't figure that out. Thank you.

-------------------------

vivienneanthony | 2017-01-02 01:10:34 UTC | #4

[quote="yushli"]Would you like to share the solution? I didn't figure that out. Thank you.[/quote]

[code]
<carnalis> i think adjusting camera nearclip should affect z-buffering a bit, and probably reveal if that is an issue.
<viviennea> looking
<viviennea> I'm going set a near clip and see whtat happens
<viviennea> That actually helped.
<viviennea> http://imgur.com/Bj8dsb9
<carnalis> urho uses a traditional depth buffer and much of the z-space is used near the camera, so setting a nearclip as far as possible helps. limiting farclip should help a bit too
[/code]

I had to set the near clip to a decent number like 1.0. For some reason the camera couldn't figure the depth correct with no near clip.

-------------------------

yushli | 2017-01-02 01:10:35 UTC | #5

Nice trick. Thank you for sharing this.

-------------------------

