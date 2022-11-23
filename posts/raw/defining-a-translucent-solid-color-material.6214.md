btschumy | 2020-06-19 19:57:08 UTC | #1

I am trying to create a solid color translucent material (with alpha).  It seems the alpha component is not respected and it is just a solid color.  Here is the Material.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<material>
    <technique name="Techniques/NoTextureUnlit.xml" />
    <parameter name="MatDiffColor" value="0.97 0.93 0.77 0.1" />
</material>
```

As I say, the material color is being used but it is drawn as if alpha = 1.0.

Do I need to be using a different Technique?  Are there other parameters I need other than the defaults?

-------------------------

Lys0gen | 2020-06-19 21:56:20 UTC | #2

Yes, most shader techniques just ignore the alpha component or discard the pixel completely if alpha is below 0.5.

Try one of the techniques with "Alpha" in the name.

-------------------------

throwawayerino | 2020-06-20 12:04:29 UTC | #3

There's even a technique called "DiffAlphaTranslucent.xml". Try applying that

-------------------------

btschumy | 2020-06-22 14:44:03 UTC | #4

Thank you all for the suggestions.  I had previously tried various "Alpha" techniques but they weren't working for me.  The galactic bulge (which is what I'm trying to texture) ends up using the texture material for the galaxy rather than the translucent color I want.  

![image|666x500](upload://fNlhtUNNH5yR0smGCQRPuU2Paqb.jpeg) 

I assume there is something missing from my material .xml file but I don't know what it could be.  I've tried adding:

    <parameter name="UOffset" value="1 0 0 0" />
    <parameter name="VOffset" value="0 1 0 0" />

just in case that was it, but same effect.

If I change the material to use a solid .jpg then it does texture correctly.

Thoughts?

-------------------------

SirNate0 | 2020-06-22 15:26:36 UTC | #5

If the technique expects a technique (which most/all of the techniques other than the \*NoTexture techniques do expect) and you don't provide one it will just use one of the other textures in the scene in a rather random fashion. You'll need a different technique or you will need to supply a texture.

-------------------------

btschumy | 2020-06-22 16:35:21 UTC | #6

OK, got it. There is a built-in NoTextureUnlitAlpha technique that seems to combine all the right elements.  It does work as I want it to.

Thanks again for helping a newbie.

-------------------------

SirNate0 | 2020-06-22 21:50:44 UTC | #7

You're welcome, glad you got it working!

-------------------------

