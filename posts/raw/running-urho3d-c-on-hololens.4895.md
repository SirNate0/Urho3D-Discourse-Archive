I3DB | 2019-02-06 04:26:10 UTC | #1

I've been using the UrhoSharp binding to run Urho3D on hololens.

Now wondering if I can get the latest Urho3D release and run it directly on hololens.

Is it possible?

[The urhosharp binding adds urhoholo.h/.cpp](https://github.com/xamarin/urho/tree/master/Urho3D/Urho3D_SharpReality/UrhoSharp.SharpReality) in creating a specific UrhoSharp version used by the hololens. This goes into a dll, mono-holourho.dll.

This dll is consumed by[the SharpReality binding](https://github.com/xamarin/urho/tree/master/Bindings/SharpReality).

Of course, I'd be switching over to c++ in walking away from the binding. That's understood. I don't want to update the binding, that's not the goal here.

[Here's some windows docs on starting a holographic app in c++](https://docs.microsoft.com/en-us/windows/mixed-reality/creating-a-holographic-directx-project).

-------------------------

I3DB | 2019-02-06 05:04:07 UTC | #2

Here's a [sample UWP app](https://github.com/Microsoft/Windows-universal-samples/blob/master/Samples/BasicHologram/cpp/AppView.cpp), that shows AppView and AppViewSource, both in c++.

The UrhoSharp binding provides [UrhoAppView.cs](https://github.com/xamarin/urho/blob/050fdf9943b154549e7928b32f398e727191202a/Bindings/SharpReality/UrhoAppView.cs#L1) and [UrhoAppViewSource.cs](https://github.com/xamarin/urho/blob/050fdf9943b154549e7928b32f398e727191202a/Bindings/SharpReality/UrhoAppViewSource.cs#L1)

[Then this c++ file ties urho3d to the urhoappview](https://github.com/xamarin/urho/blob/050fdf9943b154549e7928b32f398e727191202a/Urho3D/Urho3D_SharpReality/UrhoSharp.SharpReality/UrhoHolo.cpp#L1).

-------------------------

