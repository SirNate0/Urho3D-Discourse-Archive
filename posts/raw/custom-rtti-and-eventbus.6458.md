Athos | 2020-10-26 05:06:43 UTC | #1

I've finished changing the way events work in Urho3D, implemented a custom RTTI and wanted to share some details of it.
First, the regular Urho3D code:

    // Custom sample event
    URHO3D_EVENT(E_SAMPLEEVENT, SampleEvent)
    {
    	URHO3D_PARAM(P_OBJ, Obj);		// (void*) RefCounted*
    	URHO3D_PARAM(P_INDEX, Index);	// (long long) size_t
    }

    // =================================================
    // A class which will listen to the new event:
    class NodeListener : public Node
    {
    public:
    	NodeListener(Context* context) :
    		Node(context)
    	{
    		SubscribeToEvent(E_SAMPLEEVENT, URHO3D_HANDLER(NodeListener, OnSampleEvent));
    	}

    	~NodeListener() override = default;

    	URHO3D_OBJECT(NodeListener, Node);

    	void SetId(size_t id)
    	{
    		id_ = id;
    	}

    	size_t GetId() const
    	{
    		return id_;
    	}

    private:
    	void OnSampleEvent(StringHash type, VariantMap& data)
    	{
    		Variant& node = data[SampleEvent::P_OBJ];
    		Variant& index = data[SampleEvent::P_INDEX];

    		NodeListener* listener = dynamic_cast<NodeListener*>((RefCounted*)node.GetVoidPtr());
    		if (listener == this)
    		{
    			SetId((size_t)index.GetInt64());
    		}
    	}

    private:
    	size_t id_ {};
    };

    // =================================================
    // Assuming you have a basic class for creating the Urho3D loop, scene, etc:
    // Create 1000 node listeners
    {
    	// listeners_ is of type Vector<SharedPtr<NodeListener>>
    	const size_t count = 100 * 10;
    	listeners_.Reserve(count);

    	for (size_t i = 0; i < count; ++i)
    	{
    		SharedPtr<NodeListener> node {new NodeListener(context_)};
    		scene_->AddChild(node);

    		listeners_.Push(node);
    	}
    }

    // =================================================
    // Now, somewhere in the main loop, when you press a key:
    if (input_->GetKeyPress(Key::KEY_SPACE))
    {
    	const size_t listenerCount = listeners_.Size();

    	VariantMap& data = GetEventDataMap();

    	auto start = std::chrono::high_resolution_clock::now();
    	{
    		for (size_t i = 0; i < listenerCount; ++i)
    		{
    			data[SampleEvent::P_OBJ] = (void*)listeners_[i].Get();
    			data[SampleEvent::P_INDEX] = (long long)i;

    			SendEvent(E_SAMPLEEVENT, data);
    		}
    	}
    	auto end = std::chrono::high_resolution_clock::now();
    	auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    	URHO3D_LOGINFOF("Sending %d events to %d node listeners took %d ms", listenerCount, listenerCount, duration);
    }

On my hardware, the above scenario consistently produces:
"INFO: Sending 1000 events to 1000 node listeners took 36 ms"

Now, after some major changes, here's the same sample:

    // Custom sample event
    struct SampleEvent
    {
    	RefCounted* obj;
    	size_t index;
    };

    // =================================================
    // The class which will listen to the event:
    class NodeListener : public Node
    {
    public:
    	NodeListener(Context* context) :
    		Node(context)
    	{
    		ListenEvent<SampleEvent>([this](const SampleEvent& data)
    		{
    			NodeListener* listener = RTTI::DynamicCast<NodeListener*>(data.obj);
    			if (listener == this)
    			{
    				SetId(data.index);
    			}
    		});
    	}
    	~NodeListener() override = default;

    	RTTI_IMPL();

    	void SetId(size_t id)
    	{
    		id_ = id;
    	}

    	size_t GetId() const
    	{
    		return id_;
    	}

    private:
    	size_t id_ {};
    };

    // =================================================
    // Creating the 1000 node listeners is exactly the same as before (except it's using the std::vector);
    // Then, somewhere in the main loop:

    if (input_->GetKeyPress(KeyCode::Space))
    {
    	size_t listenerCount = listeners_.size();

    	auto start = std::chrono::high_resolution_clock::now();
    	{
    		for (size_t i = 0; i < listenerCount; ++i)
    		{
    			SendEvent(SampleEvent {
    				listeners_[i].Get(),
    				i
    			});
    		}
    	}
    	auto end = std::chrono::high_resolution_clock::now();
    	auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    	URHO3D_LOGINFO(fmt::format("Sending {0:d} events to {0:d} node listeners took {1:d}ms", listenerCount, duration).c_str());
    }

On my hardware, the changes above consistently produces:
"INFO: Sending 1000 events to 1000 node listeners took 8ms"

Both of the tests were compiled on windows using MSVC 2019: x64 Static Release, C++17;
C++ exceptions disabled;
The regular Urho3D uses the default c++ RTTI, and thus it was enabled;

The custom RTTI was coded by Samuel Kahn, he explains how the magic works here:
[http://kahncode.com/2019/09/24/c-tricks-fast-rtti-and-dynamic-cast/](http://kahncode.com/2019/09/24/c-tricks-fast-rtti-and-dynamic-cast/)
I've only made minor changes to it. Instead of generating a random id at runtime, it is generated at compile time.

The event handler was replaced by EventBus (2.6):
[https://github.com/gelldur/EventBus](https://github.com/gelldur/EventBus)
One thing to consider is you can't listen an event from a specific sender.

Some other notes:
All containers (except String) were replaced by the ::std ones;
Urho2D/UI and scripting languages were ditched (I'll be using a third party lib for UI);

-------------------------

Eugene | 2020-10-26 08:30:12 UTC | #2

I wonder how much of this performance difference is from doing some work more optimally, and how much is from not doing some work you personally don't need. E.g. your event doesn't use VariantMap for paramters, which makes it incompatible with Urho scripting API.

Also, how much of performance difference comes from new RTTI and how much from different event logic?

-------------------------

Athos | 2020-10-26 16:02:52 UTC | #3

Sending an event without any parameters (using same sample as before, but simplified):

    // Event sender
    VariantMap& data = GetEventDataMap();
    auto start = std::chrono::high_resolution_clock::now();
    {
    	for (size_t i = 0; i < listenersCount; ++i)
    	{
    		SendEvent(E_SAMPLEEVENT, data);
    	}
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    // And the event handler:
    void NodeListener::OnSampleEvent(Urho3D::StringHash type, Urho3D::VariantMap& data)
    {
    	SetId(GetId() + 1);
    }

takes 11ms

If I change the event a little bit (no dynamic casting):

    // Sender
    VariantMap& data = GetEventDataMap();
    auto start = std::chrono::high_resolution_clock::now();
    {
    	for (size_t i = 0; i < listenersCount; ++i)
    	{
    		data[SampleEvent::P_OBJ] = (void*)listeners[i].Get();
    		data[SampleEvent::P_INDEX] = (long long)i;
    		SendEvent(E_SAMPLEEVENT, data);
    	}
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    // Event handler
    void NodeListener::OnSampleEvent(Urho3D::StringHash type, Urho3D::VariantMap& data)
    {
    	NodeListener* listener = (NodeListener*)data[SampleEvent::P_OBJ].GetVoidPtr();
    	size_t index = (size_t)data[SampleEvent::P_INDEX].GetUInt64();

    	if (listener == this)
    	{
    		SetId(index);
    	}
    }

takes 20ms

**Switching to EventBus**

    // Sender
    auto start = std::chrono::high_resolution_clock::now();
    {
    	for (size_t i = 0; i < listenersCount; ++i)
    	{
    		SendEvent(SampleEvent {});
    	}
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    // Same simple handler
    NodeListener::NodeListener(Context* context) :
    	Node(context)
    {
    	ListenEvent<SampleEvent>([this](const SampleEvent& data)
    	{
    		SetId(GetId() + 1);
    	});
    }

takes 2ms

Also, I tested using a VariantMap:

    // The event
    struct SampleEvent
    {
    	mutable Urho3D::VariantMap map;
    };

    // The event handler
    NodeListener::NodeListener(Context* context) :
    	Node(context)
    {
    	ListenEvent<SampleEvent>([this](const SampleEvent& data)
    	{
    		static StringHash obj_h {"obj"};
    		static StringHash index_h {"index"};

    		NodeListener* listener = (NodeListener*)data.map[obj_h].GetVoidPtr();
    		size_t index = (size_t)data.map[index_h].GetUInt64();

    		if (listener == this)
    		{
    			SetId(index);
    		}
    	});
    }

    // The event sender
    auto start = std::chrono::high_resolution_clock::now();
    {
    	static StringHash obj_h {"obj"};
    	static StringHash index_h {"index"};

    	for (size_t i = 0; i < listenersCount; ++i)
    	{
    		SampleEvent data {};
    		data.map[obj_h] = (void*)listeners[i].Get();
    		data.map[index_h] = (long long)i;

    		SendEvent(data);
    	}
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

Takes 11ms

**RTTI and dynamic casts**

I noticed the custom RTTI is actually slower than default dynamic_cast<>;
I think I messed up somewhere, need to test more.
But here some numbers (1 000 000 dynamic cast from RefCounted* to NodeListener*):

dynamic_cast<> takes 34ms
RTTI::DynamicCast<> takes 45ms

The code used:

    long long duration {};
    for (size_t c = 0; c < 1000; ++c)
    {
    	for (size_t i = 0; i < listeners.Size(); ++i)
    	{
    		NodeListener* node {};
    		RefCounted* src = listeners[i].Get();

    		auto start = std::chrono::high_resolution_clock::now();
    		{
    			// Select which RTTI to use
    			//node = dynamic_cast<NodeListener*>(src);
    			//node = RTTI::DynamicCast<NodeListener*>(src);
    		}
    		auto end = std::chrono::high_resolution_clock::now();
    		duration += std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();

    		if (node)
    		{
    			node->SetId(node->GetId());
    		}
    	}
    }

-------------------------

vmost | 2020-10-26 17:08:01 UTC | #4

Pretty sure VariantMap uses dynamic allocation, while your `SampleEvent` struct is being statically allocated. Could explain a lot of the performance gap.

-------------------------

vmost | 2020-10-27 17:45:50 UTC | #5

Thought about this some more, and had an idea that may work pretty well without redoing much of Urho3D's current event handling system. I have not tested it or anything, and it's surely incomplete.

```
//hypothetical event system for Urho3D

//event base
class EventBase
{
public:
//constructors
	/// default constructor: disabled
	EventBase() = delete;

	/// normal constructor
	EventBase(StringHash eventType) : m_event_type{eventType}
	{}

//member functions
	/// get the event type
	StringHash GetEventType() {return m_event_type;}

	/// get string hash representing type of derived object
	virtual StringHash GetType() const = 0;
	/// silence expectations of URHO3D_OBJECT() macro
    virtual const String& GetTypeName() const = 0;
    virtual const TypeInfo* GetTypeInfo() const = 0;
    static const TypeInfo* GetTypeInfoStatic() { return nullptr; }

//member variables
	StringHash m_event_type;
};

//example event
static const Urho3D::StringHash E_KEYDOWN(Urho3D::GetEventNameRegister().RegisterString(#KeyDown));
class KeyDown final : public EventBase
{
	URHO3D_OBJECT(KeyDown, EventBase);

public:
//constructors
	/// default constructor
	KeyDown() : EventBase{E_KEYDOWN}
	{}

//member variables
	int P_KEY;
    int P_SCANCODE;
    int P_BUTTONS;
    int P_QUALIFIERS;
    bool P_REPEAT;
};

template <typename T>
T* GetEventInfo(EventBase* event_base)
{
	if (!event_base)
		return nullptr;

	// poor man's dynamic cast
	if (event_base->GetType() == T::GetTypeStatic())
		return static_cast<T*>(event_base);
	else
		return nullptr;
}

//creating and sending an event
void SomeObj::SomeFunct()
{
	KeyDown keydown_event{};

	keydown_event.P_KEY = KEY_L;
	keydown_event.P_QUALIFIERS = QUAL_SHIFT | QUAL_ALT;

	SendEvent(&keydown_event);
}

//signature of SendEvent()
void Urho3D::Object::SendEvent(EventBase* event);
```

-------------------------

Eugene | 2020-10-27 18:38:14 UTC | #6

1) I like it.
2) It will never work as PR, due to the same issues as before.

You can either have nice strict type or easy interop with scripts. Urho goes the second way. VariantMap is the only way to send event into script without reflection or manual bindings (we have enough of those)

-------------------------

vmost | 2020-10-27 18:46:12 UTC | #7

Actually I don't know anything about Urho3D scripting! Maybe that's why I came up with this lol

-------------------------

