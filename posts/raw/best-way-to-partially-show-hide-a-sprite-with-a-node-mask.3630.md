stark7 | 2017-10-03 14:35:24 UTC | #1

Hello - I am looking into creating a healthbar and while it was pretty straight forward to create a sprite and modifying it with scale, I would like a more fancy looking one and not necessarily linear.

To that end, what is the best way to have a sprite and then a mask over it that will only show the parts behind the mask. I am hoping for a solution where the mask is a node so I can move, scale and rotate at will.

From here, what I ideally need is the **A in B** version - although knowing how to do all of those would make for some really fancy visuals. Any ideas?

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/cca72dfbacec3101e0974599db8137aa3efdd6fa.png'>

-------------------------

Eugene | 2017-10-03 14:37:53 UTC | #2

Classical GAPI pipeline doesn't provide good way to do such boolean things (except stencil tricks that are neither cheap nor easy)

However, it's easy to cut the sprite manually changing its size and texture coordinates simultaneously. Would it be enough for you?

-------------------------

stark7 | 2017-10-03 14:50:57 UTC | #3

I think it would have to do - or have precomputed spritesheet for the really fancy ones. I was wondering if there was already a solution I could code instead of art.

-------------------------

Modanung | 2017-10-03 14:57:42 UTC | #4

Have you seen these?
https://discourse.urho3d.io/t/diablo-3-resource-bubbles/3534
It may not be the solution your looking for, but it might be close to the desired result.

-------------------------

stark7 | 2017-10-03 15:07:09 UTC | #5

Hey - yes, it looks like a step in the direction I want. I saw that blog post before only I didn't make the connection that it could apply. I think I will focus on something like that after the initial release which will only scaling bars :D .

-------------------------

JTippetts | 2017-10-04 01:35:05 UTC | #6

The thing about doing life bars like those resource bubbles is that it requires a custom shader, something that isn't currently possible with UI Sprites. So you'll probably have to use an overlay. Typically, I will have an Urho2D overlay scene that uses a custom renderpath that doesn't clear the render buffer, and render any elements that require a custom material there after the main scene is drawn, so that the 2D layer overlays it. Would be kinda nice if UI::Sprite components allowed a custom material, though, which would make it a bit easier by allowing these kinds of elements in-place in the UI system, rather than requiring another render path and scene.

-------------------------

stark7 | 2017-10-04 03:07:22 UTC | #7

Yeah it probably won't work on mobile either. I am currently waiting around for the new UIComponent to work on urhosharp to try to use it in various creative ways.

BTW @JTippetts, you and I have the same fetish for hexagons and you will see what I mean as soon as I get to showcase my work :smiley:

-------------------------

