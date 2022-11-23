huminzheng | 2022-02-15 08:00:39 UTC | #1

Hi guys!
  Is there a sample about calling C++ Assimp function from javascrip?

-------------------------

Eugene | 2022-02-15 08:12:11 UTC | #2

[quote="huminzheng, post:1, topic:7194"]
Is there a sample about calling C++ Assimp function from javascrip?
[/quote]
Assimp is not even linked to Emscripten binary by default. You cannot call it from C++, not just from javascript.

If you link Assimp to your binary, you should be able to expose its functions in JS like here:
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp#L138

-------------------------

huminzheng | 2022-02-15 09:05:09 UTC | #3

Thanks  for your reply. I have already build the Urho3D success with emscripten on windows. How could i link assimp to the Urho3D Emscripten binary ?

-------------------------

