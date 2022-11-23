bbm | 2017-01-02 01:14:27 UTC | #1

I do something like this

[code]
            for(int i = 0; i < renderPath->GetNumCommands(); ++i){
                RenderPathCommand *command = renderPath->GetCommand(i);
                if(command->type_ == CMD_CLEAR) {
                    command->clearColor_ = Color(0, 0, 0, 0);
                }
                for(int outputIndex = 0; outputIndex < command->GetNumOutputs(); ++outputIndex){
                    if(command->GetOutputName(outputIndex) == "viewport" || command->GetOutputName(outputIndex) == "") {
                        command->SetOutputName(outputIndex, mViewportTexture->GetName());
                    }
                }
                static_assert(TU_DIFFUSE == 0, "diffuse is not first texture");
                for(TextureUnit inputIndex = TU_DIFFUSE; inputIndex < MAX_TEXTURE_UNITS; inputIndex = (TextureUnit)((int)inputIndex+1)){
                    if(command->GetTextureName(inputIndex) == "viewport") {
                        command->SetTextureName(inputIndex, mViewportTexture->GetName());
                    }
                }
            }
[/code]

to draw everything to mViewportTexture which is created like this

[code]
            mViewportTexture->SetSize(
                width,
                height,
                GL_RGBA, TEXTURE_RENDERTARGET);
[/code]

this is my final RenderPathCommand which takes the special viewport texture and sends to the viewport which already has the camera background. 

[code]
            command = RenderPathCommand();
            command.tag_                        = "InterestingCommand";
            command.enabled_                    = true;
            command.textureNames_[TU_DIFFUSE]   = mViewportTexture->GetName();
            command.type_                       = CMD_QUAD;
            command.pixelShaderDefines_         = "DIFFMAP";
            command.vertexShaderDefines_        = "DIFFMAP";
            command.vertexShaderName_           = "InterestingPass";
            command.pixelShaderName_            = "InterestingPass";
            command.SetNumOutputs(1);
            command.SetOutputName(0, "viewport");
            command.shaderParameters_["InterestingParam"]      = 3.0f;
            command.blendMode_ = BLEND_PREMULALPHA;
            renderPath->AddCommand(command);
[/code]

The problem the background is all black. My issue is that in mViewportTexture alpha is 1.0 (fully opaque) everywhere. I did specify GL_RGBA. I have a background texture that is updated based on camera and want to apply a shader that only applies on the final rendered scene and not the background texture. Checking for black pixels in the shader is no good because then everything has a black bolder as it alpha blends into the background. Is there something I'm missing?

Thank you.

-------------------------

cadaver | 2017-01-02 01:14:27 UTC | #2

This will need to be checked. It can be a render (blend) state oversight that prevents the alpha being written to properly.

-------------------------

bbm | 2017-01-02 01:14:27 UTC | #3

[code]
            // redirect all viewport to this special buffer
            for(int i = 0; i < renderPath->GetNumCommands(); ++i){
                RenderPathCommand *command = renderPath->GetCommand(i);
                if(command->type_ == CMD_CLEAR) {
                    command->clearColor_ = Color(0, 0, 0, 0);
                    command->clearFlags_ |= CLEAR_COLOR | CLEAR_DEPTH;
                    command->useFogColor_ = false;
                } else {
                    command->blendMode_ = BLEND_PREMULALPHA;
                }
                for(int outputIndex = 0; outputIndex < command->GetNumOutputs(); ++outputIndex){
                    if(command->GetOutputName(outputIndex) == "viewport" || command->GetOutputName(outputIndex) == "") {
                        command->SetOutputName(outputIndex, mViewportTexture->GetName());
                    }
                }
                static_assert(TU_DIFFUSE == 0, "diffuse is not first texture");
                for(TextureUnit inputIndex = TU_DIFFUSE; inputIndex < MAX_TEXTURE_UNITS; inputIndex = (TextureUnit)((int)inputIndex+1)){
                    if(command->GetTextureName(inputIndex) == "viewport") {
                        command->SetTextureName(inputIndex, mViewportTexture->GetName());
                    }
                }
            }
[/code]

notice the fog color is disabled. I browsed the code and noticed the fog color was used instead of my specified clearcolor. And fog color was black. I don't think I have specified any fog. Doing above worked.

Here is code in Urho3D

[code]
            case CMD_CLEAR:
                {
                    URHO3D_PROFILE(ClearRenderTarget);

                    Color clearColor = command.clearColor_;
                    if (command.useFogColor_)
                        clearColor = actualView->farClipZone_->GetFogColor();

                    SetRenderTargets(command);
                    graphics_->Clear(command.clearFlags_, clearColor, command.clearDepth_, command.clearStencil_);
                }
                break;

[/code]

-------------------------

cadaver | 2017-01-02 01:14:27 UTC | #4

Where are you getting your renderpath from? Almost all of the preprovided ones in Urho clear to the fog color, so if you're using & modifying those it's indeed necessary to set useFogColor_ false manually.

-------------------------

bbm | 2017-01-02 01:14:29 UTC | #5

I'm getting all the renderpaths from the default and just modifying them. Everything is good with Urho3D. Post above was me just showing my process on how I found how to fix my problem.

Thank you.

-------------------------

