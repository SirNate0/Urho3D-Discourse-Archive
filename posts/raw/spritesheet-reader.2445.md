sabotage3d | 2017-01-02 01:15:25 UTC | #1

Hi,

Based on SpriteSheet2D class in Urho3D. I have made this simple SpriteSheet Reader where you can query the offsets in different formats. Credits for animating the spritesheets to 1vanK and ghidra.
The format is compatable with Leshy SpriteSheet Tool: [url]https://www.leshylabs.com/apps/sstool/[/url]. This is an example spritesheet for testing where you can generate the offsets using Leshy's tool:[url]http://i.imgur.com/HRuK0iD.png[/url].


[b]SpriteSheet.h[/b]
[code]//
// Copyright (c) 2008-2016 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

#pragma once


#include <Urho3D/Resource/Resource.h>

namespace Urho3D
{

class Texture2D;
class XMLFile;

/// Sprite sheet.
class URHO3D_API SpriteSheet : public Resource
{
    URHO3D_OBJECT(SpriteSheet, Resource);

public:
    /// Construct.
    SpriteSheet(Context* context);
    /// Destruct.
    virtual ~SpriteSheet();
    /// Register object factory.
    static void RegisterObject(Context* context);

    /// Load resource from stream. May be called from a worker thread. Return true if successful.
    virtual bool BeginLoad(Deserializer& source);
    /// Finish resource loading. Always called from the main thread. Return true if successful.
    virtual bool EndLoad();

    /// Set texture.
    void SetTexture(Texture2D* texture);

    /// Return texture.
    Texture2D* GetTexture() const { return texture_; }

    /// Return offsets at index
    const IntVector2& GetOffset(int index) const { return offsets_.At(index); }
    const IntRect& GetRectangle(int index) const { return rectangles_.At(index); }
    const Rect& GetTextureRectangle(int index) const { return textureRectangles_.At(index); }
    unsigned GetOffsetsCount() const { return offsetsCount_; }

private:
    /// Begin load from XML file.
    bool BeginLoadFromXMLFile(Deserializer& source);
    /// End load from XML file.
    bool EndLoadFromXMLFile();

    /// Texture.
    SharedPtr<Texture2D> texture_;
    /// Sprite mapping.
    HashMap<String, SharedPtr<Sprite2D> > spriteMapping_;
    /// XML file used while loading.
    SharedPtr<XMLFile> loadXMLFile_;
    /// Texture name used while loading.
    String loadTextureName_;

    /// Cache
    void CacheOffsets(int x, int y, int width, int height);

    PODVector<IntVector2> offsets_;
    PODVector<IntRect> rectangles_;
    PODVector<Rect> textureRectangles_;

    unsigned offsetsCount_;

};

}[/code]

[b]SpriteSheet.cpp[/b]
[code]//
// Copyright (c) 2008-2016 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//



#include <Urho3D/Core/Context.h>
#include <Urho3D/Graphics/Texture2D.h>
#include <Urho3D/IO/Deserializer.h>
#include <Urho3D/IO/FileSystem.h>
#include <Urho3D/IO/Log.h>
#include <Urho3D/Resource/PListFile.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Resource/XMLFile.h>
#include <Urho3D/Resource/JSONFile.h>
#include <Urho3D/Urho2D/Sprite2D.h>

#include "SpriteSheet.h"


using namespace std;

namespace Urho3D
{

SpriteSheet::SpriteSheet(Context* context) :
    Resource(context),
    offsetsCount_(0)
{
}

SpriteSheet::~SpriteSheet()
{
}

void SpriteSheet::RegisterObject(Context* context)
{
    context->RegisterFactory<SpriteSheet>();
}

bool SpriteSheet::BeginLoad(Deserializer& source)
{
    if (GetName().Empty())
        SetName(source.GetName());

    loadTextureName_.Clear();
    spriteMapping_.Clear();

    /// clear cache
    offsets_.Clear();
    rectangles_.Clear();
    textureRectangles_.Clear();


    String extension = GetExtension(source.GetName());

    if (extension == ".xml")
        return BeginLoadFromXMLFile(source);

    URHO3D_LOGERROR("Unsupported file type");
    return false;
}

bool SpriteSheet::EndLoad()
{

    if (loadXMLFile_)
        return EndLoadFromXMLFile();


    return false;
}

void SpriteSheet::SetTexture(Texture2D* texture)
{
    loadTextureName_.Clear();
    texture_ = texture;

}


/// Cache
void SpriteSheet::CacheOffsets(int x, int y, int width, int height)
{

    /// Cache offsets
    offsets_.Push(IntVector2(x,y));

    IntRect rectangle(x, y, (x + width), (y + height));

    /// Cache rectangles
    rectangles_.Push(rectangle);

    int textureWidth = texture_->GetWidth();
    int textureHeight = texture_->GetHeight();
    float invWidth = 1.0f / textureWidth;
    float invHeight = 1.0f / textureHeight;

    Rect rect;
    rect.min_.x_ = ((float)rectangle.left_) * invWidth;
    rect.max_.x_ = ((float)rectangle.right_) * invWidth;

    rect.min_.y_ = ((float)rectangle.bottom_) * invHeight;
    rect.max_.y_ = ((float)rectangle.top_) * invHeight;

    /// Cache texture rectangles
    textureRectangles_.Push(rect);


}


bool SpriteSheet::BeginLoadFromXMLFile(Deserializer& source)
{
    loadXMLFile_ = new XMLFile(context_);
    if (!loadXMLFile_->Load(source))
    {
        URHO3D_LOGERROR("Could not load sprite sheet");
        loadXMLFile_.Reset();
        return false;
    }

    SetMemoryUse(source.GetSize());

    XMLElement rootElem = loadXMLFile_->GetRoot("textureatlas");
    if (!rootElem)
    {
        URHO3D_LOGERROR("Invalid sprite sheet");
        loadXMLFile_.Reset();
        return false;
    }

    // If we're async loading, request the texture now. Finish during EndLoad().
    loadTextureName_ = GetParentPath(GetName()) + rootElem.GetAttribute("imagepath");
    if (GetAsyncLoadState() == ASYNC_LOADING)
        GetSubsystem<ResourceCache>()->BackgroundLoadResource<Texture2D>(loadTextureName_, true, this);

    return true;
}

bool SpriteSheet::EndLoadFromXMLFile()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    texture_ = cache->GetResource<Texture2D>(loadTextureName_);
    if (!texture_)
    {
        URHO3D_LOGERROR("Could not load texture " + loadTextureName_);
        loadXMLFile_.Reset();
        loadTextureName_.Clear();
        return false;
    }

    XMLElement rootElem = loadXMLFile_->GetRoot("textureatlas");
    XMLElement subTextureElem = rootElem.GetChild("subtexture");

    while (subTextureElem)
    {
        String name = subTextureElem.GetAttribute("name");

        int x = subTextureElem.GetInt("x");
        int y = subTextureElem.GetInt("y");

        int width = subTextureElem.GetInt("width");
        int height = subTextureElem.GetInt("height");

        /// Cache offsets
        CacheOffsets(x, y, width, height);

        subTextureElem = subTextureElem.GetNext("subtexture");
    }

    offsetsCount_ = offsets_.Size();

    loadXMLFile_.Reset();
    loadTextureName_.Clear();
    return true;
}



}
[/code]


Register the class.
[code]context_->RegisterFactory<SpriteSheet>();[/code]

Basic usage.
[code]void App::Init()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    spritesheet_ = cache->GetResource<SpriteSheet>("Particles/text.xml");
}

void App::Update(float timeStep)
{
     Time* time_ = GetSubsystem<Time>();
     float elapsedTime = time_->GetElapsedTime();
     float fps = 30.0;
     float frames = spritesheet->GetOffsetsCount();
     float frame = std::fmod(std::floor((elapsedTime*fps)),frames);

     const IntRect& rect = spritesheet->GetRectangle(frame);
     sprite_->SetRectangle(rect);
}
[/code]

-------------------------

Lumak | 2017-01-02 01:15:26 UTC | #2

Thanks for this!

-------------------------

dakilla | 2017-01-02 01:15:26 UTC | #3

thanks, it may be usefull later for my particles works.

-------------------------

