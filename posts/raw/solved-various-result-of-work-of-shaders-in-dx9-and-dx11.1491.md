Sasha7b9o | 2017-01-02 01:08:07 UTC | #1

I create the plane from two triangles with texture.

Code:
[code]        const float vertexes[4 * (3 + 2)] =
        {
            0.0f + d, 0.0f, 0.0f + d, 0.0f, 1.0f,
            1.0f - d, 0.0f, 0.0f + d, 1.0f, 1.0f,
            1.0f - d, 0.0f, -1.0f + d, 1.0f, 0.0f,
            0.0f + d, 0.0f, -1.0f + d, 0.0f, 0.0f
        };

        const uint16 indexes[6] =
        {
            2, 1, 0,
            3, 2, 0
        };

        SharedPtr<CustomGeometry> geometry(node->CreateComponent<CustomGeometry>());

        geometry->BeginGeometry(0, Urho3D::TRIANGLE_LIST);
        geometry->SetViewMask(VIEW_MASK_FOR_EFFECTS);

        for (int i = 0; i < 6; i++)
        {
            const float *p = vertexes + indexes[i] * 5;
            geometry->DefineVertex(Vector3(*p++, *p++, *p++));
            geometry->DefineTexCoord(Vector2(*p++, *p));
        }

        geometry->SetMaterial(gCache->GetResource<Material>("Materials/Decals/PathDecal.xml"));

        geometry->Commit();[/code]

Material:
[code]- <material>
  <technique name="Techniques/Decals/PathDecal.xml" /> 
  <texture unit="diffuse" name="Textures/Decals/PathDecal.png" /> 
  <parameter name="MatDiffColor" value="0 0 0 0.8" /> 
  <depthbias constant="-0.00001" slopescaled="0" /> 
  </material>[/code]

Technique:
[code]<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="alpha" depthwrite="false" blend="alpha" />
    <pass name="litalpha" depthwrite="false" blend="addalpha" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>[/code]

Shaders from "Core data" I didn't change.

In DX9 the result meets expectation, in DX11 error message in log:
[code]ERROR: Failed to create input layout for shader LitSolid(), missing element mask 2
[/code]

-------------------------

Sasha7b9o | 2017-01-02 01:08:07 UTC | #2

[quote="Sinoid"]Looks like you just need to add vertex normals to your custom geometry. CustomGeometry::DefineNormal.[/quote]

Thanks. Now everything is correct.

-------------------------

