Jimmy781 | 2017-01-03 18:31:01 UTC | #1

Hey guys , 

I created a XF and Urho sharp application . 

I added the "Data" folder in Android->Assets , iOS ->Resources

It works well in android and the models load in iOS , however the images don't load in iOS.

`plane.SetMaterial(Material.FromImage("image.png"));`

The image is located in the Data folder . It works in android but for iOS - i get a black plane

Any idea how to fix it ?

* The image is set as BundleResource in the iOS project

-------------------------

Andre_B | 2017-01-05 18:46:39 UTC | #2

In IOS every texture needs to have a power of two resolution, like 256/256 or 512/512.

Check if that is the issue.

Additionally check that your using the latest UrhoSharp version, a lot of exceptions are thrown now that weren't before.

Like missing resources, shader compilation errors among other things.

-------------------------

artgolf1000 | 2017-01-05 18:46:37 UTC | #3

Sometimes the issue was caused by the filename, 'image.png' and 'image.PNG' are different files on iOS device.

-------------------------

