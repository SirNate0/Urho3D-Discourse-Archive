diverlin | 2020-08-17 14:25:48 UTC | #1

Greetings! 
I have problem having dynamically generated mask on C++ and using it in my custom renderpath Custom.xml.

i read documentation:
`    Note that if you already have created a named rendertarget texture in code and have stored it into the resource cache by using AddManualResource() you can use it directly as an output (by referring to its name) without requiring a rendertarget definition for it.`

and probably miss something or using it in wrong way
in C++ I generate sampler

    m_texture(new Urho3D::Image(context->context()));
    m_texture->SetName("rtLightMap");

    unsigned int width = 1024;
    unsigned int height = 768;
    m_texture->SetSize(width, height, 3, Urho3D::TEXTURE_RENDERTARGET);

    for (int x=0; x<width; ++x) {
        for (int y=0; y<height; ++y) {
            m_texture->SetPixel(x, y, Urho3D::Color(1.0,1.0,1.0));
        }
    }

    context->cache()->AddManualResource(m_texture);

in Custom.xml the following renderpath is described:
    
    <rendertarget name="rtDiffuseMap" sizedivisor="1 1" format="rgba" />
    <rendertarget name="rtNormalMap" sizedivisor="1 1" format="rgba" />
<!--    <rendertarget name="rtLightMap" sizedivisor="1 1" format="rgba" />-->

    <command type="clear" color="0 0 0 0" output="rtDiffuseMap"></command>
    <command type="clear" color="0 0 0 0" output="rtNormalMap"></command>

    <command type="scenepass" pass="normal" output="rtNormalMap"></command>
    <command type="scenepass" pass="diffuse" output="rtDiffuseMap"></command>

    <command type="quad" vs="Urho2DCombine" ps="Urho2DCombine" output="viewport">
        <texture unit="diffuse" name="rtDiffuseMap" />
        <texture unit="normal" name="rtNormalMap" />
        <texture unit="specular" name="rtLightMap" />
    </command>

</renderpath>

My final viewport is black, because the rendertarget="rtLightMap" considered be black (I multiply by it's color in shader Urho2DCombine). if I use the path "asteroid/concept/nm_combine_concept.png" instead of render target name, I got proper scene picture, but with static mask.
What I want to have, is dynamic mask in C++ and use it in my renderpath.

Could someone point me on what I was missing? 
My appreciation in advance

-------------------------

JTippetts1 | 2020-08-17 13:48:40 UTC | #2

I assume by the presence of the call to m_texture->SetPixel that m_texture is actually an Image resource, and not a Texture resource. You have to create a named Texture resource instead, and upload data to it from the generated image. Texture resources come in a number of different varieties: Texture2D, Texture3D, TextureCube, Texture2DArray. Texture2D is probably the one you want. You can upload data from an Image using the Texture2D::SetData method.

-------------------------

Eugene | 2020-08-17 13:59:05 UTC | #3

[quote="diverlin, post:1, topic:6332"]
`m_texture->SetSize(width, height, 3, Urho3D::TEXTURE_RENDERTARGET);`
[/quote]

`Image::SetSize` has signature `(int width, int height, int depth, unsigned components)`, so you are basically creating `width*height*3` 3D texture with TEXTURE_RENDERTARGET=2 color components (red and green)... Probably not what you want to do.

-------------------------

diverlin | 2020-08-17 14:25:33 UTC | #4

[JTippetts1](https://discourse.urho3d.io/u/JTippetts1)
thank you! using Urho3D::Texture2D resource works perfectly

-------------------------

Modanung | 2020-08-17 23:44:44 UTC | #5

@diverlin Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

diverlin | 2020-08-22 17:11:42 UTC | #6

@ [Modanung](https://discourse.urho3d.io/u/Modanung)
thank you!

-------------------------

