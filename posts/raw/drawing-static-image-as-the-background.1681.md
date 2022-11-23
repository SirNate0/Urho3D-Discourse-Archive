atai | 2017-01-02 01:09:28 UTC | #1

Hi, what is the best way to render a static image as the background, such that all the other rendering objects appear on top of and cover the background image, but the background image will fill the viewport and show up where no other rendering object exist?  Think this background in the same manner as the static desktop background image, but here this is for the background of a viewport in a  Urho3d rendering area or window

-------------------------

jmiller | 2017-01-02 01:09:28 UTC | #2

You may want to check "Static Background in 3D Scene" thread:
[topic945.html](http://discourse.urho3d.io/t/static-background-in-3d-scene/922/1)

-------------------------

atai | 2017-01-02 01:09:31 UTC | #3

[quote="carnalis"]You may want to check "Static Background in 3D Scene" thread:
[topic945.html](http://discourse.urho3d.io/t/static-background-in-3d-scene/922/1)[/quote]


Thanks.  Using a quad in the rendering path before scene pass works, as suggested in that thread.

-------------------------

sabotage3d | 2017-01-02 01:15:01 UTC | #4

Hey guys can someone share a renderpath example for this?

-------------------------

1vanK | 2017-01-02 01:15:02 UTC | #5

[url=http://savepic.ru/12094484.htm][img]http://savepic.ru/12094484m.png[/img][/url]

Modified Forward.xml:
[code]
<renderpath>
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    
    <!-- Added -->
    <command type="quad" vs="CopyFramebuffer" ps="CopyFramebuffer" output="viewport">
        <texture unit="diffuse" name="Textures/UrhoDecal.dds" />
    </command>
    
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>[/code]

In OpenGL texture is flipped. Also texture is stretched in full screen, so it looks different for 4x3 and 16x9 screens. U need make own shader and fix it.

-------------------------

sabotage3d | 2017-01-02 01:15:02 UTC | #6

Thanks a lot. Works like a charm.

-------------------------

Petryk | 2017-01-02 01:15:40 UTC | #7

Thanks for example of renderpath! Good job! Does anybody know how to create shader with fixing texture issue?

-------------------------

