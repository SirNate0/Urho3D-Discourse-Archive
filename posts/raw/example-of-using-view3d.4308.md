x6herbius | 2018-06-11 19:37:16 UTC | #1

I'd like to create a view layout in my main window with 4 viewports (similar to CAD programs). I've managed to do this by manually giving the default window renderer 4 viewports and sizing them appropriately, but I have noticed that there's a `View3D` UI element that can supposedly render a scene. However, when I try to use this, nothing gets drawn to the screen.

```
void CalliperApplication::Start()
{
	Urho3D::ResourceCache* cache = GetSubsystem<Urho3D::ResourceCache>();
	Urho3D::Graphics* graphics = GetSubsystem<Urho3D::Graphics>();
	Urho3D::UI* ui = GetSubsystem<Urho3D::UI>();

	graphicsWidth_ = graphics->GetWidth();
	graphicsHeight_ = graphics->GetHeight();

	ui->GetRoot()->SetDefaultStyle(cache->GetResource<Urho3D::XMLFile>("UI/DefaultStyle.xml"));

	sampleScene_ = new SampleScene(context_);
	sampleScene_->Initialise();

	// Old code - draws 4 viewports on screen:
	/*Urho3D::Renderer* renderer = GetSubsystem<Urho3D::Renderer>();
	renderer->SetNumViewports(4);

	for ( uint32_t viewportIndex = 0; viewportIndex < 4; ++viewportIndex )
	{
		Urho3D::SharedPtr<Urho3D::Camera> camera = sampleScene_->cameras_[viewportIndex];
		Urho3D::SharedPtr<Urho3D::Viewport> viewport(new Urho3D::Viewport(context_ , sampleScene_->scene_, camera, RectForViewport(viewportIndex)));
		renderer->SetViewport(viewportIndex, viewport);
	}*/

	// New code - everything is black:
	Urho3D::SharedPtr<Urho3D::View3D> view(new Urho3D::View3D(context_));
	view->SetView(sampleScene_->scene_, sampleScene_->cameras_[0], false);
	ui->GetRoot()->AddChild(view);

	SubscribeToEvent(Urho3D::E_BEGINFRAME, URHO3D_HANDLER(CalliperApplication, HandleBeginFrame));
	SubscribeToEvent(Urho3D::E_ENDFRAME, URHO3D_HANDLER(CalliperApplication, HandleEndFrame));
	SubscribeToEvent(Urho3D::E_KEYDOWN, URHO3D_HANDLER(CalliperApplication, HandleKeyDown));
	SubscribeToEvent(Urho3D::E_UPDATE, URHO3D_HANDLER(CalliperApplication, HandleUpdate));
	SubscribeToEvent(Urho3D::E_SCREENMODE, URHO3D_HANDLER(CalliperApplication, HandleScreenModeChanged));
}
```

I may be using the `View3D` in the wrong way, I'm not sure. Are there any examples of how it's supposed to be set up?

-------------------------

lezak | 2018-06-12 09:55:10 UTC | #2

From this code, it looks like You're not setting the size of Your View3D. 
View3D element is used several times in the editor, take a look at EditorMaterial.as, EditorParticleEffect.as or EditorResourceBrowser.as - You can find there examples of setting it up (it's script, but it's almost the same in c++).
You may also want to go through the EditorView.as - there are implementations of multiple viewports layouts (but it doesn't use View3D).

-------------------------

x6herbius | 2018-06-12 12:33:09 UTC | #3

Awesome, setting width and height seemed to work! I'd only been searching through C++ files so I hadn't realised there were `View3D`s in script files.

-------------------------

