CodeCrafty | 2019-07-22 22:18:00 UTC | #1

I really need to add a model to my scene that I download from our server at runtime.
Getting the file over the net is easy... HTTP Get etc.

Now how do I get the resourcecache to load it?? 

Tried lots of stuff with MemoryBuffer but no luck 8( 
Also tried writing to mass storage but again no Bueno...

Might have found a happy path... I'll post the results for all once confirmed and cleaned up.

-------------------------

Modanung | 2019-07-23 01:14:35 UTC | #2

Maybe `Resource::LoadFile` and then `ResourceCache::AddManualResource`?
I have not tried this.

-------------------------

SirNate0 | 2019-07-23 15:40:32 UTC | #3

Make sure you set the (file?) name on the resource before adding it as a manual resource. What's happening when you try using the MemoryBuffer?

-------------------------

TheComet | 2019-07-23 16:15:07 UTC | #4

Probably stating the obvious here but the standard way to do this is through [Scene::AddRequiredPackageFile](https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_scene.html#adb229515c3873cb6dbafe3ac58ab2053) and [Network::SetPackageCacheDir](https://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_network.html#a57b30be42b797f89acad15c24e5adcfe).

Is this not possible in your situation?

-------------------------

CodeCrafty | 2019-07-23 22:42:42 UTC | #5

[quote="TheComet, post:4, topic:5321"]
us here b
[/quote]

That sounds like what I should explore... but here's our hacky 'working' version as we spike this functionality:
```
        public Model LoadModel()
        {
            var _model = scene.GetComponent<StaticModel>(true);

            try
            {
                // This mimics the bytes we will get from the server
                var file = ResourceCache.GetFile("Models/Sphere.mdl");
                byte[] fileBytes = new byte[file.Size];
                file.Read(fileBytes, file.Size);

                //This is stuffing it into the Urho system as if we got it off the network etc...
                MemoryBuffer buff = new MemoryBuffer(fileBytes);
                _model.Model = new Model();
                _model.Model.Load(buff);
            }
            catch (Exception ex)
            {
                System.Console.WriteLine(ex);
            }

            return _model.Model;
        }
```
You'll notice it's C# and I've already read that this is not the C# forum but there is no other documentation for us-- it is just a thin wrapper to the same bits covered in this forum. 
So it's what I have to work with, ya know?
Someday you guys may need to do a Xamarin thing, I'll be glad to help with the various gotchas I have encountered.

-------------------------

Modanung | 2019-07-23 22:46:35 UTC | #6



-------------------------

