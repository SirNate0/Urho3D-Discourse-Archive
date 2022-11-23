evolgames | 2020-03-08 07:41:49 UTC | #1

So the Scene Replication binary runs and works fine.
Running the Lua sample unmodified gives me the error:
```
attempt to call method SetInt (a nil value)
```

Is there another prerequisite for Networking that this needs for Lua?
Is this a JSON thing? I don't see SetInt in the Lua api...
I tried changing it to SetInterpolation and that wasn't it.

Can anyone else get the 17_SceneReplication lua sample to work without getting any errors? (mine runs, but it'll never instantiate the ball)

-------------------------

Miegamicis | 2020-03-08 08:09:06 UTC | #2

It should work out of the box. If there are issues like this, there's possibility that indeed some api bindings are missing.

-------------------------

Miegamicis | 2020-03-08 15:25:20 UTC | #3

never mind, it was actually a syntax issue. Fixed in https://github.com/urho3d/Urho3D/commit/02c9072fee44dcb6d3165a27f1ab1c2319e03396

-------------------------

evolgames | 2020-03-08 15:25:44 UTC | #4

Great! Thanks for that, I would have never figured that out.

-------------------------

