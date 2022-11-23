Yatsomi | 2018-12-10 16:46:30 UTC | #1

Hi, im new to urho3D and developing a 2D pixel-art game. is it possible to achieve pixel-perfection in urho?

-------------------------

orefkov | 2018-12-11 06:00:01 UTC | #2

You can try do all in UI - it is pixel perfect by default.
Or use scene/node with ortographic camera, set camera's ortoSize by screen height in pixels.
In the engine itself, it is assumed that in one world unit there are 100 pixels (it is PIXEL_SIZE constant, which is 0.01)
You can set camera's ortoSize in screen height multipled by  PIXEL_SIZE and all coordinates calculated with this in mind. I used this approach in a mobile game, because if you use the pixels themselves for world coordinates, then for big values (500-1000 or more), problems can occur with the accuracy of floats on the GPU.

-------------------------

Yatsomi | 2018-12-11 09:13:55 UTC | #3

thank you for the answer sir. i'll try it :upside_down_face:

-------------------------

orefkov | 2018-12-11 09:17:00 UTC | #4

Hope, you read this - https://urho3d.github.io/documentation/1.7/_urho2_d.html

-------------------------

