mrchrissross | 2018-12-20 23:58:13 UTC | #1

Hi everyone!
I have an issue with collision detection in my game, currently i have two object that have: 

    CollisionShape* shape = objectNode->CreateComponent<CollisionShape>();
    shape->SetTriangleMesh(model->GetModel(), 0);

One object is the player and another is a wall, or rock. The problem is that both objects cannot collide with each other (i.e., the player goes through the wall).

Any help would be much appreciated!

-------------------------

Modanung | 2018-12-21 00:01:48 UTC | #2

Try using `SetConvexHull` instead for non-static bodies like the player.

-------------------------

mrchrissross | 2018-12-21 00:02:53 UTC | #3

is that instead of SetTriangleMesh(model-&gt;GetModel(), 0);?

-------------------------

mrchrissross | 2018-12-21 00:04:15 UTC | #4

thing is, strangely other non-static objects that have collider->SetBox(Vector3::ONE); seem to be able to hit the player no problem?

-------------------------

Modanung | 2018-12-21 00:05:41 UTC | #5

If I'm not mistaken, yes.
Moving triangle mesh colliders are advised against in Bullet's documentation, I think.

-------------------------

mrchrissross | 2018-12-21 00:14:20 UTC | #7

ah works beautifully however when i collide them both together it seems to lag the game massively. Really amazing for the SetBox(Vector3::ONE) collision though. Any way to get around the lag?

-------------------------

Modanung | 2018-12-21 01:53:05 UTC | #8

I'm not sure what could be causing that.

-------------------------

Sinoid | 2018-12-21 02:09:57 UTC | #9

Bullet is stupid slow in debug builds and when a debugger is hooked. 

Doing either of those?

-------------------------

mrchrissross | 2018-12-21 08:02:44 UTC | #10

Do you mean this type of debug below?

    #include <Urho3D/DebugNew.h>
        if (drawDebug)
    		renderer->DrawDebugGeometry(true);

other than that the only debug build that I use is the visual studio one.

-------------------------

Modanung | 2018-12-21 11:08:17 UTC | #11

[quote="mrchrissross, post:10, topic:4769"]
other than that the only debug build that I use is the visual studio one.
[/quote]

I think that's the one @Sinoid meant.

-------------------------

mrchrissross | 2018-12-21 11:33:15 UTC | #12

Ah alright so it's visual studio debugger. Is there anyway to speed it up? Or should I just open with the exe?

-------------------------

Sinoid | 2018-12-21 19:26:15 UTC | #13

Only use release builds for checking performance - the difference is usually large. In VS you can run as `Debug -> Start without Debugging` (shift+F5 default) to launch from VS without hooking - mostly no different than launching from the executable itself (*mostly*, still honors VS launch parameters).

The debugger has to *patch* things out in order for it to even work (alloc, grabbing stacks, etc) so once you hook you've got overhead just for that regardless of whether you're running Debug/Release.

Although there's a profiler in Urho3D it's just a ballpark tool, you still want to use VS' `Debug -> Performance Profiler` to find where things are slowing down, which is also only reliable in a Release build.

-------------------------

GodMan | 2018-12-22 23:49:52 UTC | #14

Also one thing to note is this. If your using your render model for the physics make sure its a simple model. If you use a model that has quite a few polygons then your game will lag bad due to the physics engine having to run calculations on your entire mesh. Most modern games use a very simple representation of the render model that is not rendered in the game "obviously".

-------------------------

