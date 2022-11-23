Molurus | 2017-10-10 14:15:14 UTC | #1

Dear developers,


Currently we are working on an app that visualizes IFC Models on iOS / iPad. We are using Xamarin and Visual Studio 2015 to do this.

Implementation specifics:

1) We are using the class Urho.iOS.UrhoSurface to display our scene creator implementation. (This UrhoSurface is instantiated only once.)

2) We are using a custom scene creator class which extends Urho.Application. The implementation of the Application class pretty much follows the standard examples for Urho3D that we've found. 

3) We use an implementation of the Geometry class to create and add geometry objects to the scene. We fill these geometry objects with VertexBuffers and IndexBuffers we create on the basis of geometry data we import from IFC models.

This all seems to work ok in the sense that we can load complete IFC models and display them without problem. When we load subsequent models we clear the geometry objects from the viewport and add the new geometry as desired.

We however run into one problem that we cannot seem to fix in any way:

Regardless of whether we load various different models or just one model which we leave completely untouched in the viewport, the app just terminates after about 5 minutes. We have set the iPad to not lock the device upon idle, nor does this really seem related to the app going idle in any way. (If we load other models meanwhile, the crash also occurs after about the same amount of time.)

I don't think this is related to memory use or memory management, crashes seem untirely unrelated to the kind of model we load or the amount of memory consumed for it.

We're also not getting any kind of feedback from either Xamarin or Visual Studio. The only message we are getting is a mysterious:

"The app has been terminated."

No other diagnostics info of any kind.

Do you have any ideas or pointers to what might be causing this behaviour?


Thanks in advance,

Best regards,

Molurus

-------------------------

Eugene | 2017-10-10 15:29:53 UTC | #2

>We use an implementation of the Geometry

Do you subclass `Geometry` in C#?
~~I'm unsure whether such things are supported by UrhoSharp.
Well, I doubt that it's possible even in C++ core...~~
I think you don't. Could you share some code?

PS. Note that UrhoSharp is not supported here.I suggest you to somehow check whether the problem is caused by Urho3D core.

-------------------------

Molurus | 2017-10-10 16:28:28 UTC | #3

No, We do not subclass Geometry at all.

We do use UrhoSharp.Forms. If this is not the place for questions related to UrhoSharp, is there any place you can recommend asking our question?

The function creating our geometry objects is listed below. It's now marked as 'unsafe' because we've tried moving it to the iOS layer to have it insert the vertices with a fixed() statement, but that doesn't appear to make any kind of difference. Behaviour remains the same.

PS: I have no clue on how to check if this is caused by the Urho3D core. Any suggestions?

Here's the code converting our vertices and indices to a geometry object:

        public unsafe Node Mesh2UrhoModel(Context Context, Scene scene, Node PlotNode, Material material, float[] verticesArray, Int32[] indicesArray, string globalID, string IFC_Type, string ObjectType)
        {
            // called very often
            // DebugMessage("private void Mesh2UrhoModel(float[] verticesArray, long[] indicesArray, string globalID, string IFC_Type, string ObjectType)");

            VertexBuffer vertexBuffer = new VertexBuffer(Context, false); // false
            IndexBuffer indicesBuffer = new IndexBuffer(Context, false); // false
            uint numberOfVertices = (uint)verticesArray.Length;
            uint numberOfIndices = (uint)indicesArray.Length;

            // Shadowed buffer needed for raycasts to work, and so that data can be automatically restored on device loss
            vertexBuffer.Shadowed = true;
            vertexBuffer.SetSize(numberOfVertices / 6, ElementMask.Position | ElementMask.Normal, false);

            try
            {
                fixed (float* p = &verticesArray[0])
                    vertexBuffer.SetData(p);
            }
            catch (Exception e)
            {
                Debug.WriteLine("Thrown: " + e.Message);
            }

            indicesBuffer.Shadowed = true;
            indicesBuffer.SetSize(numberOfIndices, false, false); // indicesBuffer.SetSize(numberOfIndices, false, false);

            //Reversing the indices array
            //Polygon direction is dependant on the direction in which you reference the vertices
            //So instead of making a polygon between vertices 0-1-2, it should be made between 2-1-0
            //This prevents backfacing; geometry displaying inside out

            // this seems to undo an already executed inversion! see SwapIndices in IFCgeometry.cs

            var indices = new short[numberOfIndices];
            for (var i = numberOfIndices; i > 0; i--)
            {
                var index = numberOfIndices - i;
                indices[index] = (short)indicesArray[i - 1];
            }

            //var indices = new short[numberOfIndices];
            //for (var i = numberOfIndices; i < numberOfIndices; i++)
            //    indices[i] = (short)indicesArray[i];

            // indicesBuffer.SetData(indices); // cannot convert int[] to void *. ask Peter.

            try
            {
                fixed (short* p = &indices[0])
                    indicesBuffer.SetData(p);
            }
            catch (Exception e)
            {
                Debug.WriteLine("Thrown: " + e.Message);
            }

            var geometry = new Geometry();
            geometry.SetNumVertexBuffers(1); // added Sander
            geometry.SetVertexBuffer(0, vertexBuffer);

            geometry.IndexBuffer = indicesBuffer;
            // geometry.SetDrawRange(PrimitiveType.TriangleList, 0, numberOfIndices, true);
            geometry.SetDrawRange(PrimitiveType.TriangleList, 0, numberOfIndices, 0, numberOfVertices / 6, true);

            var model = new Urho.Model();
            model.NumGeometries = 1;
            model.SetGeometry(0, 0, geometry);

            Vector3 minVector = new Vector3(1000000, 1000000, 1000000);
            Vector3 maxVector = new Vector3(-1000000, -1000000, -1000000);

            for (int i = 0; i < verticesArray.Length; i += 3)
            {
                float x = verticesArray[i];
                float y = verticesArray[i + 1];
                float z = verticesArray[i + 2];

                if (x < minVector.X) minVector.X = x;
                if (y < minVector.Y) minVector.Y = y;
                if (z < minVector.Z) minVector.Z = z;

                if (x > maxVector.X) maxVector.X = x;
                if (y > maxVector.Y) maxVector.Y = y;
                if (z > maxVector.Z) maxVector.Z = z;
            }

            model.BoundingBox = new BoundingBox(minVector, maxVector);
            
            //model.BoundingBox = new BoundingBox(new Vector3(-100f, -100f, -100f), new Vector3(100f, 100f, 100f));

            var node = PlotNode.CreateChild(globalID); // scene.CreateChild(); // 
            node.Position = new Vector3(0.0f, 0.0f, 0.0f);
            node.SetScale(1.0f);

            var nodeObject = node.CreateComponent<StaticModel>();
            nodeObject.Model = model;

            nodeObject.SetMaterial(material);

            return (node);
        }

-------------------------

Molurus | 2017-10-10 16:42:57 UTC | #4

PS: I'm sorry if this code looks a bit messy. I've obviously been trying a lot of different things.

The code as it is now does work in the sense that it's capable of creating Geometry objects for our IFC objects that are displayed correctly.

-------------------------

Eugene | 2017-10-10 17:51:40 UTC | #5

[quote="Molurus, post:3, topic:3646"]
We do use UrhoSharp.Forms. If this is not the place for questions related to UrhoSharp, is there any place you can recommend asking our question?
[/quote]

Try UrhoSharp forums or their GitHub. This forum is about original C++ Urho3D.

> I have no clue on how to check if this is caused by the Urho3D core. Any suggestions?

Could you reproduce the problem with UrhoSharp samples?

I'll check your code more thoughtfully later, but I am unsure that I'll find anything.

-------------------------

Lumak | 2017-10-10 18:32:08 UTC | #6

This line looks suspicious: edit- disregard the divide by 6. I'm going to assume that the [b]float[] verticesArray[/b] is correctly packed with 3-floats for position and 3-floats for normal.


And you should check if [b]numberOfIndices [/b] is >= 64k boundary and set largetIndeces flag appropriately when calling
[code]
    bool SetSize(unsigned indexCount, bool largeIndices, bool dynamic = false);
[/code]

-------------------------

Eugene | 2017-10-10 18:31:32 UTC | #7

[quote="Lumak, post:6, topic:3646"]
because of divide by 6, index probably exceeds the boundary.
[/quote]

I think `numberOfVertices` is just mis-name, because input is not vertices but floats.

-------------------------

Lumak | 2017-10-10 18:33:39 UTC | #8

Yeah, I realized that when I reviewed the argument list, and edited my comment.

-------------------------

weitjong | 2017-10-11 05:57:30 UTC | #9

Could it be caused by C# GC? Something like objects that are still being used but accidentally got GC-ed? Or the other way around, GC took too long and iOS decided to terminate the unresponsive app?

The error message "The app has been terminated.” string does not come from our Urho code base. Did a git grep and found nothing. Did a google search on that string, however, showed the Xamarin.form are all over the result page. It looks like a common pitfall for Xamarin and I would suspect it has has nothing to do with custom geometry specifically. Since I also do not use Xamarin/UrhoSharp, please take this with a pinch of salt. 

Slightly off-topic, but what say you if we create another forum subcategory here for UrhoSharp? Not that we will have a dedicated support for them, but simply just to separate their issues/questions from ours. UrhoSharp users may also be able to help each other if they could find common topics for them easily.

-------------------------

johnnycable | 2017-10-11 10:33:05 UTC | #10

@Molurus
What about the ios device logs? Do they report anything on killing your app?

-------------------------

Molurus | 2017-10-12 09:56:14 UTC | #11

Everyone, first of all thanks for all the responses!

Some remarks from my side:

Indeed, the variable numberOfVertices is mis-named. The parameter float[] does contain correct sets of coordinates and normals. (Sets of 6 floats.)

At this point I have no reason to believe that the numberOfIndices ever exceeds 64k. But I will check again to make sure.

Yes, the idea that Garbage Collection plays a role here did occur to me. I've tried to determine if it does, but to no avail. Things I've tried:

- running the garbage collector during OnUpdate() cycle. (Once every 100 cycles.)
- monitoring memory use changes. (No strange things there.)
- using GC.AddMemoryPressure in the hope that natively allocated memory isn't released unpredictably. (This didn't influence the crash behaviour.)

The device logs (thanks for that pointer, hadn't seen those before) contain rather extensive entries, and I'm a bit unsure how to interpret them. There are a few lines that draw my attention:

Edit: log lines removed. I may have been looking at the wrong entry due to confusing order of events in the logs.

I will get back on my analysis of the log entries.

-------------------------

Molurus | 2017-10-12 08:45:55 UTC | #12

Short remark on the basis of the device logs: the log entry I see seems to indicate the app was terminated because it had an average CPU usage over 80% for more than 3 minutes. (84% to be precise.)

This 3 minute period seems consistent with the problems I'm seeing. If I'm interpreting the device logs correctly, the app is killed by iOS on the basis of high CPU usage.

I'm going to google the specific entries to see if this is a known show stopper for apps.

-------------------------

Eugene | 2017-10-12 08:57:03 UTC | #13

[quote="Molurus, post:12, topic:3646"]
This 3 minute period seems consistent with the problems I’m seeing. If I’m interpreting the device logs correctly, the app is killed by iOS on the basis of high CPU usage.
[/quote]

I'm glad to hear that you've got a clue.

-------------------------

Molurus | 2017-10-12 08:59:56 UTC | #14

Me too. Now it's a matter of trying to figure out if it is possible to create a workaround for this. At this point I'm not at all sure if this problem can be fixed in our code, or if it should be fixed in UrhoSharp.

But at least I now have some indication of what's going on!

-------------------------

johnnycable | 2017-10-12 10:56:59 UTC | #15

Yes, CPU Monitor. Since IOS 8.
Time to fire up Instruments and find who's guilty.:wink:

https://developer.apple.com/library/content/documentation/Performance/Conceptual/EnergyGuide-iOS/WorkLessInTheBackground.html

> Resolving Runaway Background App Crashes
> 
> iOS employs a CPU Monitor that watches background apps for excessive CPU usage and terminates them if they fall outside of certain limits. Most apps performing normal background activity should never encounter this situation. However, if your app reaches the limits and is terminated, the crash log indicates the reason for the termination. An exception type of EXC_RESOURCE and subtype of CPU_FATAL is specified, along with a message indicating that limits were exceeded. See Listing 3-6.
> Listing 3-6Example of an Excess CPU Usage Crash Log Entry
> 
>     Exception Type: EXC_RESOURCE
>     Exception Subtype: CPU_FATAL
>     Exception Message: (Limit 80%) Observed 89% over 60 seconds
> 
> The log also includes a stack trace, which lets you determine what your app was doing right before it was terminated. By analyzing the stack trace, you can identify the location of the runaway code and resolve it.
> 
> Note
> 
> CPU Monitor is available in iOS 8 and later.

-------------------------

Molurus | 2017-10-12 12:19:54 UTC | #16

There are continuous rendering cycles going on. I'm trying to pause the engine, by calling UrhoSurface.Pause(), but this doesn't appear to stop OnUpdate() being called, nor does it seem to influence the problem in any way.

I'm not surprised that CPU use is high during rendering, but I seem to be unable to stop the UrhoSharp.Forms from rendering.

Searching further, will keep you updated.

-------------------------

Victor | 2017-10-12 16:31:35 UTC | #17

Just a shot in the dark as a test..., what if you did something like:

void PostUpdate( ... ) {
   Urho3D::Time::Sleep(10);
}

Do you think that would work for you? Or, get you closer to a solution?

-------------------------

Molurus | 2017-10-12 17:29:29 UTC | #18

@ Victor:

This would probably require me calling Time.Sleep(10) from the OnUpdate() function? Otherwise it will just sleep 10 ms and then display the same behaviour again.

I could try calling Time.Sleep(10) from the OnUpdate() when I feel that it shouldn't be rendering at all, but it feels a bit iffy. I will try this anyway tomorrow.

In general, I must say I'm extremely confused by the available functions in UrhoSurface and Urho.Application.

Urho.Application has Start() and Stop() functions, but these don't seem to stop OnUpdate() being called.

UrhoSurface has Pause() and Resume() functions, which don't stop OnUpdate() being called either. (This is really strange imho. If these functions don't stop and resume rendering, do they do anything at all?)

UrhoSurface has a Stop() function, but doesn't appear to have a Start() function. This seems to be intended for application exit, not for a temporary Pause of rendering. So this one isn't useful either it seems.

UrhoSurface has a StopRendering(Urho.Application) function, which *does* stop rendering, but there doesn't appear to be any StartRendering() function that would allow me to resume, which makes it completely useless.

There must be some simple way of temporarily pausing rendering so I can bring down the CPU usage while the user isn't interacting with the model (and start it again when the user wants to interact with the model), but sofar I haven't found it.

Btw, I cannot stress enough how much I appreciate you people trying to help me here. This really is a frustrating problem. I feel like I am really close to a workable solution, yet... I am not quite there.

-------------------------

Molurus | 2017-10-13 08:39:17 UTC | #19

Ok, I have tried Victor's suggestion, having a Time.Sleep(20) call in the OnUpdate() function to reduce the CPU used. (I'm for now not making any attempts to pause rendering and/or load other models and/or handle user interaction. Just displaying a model.)

The good news is that I no longer seem to get crashes related to high CPU use in the sense that I'm simply not getting any entries about it in the iPad device log anymore. (Or entries of any kind.)

De bad news is: the app is still terminating after a few minutes of being idle while displaying a model. (The app does not crash if I don't load any model and just display an empty viewport.)

So yeah.... I'm not sure if I really made any kind of progress here. The only improvement seems that I now don't have any diagnostics information that I could check anymore.

If anyone has other ideas on what I could check further I would be very much interested.

-------------------------

Eugene | 2017-10-13 08:49:46 UTC | #20

Have you tried to run standard UrhoSharp samples?
If they crash too, you could also try our native samples.

-------------------------

Molurus | 2017-10-13 09:34:24 UTC | #21

Ok, I seem to have another lead here. The stability seems related to model complexity.

The models I was trying to load had (roughly) 250,000 triangles. Those tended to crash after a few minutes.

If I limit the loading of these models to 30,000 triangles max, the stability seems to be improving! I've displayed the same model for over 10 minutes without a crash. (Checking if this is ad infinite now.)

Now I'm not exactly sure what a reasonable number of triangles is for a mobile device. The models we're trying to load wouldn't be shocking for a desktop application.

-------------------------

Victor | 2017-10-13 10:01:13 UTC | #22

Ah, nice to hear you've made progress! I must have read the issue incorrectly. This has been an issue for me as well when I was creating a CustomMesh class. For me, it had something to do with the Vertex Buffer, so I did the following in my code:

https://gist.github.com/victorholt/926bdb48f40bb8a27cd613ed8e94fc99#file-custommesh-h-L1-L2

Interesting for large meshes we came up with around the same "max" number of triangles.

-------------------------

Molurus | 2017-10-13 10:02:04 UTC | #23

@ Eugene:

The samples I've seen don't load very large / complex models and tend to be stable. The problems seem to arise when models get larger. (And the time it takes for them to crash seems to have a relation with model complexity.)

I'm currently still looking at the same model for about 20 minutes. Still no crash. (With the number of triangles capped at 30,000.)

Of course this is no real solution yet, we need to be able to display complete models. But at least this is a new lead. Maybe this will trigger someone's intuition as to what might be causing this.

-------------------------

Victor | 2017-10-13 10:40:55 UTC | #24

In my solution above, what I do is just split the larger models, that have reached the max triangles, into their own Vertex/Index buffer. I think that should work for you. Perhaps, the Urho3D exporter could be modified a bit too with dealing with the issue in a similar way, around here:

https://github.com/reattiva/Urho3D-Blender/blob/master/export_urho.py#L858-L862

When I originally looked into this issue, I couldn't find that Urho was doing anything special with OpenGL vertex buffers, so I didn't necessarily think it was an issue with Urho... I could be wrong however.

-------------------------

Molurus | 2017-10-13 10:47:15 UTC | #25

@ Victor:

For clarity, our models are not contained in a single object. The 250,000 triangles I'm referring to are for the complete model.

In other words: the objects within the model each have their own VertexBuffer and are already substantially smaller than 30,000 each.

What I could do is put them in seperate Node objects over a certain threshhold, but I see no reason to believe that would make a difference here.

-------------------------

Eugene | 2017-10-13 11:21:03 UTC | #26

[quote="Molurus, post:23, topic:3646"]
The samples I’ve seen don’t load very large / complex models and tend to be stable. The problems seem to arise when models get larger. (And the time it takes for them to crash seems to have a relation with model complexity.)
[/quote]

I still think that first guess about watchdogs is still valid.
Mb your application it just is too heavy for the device and get killed by OS. You feed one watchfog with sleep but there may be others...

-------------------------

johnnycable | 2017-10-13 12:15:55 UTC | #27

@Molurus
Smells like a limit on opengl model structure, like you were using open gles 2. But since IOS7 it is open gles 3, if I'm not mistaken... which open gl es version urho sharp is using?
Anyway I don't believe to be that... 
Did you check all the background threads? Any of them doing some infinite UI rendering?

-------------------------

Molurus | 2017-10-13 15:17:33 UTC | #28

@ Eugene:

Well, by now I've pretty much stripped everything from the app, so there's very little left that might be taking up too much resources. (At least from our app itself.)

I really don't know what other kind of monitoring I could be doing here.

I'll sleep on this a bit. I am (again) pretty much lost. Reducing the model size / complexity just increases the time it takes for crashes to occur. I'm not at all sure anymore that even simple models are stable. (It might take hours in extreme cases, but that doesn't mean there's no problem.)

-------------------------

Molurus | 2017-10-13 15:18:50 UTC | #29

@johnnycable:

To be honest, I have no idea what version of open gl UrhoSharp.Forms is using.

-------------------------

johnnycable | 2017-10-13 16:58:50 UTC | #30

Does urho sharp prevent [Apple Instruments](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html) from working?

-------------------------

Molurus | 2017-10-26 12:16:08 UTC | #31

It's been a while since I've last researched this problem. I'm currently trying to figure out Apple Instruments and how to use it.

After a few hours of struggling, I finally got my Apple Instruments to attach to my process. Progress, of a kind. :slight_smile:

Now I'm trying to find my way through the templates and trying to figure out which ones may be relevant to my problem. Memory use seems ok, nothing shocking. 500 mb memory use for my app at the moment of crash.

-------------------------

Molurus | 2017-11-03 17:15:32 UTC | #32

Well, some update remarks.

1) I've been looking Apple Instruments... but I'm really unsure what to look at. I see no memory leaks, CPU usage remains high as we might expect from a rendering engine. It's a bit unclear if this is the actual cause of the sudden crashes.

2) I've tried running our App on IphoneSimulator. Not only does the app work on this simulator, it's completely stable. It doesn't crash at all. (Simulator used is iPad 5th generation, iOS 11.)

3) When I run the app on an iPad mini 2 the crashes occur quite quickly. No stack trace, no exceptions, nothing whatsoever.

4) There still is a suspicion that the iPad itself decides to terminate the app based on the CPU load. With that in mind I would like to stop rendering. Yet, I've found absolutely no way of stopping the rendering process. No matter what I try, OnUpdate(float timeStep) keeps getting called continuously.

If anyone has any further ideas.... especially regarding point 4), that would be much appreciated. It seems I'm running out of things to try. :(

-------------------------

johnnycable | 2017-11-03 19:00:32 UTC | #33

1. Any background thread that may cause Ios monitor to trigger.
2. Forget it. You're running on Os X not Ios. It's a simulator, not an emulator. Simply no point. This is renowned.
3. see 1 and 2. Consider your first friend is always XCode. Set breakpoints and check memory usage. Check the ipad logs on device tabs.
4. Don't know, but I'd look for some process spawning too.

-------------------------

Molurus | 2017-11-05 14:54:03 UTC | #34

Hi johnnycable.

1) The app itself is completely stable when I load the entire thing and just don't load any model. (And do load an UrhoSurface object.) There is nothing that runs in the background that is triggered by the loading of the model. Even if there was I wouldn't know how to look for it using Apple Instruments, but it would have to be something that's part of our app regardless if we load a model. At this point, I'm 99% certain the ios monitor is triggered by Urho's rendering engine, nothing else. (Although there doesn't appear to be much I can do to further investigate this.)

2) Ok.

3) Are you aware we're not using XCode at all? We're developing in Xamarin / Visual Studio for Windows. Most of our code is in PCL classes we use for other applications. (Which don't do any threading stuff in the iOS environment, we can pretty much exclude that part.) I do set breakpoints, have the code display current memory use, etc. Absolutely no clues there. Nothing that could explain the crashes, other than iOS killing Urho.

4) How? It appears there simply is nothing left to look at. I could live with temporarily stopping the engine from rendering and restarting it when required, but that seems impossible as well.

At this point I'm beginning to wonder if anyone ever managed to use UrhoSharp on iOS with large models without it crashing. To be honest... I doubt it. And I'm completely unsure if this could be done with different rendering engines without running into similar problems, so I'm not thrilled about trying to re-implement this in other ways either.

But if we don't get *something* working, my company has a huge problem. So we're really quite desperate.

-------------------------

Eugene | 2017-11-05 15:37:02 UTC | #35

Did you tried to build sketch Unity build with the same models, for example?
It shouldn't take a lot of time but could give us a clue.
[spoiler]Or you just drop Urho and switch to Unity if it works[/spoiler]

-------------------------

Molurus | 2017-11-06 08:32:04 UTC | #36

At this point we're so desperate that we might even consider re-implementing something that uses Unity.

But as I understand it, Unity doesn't work with Xamarin. So even if I could get this to work, what good would it do?

The only path I can think of that might stand a chance of solving our problem is one of two options:

1) somehow reducing the frame rate and thus reduce the CPU load.
2) stopping rendering altogether when it's not required.

If there is any way of doing this with UrhoSharp, I'd love to know about it.

-------------------------

johnnycable | 2017-11-06 10:20:03 UTC | #37

Oh, oh... I didn't got that.

Now googlin I see what's your real problem...

https://stackoverflow.com/questions/41930969/export-xcode-project-from-xamarin-project

you can't even export a project, cannot open anything with xcode. :crazy_face::crazy_face::crazy_face:
you're completely bound into Microsoft cage... :tired_face::tired_face::tired_face:
The reason why we guys here use much more setup-complicated open source effort-prone urho3d for c++; because we can solve error ourselves, without recurring to Microsoft support (they won't answer us anyway, unless we are fortune 500 :stuck_out_tongue_closed_eyes:)

(did you used Instruments with the device, not emulator, didn't you? just for the luck of it)

So, to recap, you have a threefold problem:

1. At the lowest level, it's possible urho3d renderer doesn't work.
2. At the intermediate level, xamarin bindings for urho 3d don't work.
3. At the highest level, xamarin.ios doesn't work.

Without using Instruments or Xcode we are clueless. But, I don't know why, I would bet on 2...:wink:

Consider those frameworks are beefed up for 2d business presentations... xamarin first worry is to let their customers build beautiful 2d UIs for selling shoes... they don't care a fuck about videogaming, which is 5% of their user base... they wanted urho sharp in just because Unity didn't want to sell to them... :wink:
So to reply about

[quote="Molurus, post:34, topic:3646"]
At this point I’m beginning to wonder if anyone ever managed to use Urho Sharp on iOS with large models without it crashing. To be honest… I doubt it.
[/quote]

I doubt anyone ever used it... UrhoSharp is dead. So is Atomic. No need to tell you your error was getting on the toughest platform last. You always need to test continuously on mobile, as features deployment go on... 

If your codebase is C#, maybe you could port to Godot. Now it has a C# bindings (paid by Microsoft, just to let you know) https://godotengine.org/article/introducing-csharp-godot. Of course, it's a move of last resort.

But what about xamarin builtin debugger? https://developer.xamarin.com/guides/ios/deployment,_testing,_and_metrics/debugging_in_xamarin_ios/
That's what you should use for first...

-------------------------

Molurus | 2017-11-15 08:44:44 UTC | #38

Another small update. We've re-implemented the viewport in a separate app to exclude any kind of external influences from other code. The effect remains the same.

What is interesting: I've managed to reduce the frame rate to 10 FPS, but this doesn't appear to affect the problem at all. It crashes just as quickly. (Default MaxFPS = 60. With our model it produces 30 FPS. But when I reduce the frame rate to 10 FPS it still crashes. That's.... odd.)

-------------------------

johnnycable | 2017-11-15 10:11:10 UTC | #39

If you post the model,  I can try give it a run on my ipad on ios 10. I have a couple of fast project scaffolding scripts, so it doesn't take me much to set it up on Os X and Ios. 
I can run it by simply inserting the model into a new scene in Urho.
And post your ios crash log, too.

-------------------------

Molurus | 2017-11-15 16:37:47 UTC | #40

Ok... this is very interesting. I'm sure the developers of Urho3D will agree....

We just succeeded in loading our entire model and have it completely stable!

IFC models have geometry objects of various different (pre-defined) types. There are 11 different types we're displaying in our Viewport.

The IFC model we're trying to display contains 1864 objects in total.

Now what we did before was create separate Urho.Model objects for each of the objects in the IFC model, which seems the logical thing to do.

In an effort to solve our problem, we tried grouping these objects based on IFC type. So what we did was create an Urho.Model object for each of the IFC types, so that's only 11 Urho.Model objects.

And what do you know? This helps!!

The one thing we have to solve now is being able to select elements in the model we truly want to be able to select. Selectable objects are probably going to require having a separate Urho.Model object. But this is something we may be able to fix in a generic way, we're currently investigating this.

So the conclusion: the problem isn't related to model complexity per se. It's related to the number of Urho.Model objects.

@ Johnnycable: thanks for the offer, it seems your help is no longer required. :)

-------------------------

Eugene | 2017-11-15 17:57:54 UTC | #41

[quote="Molurus, post:40, topic:3646"]
It’s related to the number of Urho.Model objects.
[/quote]

So strange. Processing 2k objects shan't be very CPU-consuming.
Do you have any changes in resource metrics? Profiling, smth else...

-------------------------

Molurus | 2017-11-15 18:17:22 UTC | #42

@ Eugene:

There are absolutely no changes in resource metrics as far as I can tell, no. I haven't really profiled it again with Apple Instruments though.

There is another remarkable difference: the model seems to load quite a bit faster than it did before. I'm not quite sure if the frame rate is better too, I will check this tomorrow.

No other changes to our software either. It's completely the same code, except the changes required to group the geometry into fewer Model objects.

Right now I'm thinking this isn't a resource thing. Which was also indicated by the fact that lowering the frame rate doesn't affect the problem at all. This is very suspicious, imho.

I'd say it's a bug in the Urho3D engine that doesn't respond well to a large number of Model objects running on iPad in a Xamarin.Forms application. That's as specific as I can make it right now.

Specific enough for what we want to do with it. But this may be worth looking into for the developers of Urho3D.

-------------------------

esakylli | 2017-11-16 18:56:39 UTC | #43

It would be interesting to know if the problem lies in core Urho3D or in UrhoSharp (Xamarin).
Maybe you can post this thread to the xamarin forums (UrhoSharp) also, and ping EgorBo to take a look at it (but I think he would need a reproducable sample)?

-------------------------

Molurus | 2017-11-21 08:36:41 UTC | #44

I cross posted this solution to the UrhoSharp forum and tagged EgorBo, but I'm getting no response there at all.

Meanwhile we've managed to do selection on sub-geometries of Model objects. So it seems our problem is now completely solved!!!

This has taken us a lot of time. But I'm happy to say: we finally did it! We have a complete working solution. It still feels like a workaround, but we can do everything we want to do with this.

Thanks for everyone who has brought input here. Much appreciated!


Best regards,

Molurus

-------------------------

Eugene | 2017-11-21 08:52:38 UTC | #45

Good luck with your project, @Molurus

-------------------------

