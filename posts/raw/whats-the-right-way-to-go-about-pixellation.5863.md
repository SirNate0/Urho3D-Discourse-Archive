evolgames | 2020-02-05 02:02:49 UTC | #1

In some other engines I believe people use post-processing to do pixellated effects. I'm not sure if that's actually the most efficient way to do it, but I'm wondering what the best course is to do this with Urho3d.

I will be dealing with very simple models anyway, so loss of detail will be a part of the art style. Below is what I'm after. I *want* the very jagged aliasing lines.

![Screenshot__35_.0|690x459](upload://d6dWpZjPinjzjNrW7B5RukFecAF.jpeg) 

Either way I'm not sure if I should be looking into post-processing, camera, or resolution settings. How can I achieve this or something similar with Urho3d?

-------------------------

SirNate0 | 2020-02-05 03:19:08 UTC | #2

What I would do is render the scene to a much lower resolution viewport and then scale that up without any filtering (or maybe nearest?) on the texture to the full game resolution. You might need to use a texture render target for that, but it may also be possible through just the render path.

-------------------------

evolgames | 2020-02-05 04:08:55 UTC | #3

I appreciate the help. Okay so with the following I was able to reduce the viewport to something ridiculous.

```
viewport=Viewport:new(scene_, camera)
viewport:SetRect(IntRect(0,0, 80,60))
```

This works except it's now a small resolution box in the corner, to which I'd imagine would be perfect once blown back up.

How do I scale this new resolution up? Do I need a second viewport?

I tried using a renderpath via this:
https://urho3d.github.io/documentation/1.6/_render_paths.html

but the "sizemultiplier" doesn't seem to be the right thing to scale this back up, it only affects what is already sized down.

-------------------------

dertom | 2020-02-05 09:36:28 UTC | #4

As @SirNate0 said, one way to achieve it, is to render it to a rendertexture in low resolution and scale this up to window-size. 
Take the RenderToTexture-Example as base:
https://github.com/urho3d/Urho3D/blob/master/Source/Samples/10_RenderToTexture/RenderToTexture.cpp#L184
(Should be similar in lua) But to be honest I'm not completely sure how to use this rendertexture in the current viewport...

-------------------------

orefkov | 2020-02-05 14:04:32 UTC | #5

Imho, if you want get all scene pixelated, you can just modify renderpath to render all to rendertarget, and add command to end to copy rendertarget to viewport. For example, for forward renderpath:

    <renderpath>
    	<rendertarget name="buffer" sizedivisor="4 4" filter="false"/> 
        <command type="clear" color="fog" depth="1.0" stencil="0" output="buffer"/>
        <command type="scenepass" pass="base" vertexlights="true" metadata="base" output="buffer" />
        <command type="forwardlights" pass="light" output="buffer" />
        <command type="scenepass" pass="postopaque" output="buffer" />
        <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" output="buffer" />
        <command type="scenepass" pass="postalpha" sort="backtofront" output="buffer" />
    	<command type="quad" vs="CopyFramebuffer" ps="CopyFramebuffer" output="viewport">
    		<texture unit="diffuse" name="buffer" />
    	</command>
    </renderpath>

For deffered:

    <renderpath>
    	<rendertarget name="buffer" sizedivisor="4 4" filter="false"/> 
        <rendertarget name="albedo" sizedivisor="4 4" format="rgba" />
        <rendertarget name="normal" sizedivisor="4 4" format="rgba" />
        <rendertarget name="depth" sizedivisor="4 4" format="lineardepth" />
        <command type="clear" color="1 1 1 1" output="depth" />
        <command type="clear" color="fog" depth="1.0" stencil="0" />
        <command type="scenepass" pass="deferred" marktostencil="true" vertexlights="true" metadata="gbuffer">
            <output index="0" name="buffer" />
            <output index="1" name="albedo" />
            <output index="2" name="normal" />
            <output index="3" name="depth" />
        </command>
        <command type="lightvolumes" vs="DeferredLight" ps="DeferredLight" output="buffer">
            <texture unit="albedo" name="albedo" />
            <texture unit="normal" name="normal" />
            <texture unit="depth" name="depth" />
        </command>
        <command type="scenepass" pass="postopaque" output="buffer"/>
        <command type="scenepass" pass="refract" output="buffer">
            <texture unit="environment" name="viewport" />
        </command>
        <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" output="buffer">
            <texture unit="depth" name="depth" />
        </command>
        <command type="scenepass" pass="postalpha" sort="backtofront" output="buffer"/>
    	<command type="quad" vs="CopyFramebuffer" ps="CopyFramebuffer" output="viewport">
    		<texture unit="diffuse" name="buffer" />
    	</command>
    </renderpath>

-------------------------

evolgames | 2020-02-05 14:17:53 UTC | #6

@orefkov, This works great and was super simple to do. For whatever reason, if I combine both of those it freezes up my machine. I'm not sure if that is a separate thing because I'm on an integrated graphics laptop...or maybe I just did it wrong, I'm still a bit of a noob with U3d but I'm getting accustomed to things.

But either way thank you. Using just the second one above, it's almost exactly how I wanted, so I'm satisfied with this and will spend some time learning how this works.

@dertom, that also looks feasible, if anyone is looking for something similar. By changing the resolution on that render, it easily makes things pixellated, while remaining at the same size. However, I guess it would require a few more steps to put that plane on the camera. I think both could work as solutions, but I will be using the below because it is already working. Though I suppose if I want to add a TV screen effect, I would use RenderToTexture to do so.

Thanks to both of you guys for the help!

-------------------------

JTippetts | 2020-02-06 00:11:46 UTC | #7

[quote="evolgames, post:6, topic:5863"]
This works great and was super simple to do. For whatever reason, if I combine both of those it freezes up my machine.
[/quote]

You don't want to use both of those renderpaths. He presented one for Forward rendering and one for the Deferred rendering.

-------------------------

evolgames | 2020-02-06 00:50:18 UTC | #8

@JTippetts Oh okay, well that makes more sense. I'll need to learn more about renderpaths before I understand how they work.

However, it seems the first one doesn't work, then, or at least with my machine. This is the result with the first (it's just garbled up from the file manager behind the window):
![Screenshot-6|690x369, 75%](upload://lGTzFvZtNOmlsQE7tYQ0Z49eiiM.png) 

And here is the second:
![Screenshot-5|690x369, 75%](upload://2YMnvqF59R9b6gNmdRQQT5JawqE.png) 

Who knows. But at least the second one works.

-------------------------

Modanung | 2020-02-06 01:00:51 UTC | #9

Are you using it with a forward render path? (see bin/CoreData/RenderPaths/)

-------------------------

evolgames | 2020-02-06 01:06:14 UTC | #10

@Modanung 
No idea what the difference between them is, or even which I'm doing.
Using the Samples and the above help, this is what I have:

```
viewport=Viewport:new(scene_, camera)
local effectRenderPath = viewport:GetRenderPath():Clone()
effectRenderPath:Append(cache:GetResource("XMLFile", "PostProcess/pixellate2.xml"))
viewport:SetRenderPath(effectRenderPath)
renderer:SetViewport(0, viewport)
```

The pixellate2.xml is simply the above posted by @orefkov that says for deferred. If there is something I'm supposed to do to make these forward or deferred, then I don't know what that is. I've only tested the same thing with each respective renderpath posted above.

-------------------------

Modanung | 2020-02-06 01:16:01 UTC | #11

You could either set the default render path - on the `Renderer` subsystem I believe - or load the render path from XML when creating the viewport (instead of cloning it).

-------------------------

evolgames | 2020-02-06 01:38:43 UTC | #12

I just did this:

```
viewport:SetRenderPath("XMLFile", "RenderPaths/Forward.xml")
local effectRenderPath = viewport:GetRenderPath():Clone()
effectRenderPath:Append(cache:GetResource("XMLFile", "PostProcess/pixellate.xml"))
```

The lua api only lists SetRenderPath under Viewport. I just get the same thing.

-------------------------

orefkov | 2020-02-06 04:16:44 UTC | #13

Do not use Append! It just double render work.
Just create new RenderPath from xml, and set it for viewport.
Forward rendering and Deffered rendering - it is two different methods for rendering, you need choice one from them. See https://urho3d.github.io/documentation/1.7.1/_rendering_modes.html

-------------------------

