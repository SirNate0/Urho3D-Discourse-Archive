magic.lixin | 2017-01-02 01:10:05 UTC | #1

I`m trying to use UI Text with font "Fonts/BlueHighway.sdf", but it looks like this:
    [img]http://chuantu.biz/t2/26/1455596012x-1922738981.png[/img]

-------------------------

OvermindDL1 | 2017-01-02 01:10:06 UTC | #2

Your image appears broken to me, but I'm guessing that you did not apply the correct shader.

-------------------------

magic.lixin | 2017-01-02 01:10:06 UTC | #3

sorry, the link should be fixed now, I can`t find a way to apply shader to UIElement.

-------------------------

OvermindDL1 | 2017-01-02 01:10:11 UTC | #4

[quote="magic.lixin"]sorry, the link should be fixed now, I can`t find a way to apply shader to UIElement.[/quote]
On your custom Material do something like:
[code]
material->SetTechnique(0, sdfShader)
[/code]
And you can also set the shader parameters as necessary to set an effect if you want, one or the other of (or none for normal text):
[code]
material->SetShaderParameter("ShadowOffset", shadowOffset);
material->SetShaderParameter("ShadowColor", shadowColor);
// -- or --
material->SetShaderParameter("StrokeColor", strokeColor);
[/code]

I've not tested the above yet, though probably should, would be nice to use SDF in my UIElements as well so I know the text scales well on different screen sizes, would be nice if SDF were default, though I can see why it is not until it is fully refined with a good source.

-------------------------

magic.lixin | 2017-01-02 01:10:12 UTC | #5

UIElement has not function to set custom material, also by looking through the implementation of UI::Render, there is no way to set custom shader, I think it`s not a big deal, I can live without that  :smiley:

-------------------------

thebluefish | 2017-01-02 01:10:12 UTC | #6

[quote="magic.lixin"]by looking through the implementation of UI::Render, there is no way to set custom shader[/quote]

TBH this is a relatively easy fix.

-------------------------

