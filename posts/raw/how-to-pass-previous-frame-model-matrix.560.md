ucupumar | 2017-01-02 01:01:22 UTC | #1

I'm trying to implement per object motion blur on Urho based on this [url=http://john-chapman-graphics.blogspot.co.uk/2013/01/per-object-motion-blur.html]blog post[/url]. but I don't find easy way to pass previous frame model matrix to shader. It's seems it need to be done by edit the engine source code itself. 
I already tried to do it myself but ended up failed. I can't pass the previous frame model matrix to shader. 

Long story short, my implementation is basically adding previous frame matrix properties to node object and pass them on Batch.cpp by this code (on around line 233 until 255):
[code]    // Set model or skinning transforms
    if (setModelTransform && graphics->NeedParameterUpdate(SP_OBJECTTRANSFORM, worldTransform_))
    {
        if (geometryType_ == GEOM_SKINNED)
        {
            graphics->SetShaderParameter(VSP_SKINMATRICES, reinterpret_cast<const float*>(worldTransform_), 
                12 * numWorldTransforms_);
        }
        else
        {
            graphics->SetShaderParameter(VSP_MODEL, *worldTransform_);
            /////////////// this is my addition ////////////////
            graphics->SetShaderParameter(VSP_PREVMODEL, *prevWorldTransform_); 
            ////////////////////////////////////////////////////
        }
        
        // Set the orientation for billboards, either from the object itself or from the camera
        if (geometryType_ == GEOM_BILLBOARD)
        {
            if (numWorldTransforms_ > 1)
                graphics->SetShaderParameter(VSP_BILLBOARDROT, worldTransform_[1].RotationMatrix());
            else
                graphics->SetShaderParameter(VSP_BILLBOARDROT, cameraNode->GetWorldRotation().RotationMatrix());
        }
    }[/code]
I don't what happens, but it doesn't work. I already set prevWorldTransform_ on Batch object.
Do anyone can help me?  :unamused:

-------------------------

ucupumar | 2017-01-02 01:01:24 UTC | #2

Ah, nevermind, I found it.

The shader only get identity matrix because I never set them in the first place. 
Previous model matrix had to sent to batch object on UpdateBatches() function. At first, I thought I only need on set them on drawable's UpdateBatches(), but then I found out static model has it's own UpdateBatches() function.  :unamused:

-------------------------

