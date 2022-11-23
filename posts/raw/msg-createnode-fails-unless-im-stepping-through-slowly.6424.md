SeanV | 2020-10-10 04:11:51 UTC | #1

I'm working on a networked application in which `MSG_CREATENODE` works in most cases, except when the server moves an object from a non-networked scene into the networked scene. The server sees nothing wrong, but the client appears to corrupt the network message. StaticModel's "Material" attribute sees an array of 10238 elements with resource names such as "`Yj„`" and "`ÿeo/õ…`" The next component creation fails with "`Could not create unknown component type CCCCCCCC`".

I've recently discovered that if I step slowly through the client's `component->ReadDeltaUpdate(msg)` while processing the `MSG_CREATENODE` message, when I'm done stepping through `Connection::ProcessSceneUpdate` the entire node successfully appears in the client's scene.

What could cause symptoms like this? I might guess that stepping through changes the speed and possibly order of received network packets... but I've had a previous attribute corruption error that turned out to be caused by calling `RegisterObject(context)` on a component more than once so I'm afraid it could be anything and thought it would be best to reach out and see if anyone has seen this before.

-------------------------

SirNate0 | 2020-10-10 04:33:57 UTC | #2

I can't comment on the rest of it, as I've not used the networking stuff yet, but the `unknown component type CCCCCCCC` looks like uninitialized stack memory, assuming you're on Windows.
https://stackoverflow.com/questions/127386/in-visual-studio-c-what-are-the-memory-allocation-representations

-------------------------

Miegamicis | 2020-10-10 11:16:41 UTC | #3

What urho version are you using? I did some updates regarding network packet optimization a while ago. Basically it sent out updates in chunks to get linear network load when client count increases. I'm pretty sure there shouldn't be a problem with that, but can check this in the evening.

-------------------------

SeanV | 2020-10-10 18:52:38 UTC | #4

We're using 1.7, we made a fork on Nov 03 2018.

-------------------------

Modanung | 2020-10-10 21:26:41 UTC | #5

You may want to consider syncing.

And maybe you made changes that would make for some nice PRs?

-------------------------

SeanV | 2020-10-11 02:05:36 UTC | #6

I would love to sync but our team only has a rudimentary understanding of git and CMake; Our fork was done "manually." We have someone focusing on learning those skills now.

Three of us, experienced with code but unfamiliar with traditional workflows, have spent months searching through documentation in order to get our project to generate and build properly but if someone has a guide to recommend we would love to continue learning. I personally remember many years of programming classes where we learned all about coding with not a single consideration of where the code gets typed into and how it becomes an application.

On a similar note, we do have some improvements and additions, such as Python integration and OpenVR support as seen in [this post](https://discourse.urho3d.io/t/shadows-do-not-render-on-more-than-one-render-texture-using-hwdepth/3457), but as seen [here](https://discourse.urho3d.io/t/openvr-render-to-the-framebuffer/2107/9) and [here](https://github.com/urho3d/Urho3D/issues/1956#issuecomment-325885456), git and CMake has been our issue.

-------------------------

