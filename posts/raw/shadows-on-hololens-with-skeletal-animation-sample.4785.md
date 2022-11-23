I3DB | 2019-01-01 13:06:37 UTC | #1

[Feature Sample For Skeletal Animation](https://github.com/xamarin/urho-samples/tree/master/FeatureSamples/Core/06_SkeletalAnimation)

Converted this above Feature Sample to work on Hololens. All works fine except for shadows.

The default DirectionalLight setup in the StereoApplication in UrhoSharp.SharpReality sets CastShadows to false.

That is shown here:https://github.com/xamarin/urho/blob/050fdf9943b154549e7928b32f398e727191202a/Bindings/Portable/SharpReality/StereoApplication.cs#L110

Tried setting the DirectionalLight to cast shadows, and also setup a new light for the scene and tried that way.

Likewise, the default setting for Renderer also is set to not draw shadows, but overriding that also has no effect. And also the Zone component setup override to CastShadows.

Also reviewed this https://forums.xamarin.com/discussion/72843/urhosharp-is-casting-shadows-possible

Still  ... no shadows on Hololens.

Any ideas? Is Hololens shadowless?

-------------------------

I3DB | 2019-01-25 16:38:28 UTC | #2

When I try other platforms with[the C# feature samples](https://github.com/xamarin/urho-samples), the WPF and WinForms bindings samples show shadows. The UWP binding doesn't.

There isn't provided a Hololens port for the Feature Samples, and I've been working through them to see which work on Hololens and which don't. Most of them do work with some modifications, but not able to get shadows working.

The SharpReality binding for Urho3D seems suspect, else there is some missing setup. Hololens uses the StereoApplication as it's Urho3D Application.

I'm not familiar enough with shadows or what's required to be able to troubleshoot this currently. Have gone through numerous tests and don't know if I've gotten closer or not.

If anyone is able to give a brief setup of what is required for shadows, that would be helpful. On various other threads there have been comments related, such as setting CastShadows = true. But this is something deeper I suspect, and I need details on what's required from beginning to end, to be able to verify if all is in place.

-------------------------

