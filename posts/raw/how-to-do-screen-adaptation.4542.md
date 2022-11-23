CaptainCN | 2018-09-17 07:45:00 UTC | #1

![image|690x179](upload://gxeDbsT74Tfjwt4ktsbF8zhk5Ik.png) 
image from godot engine.

-------------------------

Modanung | 2018-09-17 07:45:16 UTC | #2

Could you explain what the displayed option does?

-------------------------

extobias | 2018-09-17 17:57:41 UTC | #3

It's for automatic UI adaptation?

-------------------------

CaptainCN | 2018-09-18 09:33:14 UTC | #4

Sorry. I can't explain  this in English. My English too bad.
just read this doc.

http://docs.godotengine.org/en/3.0/tutorials/viewports/multiple_resolutions.html?highlight=KEEP_WIDTH

-------------------------

jmiller | 2018-09-19 16:03:41 UTC | #5

As maybe a starting point, Urho offers x y render target size multiplier.
  https://urho3d.github.io/documentation/HEAD/_render_paths.html
[code]
    <renderpath>
        <rendertarget name="RTName" tag="TagName" enabled="true|false" cubemap="true|false" size="x y"|sizedivisor="x y"|sizemultiplier="x y"
[/code]

demonstrated by the AutoExposure shader (active in 42_PBRMaterials sample):
  https://github.com/urho3d/Urho3D/blob/master/bin/Data/PostProcess/AutoExposure.xml

-------------------------

