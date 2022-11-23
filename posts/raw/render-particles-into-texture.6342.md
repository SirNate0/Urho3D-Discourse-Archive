diverlin | 2020-08-22 17:37:12 UTC | #1

Probably the question is silly, but I spend a couple of hours to solve it, and haven't found a solution yet.

if I perform the following:

    <renderpath>
    <command type="scenepass" pass="base" output="viewport"></command></renderpath>

i see the particles in the screen, but I got the black screen when try to render them into the render target texture

    <renderpath>
    <rendertarget name="rtParticles" sizedivisor="1 1" format="rgba" />

    <command type="scenepass" pass="base" output="rtParticles"></command>

    <command type="quad" vs="Urho2DQuad" ps="Urho2DQuad" output="viewport">
        <texture unit="diffuse" name="rtParticles" />
    </command></renderpath>

the shader Urho2DQuad works properly (I used it to debug other operation steps, to draw different maps). i tried all variations for pass

    base,litbase,light,alpha,litalpha,postopaque,refract,postalpha,prepass,material,deferred,depth,shadow

what I want is to draw particles after I did post effect, or render them to separate texture (for possible next post effect)

Ideally, my main target is to learn how to get full control over the render path command type="scenepass" render order, when I added post effects, I realized that some objects which were drawn before, are gone now, and I assume they are drawn to viewport still but are overridden by post effect quad

-------------------------

