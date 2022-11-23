tianlv777 | 2022-03-22 06:21:35 UTC | #1

NavigationMesh navMesh = scene.GetComponent<NavigationMesh>();
Vector3 pathPos = navMesh.FindNearestPoint(hitPos, new Vector3(1.0f, 1.0f, 1.0f));
Node jack1 = scene.GetChild("jack", false);
var result = navMesh.FindPath(jack1.Position, pathPos);


note:navMesh.FindPath(jack1.Position, pathPos);//this will crash every running this


android crash.
i use xamarin android and nuget.
I have no test it by urho.net. I guess it will crashed too.

-------------------------

tianlv777 | 2022-03-22 07:25:00 UTC | #2

urho.net is ok....seem
   	var result = navMesh.FindPath(jackGroup.Position, pathPos);

-------------------------

tianlv777 | 2022-03-22 07:25:24 UTC | #3

so nuget is problem?

-------------------------

elix22 | 2022-03-22 14:05:58 UTC | #4

[quote="tianlv777, post:2, topic:7223, full:true"]
[urho.net](http://urho.net) is ok…seem
var result = navMesh.FindPath(jackGroup.Position, pathPos);
[/quote]

Yep , in Urho.net was fixed by @dertom 
https://github.com/elix22/Urho3D/pull/71

-------------------------

Nerrik | 2022-03-22 14:54:30 UTC | #5

In my project i updated the complete old recast nav. thats used by urho3d with https://github.com/recastnavigation/recastnavigation because of many crashes (segfaults) with complicated large navmeshes (large terrain with objects). There are many bugs that causes crashes fixed in this further developed version and a crash never happend again after the update.

-------------------------

tianlv777 | 2022-03-25 08:07:30 UTC | #6

[Uploading: QQ图片20220325155932.png...]()
![QQ图片20220325160118|640x258](upload://9pbXElSGVPMlFNKybyQUpVdFPq.png)
why plane has different color.
            Node planeNode = scene.CreateChild("Plane");
            planeNode.Scale = new Vector3(100.0f, 1.0f, 100.0f);
            StaticModel planeObject = planeNode.CreateComponent<StaticModel>();
            planeObject.Model = (ResourceCache.GetModel("Models/Plane.mdl"));
           planeObject.SetMaterial(ResourceCache.GetMaterial("Materials/StoneTiled.xml"));

<material>

    <technique name="Techniques/DiffNormal.xml" quality="1" />

    <technique name="Techniques/Diff.xml" quality="0" />

    <texture unit="diffuse" name="Textures/StoneDiffuse.dds" />

    <texture unit="normal" name="Textures/StoneNormal.dds" />

    <shader psdefines="PACKEDNORMAL" />

    <parameter name="MatSpecColor" value="0.3 0.3 0.3 16" />

    <parameter name="UOffset" value="4 0 0 0" />

    <parameter name="VOffset" value="0 4 0 0" />

</material>

the  TerrainDetail2.dds how to add?or how to edit dds?
I remove resource Textures/StoneDiffuse.dds from asset folder.But urho.net run As usual.
I can't get the right logic to edit TerrainDetail or how to add it.

-------------------------

tianlv777 | 2022-03-25 08:09:34 UTC | #8

![QQ图片20220325160905|690x443](upload://lgnSXLdU7kSYSIHMiBtSIyKlZQJ.jpeg)

-------------------------

elix22 | 2022-03-25 11:12:10 UTC | #9

[quote="tianlv777, post:6, topic:7223"]
I remove resource Textures/StoneDiffuse.dds from asset folder.But [urho.net](http://urho.net) run As usual.
[/quote]

During first run , the Assets folder is copied into the **Bin** folder (i.e. **bin/Debug/netcoreapp3.1**) 
Every time you **modify** the content of some files in the Assets folder , before the next run only the modified files are copied to the **Bin** folder.

During the runtime , the application is reading from the generated **Bin** folder not the Assets folder.


If you **delete** a file in the Assets folder the file is **not** deleted from the Bin folder (I guess it might be considered a bug , but I didn't find an optimized solution for that)

Currently you have 2 options 
- Delete the file manually from the Bin folder
- make a clean build 

Regarding DDS  , you can read more about it in 
https://fileinfo.com/extension/dds

-------------------------

tianlv777 | 2022-03-27 05:50:27 UTC | #11

THANKS very much！！！THANKS very much！！！

-------------------------

tianlv777 | 2022-03-27 09:24:09 UTC | #12

My main game target platform is Android, so I can't accept Urho Net cannot debug Android programs in real time
So there's any way to make Urho Net can debug Android programs in real time.
I have two choices now.
1、 Using Urho net that it could debug android program real time. And I find way to migrate V8 and Android WebView to Urho net. Because my android game is using v8 engine and webview.
2、find a way to let urho. net could be packed nuget. So I can use the latest Urho.Net function in xamarin.android at visual sutdio 2022.the findpath function is ok.The Jint is cool to create many maps.

What about your suggestion?

-------------------------

elix22 | 2022-03-27 19:06:19 UTC | #13

[quote="tianlv777, post:12, topic:7223"]
So there’s any way to make Urho Net can debug Android programs in real time.
[/quote]

Currently the Android mono debugger is not supported  , it might be supported in 2022/Q4 once my Net.6 Game Editor Will be released.
You can use **Urho.IO.Log.Info , Urho.IO.Log.Debug , Urho.IO.Log.Error** , (supported on all platforms)

[quote="tianlv777, post:12, topic:7223"]
So I can use the latest [Urho.Net](http://urho.net/) function in xamarin.android
[/quote]

Urho.net can not  run with Xamarin.Android , I don't plan to support it .
On mobile devices Urho.Net  interacts directly with the Mono runtime (not using Xamarin) , this is one of the reasons it's so blazing fast (fast as C++)

Javascript interacts/runs nicely with Urho.net on all platforms , I guess you played with the Javascript Sample , It's not my cup of tea but I understand people that are using it.
https://github.com/Urho-Net/Samples/tree/main/JavaScriptSample

I have written a small Wiki page for Android
https://github.com/Urho-Net/Urho.Net/wiki/Android

-------------------------

tianlv777 | 2022-03-30 06:44:24 UTC | #14

https://github.com/1vanK/Urho3DOutline
outline is not ok at android.but ok at pc.
  void SetupViewport()
        {
            var cache = ResourceCache;

            var g = Graphics;
            var renderer = Renderer;

            var viewport = new Viewport(Context, scene, CameraNode.GetComponent<Camera>());
            renderer.SetViewport(0, viewport);
            RenderPath effectRenderPath = viewport.RenderPath.Clone();
            effectRenderPath.Append(cache.GetXmlFile("PostProcess/Outline.xml"));
            effectRenderPath.Append(cache.GetXmlFile("PostProcess/FXAA3.xml"));
            viewport.RenderPath = effectRenderPath;

            int w = g.Width;
            int h = g.Height;
            var renderTexture = new Urho.Urho2D.Texture2D(Context);
            renderTexture.SetSize(w, h, Graphics.RGBFormat, TextureUsage.Rendertarget);
            renderTexture.FilterMode = TextureFilterMode.Nearest;
            renderTexture.Name = "OutlineMask";
            cache.AddManualResource(renderTexture);

            var surface = renderTexture.RenderSurface;
            surface.UpdateMode = RenderSurfaceUpdateMode.Updatealways;
            var outlineViewport = new Viewport(Context, outlineScene, outlineCameraNode.GetComponent<Camera>());
            surface.SetViewport(0, outlineViewport);


        }

I guess Outline.glsl can't use at android.......

-------------------------

tianlv777 | 2022-03-30 06:48:28 UTC | #15

![QQ图片20220330144545|375x500](upload://3YbzG9foivdhHyekXH1igSvrYeE.jpeg)

-------------------------

tianlv777 | 2022-03-30 09:25:56 UTC | #16

https://github.com/tianlv777/urho.net-test/blob/main/outline.cs

-------------------------

elix22 | 2022-03-30 17:48:22 UTC | #17

Remove this line , will show outline on mobile iOS/Android.

https://github.com/tianlv777/urho.net-test/blob/main/outline.cs#L197

-------------------------

