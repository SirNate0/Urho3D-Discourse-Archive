Bananaft | 2017-01-02 01:14:08 UTC | #1

So I want to make render path quad command that will output to several rendertargets.

[code]
    <command type="quad" tag="myquad" vs="myquad" ps="myquad">
      <output index="0" name="viewport" />
      <output index="1" name="albedo" />
      <output index="2" name="normal" />
      <output index="3" name="depth" />
    </command>
[/code]

And in pixel shader:
[code]  
  gl_FragData[0] = vec4(ambient , 1.0);
  gl_FragData[1] = vec4(diffColor.rgb, 1.7 );
  gl_FragData[2] = vec4(normal * 0.5 + 0.5, 1.0);
  gl_FragData[3] = vec4(vec3(0.5), 0.0);
[/code]

This way it says "ERROR: Array index out of bounds". If I remove everything but gl_FragData[0], it says nothing, but also renders nothing. :frowning:

-------------------------

1vanK | 2017-01-02 01:14:08 UTC | #2

May be you forgot
[code]
    <rendertarget name="albedo" ... />
    <rendertarget name="normal" ...  />
    <rendertarget name="depth" ...  />
[/code]

-------------------------

codingmonkey | 2017-01-02 01:14:09 UTC | #3

i guess that you needed fix this (last define)
transforms.glsl
[code]// \todo: should not hardcode the number of MRT outputs according to defines
#if defined(DEFERRED)
out vec4 fragData[4];
#elif defined(PREPASS)
out vec4 fragData[2];
#else
out vec4 fragData[1];
#endif[/code]

-------------------------

cadaver | 2017-01-02 01:14:09 UTC | #4

Or you can define the symbol DEFERRED before you include Transform.glsl. It's a bit nasty, but needed to unify GL3 & GL2 behavior & remove deprecation warnings.

-------------------------

Bananaft | 2017-01-02 01:14:09 UTC | #5

Thank you all for replies. I've fixed by adding psdefines="DEFERRED" to my command.

Also, I want to clarify: If I want to write depth, I can't use readable depth (HWDepth), but only regular deferred renderpath, right?

-------------------------

cadaver | 2017-01-02 01:14:09 UTC | #6

Presently the QUAD command never writes hardware depth, so yes you can't use the HWDepth style renderpaths if you want to output a specific depth value in the quad. However you could use a CLEAR command beforehand which sets the hardware depth to the desired value.

-------------------------

Bananaft | 2017-01-02 01:14:10 UTC | #7

I want to write depth per pixel. I'm playing with raymarching. 

Unfortunately I have another wierd behavior:

It works well, but direction light can only read g-buffer, that was writen on top of some "real" geometry.

Here is the picture. I hacked DeferredLight.glsl to output depth. There is a single plane in scene, and depth writen by my quad command is only visible on this plane.
[i.imgur.com/OriHdFo.png](http://i.imgur.com/OriHdFo.png)

I bet it has something to do with depthstencils, I tried to set stencil="1" in CLEAR command, or add depthstencil="0"  or "1" to my command. Every one of these changes fixed the problem but only if that "real" plane is in camera frustrum. If I turn around everything disappears.

Sure I can hack my way around by ensuring there are always some real geometry in frame :slight_smile:, but maybe there is a more civilized way?

-------------------------

cadaver | 2017-01-02 01:14:11 UTC | #8

You could try writing 255 to the stencil buffer in the clear command. The deferred light volumes are being drawn with a stencil test to allow primitive (8 bits only) per-object lightmasking.

-------------------------

Bananaft | 2017-01-02 01:14:11 UTC | #9

So that's how stencil buffer is used, good to know. No, actually that's does not fixed the problem.

Also I found out, that lineardepth texture is not cleared between frames. And I had to clean it too.

[code]
    <command type="clear" color="fog" depth="1.0" stencil="255" />
    <command type="clear" color="800 0 0 0" output="depth" />
[/code]

-------------------------

1vanK | 2017-01-02 01:14:11 UTC | #10

[quote]color="800 0 0 0"[/quote] ???

May be [code]<command type="clear" color="0 0 0 0" depth="1.0" output="depth" />[/code]

-------------------------

Bananaft | 2017-01-02 01:14:11 UTC | #11

[quote="1vanK"] ???

May be [code]<command type="clear" color="0 0 0 0" depth="1.0" output="depth" />[/code][/quote]

No, that's does not work. 800 is the far plane value, and works for me.

Boy, what an ugly hacky mess am I doing. :smiley:

-------------------------

Bananaft | 2017-01-02 01:14:11 UTC | #12

If anyone want to join the fun here is the data (OpenGL script only):
[dl.dropboxusercontent.com/u/884 ... _thing.zip](https://dl.dropboxusercontent.com/u/8845134/dev/fractal_thing.zip)

How it should look:
[dl.dropboxusercontent.com/u/884 ... 7_2016.png](https://dl.dropboxusercontent.com/u/8845134/dev/Screenshot_Wed_Sep_14_03_26_07_2016.png)

I've got 40-60 fps on GTX 960. If it runs too slow, lower the "const int RAY_STEPS = 96;" at line 35 of raymarch.glsl. Or just reduce window size.

Right now I'm desperately trying to figure out how to make depth of raymarch to correspond to depth from real geometry? And why it changing if I change camera fov(mouse wheel)?

-------------------------

