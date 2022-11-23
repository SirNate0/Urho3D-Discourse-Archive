codingmonkey | 2017-01-02 01:01:21 UTC | #1

[url=http://savepic.org/6426555.htm][img]http://savepic.org/6426555m.png[/img][/url]

I create sphere model and paint clouds on it, then export model and convert texture png to dds1.
then i copy skybox.xml material and rename it to skysphere.xml and rewrite in it name of texture to skySphere.dds

in Editor i add skybox component to root of scene, select my SkySphere.mdl and setup material with SkySphere.xml
and in this case it's not drawing anything.

then i inspect material settings and choice Techniques/DiffSkyplane.xml now it's rendered but overrider all objects in scene, it's like a sphere on top of layers in paint program. Then i see other parameter in material editor - "constant bias" and set them to = 1. Now he draws as necessary, but now I feeling that I did something wrong. Is that so?

-------------------------

