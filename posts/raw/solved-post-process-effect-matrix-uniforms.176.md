reattiva | 2017-01-02 00:58:39 UTC | #1

Hello all!

I have some questions about passing uniforms to a post-process effect.
Suppose I need camera rotation, projection matrix, projection-view matrix (let's ignore that I should get it from the camera inverse) in a "quad" command. How can I set these uniforms?
Urho variants can't store a matrix, but I can use 4 vectors. I've tried this:
[code]void WorkSample::HandleRenderUpdate(StringHash eventType, VariantMap& eventData)
{
    // Camera rotation
    Matrix3 r = camera_->GetEffectiveWorldTransform().RotationMatrix();
    // Projection matrix
    Matrix4 p = camera_->GetProjection();
    // Projection-View matrix
    Matrix4 pv = p * camera_->GetView();

    #ifdef USE_OPENGL
    r = r.Transpose();
    p = p.Transpose();
    pv = pv.Transpose();
    #endif
        
    renderPath_->SetShaderParameter("CamRotRow0", *(Vector3*)&r.m00_);
    renderPath_->SetShaderParameter("CamRotRow1", *(Vector3*)&r.m10_);
    renderPath_->SetShaderParameter("CamRotRow2", *(Vector3*)&r.m20_);

    renderPath_->SetShaderParameter("ProjRow0", *(Vector4*)&p.m00_);
    renderPath_->SetShaderParameter("ProjRow1", *(Vector4*)&p.m10_);
    renderPath_->SetShaderParameter("ProjRow2", *(Vector4*)&p.m20_);
    renderPath_->SetShaderParameter("ProjRow3", *(Vector4*)&p.m30_);

    // Frustum size
    Vector3 nearVector, farVector;
    camera->GetFrustumSize(nearVector, farVector);
    renderPath_->SetShaderParameter("FrustumSize", farVector);
}[/code]
And then in the shader:
[code]uniform vec4 cProjRow0;
uniform vec4 cProjRow1;
uniform vec4 cProjRow2;
uniform vec4 cProjRow3;

void PS()
{
    mat4 proj = mat4(cProjRow0, cProjRow1, cProjRow2, cProjRow3);
}[/code]
Can this work? Am I getting the correct matrices?
Another problem, suppose I wanted to use GetFarRay() which uses the uniform mat3 cCameraRot, but how can I set it? Is there a way to set uniforms directly after the shader program was binded?

Thank you.

-------------------------

GIMB4L | 2017-01-02 00:58:39 UTC | #2

There is a shader file you can include which contains a whole bunch of matrices. Maybe the ones you need are in there?

-------------------------

Azalrion | 2017-01-02 00:58:39 UTC | #3

Uniforms.glsl or Uniforms.hlsl contains a set of matrices that are auto-populated if defined (I think, its been a long day, you might need to define them in the path) which includes cCameraRot matrix.

-------------------------

reattiva | 2017-01-02 00:58:39 UTC | #4

Thanks GIMB4L and Azalrion. I know where these uniforms are defined and for sure they are set in a "scenepass" command, but I don't think they are all set in a "quad" command.

In a quad command Urho calls:
void View::RenderQuad(RenderPathCommand& command)
which, from what I can see, sets these uniforms:
DELTATIME,NEARCLIP,FARCLIP,VSP_GBUFFEROFFSETS,PSP_GBUFFERINVSIZE,VSP_MODEL,VSP_VIEWPROJ
As you can see not all the uniforms are set (to tell the truth, I've only read the code without doing a real test in the shader, I'll do it).
But for sure VSP_VIEWPROJ is set to render a Quad, instead I need the ViewProject matrix used in the scene pass.

-------------------------

Azalrion | 2017-01-02 00:58:39 UTC | #5

The are set as part of the Batch::Prepare phase thats called when a Batch::Draw is called. It would be interesting to see if that is called before the DrawQuad command.

Anyway incase it isn't called the code used in those instances is as follows:

[code]
        Matrix3x4 cameraEffectiveTransform = camera_->GetEffectiveWorldTransform();
        
        graphics->SetShaderParameter(VSP_CAMERAPOS, cameraEffectiveTransform.Translation());
        graphics->SetShaderParameter(VSP_CAMERAROT, cameraEffectiveTransform.RotationMatrix());
        graphics->SetShaderParameter(VSP_VIEWPROJ, camera_->GetProjection());
        graphics->SetShaderParameter(VSP_VIEWPROJ, camera_->GetProjection() * camera_->GetView());
[/code]

There are overriden versions of SetShaderParameter that handle matrices which binds to a float3x3 or float4x4 or float4x3, etc.

-------------------------

reattiva | 2017-01-02 00:58:39 UTC | #6

Yes, but the problem is that for a post-process you have to use a variant to set a uniform, you cannot use direclty graphics because the shader program is not binded yet in the event RenderUpdate. If the uniforms can be stored in a variant everything is ok, but variants do not support matrices. Unfortunately, the code you found (Batch::Prepare called by Batch::Draw) is not called in a quad command, and this for sure as the View Project matrix must be different from a scene pass. This is from my little knowledge, not much trustworthy.
I was looking from some other event after the program is binded, but I don't think there are any.
The code I've written seems to work, but the results were a bit off (but maybe this was due to the depth buffer float precision), so I was looking for a confirm that I was doing it right...
And there is also the problem of setting a Urho defined matrix uniform (like cCameraRot), (the obviously way is to rewrite the function using it with a custom cMyCameraRot).

Anyway thanks for the help!

-------------------------

Azalrion | 2017-01-02 00:58:40 UTC | #7

Ah I see, I'd raise that an issue against that if I were you, there is no technical reason that renderpath couldn't store a HashMap of StringHash Matrix to use as ShaderParams.

-------------------------

reattiva | 2017-01-02 00:58:40 UTC | #8

Yes, that's actually what I've done, see the first code in my first post.
Matrix can't be stored in a Variant because its struct is a 32bits x 4 (interpreted in various ways according to its type), see "struct VariantValue".
I'll investigate VAR_VARIANTVECTOR and VAR_VARIANTMAP, but for sure they cannot be used by shader uniforms, Graphics::SetShaderParameter for variant supports only VAR_BOOL, VAR_FLOAT, VAR_VECTOR2, VAR_VECTOR3, VAR_VECTOR4 and VAR_COLOR.

EDIT: wrong, we can store anything we want in a Variant.

-------------------------

cadaver | 2017-01-02 00:58:40 UTC | #9

Generally, Variant would need expanding to support arbitrary matrices as shader parameters.

However, the quad rendering code is simply missing the setup of basic inbuilt matrices and camera parameters, which are easy to add, if we assume it's the same camera that is used to render the scene.

-------------------------

reattiva | 2017-01-02 00:58:41 UTC | #10

I'll try to use a VAR_VARIANTVECTOR with 3 Vector3 or 4 Vector4 and then modify Graphics::SetShaderParameter for variants to use them as matrices. Thanks.

-------------------------

cadaver | 2017-01-02 00:58:42 UTC | #11

Now there should be proper matrix type support in Variant, however it hasn't been tested much yet.

-------------------------

reattiva | 2017-01-02 00:58:42 UTC | #12

Fantastic! I've tested with a Matrix3 and a Matrix4 and it works flawlessly, even without specifying the values in the effect xml. Thank you.
By the way, cFrustumSize is a float3, why do we set it as a Vector4?
[code]Vector4 viewportParams(farVector.x_, farVector.y_, farVector.z_, 0.0f);
graphics_->SetShaderParameter(VSP_FRUSTUMSIZE, viewportParams);
[/code]

-------------------------

friesencr | 2017-01-02 00:58:42 UTC | #13

We could basically make our own shader toy in like 15 lines of script with hot reloading.

-------------------------

