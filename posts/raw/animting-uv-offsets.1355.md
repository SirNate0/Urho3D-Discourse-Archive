sabotage3d | 2017-01-02 01:07:09 UTC | #1

Hi guys, 
Is it currently possible to animate UV offsets ? I am trying to fake water for mobile and I am thinking of animating the UV offset to fake the ripples.

-------------------------

1vanK | 2017-01-02 01:07:09 UTC | #2

[video]https://www.youtube.com/watch?v=maoDVSdKmiQ[/video]

All questions to codingmonkey :)

-------------------------

codingmonkey | 2017-01-02 01:07:09 UTC | #3

In these dark times i'm just do not knowed about - cUOffset.w and cVOffset.w uniforms ) and that's why I made custom shader for sea foam : oTexCoord +=vec2(cUVShift)


actually for animate textures you need just create ValueAnimation for these this two uniforms: cUOffset and cVOffset especially for last float - "w" this is scroll 

Or you may do little tweak(to animate one common uniform and not two) to the std LitSolid Shader with adding one line:

61     vTexCoord.xy += cUVShift.xy;
and also you need add you custom uniform to Uniforms.glsl
30     uniform vec2 cUVShift;

then just add new uniform to you mat that will be animated
[url=http://savepic.su/6133397.htm][img]http://savepic.su/6133397m.jpg[/img][/url]

and at last you may now animate this uniform with std stuff - ValueAnimation

[code]	Material* seaFoamMaterial = cache->GetResource<Material>("Materials/UL_MAT/MAT_SEAFOAM.xml");
	SharedPtr<ValueAnimation> uvShiftAnimation (new ValueAnimation(context_));
	
	uvShiftAnimation->SetKeyFrame(0.0f, Vector2(0.0f, 0.3f));
	uvShiftAnimation->SetKeyFrame(2.0f, Vector2(0.0f, 0.7f));
	uvShiftAnimation->SetKeyFrame(3.0f, Vector2(0.0f, 0.5f));
	uvShiftAnimation->SetKeyFrame(4.0f, Vector2(0.0f, 0.4f));
	uvShiftAnimation->SetKeyFrame(5.0f, Vector2(0.0f, 0.3f));

	seaFoamMaterial->SetShaderParameterAnimation("UVOffset",uvShiftAnimation );
	seaFoamMaterial->SetScene(Scene);[/code]

-------------------------

sabotage3d | 2017-01-02 01:07:09 UTC | #4

Thanks a lot I will try it out :slight_smile:

-------------------------

Bananaft | 2017-01-02 01:07:11 UTC | #5

Or you can do the whole animation in vertex shader using cElapsedTime uniform to offset UVs.

-------------------------

