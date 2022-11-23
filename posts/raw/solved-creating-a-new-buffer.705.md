ghidra | 2017-01-02 01:02:16 UTC | #1

more shader questions.

I am playing around with trying to create a custom buffer, the way that defered renderpaths create three rendertargets, albedo, depth, and normal for example.

In the docs for RenderPaths it says under the available commands for scene pass:

[quote]
Textures global to the pass can be [u]bound to free texture units[/u]; these can either be the viewport, [u]a named rendertarget[/u], or a 2D texture resource identified with its pathname.
[/quote]
so theoretically, if I have this:
[code]
<rendertarget name="mytarget" sizedivisor="1 1" format="rgba"/>
<command type="quad" vs="myshader" ps="myshader" output="mytarget">
      <texture unit="environment" name="viewport" />
</command>
<command type="scenepass" pass="mypass">
      <texture unit="mytarget" name="mytarget" />
</command>
[/code]
I should be able to use my declared render target as a texture, however, i get the error:
[quote]
ERROR: Unknown texture unit name mytarget
[/quote]

Just trying to figure out how I can make a NEW texture unit. I can change all those "mytarget" to "albedo" and i get no errors. So I assume I am not adding it as a uniform (which I also tried sMytargetBuffer in the shader) properly or something else somwhere else.

Thanks.

-------------------------

reattiva | 2017-01-02 01:02:17 UTC | #2

Try this:
[code]<texture unit="diffuse" name="mytarget" />[/code]
to have your buffer mapped to the sDiffMap sampler.
You can find the list of textures names you can use in Material.cpp.

-------------------------

ghidra | 2017-01-02 01:02:18 UTC | #3

Thanks, I'll try that.
I see that there are a fair number of unit names, however; I'm still curious if it is possible to somehow declare a custom unit name.

Edit:
Actully, I see that its unesssisary to make my own. It seems I can just use the same one over and over for each pass if I want, since it apears to just set a variable so to speak. This will work fine. Thanks again.

-------------------------

