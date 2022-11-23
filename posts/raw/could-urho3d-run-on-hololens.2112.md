larsonmattr | 2017-01-02 01:13:10 UTC | #1

The Microsoft Hololens is an augmented reality device that can display 3D objects as if they were physical objects.  Currently there is support to deploy Unity3D UWP programs to the Hololens, but no other available 3D engines.  How difficult would it be to use Urho3D with the Hololens?

There was a prior thread with users experimenting with deploying Urho3D as a UWP application.  It sounded like a successful effort sans mixing with XAML UI.  The hololens requires UWP support, and additionally supporting the Hololens library for interacting with the mesh of the environment & probably for gestures.

The Hololens is an x86 device, ~1 gigahertz cpu.  It has a limit of ~150,000 triangles max for good performance and suggested basic textures/illumination.

Any thoughts on how I could start experimenting along creating and deploying as a UWP application for the Hololens?

-------------------------

Egorbo | 2017-01-02 01:13:11 UTC | #2

I've just managed to launch Urho3D (C++) in 2D mode (UWP) on HoloLens emulator:

[img]https://habrastorage.org/files/168/78f/ad2/16878fad2e3c4d0ba766e0d91e59811e.png[/img]

I'll send a PR soon.

-------------------------

larsonmattr | 2017-01-02 01:13:11 UTC | #3

@Egorbo

 Good news, thanks for working on this and the PR.

-------------------------

Vincentwx | 2017-01-02 01:13:15 UTC | #4

@Egorbo, I am just wondering if you will do an C# binding wrapper.

-------------------------

larsonmattr | 2017-01-02 01:13:18 UTC | #5

It looks like the work on Urho3D & UWP is happening on the UrhoSharp (xamarin/urho) project.  EgorBo has been building on a branch there ([github.com/xamarin/urho/tree/uwp](https://github.com/xamarin/urho/tree/uwp)).  

@EgorBo
For us non-C# people, what is the best way to get the UWP code into urho/urho3D?  What is the relationship between the urho/urho3d and xamarin/urho projects?  Does the xamarin codebase push changes back to urho/urho3D?

-------------------------

Egorbo | 2017-01-02 01:13:18 UTC | #6

[quote="larsonmattr"]It looks like the work on Urho3D & UWP is happening on the UrhoSharp (xamarin/urho) project.  EgorBo has been building on a branch there ([github.com/xamarin/urho/tree/uwp](https://github.com/xamarin/urho/tree/uwp)).  

@EgorBo
For us non-C# people, what is the best way to get the UWP code into urho/urho3D?  What is the relationship between the urho/urho3d and xamarin/urho projects?  Does the xamarin codebase push changes back to urho/urho3D?[/quote]
The screenshot above is C++ UWP. I had to rewrite UWP SDL and now I am trying to figure out how to merge it with urho3d cmake system.

-------------------------

AlCaTrAzz | 2017-01-02 01:13:23 UTC | #7

would be very interested to see how this works out, is it very different to getting it to work on VR?

-------------------------

