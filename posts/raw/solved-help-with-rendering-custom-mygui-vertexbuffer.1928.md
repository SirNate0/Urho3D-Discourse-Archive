ViteFalcon | 2017-01-02 01:11:37 UTC | #1

Hi fellow Urho3D devs,

I'm very new to Urho3D and so far I'm loving it. I'm attempting to get MyGUI to work with Urho3D (because I really like that GUI library, Urho3D's UI would need more work to do what I'd like). I'm having a problem where the UI rendering doesn't show up. I have tried to debug it to the point where I'm out of ideas would really need your help.

So, to start off, I'll give a brief idea of how MyGUI 'platform' code works. For those who aren't familiar about MyGUI please search for MyGUI in your favorite search engine, or visit mygui-dot-info to visit their website (sorry, it seems like I'm not allowed to post a link in my first post).

MyGUI platform code needs some implementation of engine-specific code to get MyGUI integrated with your engine. These are (not real class/interface names):
[ul]
[li] [b]DataStream[/b]: A stream to the resource data[/li]
[li] [b]DataStreamManager[/b]: A singleton class that needs to be initialized before initializing MyGUI and gets used by MyGUI to retrieve data streams to the engine's resources[/li]
[li] [b]Texture[/b]: A class that implements interactions with the engine's texture (creating manual textures, loading existing textures from engine, etc)[/li]
[li] [b]VertexBuffer[/b]: A class that wraps interactions with the engine's vertex buffer implementation.[/li]
[li] [b]RenderTarget[/b]: A class that wraps the target to which MyGUI renders itself. This for Urho3D is [b]Urho3D::Renderer[/b] class.[/li]
[li] [b]RenderManager[/b]: A singleton class that MyGUI interacts with to create/delete VertexBuffers/textures to render them the default render target (or to any render target for that matter).[/li][/ul]

My RenderManager looks something like this:
[code]#include "MyGUI_UrhoRenderManager.h"
#include "MyGUI_UrhoRenderer.h"
#include "MyGUI_UrhoTexture.h"
#include "MyGUI_UrhoVertexBuffer.h"

#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/GraphicsEvents.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Graphics/Texture.h>
#include <Urho3D/Graphics/Texture2D.h>
#include <Urho3D/Graphics/View.h>
#include <Urho3D/Graphics/Viewport.h>
#include <Urho3D/Scene/SceneEvents.h>
#include <Urho3D/Urho2D/Drawable2D.h>

namespace MyGUI
{
	namespace detail
	{
		static const TextureUsage TEXTURE_USAGE = TextureUsage::RenderTarget;
		static const PixelFormat PIXEL_FORMAT = PixelFormat::R8G8B8A8;
	}

	UrhoRenderManager::UrhoRenderManager(Urho3D::Context* context)
		: Urho3D::Object(context)
		, mGraphics(*GetSubsystem<Urho3D::Graphics>())
		, mRenderer(*GetSubsystem<Urho3D::Renderer>())
		, mUiRenderer(new UrhoRenderer(context))
	{
		SubscribeToEvent(Urho3D::E_RENDERUPDATE, URHO3D_HANDLER(UrhoRenderManager, handleUpdate));
		SubscribeToEvent(Urho3D::E_ENDRENDERING, URHO3D_HANDLER(UrhoRenderManager, render));
	}

	IVertexBuffer * UrhoRenderManager::createVertexBuffer()
	{
		return new UrhoVertexBuffer(context_);
	}

	void UrhoRenderManager::destroyVertexBuffer(IVertexBuffer* _buffer)
	{
		delete _buffer;
	}

	MyGUI::ITexture* UrhoRenderManager::createTexture(const std::string& _name)
	{
		return new UrhoTexture(context_, _name);
	}

	void UrhoRenderManager::destroyTexture(ITexture* _texture)
	{
		delete _texture;
	}

	MyGUI::ITexture* UrhoRenderManager::getTexture(const std::string& _name)
	{
		auto texture = new UrhoTexture(context_, _name);
		texture->loadFromFile(_name);
		return texture;
	}

	const MyGUI::IntSize& UrhoRenderManager::getViewSize() const
	{
		static IntSize viewSize;
		static auto& graphics = *GetSubsystem<Urho3D::Graphics>();
		viewSize.width = graphics.GetWidth();
		viewSize.height = graphics.GetHeight();
		return viewSize;
	}

	VertexColourType UrhoRenderManager::getVertexFormat()
	{
		return VertexColourType(VertexColourType::ColourABGR);
	}

	bool UrhoRenderManager::isFormatSupported(PixelFormat _format, TextureUsage _usage)
	{
		bool isPixelFormatSupported = false;
		bool isTextureUsageSupported = true;
		switch (_format.getValue())
		{
		case PixelFormat::L8:
		case PixelFormat::L8A8:
		case PixelFormat::R8G8B8A8:
			isPixelFormatSupported = true;
		}
		return isPixelFormatSupported && isTextureUsageSupported;
	}

	void UrhoRenderManager::begin()
	{
		using namespace Urho3D;

		Vector2 invScreenSize(1.0f / (float)mGraphics.GetWidth(), 1.0f / (float)mGraphics.GetHeight());
		Vector2 scale(2.0f * invScreenSize.x_, -2.0f * invScreenSize.y_);
		Vector2 offset(-1.0f, 1.0f);

		projection = Matrix4::IDENTITY;

		projection.m00_ = scale.x_;
		projection.m03_ = offset.x_;
		projection.m11_ = scale.y_;
		projection.m13_ = offset.y_;
		projection.m22_ = 1.0f;
		projection.m23_ = 0.0f;
		projection.m33_ = 1.0f;

		noTextureVS = mGraphics.GetShader(VS, "Basic", "VERTEXCOLOR");
		diffTextureVS = mGraphics.GetShader(VS, "Basic", "DIFFMAP VERTEXCOLOR");
		noTexturePS = mGraphics.GetShader(PS, "Basic", "VERTEXCOLOR");
		diffTexturePS = mGraphics.GetShader(PS, "Basic", "DIFFMAP VERTEXCOLOR");
		diffMaskTexturePS = mGraphics.GetShader(PS, "Basic", "DIFFMAP ALPHAMASK VERTEXCOLOR");
		alphaTexturePS = mGraphics.GetShader(PS, "Basic", "ALPHAMAP VERTEXCOLOR");

		mGraphics.ClearParameterSources();
		mGraphics.SetColorWrite(true);
		mGraphics.SetCullMode(Urho3D::CULL_NONE);
		mGraphics.SetDepthTest(Urho3D::CMP_ALWAYS);
		mGraphics.SetDepthWrite(false);
		mGraphics.SetFillMode(Urho3D::FILL_SOLID);
		mGraphics.SetStencilTest(false);
		mGraphics.ResetRenderTargets();
		mGraphics.SetBlendMode(Urho3D::BlendMode::BLEND_ALPHA);
		mGraphics.SetScissorTest(false);
		mGraphics.SetViewport(GetSubsystem<Renderer>()->GetViewport(0)->GetRect());
		// MyGUI doesn't create / need index buffers
		mGraphics.SetIndexBuffer(nullptr);
	}

	void UrhoRenderManager::end()
	{
	}

	void UrhoRenderManager::doRender(IVertexBuffer * _buffer, ITexture * _texture, size_t _count)
	{
		mUiRenderer->doRender(_buffer, _texture, _count);
	}

	const RenderTargetInfo & UrhoRenderManager::getInfo()
	{
		static RenderTargetInfo info;
		info.aspectCoef = float(mGraphics.GetWidth()) / float(mGraphics.GetHeight());
		// Depth range for OpenGL is [-1.0f, 1.0f]
		info.maximumDepth = 1.0f;
		info.pixScaleX = Urho3D::PIXEL_SIZE;
		info.pixScaleY = Urho3D::PIXEL_SIZE;
		return info;
	}

	void UrhoRenderManager::handleUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap & eventData)
	{
		using namespace Urho3D;
		using namespace RenderUpdate;
		auto deltaTime = eventData[P_TIMESTEP].GetFloat();
		onFrameEvent(deltaTime);
	}

	void UrhoRenderManager::render(Urho3D::StringHash eventType, Urho3D::VariantMap & eventData)
	{
		begin();
		onRenderToTarget(this, true);
		end();
	}
}[/code]

I have verified that:
[ul]
[li]All textures are getting loaded correctly[/li]
[li]Vertex buffer contents seems to be correct[/li]
[li]Rendering calls do happen before the buffers are swapped[/li][/ul]

Is there anything that I'm grossly missing? Am I doing something incredibly stupid, which is making this not work? Thanks a lot for your time.

P.S.: I'm currently only focusing on getting this to work with OpenGL renderer.

-------------------------

cadaver | 2017-01-02 01:11:37 UTC | #2

Welcome to the forums.

You're not showing all of your code -- e.g. how the vertex buffer is bound and how you actually issue the draw call. I recommend ruling out things one by one - for example first verifying that a simple hardcoded quad comes up right, then replace that with MyGUI supplied data. Or first use no textures, or the "replace" blend mode, then substitute those with the proper ones. If you were using Direct3D you could use graphics analysis tools like Pix, but for OpenGL the tools are poorer. Not sure if e.g. gDebugger could actually show the mesh you're about to render, similar to how Pix can.

-------------------------

ViteFalcon | 2017-01-02 01:11:41 UTC | #3

Sorry for the late reply. I was on vacation and had very little time to reply.

[quote="cadaver"]Welcome to the forums.[/quote]

Thanks!

[quote="cadaver"]You're not showing all of your code -- e.g. how the vertex buffer is bound and how you actually issue the draw call.[/quote]

Oops! Here's the relevant code:

[code]
	void UrhoRenderer::doRender(IVertexBuffer* _buffer, ITexture* _texture, size_t _count)
	{
		using namespace Urho3D;
		MyGUI::GlErrorHandler glErrors;
		auto vs = noTextureVS;
		auto ps = noTexturePS;
		if (_texture != nullptr)
		{
			vs = diffTextureVS;
			ps = diffTexturePS;
			mGraphics.SetTexture(0, dynamic_cast<UrhoTexture*>(_texture)->getTexture());
		}
		mGraphics.SetShaders(vs, ps);
		if (mGraphics.NeedParameterUpdate(SP_OBJECT, this))
			mGraphics.SetShaderParameter(VSP_MODEL, Matrix3x4::IDENTITY);
		if (mGraphics.NeedParameterUpdate(SP_CAMERA, this))
			mGraphics.SetShaderParameter(VSP_VIEWPROJ, projection);
		if (mGraphics.NeedParameterUpdate(SP_MATERIAL, this))
			mGraphics.SetShaderParameter(PSP_MATDIFFCOLOR, Color(1.0f, 1.0f, 1.0f, 1.0f));
		mGraphics.SetVertexBuffer(dynamic_cast<UrhoVertexBuffer*>(_buffer)->getBuffer());
		if (glErrors)
		{
			log.Error(ToString("GL ERROR: %s", glErrors.getError().c_str()));
		}
		mGraphics.Draw(Urho3D::PrimitiveType::TRIANGLE_LIST, 0, (unsigned int)_count);
		if (glErrors)
		{
			log.Error(ToString("GL ERROR: %s", glErrors.getError().c_str()));
		}
	}
[/code]

[quote="cadaver"]I recommend ruling out things one by one - for example first verifying that a simple hardcoded quad comes up right, then replace that with MyGUI supplied data. Or first use no textures, or the "replace" blend mode, then substitute those with the proper ones.[/quote]
Good suggestion. I'll try them out and let you know the details below:

[ul]
[li] [b]Hardcoded quad[/b]: TODO[/li]
[li] [b]Use no texture[/b]: TODO[/li]
[li] [b]Use 'replace' blend mode[/b]: TODO[/li][/ul]

[quote="cadaver"]If you were using Direct3D you could use graphics analysis tools like Pix, but for OpenGL the tools are poorer. Not sure if e.g. gDebugger could actually show the mesh you're about to render, similar to how Pix can.[/quote]
I'll give that a try anyway.

-------------------------

ViteFalcon | 2017-01-02 01:11:43 UTC | #4

Okay, so I figured out the problem. It had to do with the projection matrix. It seems like the projection matrix that works for MyGUI is the following:
[code]
        auto width = mGraphics.GetWidth();
        auto height = mGraphics.GetHeight();
        Vector2 invScreenSize(1.0f / float(width), 1.0f / float(height));
        Vector2 scale(1.0f * invScreenSize.x_, 1.0f * invScreenSize.y_);
        Vector2 offset(-1.0f, 1.0f);

        projection.m00_ = scale.x_;
        projection.m03_ = offset.x_;
        projection.m11_ = scale.y_;
        projection.m13_ = offset.y_;
        projection.m22_ = 1.0f;
        projection.m23_ = 0.0f;
        projection.m33_ = 1.0f;
[/code]

Instead of my previous implementation (which was borrowed from Urho3D::UI:
[code]
      Vector2 invScreenSize(1.0f / (float)mGraphics.GetWidth(), 1.0f / (float)mGraphics.GetHeight());
      Vector2 scale(2.0f * invScreenSize.x_, -2.0f * invScreenSize.y_);
      Vector2 offset(-1.0f, 1.0f);

      projection = Matrix4::IDENTITY;

      projection.m00_ = scale.x_;
      projection.m03_ = offset.x_;
      projection.m11_ = scale.y_;
      projection.m13_ = offset.y_;
      projection.m22_ = 1.0f;
      projection.m23_ = 0.0f;
      projection.m33_ = 1.0f;
[/code]

Thanks, Cadaver! Your tip of using gDEBugger actually panned out. I didn't create a custom vertex buffer. Instead, I went with gDEBugger and found that the vertex coordinates in the vertex buffer populated by MyGUI was in 'window' space I guess. So I tweaked the projection matrix accordingly.

-------------------------

