dakilla | 2017-01-03 10:53:36 UTC | #1

Hi

I want to use a material builded manually at runtime that can have from 1 to 4 textures.
How to specify theses texture units using material->SetTexture(...   I don't know which TextureUnit enum to use.



thanks

-------------------------

jmiller | 2017-01-03 10:57:59 UTC | #2

Hello.

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/GraphicsDefs.h#L315

-------------------------

dakilla | 2017-01-03 12:09:05 UTC | #3

So for custom units index is this correct to do that ? :
 
material->SetTexture(TextureUnit(0), myNormalTexture );
material->SetTexture(TextureUnit(1), myUVTexture1 );
material->SetTexture(TextureUnit(2), myUVTexture2 );
material->SetTexture(TextureUnit(3), myUVTexture3 );
material->SetTexture(TextureUnit(4), myUVTexture4 );

-------------------------

jmiller | 2017-01-03 12:28:16 UTC | #4

I think that should work; Terrain, for example, uses most of those for its detail textures.

-------------------------

Andre_B | 2017-01-03 12:38:41 UTC | #5


(Note: using UrhoSharp) you can have as much indexes as you want.

On a shader i have 

//previous texture
uniform sampler2D sLayer0;

//current texture
uniform sampler2D sLayer1;

When coding my materials i just use the following:

material->SetTexture(0, tex0 );
material->SetTexture(1, tex1);

The order is related to the sampler2D uniforms you have on your fragment shader.

-------------------------

