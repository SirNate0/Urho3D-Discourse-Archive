dev4fun | 2018-07-05 22:13:37 UTC | #1

Hey, Im integrating the Urho3D as a library to my old game, and so far, I'm having success. 

My game render uses transformed vertex (rhw) with DrawPrimitiveUP (Directx 9). So, while I dont upgrade all render to urho correctly (using vb and ib, projection etc) I want to keep using my game render working together the Urho render. 

For now, Im rendering my game after E_ENDALLVIEWSRENDER urho event, works good, but that's not what I want. I want to put my render on a renderpath (yet using transformed vertices, rhw, drawprimitiveup etc), like any other thing, this way I can use PostProcess correctly etcc.

I have no idea how I could make it, someone have?

Thanks.

-------------------------

Eugene | 2018-07-06 11:01:09 UTC | #2

There's render path `sendevent` command that allows you to run arbitrary code in arbitrary place of rendering. Is it what you want to achieve?

-------------------------

Alan | 2018-07-06 12:17:18 UTC | #3

I could never get this to work:
```C++
RenderPath * rp = viewport->GetRenderPath();
auto rpc = RenderPathCommand();
rpc.type_ = CMD_SENDEVENT;
rpc.enabled_ = true;
rp->AddCommand(rpc);
SubscribeToEvent(E_RENDERPATHEVENT, URHO3D_HANDLER(SomeClass, SomeFunc));
```

-------------------------

dev4fun | 2018-07-06 18:58:26 UTC | #4

I think so. I want to integrate my render code inside to Urho render. So i believe I need to put this on renderpath.

-------------------------

dev4fun | 2018-07-06 18:58:39 UTC | #5

Some special reason? ll try it anyway, thanks.

-------------------------

