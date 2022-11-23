bremby | 2017-07-14 20:11:36 UTC | #1

Hello,

Newbie here, please be patient with me :slight_smile:. I have an image as a static 2D sprite and ortographic camera pointed at it. The ortosize of the camera is set up the same way like in the samples - using PIXEL_SIZE and the height from the graphics subsystem (which is the height of the window in pixels). When I click on that sprite, I need to calculate the pixel coordinates under the mouse pointer on that image. If the camera was static and unable to zoom, the calculation could be somewhat simple, but if I use camera zoom, then I have to first recalculate the mouse coordinates to a point in the world space (following the 2D Constraints sample). To get the coordinates of the pixel under the mouse cursor I multiply the world coordinates by the dimensions of the image and some magic constant 0.05f (and I add an offset depending on what is the position of the sprite in worldspace). This works well, but I want to understand how the calculation should be done properly.

So can anyone suggest a better way? Or explain what is going on with PIXEL_SIZE, world space coordinates and that magic constant 0.05f?

Thank you.

-------------------------

ricab | 2017-07-15 14:26:16 UTC | #2

If I understand properly, what you are looking for is [Viewport::ScreenToWorldPoint](https://urho3d.github.io/documentation/1.6/class_urho3_d_1_1_viewport.html#a03a1325f33ff1ef8b3af90fade4bdbc9)

-------------------------

bremby | 2017-07-15 16:22:28 UTC | #3

How is that different from Camera::ScreenToWorldPoint()? I still get some point in world space, but I don't understand how to translate it into pixel coordinates on a static 2D sprite that the camera is looking at.

-------------------------

1vanK | 2017-07-15 18:27:48 UTC | #4

[quote="bremby, post:1, topic:3354"]
Or explain what is going on with PIXEL_SIZE, world space coordinates and that magic constant 0.05f?
[/quote]

0.01f

Float loses precision for large values (and camera begins to vibrate when its very far from center of scene). You can not use same units of measurement for screen and scene. 1920x1080 is ULTRA BIG scene... but only single screen. So pixels just are multiplied to some small value when convert to scene coords (it just random const)

EDIT: some note about big float (camera pos) + small float (offset) that cause camera vibrations 
 https://stackoverflow.com/questions/22186589/why-does-adding-a-small-float-to-a-large-float-just-drop-the-small-one

-------------------------

bremby | 2017-07-15 18:26:50 UTC | #5

1vanK: Alright, I think I get it now, thanks!

Solved!

-------------------------

