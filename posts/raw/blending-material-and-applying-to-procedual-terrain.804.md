vivienneanthony | 2017-01-02 01:03:01 UTC | #1

Hello,

After some research, help for JTippett, and more looking online. I'm trying to make code that basically gets the normal and Y-up position to get a cosine, then run it through a threshold cutoff, and the last part I'm lost. Basically, I need to tell urho3d to change the terrain texture using a lerp method. I'm not sure if I have to change material, texture2d, or get two materials from the shader and create new material then apply it.

This is to make a cliff texture to any  procedural terrain.

The code I have so far is. Any help is appreciated.

Vivienne

[code]float cutoff(float inputvalue, float pointmid, float range)
{

    /// Create valuables to calculate
    float midpoint=pointmid;

    float midpoint_low=midpoint-range;
    float midpoint_max=midpoint+range;

    float midpoint_range;
    float result;

    if(midpoint_low<0){ midpoint_low=0;}

    if(midpoint_max>1){midpoint_max=1;}

    midpoint_range=midpoint_max-midpoint_low;

    /// Calculate value to range

    if(inputvalue<midpoint_low)
    {
        result=0;
    }
    else if(inputvalue>midpoint_max)
    {
        result=1;
    }
    else
    {
        result=(inputvalue-midpoint_low)/midpoint_range;
    }

    return result;
}

int main()
{
  //rest of code

    /// testing
    float bw=2048;
    float bh=2048;
    float x=1024;
    float y=1024;

    Vector2 nworld=Vector2(x/bw, y/bh);
    Vector3 worldvalue=NormalizedToWorld( producedHeightMapImage,terrain,nworld);
    Vector3 normalvalue=terrain ->GetNormal(Vector3(worldvalue));
    float steep=abs(normalvalue.DotProduct(Vector3(0,1,0)));


}[/code]

-------------------------

vivienneanthony | 2017-01-02 01:03:01 UTC | #2

I tried this. It's still giving me a high steep value

[code]	Vector2 nworld=Vector2(x/bw, y/bh);
    Vector3 worldvalue=NormalizedToWorld( producedHeightMapImage,terrain,nworld);
    Vector3 normalvalue=terrain ->GetNormal(Vector3(worldvalue));
    float steep=abs(normalvalue.DotProduct(Vector3(0,1,0)));[/code]

GitHub
[github.com/vivienneanthony/Exis ... evelopment](https://github.com/vivienneanthony/Existence/tree/development)

-------------------------

vivienneanthony | 2017-01-02 01:03:02 UTC | #3

Update. Someone can tell me if it's wrong. Now I have to figure out the texture mixing.

[code]    /// Testing
    float bw=2048.0f;
    float bh=2048.0f;
    float x=1024.0f;
    float y=1024.0f;

    /// Get steepness
    Vector2 nworld=Vector2(x/bw, y/bh);
    Vector3 worldvalue=NormalizedToWorld( producedHeightMapImage,terrain,nworld);
    Vector3 normalvalue=terrain ->GetNormal(Vector3(worldvalue));
    float steep=1.0f-abs(normalvalue.DotProduct(Vector3(0,1,0)));

    cout << steep << " "<< normalvalue.x_<< " " << normalvalue.y_ << " " << normalvalue.z_;
[/code]

-------------------------

JTippetts | 2017-01-02 01:03:02 UTC | #4

[quote="vivienneanthony"]Hello,
 I'm not sure if I have to change material, texture2d, or get two materials from the shader and create new material then apply it.
[/quote]

You don't have to do any of that. All you need is a material that uses the TerrainBlend technique. You assign a texture for the blend texture, and give that texture an image. By modifying the colors of that image, you modify the terrain that is drawn. For example:

[code]
terrain = terrainNode:CreateComponent("Terrain")
    terrain.patchSize = 64
    terrain.spacing = Vector3(0.20, 0.08, 0.20)
    terrain.smoothing = true
    hmap=Image:new(context)
    hmap:SetSize(1025,1025,3)
    terrain.heightMap = hmap
    terrain.material = cache:GetResource("Material", "Materials/TerrainEdit.xml")
	
    blendtex=Texture2D:new(context)
    blendtex:SetSize(0,0,0,TEXTURE_DYNAMIC)
    terrain:GetMaterial():SetTexture(0,blendtex)
	
    blend=Image(context)
    blend:SetSize(512,512,4)
    blend:Clear(Color(1,0,0,0))
    blendtex:SetData(blend, false)
[/code]

This creates a terrain, sets a blank heightmap, creates an image and a texture for the blend map. The terrain is given a material. That material specifies the 3 (or, in my case, 4) detail layers to use. The colors of the blend texture specify which detail layers to draw at a given location, with the blend texture being mapped across the entire terrain.

Now, the red channel of blend represents the 1st detail layer, the green channel represents the second, and so on. If a given pixel in blend is set to Color(1,0,0,0), that means it draws fully from the first detail layer. If set to Color(0,1,0,0) it draws fully from the second detail layer. If set to Color(0.5,0.5,0,0) then it mixes the first and second layers, each at 50% strength. So if your cliff texture is at the third detail layer, then setting the pixel to Color(0,0,1,0) will set it to full cliff.

As for the steepness, one simplification that you can make is that for terrain normals that are generated on a terrain that occupies the XZ plane, you can get the angle of the normal relative to the ground plane by dot product against the UP vector, (0,1,0). The simplification is that this is equal to (0*normal.x + 1*normal.y + 0*normal.z). Of course, the 0 multiplications equal zero, so the final result of the dot product operation is simply equal to the Y component of the normal vector. The dot product operation really isn't necessary. You can just take the y and use that.

The Lerp operation (and Urho3D's Color class implements a Lerp method) is simply a linear fade from one color to the next. The t parameter (in the range of 0 to 1) determines where on the gradient scale between color A and color B to get the result. So if A=Color(1,0,0,0) and B=Color(0,1,0,0), then the operation A:Lerp(B, 0.5) will result in the color value Color(0.5,0.5,0,0), or a 50% blend between layer 1 and layer 2. Similarly, the operation A:Lerp(B,0.7) will result in a 30%/70% blend between layer 1 and 2. The closer the interpolant factor gets to 1, the more you get from layer 0, and the closer it gets to 1 the more you get from layer 2.

Now, when generating slope-based cliffs, what I do is I read the blend image to get the pixel at the current location. Usually, this is some mix of colors representing the blend of terrain I have applied to the map. Then, assuming the cliff detail layer is layer 3, represented by blend's blue channel, then I can do an operation like [b]result=currentcol:Lerp(Color(0,0,1,0), normal.y)[/b] to get a smooth blend based entirely on the slope. Applying the change, then, is as simple as calling SetPixel() with the new color then, after the full pass is completed, calling [b]blendtex:SetData(blend)[/b] to finalize the texture.

Of course, using a fade using the unmodified normal.y really isn't that useful, so I apply the cutoff/fade factors I described to you earlier. It is important to note that the value of normal.y isn't going to follow a linear progression. It represents the cosine of the angle, so as the angle decreases linearly the cosine follows the cosine curve. If you use a shallow terrain (not a large amount of Y variation) then a lot of your normal.y values will tend to cluster around the value of 1. For example, in [url=http://i.imgur.com/GeWzdoh.jpg]this image[/url], the terrain is relatively shallow, with not a lot of steep variation. Thus, the cliff blend is applied in only a few very small places. By steepening the terrain, though, I get a lot larger variance in the normal and thus the cliff terrain is applied over [url=http://i.imgur.com/MoMGMgT.jpg]much larger areas[/url]. If you are seeing normal values mostly around the top end of the curve, then you might need to either steepen your terrain variance or adjust your cutoff value.

-------------------------

vivienneanthony | 2017-01-02 01:03:02 UTC | #5

[quote="JTippetts"][quote="vivienneanthony"]Hello,
 I'm not sure if I have to change material, texture2d, or get two materials from the shader and create new material then apply it.
[/quote]

You don't have to do any of that. All you need is a material that uses the TerrainBlend technique. You assign a texture for the blend texture, and give that texture an image. By modifying the colors of that image, you modify the terrain that is drawn. For example:

[code]
terrain = terrainNode:CreateComponent("Terrain")
    terrain.patchSize = 64
    terrain.spacing = Vector3(0.20, 0.08, 0.20)
    terrain.smoothing = true
    hmap=Image:new(context)
    hmap:SetSize(1025,1025,3)
    terrain.heightMap = hmap
    terrain.material = cache:GetResource("Material", "Materials/TerrainEdit.xml")
	
    blendtex=Texture2D:new(context)
    blendtex:SetSize(0,0,0,TEXTURE_DYNAMIC)
    terrain:GetMaterial():SetTexture(0,blendtex)
	
    blend=Image(context)
    blend:SetSize(512,512,4)
    blend:Clear(Color(1,0,0,0))
    blendtex:SetData(blend, false)
[/code]

This creates a terrain, sets a blank heightmap, creates an image and a texture for the blend map. The terrain is given a material. That material specifies the 3 (or, in my case, 4) detail layers to use. The colors of the blend texture specify which detail layers to draw at a given location, with the blend texture being mapped across the entire terrain.

Now, the red channel of blend represents the 1st detail layer, the green channel represents the second, and so on. If a given pixel in blend is set to Color(1,0,0,0), that means it draws fully from the first detail layer. If set to Color(0,1,0,0) it draws fully from the second detail layer. If set to Color(0.5,0.5,0,0) then it mixes the first and second layers, each at 50% strength. So if your cliff texture is at the third detail layer, then setting the pixel to Color(0,0,1,0) will set it to full cliff.

As for the steepness, one simplification that you can make is that for terrain normals that are generated on a terrain that occupies the XZ plane, you can get the angle of the normal relative to the ground plane by dot product against the UP vector, (0,1,0). The simplification is that this is equal to (0*normal.x + 1*normal.y + 0*normal.z). Of course, the 0 multiplications equal zero, so the final result of the dot product operation is simply equal to the Y component of the normal vector. The dot product operation really isn't necessary. You can just take the y and use that.

The Lerp operation (and Urho3D's Color class implements a Lerp method) is simply a linear fade from one color to the next. The t parameter (in the range of 0 to 1) determines where on the gradient scale between color A and color B to get the result. So if A=Color(1,0,0,0) and B=Color(0,1,0,0), then the operation A:Lerp(B, 0.5) will result in the color value Color(0.5,0.5,0,0), or a 50% blend between layer 1 and layer 2. Similarly, the operation A:Lerp(B,0.7) will result in a 30%/70% blend between layer 1 and 2. The closer the interpolant factor gets to 1, the more you get from layer 0, and the closer it gets to 1 the more you get from layer 2.

Now, when generating slope-based cliffs, what I do is I read the blend image to get the pixel at the current location. Usually, this is some mix of colors representing the blend of terrain I have applied to the map. Then, assuming the cliff detail layer is layer 3, represented by blend's blue channel, then I can do an operation like [b]result=currentcol:Lerp(Color(0,0,1,0), normal.y)[/b] to get a smooth blend based entirely on the slope. Applying the change, then, is as simple as calling SetPixel() with the new color then, after the full pass is completed, calling [b]blendtex:SetData(blend)[/b] to finalize the texture.

Of course, using a fade using the unmodified normal.y really isn't that useful, so I apply the cutoff/fade factors I described to you earlier. It is important to note that the value of normal.y isn't going to follow a linear progression. It represents the cosine of the angle, so as the angle decreases linearly the cosine follows the cosine curve. If you use a shallow terrain (not a large amount of Y variation) then a lot of your normal.y values will tend to cluster around the value of 1. For example, in [url=http://i.imgur.com/GeWzdoh.jpg]this image[/url], the terrain is relatively shallow, with not a lot of steep variation. Thus, the cliff blend is applied in only a few very small places. By steepening the terrain, though, I get a lot larger variance in the normal and thus the cliff terrain is applied over [url=http://i.imgur.com/MoMGMgT.jpg]much larger areas[/url]. If you are seeing normal values mostly around the top end of the curve, then you might need to either steepen your terrain variance or adjust your cutoff value.[/quote]

1) The code I have do that partially. The heightmap is created procedurally to a image that's applied to the terrain component.
2) Using the NormalToWorld function I can get a slope of any given point.

The last point is like you mentioned the material. Which I assume is?

[code]    terrain.material = cache:GetResource("Material", "Materials/TerrainEdit.xml")
	
    blendtex=Texture2D:new(context)
    blendtex:SetSize(0,0,0,TEXTURE_DYNAMIC)
    terrain:GetMaterial():SetTexture(0,blendtex)
	
    blend=Image(context)
    blend:SetSize(512,512,4)
    blend:Clear(Color(1,0,0,0))
    blendtex:SetData(blend, false)[/code]

The cutoff function that I made should be able to determine the cliff mix based on a threshold which again.

[quote]Now, when generating slope-based cliffs, what I do is I read the blend image to get the pixel at the current location. Usually, this is some mix of colors representing the blend of terrain I have applied to the map. Then, assuming the cliff detail layer is layer 3, represented by blend's blue channel, then I can do an operation like [b]result=currentcol:Lerp(Color(0,0,1,0), normal.y)[/b] to get a smooth blend based entirely on the slope. Applying the change, then, is as simple as calling SetPixel() with the new color then, after the full pass is completed, calling [b]blendtex:SetData(blend)[/b] to finalize the texture.
[/quote]

I would have to go through x=0 to x=imagesize and I guess take the cutoff function then put it through the loop. Probably to blend between Color(1,0,0) and  Color(1,1,0);

-------------------------

vivienneanthony | 2017-01-02 01:03:04 UTC | #6

This is what I have. Hope it makes sense

[code]   /// generatescene
    terrain->GenerateProceduralHeightMap(terrainrule);

    Image * producedHeightMapImage = new Image(context_);
    producedHeightMapImage -> SetSize(2048,2048, 1, 4);
    producedHeightMapImage -> SetData(terrain -> GetData());

    /// Use Jtippet mthod
    terrain->SetMaterial(cache->GetResource<Material>("Materials/TerrainEdit.xml"));

    int bw=2048,bh=2048;

    Texture2D * blendtex=new Texture2D(context_);
    blendtex -> SetSize(0,0,0,TEXTURE_DYNAMIC);
    terrain-> GetMaterial() -> SetTexture(TU_DIFFUSE ,blendtex);

    Image * blend = new Image(context_);
    blend -> SetSize(bw,bh,4);
    blend -> Clear(Color(1,0,0,0));

    /// create blend here
    for(unsigned int x=0; x<bw; x++)
    {
        for(unsigned int y=0; y<bh; y++)
        {
            Vector2 nworld=Vector2(x/bw, y/bh);
            Vector3 worldvalue=NormalizedToWorld( producedHeightMapImage,terrain,nworld);
            Vector3 normalvalue=terrain->GetNormal(worldvalue);
            float steep=1.0f-abs(normalvalue.DotProduct(Vector3(0,1,0)));

            Color currentcolor = blend -> GetPixel(x,y);
            Color resultcolor=currentcolor.Lerp(Color(0,0,1,0), cutoff(steep,.5,.2));

            blend-> SetPixel(x,y,resultcolor);
        }
    }

    blendtex ->SetData(blend ->GetNextLevel (), false);[/code]

-------------------------

vivienneanthony | 2017-01-02 01:03:06 UTC | #7

Im having a problem. My code and JTippet code works. I loaded a image and inclination or steepness rendered in the blended text.

But when I use the blend texture from the generated image. The math part works if i say any point but the texture isn't blending.

I will compare the image from graphics program to the generated one. 

Could the problem be MIP levels? How can I set to one?  Is get the function get the next MIP level correct?

-------------------------

JTippetts | 2017-01-02 01:03:06 UTC | #8

blend->GetNextLevel() gets the next mip level down from the current image. Perhaps you want to just do blendtex:SetData(blend,false) instead?

-------------------------

vivienneanthony | 2017-01-02 01:03:06 UTC | #9

[quote="JTippetts"]blend->GetNextLevel() gets the next mip level down from the current image. Perhaps you want to just do blendtex:SetData(blend,false) instead?[/quote]


I am going try it when I get home. I'm going create a component that hold information for procedural generation.

-------------------------

vivienneanthony | 2017-01-02 01:03:07 UTC | #10

Someone recommended another solution. For testing I am using a preformatted image. I'm not sure what's causing a problem in scale. I'm post the code and example.

Gallery
[imgur.com/a/UEgzR](http://imgur.com/a/UEgzR)

Black/White is the terrain texture
Red/Blue is the lerped results
Merged is a overlap

[b]Function - Cutoff/Threshold[/b]
[code]
float cutoff(float inputvalue, float pointmid, float range, bool debug)
{

    /// Create valuables to calculate
    float midpoint=pointmid;

    float midpoint_low=midpoint-range;
    float midpoint_high=midpoint+range;
    float midpoint_range=midpoint_range=midpoint_high-midpoint_low;

    float result;
    
    if(midpoint_low<0.0f)
    {
        midpoint_low=0.0f;
    }

    if(midpoint_high>1.0f)
    {
        midpoint_high=1.0f;
    }


    if(midpoint_low>inputvalue)
    {
        result=0;
        cout << "set zero";
    }
    else if(inputvalue>midpoint_high)
    {
        result=1;
        cout << "set one";
    }
    else
    {
        result=(inputvalue-midpoint_low)/midpoint_range;
        cout << "set" << result;
    }

    return result;
}[/code]

[b]Function - Normalized[/b]
[code]
Vector3 NormalizedToWorld(Image *height, Terrain *terrain, Vector2 normalized)
{
    if(!terrain || !height) return Vector2(0,0);
    Vector3 spacing=terrain->GetSpacing();
    int patchSize=terrain->GetPatchSize();
    IntVector2 numPatches=IntVector2((height->GetWidth()-1) / patchSize, (height->GetHeight()-1) / patchSize);
    Vector2 patchWorldSize=Vector2(spacing.x_*(float)(patchSize*numPatches.x_), spacing.z_*(float)(patchSize*numPatches.y_));
    Vector2 patchWorldOrigin=Vector2(-0.5f * patchWorldSize.x_, -0.5f * patchWorldSize.y_);
    return Vector3(patchWorldOrigin.x_+normalized.x_*patchWorldSize.x_, 0, patchWorldOrigin.y_+normalized.y_*patchWorldSize.y_);
}
[/code]
[b]Main Code[/b]
[code]  /// Generate Terrain
    Node* terrainNode = scene_->CreateChild("Terrain");

    Terrain* terrain = terrainNode->CreateComponent<Terrain>();
    terrain->SetPatchSize(64);
    terrain->SetSpacing(Vector3(1.0f, 1.0f, 1.0f)); /// Spacing between vertices and vertical resolution of the height map
    terrain->SetSmoothing(true);
    terrain->SetCastShadows(true);

    /// generatescene
    terrain->SetHeightMap(cache->GetResource<Image>("Textures/terraintest.png"));
    terrain->ApplyHeightMap();

    //terrain->GenerateProceduralHeightMap(terrainrule);

    //Image * producedHeightMapImage = new Image(context_);
    Image * producedHeightMapImage = cache->GetResource<Image>("Textures/terraintest.png");
    producedHeightMapImage -> SetSize(2048,2048, 1, 4);

    /// Use Jtippet mthod
    terrain->SetMaterial(cache->GetResource<Material>("Materials/TerrainEdit.xml"));

    int bw=2048,bh=2048;

    Texture2D * blendtex=new Texture2D(context_);
    blendtex -> SetNumLevels(1);
    blendtex -> SetSize(0,0,0,TEXTURE_DYNAMIC);
    terrain-> GetMaterial() -> SetTexture(TU_DIFFUSE ,blendtex);

    /// Shared pointer
    SharedPtr<Image> blend;

    blend = new Image(context_);
    blend -> SetSize(bw,bh,1,4);
    blend -> Clear(Color(1,0,0,1));

    float steep=0.0f;
    float steepforlerp=0.0f;

    /// create blend here
    for(unsigned int x=0; x<bw; x++)
    {
        for(unsigned int y=0; y<bh; y++)
        {
            Vector2 nworld=Vector2(x/(float)bw, y/(float)bh);
            Vector3 worldvalue=NormalizedToWorld( producedHeightMapImage,terrain,nworld);
            Vector3 normalvalue=terrain->GetNormal(worldvalue);

            steep=1.0f-fabs(normalvalue.DotProduct(Vector3(0,1,0)));
            steepforlerp=cutoff(steep,0.5f,0.20f,false);

            Color currentcolor = blend -> GetPixel(x,y);
            Color resultcolor=currentcolor.Lerp(Color(0,0,1,1), steepforlerp);

            blend-> SetPixel(x,y,resultcolor);
        }
    }

    blend -> 	FlipVertical ();
    blend -> 	SavePNG ("terrainsteep.png");


    blendtex ->SetData(blend, true);[/code]

-------------------------

vivienneanthony | 2017-01-02 01:03:07 UTC | #11

Image of difference

[i.imgur.com/OhYJemF.png](http://i.imgur.com/OhYJemF.png)

-------------------------

JTippetts | 2017-01-02 01:03:07 UTC | #12

Make sure that your terrain heightmap is sized 2^n+1 rather than 2^n. That is, instead of using an image 2048x2048 for the heightmap, use one that's 2049x2049. Otherwise, the last terrain patch row and column in X and Z won't be generated, meaning that the blend map will extend out beyond the edges of the terrain itself.

-------------------------

vivienneanthony | 2017-01-02 01:03:08 UTC | #13

[quote="JTippetts"]Make sure that your terrain heightmap is sized 2^n+1 rather than 2^n. That is, instead of using an image 2048x2048 for the heightmap, use one that's 2049x2049. Otherwise, the last terrain patch row and column in X and Z won't be generated, meaning that the blend map will extend out beyond the edges of the terrain itself.[/quote]

So, I should do it  for the procedual terrain heightmap image I created? Instead of 2048.

I'm just making sure.  I have to probably add the procedural seed as part of a component to Terrain. So,  information can be saved or retrieved. Additionally, create a better randomize system separate for mine for any procedural stuff for content generation.     (I kinda would like the math part to be part assembly so it can be super dirt fast). Oh well.

That might be in the future.

-------------------------

JTippetts | 2017-01-02 01:03:09 UTC | #14

[quote="vivienneanthony"]
So, I should do it  for the procedual terrain heightmap image I created? Instead of 2048.
[/quote]

Yes. Do it for any image that you use as a heightmap, whether you load it from a file or generate it procedurally. The way the terrain calculates the number of terrain patches to build is by [b]IntVector2((heightMap_->GetWidth() - 1) / patchSize_, (heightMap_->GetHeight() - 1) / patchSize_)[/b] The size should be a number that if you subtract 1 from it, the result is evenly divisible by your patch size (default: 32). For instance, if you have a patch size of 32 and a heightmap size of 2049, the number of patches in X and Z comes out to (2049-1)/32, or 64 patches. However, if you use 2048, then you end up with only (2048-1)/32 or 63 patches (integer division). Meaning that the last patch row and column are not built, and the heightmap is trimmed off so that only the first 2017x2017 pixels of the heightmap are used in generating terrain (the size of 63 patches + 1 pixel).

[quote]

I'm just making sure.  I have to probably add the procedural seed as part of a component to Terrain. So,  information can be saved or retrieved. Additionally, create a better randomize system separate for mine for any procedural stuff for content generation.     (I kinda would like the math part to be part assembly so it can be super dirt fast). Oh well.

That might be in the future.[/quote]

I wouldn't really recommend adding anything directly to Terrain itself. I'd recommend instead writing your own separate component so you don't have to modify the Urho3D library itself. Modifying the library means that every time you pull from upstream you have to do a merge, and given the amount of churn that Urho3D sometimes has in master, you might end up spending a lot more time than you really want to fixing conflicts. And besides, Terrain probably shouldn't have to care exactly how the heightmap data is constructed. It can do what it needs to do without knowing the details, so from the perspective of the single responsibility principle, the procedural stuff just doesn't belong in there.

-------------------------

vivienneanthony | 2017-01-02 01:03:10 UTC | #15

Ah. I agree with you 200%. I have to replace the diamond-method I use also because it expects the heightmap to be in square increments (1024,2048). As for component, maybe a TerrainProcedural component would work. When I'm finish I have to tie it into the Editor in the future.  The thing I haven't figured out is getting the texture to look more decent not tiled weirdly.

[quote="JTippetts"][quote="vivienneanthony"]
So, I should do it  for the procedual terrain heightmap image I created? Instead of 2048.
[/quote]

Yes. Do it for any image that you use as a heightmap, whether you load it from a file or generate it procedurally. The way the terrain calculates the number of terrain patches to build is by [b]IntVector2((heightMap_->GetWidth() - 1) / patchSize_, (heightMap_->GetHeight() - 1) / patchSize_)[/b] The size should be a number that if you subtract 1 from it, the result is evenly divisible by your patch size (default: 32). For instance, if you have a patch size of 32 and a heightmap size of 2049, the number of patches in X and Z comes out to (2049-1)/32, or 64 patches. However, if you use 2048, then you end up with only (2048-1)/32 or 63 patches (integer division). Meaning that the last patch row and column are not built, and the heightmap is trimmed off so that only the first 2017x2017 pixels of the heightmap are used in generating terrain (the size of 63 patches + 1 pixel).

[quote]

I'm just making sure.  I have to probably add the procedural seed as part of a component to Terrain. So,  information can be saved or retrieved. Additionally, create a better randomize system separate for mine for any procedural stuff for content generation.     (I kinda would like the math part to be part assembly so it can be super dirt fast). Oh well.

That might be in the future.[/quote]

I wouldn't really recommend adding anything directly to Terrain itself. I'd recommend instead writing your own separate component so you don't have to modify the Urho3D library itself. Modifying the library means that every time you pull from upstream you have to do a merge, and given the amount of churn that Urho3D sometimes has in master, you might end up spending a lot more time than you really want to fixing conflicts. And besides, Terrain probably shouldn't have to care exactly how the heightmap data is constructed. It can do what it needs to do without knowing the details, so from the perspective of the single responsibility principle, the procedural stuff just doesn't belong in there.[/quote]

-------------------------

vivienneanthony | 2017-01-02 01:03:12 UTC | #16

Hello. 

I was able to implement the shader and elevation. A image is here [i.imgur.com/6sCwGne.png](http://i.imgur.com/6sCwGne.png)

The only problem I have. When I try to get the normal for a spot I think it's not being calculated correctly.  Basically I choose a random position like 17. Then I subtract half of it. So, I always get a position -X,+X, -Y,+Y to 0,0. 

[code]   /// Pick a random spotskx
        Spotx=rand()%1024;
        Spotz=rand()%1024;

        /// Calculat z,x location
        //randomSpotx=((float)Spotx/100)-768.0f;
        //randomSpotz=((float)Spotz/100)-768.0f;

        randomSpotx=(float)Spotx-512.0f;
        randomSpotz=(float)Spotz-512.0f;
[/code]

When I calculate the normal.  I use position+1024. So, it's centered to the size of the height map dimensions since 0,0 is 1024,1024 half of 2048,2048. Since the original heightmap image is 2049. I'm trying to figuring out should I use 1023 or 1025.

[code]
 float xposition=position_x+1024.0f;
 float zposition=position_z+1024.0f;

            Color terrainHeightvalue=terrainHeightMap->GetPixel(xposition, zposition);

            if(terrainHeightvalue.r_<.50)
            {
                continue;
            }

            Vector3 normalvalue=terrain -> GetNormal(Vector3(xposition+1.0f,0.0f,zposition+1.0f));

            float steep=1.0f-normalvalue.y_;

            if(steep>.009)
            {
                continue;
            }

[/code]

-------------------------

vivienneanthony | 2017-01-02 01:03:12 UTC | #17

I am placing my development code on Github. It has to be cleaned up. It looks like there is a offset of 1. 

The code I mentioned is at 

[b]https://github.com/vivienneanthony/Existence/blob/master/Source/ExistenceApps/ExistenceClient/ExistenceClient.cpp
[github.com/vivienneanthony/Exis ... dBuild.cpp](https://github.com/vivienneanthony/Existence/blob/master/Source/ExistenceApps/ExistenceClient/WorldBuild.cpp)[/b]

[code]void ExistenceClient::GenerateScene(const time_t &timeseed, terrain_rule terrainrule)
int WorldBuild::CreateTreeObjectAlongPath(float worldsize_x, float worldsize_y, float x, float z, float numberofobjects, float length, Image * terrainHeightMap)
[/code]

I created a stripped down procedural component. So, I'm thinking of setting terrainrules and variables there. As a logiccomponent it can retrieved in the functions relating to content creation.

-------------------------

