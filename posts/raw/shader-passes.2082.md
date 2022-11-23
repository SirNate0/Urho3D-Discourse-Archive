codder | 2017-01-02 01:12:53 UTC | #1

Hello,

I want to use two passes on some custom vertices.
What I could not figure out is this scheme:

graphics->SetShaderParameter(....)
graphics->Draw(....)
// How to have the first processed vertices as input on the second draw call?
graphics->SetShaderParameter(...)
graphics->Draw(...)

I don't want to have dependency on the scene/camera to create a rendertarget.
Is there a way to work on this low level and have the processed data as input on the new draw call?

-------------------------

cadaver | 2017-01-02 01:12:53 UTC | #2

If you mean transform feedback, that isn't implemented in Urho.

-------------------------

codder | 2017-01-02 01:12:54 UTC | #3

Basically the shader just modify fragment uniforms, so what change effectively are pixels and not vertex.
But again what comes to my mind is RenderTarget with Scene/Camera/Material/etc.. dependency.
I draw vertices without creating any material for them and I don't know how to capture drawed pixels.

graphics->SetVertexBuffer(vBuff);
graphics->SetIndexBuffer(iBuff);
graphics->SetShaders(vs, ps);

graphics->SetShaderParameter("EffectAmount", effectAmount);
graphics->Draw(Urho3D::TRIANGLE_LIST, 0, iBuff->GetIndexCount(), 0, vBuff->GetVertexCount());

-------------------------

cadaver | 2017-01-02 01:12:54 UTC | #4

Ah, now I understand. You want to do the same as what the renderpath post-process chain does automatically. Sampling & writing to same rendertarget is illegal, so you need to have 2 rendertarget textures and do:

- Set rendertarget 1
- Render pass 1
- Set rendertarget 2
- Assign rendertarget 1 to some texture unit (SetTexture)
- Sample the texture unit when rendering pass 2

-------------------------

codder | 2017-01-02 01:12:55 UTC | #5

First of all all my code is executed in an E_ENDRENDERING event.

I have some issues:

Adding just:
SharedPtr<Texture2D> renderTexture(new Texture2D(context_));
renderTexture->SetSize(size.x_, size.y_, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
...
graphics->Draw(....);

Invalidates the Draw call which doesn't draw anything.
The issue seems to be with SetSize.

-------------------------

