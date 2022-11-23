I3DB | 2018-12-20 15:50:30 UTC | #1

 On some models, for instance these 

https://github.com/xamarin/urho-samples/tree/master/SamplyGame/Assets/Data/Models

When executing the line:

var player = ResourceCache.GetModel("Models/Player1.mdl"); an exception is thrown whereas the model can't be found, but the file is clearly there. 

Yet the code:
var plane = ResourceCache.GetModel("Models/Plane.mdl"); will work fine.

Opening the files in Blender doesn't provide any useful info (that I can glean).

How can this be troubleshooted further?

When I run the Samply game as a Windows Forms app it runs fine and the models are found.

When I run this as a StereoApplication with UrhoSharp, some of the models are not found. Teapot.mdl is another that can't be found.

My dev environment is c#.

-------------------------

Modanung | 2018-12-20 11:32:59 UTC | #2

Did you add all resource folders by means of engine parameters?

-------------------------

I3DB | 2018-12-20 14:12:56 UTC | #3

Yes, can load the basic models in the resource folder. Here's how it's specified:

    internal class Program
	{
		[MTAThread]
		static void Main() => CoreApplication.Run(new UrhoAppViewSource<QuantumRoq>(new ApplicationOptions("Data")));
	}

The model and all associated files when taken from here, as an example, load fine:
https://github.com/xamarin/urho-samples/tree/master/HoloLens/06_CrowdNavigation/Data

So the mutant model, works with all animations running error free.

But none of these will load, except Box and Plane:
https://github.com/xamarin/urho-samples/tree/master/SamplyGame/Assets

When attempting to load teapot.mdl or any of the non-baisic, throws this exception:
Could not find resource models/Teapot.mdl. You can omit this exception by subscribing to Urho.Application.UnhandledException event and set Handled property to True.
ApplicationOptions: args -w -nolimit -x 1268 -y 720 -p "CoreData;Data" -touch -hd -landscape -portrait 

However, the Sounds, as an example, do work when used. Also can load the materials. No models, no particles will load.

So the resource folder is mapped, else Sounds and the other working models wouldn't be loaded.

If I had the C++ environment up and running, it would be rather simple to debug and step right to the issue. But much of what's happening is hidden when using UrhoSharp. So trying to figure out how to troubleshoot such issues.

I've not got any experience with Blender or the asset importer, so don't know if there is something in the format of the models, or something in the import that keeps them from working correctly.

-------------------------

I3DB | 2018-12-20 14:26:29 UTC | #4

Another example of a model failing to load is the SphereVCol.mdl from this folder:
https://github.com/xamarin/urho-samples/tree/master/FeatureSamples/Assets/Data/Sample43

But most of the materials do work, water doesn't though, but no errors are thrown when loading the water material, it's just not displaying properly.

-------------------------

I3DB | 2018-12-20 15:50:40 UTC | #5

Ok, have realized the underlying problem. The files really are not being found, and when models such as Plane or Box that are part of CoreAssets, it would appear the models are being taken from CoreAssets, and not the 'Box.mdl' file.

What I found is when the app is compiled by Visual Studio, the .mdl files were not being included in the Data folder that is uploaded to the device. When I manually copy the files after compilation, but before upload to the device, all works fine.

Some of the files such as the Mutant.mdl, are included in the Data folder.

So this isn't an Urho related issue at all, but something with the files on my Windows OS system (probably unzipped from a blocked zip file or something like that). The Urho Exception thrown is correct, the files really are not there.

-------------------------

