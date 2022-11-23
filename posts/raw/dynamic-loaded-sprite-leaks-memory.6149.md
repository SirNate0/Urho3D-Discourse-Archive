Kimichura | 2020-05-09 12:59:22 UTC | #1

Hi there,

i was trying out Urho3D and tried to render some Sprites. I get the sprites from a file and change colors at runtime which is the reason why i think need MemoryBuffer to load them as Sprite2D.

My problem is, that my program somehow leaks memory. I checked it with Visual Studio and it shows me that i have an increasing number of Urho3D::Texture2D and Urho3D::Material objects (Texture2D is referenced by Material). Those Material objects are created through 'SetSprite' and as it seems they are never deleted (event though I think they should, since I remove all created Nodes from the Scene)

Am I doing something wrong here?

Below is the code I used, that's the content of my Scene Update function (E_SCENEUPDATE event):

    using namespace Urho3D;
    Urho3D::ResourceCache* cache = GetSubsystem<Urho3D::ResourceCache>();

    // Get a image (m_registry -> custom class that loads images from a file and changes some colors)
    ImageData img_data = m_registry.get_image(20, 6, { 255, (uint8_t)Random(255), (uint8_t)Random(255), (uint8_t)Random(255) });
    // Convert it to png data
    std::vector<uint8_t> img_as_png = m_registry.get_image_as_png(img_data);

    // Create a Urho3D::Sprite2D out of the image
    SharedPtr<Sprite2D> sprite = SharedPtr<Sprite2D>(new Sprite2D(context_));
    Urho3D::MemoryBuffer buffer(img_as_png.data(), img_as_png.size());
    sprite->Load(buffer);

    // Create a node and set the sprite
    SharedPtr<Node> spriteNode(scene_->CreateChild("StaticSprite2D", Urho3D::LOCAL));
    spriteNode->SetPosition(Urho3D::Vector3(0, 0, 0));

    StaticSprite2D* staticSprite = spriteNode->CreateComponent<StaticSprite2D>(Urho3D::LOCAL);
    staticSprite->SetSprite(sprite);

    // This should clear all things up - but it doesn't.
    scene_->RemoveChild(spriteNode);
    GetSubsystem<ResourceCache>()->ReleaseAllResources(true);
Allocation call stack from one of the 'surviving' Material objects:
![grafik|360x105](upload://jxzltahtPCa11vTbYWoiqS7Id1i.png) 
thanks in advance

-------------------------

Lys0gen | 2020-05-09 22:02:39 UTC | #2

Haven't tried this myself so there might be an error somewhere else - but any chance you might still have those SharedPtrs in scope/saved somewhere else, so they aren't actually destroyed?

-------------------------

Kimichura | 2020-05-09 22:29:48 UTC | #3

I don't think so since that's exactly the code I used (that's the whole function - no other code there).
The only thing I used from outside that function scope is the scene_ where the Node is added and removed.

-------------------------

Eugene | 2020-05-10 23:50:56 UTC | #4

Here is the "leak".
It's possible to make the cache more smart by using WeakPtr-s instead.
https://github.com/urho3d/Urho3D/blob/97b09f848b9388c0b3cd116906cc0ab3b442ded0/Source/Urho3D/Urho2D/Renderer2D.h#L130-L133

-------------------------

Kimichura | 2020-05-11 10:53:10 UTC | #5

Thank you very much the cache was indeed my problem. Clearing it solves my memory issue.

But I don't know how I would get it to work with WeakPtrs because the Material is created inside of GetMaterial and would be freed immediately (it would have to return a SharedPtr instead of a raw ptr to keep it alive?) [https://github.com/urho3d/Urho3D/blob/97b09f848b9388c0b3cd116906cc0ab3b442ded0/Source/Urho3D/Urho2D/Renderer2D.cpp#L251-L253](https://github.com/urho3d/Urho3D/blob/97b09f848b9388c0b3cd116906cc0ab3b442ded0/Source/Urho3D/Urho2D/Renderer2D.cpp#L251-L253)

But I got a workaround for me by removing the texture from the 'cachedMaterials_' manually, it's not pretty (i guess?) but I think it'll work out for my small project.

    void Renderer2D::UncacheTexture(Texture2D* texture)
    {
    	if (!texture)
    		return;

    	HashMap<Texture2D*, HashMap<int, SharedPtr<Material> > >::Iterator t = cachedMaterials_.Find(texture);
    	if (t != cachedMaterials_.End())
    	{
    		cachedMaterials_.Erase(t);
    	}
    }

-------------------------

Eugene | 2020-05-11 08:07:10 UTC | #6

[quote="Kimichura, post:5, topic:6149"]
it would have to return a SharedPtr instead of a raw ptr to keep it alive?
[/quote]
Yes, it would. That’s it. If you ever want proper solution, you know where to go.

-------------------------

