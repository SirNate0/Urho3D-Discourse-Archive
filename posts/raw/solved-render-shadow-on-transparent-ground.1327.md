victorfence | 2017-01-02 01:06:50 UTC | #1

Hello everyone,

I need to render a character and his shadow, if a ground is necessary(I wish not), how to render the ground as transparent but keep the shadow visible?

Thanks for any suggestion.

-------------------------

cadaver | 2017-01-02 01:06:51 UTC | #2

The default rendering setup renders each shadowed light at once and then reuses the shadowmap texture, which means that shadowmaps aren't available during transparent rendering anymore.

Call Renderer::SetReuseShadowmaps(false) or renderer.reuseShadowmaps = false in script to disable reuse and allow transparent geometry to receive shadows. The downside is that shadow maps will now use more video memory, and you may run out of shadow maps if there are too many shadowed lights visible at once. See the Renderer::SetMaxShadowMaps() function in case you run out.

-------------------------

victorfence | 2017-01-02 01:06:59 UTC | #3

Thanks a lot for the reply, I tried the idea, and need more help.

I created a ground with a transparent material:
[code]
<material>
      <technique name="Techniques/NoTextureAlpha.xml" />
      <parameter name="MatDiffColor" value="0 1 0 0" />
      <parameter name="MatSpecColor" value=" 0 0 0 0" />
</material>
[/code]

In script, this line added:
[code]
renderer.reuseShadowMaps = false;
[/code]

I found no shadow(on ground) rendered. if I increase the opacity, I can see the shadow.
The shadow is gone when the ground is completely transparent.

Here's some pictures, the green centered rectangle is the ground, 
I change the opacity by changing the MatDiffColor of the material:

opacity 100%
[url]http://www.tiikoni.com/tis/view/?id=c0df6e4[/url]
opacity 75%
[url]http://www.tiikoni.com/tis/view/?id=96f426c[/url]
opacity 25%
[url]http://www.tiikoni.com/tis/view/?id=9a08ad8[/url]
opacity 0%
[url]http://www.tiikoni.com/tis/view/?id=cdf8d1a[/url]

-------------------------

cadaver | 2017-01-02 01:06:59 UTC | #4

With straightforward alpha-blending, this is the expected result. You could try making the ground white and using multiply blend mode, but I don't guarantee that is what you want either.

-------------------------

victorfence | 2017-01-02 01:07:00 UTC | #5

Hi Cadaver, finally, I got it!! urho3d is so nice!!

I use a technique as:
[code]
<technique vs="LitSolid" ps="LitSolid" vsdefines="NOUV" >
  <pass name="litalpha" depthwrite="false" blend="multiply" />
</technique>
[/code]

-------------------------

