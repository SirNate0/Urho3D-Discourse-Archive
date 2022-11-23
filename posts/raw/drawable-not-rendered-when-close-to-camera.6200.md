Pencheff | 2020-06-15 16:58:51 UTC | #1

I have custom geometry (RichText3D) which uses multiple Drawable objects to create text and images. Everything works fine on DirectX/OpenGL, however, on GLES2 (RockPro64 board with ARM soc), the Drawable is not rendered. When I move the camera backwards a bit, it renders fine. My near/far clip planes are 0.1 / 100 and it doesn't seem related. 

https://www.youtube.com/watch?v=YlMu7-1eodY

Notice that if I move the camera to look just a bit up or down away from the text, it disappears. I cannot reproduce this problem on PC and debugging is hard since the project is cross-compiled on GitLab CI/CD.

-------------------------

Pencheff | 2020-06-16 14:32:14 UTC | #2

[code]
void FrustumOctreeQuery::TestDrawables(Drawable** start, Drawable** end, bool inside)
{
    while (start != end)
    {
        Drawable* drawable = *start++;

        if ((drawable->GetDrawableFlags() & drawableFlags_) && (drawable->GetViewMask() & viewMask_))
        {
            if (inside || frustum_.IsInsideFast(drawable->GetWorldBoundingBox()))
                result_.Push(drawable);
        }
    }
}
[/code]

It looks like this code is completely ignoring my drawable, but its world bouding box is valid.

-------------------------

Pencheff | 2020-06-18 00:23:23 UTC | #3

[quote="Eugene, post:2, topic:6210, full:true"]
Set an infinite bouning box for this drawable.
I mean, it's literally what `Skybox` does, just check its code.
[/quote]


That actually fixes my problem, thanks @Eugene :
[code]worldBoundingBox_.Define(-M_LARGE_VALUE, M_LARGE_VALUE);[/code]

But I still am trying to understand why is it happening, the world bounding box seems perfectly fine when I draw it using the DebugRenderer.

-------------------------

