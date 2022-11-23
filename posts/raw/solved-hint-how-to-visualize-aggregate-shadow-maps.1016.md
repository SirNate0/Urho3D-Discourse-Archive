grumbly | 2017-01-02 01:04:51 UTC | #1

Hi everyone. I've been researching this for a couple weeks now and decided I need some help!

Goal
I'm trying to render a bird's eye view (not the main view) of my puzzle game and extract only the shadow information from all shadows/lights as a simple texture where it's easy to tell if there is or is not shadow from the bird's eye perspective, such as a black and white texture. Having a Texture minimap version of all shadows in the puzzle will allow me to perform texture lookups instead of performing an ungodly number of raycasts to detect which parts of space are in or out of shadows.

Approach
Judging by the links below, and others, I would have to create my own renderpath, technique, and material to achieve this effect. This seems doable, however, I'm unsure how then I could render the scene from my normal camera which looks fine with objects having been assigned the default materials/techniques, if I have to replace those materials and techniques to get the shadowmap effect. I suppose I could manage a duplicate scene with identical everything except materials, or switch materials on every shadowcasting object before and after I want the shadowmap rendered, but both approaches smell bad because I don't care about materials at all when rendering only the shadowmap.

What about these? I haven't looked up the source yet to determine what they do.
Renderer.GetShadowCamera()
Renderer.SetBatchShaders(Batch/Geometry, Technique, allowShadows)

Sources
[nervegass.blogspot.de/2014/12/ur ... ction.html](http://nervegass.blogspot.de/2014/12/urho-shaders-edge-detection.html)
[post4108.html?hilit=simple%20renderpath#p4108](http://discourse.urho3d.io/t/high-level-description-about-rendering-process/727/3%20renderpath#p4108)

-------------------------

Bananaft | 2017-01-02 01:04:51 UTC | #2

But how many lights and how many objects need to know if it in shadow or not in each frame?

Couple hundred raycasts still sound more reasonable for me.

-------------------------

grumbly | 2017-01-02 01:04:52 UTC | #3

Hi, thanks for the replies. I'm using forward rendering, so the suggestion to add another pass in a technique and make a variant of the default renderpath sounds good. There is no upper limit to the number of lights in the scene affecting all objects, but reasonably an upper limit for raycasts would be 1k, which only needs to happen every 250ms. I've been thinking of breaking this batch of raycasts down per frame so the net effect would be 1k calculated every 250ms spread over however many frames are being processed in that time.

-------------------------

grumbly | 2017-01-02 01:05:08 UTC | #4

The raycast approach was the correct one. I just needed a better fundamental algorithm for what I was doing. Thanks!

-------------------------

