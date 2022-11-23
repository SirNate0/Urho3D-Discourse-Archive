btschumy | 2020-11-10 16:47:36 UTC | #1

This question pertains to using ResourceCache.GetTempResource() from C#.  Even though you all work with the C++ version, I'm hoping you can shed some light on this.

I've recently realized that if you modify a resource obtained from the ResourceCache using something like:

> component.Model = ResourceCache.GetModel("Models/UVSphere.mdl");

and then modify it, others that get the same thing from the resource cache will also get that change.

So I need to get a unique copy.  

It seems one possible solution is to use Clone() after getting the resource, but for some reason, Clone() is giving me grief on Windows in UrhoSharp.  I suspect it has do do with the thread it is called on and it is going to be a big change to invoke this on the Urho thread.

The other possibility is to use GetTempResource.  

> component.Model = (Model)ResourceCache.GetTempResource(Model.TypeStatic, "Models/UVSphere.mdl", false);

This will be easier to implement, assuming it works, but the above code throws a class cast exception saying the Resource returned can't be cast as a Model.  Can anyone explain how this should be used?

Thanks

-------------------------

Eugene | 2020-11-10 20:47:17 UTC | #2

On C++ side GetTempResource returns owning pointer of the same type as GetResource. My best guess is that you have incorrect bindings that destroy object before you even get it.

Clone returns owning pointer as well, so your issue with Clone and with GetTempResource might be actually the same bug.

-------------------------

btschumy | 2020-11-10 21:16:34 UTC | #3

I thought perhaps my problems with Clone() were due to not calling it on the "main" thread.  It is not totally clear what the main thread is in the UrhoSharp context.  I've tried calling the code that uses Clone() from the true main thread of the application, from the Urho3D update thread that is called before drawing, and from the application's event thread.  In all cases it crashes with:

> **System.AccessViolationException:** 'Attempted to read or write protected memory. This is often an indication that other memory is corrupt.'

I have been programming for about 40 years now.  Using UrhoSharp has been the most frustrating project I've ever been involved with.  I did finally connect with the project manager and he confirmed that there will be no further development of it so it really is dead.  I can't make any more progress as it is.

I think I will connect with the rbfx folks and see if I can become involved in their C# bindings project. I know it is in the experimental phase, but perhaps I can either help or at least be a test case for them.  I was hoping to have this app released by end of year, but I will now have to rethink it and it will be done whenever it is done.

-------------------------

btschumy | 2020-11-14 23:41:37 UTC | #4

I've done some more searching and rbfx is not ready yet for what I need it for.  There really do not seem do be any alternatives I can find to do what I need.  

1. I might try cloning the UrhoSharp project and see if I can figure out why Clone() is crashing.

2. Is there another way to load resources that doesn't use the ResourceCache?  If I could use that then I wouldn't need Clone() or LoadTempResource().  I would like to be able to load a resource and get an exclusive copy.  If I load it again, I need another copy.

-------------------------

SirNate0 | 2020-11-15 15:07:46 UTC | #6

You can just create the resource directly using `new` and then load from the file directly. If you want, you can probably also use the resource cache to get the file, and then load from that, though you might end up with a similar issue with the returned SharedPtr<File>.

-------------------------

btschumy | 2020-11-15 19:46:59 UTC | #7

Ah, that must be how I used to do it.  I remembered another way but couldn't come up with it.  I will try this on Monday.

I suspect that a number of my issues may be due to modifying a shared copy of a resource and not realizing that all users of the object will get the last modifications, regardless of what they previously set it to.  We'll see,

-------------------------

btschumy | 2020-11-16 15:52:23 UTC | #8

Using the LoadFile() function, I'm getting an exception saying the file couldn't be found.  I am specifying the same relative path that works with ResourceCache.

			component.Model = new Model();
			var success = component.Model.LoadFile("Models/UVSphere.mdl");

The file Models/UVSphere.mdl is located in the Urho resource directory I specify upon startup.  Do I need to give a full path name here?

-------------------------

btschumy | 2020-11-16 16:06:35 UTC | #9

Looks like you might need to specify the path relative to the executable's directory.  If I use "UrhoData/Models/UVSphere.mdl" then I no longer get a file not found error.  I get "true" returned from LoadFile().

However, even though there is no error, I don't get the model drawn.  Is there some other initialization I need to do that ResourceCache does automatically?

-------------------------

btschumy | 2020-11-16 16:33:10 UTC | #10

And examining the Model object, it seems to be the same whether it is loaded from the ResourceCache or via LoadFile().  Same number of vertices, same memory usage, same bounding box.  There must be some subtle difference that is causing one to work and the other not.

-------------------------

btschumy | 2020-11-16 17:13:48 UTC | #11

OK, I got it to work, but I really don't understand why my original attempt fails.  Initially I created a new Model() and assigned it to component.Model.  Then I referenced the model via component.Model to do a LoadFile and ConvertToWireframe.  This doesn't work.

However, if I create the new model, assign it to a local variable, use the local variable for the LoadFile and ConvertToWireframe, and then finally assign it to component.Model, that works!

Anyone know why this would be?  If useLocalVariable is true, it works.  If false, it doesn't.  Am I making some stupid error here that I'm missing?

			var useLocalVariable = true;
			if (useLocalVariable)
			{
				var model = new Model();
				var success = model.LoadFile("UrhoData/Models/UVSphere.mdl");
				ConvertToWireframe(model);
				component.Model = model;
			}
			else
			{
				component.Model = new Model();
				var success = component.Model.LoadFile("UrhoData/Models/UVSphere.mdl");
				ConvertToWireframe(component.Model);
			}

-------------------------

btschumy | 2020-11-16 17:43:43 UTC | #12

The only explanation I have of this behavior is that there is a setter for the assignment of the component's Model.  The setter must cache something that doesn't get updated with later modifications of the model.

The take home message is to assign the Model after all modification to it are done.

-------------------------

btschumy | 2020-11-16 18:33:59 UTC | #13

And then my (hopefully) final question on this subject...

Most of the models (and other resources) I use are standard and not something I've added.  For example:

			var component = thickDiskStructureNode.CreateComponent<StaticModel>();
			component.Model = CoreAssets.Models.Sphere.Clone();

Clone here is crashing, but I need a unique copy of the sphere model.  Can I do this using the same LoadFile() mechanism?  From what I can see there is no Sphere.mdl in the file system that is part of Urho3D.  How can I get a unique Sphere?

-------------------------

SirNate0 | 2020-11-16 19:34:45 UTC | #14

Those "standard" models are something UrhoSharp added, to the best of my knowledge they don't exist in Urho (unless they're just a wrapper for loading the Sphere.mdl that Urho3D does come with). I would suggest either downloading the Sphere.mdl from github [here](https://github.com/urho3d/Urho3D/tree/master/bin/Data/Models), or creating your own using the AssetImporter and/or the Blender exporter.

I have no idea why your having those issues, but I suspect that it has something to do with the UrhoSharp bindings. What happens if you instead do the following:
```
var model =  CoreAssets.Models.Sphere;
var newModel = model.Clone();
component.Model = newModel;
```

Also, note that `component.Model` is also an UrhoSharp specific thing, though it's probably just a wrapper for Get/SetModel.

---
[quote="btschumy, post:8, topic:6517, full:true"]
Using the LoadFile() function, I’m getting an exception saying the file couldn’t be found. I am specifying the same relative path that works with ResourceCache.

```
		component.Model = new Model();
		var success = component.Model.LoadFile("Models/UVSphere.mdl");
```

The file Models/UVSphere.mdl is located in the Urho resource directory I specify upon startup. Do I need to give a full path name here?
[/quote]
This is expected. The ResourceCache is what handles the resource directories and looking for the files in them, all of the other file operations not done through the resource cache won't use the resource directories.

-------------------------

btschumy | 2020-11-16 20:13:02 UTC | #15

Ah, I didn't realize those "standard" models were only UrhoSharp.  Yes, I can certainly make my own Sphere.mdl and place it in my resources.

As far as I can tell, anytime I use Clone() on a model, the app crashes.  The UrhoSharp bindings may just be doing something wrong here.  I have toyed with the idea of cloning the UrhoSharp project and trying to fix some of these things myself.  Then I would build with my local copy.

Thanks again for your excellent help.

-------------------------

Eugene | 2020-11-16 20:15:58 UTC | #16

[quote="btschumy, post:15, topic:6517"]
I have toyed with the idea of cloning the UrhoSharp project and trying to fix some of these things myself
[/quote]
I hope you have Mac because UrhoSharp can be built (to be precise, binding generation phase) only on OSX.

However, you should be ok if you are ready to patch bindings manually.

-------------------------

