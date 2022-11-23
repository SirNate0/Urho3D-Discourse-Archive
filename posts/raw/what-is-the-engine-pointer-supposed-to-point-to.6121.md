archwind | 2020-04-26 03:03:06 UTC | #1


[code]

IntPtr handle = new IntPtr (????);
Engine engine = new Engine(handle); -- throws a null pointer assignment;

[/code]
 What is the context to point to? It obviously does not return a pointer to itself which I made that assumption.

-------------------------

JTippetts | 2020-04-26 10:53:04 UTC | #2

Subsystem objects such as Engine take a pointer to a Context object, ie:

    SharedPtr<Context> ctx(new Context());
    SharedPtr<Engine> eng(new Engine(ctx));

You can take a look at how Application.h defines [URHO3D_DEFINE_APPLICATION_MAIN](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Engine/Application.h#L73) for how it's done for the samples and Urho3DPlayer application.

Edit: fixed

-------------------------

archwind | 2020-04-26 05:00:24 UTC | #3

Oh, Okay it needs a pointer not returning one. Thanks!

Always fun in C# BTW. :)

-------------------------

archwind | 2020-04-27 11:36:44 UTC | #4

Okay. I have it working now. Thanks @JTippetts  

My current project here. Once I get the engine up and going 100% I'll fixed the mess there.

https://github.com/dmacka/MultiverseClientServer

-------------------------

