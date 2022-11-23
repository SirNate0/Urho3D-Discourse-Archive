sabotage3d | 2017-01-02 01:02:00 UTC | #1

Hello,
Is it currently possible to enable wireframe on shaded like in the Urho3d editor but in an actual application ?

-------------------------

hdunderscore | 2017-01-02 01:02:01 UTC | #2

Of course, anything you see in the editor can be done in your application:

Camera class: Set Fill Mode: [urho3d.github.io/documentation/1 ... f718da0c1a](http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_camera.html#a0343192a92c8a1401453e2f718da0c1a)
Fill mode enum from GraphicsDefs.h
[code]/// Fill mode.
enum FillMode
{
    FILL_SOLID = 0,
    FILL_WIREFRAME,
    FILL_POINT
};[/code]

-------------------------

sabotage3d | 2017-01-02 01:02:03 UTC | #3

thanks a lot :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:02:04 UTC | #4

Can we combine FILL_WIREFRAME and FILL_SOLID and choose a color for the wireframe ?

-------------------------

weitjong | 2017-01-02 01:02:04 UTC | #5

I believe it is not easy to do so without tinkering with the engine's code. I have not tried this myself but I think you need to draw the model twice in two separate batches, one with FILL_SOLID and one with FILL_WIREFRAME. You may need to use Graphics::SetDepthBias() method in between the draws to avoid z-fighting. Basically if you want this to happen on all the models in your scene then you could modify the renderpath to have two scene-pass commands or something like that (see [github.com/urho3d/Urho3D/blob/m ... 1466-L1478](https://github.com/urho3d/Urho3D/blob/master/Source/Engine/Graphics/View.cpp#L1466-L1478)).

-------------------------

hdunderscore | 2017-01-02 01:02:04 UTC | #6

Another way might be to write a shader for wireframe.

-------------------------

sabotage3d | 2017-01-02 01:02:07 UTC | #7

Thanks I will try that :slight_smile:

-------------------------

godan | 2017-01-02 01:04:31 UTC | #8

To write a wireframe shader for a specific model - would you specify the fill mode in the shader code or is it possible to send that option through the material/technique xml files (i.e. similar to how you specify the cull mode)?

-------------------------

cadaver | 2017-01-02 01:04:32 UTC | #9

Currently the fill mode is only the camera's property, not a material property. To make a model wireframe you would have to make its geometry use for example LINE_LIST primitive mode. You can do that programmatically but I believe the exporters assume TRIANGLE_LIST always.

This could be added to material though, at a small efficiency cost (now we just need to set fill mode once per scene pass, if it's a material property we have to set it on each material change.)

-------------------------

cadaver | 2017-01-02 01:04:33 UTC | #10

Material fill mode has been added.

-------------------------

godan | 2017-01-02 01:04:44 UTC | #11

Perfect! Thanks for adding this.

Syntax is <fill value="wireframe"/>?

-------------------------

cadaver | 2017-01-02 01:04:45 UTC | #12

Yes. This was missing from documentation, thought I updated it but apparantly didn't. :slight_smile: It's there in the master branch now.

-------------------------

