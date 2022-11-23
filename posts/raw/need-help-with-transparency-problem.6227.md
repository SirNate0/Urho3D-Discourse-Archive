btschumy | 2020-06-25 15:04:00 UTC | #1

I'm, having a problem with transparent regions in my texture being drawn in black rather than being clear.

The main object in my scene is a plane with a texture of an image of the galaxy.  To illustrate the problem I have another plane with a solid color oriented at right angles to galaxy plane.  Here is the galaxy technique:

```
<technique vs="Unlit" ps="Unlit" psdefines="DIFFMAP">
    <pass name="alpha" depthwrite="true" blend="alpha" />
</technique>
```

Here is the plane's technique:

```
<technique vs="Unlit" ps="Unlit" psdefines="DIFFMAP">
    <pass name="alpha" depthwrite="false" blend="alpha" />
</technique>
```

If the galaxy is rendered *before* the plane (which is what I require) then the transparent regions are drawn black.

![8E76111B-8EAB-43FC-B224-A80C67D0C4B1_1_105_c|666x500](upload://uJsZrOJaR38QhHlUEyjWTFczf2S.jpeg) 

If I change the rendering order so that the galaxy is drawn *after* the plane, the alpha looks correct.

![07707A68-5846-450B-A247-E4BCC0C5CF11_1_105_c|666x500](upload://afDouSyeoYwhVk6PcGAdGZ60kQc.jpeg) 

Changing the plane to write to the depth buffer doesn't help.  

In my initial attempts to illustrate the problem, I tried changing the scene's background color to something other than black using this code I found on the web.

        //Set a background color
        unsafe
        {
            RenderPath rp = vp.RenderPath;
            for (uint i = 0; i < rp.NumCommands; i++)
            {
                RenderPathCommand* cmd = rp.GetCommand(i);
                cmd->UseFogColor = 0;
                cmd->ClearColor = new Color(1.0f, 0.0f, 0.0f, 1);

            }
        }

This does change the background color to red but the transparent corners of the image are also drawn as red now.  It seems the transparent region is filled with the ClearColor.  I tries making the ClearColor transparent, but that doesn't work either.

Is this a bug in the system, or am I just misunderstanding something?

-------------------------

SirNate0 | 2020-06-27 00:06:42 UTC | #2

I believe that is the expected behavior - if you tell it to write to the depth buffer with the normal alpha setup I'm pretty sure it will write the whole plane the image is on to the buffer, so you'll end up with black for the rest of it from the clear/fog color presumably. The cream colored plane is then behind the galaxy and it doesn't show up except where it is in front of the galaxy, which has written to the depth buffer. If you draw the cream colored plane first then the galaxy always passes the depth test and blends with the plane behind it as you would expect.

I think you're misunderstanding might be about how the transparency works. It's all fake transparency (with the possible exception of alpha=0 pixels). All of the rendering is like painting - you add more and more layers to the image, but you can never insert a layer between the layers later. Transparency is an illusion created by choosing the appropriate color that blends between the existing color at the pixel and the new color based on alpha. Hance, you always have to draw the transparent object after the "background".

-------------------------

btschumy | 2020-06-29 17:02:29 UTC | #3

SirNate,

You are correct that I'm misunderstanding how transparency works in Urho3D.  My only other experience with 3D rendering is Apple's SceneKit.  With that I never had any issues with transparency not really being transparent.  SceneKit also does not seem to expose the concept of depthwrite so I never had to decide if it was true or false (I assume it was always true).  Things just worked.

In SceneKit I would set the rendering order of the galaxy plane to 128 and the bulge node to 129.  There was never an issue of the "transparent" corners being visible agains the bulge.

I've been playing around with (I think) all possible combinations of the rendering orders and whether depthwrite is true of false and I can't find anything that renders the bulge embedded in the galaxy correctly.  I'm going to be having many nodes with transparency so I need to know how I can get this to work.  Surely it is possible.

It seems I must render the galaxy first with depthwrite = true and the draw the bulge to get the bulge to appear bisected by the galactic plane.  However, this alway causes the corners to appear black against the bulge.

I would think what I'm trying to do is not uncommon, so I must be missing something obvious.  Any advice?

-------------------------

btschumy | 2020-07-01 18:20:51 UTC | #4

SirNate (and others),

Based upon a suggestion you made in another thread of mine several weeks ago I took another stab at this.  My galactic bulge and the deep sky objects (star clusters, galaxies, etc) and all managed using  BillboardSets.  They seem really efficient.  I would divide this objects into sets for the north galactic hemisphere and the south galactic hemisphere.  If the camera was in the north hemisphere looking down on the galaxy, I'd dra the southern objects first, then the galaxy, then the northern objects.  This does make the transparent corners of the galaxy image work correctly.  I now see the southern objects that were previously hidden by the black corners of the galaxy image.

However, I don't think this will work in general.  Some of the billboards, even though small,  will end up spanning the two hemispheres.  So the corners of the billboard will look correct in one hemisphere, I will see black corners in the side the stick into the other hemisphere.

As I mentioned before, with Apple's SceneKit, this all just worked.  Are you absolutely sure there there is not some option to enable in Urho3D to make this work?  I would think that it would be possible to draw the galaxy first and then the output buffer would remember what pixels are transparent.  So when I later draw the other objects, the ones behind the transparent corners would show thorough.

If this is really the only way Urho3D can work, then I may have to abandon it.  Is this the way all OpenGL systems work or might I have better luck with a different framework?

I was really hoping to may this an cross-platform product (not just Apple), but it may not be feasible.

Thanks for any help you can provide.

Bill

-------------------------

SirNate0 | 2020-07-01 18:54:04 UTC | #5

I don't remember if it's been suggested yet, but try adding `<shader psdefines="ALPHAMASK" />` to your Galaxy material. (The UrhoDecalAlphaMaskTwoSided.xml material uses it if you need to see where to add it). That should discard the corners of the Galaxy while leaving the fully opaque disk. Anything that would otherwise be "behind" those corners will still be drawn in that case. If you want all objects to be drawn like this, remove the `#ifdef ALPHAMASK` and `endif` from the check in Unlit.glsl, though that will also make it impossible to have a visible alpha < 0.5 and there's also a chance it could slow down rendering in general (I assume that's why the `discard;` is behind the `#ifdef`, and hence I don't recommend doing that). 

I think you could also add the shader define to the technique, but I don't remember how that works off the top of my head (I'm sure one of the existing techniques has an example with a different shader define if you want to do it that way).

-------------------------

btschumy | 2020-07-01 20:56:30 UTC | #6

Brilliant!!  That does indeed solve the problem.  Thanks so much for that.

While we are talking about transparency, is there a way to programmatically change the transparency of a material (or of a Node)?  In the iOS version of the product, I make the galaxy increasingly transparent as you get closer to the galactic plane.  This allows you to see object below the plane.

Thanks again,
Bill

-------------------------

SirNate0 | 2020-07-06 18:15:30 UTC | #7

If it's one object per material (like all of the galaxy) you can just update the diffuse color in the material to have a different alpha value. If it's multiple objects sharing the material and you need it done individually the simplest way is probably just to adjust the diffuse color in the shader based on the depth of the object (simple if you don't mind working with shaders. If you do, it might be easier to use one material for each object (e.g. each galaxy, assuming there are multiple) unless you observe that that doesn't give you the necessary performance).

-------------------------

