Enhex | 2017-01-02 01:06:20 UTC | #1

How can you control render order?
A use case for example is an FPS game. You don't want the player's gun to clip with world objects that get too close. So you need to render the gun on top of everything.

-------------------------

cadaver | 2017-01-02 01:06:20 UTC | #2

You control render order with passes. The RenderPath defines the passes that will get rendered, which are assigned in the material's Technique file.

I'm assuming the gun needs to be lit and you're using forward rendering. You could for example add a pass called "basefps" in the Forward.xml renderpath, right after the "base" pass (normal opaque objects)

[code]
<renderpath>
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="scenepass" pass="basefps" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>
[/code]

For the technique, you could copy e.g. Diff.xml to DiffFps.xml and add a "basefps" pass definition with depth test set to "always" (I have intentionally omitted the deferred rendering passes for clarity. Obviously, if you're using deferred rendering, you would need to split the G-buffer pass into a "fps" G-buffer pass instead)

[code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="basefps" depthtest="always" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>
[/code]

This is a bit complex, so I'll look into adding for example a simple 8-bit render priority identifier to materials, which would affect the state sorting normally used by rendering within each pass. After that, the additional pass would not be required.

However, note that render order tweaking isn't troublefree, because shadow rendering will not respect the depth test override, so your gun might appear shadowed when inside a wall. Therefore another approach is to create a second camera & viewport for your firstperson objects, and tweak the view masks in the cameras & objects to make the gun not render in the normal "world" viewport, but only in the "firstperson" viewport. The firstperson viewport will need to have a renderpath definition where the color clear has been disabled.

-------------------------

1vanK | 2017-01-02 01:06:20 UTC | #3

Also see nice fps game [bitbucket.org/cin/outbreak/down ... utbreak.7z](https://bitbucket.org/cin/outbreak/downloads/Outbreak.7z)
[video]http://www.youtube.com/watch?v=pl2qJHTt5sY[/video]

-------------------------

cadaver | 2017-01-02 01:06:20 UTC | #4

In master branch, a 8-bit render order specifier has been added to materials (Material::SetRenderOrder()). This allows to override both state & distance sorting within a pass: default order value is 128 and smaller values render first, larger values render later.

Meaning that you could do the FPS gun by setting the gun material's renderOrder to e.g. 129. You still need to touch the technique for disabling depth test.

-------------------------

1vanK | 2017-01-02 01:09:04 UTC | #5

> your gun might appear shadowed when inside a wall

It is very noticeable :(

> Therefore another approach is to create a second camera & viewport for your firstperson objects, and tweak the view masks in the cameras & objects to make the gun not render in the normal "world" viewport, but only in the "firstperson" viewport.

Then shadows will not fall on the weapon at all. The hero enters the room, but a weapon will be lit as outdoors by the sun. Are there any other solution?

-------------------------

Enhex | 2019-06-30 11:14:31 UTC | #6

[quote="cadaver"]
In master branch, a 8-bit render order specifier has been added to materials (Material::SetRenderOrder()). This allows to override both state & distance sorting within a pass: default order value is 128 and smaller values render first, larger values render later.

Meaning that you could do the FPS gun by setting the gun material's renderOrder to e.g. 129. You still need to touch the technique for disabling depth test.
[/quote]

Material render order doesn't seem to work. I've tried using it in the character demo, in CharacterDemo::CreateCharacter():
[code]
object->SetModel(cache->GetResource<Model>("Models/Jack.mdl"));

auto mat = cache->GetResource<Material>("Materials/Jack.xml")->Clone();
mat->SetRenderOrder(200);	// higher render order
auto tec = mat->GetTechnique(0)->Clone();
tec->GetPass(0)->SetDepthTestMode(CMP_ALWAYS);	// Always pass depth test
mat->SetTechnique(0, tec);

object->SetMaterial(mat);
[/code]

-------------------------

gawag | 2017-01-02 01:10:37 UTC | #7

Is there no z-offset like in many other systems?

-------------------------

Enhex | 2017-01-02 01:10:37 UTC | #8

Using an extra pass with depth test always doesn't work well in cases that triangles are overlapping.
It needs to use some sort of local depth testing.

-------------------------

gawag | 2017-01-02 01:10:37 UTC | #9

Aha! I found something!
I tested a custom shader and when modifying the vertex shader there can be a z-offset.
In a HLSL (DirectX) shader:
[code]
...
void VS(...)
{
...
    oPos = GetClipPos(worldPos);
    // when inserting this:
    oPos.z*=0.999;
...
[/code]
This material of the ground is slightly in front of other materials: [i.imgur.com/6Y9R7Tk.jpg](http://i.imgur.com/6Y9R7Tk.jpg)
The player, torch and the rocks appear cut off because the ground behind them is partly rendered in front. The shadows and lighting seem to be still correct.
Try modifying the shader of your weapon material(s) like this and it could work as you want. Instead of multiplying you could also try subtracting.

In a GLSL (OpenGL) shader the code could be similar but I can't test that without rebuilding Urho:
[code]
...
    // also in the vertex shader VS()
    gl_Position = GetClipPos(worldPos);  // the line is identical but the variable has a different name. Could be the default name used in the Urho shader
    gl_Position.z*=0.999;
...
[/code]

Does that work as expected?

-------------------------

Enhex | 2017-01-02 01:10:38 UTC | #10

It sounds like a brittle solution.
What if a player in an FPS game stands next to a wall, and the weapon is longer than the distance from the wall? You won't have any z margin to offset.

-------------------------

gawag | 2019-06-30 11:14:03 UTC | #11

? I don't know what you mean by that.
I tested it again:
Without any offset: [i.imgur.com/FJouvSX.jpg](http://i.imgur.com/FJouvSX.jpg)
The blocks with the dots with oPos.z*=0.01;: [i.imgur.com/eXYWiHR.jpg](http://i.imgur.com/eXYWiHR.jpg)
They are quite far away behind the player and torch. They are rendered in front as intended. Also the shadows are still all correct, they throw and receive shadows as without any offset.
The Z distance is still calculated and compared but it seems I correctly manipulated it to change it artificially. I'm not sure if I did everything correct but it looks fine for me (have only checked DirectX9 though).

-------------------------

codingmonkey | 2019-06-30 11:13:45 UTC | #12

>player in an FPS game stands next to a wall, and the weapon is longer than the distance from the wall?

Earlier I have read some relative topic about gun & shadows on gamedev ([gamedev.ru/code/forum/?id=211365](http://www.gamedev.ru/code/forum/?id=211365))
there some code example for "depth hack" that uses in doom3 I guess

[code]
void Camera::EnterDepthHack( float depth ) {
    // store initial matrix
    if( !mInDepthHack ) {
        mDepthHackMatrix = mProjection;
    }
    mInDepthHack = true;
    // modify matrix
    mProjection._43 -= depth;
}

void Camera::LeaveDepthHack() {
    // restore matrix
    mInDepthHack = false;
    mProjection = mDepthHackMatrix;
}
[/code]

using:

[code]
if( needOverlay ) {
  camera->EnterDepthHack( depth );
}
node->Draw( camera );
if( needOverlay ) {
  camera->LeaveDepthHack();
}
[/code]

-------------------------

gawag | 2017-01-02 01:10:38 UTC | #13

Not sure how that would work in Urho. It seems to be also offsetting the depth, then rendering the things that should be in front and then restoring the "normal depth mode" and rendering the rest. I guess that would require an additional rendering pass/step or something?
My solution works simply on a shader level. Everything using that shader has the offset. The offset could also be changed on a material level by making the offset a shader parameter: [urho3d.wikia.com/wiki/Custom_shader_parameters](http://urho3d.wikia.com/wiki/Custom_shader_parameters)

-------------------------

Enhex | 2017-01-02 01:10:38 UTC | #14

I'm using the extra viewport & camera solution, which works.
Is there a way to have world shadows with it? At least the directional light's shadow?

-------------------------

gawag | 2019-06-30 11:12:43 UTC | #15

Works perfectly with my solution. It could also have a better performance.

-------------------------

Enhex | 2017-01-02 01:10:39 UTC | #16

[quote="gawag"]Works perfectly with my solution. It could also have a better performance.[/quote]
But it isn't suitable for FPS game.

It would be more elegant to use render order, but it doesn't seem to work right now.

-------------------------

gawag | 2019-06-30 11:13:10 UTC | #17

[quote="Enhex"]
But it isn't suitable for FPS game.
[/quote]
Ha, I was going to write "Why wouldn't it?" and post picture of proof that it works. Uhm...
3rd person view without offset: [i.imgur.com/MQx606M.jpg](http://i.imgur.com/MQx606M.jpg) The torch (marked with blue) is attached to the player and properly casts shadows.
1st person view without offset: [i.imgur.com/IaMwzkW.jpg](http://i.imgur.com/IaMwzkW.jpg) Torch logically disappears in the rock.
3rd person view with offset of *=0.01: [i.imgur.com/Ei7uqCR.jpg](http://i.imgur.com/Ei7uqCR.jpg) Torch still properly casting and receiving shadows and layered in front of the player.
1st person view with offset: [i.imgur.com/Vo4svN3.jpg](http://i.imgur.com/Vo4svN3.jpg)
Ah snap! Torch is properly in front but shadowed from the rock it is in. I guess that's not good enough. It works though, kinda.

One could disable shadow receiving for the model but then it's not receiving [b]any[/b] shadows. One would need some kind of shadow receive offset. Only receive shadows of models under certain conditions. It would to be shadowed when on the shadowed side of the model it is in and not shadowed when on the lit side. Not sure if that could be done.

-------------------------

Enhex | 2017-01-02 01:10:41 UTC | #18

Ah so it doesn't go behind the camera? Nice.

-------------------------

weitjong | 2017-01-02 01:10:42 UTC | #19

If you are using OpenGL, may be you could use glDepthRange() to specify different depth range  between world objects and your weapon such that your weapon always has the preferred z.

-------------------------

Enhex | 2017-01-02 01:10:43 UTC | #20

I rather have the possibility of shadows on the weapon when clipping, than not being able to use shadows at all. I noticed Battlefield 3 has this behavior too.
Z-offset seems like the way to achieve this behavior. I want to know and specify how much offset is needed (perhaps the total bounding box of all the viewport models).
I wonder if codingmonkey's method can work with urho, and what it takes to implement it?

[quote="weitjong"]If you are using OpenGL, may be you could use glDepthRange() to specify different depth range  between world objects and your weapon such that your weapon always has the preferred z.[/quote]
How does it compare to depth offset? It would make z-fighting more likely?
Is it possible to add it without modifying Urho?


EDIT:
gawag's solution actually works quite well. Multiplying the Z value by a positive fraction "squishes" the model to fit. Calling it "depth offset" made me think it was translation backwards instead of scaling.
This solution is very efficient but there's a limit. Basically it's depth scaling the weapon to fit inside the character controller's rigid body's range. That means that theoretically if you have a very long model and/or a very short character rigid body, at some point you won't have enough precision to scale the depth to fit in without z-fighting.
Also if something can go past the character's rigid body it will intersect with the weapon.

-------------------------

hunkalloc | 2022-11-16 04:57:57 UTC | #21

Is this still an issue? Or is there a way of handling render order?

-------------------------

