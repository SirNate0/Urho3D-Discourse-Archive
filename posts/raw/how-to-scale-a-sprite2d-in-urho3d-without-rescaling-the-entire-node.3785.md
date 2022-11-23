cirosantilli | 2017-12-13 11:02:44 UTC | #1

http s://stackoverflow.com/questions/47488411/how-to-scale-a-sprite2d-in-urho3d-without-rescaling-the-entire-node

[link is deleted by Admin]

-------------------------

jmiller | 2017-12-06 19:06:57 UTC | #2

Hello,

I have not tried this, but I'm guessing: (**edit**: it's the latter; I confused the two)
```
SetTextureRect(rect);
SetUseTextureRect(true);
```

https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_static_sprite2_d.html

There is also SetDrawRect()/SetUseDrawRect() to play with.

Here are the effects of those:
  https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Urho2D/StaticSprite2D.cpp#L290

-------------------------

cirosantilli | 2017-12-05 23:40:26 UTC | #3

Thanks, `SetDrawRect()` does what I need, runnable example at: https://github.com/cirosantilli/Urho3D-cheat/blob/1905d1f4824c6b88aca867c5be8ccb5dfae957f3/scale_sprite.cpp

`SetTextureRect` appears to change the uv coordinates of the texture. Not what I needed, but also good to know.

-------------------------

weitjong | 2017-12-13 11:46:32 UTC | #4



-------------------------

