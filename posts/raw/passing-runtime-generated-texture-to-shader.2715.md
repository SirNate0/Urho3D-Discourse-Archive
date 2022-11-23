GoogleBot42 | 2017-03-18 02:11:01 UTC | #1

Hello I cannot seem to figure out how to pass a texture I generate at runtime to a shader.  I am trying to pass it with the "TU_CUSTOM1" texture unit.  But the program crashes every time I try to add it with 

[code]mat->SetTexture(TU_CUSTOM1, someTexture);[/code]

Looking at how SetTexture is implemented, the internal texture array for storing the material's textures needs to be increased but I don't see any function for increasing the number of textures.  There must be something that I am missing here.

Thanks in advance!  ;)

-------------------------

cadaver | 2017-01-17 09:05:41 UTC | #2

Available texture units are from 0 to 15, there is no need to tell Material how many you want to use, but you can't use more than 16. Depending on the rendering you're doing some of the units are engine reserved (e.g. shadow map, light ramps etc.) In GLSL use matching numbers in the samplers, eg. sMySampler15 to access unit 15, unless you use the predefined names.

-------------------------

GoogleBot42 | 2017-01-18 13:27:02 UTC | #4

Thanks!  That really helps.  The crash was because I was creating a SharePtr< Texture> and then returning a Texture* from a function.  So the Texture deletes itself upon returning from the function because the ref count is 0.  Whoops.  LOL  :blush: 

Anyway your answer I definitely still needed.

-------------------------

