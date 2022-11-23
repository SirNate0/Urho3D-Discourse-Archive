tianlv777 | 2022-02-10 05:39:15 UTC | #1

![QQ图片20220210133856|530x433](upload://7HFv5jM1BQAXbdCrvItiBtiR7Vu.png)

-------------------------

Nerrik | 2022-02-10 12:32:56 UTC | #2

don't really understand the question, but looks like a lens flare effect. https://www.shadertoy.com/view/4sX3Rs

normally implemented in the fragmentshader

-------------------------

tianlv777 | 2022-02-10 15:47:04 UTC | #5

![73RGWC{E}OK8B314(K97C0A|437x326](upload://1SBSxMxxidtgLizDZu4hTnyrd8S.png)
texture is tga picture,and geometry is plane.I don't know how to get this affect.

-------------------------

tianlv777 | 2022-02-10 15:48:02 UTC | #6

texture is tga picture,and geometry is plane.I don’t know how to get this affect.

-------------------------

Nerrik | 2022-02-10 19:12:56 UTC | #7

any alpha technique. 
try as material file
```
<?xml version="1.0"?>
<material>
	<technique name="Techniques/DiffAlpha.xml" />
	<texture unit="diffuse" name="Textures/mytexture.tga" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatSpecColor" value="1 1 1 16" />
</material>
```
the texture must have an alpha channel, the background of the circle must be transparent.
the circle in the image can be a little bit transparent also.

-------------------------

Nerrik | 2022-02-10 19:51:12 UTC | #8

if you mean something else, you have to be on mind with shaders.

edit: 
the only other thing that comes to mind is that you mean a particle, then you can look at
https://urho3d.io/documentation/1.7/class_urho3_d_1_1_particle_emitter.html, there are also some samples and a Particle Editor in the Urho3D Editor

-------------------------

SirNate0 | 2022-02-10 23:14:10 UTC | #9

I believe it's an additive blending technique. One of the particle techniques does that, I forget the exact name. I'm not certain though, but the black background rather than a transparent one makes me think that this is how it was done.

-------------------------

tianlv777 | 2022-02-11 05:21:11 UTC | #10

It is war3 game,So it can't be particle.
but i don't know how to do this effect.
if alpha technique,it is wrong.
![6GU9J2`9H9SLM~N(H`D@)Q|289x256](upload://2D2zXTp3Jn19R7hquiqhQGJxmpj.png)

-------------------------

tianlv777 | 2022-02-11 05:29:06 UTC | #11

Techniques/DiffAddAlpha.xml
look like......
![GV07515@YL~PQ5CYE`2AG3|367x340](upload://sS9KDwy1ntyp5m9hYTQJ4e0YqxA.png)

-------------------------

JTippetts1 | 2022-02-11 17:29:59 UTC | #12

Did you try DiffAdd? Looks like a simple additive blend to me.

-------------------------

