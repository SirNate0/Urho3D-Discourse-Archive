wqf | 2021-08-02 17:28:35 UTC | #1

I need to create a scene. Use opencv to capture the camera image and render the image on the urho3d window in real time, and then place a 3d model somewhere in the window. Now I don't know how to draw the image on the window of urho3d, the image is an array in rgb format, like "rgbrgbrgb", if anyone can give me some suggestions, I will be grateful.

-------------------------

nickwebha | 2021-08-21 06:38:27 UTC | #2

This is not a complete answer to your question but [this code](https://discourse.urho3d.io/t/infinitely-scrolling-tile-based-map-with-external-textures/6749/28) might help. `tileString` is expected to be a supported image format (PNG in my case).

As far as getting the image from OpenCV into Urho3D I have no clue.

-------------------------

SirNate0 | 2021-08-21 16:15:57 UTC | #3

You can probably use an Urho3D::Image and use SetSize and SetData to copy the data from whatever buffer OpenCV stores it in to a format supported by Texture2D. You may also be able to set the data directly to a texture, using an RGB format (you can get the format for that from Graphics).

-------------------------

