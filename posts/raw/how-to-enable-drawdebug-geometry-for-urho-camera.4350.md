lheller | 2018-06-25 15:09:15 UTC | #1

Hi!

As the title says, I just want to know, whether it is possible to enable/draw **debug geometry** for **Urho camera**?

I am asking it, since the **Camera** class also has the method called **DrawDebugGeometry( )**.

BR,

Ladislav

-------------------------

TheComet | 2018-06-26 07:42:52 UTC | #2

You have to register to E_POSTRENDERUPDATE and call camera->DrawDebugGeometry() yourself. This might look something like this in your application code:

    MyApplication::Start() {
        SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(MyApplication, HandlePostRenderUpdate));
    }

    MyApplication::HandlePostRenderUpdate() {
        DebugRenderer* debug = scene_->GetComponent<DebugRenderer>();
        for (const auto& camera : listOfCameras_)
            camera->DrawDebugGeometry(debug, true);
    }

-------------------------

lheller | 2018-06-26 08:23:39 UTC | #3

Hi @TheComet !

Thanks for replying. Tried your code, it works well, but the debug geometry lines were displayed only for **inactive** cameras, but not for the current active one (which is attached to viewport). Is that OK?

-------------------------

rku | 2018-06-26 10:23:15 UTC | #4

Debug geometry displays view frustum. Active camera can not see it's own debug geometry because it's lines align with screen edges.

-------------------------

lheller | 2018-06-26 10:23:46 UTC | #5

It makes sense!
Thanks!

-------------------------

