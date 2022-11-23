sabotage3d | 2017-01-02 01:15:14 UTC | #1

Hi,
Is it possible to clamp UV coords of a texture unit inside a quad command? 
I am trying to offset the uvs in the shader but I am getting repeat by default. 

For example if I have texture unit in the diffuse slot inside a quad command.
[code]<texture unit="diffuse" name="test.jpg"/>[/code]

And I want to clamp the UV coords. 
[code]<address coord="u" mode="clamp" />
<address coord="v" mode="clamp" />[/code]

Would this work or it is not supported?

-------------------------

cadaver | 2017-01-02 01:15:16 UTC | #2

The UV addressing mode of the texture must have been set beforehand to what you want, the renderpath commands are not going to change it.

-------------------------

sabotage3d | 2017-01-02 01:15:16 UTC | #3

Thanks cadaver. 
Do you mean something like this? And then passing this to the texture unit.
[code]Texture2D* texture = cache->GetResource<Texture2D>(filepath);
texture->SetAddressMode(COORD_U, ADDRESS_CLAMP);
texture->SetAddressMode(COORD_V, ADDRESS_CLAMP);[/code]

-------------------------

cadaver | 2017-01-02 01:15:16 UTC | #4

Yes, or using the xml definition file alongside the texture.

-------------------------

