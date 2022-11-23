Jimmy781 | 2017-01-05 23:51:06 UTC | #1

Hi , 

I'm trying to populate my scene from my page after it has been created but i'm getting the above error.
This is for android , it works on Ios

    01-05 18:45:19.139 E/Urho3D  (32719): Sending events is only supported from the main thread
    01-05 18:45:19.139 E/Urho3D  (32719): Sending events is only supported from the main thread
    01-05 18:45:19.139 E/Urho3D  (32719): Sending events is only supported from the main thread
    01-05 18:45:19.139 E/Urho3D  (32719): Attempted to get resource Models/Box.mdl from outside the main thread
    01-05 18:45:19.149 E/Urho3D  (32719): Attempted to get resource Materials/Stone.xml from outside the main thread


Any idea how to add items to my scene after it has been created ?

`urhoApp?.addItem(urhoval);`

In my urho App :

    public void addItem(string p)
            {

                modelNode2 = scene.CreateChild(p);
                modelNode2.Position = new Vector3(5.0f, 1.0f, 5.0f);

                modelNode2.SetScale(10.0f);

                var obj2 = modelNode2.CreateComponent<StaticModel>();
                obj2.Model = ResourceCache.GetModel("Models/Box.mdl");
                obj2.SetMaterial(urhoAssets.GetMaterial("Materials/Stone.xml"));
            }

-------------------------

hdunderscore | 2017-01-06 02:35:03 UTC | #2

Duplicate topic again:

http://discourse.urho3d.io/t/urhosharp-add-object-on-scene-after-urhosurface-created/2672

Anyway, in your other topic you were using tasks which is probably why there were errors. Does the modified version above still give errors?

-------------------------

Jimmy781 | 2017-01-06 02:55:29 UTC | #3

@hdunderscore , yes the issue still persists (same error)

-------------------------

hdunderscore | 2017-01-06 03:19:40 UTC | #4

You'd probably need to share more code. Did you try set up threaded code elsewhere?

If this was an UrhoSharp or C# specific issue, the correct place to ask would be the UrhoSharp Xamarin forums. I suspect in this case it's a simple matter though.

-------------------------

Jimmy781 | 2017-01-06 03:26:02 UTC | #5

@hdunderscore

I think it has something to do with this :
https://urho3d.prophpbb.com/topic1753.html  


The thing is that it works on iOS , but not on Android

-------------------------

cadaver | 2017-01-06 09:34:18 UTC | #6

From Urho library's point of view, the C++ main thread is started in a cross-platform way by the URHO3D_DEFINE_MAIN macro in Core/Main.h. From within this thread, event / scene / resource access is safe. On iOS or Emscripten the rest of the application actually happens from within a frame or animation callback, but that too is considered the main thread.

My guess is that the UrhoSharp Android activity events are running on another thread, and therefore it cannot behave as if it was the main. Fixing this is outside the scope of the Urho project; UrhoSharp should be providing the required safe access to the actual Urho main thread.

-------------------------

Andre_B | 2017-01-06 13:44:46 UTC | #7

The way we use Urho in android, every button or any UI call that wants to mess around with Urho, either creating a new object or clearing the resource cache when the app exits, runs inside the main Update loop. 

Something like this:

    Update()
        ....
        foreach(Action a in actionQueue)
        {
           run(a);
        }
        //Do whatever you want after
        ...
   


Our player has a queue of actions that are run inside our update loop. And every time the UI wants to do any action these get added to an action queue.

DoStuff()

    actionQueue.Enqueue(() =>
	{
				InitInternal();
	});


Now there might be other ways to do this, but this way we have done it.

-------------------------

