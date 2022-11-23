projector | 2017-11-23 01:16:20 UTC | #1

Hi All, 

I'm new to Urho, is there a way to use grascale texture file for alpha together with another RGB texture file, in one material?

-------------------------

Bananaft | 2017-11-24 18:51:35 UTC | #2

Create your own technique, copy DiffAlpha.xml or whatever you need, add psdefines = "MY_CUSTOM_DEF" in alpha pass, then in shader code LitSolid.glsl:

    #ifdef  MY_CUSTOM_DEF
 multiply diffuse alpha with specular texture alpha, do whatever you want, for this particular case.

    #endif

-------------------------

projector | 2017-11-24 18:51:48 UTC | #3

Thank you, it's very helpful, I will try that.

-------------------------

