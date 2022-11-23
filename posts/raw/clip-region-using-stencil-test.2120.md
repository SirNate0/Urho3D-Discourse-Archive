unique_jack | 2017-01-02 01:13:16 UTC | #1

Rather than using the scissor test for clipping a region I'd like to use the stencil test since I'd like to transform it.
This is the code I've been writing so far:

[code]            graphics->SetStencilTest(true);
            graphics->SetColorWrite(false);

            Urho3D::VertexBuffer vertices(context_);
            vertices.SetSize(4, Urho3D::MASK_POSITION, true);

            float* vBuf = (float*) vertices.Lock(0, 4, true);
            // Vertex 1
            vBuf[0] = scissors_.left_;
            vBuf[1] = scissors_.top_;
            vBuf[2] = 0.f;
            // Vertex 2
            vBuf[3] = scissors_.left_;
            vBuf[4] = scissors_.bottom_;
            vBuf[5] = 0.f;
            // Vertex 3
            vBuf[6] = scissors_.right_;
            vBuf[7] = scissors_.bottom_;
            vBuf[8] = 0.f;
            // Vertex 4
            vBuf[9] = scissors_.right_;
            vBuf[10] = scissors_.top_;
            vBuf[11] = 0.f;

            vertices.Unlock();

            Urho3D::IndexBuffer indices(context_);
            indices.SetSize(4, true);

            int* iBuf = (int*)indices.Lock(0, 4, true);
            iBuf[0] = 1;
            iBuf[1] = 2;
            iBuf[2] = 0;
            iBuf[3] = 3;
            indices.Unlock();
            
            graphics->SetVertexBuffer(&vertices);
            graphics->SetIndexBuffer(&indices);

            // Render using Stencil Shader
            graphics->SetShaders(vs, ps);

            if (graphics->NeedParameterUpdate(Urho3D::SP_OBJECT, this))
                graphics->SetShaderParameter(Urho3D::VSP_MODEL, Urho3D::Matrix3x4(stack_.Back()));
            if (graphics->NeedParameterUpdate(Urho3D::SP_CAMERA, this))
                graphics->SetShaderParameter(Urho3D::VSP_VIEWPROJ, projection);

            graphics->Draw(Urho3D::TRIANGLE_STRIP, 0, 4, 0, 4);

            graphics->SetColorWrite(true);
            
            // Render textures using 2D shader...
[/code]
However it doesn't seem to work, the texture is always visible, maybe I forgot to set some other stuff?

-------------------------

cadaver | 2017-01-02 01:13:16 UTC | #2

You need more parameters for the stencil test, ie. what ref value you are writing to the stencil in the write phase, and how you're testing in the compare phase.

See Renderer::OptimizeLightByStencil for an example.

-------------------------

