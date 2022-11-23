theak472009 | 2017-01-02 01:06:47 UTC | #1

Hello,
Is there any way to visualize / debug draw the software rasterized zbuffer?

Thanks.

-------------------------

cadaver | 2017-01-02 01:06:47 UTC | #2

Currently no. I used to have an internal hack for it. Probably would be best if it could copy the contents to a texture for debug rendering e.g. in the UI.

-------------------------

cadaver | 2017-01-02 01:06:48 UTC | #3

I've made some minor modifications to the master branch that allow public access to the occlusion. Rendering it can be done for example with a UI element (note that script bindings are unfortunately out of question due to the needed access to internal classes and raw arrays):

[code]
    /// Depth debug texture
    SharedPtr<Texture2D> occlusionTex_;
    /// Depth debug borderimage
    SharedPtr<BorderImage> occlusionElement_;

    // Setup:
    occlusionTex_ = new Texture2D(context_);
    occlusionElement_ = GetSubsystem<UI>()->GetRoot()->CreateChild<BorderImage>();
    occlusionElement_->SetTexture(occlusionTex_);

    // Per-frame update:
    OcclusionBuffer* buffer = GetSubsystem<Renderer>()->GetViewport(0)->GetView()->GetOcclusionBuffer();
    if (buffer)
    {
        unsigned w = buffer->GetWidth();
        unsigned h = buffer->GetHeight();
        if (w != occlusionTex_->GetWidth() || h != occlusionTex_->GetHeight())
        {
            occlusionTex_->SetNumLevels(1); // No mipmaps
            occlusionTex_->SetSize(w, h, Graphics::GetFloat32Format(), TEXTURE_DYNAMIC);
            occlusionElement_->SetSize(w, h);
        }
        int* depthInts = buffer->GetBuffer();
        float* depthFloats = new float[w * h];
        for (unsigned i = 0; i < w * h; ++i)
        {
            // Depth data is 24bit ints. Convert to float
            depthFloats[i] = depthInts[i] / (float)OCCLUSION_Z_SCALE;
        }
        occlusionTex_->SetData(0, 0, 0, w, h, depthFloats);
        delete[] depthFloats;
    }
[/code]

-------------------------

theak472009 | 2017-01-02 01:06:48 UTC | #4

Thanks for the very quick response

-------------------------

