z80 | 2019-11-20 03:28:48 UTC | #1

Hello!

I'm trying to make a derivative object based on **Urho3D::Component** to be replicated over network.

How I do that is the following:

    class RefFrame:  public Urho3D::Component
    {
        URHO3D_OBJECT( RefFrame, Component )
    public:
        /// Register object factory.
        static void RegisterObject( Context * context);

        RefFrame( Context * ctx, const String & name=String() );
        virtual ~RefFrame();

        void setName( const String & name );
        ...


    void RefFrame::RegisterObject( Context * context )
    {
        context->RegisterFactory<RefFrame>();
        URHO3D_COPY_BASE_ATTRIBUTES( Component );
        URHO3D_ATTRIBUTE( "Name", String, name_, "", AM_DEFAULT );
    }


And when I create the "**RefFrame**" component as either **Scene::CreateComponent\<RefFrame\>( REPLICATED )** or **Node::CreateComponent\<RefFrame\>( REPLICATED )** it is created. But there is no reaction on component attributes change.

Even when I explicitly call "**MarkNetworkUpdate()**" nothing happens. Inside "**MarkNetworkUpdate()**" the "**networkUpdate_**" field is always "**true**". 

And **Component::PrepareNetworkUpdate()** for this component is called only once and exits because of "**networkState_->attributes_**" is **NULL**.

What do I miss here?

-------------------------

Modanung | 2019-11-21 23:59:59 UTC | #2

Is the `Node` itself a _replicated_ one?

> Note that a replicated component created into a local node will not be replicated, as the node's locality is checked first.

-------------------------

Modanung | 2019-11-22 00:03:00 UTC | #3

Does `setName` call `SetAttribute`?  
It would in turn call `OnSetAttribute`, which contains a call to `MarkNetworkUpdate()`.

-------------------------

z80 | 2019-11-22 02:38:46 UTC | #4

[quote="Modanung, post:2, topic:5726"]
Is the `Node` itself a *replicated* one?
[/quote]
Yes. It is replicated. I also tried to create component directly by Scene.


[quote="Modanung, post:3, topic:5726, full:true"]
Does `setName` call `SetAttribute` ?
It would in turn call `OnSetAttribute` , which contains a call to `MarkNetworkUpdate()` .
[/quote]

No I didn't try calling **SetAttribute()**. What it does is

    void setName( const String & name )
    {
        name_ = name;
        MarkNetworkUpdate();
    }

I'll try calling "SetAttribute()".

BTW, does it matter when exactly replicated components are created before/after connection?

Thank you!

-------------------------

Modanung | 2019-11-22 09:22:12 UTC | #5

[quote="z80, post:4, topic:5726"]
BTW, does it matter when exactly replicated components are created before/after connection?
[/quote]
This should not make any difference, as long as they are created by the server.

-------------------------

