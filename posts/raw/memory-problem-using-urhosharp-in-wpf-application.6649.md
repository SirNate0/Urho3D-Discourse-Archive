HJ2012 | 2021-01-04 07:41:21 UTC | #1

Hi, I have a WPF application with different pages that the user switches between. One of these pages should show an UhroSharp application. This contains a custom geometry and displays a point cloud.
The display works great, but there is a memory leak somewhere. Every time I switch to another page and go back to the Urho application, the memory footprint of my application increases. What I also noticed, on the second visit to the page the show function is called twice, on the third visit three times and so on.
I have tried not to destroy the Urho application, however, when I go to the page the second time, I am only shown a black screen.
How do I exit the application cleanly and restart it?
My code is very simple:

using UrhoSharpWpfExtension = UrhoExtensionsWpf::Urho.Extensions.Wpf;
using UrhoSharp = UrhoSharpGlobal::Urho;

public partial class UrhoWrapperWpf : UserControl
    {
        private UrhoSharpWpfExtension.UrhoSurface _urhoSurface;
        SceneView _urhoApp;

        public UrhoWrapperWpf()
        {
            InitializeComponent();
            _urhoSurface = new UrhoSharpWpfExtension.UrhoSurface()
            {
                HorizontalAlignment = HorizontalAlignment.Stretch,
                VerticalAlignment = VerticalAlignment.Stretch
            };
            Content = _urhoSurface;
            Unloaded += UrhoWrapperWpf_Unloaded;
        }

        private void UrhoWrapperWpf_Unloaded(object sender, RoutedEventArgs e)
        {
            if (_urhoApp?.IsActive == true)
                _urhoSurface.Stop();
            Unloaded -= UrhoWrapperWpf_Unloaded;
        }

        public void ShowPoints(float[] data)
        {
            if (_urhoApp?.IsActive == true)
            {
                UrhoSharp.Application.InvokeOnMain(() =>
								{
                try
                {
                    _urhoApp.ShowPoints(data);
                }
                catch
                {
                }
            });
            }
        }

        public Task<Unit> StartUrhoApp()
        {
            var appOpt = new UrhoSharp.ApplicationOptions(assetsFolder: null)
            {
                Orientation = UrhoSharp.ApplicationOptions.OrientationType.LandscapeAndPortrait,
                UseDirectX11 = true,
                TouchEmulation = true,
                LimitFps = true,
                DelayedStart = true,
                AdditionalFlags = "-q",
                ResourcePrefixPaths = new string[0],
            };

            try
            {
                _urhoApp = await _urhoSurface.Show<SceneView>(appOpt);
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                //ToDo log exception
            }

            return Task.FromResult(Unit.Default);
        }

        public Task<Unit> StopUrhoApp()
        {
            return Task.FromResult(Unit.Default);
        }
}

The Stop Method in SceneView looks like this:

protected override void Stop()
        {
            base.Stop();
            SizeBuffers(0);
            scene.RemoveAllChildren();
            CameraNode.RemoveAllChildren();
            CameraNode.Remove();
            Dispose();
            Task.Delay(25);
            vertexData = null;
            indexData = null;
        }

I use UrhoSharp and UrhoSharp.Wpf v1.9.67

I still found this link, could it have something to do with this?
[https://github.com/xamarin/urho/issues/311](https://github.com/xamarin/urho/issues/311)

Thank you for your help!

-------------------------

1vanK | 2021-01-04 21:40:50 UTC | #2

We have nothing to do with UrhoSharp, use Xamarin forum

-------------------------

