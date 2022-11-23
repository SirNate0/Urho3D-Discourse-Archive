furkansarihan | 2019-02-13 09:22:51 UTC | #1

Hello forum. 

I am developing a Xamarin application with Urho3D. Can someone guide me to level design tool? So I will be able to export my scene from it.

I found a material graph editor with binary disturbition and it comes with urho renderer and works. But I think it was not official and It is not enough for me.

I could not complete Urho3D installation from source code. Is there any other way to launch Urho3D?

Note: I don’t have complex scene, there is just some bunch of models and materials.

Thanks.

-------------------------

smellymumbler | 2019-02-12 20:08:05 UTC | #2

You probably want to ask here: https://github.com/xamarin/urho/issues

-------------------------

glebedev | 2019-02-13 22:47:48 UTC | #3

Hey.

I made the material editor. The source code of the editor is on GitHub. It's incomplete (missing hlsl generator) and there are few issues. But at least it's useful for prototyping.

You can download binaries of Urho3D from https://sourceforge.net/projects/urho3d/files/Urho3D/1.7/

If you need UrhoSharp binaries you can get them via nuget.

-------------------------

glebedev | 2019-02-14 16:44:08 UTC | #4

Also I have plans to start a UrhoSharp version of the editor. FYI.

-------------------------

I3DB | 2019-02-14 16:59:32 UTC | #5

How will this differ from the current editor?

And why UrhoSharp and not, for example to ask this question, a c# implementation like https://github.com/rokups/rbfx ?

I use urhosharp by the way, and use only code, haven't used the editor for any object or scene creation.

-------------------------

glebedev | 2019-02-14 17:17:42 UTC | #6

The difference is that I'll do a nuget package that you can use to build an editor for your particular game. Kind of a building block for editor + default implementation.

I'm not familiar with rbfx.

-------------------------

I3DB | 2019-02-14 19:34:32 UTC | #7

I'm not that familiar with rbfx either, but it seemed @Egorbo was warming up to it due to the complexities the SDL updates added to his methodology for creating the current version of Urhosharp, if he upgrades the fork of Urho3D to use the latest SDL updates.

But anyway, looking forward to trying out your urhosharp editor. 

One of the issues I had running urhosharp on a hololens was when loading scene files urhosharp fails. For instance on the PBRMaterials scene, I had to manually edit the scene file to comment out the initial scene and just load the nodes.

Taking a look at one of @Egorbo 's samples where it looks like he used the editor, he has two scene files.

[The first wraps all the nodes in a scene, the second file just has nodes.](https://github.com/EgorBo/SimpleUrhoRoomScene/tree/master/Assets/Scenes)

That scene file is the one loaded by stereo applications, [as shown here.](https://github.com/EgorBo/SimpleUrhoRoomScene/blob/d023ffca76f0e83708e2ce9055da077b0d8db65f/SimpleUrhoRoomScene.MixedRealityPortal/Program.cs#L44)

Pointing this out because if the editor handled that (maybe it does already), it would be a nice feature to be able to export the scene and not have to manually modify it for a stereo application.

He also still loads it to the scene, and I load it to a child using code like this:
```
node.LoadXml("Data/Scenes/PBRHoloExample.xml");
```

[I learned about rbfx from this thread](https://discourse.urho3d.io/t/net-bindings-for-urho3d/4119).

-------------------------

glebedev | 2019-02-14 20:15:29 UTC | #8

Actually @Egorbo may change how stereo application works soon. I hope so...

-------------------------

furkansarihan | 2019-02-15 13:22:03 UTC | #9

@glebedev I really like the material graph editor, but sadly I am not a materail artist yet :frowning: (out of topic) Is there any source for rapid learning about designing materials ?

Also I am waiting for development news for Editor for UrhoSharp. Will it be on github ? and I am curious about How renderers genereliased for multiplatform. Thanks.

-------------------------

Modanung | 2019-02-15 19:41:51 UTC | #10

[quote="furkansarihan, post:9, topic:4915"]
Is there any source for rapid learning about designing materials ?
[/quote]

I'd say it depends on the model and art-style how you create the textures for your materials. There's many approaches and techniques you could consider and combine. If you intend to draw (parts of) your textures on the computer - and you're not making pixel-art - I would advise you to obtain a [graphics tablet](https://en.wikipedia.org/wiki/Graphics_tablet).

-------------------------

