Vincentwx | 2017-01-02 01:14:35 UTC | #1

Just share a interesting and good news for Urho3D. Micrsoft's UrhoSharp, which is a C# binding to Urho3d, allows you to develop games for HoloLens. Here is the link to the demo project:

[url]https://github.com/xamarin/urho-samples/tree/master/HoloLens[/url]

-------------------------

larsonmattr | 2017-01-02 01:14:38 UTC | #2

Vincent, this is extremely exciting news!  There was an earlier thread about Hololens and Urho3D, but it was limited to trying to get it to works as a UWP application (i.e. 2D window).  I'll take a look at the code example and start trying this out.

-------------------------

larsonmattr | 2017-01-02 01:14:38 UTC | #3

It was surprisingly easy to get the samples working in Visual Studio.  Very awesome.  And big congrats to Egor

I really enjoyed the crowdnavigation sample where you direct the movement of a group of 3d models walking on the floor.   The rendering and frame rates with some complex models were great and this looks extremely useable to HoloLens development.  I can see this being the best alternative to Unity3d now for the HoloLens!  Great news.

One thing I noticed with multiple of the samples is that there is some poor stability of the object positions in the room when compared against the DirectX samples or unity samples.   Possibly something with the reference frame or the spatial anchors is causing this.

-------------------------

larsonmattr | 2017-01-02 01:14:39 UTC | #4

I wonder if any custom Hololens code will be brought into the base Urho3D codebase from UrhoSharp?

-------------------------

sabotage3d | 2017-01-02 01:14:39 UTC | #5

Awesome work guys. The only problem is the price of the hololens devkit :slight_smile:

-------------------------

Egorbo | 2017-01-02 01:14:40 UTC | #6

heh, thanks guys!
it's still a bit experimental,
for example, [i.imgur.com/Bavyucp.png](http://i.imgur.com/Bavyucp.png) the doc says I should render geometry via the "gree" approach but I've done it via "red" one. 
The green one is done via Geometry Shaders (SV_RenderTargetArrayIndex) - [developer.microsoft.com/en-us/w ... in_directx](https://developer.microsoft.com/en-us/windows/holographic/rendering_in_directx)

HL device hides SwapChain and provides just a backbuffer. So I created two render targets from that backbuffer via this ugly code:
[github.com/xamarin/Urho3D/blob/ ... 2281-L2292](https://github.com/xamarin/Urho3D/blob/master/Source/Urho3D/Graphics/Direct3D11/D3D11Graphics.cpp#L2281-L2292)
(you can find my HL & UWP changes under #if UWP and #id UWP_HOLO)

You can find some gifs in each directory of:
[github.com/xamarin/urho-samples ... r/HoloLens](https://github.com/xamarin/urho-samples/tree/master/HoloLens)

In my twitter, for example:
[twitter.com/EgorBo/status/775816447041777664](https://twitter.com/EgorBo/status/775816447041777664)
[twitter.com/EgorBo/status/780913171263619072](https://twitter.com/EgorBo/status/780913171263619072)
[twitter.com/EgorBo/status/785103710829551616](https://twitter.com/EgorBo/status/785103710829551616)
[twitter.com/migueldeicaza/statu ... 8316926976](https://twitter.com/migueldeicaza/status/775383058316926976)

Youtube channel:
[youtube.com/watch?v=sKDO19lMf-I](https://www.youtube.com/watch?v=sKDO19lMf-I)

The implementation is not backported to upstream as it's not perfect, it has a custom SDL project and messy in general.

I'd love to hear some advices how to improve two-viewports performance or ideas how to implement that GS-based rendering.
PS: I love Urho3D architecture - it's very clean! :slight_smile:

[img]https://habrastorage.org/files/a73/3c5/c3c/a733c5c3c51d451b9ac0cd8081833206.gif[/img]

-------------------------

sabotage3d | 2017-01-02 01:14:41 UTC | #7

What is the performance of these tests? Can you make a screen with the HUD on the actual device?

-------------------------

larsonmattr | 2017-01-02 01:14:41 UTC | #8

EgorBo,

I looked back at the DirectX hololens samples I'm working with.  What I've seen is that although it contains shaders for both geometry-based instanced rendering and viewport shaders, it isn't using the geometry shaders.  The renderers do a call to check if there is viewport support in the device, and for the hololens it is yes - so they use the viewport shaders.  With the viewport shaders it will render each eye's camera pose independently, but right after each other.  Their performance guidelines seem to say avoid geometry shaders ([developer.microsoft.com/en-us/w ... mendations](https://developer.microsoft.com/en-us/windows/holographic/performance_recommendations)), perhaps geometry shaders are not well suited to the HoloLens GPU?

What might be important for the performance is that the DirectX render loop in the main application does an update of the holographicFrame prediction (camera viewProject matrices for left/right eye) immediately prior to doing the actually viewport shader render calls.

        // Up-to-date frame predictions enhance the effectiveness of image stablization and
        // allow more accurate positioning of holograms.
        holographicFrame->UpdateCurrentPrediction();
        HolographicFramePrediction^ prediction = holographicFrame->CurrentPrediction;

-------------------------

