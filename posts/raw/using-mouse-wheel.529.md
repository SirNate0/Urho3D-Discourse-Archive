rogerdv | 2017-01-02 01:01:09 UTC | #1

How can I detect (and interpret) mouse wheel events? I would like to use it for zoom in/out, but havent seen a sample that uses it.

-------------------------

Mike | 2017-01-02 01:01:09 UTC | #2

You can use input::GetMouseMoveWheel() to capture the wheel delta. For example, set zoom variable to zoom += delta
Alternatively you can use 'E_MOUSEWHEEL' event (see [url]http://urho3d.github.io/documentation/HEAD/_event_list.html[/url]).
You can also check how the Editor handles zoom.

-------------------------

rogerdv | 2017-01-02 01:01:10 UTC | #3

Thanks, worked using input::GetMouseMoveWheel, but got a weird problem, when I zoom in, I can get close to floor, but when zoom out, almost inmediatly I get a black screen.
This is my camera creation code:

[quote] _target = new Urho3D::Node(context_);
			_cameraNode = _target->CreateChild("cam");  //new Urho3D::Node(context_);

			camera = _cameraNode->CreateComponent<Camera>();
			camera->SetFarClip(300.0f);
			camera->SetOrthographic(true);[/quote]

And zoom code, in scene update handler:

[code]delta = GetSubsystem<Urho3D::Input>()->GetMouseMoveWheel();
					zoom = camera->GetZoom()+delta;
					camera->SetZoom(zoom);[/code]

Initially I thought that it was the far clip distance, increased it until 10000, same result.

-------------------------

Mike | 2017-01-02 01:01:10 UTC | #4

You might need to 'scale' delta to customize zoom speed. Try to multiply delta by 0.01 (or divide by 100).

-------------------------

