Athos | 2019-11-21 21:08:49 UTC | #1

I noticed the **todo** in [https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Core/Context.cpp#L138](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Core/Context.cpp#L138)

Since those subsystems were created by the Engine class, why not remove them in the Engine destructor?

	Engine::~Engine()
	{
		context_->RemoveSubsystem<Audio>();
		context_->RemoveSubsystem<UI>();
		context_->RemoveSubsystem<Input>();
		context_->RemoveSubsystem<Renderer>();
		context_->RemoveSubsystem<Graphics>();
	}

-------------------------

weitjong | 2019-11-22 14:15:52 UTC | #2

It was from a quick fix about 7 years ago. See https://github.com/urho3d/Urho3D/commit/4f5e060a6acf9640e2940aa3f7189fb7eaa0b6b5

-------------------------

SirNate0 | 2019-11-22 14:34:30 UTC | #3

I like the suggestion! If I'm not mistaken, Engine is also a subsystem, so when the context is destroyed and it's hash map holding the subsystems is emptied, there won't be a guarantee that the Engine subsystem is destroyed first. I haven't looked through the code regarding that, so I could be wrong. If I'm correct, though, I think you'll also need to either have shared pointers to those subsystems in Engine or will have to explicitly remove the engine subsystem in Context's destructor.

-------------------------

weitjong | 2019-11-22 14:45:28 UTC | #4

Two things for sure, the `Engine` is not a subsystem and the "todo" marker is not intended to remind the original author (Lasse) to revert the code back. My two cents.

-------------------------

Modanung | 2019-11-22 15:10:06 UTC | #5

[quote="weitjong, post:4, topic:5728"]
the `Engine` is not a subsystem
[/quote]

Actually...

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Engine/Engine.cpp#L118-L119

-------------------------

weitjong | 2019-11-22 16:12:01 UTC | #6

Hah! I should have double checked the codebase myself before making that previous post. To me the “Engine” doesn’t seem to be in the same level as the rest of the subsystems. Perhaps we have not modeled the dependency between the subsystems properly. The context class should not know/have the harcoded order to remove the subsystems. It will be great if Lasse can comment on this todo marker.

-------------------------

Modanung | 2019-11-22 16:45:03 UTC | #7

[quote="weitjong, post:6, topic:5728"]
It will be great if Lasse can comment on this
[/quote]
Mentioning @cadaver occasionally summons him. :slightly_smiling_face:

-------------------------

Athos | 2019-11-22 21:22:39 UTC | #8

This is what I came up with:
The Application registers the Engine as subsystem and also removes it when the Engine is stoped.

I don't know how to make this work on Android/iOS since I'm not targeting those platforms (Perhaps remove the Engine subsystem in RunFrame when exiting?), but here's some code:

**Application.cpp**

	Application::Application(Context *context) :
		Object(context),
		exitCode_(EXIT_SUCCESS)
	{
		...

		engine_ = context_->RegisterSubsystem<Engine>();
		
		...
	}
	
	int Application::Run()
	{
		...

		Stop();

		// Now this Application is the only object holding a reference to an Engine instance.
		context_->RemoveSubsystem<Engine>();
		
		return exitCode_;
		
		...
	}

**Context.cpp**

	Context::~Context()
	{
		subsystems_.Clear();
		factories_.Clear();

		...
	}


**Engine.h**

	class URHO3D_API Engine : public Object
	{
		...
		
	private:
		SharedPtr<FileSystem> filesystem_;
	#ifdef URHO3D_LOGGING
		SharedPtr<Log> log_;
	#endif
	#ifdef URHO3D_PROFILING
		SharedPtr<Profiler> profiler_;
		SharedPtr<EventProfiler> eventProfiler_;
	#endif

		// Note the ordering, we want Graphics to be the last to be destructed.
		SharedPtr<Graphics> graphics_;
		SharedPtr<Renderer> renderer_;
		SharedPtr<Input> input_;
		SharedPtr<Audio> audio_;
		SharedPtr<UI> ui_;

		SharedPtr<Time> time_;
		SharedPtr<WorkQueue> workQueue_;
		SharedPtr<ResourceCache> resourceCache_;
		SharedPtr<Localization> localization_;
	#ifdef URHO3D_NETWORK
		SharedPtr<Network> network_;
	#endif
	#ifdef URHO3D_DATABASE
		SharedPtr<Database> database_;
	#endif
	
		...
	}
	
	
**Engine.cpp**

	Engine::Engine(Context *context) :
		...
	{
		filesystem_ = context_->RegisterSubsystem<FileSystem>();
	#ifdef URHO3D_LOGGING
		log_ = context_->RegisterSubsystem<Log>();
	#endif
	#ifdef URHO3D_PROFILING
		profiler_ = context_->RegisterSubsystem<Profiler>();
	#endif
		input_ = context_->RegisterSubsystem<Input>();
		audio_ = context_->RegisterSubsystem<Audio>();
		ui_ = context_->RegisterSubsystem<UI>();
		time_ = context_->RegisterSubsystem<Time>();
		workQueue_ = context_->RegisterSubsystem<WorkQueue>();
		resourceCache_ = context_->RegisterSubsystem<ResourceCache>();
		localization_ = context_->RegisterSubsystem<Localization>();
	#ifdef URHO3D_NETWORK
		network_ = context_->RegisterSubsystem<Network>();
	#endif
	#ifdef URHO3D_DATABASE
		database_ = context_->RegisterSubsystem<Database>();
	#endif
	
		...
	}
	
	Engine::~Engine()
	{
		// Remove SDL based subsystems from the context.
		context_->RemoveSubsystem<UI>();
		context_->RemoveSubsystem<Audio>();
		context_->RemoveSubsystem<Input>();
		context_->RemoveSubsystem<Renderer>();
		context_->RemoveSubsystem<Graphics>();
	}

This also reduces the number of GetSubsystem() calls.

-------------------------

Modanung | 2019-11-22 22:13:15 UTC | #9

@Athos Could you turn this into a PR and link to it from here?
I think that would make it easier to discuss it further.

-------------------------

Athos | 2019-11-23 00:53:18 UTC | #10

https://github.com/urho3d/Urho3D/pull/2549

-------------------------

cadaver | 2019-11-25 08:54:24 UTC | #11

If you wanted to guarantee subsystem removal order, you could use a different data structure for that in addition to the lookup map, ie. a vector in Context, that the subsystems are also added to. And then removed in a reverse order.

-------------------------

