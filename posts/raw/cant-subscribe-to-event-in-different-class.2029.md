nairdap | 2017-01-02 01:12:24 UTC | #1

My project looks like this:

I have a MainApplication:
[code]...

URHO3D_DEFINE_APPLICATION_MAIN(MainProcessor)

MainProcessor::MainProcessor(Context* context) :
	Base(context)
{
	// Set up MainProcessor
}
...[/code]

a custom scene class:
[code]...

namespace Urho3D
{
	class Node;
	class Scene;
	class Sprite;
}

using namespace Urho3D;

class CustomScene {
public:
	CustomScene(SharedPtr<Scene> scene, ResourceCache* cache, KinectProcessor* kinectProcessor, SharedPtr<Urho3D::Image> chromaKeyImage) {
		scene_ = scene;
		cache_ = cache;
		// Set up the rest
	};

protected:
	SharedPtr<Scene> scene_;
	SharedPtr<ResourceCache> cache_;
	KinectProcessor* kinectProcessor_;
	SharedPtr<Material> backgroundMaterial_;
	SharedPtr<Urho3D::Image> chromaKeyImage_;
};
...[/code]

and a custom scene:
[code]...

namespace Urho3D
{
	class Node;
	class Scene;
}

using namespace Urho3D;

class UnderwaterScene : public CustomScene {
public:
	UnderwaterScene(SharedPtr<Scene> scene, ResourceCache* cache, KinectProcessor* kinectProcessor, SharedPtr<Urho3D::Image> chromaKeyImage)
		: CustomScene(scene, cache, kinectProcessor, chromaKeyImage)
	{
		// Set up custom scene
        scene_->SubscribeToEvent(E_ANIMATIONFINISHED, URHO3D_HANDLER(UnderwaterScene, HandleAnimationFinished));
	};

       void HandleAnimationFinished(StringHash eventType, VariantMap& eventData)
   {
      // Do stuff
   }

...[/code]

Problem is, I can't subscribe to events using SubscribeToEvent() in the UnderwaterScene class. I get the following errors:

[quote]Severity    Code    Description    Project    File    Line    Suppression State
Error    C2664    'Urho3D::EventHandlerImpl<UnderwaterScene>::EventHandlerImpl(Urho3D::EventHandlerImpl<UnderwaterScene> &&)': cannot convert argument 1 from 'void (__cdecl UnderwaterScene::* const )(Urho3D::StringHash,Urho3D::VariantMap &)' to 'UnderwaterScene *'    ChromaProject    c:\urho3d\build\include\urho3d\Core\Object.h    319[/quote]
and
[quote]
Severity    Code    Description    Project    File    Line    Suppression State
Error    C2440    'static_cast': cannot convert from 'Urho3D::Object ?*const ' to 'UnderwaterScene *?'    ChromaProject    c:\urho3d\build\include\urho3d\Core\Object.h    319[/quote]

What am I doing wrong?

-------------------------

cadaver | 2017-01-02 01:12:24 UTC | #2

You must inherit Object to send & receive events.

-------------------------

