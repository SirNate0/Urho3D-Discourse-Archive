codingmonkey | 2017-01-02 01:13:16 UTC | #1

Hi there!
I trying to figure out with new changes in renderer. So i porting my prev GS-related code into the new master.
And it's seems works in most cases fine (i mean as before), but when I try to implement shadow pass (from unlit grass onto floor) and there is nothing to visible, but in same time all shaders programs linked sucessful and grass has rendered in firs pass fine. Only shadow from grass are not visible, so my question is why?

Is shadow pass has custom primitive input state? (not from material) ?
is shadow pass do not use all elements from vertex (model) (use only position semantic in vertex for example) ? 

tech
[code]
<technique vs="UnlitGSGrass" ps="UnlitGSGrass" gs="UnlitGSGrass" vsdefines="VERTEXCOLOR" gsdefines="VERTEXCOLOR" psdefines="DIFFMAP ALPHAMASK VERTEXCOLOR" alphamask="true">
    <pass name="alpha" blend="replace"/>
    <pass name="shadow" vs="GrassShadow" vsdefines="VERTEXCOLOR" gs="GrassShadow" gsdefines="VERTEXCOLOR" ps="GrassShadow" psdefines="ALPHAMASK" />
</technique>
[/code] 

forward render, pcf shadows 24bit
debug info
[url=http://savepic.ru/10493947.htm][img]http://savepic.ru/10493947m.png[/img][/url]

-------------------------

cadaver | 2017-01-02 01:13:16 UTC | #2

Shadow shader uses only the position and first texcoord in case alpha masking is needed. However you would easily end up in the same situation with a textured unlit shader as well. Otherwise there shouldn't be anything special in how it works. If your old code was from the time before arbitrary vertex declarations, then handling them has changed quite a bit.

-------------------------

codingmonkey | 2017-01-02 01:13:17 UTC | #3

Yes I see what std shadow shader use position and texcoords. 
actually I use almost the same: position, texcoord(only for randomization in GS, real texcoord generated in GS for PS shader), and VertexColor
anyway I guess I find the solution.
I find that the shadow pass are rendered through Graphics::Draw(...) but I was thinking what it use only Batch::Draw(...). (with my GS hack code) 
So that's why it was not be visible.

Fixed Graphics::Draw()
[spoiler][code]
void BatchGroup::Draw(View* view, Camera* camera, bool allowDepthWrite) const
{
    Graphics* graphics = view->GetGraphics();
    Renderer* renderer = view->GetRenderer();
	
	

    if (instances_.Size() && !geometry_->IsEmpty())
    {
        // Draw as individual objects if instancing not supported or could not fill the instancing buffer
        VertexBuffer* instanceBuffer = renderer->GetInstancingBuffer();
        if (!instanceBuffer || geometryType_ != GEOM_INSTANCED || startIndex_ == M_MAX_UNSIGNED)
        {
            Batch::Prepare(view, camera, false, allowDepthWrite);

            graphics->SetIndexBuffer(geometry_->GetIndexBuffer());
            graphics->SetVertexBuffers(geometry_->GetVertexBuffers());

            for (unsigned i = 0; i < instances_.Size(); ++i)
            {
				if (graphics->NeedParameterUpdate(SP_OBJECT, instances_[i].worldTransform_))
				{
					graphics->SetShaderParameter(VSP_MODEL, *instances_[i].worldTransform_);
					graphics->SetShaderParameter(GSP_MODEL, *instances_[i].worldTransform_);
				}

				PrimitiveType gsPrimitiveType = graphics->GetEffectivePrimitiveTypeOverGSInput(geometry_->GetPrimitiveType());

				graphics->Draw(gsPrimitiveType, geometry_->GetIndexStart(), geometry_->GetIndexCount(),
                    geometry_->GetVertexStart(), geometry_->GetVertexCount());
            }
        }
        else
        {
            Batch::Prepare(view, camera, false, allowDepthWrite);

            // Get the geometry vertex buffers, then add the instancing stream buffer
            // Hack: use a const_cast to avoid dynamic allocation of new temp vectors
            Vector<SharedPtr<VertexBuffer> >& vertexBuffers = const_cast<Vector<SharedPtr<VertexBuffer> >&>(
                geometry_->GetVertexBuffers());
            vertexBuffers.Push(SharedPtr<VertexBuffer>(instanceBuffer));

            graphics->SetIndexBuffer(geometry_->GetIndexBuffer());
            graphics->SetVertexBuffers(vertexBuffers, startIndex_);
			PrimitiveType gsPrimitiveType = graphics->GetEffectivePrimitiveTypeOverGSInput(geometry_->GetPrimitiveType());
			graphics->DrawInstanced(gsPrimitiveType, geometry_->GetIndexStart(), geometry_->GetIndexCount(),
                geometry_->GetVertexStart(), geometry_->GetVertexCount(), instances_.Size());

            // Remove the instancing buffer & element mask now
            vertexBuffers.Pop();
        }
    }
}
[/code][/spoiler]

But now I have other problem unlit box with texture and shadows are gone )
[url=http://savepic.ru/10532611.htm][img]http://savepic.ru/10532611m.png[/img][/url]

-------------------------

codingmonkey | 2017-01-02 01:13:17 UTC | #4

I have solved last problem with the "disappeared Box" I just manualy set Primitive mode in material, by default it's uses wrong type: point list insted triangle list

So now I have other problem with shadows from my grass, and I thinking that this is because render gets wrong BoundaryBox of rendered model. Since I use GS for generate model I do not have ability to set BB manualy, or somehow else. 

So, Is it BB issue produce this "shadows flickering/cliping" or something else?

[video]https://youtu.be/PNq_ha7PfXk[/video]

-------------------------

cadaver | 2017-01-02 01:13:18 UTC | #5

Obviously if bounding box of model is smaller than what the GS creates, there is bound to be culling issues. That sounds like it could be a job for a subclass of StaticModel that can define the BB expansion.

However I can't wrap my head around why moving one node would cause the other's shadow to disappear.

-------------------------

Modanung | 2017-01-02 01:13:18 UTC | #6

[quote="cadaver"]However I can't wrap my head around why moving one node would cause the other's shadow to disappear.[/quote]
Ordering? I'm guessing it doesn't matter which one is moved.

-------------------------

codingmonkey | 2017-01-02 01:13:18 UTC | #7

[quote]That sounds like it could be a job for a subclass of StaticModel that can define the BB expansion.[/quote]
I hack this in minor code change style - just add
[code]
	URHO3D_ATTRIBUTE("Use Manual BBox", bool, useManualBoundingBox_, false, AM_DEFAULT);
	URHO3D_ATTRIBUTE("Manual BBox", Vector3, manualBoundingBox_, Vector3(1,1,1), AM_DEFAULT);[/code]

[code]
void StaticModel::SetBoundingBox(const BoundingBox& box)
{
	if (!useManualBoundingBox_)
		boundingBox_ = box;
	else
	{
		boundingBox_.Clear();
		boundingBox_.Merge(manualBoundingBox_ / -2.0);
		boundingBox_.Merge(manualBoundingBox_ / 2.0);
	}
	
    OnMarkedDirty(node_);
}
[/code]

[quote]Ordering? I'm guessing it doesn't matter which one is moved.[/quote]
No, I guess it because instansing somehow "purge" data for shadows pass (in case GS using)
because if I try to use two various model there is no bug, but if I try use two equal models shadows are disappears
example:
[video]https://www.youtube.com/watch?v=WA1MESkVS3E[/video]

-------------------------

cadaver | 2017-01-02 01:13:18 UTC | #8

Can your GS handle instancing properly? If not, you could test with turning instancing off. Or if you want the GS-objects to never use instancing while others can still use it, you can use the geometry type GEOM_STATIC_NOINSTANCING.

-------------------------

codingmonkey | 2017-01-02 01:13:18 UTC | #9

Oh you right, I guess i missed something big :slight_smile:

after turn-off instansing in Editor, two grass planes rendered fine with shadows
[url=http://savepic.ru/10601886.htm][img]http://savepic.ru/10601886m.png[/img][/url]

so I think, i take a look into transfoms.glsl
[code]#ifdef INSTANCED
mat4 GetInstanceMatrix()
{
    const vec4 lastColumn = vec4(0.0, 0.0, 0.0, 1.0);
    return mat4(iTexCoord4, iTexCoord5, iTexCoord6, lastColumn);
}
#endif[/code]
and try to find way to use instansing with GS

add:
I found interesting results of perfomance ( GS with instansing )
[joshbarczak.com/blog/?p=667](http://www.joshbarczak.com/blog/?p=667)

-------------------------

codingmonkey | 2017-01-02 01:13:20 UTC | #10

Finally I solved this problem with using iModelMatrix it store within the propely object's transformation, in case auto pushed shaders definition such as #INSTANCED
So i just fix VS

[b]gl_Position = pos * cModel;  
[/b]
to

[b]gl_Position = pos * iModelMatrix; [/b]

Now shadowed GS-generated models working fine even with instansing

grassShadow.glsl for 
<pass name="shadow" vs="GrassShadow" vsdefines="VERTEXCOLOR" gs="GrassShadow" gsdefines="VERTEXCOLOR" ps="GrassShadow" psdefines="ALPHAMASK" />
[spoiler][pastebin]YrSeUjef[/pastebin][/spoiler]

-------------------------

