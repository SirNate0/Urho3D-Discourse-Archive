thebluefish | 2017-01-02 01:07:13 UTC | #1

I've had this for over a month now, and progress has been slow. I don't foresee any modifications that I need to do to the port itself, so I feel confident enough in releasing this. However this implementation makes several assumptions that will not be true for everyone, so some modification may be required to fit your specific needs.

This is primarily based off the existing Urho3D UI implementation, so there will be a lot of similarities.

It still uses Urho3D resources to load files, so turbobadger file paths are the same as loading any files through Urho3D. I did hard-code the skin and override skin paths in TBUI.cpp, so you may need to change these if you use different paths.

[url=http://i.imgur.com/H7kQDU8.png][img]http://i.imgur.com/H7kQDU8m.png[/img][/url]
[size=85]Turbo Badger running in Urho3D in a wxWidgets window.[/size]


TBUI.h:
[code]
>>Removed<<
[/code]

TBUI.cpp:
[code]
>>Removed<<
[/code]

To setup the subsystem:
[code]
// Setup Turbo Badger UI
UI::TBUI::RegisterSystem(_context);
_context->RegisterSubsystem(new UI::TBUI(_context));
_context->GetSubsystem<UI::TBUI>()->Init();
[/code]

Adding an editor control that expands the entire window is easy:
[code]
_editorUI = ui->LoadWidget<tb::TBWidget>("UI/ui_resources/editor_tab_content.tb.txt");
ui->SetRoot(_editorUI);
[/code]

-------------------------

rasteron | 2017-01-02 01:07:14 UTC | #2

Great share! :slight_smile:

-------------------------

jmiller | 2017-01-02 01:07:17 UTC | #3

Excellent, thanks blue :sunglasses:

diff from tb_config.h
[code]
35c35
< #define TB_FONT_RENDERER_TBBF
---
> //#define TB_FONT_RENDERER_TBBF
38c38
< //#define TB_FONT_RENDERER_FREETYPE
---
> #define TB_FONT_RENDERER_FREETYPE
102c102
< #define TB_FILE_POSIX
---
> //#define TB_FILE_POSIX
107c107
< #define TB_FILE_POSIX
---
> //#define TB_FILE_POSIX
112c112
< #define TB_FILE_POSIX
---
> //#define TB_FILE_POSIX
[/code]

Initialize subsystem (assuming similar namespace setup):
[code]
  // Setup Turbo Badger UI
  context_->RegisterSubsystem(new App::UI::TBUI(context_));
  context_->GetSubsystem<App::UI::TBUI>()->Init();
[/code]

-------------------------

thebluefish | 2017-01-02 01:07:18 UTC | #4

A little example to working with events, including input.

Working with Carnalis' example, your class needs to inherit from TBWidgetListener and set itself as a global event handler. This example is for clicking a button called "fileMenu", and showing a popup window with the File menu options:

[code]
bool Editor::OnWidgetInvokeEvent(tb::TBWidget *widget, const tb::TBWidgetEvent &ev)
{
	if (ev.target->GetID() == tb::TBID("fileMenu"))
	{
		if (ev.type == tb::EVENT_TYPE_CLICK)
		{
			static tb::TBGenericStringItemSource source;
			if (!source.GetNumItems())
			{
				source.AddItem(new tb::TBGenericStringItem("New", tb::TBID("default font")));
				source.AddItem(new tb::TBGenericStringItem("Open File", tb::TBID("large font")));
				source.AddItem(new tb::TBGenericStringItem("-"));
				source.AddItem(new tb::TBGenericStringItem("Save", tb::TBID("large font")));
				source.AddItem(new tb::TBGenericStringItem("Save All", tb::TBID("large font")));
				source.AddItem(new tb::TBGenericStringItem("-"));
				source.AddItem(new tb::TBGenericStringItem("Exit", tb::TBID("align left")));
			}

			if (tb::TBMenuWindow *menu = new tb::TBMenuWindow(widget, tb::TBID("popup_menu")))
			{
				menu->Show(&source, tb::TBPopupAlignment());
			}
		}
	}
}
[/code]

-------------------------

jmiller | 2017-01-02 01:07:26 UTC | #5

[github.com/fruxo/turbobadger](https://github.com/fruxo/turbobadger)
Very slick UI :smiley: 
Candidate for Urho3D? I really like the way TurboBadger does things, it seems rather complete, internationalized..

-------------------------

jmiller | 2019-04-20 15:19:48 UTC | #6

A TurboBadger Console (Urho3D::Object, TBWidget) inspired by Urho3D::Console.

[url=http://imgur.com/SBDcK9n][img]http://i.imgur.com/SBDcK9nl.png[/img][/url]

Still a couple rough edges..
Being a TBWidget, it's easily styled and modified. I did not implement SetNumLines() (calc the line height) but it shouldn't be hard.

Besides Urho3D's Console, the TurboBadger Demo application was helpful in developing this, and can offer a lot of insight.

After instantiating TBUI and creating a root widget..
[code]
Console* console(new ::Console(context_, tbRoot));
console->LoadResourceFile("UI/resources/console.txt"); // required widgets
console->Initialize();
// Change custom styles for LOG_* constants (output widget in console.txt has 'styling 1')..
console->styleMap_[LOG_ERROR] = Pair<String, String>("<color #ff0000>", "</color>");
console->Toggle(); // It's invisible by default

console->SetID(TBIDC("console"));
// Can be later retrieved by ID:
// Console* console(static_cast<Console*>(tbRoot->GetWidgetByID(TBIDC("console"))));
[/code]

Console.h
[gist.github.com/jforjustin/2761431647bda9c90b4d](https://gist.github.com/jforjustin/2761431647bda9c90b4d)

Console.cc
[gist.github.com/jforjustin/6fbc1202729f21f6c153](https://gist.github.com/jforjustin/6fbc1202729f21f6c153)

console.txt
TurboBadger widget definition file; leading tabs are significant.[gist.github.com/jforjustin/baa26a0943c684c4b8a9](https://gist.github.com/jforjustin/baa26a0943c684c4b8a9)

-------------------------

Lumak | 2017-01-02 01:07:53 UTC | #7

I'm looking at your code and Atomic's code for the first time, and it looks like you copied and pasted Atomics code. From rendering process to key inputs, they're identical.

Well, I guess it's ok if you gave him credit for his work.

Wow, I'm surprize to see Atomic's UIInput.cpp file is almost as long as my entire integration.

-------------------------

thebluefish | 2017-01-02 01:07:54 UTC | #8

[quote="Lumak"]I'm looking at your code and Atomic's code for the first time, and it looks like you copied and pasted Atomics code. From rendering process to key inputs, they're identical.

Well, I guess it's ok if you gave him credit for his work.

Wow, I'm surprize to see Atomic's UIInput.cpp file is almost as long as my entire integration.[/quote]

Input stuff I got from Atomic. Rendering stuff was based on Urho3D's existing UI class. The reason our code base looks similar is because we both used UI as our base. However Atomic uses a functionally different batching process which I skipped altogether. I actually finished the rendering part before I took a look at Atomic, but I got stuck on "proper" input support and filesystem stuff.

-------------------------

Lumak | 2017-01-02 01:07:56 UTC | #9

I see. It would've been nice to see a reference.

-------------------------

jenge | 2017-01-02 01:07:56 UTC | #10

I am glad that some of the Atomic code was useful.

I don't really mind for snippets, though when sharing in the "Code Exchange" section for others to use, probably a good idea to leave copyright and license notifications in place  :wink:

-------------------------

thebluefish | 2017-01-02 01:07:56 UTC | #11

[quote="jenge"]probably a good idea to leave copyright and license notifications in place  :wink:[/quote]

Granted, it's less "leaving them in place" and more "adding them to the post". The Atomic MIT license is in the correct place for the next release, whenever that will be.

-------------------------

jenge | 2017-01-02 01:07:56 UTC | #12

There's no need from here to remove code from posts, I was just mentioning that when sharing code for others to use, good to cite sources and licenses of where pulling code from... even with the permissive MIT, in any event cheers :slight_smile:

-------------------------

jmiller | 2018-02-23 20:05:29 UTC | #13

I think the implementation that was posted still exists and I'll look to posting that when it's available.

Here is my own working edition of the implementation.  Changes include a license header (let me know if it needs further changes), some private to protected members, various updates for Urho3D, formatting. no real API changes that I recall...

tb_Urho3D.h
[code]
/**
  @license MIT License
  @copyright
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.

  Portions Copyright (c) 2008-2016 the Urho3D project.
  Portions Copyright (c) Thebluefish
  Portions Copyright (c) 2014-2015 THUNDERBEAST GAMES
*/

#pragma once

#include <Urho3D/Urho3D.h>
#include <Urho3D/Core/Object.h>
#include <Urho3D/Graphics/ShaderVariation.h>

#include <tb_types.h>
#include <tb_system.h>
#include <tb_widgets_listener.h>
#include <tb_window.h>
#include <renderers/tb_renderer_batcher.h>

namespace Urho3D {
class File;
class UIBatch;
class VertexBuffer;
class Texture2D;
class ResourceCache;
class Graphics;
class Input;
}

namespace tb {
extern Urho3D::Context* context_;
}

class TBUrho3DBitmap: public Urho3D::Object, public tb::TBBitmap {
  URHO3D_OBJECT(TBUrho3DBitmap, Urho3D::Object);

public:
  TBUrho3DBitmap(Urho3D::Context* context);
  ~TBUrho3DBitmap();

  static void RegisterObject(Urho3D::Context* context);

  void Init(int width, int height, tb::uint32* data);

  virtual int Width() {
    return size.x_;
  }
  virtual int Height() {
    return size.y_;
  }

  virtual void SetData(tb::uint32* data);

  Urho3D::Vector2 size;
  Urho3D::SharedPtr<Urho3D::Texture2D> texture;
};


class TBUrho3DFile: public tb::TBFile {
public:
  TBUrho3DFile(Urho3D::File* file);
  virtual ~TBUrho3DFile();

  virtual long Size();
  virtual size_t Read(void* buf, size_t elemSize, size_t count);

private:
  Urho3D::SharedPtr<Urho3D::File> file_;
};

// =====================================

class TBUI: public Urho3D::Object, public tb::TBRendererBatcher, public tb::TBWidgetListener {
  URHO3D_OBJECT(TBUI, Urho3D::Object);
public:
  TBUI(Urho3D::Context* context);
  ~TBUI();

  static void RegisterObject(Urho3D::Context* context);
  static void RegisterSystem(Urho3D::Context* context);

  void Init(const Urho3D::String& languageFile);
  void LoadSkin(const Urho3D::String& skin, const Urho3D::String& overrideSkin);
  void AddFontInfo(const Urho3D::String& fileName, const Urho3D::String& fontName);
  void SetDefaultFont(const Urho3D::String& fontName, int size = 12);

  void SetRoot(tb::TBWidget* widget);
  tb::TBWidget* GetRoot() {
    return root_;
  }

  tb::TBWidget* LoadWidget(const Urho3D::String& fileName, tb::TBWidget* widget);
  template<class T> T* LoadWidget(const Urho3D::String& fileName) {
    T* newWidget = new T();
    return static_cast<T*>(LoadWidget(fileName, newWidget));
  }

  tb::TBWidget* GetWidget(const Urho3D::String& name, tb::TBWidget* parent = 0);
  template<class T> T* GetWidget(const Urho3D::String& name, tb::TBWidget* parent = 0) {
    if (!parent) {
      parent = root_;
    }

    return static_cast<T*>(GetWidget(name, parent));
  }

  void ResizeWidgetToFitContent(tb::TBWidget* widget, tb::TBWindow::RESIZE_FIT fit = tb::TBWindow::RESIZE_FIT_PREFERRED);

  // TB Renderer Batcher overrides
public:
  tb::TBBitmap* CreateBitmap(int width, int height, tb::uint32* data) override;
  void RenderBatch(Batch* batch) override;
  void SetClipRect(const tb::TBRect& rect) override;

protected:
  void SetupTurboBadger();
  void SubscribeToEvents();

protected:
  void SetVertexData(Urho3D::VertexBuffer* dest, const Urho3D::PODVector<float>& vertexData);

protected:
  void HandleUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
  void HandleRenderUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);

  void HandleScreenMode(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
  void HandleMouseButtonDown(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
  void HandleMouseButtonUp(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
  void HandleMouseMove(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
  void HandleMouseWheel(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
  void HandleKeyDown(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
  void HandleKeyUp(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
  void HandleTextInput(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);

protected:
  tb::TBWidget* root_;
  Urho3D::IntRect scissor_;
  Urho3D::ResourceCache* cache_;
  Urho3D::Graphics* graphics_;
  Urho3D::Input* input_;
};
[/code]

tb_Urho3D.cpp
[code]
/**
  @license MIT License
  @copyright
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.

  Portions Copyright (c) 2008-2016 the Urho3D project.
  Portions Copyright (c) Thebluefish
  Portions Copyright (c) 2014-2015 THUNDERBEAST GAMES
*/

#include "tb_Urho3D.h"

#include <Urho3D/Urho3D.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/GraphicsEvents.h>
#include <Urho3D/Graphics/VertexBuffer.h>
#include <Urho3D/Graphics/Texture2D.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/IO/Log.h>
#include <Urho3D/Resource/ResourceCache.h>

#include <tb_core.h>
#include <tb_debug.h>
#include <tb_font_renderer.h>
#include <tb_language.h>
#include <tb_skin.h>
#include <tb_widgets_reader.h>
#include <tb_message_window.h>
#include <tb_node_tree.h>
#include <animation/tb_widget_animation.h>

#include <assert.h>

// TB global functions
void register_freetype_font_renderer();

namespace tb {

Urho3D::Context* context_(nullptr);

void TBSystem::RescheduleTimer(double fire_time) { }

TBFile* TBFile::Open(const char* filename, TBFileMode mode) {
  Urho3D::SharedPtr<Urho3D::File> file(context_->GetSubsystem<Urho3D::ResourceCache>()->GetFile(filename));

  if (!file || !file->IsOpen()) {
    return nullptr;
  }

  TBUrho3DFile* tbUrho3DFile(new TBUrho3DFile(file));

  return tbUrho3DFile;
}

} // namespace tb


TBUrho3DBitmap::TBUrho3DBitmap(Urho3D::Context* context) :
  Urho3D::Object(context)
{
}

TBUrho3DBitmap::~TBUrho3DBitmap() {
}

void TBUrho3DBitmap::RegisterObject(Urho3D::Context* context) {
  context->RegisterFactory<TBUrho3DBitmap>();
}

void TBUrho3DBitmap::Init(int width, int height, tb::uint32* data) {
  size = Urho3D::Vector2(width, height);
  SetData(data);
}

void TBUrho3DBitmap::SetData(tb::uint32* data) {
  TBUI* ui(GetSubsystem<TBUI>());

  ui->FlushBitmap(this);

  if (texture.Null()) {
    texture = new Urho3D::Texture2D(context_);

    // Needs to be called BEFORE Texture2D::SetSize
    texture->SetAddressMode(Urho3D::COORD_U, Urho3D::ADDRESS_BORDER);
    texture->SetAddressMode(Urho3D::COORD_V, Urho3D::ADDRESS_BORDER), texture->SetBorderColor(Urho3D::Color(0.0f, 0.0f, 0.0f, 0.0f));
    texture->SetMipsToSkip(Urho3D::QUALITY_LOW, 0);
    texture->SetNumLevels(1);

    texture->SetSize(size.x_, size.y_, Urho3D::Graphics::GetRGBAFormat(), Urho3D::TEXTURE_STATIC);
  }

  texture->SetData(0, 0, 0, size.x_, size.y_, data);
}

TBUrho3DFile::TBUrho3DFile(Urho3D::File* file) :
  file_(file)
{
}

TBUrho3DFile::~TBUrho3DFile() {
  file_->Close();
}

long TBUrho3DFile::Size() {
  return file_->GetSize();
}

size_t TBUrho3DFile::Read(void* buf, size_t elemSize, size_t count) {
  size_t size(elemSize * count);
  size_t totalSize = 0;

  totalSize += file_->Read(buf, size);

  return totalSize;
}

// =====================================

TBUI::TBUI(Urho3D::Context* context):
  Urho3D::Object(context)
  , root_(nullptr)
  , cache_(GetSubsystem<Urho3D::ResourceCache>())
  , graphics_(GetSubsystem<Urho3D::Graphics>())
  , input_(GetSubsystem<Urho3D::Input>())
{
  tb::context_ = context;
  tb::TBWidgetsAnimationManager::Init();
  tb::TBWidgetListener::AddGlobalListener(this);
}

TBUI::~TBUI() {
  TBWidgetListener::RemoveGlobalListener(this);
  tb::TBWidgetsAnimationManager::Shutdown();
  if (root_) delete root_;
  tb::tb_core_shutdown();
}

void TBUI::RegisterObject(Urho3D::Context* context) {
  context->RegisterFactory<TBUI>();
}

void TBUI::RegisterSystem(Urho3D::Context* context) {
  TBUI::RegisterObject(context);
  TBUrho3DBitmap::RegisterObject(context);
}

void TBUI::Init(const Urho3D::String& languageFile) {
  // Initialize Turbo Badger
  tb::tb_core_init(this);

  // Setup localization
  tb::g_tb_lng = new tb::TBLanguage;
  tb::g_tb_lng->Load(languageFile.CString());

  register_freetype_font_renderer();

  SubscribeToEvents();
}

void TBUI::LoadSkin(const Urho3D::String& skin, const Urho3D::String& overrideSkin) {
  // Load the default skin, and override skin (if any)
  tb::g_tb_skin->Load(skin.CString(), overrideSkin.CString());
}


void TBUI::SetDefaultFont(const Urho3D::String& fontName, int size) {
  tb::TBFontDescription fd;
  fd.SetID(TBIDC(fontName.CString()));
  fd.SetSize(tb::g_tb_skin->GetDimensionConverter()->DpToPx(size));
  tb::g_font_manager->SetDefaultFontDescription(fd);
  // Create the font now.
  tb::TBFontFace* font(tb::g_font_manager->CreateFontFace(tb::g_font_manager->GetDefaultFontDescription()));

  // Render some glyphs in one go now since we know we are going to use them. It would work fine
  // without this since glyphs are rendered when needed, but with some extra updating of the glyph bitmap.
  if (font)
    font->RenderGlyphs(" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~????????");
}

void TBUI::AddFontInfo(const Urho3D::String& fileName, const Urho3D::String& fontName) {
  tb::g_font_manager->AddFontInfo(fileName.CString(), fontName.CString());
}

void TBUI::SetRoot(tb::TBWidget* widget) {
  root_ = widget;
  root_->SetSize(graphics_->GetWidth(), graphics_->GetHeight());
}

tb::TBWidget* TBUI::GetWidget(const Urho3D::String& name, tb::TBWidget* parent) {
  return parent->GetWidgetByID(TBIDC(name.CString()));
}

tb::TBWidget* TBUI::LoadWidget(const Urho3D::String& fileName, tb::TBWidget* widget) {
  // Load widget
  tb::TBNode node;
  if (node.ReadFile(fileName.CString())) {
    tb::g_widgets_reader->LoadNodeTree(widget, &node);
  }
  return widget;
}

void TBUI::ResizeWidgetToFitContent(tb::TBWidget* widget, tb::TBWindow::RESIZE_FIT fit) {
  assert(widget);
  tb::PreferredSize ps(widget->GetPreferredSize());
  int new_w(ps.pref_w);
  int new_h(ps.pref_h);
  if (fit == tb::TBWindow::RESIZE_FIT_MINIMAL) {
    new_w = ps.min_w;
    new_h = ps.min_h;
  } else if (fit == tb::TBWindow::RESIZE_FIT_CURRENT_OR_NEEDED) {
    new_w = tb::Clamp(widget->GetRect().w, ps.min_w, ps.max_w);
    new_h = tb::Clamp(widget->GetRect().h, ps.min_h, ps.max_h);
  }
  if (widget->GetParent()) {
    new_w = tb::Min(new_w, widget->GetParent()->GetRect().w);
    new_h = tb::Min(new_h, widget->GetParent()->GetRect().h);
  }
  widget->SetRect(tb::TBRect(widget->GetRect().x, widget->GetRect().y, new_w, new_h));
}

tb::TBBitmap* TBUI::CreateBitmap(int width, int height, tb::uint32* data) {
  TBUrho3DBitmap* bitmap(new TBUrho3DBitmap(context_));
  bitmap->Init(width, height, data);

  return bitmap;
}

void TBUI::RenderBatch(Batch* batch) {
  if (!batch->vertex_count)
    return;

  Urho3D::Texture2D* texture(NULL);

  if (batch->bitmap) {
    TBUrho3DBitmap* tbuibitmap((TBUrho3DBitmap*)batch->bitmap);
    texture = tbuibitmap->texture;
  }

  Urho3D::PODVector<float> vertexData;
  Urho3D::SharedPtr<Urho3D::VertexBuffer> vertexBuffer(new Urho3D::VertexBuffer(context_));

  Urho3D::UIBatch newBatch;
  newBatch.blendMode_ = Urho3D::BLEND_ALPHA;
  newBatch.scissor_ = scissor_;
  newBatch.texture_ = texture;
  newBatch.vertexData_ = &vertexData;
  newBatch.invTextureSize_ = (texture ? Urho3D::Vector2(1.0f / (float)texture->GetWidth(), 1.0f / (float)texture->GetHeight()) : Urho3D::Vector2::ONE);

  unsigned begin(newBatch.vertexData_->Size());
  newBatch.vertexData_->Resize(begin + batch->vertex_count * Urho3D::UI_VERTEX_SIZE);
  float* dest(&(newBatch.vertexData_->At(begin)));
  newBatch.vertexEnd_ = newBatch.vertexData_->Size();

  for (int i = 0; i < batch->vertex_count; i++) {
    Vertex* v = &batch->vertex[i];
    dest[0] = v->x;
    dest[1] = v->y;
    dest[2] = 0.0f;
    ((unsigned&)dest[3]) = v->col;
    dest[4] = v->u;
    dest[5] = v->v;
    dest += Urho3D::UI_VERTEX_SIZE;
  }

  SetVertexData(vertexBuffer, vertexData);

  Urho3D::Vector2 invScreenSize(1.0f / (float)graphics_->GetWidth(), 1.0f / (float)graphics_->GetHeight());
  Urho3D::Vector2 scale(2.0f * invScreenSize.x_, -2.0f * invScreenSize.y_);
  Urho3D::Vector2 offset(-1.0f, 1.0f);

  Urho3D::Matrix4 projection(Urho3D::Matrix4::IDENTITY);
  projection.m00_ = scale.x_;
  projection.m03_ = offset.x_;
  projection.m11_ = scale.y_;
  projection.m13_ = offset.y_;
  projection.m22_ = 1.0f;
  projection.m23_ = 0.0f;
  projection.m33_ = 1.0f;

  graphics_->ClearParameterSources();
  graphics_->SetColorWrite(true);
  graphics_->SetCullMode(Urho3D::CULL_NONE);
  graphics_->SetDepthTest(Urho3D::CMP_ALWAYS);
  graphics_->SetDepthWrite(false);
  graphics_->SetFillMode(Urho3D::FILL_SOLID);
  graphics_->SetStencilTest(false);

  graphics_->ResetRenderTargets();

  graphics_->SetVertexBuffer(vertexBuffer);

  Urho3D::ShaderVariation* noTextureVS(graphics_->GetShader(Urho3D::VS, "Basic", "VERTEXCOLOR"));
  Urho3D::ShaderVariation* diffTextureVS(graphics_->GetShader(Urho3D::VS, "Basic", "DIFFMAP VERTEXCOLOR"));
  Urho3D::ShaderVariation* noTexturePS(graphics_->GetShader(Urho3D::PS, "Basic", "VERTEXCOLOR"));
  Urho3D::ShaderVariation* diffTexturePS(graphics_->GetShader(Urho3D::PS, "Basic", "DIFFMAP VERTEXCOLOR"));
  Urho3D::ShaderVariation* diffMaskTexturePS(graphics_->GetShader(Urho3D::PS, "Basic", "DIFFMAP ALPHAMASK VERTEXCOLOR"));
  Urho3D::ShaderVariation* alphaTexturePS(graphics_->GetShader(Urho3D::PS, "Basic", "ALPHAMAP VERTEXCOLOR"));

  unsigned alphaFormat(Urho3D::Graphics::GetAlphaFormat());

  if (newBatch.vertexStart_ == newBatch.vertexEnd_) {
    return;
  }

  Urho3D::ShaderVariation* ps;
  Urho3D::ShaderVariation* vs;

  if (!newBatch.texture_) {
    ps = noTexturePS;
    vs = noTextureVS;
  } else {
    // If texture contains only an alpha channel, use alpha shader (for fonts)
    vs = diffTextureVS;

    if (newBatch.texture_->GetFormat() == alphaFormat) {
      ps = alphaTexturePS;
    } else if (newBatch.blendMode_ != Urho3D::BLEND_ALPHA && newBatch.blendMode_ != Urho3D::BLEND_ADDALPHA && newBatch.blendMode_ != Urho3D::BLEND_PREMULALPHA) {
      ps = diffMaskTexturePS;
    } else {
      ps = diffTexturePS;
    }
  }

  graphics_->SetShaders(vs, ps);
  if (graphics_->NeedParameterUpdate(Urho3D::SP_OBJECT, this)) {
    graphics_->SetShaderParameter(Urho3D::VSP_MODEL, Urho3D::Matrix3x4::IDENTITY);
  }
  if (graphics_->NeedParameterUpdate(Urho3D::SP_CAMERA, this)) {
    graphics_->SetShaderParameter(Urho3D::VSP_VIEWPROJ, projection);
  }
  if (graphics_->NeedParameterUpdate(Urho3D::SP_MATERIAL, this)) {
    graphics_->SetShaderParameter(Urho3D::PSP_MATDIFFCOLOR, Urho3D::Color(1.0f, 1.0f, 1.0f, 1.0f));
  }

  graphics_->SetBlendMode(newBatch.blendMode_);
  graphics_->SetScissorTest(true, newBatch.scissor_);
  graphics_->SetTexture(0, newBatch.texture_);
  graphics_->Draw(Urho3D::TRIANGLE_LIST, newBatch.vertexStart_ / Urho3D::UI_VERTEX_SIZE, (newBatch.vertexEnd_ - newBatch.vertexStart_) / Urho3D::UI_VERTEX_SIZE);
}

void TBUI::SetClipRect(const tb::TBRect& rect) {
  scissor_.top_ = rect.y;
  scissor_.left_ = rect.x;
  scissor_.bottom_ = rect.y + rect.h;
  scissor_.right_ = rect.x + rect.w;
}

void TBUI::SubscribeToEvents() {
  SubscribeToEvent(Urho3D::E_UPDATE, URHO3D_HANDLER(TBUI, HandleUpdate));
  SubscribeToEvent(Urho3D::E_ENDRENDERING, URHO3D_HANDLER(TBUI, HandleRenderUpdate));

  SubscribeToEvent(Urho3D::E_SCREENMODE, URHO3D_HANDLER(TBUI, HandleScreenMode));
  SubscribeToEvent(Urho3D::E_MOUSEBUTTONDOWN, URHO3D_HANDLER(TBUI, HandleMouseButtonDown));
  SubscribeToEvent(Urho3D::E_MOUSEBUTTONUP, URHO3D_HANDLER(TBUI, HandleMouseButtonUp));
  SubscribeToEvent(Urho3D::E_MOUSEMOVE, URHO3D_HANDLER(TBUI, HandleMouseMove));
  SubscribeToEvent(Urho3D::E_MOUSEWHEEL, URHO3D_HANDLER(TBUI, HandleMouseWheel));
  SubscribeToEvent(Urho3D::E_KEYDOWN, URHO3D_HANDLER(TBUI, HandleKeyDown));
  SubscribeToEvent(Urho3D::E_KEYUP, URHO3D_HANDLER(TBUI, HandleKeyUp));
  SubscribeToEvent(Urho3D::E_TEXTINPUT, URHO3D_HANDLER(TBUI, HandleTextInput));
}

void TBUI::SetVertexData(Urho3D::VertexBuffer* dest, const Urho3D::PODVector<float>& vertexData) {
  if (vertexData.Empty()) {
    return;
  }

  // Update quad geometry into the vertex buffer
  // Resize the vertex buffer first if too small or much too large
  unsigned numVertices(vertexData.Size() / Urho3D::UI_VERTEX_SIZE);
  if (dest->GetVertexCount() < numVertices || dest->GetVertexCount() > numVertices * 2) {
    dest->SetSize(numVertices, Urho3D::MASK_POSITION | Urho3D::MASK_COLOR | Urho3D::MASK_TEXCOORD1, true);
  }

  dest->SetData(&vertexData[0]);
}

void TBUI::HandleUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData) {
  tb::TBMessageHandler::ProcessMessages();
}

void TBUI::HandleRenderUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData) {
  // Setup scissor
  tb::TBRect rect(root_->GetRect());
  scissor_ = Urho3D::IntRect(0, 0, rect.w, rect.h);

  tb::TBAnimationManager::Update();

  // Update all widgets
  root_->InvokeProcessStates();
  root_->InvokeProcess();

  // Render UI
  tb::g_renderer->BeginPaint(rect.w, rect.h);

  root_->InvokePaint(tb::TBWidget::PaintProps());

  tb::g_renderer->EndPaint();

  //_root->Invalidate();
}

void TBUI::HandleScreenMode(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData) {
  using namespace Urho3D::ScreenMode;

  int width(eventData[P_WIDTH].GetInt());
  int height(eventData[P_HEIGHT].GetInt());

  root_->SetSize(width, height);
}

void TBUI::HandleMouseButtonDown(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData) {
  using namespace Urho3D::MouseButtonDown;

  unsigned button(eventData[P_BUTTON].GetUInt());
  unsigned qualifiers(eventData[P_QUALIFIERS].GetUInt());

  Urho3D::IntVector2 mousePosition(input_->GetMousePosition());

  tb::MODIFIER_KEYS modifiers(tb::TB_MODIFIER_NONE);
  if (qualifiers & Urho3D::QUAL_CTRL) {
    modifiers |= tb::TB_CTRL;
  }
  if (qualifiers & Urho3D::QUAL_SHIFT) {
    modifiers |= tb::TB_SHIFT;
  }
  if (qualifiers & Urho3D::QUAL_ALT) {
    modifiers |= tb::TB_ALT;
  }

  switch (button) {
  case Urho3D::MOUSEB_LEFT:
    root_->InvokePointerDown(mousePosition.x_, mousePosition.y_, 1, modifiers, false);
    break;
  }

}

void TBUI::HandleMouseButtonUp(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData) {
  using namespace Urho3D::MouseButtonUp;

  unsigned button(eventData[P_BUTTON].GetUInt());
  unsigned qualifiers(eventData[P_QUALIFIERS].GetUInt());

  Urho3D::IntVector2 mousePosition(input_->GetMousePosition());

  tb::MODIFIER_KEYS modifiers(tb::TB_MODIFIER_NONE);
  if (qualifiers & Urho3D::QUAL_CTRL) {
    modifiers |= tb::TB_CTRL;
  }
  if (qualifiers & Urho3D::QUAL_SHIFT) {
    modifiers |= tb::TB_SHIFT;
  }
  if (qualifiers & Urho3D::QUAL_ALT) {
    modifiers |= tb::TB_ALT;
  }

  switch (button) {
  case Urho3D::MOUSEB_LEFT:
    root_->InvokePointerUp(mousePosition.x_, mousePosition.y_, modifiers, false);
    break;
  case Urho3D::MOUSEB_RIGHT:
    tb::TBWidgetEvent ev(tb::EVENT_TYPE_CONTEXT_MENU, mousePosition.x_, mousePosition.y_, false, modifiers);
    root_->InvokeEvent(ev);
    break;
  }
}

void TBUI::HandleMouseMove(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData) {
  using namespace Urho3D::MouseMove;

/*
  int x(eventData[P_X].GetInt());
  int y(eventData[P_Y].GetInt());
*/

  unsigned qualifiers(eventData[P_QUALIFIERS].GetUInt());
  Urho3D::IntVector2 mousePosition(input_->GetMousePosition());

  tb::MODIFIER_KEYS modifiers(tb::TB_MODIFIER_NONE);
  if (qualifiers & Urho3D::QUAL_CTRL)
    modifiers |= tb::TB_CTRL;
  if (qualifiers & Urho3D::QUAL_SHIFT)
    modifiers |= tb::TB_SHIFT;
  if (qualifiers & Urho3D::QUAL_ALT)
    modifiers |= tb::TB_ALT;

  root_->InvokePointerMove(mousePosition.x_, mousePosition.y_, modifiers, false);
}

void TBUI::HandleMouseWheel(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData) {
  using namespace Urho3D::MouseWheel;

  int wheel(eventData[P_WHEEL].GetInt());
  unsigned qualifiers(eventData[P_QUALIFIERS].GetInt());

  Urho3D::Input* input_(GetSubsystem<Urho3D::Input>());
  Urho3D::IntVector2 mousePosition(input_->GetMousePosition());

  tb::MODIFIER_KEYS modifiers(tb::TB_MODIFIER_NONE);
  if (qualifiers & Urho3D::QUAL_CTRL) {
    modifiers |= tb::TB_CTRL;
  }
  if (qualifiers & Urho3D::QUAL_SHIFT) {
    modifiers |= tb::TB_SHIFT;
  }
  if (qualifiers & Urho3D::QUAL_ALT) {
    modifiers |= tb::TB_ALT;
  }

  root_->InvokeWheel(mousePosition.x_, mousePosition.y_, 0, -wheel, tb::TB_MODIFIER_NONE);
}

void TBUI::HandleKeyDown(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData) {
  using namespace Urho3D::KeyDown;

  int key(eventData[P_KEY].GetInt());
  unsigned qualifiers(eventData[P_QUALIFIERS].GetUInt());

  Urho3D::Input* input_(GetSubsystem<Urho3D::Input>());
  Urho3D::IntVector2 mousePosition(input_->GetMousePosition());

  tb::MODIFIER_KEYS modifiers(tb::TB_MODIFIER_NONE);
  if (qualifiers & Urho3D::QUAL_CTRL) {
    modifiers |= tb::TB_CTRL;
  }
  if (qualifiers & Urho3D::QUAL_SHIFT) {
    modifiers |= tb::TB_SHIFT;
  }
  if (qualifiers & Urho3D::QUAL_ALT) {
    modifiers |= tb::TB_ALT;
  }

  switch (key) {
  case Urho3D::KEY_RETURN:
  case Urho3D::KEY_RETURN2:
  case Urho3D::KEY_KP_ENTER:
    root_->InvokeKey(0, tb::TB_KEY_ENTER, modifiers, true);
    break;
  case Urho3D::KEY_F1:
    root_->InvokeKey(0, tb::TB_KEY_F1, modifiers, true);
    break;
  case Urho3D::KEY_F2:
    root_->InvokeKey(0, tb::TB_KEY_F2, modifiers, true);
    break;
  case Urho3D::KEY_F3:
    root_->InvokeKey(0, tb::TB_KEY_F3, modifiers, true);
    break;
  case Urho3D::KEY_F4:
    root_->InvokeKey(0, tb::TB_KEY_F4, modifiers, true);
    break;
  case Urho3D::KEY_F5:
    root_->InvokeKey(0, tb::TB_KEY_F5, modifiers, true);
    break;
  case Urho3D::KEY_F6:
    root_->InvokeKey(0, tb::TB_KEY_F6, modifiers, true);
    break;
  case Urho3D::KEY_F7:
    root_->InvokeKey(0, tb::TB_KEY_F7, modifiers, true);
    break;
  case Urho3D::KEY_F8:
    root_->InvokeKey(0, tb::TB_KEY_F8, modifiers, true);
    break;
  case Urho3D::KEY_F9:
    root_->InvokeKey(0, tb::TB_KEY_F9, modifiers, true);
    break;
  case Urho3D::KEY_F10:
    root_->InvokeKey(0, tb::TB_KEY_F10, modifiers, true);
    break;
  case Urho3D::KEY_F11:
    root_->InvokeKey(0, tb::TB_KEY_F11, modifiers, true);
    break;
  case Urho3D::KEY_F12:
    root_->InvokeKey(0, tb::TB_KEY_F12, modifiers, true);
    break;
  case Urho3D::KEY_LEFT:
    root_->InvokeKey(0, tb::TB_KEY_LEFT, modifiers, true);
    break;
  case Urho3D::KEY_UP:
    root_->InvokeKey(0, tb::TB_KEY_UP, modifiers, true);
    break;
  case Urho3D::KEY_RIGHT:
    root_->InvokeKey(0, tb::TB_KEY_RIGHT, modifiers, true);
    break;
  case Urho3D::KEY_DOWN:
    root_->InvokeKey(0, tb::TB_KEY_DOWN, modifiers, true);
    break;
  case Urho3D::KEY_PAGEUP:
    root_->InvokeKey(0, tb::TB_KEY_PAGE_UP, modifiers, true);
    break;
  case Urho3D::KEY_PAGEDOWN:
    root_->InvokeKey(0, tb::TB_KEY_PAGE_DOWN, modifiers, true);
    break;
  case Urho3D::KEY_HOME:
    root_->InvokeKey(0, tb::TB_KEY_HOME, modifiers, true);
    break;
  case Urho3D::KEY_END:
    root_->InvokeKey(0, tb::TB_KEY_END, modifiers, true);
    break;
  case Urho3D::KEY_INSERT:
    root_->InvokeKey(0, tb::TB_KEY_INSERT, modifiers, true);
    break;
  case Urho3D::KEY_TAB:
    root_->InvokeKey(0, tb::TB_KEY_TAB, modifiers, true);
    break;
  case Urho3D::KEY_DELETE:
    root_->InvokeKey(0, tb::TB_KEY_DELETE, modifiers, true);
    break;
  case Urho3D::KEY_BACKSPACE:
    root_->InvokeKey(0, tb::TB_KEY_BACKSPACE, modifiers, true);
    break;
  case Urho3D::KEY_ESCAPE:
    root_->InvokeKey(0, tb::TB_KEY_ESC, modifiers, true);
    break;
  default:
    if (modifiers & tb::TB_SUPER) {
      root_->InvokeKey(key, tb::TB_KEY_UNDEFINED, modifiers, true);
    }
  }
}

void TBUI::HandleKeyUp(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData) {
  using namespace Urho3D::KeyUp;

  int key(eventData[P_KEY].GetInt());
  unsigned qualifiers(eventData[P_QUALIFIERS].GetUInt());

  Urho3D::Input* input_(GetSubsystem<Urho3D::Input>());
  Urho3D::IntVector2 mousePosition(input_->GetMousePosition());

  tb::MODIFIER_KEYS modifiers(tb::TB_MODIFIER_NONE);
  if (qualifiers & Urho3D::QUAL_CTRL) {
    modifiers |= tb::TB_CTRL;
  }
  if (qualifiers & Urho3D::QUAL_SHIFT) {
    modifiers |= tb::TB_SHIFT;
  }
  if (qualifiers & Urho3D::QUAL_ALT) {
    modifiers |= tb::TB_ALT;
  }

  switch (key) {
  case Urho3D::KEY_RETURN:
  case Urho3D::KEY_RETURN2:
  case Urho3D::KEY_KP_ENTER:
    root_->InvokeKey(0, tb::TB_KEY_ENTER, modifiers, false);
    break;
  case Urho3D::KEY_F1:
    root_->InvokeKey(0, tb::TB_KEY_F1, modifiers, false);
    break;
  case Urho3D::KEY_F2:
    root_->InvokeKey(0, tb::TB_KEY_F2, modifiers, false);
    break;
  case Urho3D::KEY_F3:
    root_->InvokeKey(0, tb::TB_KEY_F3, modifiers, false);
    break;
  case Urho3D::KEY_F4:
    root_->InvokeKey(0, tb::TB_KEY_F4, modifiers, false);
    break;
  case Urho3D::KEY_F5:
    root_->InvokeKey(0, tb::TB_KEY_F5, modifiers, false);
    break;
  case Urho3D::KEY_F6:
    root_->InvokeKey(0, tb::TB_KEY_F6, modifiers, false);
    break;
  case Urho3D::KEY_F7:
    root_->InvokeKey(0, tb::TB_KEY_F7, modifiers, false);
    break;
  case Urho3D::KEY_F8:
    root_->InvokeKey(0, tb::TB_KEY_F8, modifiers, false);
    break;
  case Urho3D::KEY_F9:
    root_->InvokeKey(0, tb::TB_KEY_F9, modifiers, false);
    break;
  case Urho3D::KEY_F10:
    root_->InvokeKey(0, tb::TB_KEY_F10, modifiers, false);
    break;
  case Urho3D::KEY_F11:
    root_->InvokeKey(0, tb::TB_KEY_F11, modifiers, false);
    break;
  case Urho3D::KEY_F12:
    root_->InvokeKey(0, tb::TB_KEY_F12, modifiers, false);
    break;
  case Urho3D::KEY_LEFT:
    root_->InvokeKey(0, tb::TB_KEY_LEFT, modifiers, false);
    break;
  case Urho3D::KEY_UP:
    root_->InvokeKey(0, tb::TB_KEY_UP, modifiers, false);
    break;
  case Urho3D::KEY_RIGHT:
    root_->InvokeKey(0, tb::TB_KEY_RIGHT, modifiers, false);
    break;
  case Urho3D::KEY_DOWN:
    root_->InvokeKey(0, tb::TB_KEY_DOWN, modifiers, false);
    break;
  case Urho3D::KEY_PAGEUP:
    root_->InvokeKey(0, tb::TB_KEY_PAGE_UP, modifiers, false);
    break;
  case Urho3D::KEY_PAGEDOWN:
    root_->InvokeKey(0, tb::TB_KEY_PAGE_DOWN, modifiers, false);
    break;
  case Urho3D::KEY_HOME:
    root_->InvokeKey(0, tb::TB_KEY_HOME, modifiers, false);
    break;
  case Urho3D::KEY_END:
    root_->InvokeKey(0, tb::TB_KEY_END, modifiers, false);
    break;
  case Urho3D::KEY_INSERT:
    root_->InvokeKey(0, tb::TB_KEY_INSERT, modifiers, false);
    break;
  case Urho3D::KEY_TAB:
    root_->InvokeKey(0, tb::TB_KEY_TAB, modifiers, false);
    break;
  case Urho3D::KEY_DELETE:
    root_->InvokeKey(0, tb::TB_KEY_DELETE, modifiers, false);
    break;
  case Urho3D::KEY_BACKSPACE:
    root_->InvokeKey(0, tb::TB_KEY_BACKSPACE, modifiers, false);
    break;
  case Urho3D::KEY_ESCAPE:
    root_->InvokeKey(0, tb::TB_KEY_ESC, modifiers, false);
    break;
  default:
    if (modifiers & tb::TB_SUPER) {
      root_->InvokeKey(key, tb::TB_KEY_UNDEFINED, modifiers, false);
    }
  }
}

void TBUI::HandleTextInput(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData) {
  using namespace Urho3D::TextInput;

  Urho3D::String text(eventData[P_TEXT].GetString());

  for (unsigned i = 0; i < text.Length(); i++) {
    root_->InvokeKey(text[i], tb::TB_KEY_UNDEFINED, tb::TB_MODIFIER_NONE, true);
    root_->InvokeKey(text[i], tb::TB_KEY_UNDEFINED, tb::TB_MODIFIER_NONE, false);
  }
}
[/code]

-------------------------

sabotage3d | 2017-01-02 01:13:57 UTC | #14

Thanks a lot.

-------------------------

rku | 2017-01-02 01:14:12 UTC | #15

[quote="carnalis"]I think the implementation that was posted still exists and I'll look to posting that when it's available.

Here is my own working edition of the implementation.  Changes include a license header (let me know if it needs further changes), some private to protected members, various updates for Urho3D, formatting. no real API changes that I recall...

tb_Urho3D.h
[spoiler][code][/code][/spoiler]

tb_Urho3D.cpp
[spoiler][code][/code][/spoiler][/quote]

Is this really complete? Because i can not get it working.

Edit:
For the next poor soul that bumps into same thing here is working example:
[code]    TurboBadgerUI::RegisterSystem(context_);
    tbui.Init("TBUI/language/lng_en.tb.txt");
    tbui.LoadSkin("TBUI/default_skin/skin.tb.txt");
    tbui.AddFontInfo("TBUI/vera.ttf", "Vera");
    tbui.SetDefaultFont("Vera", 14);
    tbui.SetRoot(new tb::TBWidget());
    auto window = tbui.LoadWidget<tb::TBWindow>("TBUI/ui_resources/test_layout01.tb.txt");
    tbui.GetRoot()->AddChild(window);
    tbui.ResizeWidgetToFitContent(window);
[/code]

For some reason default fotns (.tb.txt) did not work however ttf fonts work fine. Also trick was to call tbui.ResizeWidgetToFitContent(window); because for some reason widget size initially seems to be 0;0.

Really nice class by the way. I love it how its two files handling all the integration. Thanks.

-------------------------

jmiller | 2017-01-02 01:14:13 UTC | #16

To configure tb/tb_config.h for Linux, I enable #define TB_FONT_RENDERER_TBBF, enable TB_FONT_RENDERER_FREETYPE, undefine TB_FILE_POSIX (we're using TBUrho3DFile), and it was similar for MSWindows.

And yes, to solve a problem we all had: ResizeWidgetToFitContent() was written to size widgets which are [i]not[/i] within a top-level widget like TBWindow (TB docs did not make this clear at the time).

Here is my TB-Urho3D setup code [b]*edit: added more context[/b]
cfg_ refers to the config file parser here: [topic1502.html](http://discourse.urho3d.io/t/a-more-advanced-ini-parser/1449/1)
[code]
#include <tb_widgets.h>
#include <tb_widgets_listener.h>
#include <tb_widgets_common.h>

class UIManager : public Urho3D::Object, public tb::TBWidgetListener {
//...
  TBUI* tbui_;
  tb::TBWidget* tbRoot_;
  bool OnWidgetInvokeEvent(tb::TBWidget* widget, const tb::TBWidgetEvent& ev);
//...
};

// in UIManager::Initialize()

if (!tbui_) {
  TBUI::RegisterSystem(context_); // TBBitmap & TBUI RegisterObject()
  context_->RegisterSubsystem(new TBUI(context_));
  tbui_ = GetSubsystem<TBUI>(); }
if (!tbui_) {
  URHO3D_LOGERROR("TBUI subsystem unregistered.");
  return false; }

const String langFileName(cfg_->GetString("ui", "languageFile", "UI/language/lng_en.tb.txt"));
tbui_->Init(langFileName);

// Load skin(s).
const String skinOverrideFile(cfg_->GetString("ui", "skinOverrideFile"));
const String skinDefaultFile(cfg_->GetString("ui", "skinDefaultFile"));
LoadSkins(skinDefaultFile, skinOverrideFile);

// Setup default font.
const String fontName(cfg_->GetString("ui", "fontName", "NotoMono-Regular"));
const String fontFile(cfg_->GetString("ui", "fontFile", "Fonts/NotoMono-Regular.ttf"));

if (cache_->Exists(fontFile)) {
  tbui_->AddFontInfo(fontFile, fontName);
  tbui_->SetDefaultFont(fontName); }
else {
  URHO3D_LOGERROR("UIManager: cannot find default font: " + fontFile); }

TBWidgetListener::AddGlobalListener(this); // Remember to RemoveGlobalListener(this) on delete.

tbRoot_ = new TBWidget(); // TBUI deletes the tree itself.
tbui_->SetRoot(tbRoot_);

//////////////////

bool UIManager::LoadSkins(const String& skinDefaultFile, const String& skinOverrideFile/*= String::EMPTY */) {
  bool loaded(false);
  if (skinDefaultFile == String::EMPTY) {
    URHO3D_LOGERROR("UIManager::LoadSkins: skinDefaultFile empty");
    return false; }
  if (!cache_->Exists(skinDefaultFile)) {
    URHO3D_LOGERROR("UIManager: Skin file not found: " + skinDefaultFile);
    return false; }

  if (skinOverrideFile != String::EMPTY) {
    if (!cache_->Exists(skinOverrideFile)) {
      URHO3D_LOGWARNING("UIManager: Skin override file not found: " + skinOverrideFile); }
    loaded = tb::g_tb_skin->Load(skinDefaultFile.CString(), skinOverrideFile.CString()); }
  else {
    loaded = tb::g_tb_skin->Load(skinDefaultFile.CString()); }
  if (!loaded) {
    URHO3D_LOGERROR("UIManager: Skin file load failed: " + skinDefaultFile + "  override: " + skinOverrideFile); }
  return loaded;
}
[/code]

If it is help to someone, here is the tb_Urho3D originally posted by Thebluefish. Note that it does not include my updates; I only added the license header.

[quote="Thebluefish"]
TBUI.h
[code]
/**
  @license MIT License
  @copyright
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.

  Portions Copyright (c) 2008-2016 the Urho3D project.
  Portions Copyright (c) Thebluefish
  Portions Copyright (c) 2014-2015 THUNDERBEAST GAMES
*/

#ifndef _TBUI_TBUI_H
#define _TBUI_TBUI_H

#include <Urho3D/Urho3D.h>
#include <Urho3D/Core/Object.h>
#include <Urho3D/Graphics/ShaderVariation.h>

#include <tb_types.h>
#include <tb_system.h>
#include <tb_widgets_listener.h>
#include <tb_window.h>
#include <renderers/tb_renderer_batcher.h>

namespace Urho3D
{
   class File;
   class UIBatch;
   class VertexBuffer;
   class Texture2D;
}

namespace JRPG
{
   namespace UI
   {
      class Bitmap : public Urho3D::Object, public tb::TBBitmap
      {
         OBJECT(Bitmap);

      public:
         Bitmap(Urho3D::Context* context);
         ~Bitmap();

         static void RegisterObject(Urho3D::Context* context);

         void Init(int width, int height, tb::uint32 *data);

         virtual int Width() { return size.x_; }
         virtual int Height() { return size.y_; }

         virtual void SetData(tb::uint32 *data);

         Urho3D::Vector2 size;
         Urho3D::SharedPtr<Urho3D::Texture2D> texture;
      };

      class TBUrho3DFile : public tb::TBFile
      {
      public:
         TBUrho3DFile(Urho3D::File* file);
         virtual ~TBUrho3DFile();

         virtual long Size();
         virtual size_t Read(void *buf, size_t elemSize, size_t count);

      private:
         Urho3D::SharedPtr<Urho3D::File> _file;
      };

      // Turbo Badger UI subsystem
      class TBUI : public Urho3D::Object, public tb::TBRendererBatcher, public tb::TBWidgetListener
      {
         OBJECT(TBUI);

      public:
         TBUI(Urho3D::Context* context);
         ~TBUI();

         static void RegisterObject(Urho3D::Context* context);
         static void RegisterSystem(Urho3D::Context* context);

         void Init();

         void AddFontInfo(const Urho3D::String& fileName, const Urho3D::String& fontName);
         void SetFont(const Urho3D::String& fontName, int size = 12);

         tb::TBWidget* GetRoot() { return _root; }
         void SetRoot(tb::TBWidget* widget);

         tb::TBWidget* GetWidget(const Urho3D::String& name, tb::TBWidget* parent = 0);
         template<class T> T* GetWidget(const Urho3D::String& name, tb::TBWidget* parent = 0)
         {
            if (!parent)
               parent = _root;

            return static_cast<T*>(GetWidget(name, parent));
         }

         tb::TBWidget* LoadWidget(const Urho3D::String& fileName, tb::TBWidget* widget);
         template<class T> T* LoadWidget(const Urho3D::String& fileName)
         {
            T* newWidget = new T();
            return (T*)LoadWidget(fileName, newWidget);
         }
         
         void ResizeWidgetToFitContent(tb::TBWidget* widget, tb::TBWindow::RESIZE_FIT fit = tb::TBWindow::RESIZE_FIT_PREFERRED);

         // TB Renderer Batcher overrides
      public:

         tb::TBBitmap *CreateBitmap(int width, int height, tb::uint32* data) override;
         void RenderBatch(Batch* batch) override;
         void SetClipRect(const tb::TBRect& rect) override;

         // Internal functions
      protected:

         void SetupTurboBadger();

         void SubscribeToEvents();

         
      protected:

         void SetVertexData(Urho3D::VertexBuffer* dest, const Urho3D::PODVector<float>& vertexData);

      protected:

         void HandleUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
         void HandleRenderUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);

         void HandleScreenMode(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
         void HandleMouseButtonDown(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
         void HandleMouseButtonUp(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
         void HandleMouseMove(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
         void HandleMouseWheel(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
         void HandleKeyDown(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
         void HandleKeyUp(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
         void HandleTextInput(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);

      private:

         tb::TBWidget* _root;

         Urho3D::IntRect _scissor;
      };
   }
}
#endif
[/code]

TBUI.cpp
[code]
/**
  @license MIT License
  @copyright
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.

  Portions Copyright (c) 2008-2016 the Urho3D project.
  Portions Copyright (c) Thebluefish
  Portions Copyright (c) 2014-2015 THUNDERBEAST GAMES
*/

#include "TBUI.h"

#include <Urho3D/Urho3D.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/GraphicsEvents.h>
#include <Urho3D/Graphics/VertexBuffer.h>
#include <Urho3D/Graphics/Texture2D.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/Resource/ResourceCache.h>




#include <tb_core.h>
#include <tb_debug.h>
#include <tb_font_renderer.h>
#include <tb_language.h>
#include <tb_skin.h>
#include <tb_widgets_reader.h>

#include <tb_message_window.h>
#include <tb_node_tree.h>
#include <animation/tb_widget_animation.h>

// TB global functions
void register_freetype_font_renderer();

namespace tb
{
   static Urho3D::WeakPtr<Urho3D::Context> _context;

   void TBSystem::RescheduleTimer(double fire_time) { }

   TBFile* TBFile::Open(const char *filename, TBFileMode mode)
   {
      auto cache = _context->GetSubsystem<Urho3D::ResourceCache>();

      Urho3D::SharedPtr<Urho3D::File> file = cache->GetFile(filename);

      if (!file || !file->IsOpen())
      {
         //LOGERRORF("TBUI: Unable to load file: %s", filename);
         return 0;
      }

      JRPG::UI::TBUrho3DFile* tbUrho3DFile = new JRPG::UI::TBUrho3DFile(file);

      return tbUrho3DFile;
   }
}

namespace JRPG
{
   namespace UI
   {
      Bitmap::Bitmap(Urho3D::Context* context) :
         Urho3D::Object(context)
      {
      }

      Bitmap::~Bitmap()
      {

      }

      void Bitmap::RegisterObject(Urho3D::Context* context)
      {
         context->RegisterFactory<Bitmap>();
      }

      void Bitmap::Init(int width, int height, tb::uint32 *data)
      {
         size = Urho3D::Vector2(width, height);

         SetData(data);
      }

      void Bitmap::SetData(tb::uint32 *data)
      {
         auto ui = GetSubsystem<TBUI>();

         ui->FlushBitmap(this);

         if (texture.Null())
         {
            texture = new Urho3D::Texture2D(context_);

            // Needs to be called BEFORE Texture2D::SetSize
            texture->SetAddressMode(Urho3D::COORD_U, Urho3D::ADDRESS_BORDER);
            texture->SetAddressMode(Urho3D::COORD_V, Urho3D::ADDRESS_BORDER),
               texture->SetBorderColor(Urho3D::Color(0.0f, 0.0f, 0.0f, 0.0f));
            texture->SetMipsToSkip(Urho3D::QUALITY_LOW, 0);
            texture->SetNumLevels(1);

            texture->SetSize(size.x_, size.y_, Urho3D::Graphics::GetRGBAFormat(), Urho3D::TEXTURE_STATIC);
         }

         texture->SetData(0, 0, 0, size.x_, size.y_, data);
      }

      TBUrho3DFile::TBUrho3DFile(Urho3D::File* file) :
         _file(file)
      {

      }
      TBUrho3DFile::~TBUrho3DFile()
      {
         _file->Close();
      }

      long TBUrho3DFile::Size()
      {
         return _file->GetSize();
      }

      size_t TBUrho3DFile::Read(void *buf, size_t elemSize, size_t count)
      {
         size_t size = elemSize * count;
         size_t totalSize = 0;

         totalSize += _file->Read(buf, size);

         return totalSize;
      }

      TBUI::TBUI(Urho3D::Context* context) :
         Urho3D::Object(context),
         _root(0)
      {
         tb::_context = context;
      }

      TBUI::~TBUI()
      {
         TBWidgetListener::RemoveGlobalListener(this);
         tb::TBWidgetsAnimationManager::Shutdown();

         delete _root;

         tb::tb_core_shutdown();
      }

      void TBUI::RegisterObject(Urho3D::Context* context)
      {
         context->RegisterFactory<TBUI>();
      }

      void TBUI::RegisterSystem(Urho3D::Context* context)
      {
         TBUI::RegisterObject(context);

         UI::Bitmap::RegisterObject(context);
      }

      void TBUI::Init()
      {
         SetupTurboBadger();
         SubscribeToEvents();
      }

      void TBUI::AddFontInfo(const Urho3D::String& fileName, const Urho3D::String& fontName)
      {
         tb::g_font_manager->AddFontInfo(fileName.CString(), fontName.CString());
      }

      void TBUI::SetFont(const Urho3D::String& fontName, int size)
      {
         tb::TBFontDescription fd;
         fd.SetID(tb::TBID(fontName.CString()));
         fd.SetSize(tb::g_tb_skin->GetDimensionConverter()->DpToPx(12));

         tb::g_font_manager->SetDefaultFontDescription(fd);
         tb::g_font_manager->CreateFontFace(tb::g_font_manager->GetDefaultFontDescription());
      }

      void TBUI::SetRoot(tb::TBWidget* widget)
      {
         auto graphics = GetSubsystem<Urho3D::Graphics>();

         _root = widget;
         _root->SetSize(graphics->GetWidth(), graphics->GetHeight());
      }

      tb::TBWidget* TBUI::GetWidget(const Urho3D::String& name, tb::TBWidget* parent)
      {
         return parent->GetWidgetByID(tb::TBID(name.CString()));
      }

      tb::TBWidget* TBUI::LoadWidget(const Urho3D::String& fileName, tb::TBWidget* widget)
      {
         auto cache = GetSubsystem<Urho3D::ResourceCache>();

         // Load widget
         tb::TBNode node;
         if (node.ReadFile(fileName.CString()))
         {
            tb::g_widgets_reader->LoadNodeTree(widget, &node);
         }

         return widget;
      }

      void TBUI::ResizeWidgetToFitContent(tb::TBWidget* widget, tb::TBWindow::RESIZE_FIT fit)
      {
         tb::PreferredSize ps = widget->GetPreferredSize();
         int new_w = ps.pref_w;
         int new_h = ps.pref_h;
         if (fit == tb::TBWindow::RESIZE_FIT_MINIMAL)
         {
            new_w = ps.min_w;
            new_h = ps.min_h;
         }
         else if (fit == tb::TBWindow::RESIZE_FIT_CURRENT_OR_NEEDED)
         {
            new_w = tb::Clamp(widget->GetRect().w, ps.min_w, ps.max_w);
            new_h = tb::Clamp(widget->GetRect().h, ps.min_h, ps.max_h);
         }
         if (widget->GetParent())
         {
            new_w = tb::Min(new_w, widget->GetParent()->GetRect().w);
            new_h = tb::Min(new_h, widget->GetParent()->GetRect().h);
         }
         widget->SetRect(tb::TBRect(widget->GetRect().x, widget->GetRect().y, new_w, new_h));
      }

      tb::TBBitmap* TBUI::CreateBitmap(int width, int height, tb::uint32* data)
      {
         auto bitmap = new Bitmap(context_);
         bitmap->Init(width, height, data);

         return bitmap;
      }

      void TBUI::RenderBatch(Batch* batch)
      {
         if (!batch->vertex_count)
            return;

         Urho3D::Texture2D* texture = NULL;

         if (batch->bitmap)
         {
            Bitmap* tbuibitmap = (Bitmap*)batch->bitmap;
            texture = tbuibitmap->texture;
         }

         Urho3D::PODVector<float> vertexData;
         Urho3D::SharedPtr<Urho3D::VertexBuffer> vertexBuffer(new Urho3D::VertexBuffer(context_));

         Urho3D::UIBatch newBatch;
         newBatch.blendMode_ = Urho3D::BLEND_ALPHA;
         newBatch.scissor_ = _scissor;
         newBatch.texture_ = texture;
         newBatch.vertexData_ = &vertexData;
         newBatch.invTextureSize_ = (texture ? Urho3D::Vector2(1.0f / (float)texture->GetWidth(), 1.0f / (float)texture->GetHeight()) : Urho3D::Vector2::ONE);

         unsigned begin = newBatch.vertexData_->Size();
         newBatch.vertexData_->Resize(begin + batch->vertex_count * Urho3D::UI_VERTEX_SIZE);
         float* dest = &(newBatch.vertexData_->At(begin));
         newBatch.vertexEnd_ = newBatch.vertexData_->Size();

         for (int i = 0; i < batch->vertex_count; i++)
         {
            Vertex* v = &batch->vertex[i];
            dest[0] = v->x; dest[1] = v->y; dest[2] = 0.0f;
            ((unsigned&)dest[3]) = v->col;
            dest[4] = v->u; dest[5] = v->v;
            dest += Urho3D::UI_VERTEX_SIZE;
         }

         SetVertexData(vertexBuffer, vertexData);

         auto graphics = GetSubsystem<Urho3D::Graphics>();

         Urho3D::Vector2 invScreenSize(1.0f / (float)graphics->GetWidth(), 1.0f / (float)graphics->GetHeight());
         Urho3D::Vector2 scale(2.0f * invScreenSize.x_, -2.0f * invScreenSize.y_);
         Urho3D::Vector2 offset(-1.0f, 1.0f);

         Urho3D::Matrix4 projection(Urho3D::Matrix4::IDENTITY);
         projection.m00_ = scale.x_;
         projection.m03_ = offset.x_;
         projection.m11_ = scale.y_;
         projection.m13_ = offset.y_;
         projection.m22_ = 1.0f;
         projection.m23_ = 0.0f;
         projection.m33_ = 1.0f;

         graphics->ClearParameterSources();
         graphics->SetColorWrite(true);
         graphics->SetCullMode(Urho3D::CULL_NONE);
         graphics->SetDepthTest(Urho3D::CMP_ALWAYS);
         graphics->SetDepthWrite(false);
         graphics->SetFillMode(Urho3D::FILL_SOLID);
         graphics->SetStencilTest(false);

         graphics->ResetRenderTargets();

         graphics->SetVertexBuffer(vertexBuffer);

         Urho3D::ShaderVariation* noTextureVS = graphics->GetShader(Urho3D::VS, "Basic", "VERTEXCOLOR");
         Urho3D::ShaderVariation* diffTextureVS = graphics->GetShader(Urho3D::VS, "Basic", "DIFFMAP VERTEXCOLOR");
         Urho3D::ShaderVariation* noTexturePS = graphics->GetShader(Urho3D::PS, "Basic", "VERTEXCOLOR");
         Urho3D::ShaderVariation* diffTexturePS = graphics->GetShader(Urho3D::PS, "Basic", "DIFFMAP VERTEXCOLOR");
         Urho3D::ShaderVariation* diffMaskTexturePS = graphics->GetShader(Urho3D::PS, "Basic", "DIFFMAP ALPHAMASK VERTEXCOLOR");
         Urho3D::ShaderVariation* alphaTexturePS = graphics->GetShader(Urho3D::PS, "Basic", "ALPHAMAP VERTEXCOLOR");

         unsigned alphaFormat = Urho3D::Graphics::GetAlphaFormat();

         if (newBatch.vertexStart_ == newBatch.vertexEnd_)
            return;

         Urho3D::ShaderVariation* ps;
         Urho3D::ShaderVariation* vs;

         if (!newBatch.texture_)
         {
            ps = noTexturePS;
            vs = noTextureVS;
         }
         else
         {
            // If texture contains only an alpha channel, use alpha shader (for fonts)
            vs = diffTextureVS;

            if (newBatch.texture_->GetFormat() == alphaFormat)
               ps = alphaTexturePS;
            else if (newBatch.blendMode_ != Urho3D::BLEND_ALPHA && newBatch.blendMode_ != Urho3D::BLEND_ADDALPHA && newBatch.blendMode_ != Urho3D::BLEND_PREMULALPHA)
               ps = diffMaskTexturePS;
            else
               ps = diffTexturePS;
         }

         graphics->SetShaders(vs, ps);
         if (graphics->NeedParameterUpdate(Urho3D::SP_OBJECT, this))
            graphics->SetShaderParameter(Urho3D::VSP_MODEL, Urho3D::Matrix3x4::IDENTITY);
         if (graphics->NeedParameterUpdate(Urho3D::SP_CAMERA, this))
            graphics->SetShaderParameter(Urho3D::VSP_VIEWPROJ, projection);
         if (graphics->NeedParameterUpdate(Urho3D::SP_MATERIAL, this))
            graphics->SetShaderParameter(Urho3D::PSP_MATDIFFCOLOR, Urho3D::Color(1.0f, 1.0f, 1.0f, 1.0f));

         graphics->SetBlendMode(newBatch.blendMode_);
         graphics->SetScissorTest(true, newBatch.scissor_);
         graphics->SetTexture(0, newBatch.texture_);
         graphics->Draw(Urho3D::TRIANGLE_LIST, newBatch.vertexStart_ / Urho3D::UI_VERTEX_SIZE, (newBatch.vertexEnd_ - newBatch.vertexStart_) /
            Urho3D::UI_VERTEX_SIZE);
      }

      void TBUI::SetClipRect(const tb::TBRect& rect)
      {
         _scissor.top_ = rect.y;
         _scissor.left_ = rect.x;
         _scissor.bottom_ = rect.y + rect.h;
         _scissor.right_ = rect.x + rect.w;
      }

      void TBUI::SetupTurboBadger()
      {
         auto cache = GetSubsystem<Urho3D::ResourceCache>();
         auto graphics = GetSubsystem<Urho3D::Graphics>();

         tb::TBWidgetsAnimationManager::Init();
         tb::TBWidgetListener::AddGlobalListener(this);

         // Initialize Turbo Badger
         tb::tb_core_init(this);

         // Setup localization
         tb::g_tb_lng = new tb::TBLanguage;
         tb::g_tb_lng->Load("UI/Language/lng_en.tb.txt");

         // Setup font
         register_freetype_font_renderer();
         AddFontInfo("UI/vera.ttf", "Vera");
         SetFont("Vera");

         if (cache->Exists("UI/override_skin/skin.tb.txt"))
         {
            tb::g_tb_skin->Load("UI/default_skin/skin.tb.txt", "UI/override_skin/skin.tb.txt");
         }
         else
         {
            tb::g_tb_skin->Load("UI/default_skin/skin.tb.txt");
         }
      }

      void TBUI::SubscribeToEvents()
      {
         SubscribeToEvent(Urho3D::E_UPDATE, HANDLER(TBUI, HandleUpdate));
         SubscribeToEvent(Urho3D::E_ENDRENDERING, HANDLER(TBUI, HandleRenderUpdate));

         SubscribeToEvent(Urho3D::E_SCREENMODE, HANDLER(TBUI, HandleScreenMode));
         SubscribeToEvent(Urho3D::E_MOUSEBUTTONDOWN, HANDLER(TBUI, HandleMouseButtonDown));
         SubscribeToEvent(Urho3D::E_MOUSEBUTTONUP, HANDLER(TBUI, HandleMouseButtonUp));
         SubscribeToEvent(Urho3D::E_MOUSEMOVE, HANDLER(TBUI, HandleMouseMove));
         SubscribeToEvent(Urho3D::E_MOUSEWHEEL, HANDLER(TBUI, HandleMouseWheel));
         SubscribeToEvent(Urho3D::E_KEYDOWN, HANDLER(TBUI, HandleKeyDown));
         SubscribeToEvent(Urho3D::E_KEYUP, HANDLER(TBUI, HandleKeyUp));
         SubscribeToEvent(Urho3D::E_TEXTINPUT, HANDLER(TBUI, HandleTextInput));
      }

      void TBUI::SetVertexData(Urho3D::VertexBuffer* dest, const Urho3D::PODVector<float>& vertexData)
      {
         if (vertexData.Empty())
            return;

         // Update quad geometry into the vertex buffer
         // Resize the vertex buffer first if too small or much too large
         unsigned numVertices = vertexData.Size() / Urho3D::UI_VERTEX_SIZE;
         if (dest->GetVertexCount() < numVertices || dest->GetVertexCount() > numVertices * 2)
            dest->SetSize(numVertices, Urho3D::MASK_POSITION | Urho3D::MASK_COLOR | Urho3D::MASK_TEXCOORD1, true);

         dest->SetData(&vertexData[0]);
      }

      void TBUI::HandleUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
      {
         tb::TBMessageHandler::ProcessMessages();
      }

      void TBUI::HandleRenderUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
      {
         // Setup scissor
         tb::TBRect rect = _root->GetRect();
         _scissor = Urho3D::IntRect(0, 0, rect.w, rect.h);

         tb::TBAnimationManager::Update();

         // Update all widgets
         _root->InvokeProcessStates();
         _root->InvokeProcess();

         // Render UI
         tb::g_renderer->BeginPaint(rect.w, rect.h);

         _root->InvokePaint(tb::TBWidget::PaintProps());
         
         tb::g_renderer->EndPaint();

         //_root->Invalidate();
      }

      void TBUI::HandleScreenMode(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
      {
         using namespace Urho3D::ScreenMode;

         int width = eventData[P_WIDTH].GetInt();
         int height = eventData[P_HEIGHT].GetInt();

         _root->SetSize(width, height);
      }

      void TBUI::HandleMouseButtonDown(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
      {
         using namespace Urho3D::MouseButtonDown;

         unsigned button = eventData[P_BUTTON].GetUInt();
         unsigned qualifiers = eventData[P_QUALIFIERS].GetUInt();

         auto input = GetSubsystem<Urho3D::Input>();
         auto mousePosition = input->GetMousePosition();

         tb::MODIFIER_KEYS modifiers = tb::TB_MODIFIER_NONE;
         if (qualifiers & Urho3D::QUAL_CTRL)
            modifiers |= tb::TB_CTRL;
         if (qualifiers & Urho3D::QUAL_SHIFT)
            modifiers |= tb::TB_SHIFT;
         if (qualifiers & Urho3D::QUAL_ALT)
            modifiers |= tb::TB_ALT;

         switch (button)
         {
         case Urho3D::MOUSEB_LEFT:
            _root->InvokePointerDown(mousePosition.x_, mousePosition.y_, 1, modifiers, false);
            break;
         }

      }

      void TBUI::HandleMouseButtonUp(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
      {
         using namespace Urho3D::MouseButtonUp;

         unsigned button = eventData[P_BUTTON].GetUInt();
         unsigned qualifiers = eventData[P_QUALIFIERS].GetUInt();

         auto input = GetSubsystem<Urho3D::Input>();
         auto mousePosition = input->GetMousePosition();

         tb::MODIFIER_KEYS modifiers = tb::TB_MODIFIER_NONE;
         if (qualifiers & Urho3D::QUAL_CTRL)
            modifiers |= tb::TB_CTRL;
         if (qualifiers & Urho3D::QUAL_SHIFT)
            modifiers |= tb::TB_SHIFT;
         if (qualifiers & Urho3D::QUAL_ALT)
            modifiers |= tb::TB_ALT;

         switch (button)
         {
         case Urho3D::MOUSEB_LEFT:
            _root->InvokePointerUp(mousePosition.x_, mousePosition.y_, modifiers, false);
            break;
         case Urho3D::MOUSEB_RIGHT:
            _root->InvokeEvent(tb::TBWidgetEvent(tb::EVENT_TYPE_CONTEXT_MENU, mousePosition.x_, mousePosition.y_, false, modifiers));
            break;
         }
      }

      void TBUI::HandleMouseMove(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
      {
         using namespace Urho3D::MouseMove;

         int x = eventData[P_X].GetInt();
         int y = eventData[P_Y].GetInt();

         _root->InvokeEvent(tb::TBWidgetEvent(tb::EVENT_TYPE_POINTER_MOVE, x, y, false));
      }

      void TBUI::HandleMouseWheel(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
      {
         using namespace Urho3D::MouseWheel;

         int wheel = eventData[P_WHEEL].GetInt();
         unsigned qualifiers = eventData[P_QUALIFIERS].GetInt();

         auto input = GetSubsystem<Urho3D::Input>();
         auto mousePosition = input->GetMousePosition();

         tb::MODIFIER_KEYS modifiers = tb::TB_MODIFIER_NONE;
         if (qualifiers & Urho3D::QUAL_CTRL)
            modifiers |= tb::TB_CTRL;
         if (qualifiers & Urho3D::QUAL_SHIFT)
            modifiers |= tb::TB_SHIFT;
         if (qualifiers & Urho3D::QUAL_ALT)
            modifiers |= tb::TB_ALT;

         _root->InvokeWheel(mousePosition.x_, mousePosition.y_, 0, -wheel, tb::TB_MODIFIER_NONE);
      }

      void TBUI::HandleKeyDown(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
      {
         using namespace Urho3D::KeyDown;

         int key = eventData[P_KEY].GetInt();
         unsigned qualifiers = eventData[P_QUALIFIERS].GetUInt();

         auto input = GetSubsystem<Urho3D::Input>();
         auto mousePosition = input->GetMousePosition();

         tb::MODIFIER_KEYS modifiers = tb::TB_MODIFIER_NONE;
         if (qualifiers & Urho3D::QUAL_CTRL)
            modifiers |= tb::TB_CTRL;
         if (qualifiers & Urho3D::QUAL_SHIFT)
            modifiers |= tb::TB_SHIFT;
         if (qualifiers & Urho3D::QUAL_ALT)
            modifiers |= tb::TB_ALT;

         switch (key)
         {
         case Urho3D::KEY_RETURN:
         case Urho3D::KEY_RETURN2:
         case Urho3D::KEY_KP_ENTER:
            _root->InvokeKey(0, tb::TB_KEY_ENTER, modifiers, true);
            break;
         case Urho3D::KEY_F1:
            _root->InvokeKey(0, tb::TB_KEY_F1, modifiers, true);
            break;
         case Urho3D::KEY_F2:
            _root->InvokeKey(0, tb::TB_KEY_F2, modifiers, true);
            break;
         case Urho3D::KEY_F3:
            _root->InvokeKey(0, tb::TB_KEY_F3, modifiers, true);
            break;
         case Urho3D::KEY_F4:
            _root->InvokeKey(0, tb::TB_KEY_F4, modifiers, true);
            break;
         case Urho3D::KEY_F5:
            _root->InvokeKey(0, tb::TB_KEY_F5, modifiers, true);
            break;
         case Urho3D::KEY_F6:
            _root->InvokeKey(0, tb::TB_KEY_F6, modifiers, true);
            break;
         case Urho3D::KEY_F7:
            _root->InvokeKey(0, tb::TB_KEY_F7, modifiers, true);
            break;
         case Urho3D::KEY_F8:
            _root->InvokeKey(0, tb::TB_KEY_F8, modifiers, true);
            break;
         case Urho3D::KEY_F9:
            _root->InvokeKey(0, tb::TB_KEY_F9, modifiers, true);
            break;
         case Urho3D::KEY_F10:
            _root->InvokeKey(0, tb::TB_KEY_F10, modifiers, true);
            break;
         case Urho3D::KEY_F11:
            _root->InvokeKey(0, tb::TB_KEY_F11, modifiers, true);
            break;
         case Urho3D::KEY_F12:
            _root->InvokeKey(0, tb::TB_KEY_F12, modifiers, true);
            break;
         case Urho3D::KEY_LEFT:
            _root->InvokeKey(0, tb::TB_KEY_LEFT, modifiers, true);
            break;
         case Urho3D::KEY_UP:
            _root->InvokeKey(0, tb::TB_KEY_UP, modifiers, true);
            break;
         case Urho3D::KEY_RIGHT:
            _root->InvokeKey(0, tb::TB_KEY_RIGHT, modifiers, true);
            break;
         case Urho3D::KEY_DOWN:
            _root->InvokeKey(0, tb::TB_KEY_DOWN, modifiers, true);
            break;
         case Urho3D::KEY_PAGEUP:
            _root->InvokeKey(0, tb::TB_KEY_PAGE_UP, modifiers, true);
            break;
         case Urho3D::KEY_PAGEDOWN:
            _root->InvokeKey(0, tb::TB_KEY_PAGE_DOWN, modifiers, true);
            break;
         case Urho3D::KEY_HOME:
            _root->InvokeKey(0, tb::TB_KEY_HOME, modifiers, true);
            break;
         case Urho3D::KEY_END:
            _root->InvokeKey(0, tb::TB_KEY_END, modifiers, true);
            break;
         case Urho3D::KEY_INSERT:
            _root->InvokeKey(0, tb::TB_KEY_INSERT, modifiers, true);
            break;
         case Urho3D::KEY_TAB:
            _root->InvokeKey(0, tb::TB_KEY_TAB, modifiers, true);
            break;
         case Urho3D::KEY_DELETE:
            _root->InvokeKey(0, tb::TB_KEY_DELETE, modifiers, true);
            break;
         case Urho3D::KEY_BACKSPACE:
            _root->InvokeKey(0, tb::TB_KEY_BACKSPACE, modifiers, true);
            break;
         case Urho3D::KEY_ESC:
            _root->InvokeKey(0, tb::TB_KEY_ESC, modifiers, true);
            break;
         default:
            if (modifiers & tb::TB_SUPER)
               _root->InvokeKey(key, tb::TB_KEY_UNDEFINED, modifiers, true);
         }
      }

      void TBUI::HandleKeyUp(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
      {
         using namespace Urho3D::KeyUp;

         int key = eventData[P_KEY].GetInt();
         unsigned qualifiers = eventData[P_QUALIFIERS].GetUInt();

         auto input = GetSubsystem<Urho3D::Input>();
         auto mousePosition = input->GetMousePosition();

         tb::MODIFIER_KEYS modifiers = tb::TB_MODIFIER_NONE;
         if (qualifiers & Urho3D::QUAL_CTRL)
            modifiers |= tb::TB_CTRL;
         if (qualifiers & Urho3D::QUAL_SHIFT)
            modifiers |= tb::TB_SHIFT;
         if (qualifiers & Urho3D::QUAL_ALT)
            modifiers |= tb::TB_ALT;

         switch (key)
         {
         case Urho3D::KEY_RETURN:
         case Urho3D::KEY_RETURN2:
         case Urho3D::KEY_KP_ENTER:
            _root->InvokeKey(0, tb::TB_KEY_ENTER, modifiers, false);
            break;
         case Urho3D::KEY_F1:
            _root->InvokeKey(0, tb::TB_KEY_F1, modifiers, false);
            break;
         case Urho3D::KEY_F2:
            _root->InvokeKey(0, tb::TB_KEY_F2, modifiers, false);
            break;
         case Urho3D::KEY_F3:
            _root->InvokeKey(0, tb::TB_KEY_F3, modifiers, false);
            break;
         case Urho3D::KEY_F4:
            _root->InvokeKey(0, tb::TB_KEY_F4, modifiers, false);
            break;
         case Urho3D::KEY_F5:
            _root->InvokeKey(0, tb::TB_KEY_F5, modifiers, false);
            break;
         case Urho3D::KEY_F6:
            _root->InvokeKey(0, tb::TB_KEY_F6, modifiers, false);
            break;
         case Urho3D::KEY_F7:
            _root->InvokeKey(0, tb::TB_KEY_F7, modifiers, false);
            break;
         case Urho3D::KEY_F8:
            _root->InvokeKey(0, tb::TB_KEY_F8, modifiers, false);
            break;
         case Urho3D::KEY_F9:
            _root->InvokeKey(0, tb::TB_KEY_F9, modifiers, false);
            break;
         case Urho3D::KEY_F10:
            _root->InvokeKey(0, tb::TB_KEY_F10, modifiers, false);
            break;
         case Urho3D::KEY_F11:
            _root->InvokeKey(0, tb::TB_KEY_F11, modifiers, false);
            break;
         case Urho3D::KEY_F12:
            _root->InvokeKey(0, tb::TB_KEY_F12, modifiers, false);
            break;
         case Urho3D::KEY_LEFT:
            _root->InvokeKey(0, tb::TB_KEY_LEFT, modifiers, false);
            break;
         case Urho3D::KEY_UP:
            _root->InvokeKey(0, tb::TB_KEY_UP, modifiers, false);
            break;
         case Urho3D::KEY_RIGHT:
            _root->InvokeKey(0, tb::TB_KEY_RIGHT, modifiers, false);
            break;
         case Urho3D::KEY_DOWN:
            _root->InvokeKey(0, tb::TB_KEY_DOWN, modifiers, false);
            break;
         case Urho3D::KEY_PAGEUP:
            _root->InvokeKey(0, tb::TB_KEY_PAGE_UP, modifiers, false);
            break;
         case Urho3D::KEY_PAGEDOWN:
            _root->InvokeKey(0, tb::TB_KEY_PAGE_DOWN, modifiers, false);
            break;
         case Urho3D::KEY_HOME:
            _root->InvokeKey(0, tb::TB_KEY_HOME, modifiers, false);
            break;
         case Urho3D::KEY_END:
            _root->InvokeKey(0, tb::TB_KEY_END, modifiers, false);
            break;
         case Urho3D::KEY_INSERT:
            _root->InvokeKey(0, tb::TB_KEY_INSERT, modifiers, false);
            break;
         case Urho3D::KEY_TAB:
            _root->InvokeKey(0, tb::TB_KEY_TAB, modifiers, false);
            break;
         case Urho3D::KEY_DELETE:
            _root->InvokeKey(0, tb::TB_KEY_DELETE, modifiers, false);
            break;
         case Urho3D::KEY_BACKSPACE:
            _root->InvokeKey(0, tb::TB_KEY_BACKSPACE, modifiers, false);
            break;
         case Urho3D::KEY_ESC:
            _root->InvokeKey(0, tb::TB_KEY_ESC, modifiers, false);
            break;
         default:
            if (modifiers & tb::TB_SUPER)
               _root->InvokeKey(key, tb::TB_KEY_UNDEFINED, modifiers, false);
         }
      }

      void TBUI::HandleTextInput(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
      {
         using namespace Urho3D::TextInput;

         auto text = eventData[P_TEXT].GetString();

         for (unsigned i = 0; i < text.Length(); i++)
         {
            _root->InvokeKey(text[i], tb::TB_KEY_UNDEFINED, tb::TB_MODIFIER_NONE, true);
            _root->InvokeKey(text[i], tb::TB_KEY_UNDEFINED, tb::TB_MODIFIER_NONE, false);
         }
      }
   }
}
[/code]

To setup the subsystem:
[code]
// Setup Turbo Badger UI
UI::TBUI::RegisterSystem(_context);
_context->RegisterSubsystem(new UI::TBUI(_context));
_context->GetSubsystem<UI::TBUI>()->Init();
[/code]

Adding an editor control that expands the entire window is easy:
[code]
_editorUI = ui->LoadWidget<tb::TBWidget>("UI/ui_resources/editor_tab_content.tb.txt");
ui->SetRoot(_editorUI);
[/code]
[/quote]

-------------------------

djmig | 2017-01-02 01:14:19 UTC | #17

Hi,
Turbo Badger looks great and I want to use it as the UI for my application. So, a few minutes ago 
I git clone Turbo Badger from Github and followed the instruction to clone GLFW as a submodule. All went well including its compilation, but unfortunately TurboBadgerDemo appear as an image cornered to the lower left side of the window.

[img]https://i.imgsafe.org/2fbf8b3424.png[/img]

BTW, I'm on OS X El Capitan.

Don.

-------------------------

sabotage3d | 2017-01-02 01:14:19 UTC | #18

Hey guys it seems that GetSubsystem<Input>()->SetTouchEmulation(true) is blocking the mouse events from Turbo Badger. Is there anyway around this?

-------------------------

jmiller | 2017-01-02 01:14:20 UTC | #19

[quote="djmig"]unfortunately TurboBadgerDemo appear as an image cornered to the lower left side of the window.[/quote]

I have not seen that yet... If this is just with TB's own demo, maybe there is some issue there? [github.com/fruxo/turbobadger/issues](https://github.com/fruxo/turbobadger/issues)


[quote="sabotage3d"]Hey guys it seems that GetSubsystem<Input>()->SetTouchEmulation(true) is blocking the mouse events from Turbo Badger. Is there anyway around this?[/quote]

Urho ([b]rokups[/b]) recently added some events that allow us to hook the raw events and consume them. I have not yet worked this into the tb_Urho3D implementation, so if anyone has a good way to suggest, that's welcome.
[code]
E_INPUTBEGIN : input handling starts.
E_INPUTEND : input handling ends.
E_SDLRAWINPUT
    URHO3D_PARAM(P_SDL_EVENT, SdlEvent);           // SDL_Event*
    URHO3D_PARAM(P_CONSUMED, Consumed);            // bool
[/code]
[github.com/urho3d/Urho3D/blob/a ... nts.h#L224](https://github.com/urho3d/Urho3D/blob/a44c0a7a43e9b3e344aff50f8c13469d8ec8a98c/Source/Urho3D/Input/InputEvents.h#L224)

-------------------------

cadaver | 2017-01-02 01:14:20 UTC | #20

In touch emulation mode mouse events are intentionally not sent, so that you can see the effect of only touch events and not get them mixed. Touch events should be hooked to TB too to make it work correctly with touch.

-------------------------

Dave82 | 2017-01-02 01:14:20 UTC | #21

I think this is great and a really good implementation however i would rather see a version that is more urho compatible.Instead of implementing it as an external subsystem why not wrap it like the other libraries ? So the default Urho3D::UI should use TurboBadger ? Im not familiar with TurboBadger but i think it would be even possible to add some CMake configuration to build Urho3d with the default UI or with TurboBadger.
So this way :
1 will work out of box (at some point) 
2 the Urho3D Editor would work with TurboBadger widgets without any major code modifications
3 Without code modifications it is automatically exposed to Scripts too.

-------------------------

cadaver | 2017-01-02 01:14:20 UTC | #22

I don't think you can reasonably expect to code to the same API if you switch the underlying UI library, except by simplifying a lot, and that wouldn't benefit the good parts of either UI library.

This has been discussed before and I do think the ideal would be for the UI library to be wrapped so that you use e.g. Urho events and Urho resources instead of the UI library's native ones. However in practice it's a very difficult ideal, since either you have a lot of wrapping/adaptation work to do, or lose features. Compare to Bullet: Urho's physics components don't expose Bullet nearly completely so for a physics power user using Bullet directly could actually make more sense.

-------------------------

Dave82 | 2017-01-02 01:14:22 UTC | #23

[quote]I don't think you can reasonably expect to code to the same API if you switch the underlying UI library, except by simplifying a lot, and that wouldn't benefit the good parts of either UI library.[/quote]

Yes , these are the modifications i mention , but yes this would require a lot lot work ,when probably after TurboBadger integration the default UI would be obsolete anyway.So maybe it would be better just switching to TurboBadger as the UI (by using the existing UI unterface and expanding it).Maybe it worth a new branch for testing this.


[quote]This has been discussed before and I do think the ideal would be for the UI library to be wrapped so that you use e.g. Urho events and Urho resources instead of the UI library's native ones. However in practice it's a very difficult ideal, since either you have a lot of wrapping/adaptation work to do, or lose features. Compare to Bullet: Urho's physics components don't expose Bullet nearly completely so for a physics power user using Bullet directly could actually make more sense.[/quote]

Well i would rather lose features than using api's directly.Thats the main reason i like Urho3d.It's clear and easily understandable interface.Once you learned the coding workflow you don't need extra tutorials to get into other features.By using apis directly you always have to learn the new library first...Which isn't really attractive for new users

here's a screen shot of my modified gui skin.I added some shadows , highlights to buttons and switched to monochrome style.I think it is more pleasant for the eyes than the deafult blue style.
[img]http://s20.postimg.org/uwx8jsfcd/editor_shot.jpg[/img]

-------------------------

