sirop | 2018-04-20 17:29:03 UTC | #1

Hello.

I guess my question has been already answered before explicitly or between the lines,
but the answers read did not help me...

So I want to export a blend file -- a plant, which leaves are actually mostly green, and the green Texture gets even exported, however all I see when loading the exported model with

        Node* plantNode = scene_->CreateChild("Plant");
        plantNode->SetScale(20);    
        plantNode->SetPosition(Vector3(50.0f, 0.0f, 50.0f));
        StaticModel* plantObject = plantNode->CreateComponent<StaticModel>();
        plantObject->SetModel(cache->GetResource<Model>("Models/Plant.mdl"));
        plantObject->ApplyMaterialList("Materials/Plant.txt");
is a plant with black leaves as if the exported green texture were not properly recognized.

The only material exported was:

    <material>
    	<technique name="Techniques/DiffNormalSpec.xml"/>
    	<texture name="Textures/bpng_Schwaz_wei_sten.png" unit="diffuse"/>
    	<texture name="Textures/bpng_NRM Kopie.jpg" unit="normal"/>
    	<texture name="Textures/bpng.jpg" unit="specular"/>
    	<parameter name="MatDiffColor" value="0.133919 0.245904 0.0451157 1"/>
    	<parameter name="MatSpecColor" value="0.105814 0.105814 0.105814 19"/>
    	<cull value="none"/>
    	<shadowcull value="none"/>
    </material>

What to do?

-------------------------

Modanung | 2018-04-20 10:39:59 UTC | #2

Under the export options check the **Geometries -> Tangent** box. This is required when using normal maps.

-------------------------

sirop | 2018-04-20 10:53:40 UTC | #3

Did that, but it did not help.
Still black leaves in Urho3d:
![plant|217x259](upload://6vRbMMQXByLAFDZ0btjzx1ehH9v.png)

-------------------------

Modanung | 2018-04-20 16:33:30 UTC | #4

And no errors? _Could not find resource_, for instance?

-------------------------

sirop | 2018-04-20 16:39:18 UTC | #5

Well, I do not see error messages in the log, but

    Used resources:
    Textures/Ramp.png
    Textures/Spot.png
    Textures/UI.png
    Textures/cps_logo.png
    Textures/Grids/gridBlue+512_25.png
    Textures/Test_Image_3.jpg
    Textures/Test_Image_4.jpg
    Techniques/NoTexture.xml
    Techniques/Diff.xml
    RenderPaths/Forward.xml
    UI/DefaultStyle.xml
    Config/sliders.xml
    PostProcess/Bloom.xml
    PostProcess/FXAA2.xml
    Textures/UrhoIcon.png
    Textures/UI.png
    Fonts/Anonymous Pro.ttf
    Shaders/HLSL/Basic.hlsl
    Shaders/HLSL/LitSolid.hlsl
    Shaders/HLSL/Shadow.hlsl
    Shaders/HLSL/Bloom.hlsl
    Shaders/HLSL/ClearFramebuffer.hlsl
    Models/Plane.mdl
    Models/Plant.mdl
    Models/Jack.mdl
    Materials/Grids/GridBlue+.xml
    Materials/BackPlane.xml
    Materials/LeftPlane.xml
    Materials/Jack.xml
    Models/Jack_Walk.ani

mentions only _Models/Plant.mdl_, textures or materials of Plant.mdl are not mentioned as if they were not searched for at all.

-------------------------

Modanung | 2018-04-20 16:48:35 UTC | #6

Are the contents of the material list Plant.txt as expected?

-------------------------

sirop | 2018-04-20 16:51:02 UTC | #7

Yes, they are. For instance:

    Materials/Topf.xml
    Materials/Erde.xml
    Materials/Material.036.xml

-------------------------

Modanung | 2018-04-20 16:59:08 UTC | #8

[quote="sirop, post:1, topic:4192"]
plantObject-&gt;ApplyMaterialList("Materials/Plant.txt");
[/quote]
Isn't it in your `Models` folder?

-------------------------

sirop | 2018-04-20 17:13:48 UTC | #9

Good hint. Moved Plant.txt from Models to Materials.
Now the log says:

    Used resources:
    Textures/Ramp.png
    Textures/Spot.png
    Textures/UI.png
    Textures/cps_logo.png
    Textures/Grids/gridBlue+512_25.png
    Textures/Test_Image_3.jpg
    Textures/Test_Image_4.jpg
    Textures/Teppich512X512_NRM.jpg
    Textures/Kies_NRM.jpg
    Textures/bpng_Schwaz_wei_sten.png
    Textures/bpng_NRM Kopie.jpg
    Textures/bpng.jpg
    Techniques/NoTexture.xml
    Techniques/Diff.xml
    Techniques/DiffNormal.xml
    Techniques/DiffNormalSpec.xml
    RenderPaths/Forward.xml
    UI/DefaultStyle.xml
    Config/sliders.xml
    PostProcess/Bloom.xml
    PostProcess/FXAA2.xml
    Textures/UrhoIcon.png
    Textures/UI.png
    Fonts/Anonymous Pro.ttf
    Shaders/HLSL/Basic.hlsl
    Shaders/HLSL/LitSolid.hlsl
    Shaders/HLSL/Shadow.hlsl
    Shaders/HLSL/Bloom.hlsl
    Shaders/HLSL/ClearFramebuffer.hlsl
    Models/Plane.mdl
    Models/Plant.mdl
    Models/Jack.mdl
    Materials/Grids/GridBlue+.xml
    Materials/BackPlane.xml
    Materials/LeftPlane.xml
    Materials/Topf.xml
    Materials/Erde.xml
    Materials/Material.036.xml
    Materials/Jack.xml
    Models/Jack_Walk.ani

which means all Plant materials and textures are found.

After zooming in, one can see some green textures
![plant_zoom|338x418](upload://57ywGZAjugRQvW0u9TUVj1fxSYK.png)
but this is still so far from the green of the original blend file.

-------------------------

sirop | 2018-04-20 17:28:35 UTC | #10

Ok changing something about Material.036.xml helped:

    <material>
    	<technique name="Techniques/DiffNormal.xml"/>
    	<!--texture name="Textures/bpng_Schwaz_wei_sten.png" unit="diffuse"/-->
    	<!--texture name="Textures/bpng_NRM Kopie.jpg" unit="normal"/-->
    	<texture name="Textures/bpng.jpg" unit="specular"/>
    	<parameter name="MatDiffColor" value="0.133919 0.945904 0.0451157 1"/>
    	<!--parameter name="MatSpecColor" value="0.105814 0.105814 0.105814 19"/-->
    	<cull value="none"/>
    	<shadowcull value="none"/>
    </material>
![plant_zoom_green|335x467](upload://7kzjAdi6VMfv289NkGDPygpPYli.jpg)

-------------------------

slapin | 2018-04-21 19:41:02 UTC | #11

You made your plant emit green. You disabled both normal and diffuse. Is it fine with you?

-------------------------

sirop | 2018-04-21 21:31:15 UTC | #12

As before my plant seemed to be mostly black, this "solution"  was an improvement for me.
But I am open fro any better proposals.

-------------------------

slapin | 2018-04-21 23:12:50 UTC | #13

I think you could try Diff technique first and try with only "diffuse" texture and color to get closer to required effect, then attach normal (DiffNormal). You can use a little bit of specularity, but that is secondary factor, your plant should be green even without specularity, if enough light source applied.

-------------------------

