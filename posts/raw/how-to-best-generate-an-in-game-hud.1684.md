valera_rozuvan | 2017-01-02 01:09:28 UTC | #1

In many games a HUD is always visible on the screen and shows valuable information about the game state, player's vehicle, etc. For example take a look at:

[img]https://raw.githubusercontent.com/valera-rozuvan/stuff/master/images/HUD_3B_A__x640.png[/img]
source: [url]https://github.com/valera-rozuvan/stuff/blob/master/images/HUD_3B_A__x640.png[/url]
original: [url]http://www.mellottsvrpage.com/wp-content/uploads/2014/12/HUD_3B_A.png[/url]

How to best implement this?

1.) Redraw a 2D scene (the HUD) and then overlay it on top of the 3D view.
2.) Create two 3D scenes (i.e. the HUD will be a 3D object), and then layer the scenes (as described here [post4166.html?hilit=2d%20overlay](http://discourse.urho3d.io/t/how-to-layer-scenes/740/4%20overlay) ).
3.) Or maybe a totally different approach?

Any help, or suggestions will be appreciated!

-------------------------

thebluefish | 2017-01-02 01:09:28 UTC | #2

Typically the UI subsystem would handle this sort of stuff, and is the "default" way to do a HUD/GUI. With a little bit of hax (or maybe this has some official support now), you can do RTT with UI to have HUD elements in 3D space.

If you're going for something akin to Elite Dangerous, you'd just want a sub-node in the scene to contain all of your HUD elements. Changes in the rendering order could be made, but generally you wouldn't need to if everything's already in a 3D space. A 2D quad with some shader tricks could make for some easy, yet powerful elements.

Urho2D wouldn't be up for the challenge with something like this, unfortunately, unless you layered two scenes as you've described. I couldn't recommend layering 2 scenes because honestly there needs to be better 2D support anyways due to having no control over the position in 3D space (z-axis is all but useless.) It would work for a decent work-around, but a long-term solution would be rethinking 2D elements in a 3D scene altogether.

-------------------------

Enhex | 2017-01-02 01:09:28 UTC | #3

You can use Render To Texture (see sample #10) with a UI BorderImage or Sprite.
You probably want to render it with transparent background too.

Example for a RenderPath that does that, using a transparent clear color:
ForwardDepthTransparent.xml
[code]<renderpath>
    <rendertarget name="depth" sizedivisor="1 1" format="lineardepth" />
    <command type="clear" color="1 1 1 1" depth="1.0" output="depth" />
    <command type="scenepass" pass="depth" output="depth" />
    <command type="clear" color="0 0 0 0" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>[/code]

Another option is to render it as an overlay after the scene has been rendered.

-------------------------

