Denthor | 2017-01-02 01:10:39 UTC | #1

Hi there...

I was wondering if it is possible to clip a StaticSprite2D? In my case I want a sprite to appear out of a portal, but the entire sprite is visible as it moves out to the right (even to the left of the portal it is coming through). How would I have only the section that has moved out of the portal be visible?

Regards

-------------------------

gawag | 2017-01-02 01:10:40 UTC | #2

I don't know if there is a better solution but StaticSprite2D's are also using the normal material system and you could use a shader parameter to draw only a part of the texture: [urho3d.wikia.com/wiki/Custom_shader_parameters](http://urho3d.wikia.com/wiki/Custom_shader_parameters)
You could pass the value for one axis where to fade the material out.

I just tested making all pixel colors above a certain world position transparent:
In the shader (HLSL in this case but GLSL is practically identical):
[code]
...
void PS(...)
{
...
// at the end:
if(iWorldPos.y>1)
    oColor.a=0;
}
[/code]
Normal scene: [i.imgur.com/I2xIh4n.jpg](http://i.imgur.com/I2xIh4n.jpg) (don't mind the black stripes on the terrain, some weird unrelated issue)
Cut model: [i.imgur.com/hmMkYtt.jpg](http://i.imgur.com/hmMkYtt.jpg)
The material has to support transparency for this to work. Also the shadow is here still completely there, that could be fixed though but shouldn't matter for your case.

One can also fade the color out:
[code]
oColor.a=oColor.a*clamp(1.0-(iWorldPos.y-1)/0.5,0.0,1.0);  // fades out from Y world pos 1.0 (visible) to 1.5 (completely transparent)
[/code]
This results in this: [i.imgur.com/ExY7yWh.jpg](http://i.imgur.com/ExY7yWh.jpg)

Also an interesting thing I had by having the clamp parameter in the wrong order: [i.imgur.com/Slhct4r.jpg](http://i.imgur.com/Slhct4r.jpg)

-------------------------

Denthor | 2017-01-02 01:11:18 UTC | #3

Hi there, thankfully this works, but presents another problem. For some reason all 2D objects using a custom shader (instead of the default Urho2D shader) are rendered behind standard 2D objects, even if SetLayer is called.

-------------------------

gawag | 2017-01-02 01:11:18 UTC | #4

[quote="Denthor"]Hi there, thankfully this works, but presents another problem. For some reason all 2D objects using a custom shader (instead of the default Urho2D shader) are rendered behind standard 2D objects, even if SetLayer is called.[/quote]
Sounds the default shader is doing something different. Maybe the layer is set as the Z (depth) value?
Try to copy the default material and shader and use that as a base for your custom material and shader.

-------------------------

Denthor | 2017-01-02 01:11:19 UTC | #5

Hi there, I've done that. SetCustomMaterial on a StaticSprite2D (even if that material's shader is a direct copy of Urho2D.glsl) starts ignoring the Z order.

-------------------------

Denthor | 2017-01-02 01:11:24 UTC | #6

I finally resolved it by extending the base Urho2D.glsl to have a HaveClip parameter and two vectors defining the clip region, then setting per object material parameters to set it just for those objects I want clipped. That way the loss of ordering in the UpdateViewBatchInfo in Render2D.cpp on a material switch is not an issue.

Thanks for the help, it set me on the right path.

Regards,

-------------------------

