szamq | 2017-01-02 01:04:27 UTC | #1

I have a problem, because I don't know how to setup the cameras and the postprocess effects in order to render in Anaglyph mode.

Things I have done:
- two cameras with offset
- shaders

but I don't know how to stream the viewport to two shaders and then merge them together;
Current design is 
camera1 with viewport on all the screen with postprocess anaglyph red color
camera2 with viewport on all the screen with postprocess anaglyph green blue color;

the shaders are working but I don't know how to split? the viewport form two separate cameras and send the viewport view to different postprocess effect and then merge them together. I hope you understand what I mean.

RenderPath0.Append(cache.GetResource("XMLFile", "PostProcess/AnaglyphL.xml")); //renderpath on left camera (red)
RenderPath1.Append(cache.GetResource("XMLFile", "PostProcess/AnaglyphR.xml")); // remderpath on right camera (blue green) which has some offset

I just don't know how to setup the xml files to have the outputs from two postprocess effect merged(added) together

Thanks for any help.

-------------------------

GoogleBot42 | 2017-01-02 01:04:27 UTC | #2

I am also interested in this if anyone knows how to do it.  :slight_smile:

-------------------------

szamq | 2017-01-02 01:04:27 UTC | #3

Ok I think this topic here [topic756.html](http://discourse.urho3d.io/t/how-to-layer-scenes/740/1) is relevant to my question. I am going to create separate renderpaths, and disable clear pass for the second camera ans set additive blending. Will post my results later(if it will work).

-------------------------

