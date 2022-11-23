codingmonkey | 2017-01-02 01:02:23 UTC | #1

hi folks!
I am trying to use my own unlit alpha test shader and in the editor he works normally
but in the game not. 
Why is this happening?  I just need alphatest without shading with light

video of this problem.
[video]http://www.youtube.com/watch?v=vzwmEYuKraA[/video]

this my lit tech
[code]
<technique vs="LitSolidAlphaMask" ps="LitSolidAlphaMask" psdefines="DIFFMAP ALPHAMASK" alphamask="true" >
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" psdefines="ALPHAMASK" />
    <pass name="shadow" vs="Shadow" ps="Shadow" psdefines="ALPHAMASK" />
</technique>
[/code]

this unlit tech
[code]
<technique vs="UnlitAlphaMask" ps="UnlitAlphaMask" psdefines="DIFFMAP ALPHAMASK" alphamask="true">
    <pass name="base" />
    <pass name="depth" vs="Depth" ps="Depth" psdefines="ALPHAMASK" />
    <pass name="deferred" psdefines="DEFERRED" />
</technique>
[/code]

the UnlitAlphaMask shader is the same as Unlit but only with this code fix:
[code]
    // Get material diffuse albedo
    #ifdef DIFFMAP
        float4 diffColor = cMatDiffColor * tex2D(sDiffMap, iTexCoord);
        #ifdef ALPHAMASK
            if (diffColor.a < cFactor)
                discard;
        #endif
    #else
        float4 diffColor = cMatDiffColor;
    #endif
[/code]

my cFactor is added also to Uniforms.hlsl

-------------------------

codingmonkey | 2017-01-02 01:02:27 UTC | #2

no one has any idea about this ?

maybe needed make git request for adding  DiffUnlitAlphaMask.xml,  with one then i modify by adding alpha factor uniform )

-------------------------

reattiva | 2017-01-02 01:02:29 UTC | #3

Wild guess, have you added 'Factor' in your material as a parameter?

-------------------------

codingmonkey | 2017-01-02 01:02:29 UTC | #4

Yes, it's work perfect in editor, but then i'm run compiled game.exe, the object all most time are invisible, only in initial moment it shows then gone.

this animation code. it's work for LitAlphaMask Tech, and why it can't work for unlit i don't know
[code]
void ScriptSmokeFx::Start()
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();
	maxLifeTime = 1.0f; // ???????
	currentLifeTime_ = 0.0f;

	scaleAnim_ = SharedPtr<ValueAnimation>(new ValueAnimation(context_));
	
	float startSize = 1.0f * GetNode()->GetWorldScale().Length(); // relative on inited scale
	float endSize = 3.0f * GetNode()->GetWorldScale().Length();

	scaleAnim_->SetKeyFrame(0.0f, Vector3(startSize, startSize, startSize));
	scaleAnim_->SetKeyFrame(maxLifeTime, Vector3(endSize, endSize, endSize));

	GetNode()->SetScale(startSize);
	GetNode()->SetAttributeAnimation("Scale", scaleAnim_, WM_LOOP);

	StaticModel* model = GetComponent<StaticModel>();

#if 1
	mat_ = SharedPtr<Material>(model->GetMaterial(0)->Clone("ClonedMat"));
	//cache->AddManualResource(mat_);
#else
	mat_ = model->GetMaterial(0);
#endif

	// alpha factor
	factorAnim_ = SharedPtr<ValueAnimation>(new ValueAnimation(context_));
	factorAnim_->SetKeyFrame(0.0f, 0.0f);
	factorAnim_->SetKeyFrame(maxLifeTime / 5.0f, 0.2f);
	factorAnim_->SetKeyFrame(maxLifeTime + (maxLifeTime / 5.0f), 1.0f); // litle shift (+1/5t) end value to remove visual artifacts with factor
	mat_->SetShaderParameterAnimation("Factor", factorAnim_);
	mat_->SetScene(GetScene());

	// color fade
	colorAnim_ = SharedPtr<ValueAnimation>(new ValueAnimation(context_));
	colorAnim_->SetKeyFrame(0.0f, Vector3(1.0f,1.0f,1.0f));
	colorAnim_->SetKeyFrame((maxLifeTime / 3.0f), Vector3(1.0f,1.0f,1.0f));
	colorAnim_->SetKeyFrame(maxLifeTime + (maxLifeTime / 5.0f), Vector3(0.2f,0.2f,0.2f));
	mat_->SetShaderParameterAnimation("MatDiffColor", colorAnim_);
	mat_->SetScene(GetScene());

	model->SetMaterial(0,mat_);
	
	target_ = NULL;
}
[/code]

-------------------------

codingmonkey | 2017-01-02 01:02:29 UTC | #5

i found a my mistake, now i use Vector4 instead of Vector3 for animation color value

-------------------------

