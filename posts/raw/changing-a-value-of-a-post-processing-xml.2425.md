Andre_B | 2017-01-02 01:15:20 UTC | #1

Hi,

Im using the following XML file to do a post processing blurr effect, this is equal to the Blurr example in 
[github.com/xamarin/Urho3D/blob/ ... s/Blur.xml](https://github.com/xamarin/Urho3D/blob/master/bin/Data/PostProcess/Blur.xml)

<[code]renderpath>
    <rendertarget name="blurh" tag="Blur" sizedivisor="2 2" format="rgba" filter="true" />
    <rendertarget name="blurv" tag="Blur" sizedivisor="2 2" format="rgba" filter="true" />
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR9" output="blurh">
      <parameter name="BlurDir" value="1.0 0.0" />
      <parameter name="BlurRadius" value="1.0" />
      <parameter name="BlurSigma" value="2.0" />
      <texture unit="diffuse" name="viewport" />
    </command>
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR9" output="blurv">
      <parameter name="BlurDir" value="0.0 1.0" />
      <parameter name="BlurRadius" value="1.0" />
      <parameter name="BlurSigma" value="2.0" />
      <texture unit="diffuse" name="blurh" />
    </command>
    <command type="quad" tag="Blur" vs="CopyFramebuffer" ps="CopyFramebuffer" output="viewport">
      <texture unit="diffuse" name="blurv" />
    </command>
  </renderpath>[/code]

I have a render to texture system setup, and i just append this XML to the standard viewport where i do my rendering, everything works as it should.

Now, is there a way for me to affect the BlurSigma value on this XML on a frame by frame basis? if so what would be the best way to achieve that?

EDIT: i have just read in the wiki that i can create a render path programmatically, i guess that is what i must do every frame but with different sigma values? or i guess just set the "BlurSigna" value with Viewport.RenderPath.SetShaderParameter??

-------------------------

1vanK | 2017-01-02 01:15:20 UTC | #2

[github.com/1vanK/Soulmates/blob ... aLogic.cpp](https://github.com/1vanK/Soulmates/blob/master/GameSrc/CameraLogic.cpp)

[code]renderPath->SetShaderParameter("BlurSigma", newSigma);[/code]

-------------------------

Andre_B | 2017-01-02 01:15:20 UTC | #3

[quote="1vanK"]https://github.com/1vanK/Soulmates/blob/master/GameSrc/CameraLogic.cpp

[code]renderPath->SetShaderParameter("BlurSigma", newSigma);[/code][/quote]

Thanks i just realised that renderPaths have a setShaderParameter function :slight_smile:

-------------------------

