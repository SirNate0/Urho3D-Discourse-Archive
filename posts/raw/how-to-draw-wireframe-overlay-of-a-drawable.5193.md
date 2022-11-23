WangKai | 2019-05-26 17:54:32 UTC | #1

Just like Unity Editor does to show the geometry of the drawable. e.g. draw the wireframe of a StaticModel.

Any ideas?

-------------------------

WangKai | 2019-05-26 18:18:36 UTC | #2

I duplicated the mesh in the editor for the mock-up.
![image|690x340](upload://drOtkmmWNxSFseiiK7EZDCMdFEN.png)

-------------------------

Modanung | 2019-05-26 18:49:10 UTC | #3

You could use a material with fill mode set to _wire_ maybe with a tiny tiny negative depth bias.

-------------------------

guk_alex | 2019-05-27 08:37:15 UTC | #4

When you use CollisionShape component with TriangleMesh shape of that object you can see a wireframe in DebugGeometry mode.

-------------------------

Leith | 2019-05-27 08:50:26 UTC | #5

That assumes the drawable has physics - for cases where the drawable may not have physics, the correct answer is to draw the object twice - once to fill the surfaces, and once to draw the wireframe overlay, using different material settings for the fill mode, and yes, a small negative depth bias

-------------------------

guk_alex | 2019-05-27 08:52:29 UTC | #6

True, but CollisionShape method is easy to set up in editor and try right away if you need to quickly debug something.

-------------------------

Leith | 2019-05-27 08:55:40 UTC | #7

Yep, debug drawing for physics objects is super easy and useful!
Most of the time, if you care about looking at the wireframe, it has physics - but we have to talk about all the use cases - we can't assume when we generalize

-------------------------

QBkGames | 2019-05-28 00:57:37 UTC | #8

For some strange reason, if I try to enable the physics debug draw mode, when the game is compile in the "Debug" mode on Visual Studio, the game crashes. Displays fine when compiled in the "Release" mode. Does any one have any idea why this may happen?

-------------------------

Leith | 2019-05-28 01:20:45 UTC | #9

Are you using constraints?
There is a bug in our DebugDrawer for drawing the angular limits of constraints, where those constraints are invalid / in a violated state.

I simply disabled debugdrawing of constraints, and no more crashes.
I have no idea why you're seeing a crash only occurring in Debug mode, but hey, that's good, you should be able to trace the call stack to find the problem :)

-------------------------

WangKai | 2019-05-28 08:08:08 UTC | #10

There are many issues actually -
1. Skinning is done in GPU, CPU side positions are not what we see.
2. How can we draw a material and also draw another wireframe material on it? (I duplicated the model to simulate the effect). ie. If we want to "patch" the drawable and draw wireframe for it, how can we "inject" the patch process?
3. If we want to enable the wireframe globally in the Editor, we need an extra pass after all post process passes? Otherwise any post process will ruin the wireframe

-------------------------

WangKai | 2019-10-13 08:48:00 UTC | #11

I have solved the problem.

By adding an extra wireframe pass in RenderPath and modifying some underling rendering code to support this special pass, extra wireframe rendering is implemented. 

The rendering code changes are -
https://github.com/SuperWangKai/Urho3D/commit/5145db70416730e6dc508863a052948b88027d9c

Any **selected** `drawable` is added to this pass and got its wireframe rendered -

```cpp
PODVector<Drawable*> drawables;
node->GetDerivedComponents<Drawable>(drawables, true);

for (unsigned j = 0; j < drawables.Size(); ++j)
{
    drawables[j]->SetSelected(selected);
}
```

Here is the RenderPath config I use -

```xml
<renderpath>
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
    <command type="scenepass" pass="wireframe" metadata="wireframe" tag="wireframe"/>
</renderpath>
```

`<command type="scenepass" pass="wireframe" metadata="wireframe" tag="wireframe"/>` is the extra pass I added.

We can enable & disable the wireframe pass by using the tag like this -
`renderPath->SetEnabled("wireframe", true);`

![image|575x500](upload://8iexuddJwQ9D6FA7eYcd4ooFQtp.jpeg) 

Editor can be enhanced by this feature. Hope this is useful for you.

-------------------------

GoldenThumbs | 2019-10-13 17:57:53 UTC | #12

I feel like this could be done without needing an extra pass in the renderpath. Lemme tinker a bit.

-------------------------

GoldenThumbs | 2019-10-13 17:59:19 UTC | #13

Though, I will say that your change would be great as an editor/debug feature

-------------------------

