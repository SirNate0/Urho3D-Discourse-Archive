vivienneanthony | 2017-01-02 01:02:23 UTC | #1

Hello,

Is there a way to pass a weight map from the c++ app to the xml shader? For example, my procedural terrain creates proceduralterrain image. How can I pass the image to the following?

Vivienne

[code]<material>
    <technique name="Techniques/TerrainBlendTriPlanar.xml" />
    <texture unit="0" name="Textures/TerrainWeights.dds" /> <--- Use the  Creates proceduralterrain image here
    <texture unit="1" name="Textures/GrassLarge.png" />    
    <texture unit="2" name="Textures/TerrainDetail2.dds" />    
    <texture unit="3" name="Textures/TerrainDetail3.dds" />
    <parameter name="MatSpecColor" value="0 0 0 0" />
    <parameter name="DetailTiling" value="2048 2048" />
</material>[/code]

-------------------------

vivienneanthony | 2017-01-02 01:02:24 UTC | #2

For example, 

The terrain procedual created this terrain using [b] terrain->GenerateProceduralHeightMap(terrainrule);[/b] that I can further use [b]producedHeightMapImage -> SetData(terrain -> GetData());[/b]

[img]http://i.imgur.com/cIS0VQt.png[/img]

I can now pass that information maybe to a texture to properly assign texture based on heightmap and many other things.

If I place a charater at spot 0,0,0 and the terrain is created at 0 0. Does the player 0,0 lay center of the heightmap image??

-------------------------

vivienneanthony | 2017-01-02 01:02:26 UTC | #3

I tried the Texture, Material, and Image. I don't see anywhere where I can load a load a image into a Image then load it as a material texture???

Any ideas?

-------------------------

JTippetts | 2017-01-02 01:02:26 UTC | #4

Use the SetData() method of Texture2D to set the texture from an Image.

Edit: for example, in Lua:

[code]
image=Image(context)
image:SetSize(1024,1024,3)

-- Do procedural stuffs on image here

blendtex=Texture2D:new(context)
blendtex:SetSize(0,0,0,TEXTURE_DYNAMIC)  -- Useful to set dynamic if going to modify it at runtime
blendtex:SetData(image, false)

terrain:GetMaterial():SetTexture(0,blendtex)

[/code]

-------------------------

vivienneanthony | 2017-01-02 01:02:27 UTC | #5

[quote="JTippetts"]Use the SetData() method of Texture2D to set the texture from an Image.

Edit: for example, in Lua:

[code]
image=Image(context)
image:SetSize(1024,1024,3)

-- Do procedural stuffs on image here

blendtex=Texture2D:new(context)
blendtex:SetSize(0,0,0,TEXTURE_DYNAMIC)  -- Useful to set dynamic if going to modify it at runtime
blendtex:SetData(image, false)

terrain:GetMaterial():SetTexture(0,blendtex)

[/code][/quote]


Thanks.

-------------------------

vivienneanthony | 2017-01-02 01:02:27 UTC | #6

[quote="JTippetts"]Use the SetData() method of Texture2D to set the texture from an Image.

Edit: for example, in Lua:

[code]
image=Image(context)
image:SetSize(1024,1024,3)

-- Do procedural stuffs on image here

blendtex=Texture2D:new(context)
blendtex:SetSize(0,0,0,TEXTURE_DYNAMIC)  -- Useful to set dynamic if going to modify it at runtime
blendtex:SetData(image, false)

terrain:GetMaterial():SetTexture(0,blendtex)

[/code][/quote]

I tried this approach

[code]/// Attempt to get terrain image
    Image * producedHeightMapImage = new Image(context_);
    producedHeightMapImage -> SetSize(1024,1024, 1, 4);
    producedHeightMapImage -> SetData(terrain -> GetData());

    /// Changge
    Texture2D * blendtex=new Texture2D(context_);
    blendtex -> SetSize(0,0,0,TEXTURE_DYNAMIC);
    blendtex -> SetData(producedHeightMapImage->GetNextLevel(), false);

    Material * terrainMaterial = terrain -> GetMaterial();
    terrainMaterial->SetTexture(TU_DIFFUSE,blendtex);
[/code]

It might be similiar to what you mentioned. I'm not sure. I'm not sure if I have to tell the terrain material to refresh itself but I'm assuming it would default to the xml file. Hmmm.

-------------------------

JTippetts | 2017-01-02 01:02:28 UTC | #7

Using the heightmap image for your blendmap is unlikely to produce any interesting results. The blend map is used to determine how the 3 different detail textures are blended together, with each color component acting as a weighting factor for one of the textures. If the blend image is a greyscale image, that means each color component is the same value as the others. The weights are balanced so that they add up to 1 in the shader, so any greyscale value is going to result in equal contributions from all 3 detail textures, producing the same 1/3, 1/3, 1/3 blend all across the terrain.

I am unsure exactly what you are trying to accomplish by using the heightmap texture directly. Rather, you will probably want to use the texture as part of a different process that analyzes each height sample and calculates relevant blend factors to construct a blend texture. For example, you could use the elevation to lerp between Color(1,0,0) and Color(0,1,0). This would cause the terrain to gradually fade from the first detail texture to the second based on height. Or you could use the calculated normal of the terrain at a given point, take the dot product with the vector (0,1,0) and use the result as a "steepness" factor. Test steepness against some arbitrarily chose threshold and blend from non-cliff to cliff terrain types. This is a nice filter to apply to automatically assign cliff detail to steep areas.

Edit: For example, consider this screen grab from my fledgling terrain-editor-in-progress:
[img]http://i.imgur.com/b7c4vy2.png[/img]

The associated blend texture for that terrain looks like:
[img]http://i.imgur.com/gMtDB8B.png[/img]

See how the different terrain types are demarcated in the blend texture by the various color components? Where there's red, there's dirt. Green maps to grass, and blue to stone.

-------------------------

vivienneanthony | 2017-01-02 01:02:28 UTC | #8

I see what you mean. My first thought if you had a range of 0 to 1.  If set thresholds that the filter will selective place filters.  0 to 0.4, texture 1(1.0,0.0,0.0) , then ..4 to .8 texture 2 (0.0,1.0,0.0), etc..

I understand the latter. To me it sounds overly complicated. Althougth I understand what you mean I will have to do  reading and experimenting playing with Urho3D. Of course,  at lot of debugging and poking around.

[quote="JTippetts"]Using the heightmap image for your blendmap is unlikely to produce any interesting results. The blend map is used to determine how the 3 different detail textures are blended together, with each color component acting as a weighting factor for one of the textures. If the blend image is a greyscale image, that means each color component is the same value as the others. The weights are balanced so that they add up to 1 in the shader, so any greyscale value is going to result in equal contributions from all 3 detail textures, producing the same 1/3, 1/3, 1/3 blend all across the terrain.

I am unsure exactly what you are trying to accomplish by using the heightmap texture directly. Rather, you will probably want to use the texture as part of a different process that analyzes each height sample and calculates relevant blend factors to construct a blend texture. For example, you could use the elevation to lerp between Color(1,0,0) and Color(0,1,0). This would cause the terrain to gradually fade from the first detail texture to the second based on height. Or you could use the calculated normal of the terrain at a given point, take the dot product with the vector (0,1,0) and use the result as a "steepness" factor. Test steepness against some arbitrarily chose threshold and blend from non-cliff to cliff terrain types. This is a nice filter to apply to automatically assign cliff detail to steep areas.

See how the different terrain types are demarcated in the blend texture by the various color components? Where there's red, there's dirt. Green maps to grass, and blue to stone.[/quote]

-------------------------

JTippetts | 2017-01-02 01:02:28 UTC | #9

It's not over-complicated. If anything, it's a little under-complicated due to not using the alpha channel for a 4th terrain type. Even more complicated would be to allow a second blend texture to support up to 8 terrain types. :smiley:

The issue with using thresholds is that you don't have sufficient control over terrain placement. If you assign, say, dirt to (0,0.3), grass to (0.3,0.6) and stone to (0.6,1) then it becomes impossible to have a smooth blend directly from dirt to stone, because any interpolation between dirt and stone is going to cross over grass territory, resulting in a narrow band of grass-ish blend in-between. Using a weighted blend, you can easily blend between dirt (R) and stone (B) simply by using 0 for the grass (G) color component. IMO, thresholds are only suitable for those myriad terrain "demos" you see all over youtube, and any "serious" terrain implementation is going to implement full blending or splatting. Because, really, how often in real life do you see terrain determined solely by elevation above sea level? Never, that's how often. It has an influence, sure, but it's not the sole factor.

-------------------------

vivienneanthony | 2017-01-02 01:02:28 UTC | #10

[quote="JTippetts"]It's not over-complicated. If anything, it's a little under-complicated due to not using the alpha channel for a 4th terrain type. Even more complicated would be to allow a second blend texture to support up to 8 terrain types. :smiley:

The issue with using thresholds is that you don't have sufficient control over terrain placement. If you assign, say, dirt to (0,0.3), grass to (0.3,0.6) and stone to (0.6,1) then it becomes impossible to have a smooth blend directly from dirt to stone, because any interpolation between dirt and stone is going to cross over grass territory, resulting in a narrow band of grass-ish blend in-between. Using a weighted blend, you can easily blend between dirt (R) and stone (B) simply by using 0 for the grass (G) color component. IMO, thresholds are only suitable for those myriad terrain "demos" you see all over youtube, and any "serious" terrain implementation is going to implement full blending or splatting. Because, really, how often in real life do you see terrain determined solely by elevation above sea level? Never, that's how often. It has an influence, sure, but it's not the sole factor.[/quote]

I was going write a response to that but it's too early for me to have a brain freeze.  Realistic texture on a procedural ground would require a combination of texture splatting, thresholds, elevation and steepness determination (with probably several) channels of mixing.

Yea. That will be a project. It would have to be implemented in a Terrain or World(Something I have) function.

-------------------------

vivienneanthony | 2017-01-02 01:02:29 UTC | #11

[quote="JTippetts"]It's not over-complicated. If anything, it's a little under-complicated due to not using the alpha channel for a 4th terrain type. Even more complicated would be to allow a second blend texture to support up to 8 terrain types. :smiley:

The issue with using thresholds is that you don't have sufficient control over terrain placement. If you assign, say, dirt to (0,0.3), grass to (0.3,0.6) and stone to (0.6,1) then it becomes impossible to have a smooth blend directly from dirt to stone, because any interpolation between dirt and stone is going to cross over grass territory, resulting in a narrow band of grass-ish blend in-between. Using a weighted blend, you can easily blend between dirt (R) and stone (B) simply by using 0 for the grass (G) color component. IMO, thresholds are only suitable for those myriad terrain "demos" you see all over youtube, and any "serious" terrain implementation is going to implement full blending or splatting. Because, really, how often in real life do you see terrain determined solely by elevation above sea level? Never, that's how often. It has an influence, sure, but it's not the sole factor.[/quote]

I was basing my original idea from something lik

[cprogramming.com/discussiona ... tml#whatis](http://www.cprogramming.com/discussionarticles/texture_generation.html#whatis)

Just found this also

[rastertek.com/tertut14.html](http://rastertek.com/tertut14.html)

-------------------------

vivienneanthony | 2017-01-02 01:02:29 UTC | #12

I'm going have to figure something out. Using the TerrainBlendTriPlanar.xml screws up the output but allows multiple textures but the normal method forces one texture but more accurate.

[url]http://imgur.com/a/auRLc[/url]


[b]
Method 1[/b]
[code]<?xml version="1.0"?>
<material>
	<technique name="Techniques/DiffAlpha.xml" quality="0" loddistance="0" />
	<texture unit="diffuse" name="Textures/TerrainTexture/SandCrackedSoil1.jpg" />
	<parameter name="UOffset" value="2048 0 0 0" />
	<parameter name="VOffset" value="0 2048 0 0" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatEmissiveColor" value="0 0 0" />
	<parameter name="MatEnvMapColor" value="1 1 1" />
	<parameter name="MatSpecColor" value="1 1 1 1" />
	<parameter name="DetailTiling" value="3072 3072" />
	<cull value="ccw" />
	<shadowcull value="ccw" />
	<depthbias constant="0" slopescaled="0" />
</material>[/code]

[b]Method 2[/b][code]
<?xml version="1.0"?>
<material>
	<technique name="Techniques/TerrainBlendTriPlanar.xml" quality="0" loddistance="0" />
	<texture unit="diffuse" name="Textures/TerrainWeights.dds" />
	<texture unit="normal" name="Textures/TerrainTexture/SandCrackedSoil1.jpg" />
	<texture unit="specular" name="Textures/TerrainTexture/SandSoil1.jpg" />
	<texture unit="emissive" name="Textures/TerrainTexture/SandSoil2.jpg" />
	<parameter name="UOffset" value="1 0 0 0" />
	<parameter name="VOffset" value="0 1 0 0" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatEmissiveColor" value="0 0 0" />
	<parameter name="MatEnvMapColor" value="0 0 0" />
	<parameter name="MatSpecColor" value="0 0 0 0" />
	<parameter name="DetailTiling" value="3072 3072" />
	<cull value="ccw" />
	<shadowcull value="ccw" />
	<depthbias constant="0" slopescaled="0" />
</material>[/code]

[quote="JTippetts"]It's not over-complicated. If anything, it's a little under-complicated due to not using the alpha channel for a 4th terrain type. Even more complicated would be to allow a second blend texture to support up to 8 terrain types. :smiley:

The issue with using thresholds is that you don't have sufficient control over terrain placement. If you assign, say, dirt to (0,0.3), grass to (0.3,0.6) and stone to (0.6,1) then it becomes impossible to have a smooth blend directly from dirt to stone, because any interpolation between dirt and stone is going to cross over grass territory, resulting in a narrow band of grass-ish blend in-between. Using a weighted blend, you can easily blend between dirt (R) and stone (B) simply by using 0 for the grass (G) color component. IMO, thresholds are only suitable for those myriad terrain "demos" you see all over youtube, and any "serious" terrain implementation is going to implement full blending or splatting. Because, really, how often in real life do you see terrain determined solely by elevation above sea level? Never, that's how often. It has an influence, sure, but it's not the sole factor.[/quote]

-------------------------

JTippetts | 2017-01-02 01:02:30 UTC | #13

In Method 1 you're using the DiffAlpha technique instead of the TerrainBlend technique so, yeah, you only get one texture...

-------------------------

vivienneanthony | 2017-01-02 01:02:30 UTC | #14

[quote="JTippetts"]In Method 1 you're using the DiffAlpha technique instead of the TerrainBlend technique so, yeah, you only get one texture...[/quote]

Joy.  I have to resort to creating a ad hoc method that works.

-------------------------

JTippetts | 2017-01-02 01:02:30 UTC | #15

What's wrong with using TerrainBlend?

-------------------------

vivienneanthony | 2017-01-02 01:02:30 UTC | #16

[quote="JTippetts"]What's wrong with using TerrainBlend?[/quote]

The shader somehow mixes the image properties as you see in the difference of the two images.

Additionally, my terrain is produced literally on the fly so I have to create a system to convert BW heightmap, slope, and normal data plus thresholds to produce a RGB usable for TerraBlend. My other options is to grid the terrain then texture splat it but I will also have to use the heightmap, slope, and normal data plus thresholds.

It would be awesome to have the on the fly full procedural creation although with xml export and import.

-------------------------

JTippetts | 2017-01-02 01:02:31 UTC | #17

[quote="vivienneanthony"][quote="JTippetts"]What's wrong with using TerrainBlend?[/quote]

The shader somehow mixes the image properties as you see in the difference of the two images.
[/quote]

I honestly don't know what you mean by this. I look at the images, but I really don't see what your problem is. Additionally, I assumed one of the images was made using your Method 1 (which uses DiffAlpha) so I'm not really sure what your problem with TerrainBlend is. (I haven't yet played with the tri-planar stuff so I can't comment on whatever issues you might have there.)

[quote]
Additionally, my terrain is produced literally on the fly so I have to create a system to convert BW heightmap, slope, and normal data plus thresholds to produce a RGB usable for TerraBlend. My other options is to grid the terrain then texture splat it but I will also have to use the heightmap, slope, and normal data plus thresholds.

It would be awesome to have the on the fly full procedural creation although with xml export and import.[/quote]

Well, if you really insist on having your terrain blending be determined by elevation then you can do something like this:

[code]
s=heightmap:GetPixel(x,y).r

dirt=Color(1,0,0,0)
grass=Color(0,1,0,0)
stone=Color(0,0,1,0)
cliff=Color(0,0,0,1)

if(s<0.5) then
  blendcolor=dirt:Lerp(grass, s/0.5)
else
  blendcolor=grass:Lerp(stone, (s-0.5)/0.5)
end

blend:SetPixel(x,y,blendcolor)
[/code]

This performs a straight linear interpolation between dirt and grass below 0.5, and grass and stone above 0.5.  Similar operations can be performed for your other operations. For instance, you can take the terrain normal at the point and dot it against vector3(0,1,0), and use the resulting value as the interpolant between blendcolor and cliff. (Note that this demonstrates a tiny limitation of the current TerrainBlend shader, which doesn't use the alpha component of the blend texture for a fourth detail layer. This is a very minor change, however. I could post the hlsl and xml code to change it to 4 detail layers if you wish.).

By using the TerrainBlend shader, each of the blend layers can be controlled in relative isolation from the other layers, giving you fuller control over terrain placement.

If you would like I can write a demonstration program for you to show you how it works.

-------------------------

