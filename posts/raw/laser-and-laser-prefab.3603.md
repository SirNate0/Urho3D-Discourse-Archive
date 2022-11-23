stark7 | 2017-09-25 02:02:21 UTC | #1

Hello,

Can someone please give me some direction on how to make a laser like this:
https://www.youtube.com/watch?v=kBCpiRzaRX4

And if at all possible, something like this in blender or whatever other program:
https://www.youtube.com/watch?v=DaD-IRotLBA

-------------------------

1vanK | 2017-09-24 20:16:10 UTC | #2

> Can someone please give me some direction on how to make a laser like this:

cylinder with material
```
<material>
    <technique name="Techniques/DiffAdd.xml" />
    <parameter name="MatDiffColor" value="1 0 0 1" />
</material>
```

raycast forward to find obstacle and change scale for this cylinder

EDIT:

> And if at all possible, something like this in blender or whatever other program:

I look to https://github.com/MonkeyFirst/FH

it is just intersected poligons with texture with fade alpha

-------------------------

1vanK | 2017-09-25 19:43:42 UTC | #3

![1|690x399](upload://epWJu0LlhRoGjNDr6LgK3eXemrD.jpg)

![thunder|500x500](upload://h1UOEHM3MbmvJKSgznmPCuwu3DE.png)

-------------------------

stark7 | 2017-09-24 20:32:18 UTC | #4

Thank you very much 1vank! This really puts me back on track.

-------------------------

Modanung | 2017-09-25 19:43:34 UTC | #5

Possibly related topic:
https://discourse.urho3d.io/t/rotate-node-on-local-z-facing-camera/2929

-------------------------

stark7 | 2017-09-25 00:50:25 UTC | #6

Beautiful work Modanung! I am actually coding all this in urhosharp and it will take me a little while to convert your code to c# and test it - when I do I will make sure to put it on my github. Seeing how good it looks, I will probably get it done sometime tomorrow.

-------------------------

Modanung | 2017-09-25 19:43:42 UTC | #7

In case of a laser you'd probably want to add a raycast that controls the Z-scale of the plane and the position of any impact effect.
Also you may want to implement it as a `Drawable` instead of a `LogicComponent`.

-------------------------

stark7 | 2017-09-25 02:16:54 UTC | #8

Yes - that's what I did and now I'm getting the effect I wanted. Instead of cylinder I also used two perpendicular planes (aka intersecting polygons). It looks pretty good.

-------------------------

stark7 | 2017-09-25 02:16:32 UTC | #9

Hey 1vanK - do you have any idea how LaserObject.mdl was created in the first place? Was it some blender animated model with armature and what not?

-------------------------

1vanK | 2017-09-25 04:38:58 UTC | #10

Write message to @codingmonkey

-------------------------

stark7 | 2017-10-31 21:50:42 UTC | #11

Hey Modanung,

When I tried to replicate BeamLight with urhosharp, I get the below weirdness.

I am now going to do a third pass :) - I used the white bg so you can see what I think should be the beamlight sources. I pasted the code below and I tried to reuse your variable names as much as possible for an easier transition.

One thing I am not really doing is setting the same renderpath with BloomHDR - could that be part of it? I didn't set this because I am under the impression that any render path other than the standard doesn't work for mobile devices.

https://www.youtube.com/watch?v=yn-OnXlxy_g

> class BeamLight : Component
    {
        float startEulerY_;
        Node beamNode_;
        Node flareNode_;

        Light light_;
        Material lampMaterial_;
        Material beamMaterial_;
        Material flareMaterial_;

        public BeamLight()
        {
            ReceiveSceneUpdates = true;
        }

        public void SetColor(Color color)
        {
            light_.Color = color;

            int isEnabled = light_.Enabled ? 1 : 0;

            lampMaterial_.SetShaderParameter("MatDiffColor", (light_.Color * 2.0f + Color.White) * 0.333f * isEnabled * light_.Brightness);
            lampMaterial_.SetShaderParameter("MatEmissiveColor", light_.Color * 100.0f * isEnabled * light_.Brightness);
        }

        private float Angle(Vector3 lhs, Vector3 rhs)
        {
            return (float)Math.Acos((float)Vector3.Dot(lhs, rhs) / (lhs.Length * rhs.Length));
        }

        private float Average(Color p_color)
        {
            return (p_color.R + p_color.G + p_color.B) / 3.0f;
        }

        protected override void OnUpdate(float timeStep)
        {
            base.OnUpdate(timeStep);

            float yaw = this.Node.Rotation.YawAngle;
            float pitch = this.Node.Rotation.PitchAngle;
            float roll = this.Node.Rotation.RollAngle;

            float shift = (0.23f + 0.05f * pitch * 0.5f) + (yaw / 360.0f);

            //SetColor(Color.White);

            SetColor(new Color(
                BeamLightTools.MCSine(0.111f, 0.0f, 1.0f, shift),
                BeamLightTools.MCSine(0.222f, 0.0f, 1.0f, shift + .23f),
                BeamLightTools.MCSine(0.333f, 0.0f, 1.0f, shift + .42f),
                1f
            ));

            Vector3 camDeltaPos = this.Node.WorldPosition - Vector3.Zero;

            this.Node.RotateAround(Vector3.Zero, new Quaternion(Vector3.Up, timeStep), TransformSpace.World);

            beamNode_.LookAt(this.Node.WorldPosition + this.Node.Direction, camDeltaPos);

            float normAngle = 1.0f - Angle(this.Node.Direction, camDeltaPos) / 90.0f;

            int isEnabled = light_.Enabled ? 1 : 0;

            Color lightColor = light_.Color * isEnabled * light_.Brightness;
            Color beamColor = lightColor * MathHelper.Clamp((float)Math.Pow(1.1f - Math.Abs(normAngle) - 0.16f, 0.9f), 0.0f, 1.0f);
            Color flareColor = lightColor * MathHelper.Clamp((float)Math.Pow(0.5f - normAngle, 4.0f) - 0.23f, 0.0f, 1.0f);

            beamMaterial_.SetShaderParameter("MatDiffColor", beamColor);
            flareMaterial_.SetShaderParameter("MatDiffColor", flareColor);
            flareNode_.SetScale(normAngle * (0.5f + Average(lightColor) * 0.32f));
        }
        
        public override void OnAttachedToNode(Node node)
        {
            if (node == null)
                return;

            base.OnAttachedToNode(node);

            var cache = Physics.resourcecache;

            light_ = node.CreateComponent<Light>();
            light_.LightType = LightType.Spot;

            var lampModel = node.CreateComponent<StaticModel>();
            lampModel.Model = cache.GetModel("Models/Lamp.mdl");
            lampMaterial_ = cache.GetMaterial("Materials/Lamp.xml").Clone();
            lampModel.SetMaterial(0, lampMaterial_);

            beamNode_ = node.CreateChild("Beam");
            beamNode_.Translate(Vector3.Forward * 0.82f);
            beamNode_.Scale = new Vector3(1.0f, 1.0f, 1.8f);

            var beamModel = beamNode_.CreateComponent<StaticModel>();
            beamModel.Model = cache.GetModel("Models/Plane.mdl");
            beamMaterial_ = cache.GetMaterial("Materials/Beam.xml").Clone();
            beamModel.Material = beamMaterial_;

            //beamNode_.CreateComponent<RibbonTrail>();

            flareNode_ = node.CreateChild("Flare");
            flareNode_.Rotate(new Quaternion(Vector3.Right, 90.0f));
            var flareModel = flareNode_.CreateComponent<StaticModel>();
            flareModel.Model = cache.GetModel("Models/Plane.mdl");
            flareMaterial_ = cache.GetMaterial("Materials/Flare.xml").Clone();
            flareModel.Material = flareMaterial_;
        }
    }

-------------------------

codingmonkey | 2017-11-01 06:01:57 UTC | #12

hi @stark7 
I have my old shader for beam lights (very basic), you may also take a look on it.
But I do not know how urhosharp integrate custom shaders/techniques, cuz I never used it.
![preview|690x360](upload://iDGIv3aaIbNmVcQdZWvP4LvjjwT.png)

REPO: https://github.com/MonkeyFirst/Urho3D_GeomBeamLight

-------------------------

stark7 | 2017-11-01 06:23:02 UTC | #13

foooorked! I'll try to get it working and let you know.

-------------------------

stark7 | 2017-11-01 14:59:15 UTC | #14

Hey @codingmonkey - for ease of replication, would you please add to your repo the missing assets like Sphere.mdl, Dome.mdl, Box.mdl and Plane.mdl and  Materials/BlockWithEnv.xml ? Just so I can replicate this as is and compare 1:1 - thank you again!

-------------------------

stark7 | 2017-11-01 15:18:08 UTC | #15

Here is what it looks like in urhosharp with your shader and with removing a bunch of stuff from scene1.xml - it's fantastic! I can hardly wait to put it in it's right place.

![image|485x500](upload://iC1rgbVRxKhc6C63zHUW8b6Euul.jpg)

-------------------------

stark7 | 2017-11-01 15:27:34 UTC | #16

@codingmonkey do you happen to have a similar shader or maybe you can provide some direction on how to turn this into a point light? I'm thinking to use something like that to make some glowing cannonballs :D or something along those lines. 

My current investigation is to try and use DiffEmissive but that requires a SpecularMap and I was hoping to not have to use that.

-------------------------

codingmonkey | 2017-11-01 15:33:26 UTC | #17

You are welcome, it's nice to see what it works even on urhosharp )

but shader still far from complete, it have some "angle" problems, it might disappear when you try to looking on it from some positions. also it's need to be fix to render beams in similar way as SoftParticles.

> maybe you can provide some direction on how to turn this into a point light?

use softparticles for that, there two mode of SP, don't remember exactly what mode allow make glow.

-------------------------

stark7 | 2017-11-04 05:27:05 UTC | #18

Hey @codingmonkey is there a way to have it remain visible when it's pointing at the camera or away from the camera? The version you shared makes it disappear and I'm trying to make an effect like this:

![image|690x329](upload://lj1wf6Zw7xlxz03si0bODfNsjUi.jpg)


EDIT - man.. I'm burned out - I did read your text on how you have the angle issues and completely forgot about it like 10 seconds after. I wish I could help with the shader and resolving those issues, I just don't really have any idea where to start or what to do.
Are the issues you're experiencing related to limitations in what can be done with a shader or are you in the process of learning how to do it?

-------------------------

codingmonkey | 2017-11-05 12:06:00 UTC | #19

Hey @stark7 yeah I thinking about this issue, but still no clue how fix this.

-------------------------

Eugene | 2017-11-05 15:41:43 UTC | #20

Well, if you are ready to work...
I suppose that you could utilize the same approach as used for 3d lines.
http://developer.download.nvidia.com/SDK/9.5/Samples/DEMOS/OpenGL/src/cg_VolumeLine/docs/VolumeLine.pdf

-------------------------

stark7 | 2017-11-07 05:20:24 UTC | #21

Hey @codingmonkey  just in case you don't see my comments on github :) - can you please add the missing scene and material .xmls and .mdl to your Urho3D_GeomBeamLight repo? Btw, I can't seem to be able to see anything anymore with your latest commit - although the screenshot you posted looks siiiiiick.

-------------------------

