mayatforest | 2017-01-02 01:13:12 UTC | #1

Hi
Im trying to setup antialiasing mode and nothing changed it values (Xamarin-Urho under android 4.4)
No visual changes and no change in Application.Current.Graphics.MultiSample = 1

I try in static scene example from urho examples

1)
in create scene code call
Urho.Application.Current.Graphics.SetMode(width, height, true, true, true, true, true, true, 4);
or
2)
creating surface with additional parameters
surface = UrhoSurface.CreateSurface(this, Type.GetType(Intent.GetStringExtra("Type")), 
				new ApplicationOptions(assetsFolder: "Data"){AdditionalFlags = "-m 4"},
				true);

Using FXAA shader as in MultiVieweport example helps, but it not so good effect as if i check force 4x MSAA in developer options of android.

Any ideas?

-------------------------

rasteron | 2017-01-02 01:13:12 UTC | #2

Actually this is nothing new and as I am really giving a point to this discussion [url=http://discourse.urho3d.io/t/rendering-improvements-wip/2052/1]here[/url].

You probably have to do with FXAA for now, I'm also trying to do hardware MS on mobile but it does not work on Urho for some reason. Maybe other game engines are just using their own optimized GLES shaders.

-------------------------

