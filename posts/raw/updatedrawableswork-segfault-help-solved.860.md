practicing01 | 2017-01-02 01:03:35 UTC | #1

Edit: Silly me, I have a component that deletes its node_ after some time, bad idea.  I'll have to rethink how do accomplish timed node deletion.

Hello, I'm clone()'ing some projectiles on TouchDown() and it seems to spawn and move fine but after a few seconds of movement I get a segault.  Thanks for any help.

GDB backtrace:
[code]
#0  0x0832bc9e in Urho3D::UpdateDrawablesWork(Urho3D::WorkItem const*, unsigned int) ()
#1  0x08414422 in Urho3D::WorkQueue::Complete(unsigned int) ()
#2  0x08330143 in Urho3D::Octree::Update(Urho3D::FrameInfo const&) ()
#3  0x083aa924 in Urho3D::Renderer::Update(float) ()
#4  0x083adf58 in Urho3D::EventHandlerImpl<Urho3D::Renderer>::Invoke(Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) ()
#5  0x084156c2 in Urho3D::Object::OnEvent(Urho3D::Object*, Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) ()
#6  0x08416d63 in Urho3D::Object::SendEvent(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) ()
#7  0x0840b23f in Urho3D::Engine::Update() ()
#8  0x0840b673 in Urho3D::Engine::RunFrame() ()
#9  0x084006e0 in Urho3D::Application::Run() ()
#10 0x081d366e in RunApplication() ()
#11 0x0819d690 in main ()
[/code]

-------------------------

cadaver | 2017-01-02 01:03:35 UTC | #2

What (drawable) components do your projectiles contain? What language are you using? If possible, post code and rough approximation of your objects, for example a prefab that uses bundled Urho assets, that reproduces the problem.

For timed deletion, it's legal to call Remove() on the node. For example NinjaSnowWar does this when the snowballs vanish after a set time. Just deleting a node directly (C++ or Lua) is not permitted because that doesn't remove it from the scene hierarchy and the engine will still try to access it.

-------------------------

