flintza | 2017-01-02 01:12:25 UTC | #1

Hi all, I'm working in the Atomic Game Engine project, implementing in-editor lightmapping. I've checked and the core code I'm hitting is unchanged from Urho3D's, so I thought it would make more sense to ask about it here :slight_smile:

[b]Context[/b]
To give some context to my question, I'm currently at the point of applying a generated lightmap to objects by cloning their material and setting UV scale and offset accordingly.

I've added a second set of UV transform uniforms in Uniform.hlsl:
[code]
uniform float4 cUOffset;
uniform float4 cVOffset;
uniform float4 cUOffsetLM;
uniform float4 cVOffsetLM;
uniform float4x3 cZone;
[/code]

And added a transform function to be used in lightmap shaders (currently testing with LitSolid) in Transforms.hlsl:
[code]
float2 GetTexCoord2(float2 iTexCoord)
{
    return float2(dot(iTexCoord, cUOffsetLM.xy) + cUOffsetLM.w, dot(iTexCoord, cVOffsetLM.xy) + cVOffsetLM.w);
};
[/code]

In Material.h/cpp, I added methods similar to SetUVTransform but corresponding to the second set of UVs, moving the transform calculation into a separate method and calling it from both:

[code]
void Material::SetUVTransform2(const Vector2& offset, float rotation, const Vector2& repeat)
{
    Matrix3x4 transform = CalculateUVTransform(offset, rotation, repeat);

    SetShaderParameter("UOffsetLM", Vector4(transform.m00_, transform.m01_, transform.m02_, transform.m03_));
    SetShaderParameter("VOffsetLM", Vector4(transform.m10_, transform.m11_, transform.m12_, transform.m13_));
}

Matrix3x4 Material::CalculateUVTransform(const Vector2& offset, float rotation, const Vector2& repeat)
{
    Matrix3x4 transform(Matrix3x4::IDENTITY);
    transform.m00_ = repeat.x_;
    transform.m11_ = repeat.y_;
    transform.m03_ = -0.5f * transform.m00_ + 0.5f;
    transform.m13_ = -0.5f * transform.m11_ + 0.5f;

    Matrix3x4 rotationMatrix(Matrix3x4::IDENTITY);
    rotationMatrix.m00_ = Cos(rotation);
    rotationMatrix.m01_ = Sin(rotation);
    rotationMatrix.m10_ = -rotationMatrix.m01_;
    rotationMatrix.m11_ = rotationMatrix.m00_;
    rotationMatrix.m03_ = 0.5f - 0.5f * (rotationMatrix.m00_ + rotationMatrix.m01_);
    rotationMatrix.m13_ = 0.5f - 0.5f * (rotationMatrix.m10_ + rotationMatrix.m11_);

    transform = rotationMatrix * transform;

    Matrix3x4 offsetMatrix = Matrix3x4::IDENTITY;
    offsetMatrix.m03_ = offset.x_;
    offsetMatrix.m13_ = offset.y_;

    return offsetMatrix * transform;
}
[/code]

The scale and offset are calculated in the lightmapper and applied to each model (where rect corresponds to where the model's LM is in the full LM atlas):
[code]
IntRect& rect = rects[i];
Vector2 scale((float)rect.Width() / atlasWidth, (float)rect.Height() / atlasHeight);
Vector2 offset((float)rect.left_ / atlasWidth, (float)rect.top_ / atlasHeight);

LMStaticModel* model = generators[i]->GetModel();
model->SetLightmapTexure(atlasTexture);
model->SetLightmapUVTransform(offset, 0, scale);
[/code]

LMStaticModel::SetLightmapTexure and LMStaticModel::SetLightmapUVTransform just set these values on the cloned material.

[b]The actual question, at last :slight_smile: [/b]

This is my current lightmap atlas test case (automatically generated, but with numbers added for my sanity afterwards):
[img]https://dl.dropboxusercontent.com/u/5824027/LightmapScene%20TwoObjects%20Numbered.png[/img]

As an example mapping the second, smaller cube in the atlas I would expect an offset of approx (0.6, 0.0) and a scale/repeat of approx (0.3, 0.3). Setting these values manually on the material's U/VOffsetLM I get the expected result:
[img]https://dl.dropboxusercontent.com/u/5824027/ManuallySetLMUV.PNG[/img]
[img]https://dl.dropboxusercontent.com/u/5824027/ManuallySetLMUVResult.PNG[/img]

However setting them through SetUVTransform2 (which uses the same transform calculation as SetUVTransform), the calculated values are not what I would expect, and the visual result is way off:
[img]https://dl.dropboxusercontent.com/u/5824027/HighlevelSetLMUV.PNG[/img]
[img]https://dl.dropboxusercontent.com/u/5824027/HighlevelSetLMUVCalculated.PNG[/img]
[img]https://dl.dropboxusercontent.com/u/5824027/HighlevelSetLMUVResult.PNG[/img]

So what is going on here? Is my understanding of UVs completely wrong (not impossible at all) or is that CalculateUVTransform wrong. It's been in Material.cpp as-is since before the Atomic fork, but I see Material::SetUVTransform isn't actually used anywhere so it's possible the calculation is wrong and it's never been noticed.

-------------------------

cadaver | 2017-01-02 01:12:25 UTC | #2

This is some of Urho's oldest code. When I tested it, it added a counter-intuitive offset when I adjusted repeat. I no longer remember the rationale for that, so I just removed it :slight_smile: The change is in master.

-------------------------

flintza | 2017-01-02 01:12:25 UTC | #3

Haha, so I'm not going nuts! :slight_smile: Thanks, I'll adjust it my side and leave a note for when Josh merges back again.

-------------------------

