simple | 2017-01-02 01:01:33 UTC | #1

Hello i made SpriteBatch class which are almost same like in XNA or D3DXSprite.

How to use this:
[code]
spritebatch = new SpriteBatch(context);
spritebatch->Initialize();
[/code]
these lines you must have to write somewhere in Start();
Initialize(numBatchs,numQuads); just create vertexbuffers and adding events.
numBatchs - maximum of texture changes.
numQuads - maximum of quads, possible maximum is 16300.

How to render (write this somewhere in OnHandleSceneUpdate):
[code]
// start draw
spritebatch->Begin();
// set a blend
spritebatch->SetBlendMode(BLEND_ALPHA);
// draw a texture
spritebatch->Draw(texture,Rect(0,0,100,100),Rect(0,0,256,256),color);
spritebatch->Draw(texture,Rect(100,100,200,200),Rect(0,0,256,256),rotation,origin,scale,color,SpriteBatch::SBFX_NONE);
// draw a text
spritebatch->DrawString(font,24,Vector2(10,10),"Hello World",11,color,SpriteBatch::TFX_NONE);
// draw a center text
spritebatch->DrawString(font,24,Vector2(400,10),"Hello World",11,color,SpriteBatch::TFX_HCENTER);
// draw a text using L"<text>" thing, because use TFX_UNICODE16.
spritebatch->DrawString(font,24,Vector2(10,10),L"Hello World",11,color,SpriteBatch::TFX_UNICODE16);
// draw a frame from texture from rect (0,0,96,96) and with borders (32,32,32,32)
spritebatch->DrawFrame(texture,Rect(200,200,300,300),Rect(0,0,96,96),Rect(32,32,32,32),color);
// end of draw
spritebatch->End();
[/code]
Draw() - function draw a texture.
DrawString() - function draw a text (ttf working weird, only works with bitmapfonts 32bit).
DrawFrame() - draw a frame.

Auto rescaling functions: (write somewhere around initialize() )
[code]
// now sprites will be rescaled to 800,600 and centrize if needed (similar like in flashplayer).
spritebatch->SetScreenSize(800,600);
// convert screen positions to rescaled position
Vector2 rs = spritebatch->GetPointTo(Vector2(mousex,mousey));
// convert rescaled position to screen position
Vector2 s = spritebatch->GetPointFrom(Vector2(0,0));
[/code]

Modifying exist draw() functions.
[code]
spritebatch->PushModifier();
spritebatch->Draw(texture,Rect(0,0,100,100),Rect(0,0,256,256),color);
// do gradient
spritebatch->ModifyGradientH(Color::WHITE,Color::RED);
// transformations
spritebatch->ModifyPRS(position,rotation,scale);
// etc
spritebatch->PopModifier();
[/code]

sorry for english.
[drive.google.com/file/d/0B-0l27 ... 9kNFk/view](https://drive.google.com/file/d/0B-0l276DEh6XTVBCZTUzR19kNFk/view)

-------------------------

v0van1981 | 2017-01-02 01:02:14 UTC | #2

How to drawing under UI? Is there any way draw 3d model over SpriteBatch?

-------------------------

Hevedy | 2017-01-02 01:02:15 UTC | #3

[quote="v0van1981"]How to drawing under UI? Is there any way draw 3d model over SpriteBatch?[/quote]

This looks like a problem with vector3 z ?
No idea, but looks like the engine use z in 2D like a depth pos and all vector3 in this code point to 0 and the camera is in -10.0f ?

-------------------------

v0van1981 | 2017-01-02 01:05:38 UTC | #4

I'm trying to modify the code so that the spritebatch does not overlap models in 3d space. (I'm trying to enable depth test.)

SpriteBatch.h
[code]#ifndef _SPRITEBATCH_H_
#define _SPRITEBATCH_H_

#include <vector>

namespace Urho3D
{
	class	Texture2D;
	class	Font;
	class	VertexBuffer;
	class	IndexBuffer;
	class	Graphics;
	class	SpriteBatch : public Object
	{
		public:
			OBJECT(SpriteBatch);

		public:
			struct		VERTEX
			{
				Vector3		pos;
				int			color;
				Vector2		uv;
			};
			struct		BATCH
			{
				SharedPtr<Texture2D>	pTexture;
				int						iBlendMode;
				unsigned int			iStart,iCount;
			};
			enum
			{
				SBFX_NONE			=	0,
				SBFX_FLIPH			=	1,
				SBFX_FLIPV			=	2,
				SBFX_FLIPHV			=	3,
			};
			enum
			{
				TFX_NONE			=	0,
				TFX_VTOP			=	0,
				TFX_VCENTER			=	1,
				TFX_VBOTTOM			=	2,
				TFX_HLEFT			=	0,
				TFX_HCENTER			=	4,
				TFX_HRIGHT			=	8,
				TFX_UNICODE16		=	16,
			};

		public:
			SpriteBatch(Context *context);
			virtual ~SpriteBatch();
		public:
			// Size of screen where sprites will be drawn.
			// If width,height are lower than graphics->width,graphics->height
			// then class automatic rescale up and centrize (similar like in flashplayer).
			// if width,height will be 0, then graphics->width,graphis->height will be set.
			void						SetScreenSize(float fWidth=800,float fHeight=600);
			// convert screen positions to rescaled position
			Vector2						GetPointTo(const Vector2 &screen);
			// convert rescaled position to screen position
			Vector2						GetPointFrom(const Vector2 &view);

			// start modify sprites
			void						PushModifier();
			// modify sprites, modify functions must be between PushModifier()...Draw()...<here>...PopModifier().
			bool						ModifyPRS(const Vector2 &pos=Vector2::ZERO,float rotation=0,const Vector2 &scale=Vector2::ONE);
			bool						ModifyTransform(const Matrix4 &matrix);
			bool						ModifyColor(const Color &color=Color::WHITE);
			bool						ModifyGradientH(const Color &color_up=Color::WHITE,const Color &color_down=Color::RED);
			bool						ModifyGradientV(const Color &color_lf=Color::WHITE,const Color &color_rg=Color::RED);
			// end of modify sprites
			void						PopModifier();

			// initialize, create vertexbuffer and add event to render, must be called after constructor.
			bool						Initialize(unsigned int iBatchMax=512,unsigned int iQuadsMax=16300);
			// begin()...end() between them, must be all Draw() functions
			bool						Begin();
			// change blendmode
			void						SetBlendMode(int blendmode);
			// draw sprite
			bool						Draw(Texture2D *texture,const Rect &dest,const Color &color);
			bool						Draw(Texture2D *texture,const Rect &dest,const Rect &src,const Color &color);
			bool						Draw(Texture2D *texture,const Rect &dest,const Rect &src,const Color &color,float rotation,const Vector2 &origin=Vector2::ZERO,const Vector2 &scale=Vector2::ONE,int SpriteEffect = SBFX_NONE);
			bool						Draw(Texture2D *texture,const Vector2 &dest,const Color &color);
			bool						Draw(Texture2D *texture,const Vector2 &dest,const Rect &src,const Color &color);
			bool						Draw(Texture2D *texture,const Vector2 &dest,const Rect &src,const Color &color,float rotation,const Vector2 &origin=Vector2::ZERO,const Vector2 &scale=Vector2::ONE,int SpriteEffect = SBFX_NONE);

			// get x-size in pixels of textline
			float						GetWidthString(Font *font,int fontsize,const void *text,unsigned int textlength,int TextEffect = TFX_NONE);
			// get y-size in pixels of text
			float						GetHeightString(Font *font,int fontsize,const void *text,unsigned int textlength,int TextEffect = TFX_NONE);
			// draw text (TTF may not working like expected, tested only on bitmapfonts with 32bit color)
			// if texteffect will be TFX_UNICODE16 then text parameter must be: L"HelloWorld"
			bool						DrawString(Font *font,int fontsize,const Vector2 &dest,const void *text,unsigned int textlength,const Color &color,int TextEffect = TFX_NONE);
			// draw text with transformations (TTF may not working like expected, tested only on bitmapfonts with 32bit color)
			bool						DrawString(Font *font,int fontsize,const Vector2 &dest,const void *text,unsigned int textlength,const Color &color,float rotation,const Vector2 &origin=Vector2::ZERO,const Vector2 &scale=Vector2::ONE,int TextEffect = TFX_NONE);

			// draw frame (drawframe(tex,Rect(0,0,100,100),Rect(0,0,96,96),Rect(32,32,32,32),color::white)
			void						DrawFrame(Texture2D *texture,const Rect &dest,const Rect &src,const Rect &borders,const Color &color);
			// begin()...end() between them, must be all Draw() functions
			void						End();
			void SetView(Camera* camera, Engine* engine);

			void						OnRender(StringHash eventType, VariantMap& eventData);

		protected:

		private:
			BATCH*						GetBatch(Texture2D *texture,int iBlendMode);
			static float				CalculateFixedScreenSize(float sw,float sh,float vw,float vh,float *ret);

			std::vector<unsigned int>	modifiers_;
			Graphics*					graphics_;
			SharedPtr<VertexBuffer>		vb_;
			BATCH*						batch_;
			unsigned int				maxbatch_,maxquads_,ibatch_,icount_;
			VERTEX*						vertex_;
			int							blendmode_;
			float						viewWidth_,viewHeight_;
			float						viewCalc_[5];

			Camera* camera_;
			Engine* engine_;

	};

};

#endif
[/code]

SpriteBatch.cpp
[code]#include "stdafx.h"
#include "SpriteBatch.h"

#include <stdio.h>

namespace Urho3D
{
	static	int			 g_iIB = 0;
	static	IndexBuffer	*g_pIB = 0;

	SpriteBatch::SpriteBatch(Context *context) : Object(context)
	{
		blendmode_ = BLEND_ALPHA;
		vertex_ = 0;
		graphics_ = 0;
		batch_ = 0;
		maxbatch_ = maxquads_ = ibatch_ = icount_ = 0;
		viewWidth_ = 800;
		viewHeight_ = 600;
		viewCalc_[0] = viewCalc_[1] = 0;
		viewCalc_[2] = 800;	viewCalc_[3] = 600;	viewCalc_[4] = 1;

		if (g_iIB == 0)
		{
			// only one time we create indexbuffer for save memory
			g_pIB = new IndexBuffer(context);
			g_pIB->SetShadowed(true);
			g_pIB->SetSize(16300 * 6, false);
			unsigned short *index = (unsigned short *)g_pIB->Lock(0, 16300 * 6);
			if (index)
			{
				int s = 0;
				for (unsigned int i = 0; i < 16300; i++)
				{
					index[(i * 6) + 0] = s + 0;		index[(i * 6) + 1] = s + 1;		index[(i * 6) + 2] = s + 2;
					index[(i * 6) + 3] = s + 2;		index[(i * 6) + 4] = s + 1;		index[(i * 6) + 5] = s + 3;
					s += 4;
				};
			};
			g_pIB->Unlock();
		};
		g_iIB++;
	}

	SpriteBatch::~SpriteBatch()
	{
		UnsubscribeFromEvent(graphics_, E_ENDRENDERING);
		modifiers_.clear();
		if (batch_) delete[] batch_;
		vb_.Reset();

		g_iIB--;
		if (g_iIB <= 0)
		{
			if (g_pIB) delete g_pIB;
			g_pIB = 0;
			g_iIB = 0;
		};
	}

	SpriteBatch::BATCH* SpriteBatch::GetBatch(Texture2D *texture, int iBlendMode)
	{
		if (icount_ >= (maxquads_ - 1) * 4 || texture == 0) return 0;
		BATCH *b = &batch_[ibatch_];
		if (b->pTexture == texture && b->iBlendMode == iBlendMode) return b;
		if (ibatch_ >= maxbatch_) return 0;
		ibatch_++;
		batch_[ibatch_].pTexture = texture;
		batch_[ibatch_].iBlendMode = iBlendMode;
		batch_[ibatch_].iStart = icount_;
		batch_[ibatch_].iCount = 0;
		return &batch_[ibatch_];
	};

	float SpriteBatch::CalculateFixedScreenSize(float sw, float sh, float vw, float vh, float *ret)
	{
		float sAspect = sw / sh;
		float vAspect = vw / vh;
		float scale = 1;

		ret[0] = ret[1] = 0;  ret[2] = vw;  ret[3] = vh;
		if (sAspect > vAspect)
		{
			scale = sh / vh;
			ret[0] = (sw - vw*scale)*0.5f;
		}
		else if (sAspect < vAspect) {
			scale = sw / vw;
			ret[1] = (sh - vh*scale)*0.5f;
		}
		else {
			scale = sw / vw;
		};
		ret[2] *= scale; ret[3] *= scale;
		ret[4] = scale;

		//glViewport(ret[0], ret[1], ret[2], ret[3]);
		//glOrtho(0,0,vw,vh);
		return scale;
	};

	Vector2 SpriteBatch::GetPointTo(const Vector2 &screen)
	{
		return Vector2((screen.x_ - viewCalc_[0]) * (1.0f / viewCalc_[4]), (screen.y_ - viewCalc_[1]) * (1.0f / viewCalc_[4]));
	};

	Vector2 SpriteBatch::GetPointFrom(const Vector2 &view)
	{
		return Vector2((view.x_*viewCalc_[4]) + viewCalc_[0], (view.y_*viewCalc_[4]) + viewCalc_[1]);
	};

	bool SpriteBatch::Begin()
	{
		ibatch_ = icount_ = 0;
		if (!vertex_) vertex_ = (VERTEX *)vb_->Lock(0, maxquads_ * 4);
		return (vertex_ != 0);
	};

	void SpriteBatch::End()
	{
		if (vertex_)
		{
			vb_->Unlock();
			vertex_ = 0;
		};
	};

	void SpriteBatch::SetBlendMode(int blendmode)
	{
		blendmode_ = blendmode;
	};

	bool SpriteBatch::Draw(Texture2D *texture, const Rect &dest, const Color &color)
	{
		if (!texture) return false;
		float w = (float)texture->GetWidth();
		float h = (float)texture->GetHeight();
		return Draw(texture, dest, Rect(0, 0, w, h), color);
	};

	bool SpriteBatch::Draw(Texture2D *texture, const Rect &dest, const Rect &src, const Color &color)
	{
		if (color.a_ <= 0) return true;
		BATCH *batch = GetBatch(texture, blendmode_);
		if (!batch) return false;

		vertex_[icount_ + 0].pos = Vector3(dest.min_.x_, dest.min_.y_, icount_ * -0.0001f);
		vertex_[icount_ + 1].pos = Vector3(dest.max_.x_, dest.min_.y_, icount_ * -0.0001f);
		vertex_[icount_ + 2].pos = Vector3(dest.min_.x_, dest.max_.y_, icount_ * -0.0001f);
		vertex_[icount_ + 3].pos = Vector3(dest.max_.x_, dest.max_.y_, icount_ * -0.0001f);

		vertex_[icount_ + 0].color = vertex_[icount_ + 1].color = vertex_[icount_ + 2].color = vertex_[icount_ + 3].color = color.ToUInt();

		float w = 1.0f / (float)texture->GetWidth();
		float h = 1.0f / (float)texture->GetHeight();

		vertex_[icount_ + 0].uv = Vector2(src.min_.x_*w, src.min_.y_*h);
		vertex_[icount_ + 1].uv = Vector2(src.max_.x_*w, src.min_.y_*h);
		vertex_[icount_ + 2].uv = Vector2(src.min_.x_*w, src.max_.y_*h);
		vertex_[icount_ + 3].uv = Vector2(src.max_.x_*w, src.max_.y_*h);

		icount_ += 4;
		batch->iCount += 4;
		return true;
	};

	bool SpriteBatch::Draw(Texture2D *texture, const Rect &dest, const Rect &src, const Color &color, float rotation, const Vector2 &origin, const Vector2 &scale, int SpriteEffect)
	{
		if (color.a_ <= 0) return true;
		BATCH *batch = GetBatch(texture, blendmode_);
		if (!batch) return false;

		Vector2 startxy = -origin;
		Vector2 toxy = startxy + dest.Size();

		vertex_[icount_ + 0].pos = Vector3(startxy.x_, startxy.y_, icount_ * 0.0001f);
		vertex_[icount_ + 1].pos = Vector3(toxy.x_, startxy.y_, icount_ * 0.0001f);
		vertex_[icount_ + 2].pos = Vector3(startxy.x_, toxy.y_, icount_ * 0.0001f);
		vertex_[icount_ + 3].pos = Vector3(toxy.x_, toxy.y_, icount_ * 0.0001f);

		Matrix4 m(Matrix4::IDENTITY);
		m.m00_ = cosf(rotation) * scale.x_;		m.m10_ = sinf(rotation) * scale.x_;
		m.m01_ = -sinf(rotation) * scale.y_;	m.m11_ = cosf(rotation) * scale.y_;
		m.m03_ = dest.min_.x_;					m.m13_ = dest.min_.y_;
		for (int i = 0; i < 4; i++)	vertex_[icount_ + i].pos = m * vertex_[icount_ + i].pos;

		vertex_[icount_ + 0].color = vertex_[icount_ + 1].color = vertex_[icount_ + 2].color = vertex_[icount_ + 3].color = color.ToUInt();

		float w = 1.0f / (float)texture->GetWidth();
		float h = 1.0f / (float)texture->GetHeight();

		Vector2 uv1 = src.min_;
		Vector2 uv2 = src.max_;
		if (SpriteEffect & SBFX_FLIPH) { uv1.x_ = src.max_.x_; uv2.x_ = src.min_.x_; };
		if (SpriteEffect & SBFX_FLIPV) { uv1.y_ = src.max_.y_; uv2.y_ = src.min_.y_; };

		vertex_[icount_ + 0].uv = Vector2(uv1.x_*w, uv1.y_*h);
		vertex_[icount_ + 1].uv = Vector2(uv2.x_*w, uv1.y_*h);
		vertex_[icount_ + 2].uv = Vector2(uv1.x_*w, uv2.y_*h);
		vertex_[icount_ + 3].uv = Vector2(uv2.x_*w, uv2.y_*h);

		icount_ += 4;
		batch->iCount += 4;
		return true;
	};

	bool SpriteBatch::Draw(Texture2D *texture, const Vector2 &xy, const Color &color)
	{
		if (!texture) return false;
		Rect dest(xy.x_, xy.y_, xy.x_ + (float)texture->GetWidth(), xy.y_ + (float)texture->GetHeight());
		return Draw(texture, dest, color);
	};

	bool SpriteBatch::Draw(Texture2D *texture, const Vector2 &xy, const Rect &src, const Color &color)
	{
		Rect dest(xy.x_, xy.y_, xy.x_ + src.Size().x_, xy.y_ + src.Size().y_);
		return Draw(texture, dest, src, color);
	};

	bool SpriteBatch::Draw(Texture2D *texture, const Vector2 &xy, const Rect &src, const Color &color, float rotation, const Vector2 &origin, const Vector2 &scale, int SpriteEffect)
	{
		Rect dest(xy.x_, xy.y_, xy.x_ + src.Size().x_, xy.y_ + src.Size().y_);
		return Draw(texture, dest, src, color, rotation, origin, scale, SpriteEffect);
	};

	float SpriteBatch::GetHeightString(Font *font, int fontsize, const void *text, unsigned int textlength, int TextEffect)
	{
		if (font == 0 || text == 0 || ((const char *)text)[0] == 0 || textlength == 0) return 0;
		FontFace *face = font->GetFace(fontsize);
		if (!face) return 0;

		float								row = (float)face->GetRowHeight();
		float								H = row;
		unsigned int						i = 0, chr = 0;

		if (TextEffect & TFX_UNICODE16) textlength *= 2;
		for (i = 0; i < textlength;)
		{
			chr = ((const char *)text)[i++];
			if (TextEffect & TFX_UNICODE16) chr |= (((const char *)text)[i++]) << 8;
			if (chr == 0) break;
			if (chr == 0x0A) { H += row; continue; };
		};
		if (TextEffect & TFX_VCENTER) return H*0.5f;
		if (TextEffect & TFX_VBOTTOM) return H;
		return H;
	};

	float SpriteBatch::GetWidthString(Font *font, int fontsize, const void *text, unsigned int textlength, int TextEffect)
	{
		if (font == 0 || text == 0 || ((const char *)text)[0] == 0 || textlength == 0) return 0;
		FontFace *face = font->GetFace(fontsize);
		if (!face) return 0;

		float								W = 0;
		const FontGlyph						*glyph;
		unsigned int						i = 0, chr = 0, chrn = 0;

		if (TextEffect & TFX_UNICODE16) textlength *= 2;
		for (i = 0; i < textlength;)
		{
			chr = ((const char *)text)[i];
			if (TextEffect & TFX_UNICODE16) chr |= (((const char *)text)[i + 1]) << 8;
			if (chr == 0 || chr == 0x0A) break;

			if (TextEffect & TFX_UNICODE16)
			{
				chrn = ((const char *)text)[i + 2];
				chrn |= (((const char *)text)[i + 3]) << 8;
			}
			else {
				chrn = ((const char *)text)[i + 1];
			};

			glyph = face->GetGlyph(chr);
			if (glyph == 0) continue;

			W += glyph->advanceX_;
			W += face->GetKerning(chr, chrn);
			i += ((TextEffect & TFX_UNICODE16) ? 2 : 1);
		};
		if (TextEffect & TFX_HCENTER) return -W*0.5f;
		if (TextEffect & TFX_HRIGHT) return -W;
		return W;
	};

	bool SpriteBatch::DrawString(Font *font, int fontsize, const Vector2 &dest, const void *text, unsigned int textlength, const Color &color, int TextEffect)
	{
		if (color.a_ <= 0 || text == 0 || ((const char *)text)[0] == 0 || textlength == 0) return true;
		if (!font) return false;
		FontFace *face = font->GetFace(fontsize);
		if (!face) return false;

		float	ZH = (float)face->GetRowHeight();
		Vector2 CPos = dest;
		if (TextEffect & (TFX_VBOTTOM | TFX_VCENTER)) CPos.y_ -= GetHeightString(font, fontsize, text, textlength, TextEffect);
		if (TextEffect & (TFX_HRIGHT | TFX_HCENTER))  CPos.x_ += GetWidthString(font, fontsize, text, textlength, TextEffect);

		Vector2								Scr;
		Rect								TexRect;
		const FontGlyph						*glyph;
		unsigned int						i = 0, chr = 0, chrn = 0, Step = 1;
		const Vector<SharedPtr<Texture2D> >	&texs = face->GetTextures();

		if (TextEffect & TFX_UNICODE16) { textlength *= 2; Step = 2; };
		for (i = 0; i < textlength; i += Step)
		{
			chr = ((const char *)text)[i];
			if (TextEffect & TFX_UNICODE16) chr |= (((const char *)text)[i + 1]) << 8;
			if (chr == 0) break;

			if (TextEffect & TFX_UNICODE16)
			{
				chrn = ((const char *)text)[i + 2];
				chrn |= (((const char *)text)[i + 3]) << 8;
			}
			else {
				chrn = ((const char *)text)[i + 1];
			};

			if (chr == 0x0A)
			{
				CPos.x_ = dest.x_; CPos.y_ += ZH;
				if (TextEffect & (TFX_HRIGHT | TFX_HCENTER)) CPos.x_ += GetWidthString(font, fontsize, &((const char *)text)[i + Step], (textlength - (i + Step)) / Step, TextEffect);
				continue;
			};

			glyph = face->GetGlyph(chr);
			if (glyph == 0) continue;

			Scr = Vector2(glyph->offsetX_ + CPos.x_, glyph->offsetY_ + CPos.y_);
			TexRect = Rect((float)glyph->x_, (float)glyph->y_, (float)(glyph->x_ + glyph->width_), (float)(glyph->y_ + glyph->height_));
			CPos.x_ += glyph->advanceX_;
			CPos.x_ += face->GetKerning(chr, chrn);

			if (glyph->page_ < texs.Size()) Draw(texs[glyph->page_], Scr, TexRect, color);
		};
		return true;
	};

	bool SpriteBatch::DrawString(Font *font, int fontsize, const Vector2 &dest, const void *text, unsigned int textlength, const Color &color, float rotation, const Vector2 &origin, const Vector2 &scale, int TextEffect)
	{
		if (color.a_ <= 0) return true;
		bool bOk = true;
		PushModifier();
		bOk = DrawString(font, fontsize, -origin, text, textlength, color, TextEffect);
		ModifyPRS(dest, rotation, scale);
		PopModifier();
		return bOk;
	};

	void SpriteBatch::DrawFrame(Texture2D *texture, const Rect &dest, const Rect &src, const Rect &borders, const Color &color)
	{
		if (color.a_ <= 0) return;
		//LT
		Draw(texture, Rect(dest.min_.x_, dest.min_.y_, dest.min_.x_ + borders.min_.x_, dest.min_.y_ + borders.min_.y_), Rect(src.min_.x_, src.min_.y_, src.min_.x_ + borders.min_.x_, src.min_.y_ + borders.min_.y_), color);
		//LB
		Draw(texture, Rect(dest.min_.x_, dest.max_.y_ - borders.max_.y_, dest.min_.x_ + borders.min_.x_, dest.max_.y_), Rect(src.min_.x_, src.max_.y_ - borders.max_.y_, src.min_.x_ + borders.min_.x_, src.max_.y_), color);
		//RT
		Draw(texture, Rect(dest.max_.x_ - borders.max_.x_, dest.min_.y_, dest.max_.x_, dest.min_.y_ + borders.min_.y_), Rect(src.max_.x_ - borders.max_.x_, src.min_.y_, src.max_.x_, src.min_.y_ + borders.min_.y_), color);
		//RB
		Draw(texture, Rect(dest.max_.x_ - borders.max_.x_, dest.max_.y_ - borders.max_.y_, dest.max_.x_, dest.max_.y_), Rect(src.max_.x_ - borders.max_.x_, src.max_.y_ - borders.max_.y_, src.max_.x_, src.max_.y_), color);

		//TOP
		Draw(texture, Rect(dest.min_.x_ + borders.min_.x_, dest.min_.y_, dest.max_.x_ - borders.max_.x_, dest.min_.y_ + borders.min_.y_), Rect(src.min_.x_ + borders.min_.x_, src.min_.y_, src.max_.x_ - borders.max_.x_, src.min_.y_ + borders.min_.y_), color);
		//BOTTOM
		Draw(texture, Rect(dest.min_.x_ + borders.min_.x_, dest.max_.y_ - borders.max_.y_, dest.max_.x_ - borders.max_.x_, dest.max_.y_), Rect(src.min_.x_ + borders.min_.x_, src.max_.y_ - borders.max_.y_, src.max_.x_ - borders.max_.x_, src.max_.y_), color);
		//LEFT
		Draw(texture, Rect(dest.min_.x_, dest.min_.y_ + borders.min_.y_, dest.min_.x_ + borders.min_.x_, dest.max_.y_ - borders.max_.y_), Rect(src.min_.x_, src.min_.y_ + borders.min_.y_, src.min_.x_ + borders.min_.x_, src.max_.y_ - borders.max_.y_), color);
		//RIGHT
		Draw(texture, Rect(dest.max_.x_ - borders.max_.x_, dest.min_.y_ + borders.min_.y_, dest.max_.x_, dest.max_.y_ - borders.max_.y_), Rect(src.max_.x_ - borders.max_.x_, src.min_.y_ + borders.min_.y_, src.max_.x_, src.max_.y_ - borders.max_.y_), color);

		//CENTER
		Draw(texture, Rect(dest.min_.x_ + borders.min_.x_, dest.min_.y_ + borders.min_.y_, dest.max_.x_ - borders.max_.x_, dest.max_.y_ - borders.max_.y_), Rect(src.min_.x_ + borders.min_.x_, src.min_.y_ + borders.min_.y_, src.max_.x_ - borders.max_.x_, src.max_.y_ - borders.max_.y_), color);
	};

	void SpriteBatch::PushModifier()
	{
		modifiers_.push_back(icount_);
	};

	void					SpriteBatch::PopModifier()
	{
		if (modifiers_.size() > 0) modifiers_.pop_back();
	};

	bool					SpriteBatch::ModifyPRS(const Vector2 &pos, float rotation, const Vector2 &scale)
	{
		if (modifiers_.size() == 0 || vertex_ == 0) return false;

		Matrix4 m(Matrix4::IDENTITY);
		m.m00_ = cosf(rotation) * scale.x_;		m.m10_ = sinf(rotation) * scale.x_;
		m.m01_ = -sinf(rotation) * scale.y_;	m.m11_ = cosf(rotation) * scale.y_;
		m.m03_ = pos.x_;						m.m13_ = pos.y_;

		unsigned int bk_icount = modifiers_.back();
		for (unsigned int i = bk_icount; i < icount_; i++)	vertex_[i].pos = m * vertex_[i].pos;

		return true;
	};

	bool					SpriteBatch::ModifyTransform(const Matrix4 &matrix)
	{
		if (modifiers_.size() == 0 || vertex_ == 0) return false;
		unsigned int bk_icount = modifiers_.back();
		for (unsigned int i = bk_icount; i < icount_; i++)	vertex_[i].pos = matrix * vertex_[i].pos;
		return true;
	};

	bool					SpriteBatch::ModifyColor(const Color &color)
	{
		if (modifiers_.size() == 0 || vertex_ == 0) return false;

		unsigned int col_uint = color.ToUInt();

		unsigned int bk_icount = modifiers_.back();
		for (unsigned int i = bk_icount; i < icount_; i++)	vertex_[i].color = col_uint;

		return true;
	};

	bool					SpriteBatch::ModifyGradientH(const Color &color_up, const Color &color_down)
	{
		if (modifiers_.size() == 0 || vertex_ == 0) return false;

		unsigned int col_1 = color_up.ToUInt();
		unsigned int col_2 = color_down.ToUInt();

		unsigned int bk_icount = modifiers_.back();
		for (unsigned int i = bk_icount; i < icount_; i += 4)
		{
			vertex_[i + 0].color = vertex_[i + 1].color = col_1;
			vertex_[i + 2].color = vertex_[i + 3].color = col_2;
		};

		return true;
	};

	bool					SpriteBatch::ModifyGradientV(const Color &color_lf, const Color &color_rg)
	{
		if (modifiers_.size() == 0 || vertex_ == 0) return false;

		unsigned int col_1 = color_lf.ToUInt();
		unsigned int col_2 = color_rg.ToUInt();

		unsigned int bk_icount = modifiers_.back();
		for (unsigned int i = bk_icount; i < icount_; i += 4)
		{
			vertex_[i + 0].color = vertex_[i + 2].color = col_1;
			vertex_[i + 1].color = vertex_[i + 3].color = col_2;
		};

		return true;
	};

	bool					SpriteBatch::Initialize(unsigned int iBatchMax, unsigned int iQuadsMax)
	{
		graphics_ = GetSubsystem<Graphics>();

		if (iQuadsMax > 16300 || iQuadsMax == 0) iQuadsMax = 16300;
		if (iBatchMax == 0) iBatchMax = 512;

		vertex_ = 0;
		ibatch_ = icount_ = 0;
		maxbatch_ = iBatchMax;
		maxquads_ = iQuadsMax;
		if (batch_) delete[] batch_;
		batch_ = new BATCH[maxbatch_];

		vb_.Reset();
		vb_ = new VertexBuffer(context_);
		vb_->SetSize(iQuadsMax * 4, MASK_POSITION | MASK_COLOR | MASK_TEXCOORD1, true);

		//UnsubscribeFromEvent(graphics_, E_POSTRENDERUPDATE);
		//SubscribeToEvent(graphics_, E_POSTRENDERUPDATE, HANDLER(SpriteBatch, OnRender));
		return true;
	};

	void					SpriteBatch::SetScreenSize(float fWidth, float fHeight)
	{
		if (fWidth <= 0) fWidth = (float)graphics_->GetWidth();
		if (fHeight <= 0) fHeight = (float)graphics_->GetHeight();
		viewWidth_ = fWidth;
		viewHeight_ = fHeight;
	};

	void					SpriteBatch::OnRender(StringHash eventType, VariantMap& eventData)
	{
		if (!(graphics_ && graphics_->IsInitialized() && !graphics_->IsDeviceLost())) return;
		if (icount_ == 0 || ibatch_ == 0) return;

		//engine_->Exit();
		


		ShaderVariation* vs = graphics_->GetShader(VS, "Basic", "DIFFMAP VERTEXCOLOR");
		ShaderVariation* ps = graphics_->GetShader(PS, "Basic", "DIFFMAP VERTEXCOLOR");


		graphics_->SetBlendMode(BLEND_REPLACE);
		graphics_->SetColorWrite(true);
		graphics_->SetCullMode(CULL_NONE);  // ??? ??? ????? ????? ???????? ??????? ??????? ?????????, ????? ?? ???? ????? ??? ???? ??????? (??? ?????????)
		
		graphics_->SetDepthWrite(true);
		graphics_->SetScissorTest(false);
		graphics_->SetStencilTest(false);
		graphics_->SetShaders(vs, ps);
		graphics_->SetShaderParameter(VSP_MODEL, Matrix3x4::IDENTITY);
		graphics_->SetShaderParameter(VSP_VIEWPROJ, camera_->GetProjection() * camera_->GetView());
		graphics_->SetShaderParameter(PSP_MATDIFFCOLOR, Color(1.0f, 1.0f, 1.0f, 1.0f));
		graphics_->SetVertexBuffer(vb_);
		graphics_->SetIndexBuffer(g_pIB);
		graphics_->SetDepthTest(CMP_LESSEQUAL);
		
		for (unsigned int i = 1; i < ibatch_ + 1; i++)
		{
			BATCH *b = &batch_[i];
			graphics_->SetBlendMode((BlendMode)b->iBlendMode);
			graphics_->SetTexture(0, b->pTexture);
			graphics_->Draw(TRIANGLE_LIST, (b->iStart / 4) * 6, (b->iCount / 4) * 6, 0, b->iCount);
		};
	};

	void SpriteBatch::SetView(Camera* camera, Engine* engine)
	{
		camera_ = camera;
		engine_ = engine;
	}



};
[/code]

stdafx.h
[code]#pragma once

#include <Urho3D/Urho3D.h>

#include <Urho3D/Revision.h>
#include <Urho3D/Audio/Audio.h>
#include <Urho3D/Audio/AudioDefs.h>
#include <Urho3D/Audio/BufferedSoundStream.h>
#include <Urho3D/Audio/OggVorbisSoundStream.h>
#include <Urho3D/Audio/Sound.h>
#include <Urho3D/Audio/SoundListener.h>
#include <Urho3D/Audio/SoundSource.h>
#include <Urho3D/Audio/SoundSource3D.h>
#include <Urho3D/Audio/SoundStream.h>
#include <Urho3D/Container/Allocator.h>
#include <Urho3D/Container/ArrayPtr.h>
#include <Urho3D/Container/ForEach.h>
#include <Urho3D/Container/Hash.h>
#include <Urho3D/Container/HashBase.h>
#include <Urho3D/Container/HashMap.h>
#include <Urho3D/Container/HashSet.h>
#include <Urho3D/Container/LinkedList.h>
#include <Urho3D/Container/List.h>
#include <Urho3D/Container/ListBase.h>
#include <Urho3D/Container/Pair.h>
#include <Urho3D/Container/Ptr.h>
#include <Urho3D/Container/RefCounted.h>
#include <Urho3D/Container/Sort.h>
#include <Urho3D/Container/Str.h>
#include <Urho3D/Container/Swap.h>
#include <Urho3D/Container/Vector.h>
#include <Urho3D/Container/VectorBase.h>
#include <Urho3D/Core/Attribute.h>
#include <Urho3D/Core/Condition.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Core/Main.h>
#include <Urho3D/Core/MiniDump.h>
#include <Urho3D/Core/Mutex.h>
#include <Urho3D/Core/Object.h>
#include <Urho3D/Core/ProcessUtils.h>
#include <Urho3D/Core/Profiler.h>
#include <Urho3D/Core/Spline.h>
#include <Urho3D/Core/StringUtils.h>
#include <Urho3D/Core/Thread.h>
#include <Urho3D/Core/Timer.h>
#include <Urho3D/Core/Variant.h>
#include <Urho3D/Core/WorkQueue.h>
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Console.h>
#include <Urho3D/Engine/DebugHud.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Engine/EngineEvents.h>
#include <Urho3D/Graphics/AnimatedModel.h>
#include <Urho3D/Graphics/Animation.h>
#include <Urho3D/Graphics/AnimationController.h>
#include <Urho3D/Graphics/AnimationState.h>
#include <Urho3D/Graphics/Batch.h>
#include <Urho3D/Graphics/BillboardSet.h>
#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/ConstantBuffer.h>
#include <Urho3D/Graphics/CustomGeometry.h>
#include <Urho3D/Graphics/DebugRenderer.h>
#include <Urho3D/Graphics/DecalSet.h>
#include <Urho3D/Graphics/Drawable.h>
#include <Urho3D/Graphics/DrawableEvents.h>
#include <Urho3D/Graphics/Geometry.h>
#include <Urho3D/Graphics/GPUObject.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/GraphicsDefs.h>
#include <Urho3D/Graphics/GraphicsEvents.h>
#include <Urho3D/Graphics/GraphicsImpl.h>
#include <Urho3D/Graphics/IndexBuffer.h>
#include <Urho3D/Graphics/Light.h>
#include <Urho3D/Graphics/Material.h>
#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Graphics/OcclusionBuffer.h>
#include <Urho3D/Graphics/Octree.h>
#include <Urho3D/Graphics/OctreeQuery.h>
#include <Urho3D/Graphics/ParticleEffect.h>
#include <Urho3D/Graphics/ParticleEmitter.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Graphics/RenderPath.h>
#include <Urho3D/Graphics/RenderSurface.h>
#include <Urho3D/Graphics/Shader.h>
#include <Urho3D/Graphics/ShaderPrecache.h>
#include <Urho3D/Graphics/ShaderProgram.h>
#include <Urho3D/Graphics/ShaderVariation.h>
#include <Urho3D/Graphics/Skeleton.h>
#include <Urho3D/Graphics/Skybox.h>
#include <Urho3D/Graphics/StaticModel.h>
#include <Urho3D/Graphics/StaticModelGroup.h>
#include <Urho3D/Graphics/Tangent.h>
#include <Urho3D/Graphics/Technique.h>
#include <Urho3D/Graphics/Terrain.h>
#include <Urho3D/Graphics/TerrainPatch.h>
#include <Urho3D/Graphics/Texture.h>
#include <Urho3D/Graphics/Texture2D.h>
#include <Urho3D/Graphics/Texture3D.h>
#include <Urho3D/Graphics/TextureCube.h>
#include <Urho3D/Graphics/VertexBuffer.h>
#include <Urho3D/Graphics/VertexDeclaration.h>
#include <Urho3D/Graphics/View.h>
#include <Urho3D/Graphics/Viewport.h>
#include <Urho3D/Graphics/Zone.h>
#include <Urho3D/Input/Controls.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/IO/Compression.h>
#include <Urho3D/IO/Deserializer.h>
#include <Urho3D/IO/File.h>
#include <Urho3D/IO/FileSystem.h>
#include <Urho3D/IO/FileWatcher.h>
#include <Urho3D/IO/IOEvents.h>
#include <Urho3D/IO/Log.h>
#include <Urho3D/IO/MacFileWatcher.h>
#include <Urho3D/IO/MemoryBuffer.h>
#include <Urho3D/IO/PackageFile.h>
#include <Urho3D/IO/RWOpsWrapper.h>
#include <Urho3D/IO/Serializer.h>
#include <Urho3D/IO/VectorBuffer.h>
#include <Urho3D/Math/AreaAllocator.h>
#include <Urho3D/Math/BoundingBox.h>
#include <Urho3D/Math/Color.h>
#include <Urho3D/Math/Frustum.h>
#include <Urho3D/Math/MathDefs.h>
#include <Urho3D/Math/Matrix3.h>
#include <Urho3D/Math/Matrix3x4.h>
#include <Urho3D/Math/Matrix4.h>
#include <Urho3D/Math/Plane.h>
#include <Urho3D/Math/Polyhedron.h>
#include <Urho3D/Math/Quaternion.h>
#include <Urho3D/Math/Random.h>
#include <Urho3D/Math/Ray.h>
#include <Urho3D/Math/Rect.h>
#include <Urho3D/Math/Sphere.h>
#include <Urho3D/Math/StringHash.h>
#include <Urho3D/Math/Vector2.h>
#include <Urho3D/Math/Vector3.h>
#include <Urho3D/Math/Vector4.h>
#include <Urho3D/Navigation/Navigable.h>
#include <Urho3D/Navigation/NavigationMesh.h>
#include <Urho3D/Navigation/OffMeshConnection.h>
#include <Urho3D/Network/Connection.h>
#include <Urho3D/Network/HttpRequest.h>
#include <Urho3D/Network/Network.h>
#include <Urho3D/Network/NetworkEvents.h>
#include <Urho3D/Network/NetworkPriority.h>
#include <Urho3D/Network/Protocol.h>
#include <Urho3D/Physics/CollisionShape.h>
#include <Urho3D/Physics/Constraint.h>
#include <Urho3D/Physics/PhysicsEvents.h>
#include <Urho3D/Physics/PhysicsUtils.h>
#include <Urho3D/Physics/PhysicsWorld.h>
#include <Urho3D/Physics/RigidBody.h>
#include <Urho3D/Resource/BackgroundLoader.h>
#include <Urho3D/Resource/Decompress.h>
#include <Urho3D/Resource/Image.h>
#include <Urho3D/Resource/JSONFile.h>
#include <Urho3D/Resource/JSONValue.h>
#include <Urho3D/Resource/PListFile.h>
#include <Urho3D/Resource/Resource.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Resource/ResourceEvents.h>
#include <Urho3D/Resource/XMLElement.h>
#include <Urho3D/Resource/XMLFile.h>
#include <Urho3D/Scene/Animatable.h>
#include <Urho3D/Scene/AnimationDefs.h>
#include <Urho3D/Scene/Component.h>
#include <Urho3D/Scene/LogicComponent.h>
#include <Urho3D/Scene/Node.h>
#include <Urho3D/Scene/ObjectAnimation.h>
#include <Urho3D/Scene/ReplicationState.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Scene/SceneEvents.h>
#include <Urho3D/Scene/SceneResolver.h>
#include <Urho3D/Scene/Serializable.h>
#include <Urho3D/Scene/SmoothedTransform.h>
#include <Urho3D/Scene/SplinePath.h>
#include <Urho3D/Scene/UnknownComponent.h>
#include <Urho3D/Scene/ValueAnimation.h>
#include <Urho3D/Scene/ValueAnimationInfo.h>
#include <Urho3D/Script/Addons.h>
#include <Urho3D/Script/APITemplates.h>
#include <Urho3D/Script/Script.h>
#include <Urho3D/Script/ScriptAPI.h>
#include <Urho3D/Script/ScriptEventListener.h>
#include <Urho3D/Script/ScriptFile.h>
#include <Urho3D/Script/ScriptInstance.h>
#include <Urho3D/UI/BorderImage.h>
#include <Urho3D/UI/Button.h>
#include <Urho3D/UI/CheckBox.h>
#include <Urho3D/UI/Cursor.h>
#include <Urho3D/UI/DropDownList.h>
#include <Urho3D/UI/FileSelector.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/UI/FontFace.h>
#include <Urho3D/UI/FontFaceBitmap.h>
#include <Urho3D/UI/FontFaceFreeType.h>
#include <Urho3D/UI/LineEdit.h>
#include <Urho3D/UI/ListView.h>
#include <Urho3D/UI/Menu.h>
#include <Urho3D/UI/MessageBox.h>
#include <Urho3D/UI/ScrollBar.h>
#include <Urho3D/UI/ScrollView.h>
#include <Urho3D/UI/Slider.h>
#include <Urho3D/UI/Sprite.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/Text3D.h>
#include <Urho3D/UI/ToolTip.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/UI/UIBatch.h>
#include <Urho3D/UI/UIElement.h>
#include <Urho3D/UI/UIEvents.h>
#include <Urho3D/UI/View3D.h>
#include <Urho3D/UI/Window.h>
#include <Urho3D/Urho2D/AnimatedSprite2D.h>
#include <Urho3D/Urho2D/Animation2D.h>
#include <Urho3D/Urho2D/AnimationSet2D.h>
#include <Urho3D/Urho2D/CollisionBox2D.h>
#include <Urho3D/Urho2D/CollisionChain2D.h>
#include <Urho3D/Urho2D/CollisionCircle2D.h>
#include <Urho3D/Urho2D/CollisionEdge2D.h>
#include <Urho3D/Urho2D/CollisionPolygon2D.h>
#include <Urho3D/Urho2D/CollisionShape2D.h>
#include <Urho3D/Urho2D/Constraint2D.h>
#include <Urho3D/Urho2D/ConstraintDistance2D.h>
#include <Urho3D/Urho2D/ConstraintFriction2D.h>
#include <Urho3D/Urho2D/ConstraintGear2D.h>
#include <Urho3D/Urho2D/ConstraintMotor2D.h>
#include <Urho3D/Urho2D/ConstraintMouse2D.h>
#include <Urho3D/Urho2D/ConstraintPrismatic2D.h>
#include <Urho3D/Urho2D/ConstraintPulley2D.h>
#include <Urho3D/Urho2D/ConstraintRevolute2D.h>
#include <Urho3D/Urho2D/ConstraintRope2D.h>
#include <Urho3D/Urho2D/ConstraintWeld2D.h>
#include <Urho3D/Urho2D/ConstraintWheel2D.h>
#include <Urho3D/Urho2D/Drawable2D.h>
#include <Urho3D/Urho2D/ParticleEffect2D.h>
#include <Urho3D/Urho2D/ParticleEmitter2D.h>
#include <Urho3D/Urho2D/PhysicsEvents2D.h>
#include <Urho3D/Urho2D/PhysicsUtils2D.h>
#include <Urho3D/Urho2D/PhysicsWorld2D.h>
#include <Urho3D/Urho2D/Renderer2D.h>
#include <Urho3D/Urho2D/RigidBody2D.h>
#include <Urho3D/Urho2D/Sprite2D.h>
#include <Urho3D/Urho2D/SpriteSheet2D.h>
#include <Urho3D/Urho2D/StaticSprite2D.h>
#include <Urho3D/Urho2D/TileMap2D.h>
#include <Urho3D/Urho2D/TileMapDefs2D.h>
#include <Urho3D/Urho2D/TileMapLayer2D.h>
#include <Urho3D/Urho2D/TmxFile2D.h>
#include <Urho3D/Urho2D/Urho2D.h>

#include <Urho3D/DebugNew.h>

using namespace Urho3D;
[/code]

Game.cpp
[code]#include "stdafx.h"
#include "Game.h"


DEFINE_APPLICATION_MAIN(Game)


Game::Game(Context* context) :
    Application(context),
    yaw_(0.0f),
    pitch_(0.0f)
{
}


void Game::Setup()
{
	engineParameters_["WindowTitle"] = GetTypeName();
	engineParameters_["LogName"] = GetSubsystem<FileSystem>()->GetAppPreferencesDir("urho3d", "logs") + GetTypeName() + ".log";
	engineParameters_["FullScreen"] = false;
	engineParameters_["Headless"] = false;
	engineParameters_["WindowWidth"] = 800;
	engineParameters_["WindowHeight"] = 600;
//	engineParameters_["ResourcePaths"] = "Data;CoreData;MyData";
}


void Game::Start()
{
	CreateScene();
	SetupViewport();
	SubscribeToEvents();
	spriteBatch_ = new SpriteBatch(context_);
	spriteBatch_->Initialize();
	spriteBatch_->SetView(cameraNode_->GetComponent<Camera>(), engine_);
	ResourceCache* cache = GetSubsystem<ResourceCache>();
	XMLFile* xmlFile = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
	DebugHud* debugHud = engine_->CreateDebugHud();
	debugHud->SetDefaultStyle(xmlFile);
	CreateText();
}


void Game::SetupViewport()
{
	Renderer* renderer = GetSubsystem<Renderer>();
	SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
	renderer->SetViewport(0, viewport);
}


void Game::CreateScene()
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();

	scene_ = new Scene(context_);
	scene_->CreateComponent<Octree>();
	scene_->CreateComponent<DebugRenderer>();

	Node* planeNode = scene_->CreateChild("Plane");
	planeNode->SetScale(Vector3(100.0f, 1.0f, 100.0f));
	StaticModel* planeObject = planeNode->CreateComponent<StaticModel>();
	planeObject->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));
	planeObject->SetMaterial(cache->GetResource<Material>("Materials/StoneTiled.xml"));

	Node* lightNode = scene_->CreateChild("DirectionalLight");
	lightNode->SetDirection(Vector3(0.6f, -1.0f, 0.8f));
	Light* light = lightNode->CreateComponent<Light>();
	light->SetColor(Color(0.6f, 0.5f, 0.2f));
	light->SetLightType(LIGHT_DIRECTIONAL);
	light->SetCastShadows(true);
	light->SetShadowBias(BiasParameters(0.00025f, 0.5f));
	light->SetShadowCascade(CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f));
	//light->SetShadowIntensity(0.5f);

	Node* zoneNode = scene_->CreateChild("Zone");
	Zone* zone = zoneNode->CreateComponent<Zone>();
	zone->SetBoundingBox(BoundingBox(-1000.0f, 1000.0f));
	zone->SetAmbientColor(Color(0.4f, 0.5f, 0.8f));
	zone->SetFogColor(Color(0.4f, 0.5f, 0.8f));
	zone->SetFogStart(100.0f);
	zone->SetFogEnd(300.0f);

	const unsigned NUM_OBJECTS = 0;
	for (unsigned i = 0; i < NUM_OBJECTS; ++i)
	{
		Node* mushroomNode = scene_->CreateChild("Mushroom");
		mushroomNode->SetPosition(Vector3(Random(90.0f) - 45.0f, 0.0f, Random(90.0f) - 45.0f));
		mushroomNode->SetRotation(Quaternion(0.0f, Random(360.0f), 0.0f));
		mushroomNode->SetScale(0.1f + Random(.2f));
		StaticModel* mushroomObject = mushroomNode->CreateComponent<StaticModel>();
		mushroomObject->SetModel(cache->GetResource<Model>("Models/Mushroom.mdl"));
		mushroomObject->SetMaterial(cache->GetResource<Material>("Materials/Mushroom.xml"));
		mushroomObject->SetCastShadows(true);
	}

	Node* mushroomNode = scene_->CreateChild("Mushroom");
	mushroomNode->SetPosition(Vector3(0, 0.0f, 0));
	StaticModel* mushroomObject = mushroomNode->CreateComponent<StaticModel>();
	mushroomObject->SetModel(cache->GetResource<Model>("Models/Mushroom.mdl"));
	mushroomObject->SetMaterial(cache->GetResource<Material>("Materials/Mushroom.xml"));


	cameraNode_ = scene_->CreateChild("Camera");
	Camera* camera = cameraNode_->CreateComponent<Camera>();
	cameraNode_->SetPosition(Vector3(0.0f, 0.5f, -10.0f));
	cameraNode_->LookAt(Vector3(0.0f, 0.5f, 0.0f));
	camera->SetOrthographic(true);
	Graphics* graphics = GetSubsystem<Graphics>();
	camera->SetOrthoSize((float)graphics->GetHeight() * PIXEL_SIZE);
}


void Game::MoveCamera(float timeStep)
{
	Input* input = GetSubsystem<Input>();

	const float MOVE_SPEED = 20.0f;
	const float MOUSE_SENSITIVITY = 0.1f;

	IntVector2 mouseMove = input->GetMouseMove();
	yaw_ += MOUSE_SENSITIVITY * mouseMove.x_;
	pitch_ += MOUSE_SENSITIVITY * mouseMove.y_;
	pitch_ = Clamp(pitch_, -90.0f, 90.0f);

	cameraNode_->SetRotation(Quaternion(pitch_, yaw_, 0.0f));

	if (input->GetKeyDown('Q'))
		cameraNode_->Translate(Vector3::UP * MOVE_SPEED * timeStep);
	if (input->GetKeyDown('E'))
		cameraNode_->Translate(Vector3::DOWN * MOVE_SPEED * timeStep);
	if (input->GetKeyDown('W'))
		cameraNode_->Translate(Vector3::FORWARD * MOVE_SPEED * timeStep);
	if (input->GetKeyDown('S'))
		cameraNode_->Translate(Vector3::BACK * MOVE_SPEED * timeStep);
	if (input->GetKeyDown('A'))
		cameraNode_->Translate(Vector3::LEFT * MOVE_SPEED * timeStep);
	if (input->GetKeyDown('D'))
		cameraNode_->Translate(Vector3::RIGHT * MOVE_SPEED * timeStep);

	if (input->GetKeyPress(KEY_F2))
		GetSubsystem<DebugHud>()->ToggleAll();
}


void Game::SubscribeToEvents()
{
	SubscribeToEvent(E_UPDATE, HANDLER(Game, HandleUpdate));
	SubscribeToEvent(E_SCENEUPDATE, HANDLER(Game, HandleSceneUpdate));
	SubscribeToEvent(E_POSTRENDERUPDATE, HANDLER(Game, HandlePostRenderUpdate));
	SubscribeToEvent(E_ENDRENDERING, HANDLER(Game, HandleEndRendering));
}


void Game::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
	using namespace Update;

	float timeStep = eventData[P_TIMESTEP].GetFloat();

	MoveCamera(timeStep);
}


void Game::HandleSceneUpdate(StringHash eventType, VariantMap& eventData)
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();
	spriteBatch_->Begin();
	spriteBatch_->SetBlendMode(BLEND_ALPHA);
	Texture2D* text1 = cache->GetResource<Texture2D>("Textures/Flare.dds"); // ????? ??? ?? ????? ? ??????? ????????? ? 50 ???
	Texture2D* tex2 = cache->GetResource<Texture2D>("Urho2D/Ball.png"); // ?????????? ??????? ???????
	
	spriteBatch_->Draw(tex2, Rect(0, 0, 1, 1), Color::WHITE);
	
	for (int i = 0; i < 200; i++)
	{
		//		spriteBatch_->Draw(text1, Rect(0, 0, 1, 1), Rect(0, 0, 256, 256), Color::WHITE);
	}
	for (int i = 0; i < 200; i++)
	{
		//		spriteBatch_->Draw(tex2, Rect(1, 0, 2, 1), Rect(0, 0, 256, 256), Color::WHITE);
		//spriteBatch_->Draw(text1, Rect(1, 0, 2, 1), Rect(0, 0, 256, 256), Color::WHITE);
		//spriteBatch_->Draw(tex2, Rect(1, 0.5f, 2, 1.5f), Color::WHITE);
	}
	for (int i = 0; i < 200; i++)
		//		spriteBatch_->Draw(tex2, Rect(1, 0, 2, 1), Rect(0, 0, 256, 256), Color::WHITE);
	spriteBatch_->End();
}



void Game::HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
	//GetSubsystem<Renderer>()->DrawDebugGeometry(true);

	spriteBatch_->OnRender(eventType, eventData);

}



void Game::HandleEndRendering(StringHash eventType, VariantMap& eventData)
{
	//spriteBatch_->OnRender(eventType, eventData); // ??? ????????, ?? ??????????? UI, ?????? ???? ? HandlePostRenderUpdate
}



void Game::CreateText()
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();

	// Construct new Text object
	SharedPtr<Text> helloText(new Text(context_));

	// Set String to display
	helloText->SetText("========================");

	// Set font and text color
	helloText->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 30);
	helloText->SetColor(Color(0.0f, 1.0f, 0.0f));

	// Align Text center-screen
	helloText->SetHorizontalAlignment(HA_CENTER);
	helloText->SetVerticalAlignment(VA_CENTER);

	// Add Text instance to the UI root element
	GetSubsystem<UI>()->GetRoot()->AddChild(helloText);
} [/code]

Game.h
[code]#pragma once


#include "SpriteBatch.h"


class Game : public Application
{
    OBJECT(Game);

public:
    Game(Context* context);

    virtual void Setup();
    virtual void Start();

	void CreateText();

protected:
    void SetLogoVisible(bool enable);
    SharedPtr<Scene> scene_;
    SharedPtr<Node> cameraNode_;
    float yaw_;
    float pitch_;

private:
	SpriteBatch* spriteBatch_;
	void CreateScene();
	void SetupViewport();
	void MoveCamera(float timeStep);
	void SubscribeToEvents();
	void HandleUpdate(StringHash eventType, VariantMap& eventData);
	void HandleSceneUpdate(StringHash eventType, VariantMap& eventData);
	void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData);
	void HandleEndRendering(StringHash eventType, VariantMap& eventData);
}; [/code]

But I have problem.

When I call drawing SpriteBatch in HandleEndRendering it works, but SpriteBatch overlaps UI.

[code]void Game::HandleEndRendering(StringHash eventType, VariantMap& eventData)
{
	spriteBatch_->OnRender(eventType, eventData);
}[/code]

[spoiler][img]http://s020.radikal.ru/i700/1506/20/66a9d271926e.jpg[/img][/spoiler]

When I call drawing SpriteBatch in HandlePostRenderUpdate (like DrawDebugGeometry) it does not work.

[code]void Game::HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
	//GetSubsystem<Renderer>()->DrawDebugGeometry(true);
	spriteBatch_->OnRender(eventType, eventData);
}[/code]

[spoiler][img]http://s018.radikal.ru/i527/1506/c2/802267fcd892.jpg[/img][/spoiler]

Pls help me :slight_smile:

-------------------------

v0van1981 | 2017-01-02 01:05:40 UTC | #5

I found the solution. If call rendering from E_ENDVIEWRENDER all works nice.

-------------------------

1vanK | 2017-01-02 01:12:40 UTC | #6

This is a very useful thing, but public under unknown license. So, I decided to write my own implementation (and also for self-education).
[github.com/1vanK/Urho3DSpriteBatch](https://github.com/1vanK/Urho3DSpriteBatch)
I wrote the code for personal use, so there are a lot of comments in Russian, sorry. But still decided to publish his, perhaps it would be useful for someone.
Main differences:
1) public domain license
2) infinite count of sprites
3) correct rendering ttf fonts (but still need to do some things)
4) possible to render canvas with sprites in 3d space
This is early version. And I do not know exactly when it will be finished. I will add functionality when I will to need anything.

-------------------------

Victor | 2017-01-02 01:12:40 UTC | #7

This looks interesting! I'm not familiar with XNA or D3DXSprite implementations. It sounds like this could this be used to render fonts in world space? I've had this issue for a while where I couldn't place text correctly onto terrain with a curve (and stroke effect), and so I've abandoned the idea temporarily, however if SpriteBatch renders text in world space coords perhaps that would solve my issue. Thanks man!

Reference post to the issue I'm having: [topic2130.html#p12857](http://discourse.urho3d.io/t/curved-text/2034/9)

-------------------------

1vanK | 2017-01-02 01:12:40 UTC | #8

It will not help you, it draw all spites in one plane

-------------------------

Victor | 2017-01-02 01:12:40 UTC | #9

[quote="1vanK"]It will not help you, it draw all spites in one plane[/quote]

Ah I see. Maybe I could modify it a bit to fit my needs. Either way, thanks for this man! I'm sure it can be helpful in other ways. :slight_smile:

-------------------------

1vanK | 2017-01-02 01:12:40 UTC | #10

[quote="Victor"][quote="1vanK"]It will not help you, it draw all spites in one plane[/quote]

Ah I see. Maybe I could modify it a bit to fit my needs. Either way, thanks for this man! I'm sure it can be helpful in other ways. :)[/quote]

It is unlikely that all this will be somehow useful to you. The purpose of it - rendering of previously unknown number of sprites, that change every frame without overhead from nodes. Examle of using this: [topic1765.html](http://discourse.urho3d.io/t/terraria-like-game-in-urho3d/1698/1)

-------------------------

1vanK | 2017-01-02 01:15:18 UTC | #11

About [github.com/1vanK/Urho3DSpriteBatch](https://github.com/1vanK/Urho3DSpriteBatch)

Edit: in my tests with 20000 sprites on screen
MonoGame (Directx 11) - 64 fps
XNA (DirectX 9) - 46 fps
Urho3D OpenGL - 56 fps
Urho3D DrectX - 47 fps
Urho3D DrectX11 - 62 fps

-------------------------

1vanK | 2017-01-02 01:15:33 UTC | #12

SpriteBatch [github.com/1vanK/Urho3DSpriteBatch](https://github.com/1vanK/Urho3DSpriteBatch) generally completed
The main purpose: tile-based 2D games

-------------------------

1vanK | 2017-01-06 18:17:54 UTC | #13

Currently I works on Sprite Font Generator for Sprite Batch with different special effects (for example blurred shadows):
https://github.com/1vanK/Urho3DBitmapFontGenerator
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/35d0f728ed515346ea23044bc7328c152c868f8f.png" width="690" height="468">

-------------------------

