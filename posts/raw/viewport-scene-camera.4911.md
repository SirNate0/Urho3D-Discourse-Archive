socrobot | 2019-02-12 09:54:49 UTC | #1

The camera has a owner scene as follow:
     cameraNode = scene_.CreateChild("Camera");
    cameraNode.CreateComponent("Camera");

But the when create viewport,It need pass scene & camera as follow:
   Viewport@ viewport = Viewport(scene_, cameraNode.GetComponent("Camera"));

if I use another scene with the same camera : Viewport@ viewport = Viewport(sceneTest, cameraNode.GetComponent("Camera"))
it still work! 

So I wonder whether the camera has only one scene binding?

-------------------------

Leith | 2019-02-13 05:37:57 UTC | #2

The camera binding to the viewport is one-directional binding, which means that yes, cameras can be attached to more than one viewport ... when we create a camera component, the engine internally wraps that object in a SharedPtr, which means it should be safe to destroy a scene containing a shared camera object, given that SharedPtr is a reference-counting wrapper.

What you can't do, I believe, is associate two scenes with the same viewport.

-------------------------

socrobot | 2019-02-13 06:46:37 UTC | #3

If I make a Camera through Scene1 And create viewport use the camera With Scene2,
Then,The camera created by Scene1 could render something from Scene2?
But the Api does not return any error,It's confusion.
Is it the expected retult or disign bug?

-------------------------

Leith | 2019-02-13 06:47:47 UTC | #4

A viewport is associated with exactly one camera, and one scene. The pairing of camera and scene don't need to be unique, but are unique to a specific viewport. Multiple viewports are ok, but we can only render to one viewport at a time. I'm pretty sure that is correct, or at least close to correct.
I believe it is intentional, as it provides a lot of flexibility.

-------------------------

Modanung | 2019-02-13 09:32:30 UTC | #5

I guess maybe the question is: What is expected to happen when a viewport's scene and that viewport's camera's scene are not the same?

@socrobot Are you trying to render one scene over another?

-------------------------

socrobot | 2019-02-13 10:02:35 UTC | #6

yes,In Ogre, The camera could only render the unique scene that create the camera ,In urho3d,
create camera also throuth scene,but It doesn't real associate them,Maybe I  need to read related source.

-------------------------

Modanung | 2019-02-13 10:14:58 UTC | #7

To layer viewports simply create two (or more), have the top one use a [renderpath without a clear color](
https://gitlab.com/luckeyproductions/Edddy/blob/75f7368e10a529dc508f56088fe09011a005fec4/Resources/RenderPaths/ForwardNoClear.xml) and call `SetNumViewports(2)` on the `Renderer`.

-------------------------

Leith | 2019-02-13 10:10:57 UTC | #8

to me, a second viewport could be a rear view mirror quad, and drawn separately to the scene, with depth testing off, so my concept of viewports may be skewed with respect to urho - in my mind, its just a sub- rectangle of the drawing space we are currently going to draw on.

-------------------------

Modanung | 2019-02-13 10:13:29 UTC | #9

Specifics depend greatly on the use case, there are _many_ conceivable variations.

-------------------------

Leith | 2019-02-13 10:16:07 UTC | #10

Well, we have a scene, a camera, and some limits on the screen draw rectangle, thats all. Everything else has nothing to do with the viewport - I think?

-------------------------

Modanung | 2019-02-13 10:20:00 UTC | #11

The viewport's modified render path is essential in cases where you want transparency or depth weaving.

-------------------------

Leith | 2019-02-13 10:21:51 UTC | #12

hey I'm new here, and I expect this engine to have some quirks, render paths are fine with me, I understand rendering tech pretty good, still yet to publish a shader here but I get that stuff pretty good - the possibilities are endless

Before Unity (ugh), I worked on Gamebryo, which had a very similar rendering system to Urho. Programmable rendering pipeline was a staple.

-------------------------

