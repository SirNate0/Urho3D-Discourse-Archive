vivienneanthony | 2018-03-05 19:37:06 UTC | #1

Hmmm.

Is it possible to do this with Urho3d? Like something like "WorldEnvironment" where space is defined. The higher you go up the horizon changes to black or whatever is defined. If it goes high enougth a  "WorldSpace" is loaded which shows the world for a far expect. I'll refine the idea more.

Just random thought.

https://www.youtube.com/watch?v=0bQz5ugtfLY

Vivienne

-------------------------

cadaver | 2017-01-02 00:59:42 UTC | #2

This is just as doable in Urho as any other generic scenegraph/renderer, but it doesn't do anything specifically to help you. The application must manage all the content creation and also the LOD transitions in the larger scale (*); Urho just supplies a "dumb" octree and camera frustum and renders everything that's in the camera view.

(*) The StaticModel / AnimatedModel classes do manage LOD for something like displaying a far-away tree at a lower amount of polygons if the model asset defines different LOD levels and the transition distances, but I don't think that's directly usable for this kind of planetary LOD.

-------------------------

vivienneanthony | 2018-03-04 18:18:04 UTC | #3

[quote="cadaver"]
(*) The StaticModel / AnimatedModel classes do manage LOD for something like displaying a far-away tree at a lower amount of polygons if the model asset defines different LOD levels and the transition distances, but I don't think that's directly usable for this kind of planetary LOD.
[/quote]

Yea. I'm assuming it will be trickie. The way I imagine it is I try to illustrate it.

camera  -> field of view -> statics models -> plane(after certain distances)

If something is in the far distance bypassing a certain point, anything after the plane have to be projected onto the plane. I'm assuming in real life, probably considering it a canvas like a matte painting. 

The sheet of paper for example 5 kilometers in front of the camera but the paper roject 5km to infinity.

-------------------------

vivienneanthony | 2018-03-04 18:18:58 UTC | #4

I'm looking at the engine.

I created a function in terrain.cpp that basically named generateheightmap().

I was planning to pass a created Image. Still if the Image object class would be the best route but.

Would it be just better to replicate "bool Image::Load(Deserializer& source)" to "bool Image:LoadPerlin" which either uses stb or libnoise and change the Image settings to use that information. Simply using the "bool Image::Load(Deserializer& source)" function as a template. I'm looking at "GetImageData" which I assume I'll use the replacement code their.

Calculating a memory area the size of width, height, depth, and components. [b]Which I can set to 2048*2048*(not sure what depth means)*(not sure what components means)?[/b]
Using STB I can calulate each x,y,z!

[code]
bool Image::LoadPerlinSTB(void)
{
    PROFILE(LoadImage);


    // Not DDS, KTX or PVR, use STBImage to load other image formats as uncompressed

    int width, height;
    unsigned components;
    
    unsigned char* pixelData = GetImageData(source, width, height, components);
    /// modify source which would be the memory location the stb generated area
        if (!pixelData)
    {
        LOGERROR("Could not load image " + source.GetName() + ": " + String(stbi_failure_reason()));
        return false;
    }
    SetSize(width, height, components);
    SetData(pixelData);
    FreeImageData(pixelData);

    return true;
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:01 UTC | #5

Hello

This is what I have so far. 

Vivienne

-------------------------

vivienneanthony | 2017-01-02 01:00:01 UTC | #6

Hello

This is what I have so far. Way to generate Perlin using STB? WIth this image possible the texture can be saved on a need to basis?

Vivienne

[code]
bool Terrain::GenerateHeightMap()
{
    // Generate Image
    Image * perlinimage = new Image(context_);

    if(!perlinimage->GeneratePerlin(2048,2048,0))
    {
        return false;
    }

    bool success = SetHeightMapInternal(perlinimage, true);

    return success;
}

bool Image::GeneratePerlin(int width, int height, unsigned components)
{
    // create a location for pixelData
    unsigned char* pixelData;
    int depth;

    // not sure of what the following is
    components=4;       // rgba 4 components
    depth=1;            // meaning 8-bit

    unsigned dataSize = height*width*depth*components;

    // code
    SharedArrayPtr<unsigned char> buffer(new unsigned char[dataSize]);

    // null the memory area
    for(int x=0; x<width; x++)
    {
        for(int y=0; y<height; y++)
        {
            for(int componentsidx=0; componentsidx<components; componentsidx++)
            {
                buffer[x*y*componentsidx]=0;
            }
        }
    }

    // Manipulation here

    // point pixelData to buffer
    pixelData=buffer;

    // set image information
    SetSize(width, height, depth, components);
    SetData(pixelData);
    FreeImageData(pixelData);

    return false;
}

[/code]

-------------------------

friesencr | 2017-01-02 01:00:01 UTC | #7

If you mean saved to disk the image class has a SavePNG, SaveBMP, and SaveJPG functions

-------------------------

vivienneanthony | 2018-03-04 18:20:25 UTC | #8

That's is what I'm trying. Will with the code here. I get a fuchsia color. If I attempt to change the starting value when initialized it garbage some of the texture when shaped. So maybe I'm not setting the memory right. I'm assuming components would be RGBA and depth(not sure).

VIvienne

[code]
bool Image::GeneratePerlin(int width, int height, unsigned components)
{
    // create a location for pixelData
    unsigned char* pixelData;
    int depth;

    // not sure of what the following is
    components=4;       // rgba 4 components
    depth=1;            // meaning 8-bit

    unsigned dataSize = height*width*depth*components;

    // code
    SharedArrayPtr<unsigned char> buffer(new unsigned char[dataSize]);

    // null the memory area
    for(int z=0; z<width; ++z)
    {
       for(int x=0; x<height; ++x)
        {
            for(int componentsidx=0; componentsidx<components; ++componentsidx)
          {
                buffer[z*x*componentsidx]=0;
            }
        }
    }

    //point pixelData to buffer
    pixelData=buffer;

      // set image information
    SetSize(width, height, depth, components);
    SetData(pixelData);
   //FreeImageData(pixelData);

    return false;
}
[/code]

-------------------------

friesencr | 2017-01-02 01:00:01 UTC | #9

I have actually been working on a height map generator since you brought it up.  Its not there yeat but here is my code to get you started.  I am still learning the basics of contiguous noise.  The general idea is that you need to layer the perlin noise to give it more character.  this perlin function gets interpolated between coordinates.  At the even integers there isn't much to show but in between the integers there is lots of wild things happening.  I have found some good combinations but no great combinations.  This code is commented out but the idea is there. 

[code]
      heightMap_ = new Image(context_);
      heightMap_->SetSize(terrainSize, terrainSize, 3);
      terrain_->SetHeightMap(heightMap_);

      float offset = sin(sceneTimer_.GetMSec(false) * 0.0001) * terrainDivisionSizeN3;

      for (unsigned x = 0; x < terrainSize; x++)
      {
         for (unsigned y = 0; y < terrainSize; y++)
         {
            float n1X = x / terrainDivisionSizeN1;
            float n1Y = y / terrainDivisionSizeN1;
            float n1 = stb_perlin_noise3(n1X+offset, n1Y+offset, 1.0); //, terrainDivisionsN1, terrainDivisionsN1, terrainDivisionsN1);
            /* n1 = (n1 + 1.0) / 2.0; */

            /* float n2X = x / terrainDivisionSizeN2; */
            /* float n2Y = y / terrainDivisionSizeN2; */
            /* float n2 = stb_perlin_noise3(n2X+offset, n2Y+offset, 1.0); //, terrainDivisionsN2, terrainDivisionsN2, terrainDivisionsN2); */
            /* n2 *= 0.8; */

            /* float n3X = x / terrainDivisionSizeN3; */
            /* float n3Y = y / terrainDivisionSizeN3; */
            /* float n3 = stb_perlin_noise3(n3X+offset, n3Y+offset, 1.0); //, terrainDivisionsN3, terrainDivisionsN3, terrainDivisionsN3); */
            /* n3 *= 0.6; */

            /* float n4X = x / terrainDivisionSizeN4; */
            /* float n4Y = y / terrainDivisionSizeN4; */
            /* float n4 = stb_perlin_noise3(n4X+offset, n4Y+offset, 1.0); //, terrainDivisionsN4, terrainDivisionsN4, terrainDivisionsN4); */
            /* n4 *= 0.4; */

            /* float n5X = x / terrainDivisionSizeN5; */
            /* float n5Y = y / terrainDivisionSizeN5; */
            /* float n5 = stb_perlin_noise3(n5X+offset, n5Y+offset, 1.0); //, terrainDivisionsN5, terrainDivisionsN5, terrainDivisionsN5); */
            /* n4 *= 0.3; */

            /* float n = (n1 + n2 + n3 + n4 + n5) / 5.0; */

            float h = (n1 + 1.0) / 2.0; // set noise from -1,1 to 0,1 for color
            h = n1;

            /* if (h < 0.45) */
            /*    h = 0.0; */

            /* h = pow(h,colorMag); */
            Color c =  Color(h,h,h);
            heightMap_->SetPixel(x,y,c);
         }
      }
      /* heightMap_->SavePNG("heightmap.png"); */
      terrain_->SetHeightMap(heightMap_);

[/code]

Here is a function that performs over a pointer to a buffer of data.  This data is aligned to work with stb_image_write and is agnostic to Urho.

[code]

unsigned rgba32ToUInt(unsigned r, unsigned g, unsigned b, unsigned a)
{
    return (r&255) + ((g&255) << 8) + ((b&255) << 16) + ((a&255) << 24);
}

void generatePerlinNoise1(
        unsigned* data,
        unsigned width,
        unsigned height,
        unsigned octaves, 
        float xOffset, 
        float yOffset, 
        float zOffset, 
        int xWrap, 
        int yWrap, 
        int zWrap, 
        float o1,
        float o2,
        float o3,
        float o4,
        float o5,
        float o6,
        float o7,
        float o8
    )
{
    float mag[] = {o1, o2, o3, o4, o5, o6, o7, o8};
    for (unsigned o = 0; o<octaves; o++)
    {
        float oSize = (o+1) << o;
        float oxDiv = oSize / width;
        float oyDiv = oSize / height;
        for(unsigned x = 0; x<width; x++)
        {
            for(unsigned y = 0; y<height; y++)
            {
                float hx = (float)x / (float)width;
                float hy = (float)y / (float)height;
                float noise = stb_perlin_noise3(
                        (x + xOffset) * oxDiv,
                        (y + yOffset) * oyDiv, 
                        zOffset,
                        xWrap,
                        yWrap,
                        zWrap
                );
                noise = (noise + 1.0) / 2.0; // set range to 0 - 1
                noise *= mag[o];
                unsigned col = noise * 255;
                int index = x+y*width;
                col = rgba32ToUInt(col, col * hx, col * hy, 255);
                data[index] += col;
            }
        }
    }
}

[/code]

-------------------------

vivienneanthony | 2018-03-05 19:40:39 UTC | #10

Part A - Implementation
I played around with your code and will look at it more tomorrow. I was able to get the code to at least work in Urho3D structure and was able to use a Image::SavePNG to save the produced image. I'm assuming with a little conversion it can generate height maps on the fly. Additionally, the octaves parameters can be passed through terrain so it can implemented through hard coding, xml, and the Editor. I thinking making a grayscale conversion is needed to make it work even more before using the "    //bool success = SetHeightMapInternal(perlinimage, true);" command.

Part B - Code - Edited 9/11/14
Also, very edited stb_perlin.h that can be added to ThirdParty/STB.

[sourceforge.net/projects/proteu ... Party/STB/](https://sourceforge.net/projects/proteusgameengine/files/Existence/Source/Engine/ThirdParty/STB/)

Part C - Code - Edited 9/12/14
I passed width and height to Perlin function. I'm thinking of passing the octaves from GeneratePerlin in the Terrain class to the Perlin function.

Note: Since Perlin is in the Image class I am thinking generated Perlins can be used to create weightmaps for textures and other details.

[code]
bool Image::GeneratePerlin(int width, int height, unsigned components)
{
    /// Create a pointer location for pixelData
    unsigned char* pixelData;

    unsigned int * buffer;

    /// Sure components to 4 for RGBA
    components=4;
    int depth=1;

    /// calculate memory needed to match pixelData and buffer
    unsigned dataSize = height*width*depth*components;

    /// Allocate buffer
    buffer = (unsigned int *) malloc(dataSize);

    /// Generate noise - Currently 8 octaves
    generatePerlinNoise1(buffer,width,height,8,0.0f,0.0f,0.0f,0,0,0,1.0f,0.0f,0.0f,0.0f,0.0f,0.0f,0.0f,0.0f);

    /// Point pixelData to buffer memory
    pixelData = (unsigned char *) buffer;

    /// Set image size
    SetSize(width, height, 1, components);
    CopyData(pixelData);

    /// Free Memory
    FreeImageData(pixelData);

    return true;
}

unsigned Image::rgba32ToUInt(unsigned r, unsigned g, unsigned b, unsigned a)
{
    return (r&255) + ((g&255) << 8) + ((b&255) << 16) + ((a&255) << 24);
}

///
void Image::generatePerlinNoise1(
    unsigned* data,
    unsigned width,
    unsigned height,
    unsigned octaves,
    float xOffset,
    float yOffset,
    float zOffset,
    int xWrap,
    int yWrap,
    int zWrap,
    float o1,
    float o2,
    float o3,
    float o4,
    float o5,
    float o6,
    float o7,
    float o8
)
{
    float mag[] = {o1, o2, o3, o4, o5, o6, o7, o8};
    for (unsigned o = 0; o<octaves; o++)
    {
        float oSize = (o+1) << o;
        float oxDiv = oSize / width;
        float oyDiv = oSize / height;
        for(unsigned x = 0; x<width; x++)
        {
            for(unsigned y = 0; y<height; y++)
            {
                float hx = (float)x / (float)width;
                float hy = (float)y / (float)height;
                float noise = stb_perlin_noise3(
                                  (x + xOffset) * oxDiv,
                                  (y + yOffset) * oyDiv,
                                  zOffset,
                                  xWrap,
                                  yWrap,
                                  zWrap
                              );
                noise = (noise + 1.0) / 2.0; // set range to 0 - 1
                noise *= mag[o];
                unsigned col = noise * 255;
                int index = x+y*width;
                col = rgba32ToUInt(col, col * hx, col * hy, 255);
                data[index] += col;
            }
        }
    }
}

Part  - C
I think the Perlin can probably be used to create texture weight maps a
void Image::CopyData(const unsigned char* pixelData)
{
    if (!data_)
        return;

    memcpy(data_, pixelData, width_ * height_ * depth_ * components_);
}

bool Terrain::GenerateHeightMap()
{
    /// Generate Image
    Image * perlinimage = new Image(context_);
    bool success = false;


    /// Create Image
    if(!perlinimage->GeneratePerlin(256,256,0))
    {

        return false;
    }

    perlinimage->SavePNG(String("/media/home2/vivienne/Existence/Bin/test.png"));


    //bool success = SetHeightMapInternal(perlinimage, true);

    return success;
}


[/code]

-------------------------

vivienneanthony | 2018-03-05 19:40:58 UTC | #11

Do you know how the color image is stored in memory? I just tried to do the following code. It rewrite the image to some transparent gradiant and noise. So I off a byte or something.

I'm using the first average method.
[tannerhelland.com/3643/grays ... rithm-vb6/](http://www.tannerhelland.com/3643/grayscale-image-algorithm-vb6/)

[code]
{
    // create temporary area
    unsigned char * tempdata_ = new unsigned char[width_ * height_ * depth_*components_];
    unsigned char grey;

    // loop
    for(unsigned width=0; width<width_;width++)
    {
        for(unsigned height=0; height<height_;height++)
        {
                grey=(data_[(width*height)+0]+data_[(width*height)+1]+data_[(width*height)+2])/3;

                tempdata_[(width*height)+0]=grey;
                tempdata_[(width*height)+1]=grey;
                tempdata_[(width*height)+2]=grey;
        }
    }

    // copy data
    memcpy(data_, tempdata_, width_*height_*depth_*components_);

    return;

}
[/code]

-------------------------

vivienneanthony | 2018-03-05 19:41:17 UTC | #12

I am using the code utilizing [tannerhelland.com/3643/grays ... rithm-vb6/](http://www.tannerhelland.com/3643/grayscale-image-algorithm-vb6/) 

I just have to add some clear nerirt code to clear the temporary memory to the functions I created the uncomment the actual code that creates the terrain.

This look interesting to add as a Image function since I have GenerateGrayscale() made. The link is [notes.ericwillis.com/2009/11/pix ... th-csharp/](http://notes.ericwillis.com/2009/11/pixelate-an-image-with-csharp/)

Mindcraft type terrain possibility.

So technically some type of procedural terrain can be implemented and since the Perlin noise plays with a image.  It can be manipulated for other things like terrain details from textures and probably weight maps for placing objects.

It's made for hard coding so the next trick is adding the ability to use the function in the Editor.  If someone wants to make it here! 

The code:

[code]
void Image::generateGrayScale(void)
///
{
      // create temporary area
        unsigned char * tempdata_ ;

        tempdata_=(unsigned char*) malloc(width_ * height_ * depth_*components_);

        unsigned char grey;
        unsigned width = components_;

        // loop
        for(unsigned int y=0; y<height_;y++)
        {
            for(unsigned int x=0; x<width_;x++)
            {
                grey=(data_[(y*components_*width_)+(x*components_)+0]+data_[(y*components_*width_)+(x*components_)+1]+data_[(y*components_*width_)+(x*components_)+2])/3;

                tempdata_[(y*components_*width_)+(x*components_)+0]=grey;
                tempdata_[(y*components_*width_)+(x*components_)+1]=grey;
                tempdata_[(y*components_*width_)+(x*components_)+2]=grey;
                tempdata_[(y*components_*width_)+(x*components_)+3]=255;
            }
        }

        /// Point pixelData to buffer memory
        memcpy(data_, (unsigned char *)tempdata_, width_ * height_ * depth_ * components_);

        return;

    }

}


[/code]

-------------------------

vivienneanthony | 2018-03-05 19:41:46 UTC | #13

This is a newer copy with free memory to prevent crashes.  I also allowed setting of the Perlin when calling it from the Image class. I have to look at the Editor and terrain class about fully implementing this as a new Terrain component.

If somone knows how or would take a bite at it. That would be super! and we'll start to have procedural abilities built into Urho3D starting with Terrain.

[code]
bool Terrain::GenerateHeightMap()
{
    /// Generate Image
    Image * perlinimage = new Image(context_);
    bool success = false;


    /// Create Image
    if(!perlinimage->GeneratePerlin(1024,1024,8,1.0f,.5f,0.1f,0.0f,0.0f,0.0f,0.0f,0.0f))
    {

        return false;
    }

    perlinimage->generateGrayScale();

    perlinimage->SavePNG(String("/media/home2/vivienne/Existence/Bin/test.png"));


    //bool success = SetHeightMapInternal(perlinimage, true);

    return success;
}


bool Image::GeneratePerlin(const int &width, const int &height,const unsigned &octaves,
                        const float &o1,
                        const float &o2,
                        const float &o3,
                        const  float&o4,
                        const float &o5,
                        const float &o6,
                        const float &o7,
                        const float &o8)
{
    /// Create a pointer location for pixelData
    unsigned char* pixelData;
    unsigned int * buffer;
    unsigned int components=4;

    /// Sure components to 4 for RGBA
    int depth=1;

    /// calculate memory needed to match pixelData and buffer
    unsigned dataSize = height*width*depth*components;

    /// Allocate buffer
    buffer = (unsigned int *) malloc(dataSize);

    /// Generate noise - Currently 8 octaves
    generatePerlinNoise1(buffer,width,height,octaves,0.0f,0.0f,0.0f,0,0,0,o1,o2,o3,o4,o5,o6,o7,o8);

    /// Point pixelData to buffer memory
    pixelData = (unsigned char *) buffer;

    /// Set image size
    SetSize(width, height, 1, components);
    CopyData(pixelData);

    /// Free Memory
    FreeImageData(pixelData);

    return true;
}

unsigned Image::rgba32ToUInt(unsigned r, unsigned g, unsigned b, unsigned a)
{
    return (r&255) + ((g&255) << 8) + ((b&255) << 16) + ((a&255) << 24);
}

///
void Image::generatePerlinNoise1(
    unsigned* data,
    unsigned width,
    unsigned height,
    unsigned octaves,
    float xOffset,
    float yOffset,
    float zOffset,
    int xWrap,
    int yWrap,
    int zWrap,
    float o1,
    float o2,
    float o3,
    float o4,
    float o5,
    float o6,
    float o7,
    float o8
)
{
    float mag[] = {o1, o2, o3, o4, o5, o6, o7, o8};
    for (unsigned o = 0; o<octaves; o++)
    {
        float oSize = (o+1) << o;
        float oxDiv = oSize / width;
        float oyDiv = oSize / height;
        for(unsigned x = 0; x<width; x++)
        {
            for(unsigned y = 0; y<height; y++)
            {
                float hx = (float)x / (float)width;
                float hy = (float)y / (float)height;
                float noise = stb_perlin_noise3(
                                  (x + xOffset) * oxDiv,
                                  (y + yOffset) * oyDiv,
                                  zOffset,
                                  xWrap,
                                  yWrap,
                                  zWrap
                              );
                noise = (noise + 1.0) / 2.0; // set range to 0 - 1
                noise *= mag[o];
                unsigned col = noise * 255;
                int index = x+y*width;
                col = rgba32ToUInt(col, col * hx, col * hy, 255);
                data[index] += col;
            }
        }
    }
}

void Image::generateGrayScale(void)
///
{
    // create temporary area
    unsigned char * tempdata_ ;

    tempdata_=(unsigned char*) malloc(width_ * height_ * depth_*components_);

    unsigned char grey;
    unsigned width = components_;

    // loop
    for(unsigned int y=0; y<height_; y++)
    {
        for(unsigned int x=0; x<width_; x++)
        {
            grey=(data_[(y*components_*width_)+(x*components_)+0]+data_[(y*components_*width_)+(x*components_)+1]+data_[(y*components_*width_)+(x*components_)+2])/3;

            tempdata_[(y*components_*width_)+(x*components_)+0]=grey;
            tempdata_[(y*components_*width_)+(x*components_)+1]=grey;
            tempdata_[(y*components_*width_)+(x*components_)+2]=grey;
            tempdata_[(y*components_*width_)+(x*components_)+3]=255;
        }
    }

    /// Point pixelData to buffer memory
    memcpy(data_, (unsigned char *)tempdata_, width_ * height_ * depth_ * components_);

    free(tempdata_);

    return;

}
[/code]

-------------------------

vivienneanthony | 2018-03-05 19:42:45 UTC | #14

Hard coded implementation call to Terrain generate perlin function.

https://www.youtube.com/watch?v=bKRzQbz6FUM&list=UUTObP1VzcIglm7uTgUBQjaw

Function called in scene creation. The line  [b]terrain->GenerateHeightMap();[/b]

[code]
     //Terrain
        Node* terrainNode = scene_->CreateChild("Terrain");

        Terrain* terrain = terrainNode->CreateComponent<Terrain>();
        terrain->SetPatchSize(64);
        terrain->SetSpacing(Vector3(2.0f, 0.8f, 2.0f)); // Spacing between vertices and vertical resolution of the height map
        terrain->SetSmoothing(true);

        terrain->GenerateHeightMap();

        terrain->SetMaterial(cache->GetResource<Material>("Materials/Terrain.xml"));

        RigidBody* terrainbody = terrainNode->CreateComponent<RigidBody>();
       CollisionShape* terrainshape = terrainNode->CreateComponent<CollisionShape>();
        // Set a box shape of size 1 x 1 x 1 for collision. The shape will be scaled with the scene node scale, so the
        // rendering and physics representation sizes should match (the box model is also 1 x 1 x 1.)
        terrainbody->SetCollisionLayer(1);
        terrainshape->SetTerrain();


        // Create a scene node for the camera, which we will move around
        // The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
        cameraNode_ = new Node(context_);

        cameraNode_ = scene_->CreateChild("Camera");
        cameraNode_->CreateComponent<Camera>();

        Camera* camera = cameraNode_->CreateComponent<Camera>();
        camera->SetFarClip(1500.0f);
        // Set an initial position for the camera scene node above the ground
        cameraNode_->SetPosition(Vector3(0.0f, 0.0f, 0.0f));

        SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
        renderer->SetViewport(0, viewport);

        // /create character
        Node * characternode_ = scene_->CreateChild("Character");
        characternode_->SetPosition(Vector3(0.0f, 0.0f, 0.0f));

        CreateCharacter();

        loadSceneUI();
[/code]
Office Youtube Page
https://www.youtube.com/user/cgprojectsfx

-------------------------

vivienneanthony | 2018-03-05 19:43:42 UTC | #15

I'll place my code in the message that seems to work so far. 

[b]Changes[/b]
1. Changed the final color output to RGBa grayscale since only the heightmap is being produced.

2. Changed final color to be [b](float+.5)*255[/b]. Forcing the final color output to be anywhere from 0 to 255. Since it's floats can be negative value which I think the STB is producing.

3. Separated the perlin part from color conversion and also scaling. So, steps are 1) Create Perlin using octaves as number of layers and scale  2) Scale floats to by number of octaves 3) Convert floats to RGB correcting values to be 0 to 255 final color.

4. Added each octaves layer to each other then did a final divide by number of octaves

[b]Possible Additions[/b]
1) add level to add each octave level separate from x,y

Basically, it seems to work so far after running the code. I will play with the values but it generates a basic heightmap with some a lot of flexibility by changing octaves.

Feel free to test it and  modify to clean the code. It works tho and can be integrated further.

Procedurally generated perlin terrain height map at least.

Vivienne

[code]
///
void Image::generatePerlinNoise1(
    unsigned  * data,
    unsigned width,
    unsigned height,
    unsigned octaves,
    float xOffset,
    float yOffset,
    float zOffset,
    int xWrap,
    int yWrap,
    int zWrap,
    float o1,
    float o2,
    float o3,
    float o4,
    float o5,
    float o6,
    float o7,
    float o8
)
{
    // not used
    float mag[] = {o1, o2, o3, o4, o5, o6, o7, o8};

    // allocate memory
    float * tempdata_;
    tempdata_ = (float *) malloc (width*height*width);

    for (unsigned o = 0; o<octaves; o++)
    {
        float oSize = (o+1) << o;

        float oxDiv = oSize / width;
        float oyDiv = oSize / height;

        for(unsigned x = 0; x<width; x++)
        {
            for(unsigned y = 0; y<height; y++)
            {
                // scale perlin based on octave size
                float hx = (float)x / (float)width;
                float hy = (float)y / (float)height;
                float noise = stb_perlin_noise3(x*oxDiv,y*oyDiv,zOffset,xWrap,yWrap,zWrap);

                int index = x+y*width;

                // add additional per octavenoise
                if(o)
                {
                    tempdata_[index]= tempdata_[index]+noise;
                }
                else
                {
                    // set first octave layer noise
                    tempdata_[index]= noise;
                }

            }
        }

    }

    /// loop through all the values then scale down by number of octaves
    for(unsigned x = 0; x<width; x++)
    {
        for(unsigned y = 0; y<height; y++)
        {
            int index = x+y*width;

            tempdata_[index]= tempdata_[index]/octaves;
        }
    }

    /// loop through all the floats then convert to grayscale setting the color basis to .5 (forcing values 0 to 1)
    for(unsigned x = 0; x<width; x++)
    {
        for(unsigned y = 0; y<height; y++)
        {

            int index = x+y*width;

            unsigned col = (tempdata_[index]+.5)* 255;  /// create color value

            col = rgba32ToUInt(col, col, col, 255);
            data[index] = col;      /// set grayscale - rgba is not needed. it seems to be screwy with this type of code.
        }

    }

    /// free memory
    free(tempdata_);

    return;
}

[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:05 UTC | #16

Anyone have any ideas on this code wise? Brainstorming this through out the day myself.

Hmmm. I think the same exact methods libnoise use to merge perlins can be used.

1. I'm thinking of doing a second Perlin noise and subtracting .5 from it allowing a negative or positive float.
2. Add the second Perlin noise (Using a octave Perlin with only 1 octave) I'm trying to look at how libnoise does it at [libnoise.sourceforge.net/tutoria ... rial5.html](http://libnoise.sourceforge.net/tutorials/tutorial5.html).
3. Go back and scale by dividing by 2.


The next part is this [libnoise.sourceforge.net/tutoria ... rial5.html](http://libnoise.sourceforge.net/tutorials/tutorial5.html)

-------------------------

vivienneanthony | 2018-03-05 19:43:13 UTC | #17

Hey, 

This is a little slower but more accurate. Instead of dividing by octaves. Ihe noise is  added  either negative or positve noise then scaled. The old float becomes range 0 to 1 keeping values. What could be added is a scaler size affecting z depth for each octave layer.

Tested several times and it seems to work.

Vivienne

[code]
///
void Image::generatePerlinNoise1(
    unsigned  * data,
    unsigned width,
    unsigned height,
    unsigned octaves,
    float xOffset,
    float yOffset,
    float zOffset,
    int xWrap,
    int yWrap,
    int zWrap,
    float o1,
    float o2,
    float o3,
    float o4,
    float o5,
    float o6,
    float o7,
    float o8
)
{
    // not used
    float mag[] = {o1, o2, o3, o4, o5, o6, o7, o8};

    // allocate memory
    float * tempdata_;
    tempdata_ = (float *) malloc (width*height*width);

    /// set range keeping scale
    float NewMax = 1.0f;
    float NewMin = 0.0f;
    float NewRange = (NewMax - NewMin);

    float lowfloat=0;
    float highfloat=0;

    for (unsigned o = 0; o<octaves; o++)
    {
        float oSize = (o+1) << o;

        float oxDiv = oSize / width;
        float oyDiv = oSize / height;

        for(unsigned x = 0; x<width; x++)
        {
            for(unsigned y = 0; y<height; y++)
            {
                // scale perlin based on octave size
                float hx = (float)x / (float)width;
                float hy = (float)y / (float)height;
                float noise = stb_perlin_noise3(x*oxDiv,y*oyDiv,zOffset,xWrap,yWrap,zWrap);

                int index = x+y*width;

                /noise *= mag[o];

                if(o)
                {
                    // Add additinal noise
                    // Determine high point and low point
                    tempdata_[index]= tempdata_[index]+noise;
                    if(tempdata_[index]>highfloat)
                    {
                        highfloat=tempdata_[index];
                    }
                    if(tempdata_[index]<lowfloat)
                    {
                        lowfloat=tempdata_[index];
                    }

                }
                else
                {
                    //Set initial noise
                    //Set high and low point
                    tempdata_[index]= noise;
                    if(tempdata_[index]>highfloat)
                    {
                        highfloat=tempdata_[index];
                    }
                    if(tempdata_[index]<lowfloat)
                    {
                        lowfloat=tempdata_[index];
                    }
                }
            }
        }

    }

    // Set range
    float OldRange = (highfloat-lowfloat);

    cout << lowfloat << " "<< highfloat;

    /// loop through all the values then scale down by number of octaves
    for(unsigned x = 0; x<width; x++)
    {
        for(unsigned y = 0; y<height; y++)
        {
            int index = x+y*width;

            // slower but scales the value range from 0.0f to 1.0f
            tempdata_[index]= (((tempdata_[index] - lowfloat) * NewRange) / OldRange) + NewMin;
        }
    }

    /// loop through all the floats then convert to grayscale setting the color basis to .5 (forcing values 0 to 1)
    for(unsigned x = 0; x<width; x++)
    {
        for(unsigned y = 0; y<height; y++)
        {

            int index = x+y*width;

            unsigned col = tempdata_[index]* 255;  /// create color value

            col = rgba32ToUInt(col, col, col, 255);
            data[index] = col;      /// set grayscale - rgba is not needed. it seems to be screwy with this type of code.
        }

    }

    /// free memory
    free(tempdata_);

    return;
}

[/code]

-------------------------

vivienneanthony | 2018-03-05 19:37:36 UTC | #18

Video update testing Perlin function.

https://www.youtube.com/watch?v=eUr9T6YVuIU

-------------------------

vivienneanthony | 2017-01-02 01:00:05 UTC | #19

Hello

The perlin part is working. I find this link about wormley noise with source code. 

[aftbit.com/cell-noise-2/](https://aftbit.com/cell-noise-2/)

I'm deciding about implementings the cell noise method. Might take me some time to make a C file based that matches to output like the generatePerlinNoise1.

Work In Progress
[b]1. generatePerlinNoise1 (I already coded BUT I'm In process of taking out the 3rd for xy loop with the color conversion and I'm making that generateOutput() to do that conversion)(Note: This allows adding  generateSelect() type functions combining and/or blending multiple layers out like GeneratePerlinNoise1, GenerateCellNoise1, GenerateVoroni1, generatePerlinControlNoise1(etc).)[/b]
2. generateCellNoise1 (It's a possiblity from the mentioned link))
3. generatePerlinControlNoise1 (Stripped generatePerlinNoise1 with 1 octave layer with scaling)
[b]4. Change GeneratePerlin to GenerateProcedural (I already coded)[/b]


Vivienne

-------------------------

vivienneanthony | 2017-01-02 01:00:06 UTC | #20

Hello, All.

So, I been working on the code. The design of it replicates libnoise. I have to addition select transition like libnoise, cell noise, and less intensive computation. I am posting the code so maybe something has a faster solution for the loops.

The GenerateSelectBuild(..) selects the perlin. It should act more like [libnoise.sourceforge.net/tutoria ... rial5.html](http://libnoise.sourceforge.net/tutorials/tutorial5.html).

Anyway, I would love feedback.

Vivienne


Image.h 
[code]
    /// GeneratePerlin
    unsigned rgba32ToUInt(unsigned r, unsigned g, unsigned b, unsigned a);

    bool GenerateProcedural(const int &width, const int &height,const unsigned &octaves,
                            const float &o1,
                            const float &o2,
                            const float &o3,
                            const  float &o4,
                            const float &o5,
                            const float &o6,
                            const float &o7,
                            const float &o8);
    float * GenerateSelectBuild(float * inputdata1, float * inputdata2, float *controldata1);
    unsigned int * GenerateBuild(float * buffer);
    void generatePerlinNoise1(  float * buffer,
                                unsigned width,
                                unsigned height,
                                unsigned octaves,
                                float xOffset,
                                float yOffset,
                                float zOffset,
                                int xWrap,
                                int yWrap,
                                int zWrap,
                                float o1,
                                float o2,
                                float o3,
                                float o4,
                                float o5,
                                float o6,
                                float o7,
                                float o8);
    void CopyData(const unsigned char* pixelData);[/code]

Image.Cpp
[code]
bool Image::GenerateProcedural(const int &width, const int &height,const unsigned &octaves,
                           const float &o1,
                           const float &o2,
                           const float &o3,
                           const float&o4,
                           const float &o5,
                           const float &o6,
                           const float &o7,
                           const float &o8)
{
    /// Create a pointer location for pixelData
    unsigned char* pixelData;               /// data location of final output

    unsigned int* perlinOutput;             /// final perlin output
    float * perlininput1;                         ///  perlininput11
    float * perlininput2;                         ///  perlininput11
    float * controlinput1;                         ///  perlininput11
    float * controloutput1;                         ///  perlininput11

    unsigned int components=4;
    unsigned int depth=1;

    /// calculate memory needed to match pixelData and perlininput1
    unsigned int dataSize = width*height*width;

    /// Allocate perlininput1
    perlininput1 = ( float *) malloc(dataSize);
    perlininput2 = ( float *) malloc(dataSize);
    controlinput1 = ( float *) malloc(dataSize);
    controloutput1= ( float *) malloc(dataSize);

    perlinOutput = (unsigned int *) malloc(dataSize);

    /// Set Size components of the image
    SetSize(width, height, 1, components);

    /// Generate noise - Currently 8 octaves
    generatePerlinNoise1(perlininput1,width,height,2,0.0f,0.0f,0.0f,0,0,0,o1,o2,o3,o4,o5,o6,o7,o8);

    /// Generate noise - Currently 8 octaves
    generatePerlinNoise1(perlininput2,width,height,7,0.0f,0.0f,0.0f,0,0,0,0.3f,0.6f,o3,o4,o5,o6,o7,o8);

    /// Generate noise - Currently 8 octaves
    generatePerlinNoise1(controlinput1,width,height,2,0.0f,0.0f,0.0f,0,0,0,0.4f,0.4f,o3,o4,o5,o6,o7,o8);

    /// Produce Output
    controloutput1=GenerateSelectBuild(perlininput1,perlininput2,controlinput1);

    perlinOutput=GenerateBuild(controloutput1);

    /// Point pixelData to perlininput1 memory
    pixelData = (unsigned char *) perlinOutput;

    /// Set image size
    CopyData(pixelData);

    /// Free Memory
    FreeImageData(pixelData);

    // free up memory
    free(perlininput1);
    free(perlininput2);
    free(controlinput1);
    free(controloutput1);

    return true;
}


unsigned Image::rgba32ToUInt(unsigned r, unsigned g, unsigned b, unsigned a)
{
    return (r&255) + ((g&255) << 8) + ((b&255) << 16) + ((a&255) << 24);
}

///
void Image::generatePerlinNoise1(
    float * buffer,
    unsigned width,
    unsigned height,
    unsigned octaves,
    float xOffset,
    float yOffset,
    float zOffset,
    int xWrap,
    int yWrap,
    int zWrap,
    float o1,
    float o2,
    float o3,
    float o4,
    float o5,
    float o6,
    float o7,
    float o8
)
{
    float mag[] = {o1, o2, o3, o4, o5, o6, o7, o8};

    // allocate memory
    float * tempdata_;
    tempdata_ = (float *) malloc (width*height*width);

    /// set range keeping scale
    float NewMax = 1.0f;
    float NewMin = 0.0f;
    float NewRange = (NewMax - NewMin);

    float lowfloat=0;
    float highfloat=0;

    for (unsigned o = 0; o<octaves; o++)
    {
        float oSize = (o+1) << o;

        float oxDiv = oSize / width;
        float oyDiv = oSize / height;

        for(unsigned x = 0; x<width; x++)
        {
            for(unsigned y = 0; y<height; y++)
            {
                // scale perlin based on octave size
                float hx = (float)x / (float)width;
                float hy = (float)y / (float)height;
                float noise = stb_perlin_noise3(x*oxDiv,y*oyDiv,zOffset,xWrap,yWrap,zWrap);

                int index = x+y*width;

                noise *= mag[o];

                if(o)
                {
                    // Add additinal noise
                    // Determine high point and low point
                    tempdata_[index]= tempdata_[index]+noise;
                    if(tempdata_[index]>highfloat)
                    {
                        highfloat=tempdata_[index];
                    }
                    if(tempdata_[index]<lowfloat)
                    {
                        lowfloat=tempdata_[index];
                    }

                }
                else
                {
                    //Set initial noise
                    //Set high and low point
                    tempdata_[index]= noise;
                    if(tempdata_[index]>highfloat)
                    {
                        highfloat=tempdata_[index];
                    }
                    if(tempdata_[index]<lowfloat)
                    {
                        lowfloat=tempdata_[index];
                    }
                }
            }
        }

    }

    // Set range
    float OldRange = (highfloat-lowfloat);


    /// loop through all the values then scale down by number of octaves
    for(unsigned x = 0; x<width; x++)
    {
        for(unsigned y = 0; y<height; y++)
        {
            int index = x+y*width;

            // slower but scales the value range from 0.0f to 1.0f
            tempdata_[index]= (((tempdata_[index] - lowfloat) * NewRange) / OldRange) + NewMin;
        }
    }

    // copy memory
    memcpy (buffer, tempdata_,  width*height*width);


    /// free memory
    free(tempdata_);

    return;
}


/// generate perlin output
unsigned int * Image::GenerateBuild(float * buffer)
{
    int width=width_;
    int height=height_;
    int components=components_;
    int depth=1;

    // create new memory
    unsigned * output_;
    output_ = (unsigned int *) malloc (width*height*width);

    // loop through all the floats then convert to grayscale setting the color basis to .5 (forcing values 0 to 1)
    for(unsigned x = 0; x<width; x++)
    {
        for(unsigned y = 0; y<height; y++)
        {

        /// incremennt memory which seems to work
        int index = x+y*width;

        unsigned col = buffer[index]* 255;  /// create color value

        col = rgba32ToUInt(col, col, col, 255);
        output_[index] = col;      /// set grayscale - rgba is not needed. it seems to be screwy with this type of code.
       }
    }

    return output_;
}

/// generate perlin select
float * Image::GenerateSelectBuild(float * inputdata1, float * inputdata2, float *controldata1)
{
    int width=width_;
    int height=height_;
    int components=components_;
    int depth=1;

    // create new memory
    float * output_;
    output_ = (float *) malloc (width*height*width);

    // loop through all the floats then convert to grayscale setting the color basis to .5 (forcing values 0 to 1)
    for(unsigned x = 0; x<width; x++)
    {
        for(unsigned y = 0; y<height; y++)
        {
            /// incremennt memory which seems to work
            int index = x+y*width;

            if((controldata1[index]-.5)<0)
            {
                    output_[index]=inputdata1[index];
            }else
            {
                    output_[index]=inputdata2[index]*.7;
            }

       }
    }

    return output_;
}[/code]

Terrain.cpp
[code]bool Terrain::GenerateProceduralHeightMap()
{
    /// Generate Image
    Image * perlinimage = new Image(context_);

    bool success = false;

    ///// Create Image
    if(!perlinimage->GenerateProcedural(1024,1024,3,0.1f,0.1f,0.1f,0.4f,0.1f,0.2f,0.2f,0.2f))
    {

        return false;
    }


    perlinimage->SavePNG(String("/media/home2/vivienne/Existence/Bin/test.png"));

    success = SetHeightMapInternal(perlinimage, true);


    return success;
}
[/code]

terrain.h
[code]    /// Load Terrain Using libnoise
    bool GenerateProceduralHeightMap();
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:06 UTC | #21

Code revised. So, it takes less then a second compared to 5 seconds!!! I think it can be made faster.

-------------------------

vivienneanthony | 2017-01-02 01:00:07 UTC | #22

Added diamond terrain generation with [en.wikipedia.org/wiki/Diamond-square_algorithm](http://en.wikipedia.org/wiki/Diamond-square_algorithm)


1. Code need to be modified to use offset and offset, disable warping temporarily,  divsion to scale density(maybe), and hash table for the random generation. [b](Have to be worked on since framework is made.)[/b]

2. The new code you can use any amount of GeneratePerlinNoise and generateDiamondMethod using generateSelect as long as there is memory. [b](Have to be worked on since the framework is made.)[/b]

[code]
/// Cold to create noise through the Diamond method. Requires offset and better hash table to create random heightmaps but repeatable
bool Image::generateDiamondMethod1 (float * buffer,const int &width, const int &height, const float &maxYcoords,const float &minYcoords)
{
    //an initial seed value for the corners of the data
    float SEED = 0.4f;
    static const unsigned int DATA_SIZE=width+1;
    std::vector< std::vector<float> > diamond( DATA_SIZE, std::vector<float>(DATA_SIZE) );

    //initialise the values of the corners++
    diamond[0][0] = SEED;
    diamond[0][DATA_SIZE-1] = SEED;
    diamond[DATA_SIZE-1][0] = SEED;
    diamond[DATA_SIZE-1][DATA_SIZE-1] = SEED;

    float h =300; 	//the range (-h -> h) for the average offset
    srand(256);		//seed the random generator

    //side length is the distance of a single square side
    //or distance of diagonal in diamond
    //each iteration we are looking at smaller squares and diamonds, we decrease the variation of the offset
    for (int sideLength = DATA_SIZE-1; sideLength >= 2; sideLength /= 2, h /= 2.0)
    {

        int halfSide = sideLength/2;

        //generate new square values
        for(int x=0; x<DATA_SIZE-1; x+=sideLength)
        {
            for(int y=0; y<DATA_SIZE-1; y+=sideLength)
            {

                //x,y is upper left corner of the square
                //calculate average of existing corners
                float avg = diamond[x][y] + 				//top left
                            diamond[(x+sideLength)%DATA_SIZE][y]   +				//top right
                            diamond[x][ (y+sideLength)%DATA_SIZE]   + 				//lower left
                            diamond[(x+sideLength)%DATA_SIZE][(y+sideLength)%DATA_SIZE]; 	//lower right

                avg /= 4.0;

                //center is average plus random offset in the range (-h, h)
                float offset = (-h) + (float)rand() * (h - (-h))  / RAND_MAX;

                diamond[x+halfSide][y+halfSide] = avg + offset;

            } //for y
        } // for x

        //Generate the diamond values
        //Since diamonds are staggered, we only move x by half side
        //NOTE: if the data shouldn't wrap the x < DATA_SIZE and y < DATA_SIZE
        for (int x=0; x<DATA_SIZE-1; x+=halfSide)
        {
            for (int y=(x+halfSide)%sideLength; y<DATA_SIZE-1; y+=sideLength)
            {

                //x,y is center of diamond
                //we must use mod and add DATA_SIZE for subtraction
                //so that we can wrap around the array to find the corners

                float avg =
                    diamond[(x-halfSide+DATA_SIZE)%DATA_SIZE][y] +	//left of center
                    diamond[(x+halfSide)%DATA_SIZE][y]				+	//right of center
                    diamond[x][(y+halfSide)%DATA_SIZE]				+	//below center
                    diamond[x][(y-halfSide+DATA_SIZE)%DATA_SIZE];	//above center

                avg /= 4.0;

                //new value = average plus random offset
                //calc random value in the range (-h,+h)
                float offset = (-h) + (float)rand() * (h - (-h))  / RAND_MAX;

                avg = avg + offset;

                //update value for center of diamond
                diamond[x][y] = avg;

                //wrap values on the edges
                //remove this and adjust loop condition above
                //for non-wrapping values
                if (x == 0) diamond[DATA_SIZE-1][y] = avg;
                if (y == 0) diamond[x][DATA_SIZE-1] = avg;
            } //for y
        } //for x
    } //for sideLength


    /// Set maxY and minY to 0.0f
    float maxY = diamond[1][1];
    float minY = diamond[1][1];

    for (int x = 0; x<DATA_SIZE; x++)
    {
        for(int y = 0; y<DATA_SIZE; y++)
        {
            if ((float)diamond[x][y] > maxY)
            {
                maxY = diamond[x][y];
            }
            if ((float)diamond[x][y] < minY)
            {
                minY = diamond[x][y];
            }
        }
    }

    /// Calculate height from 0 to 1
    for(int x=0; x < DATA_SIZE; x++)
    {
        for(int y=0; y < DATA_SIZE; y++)
        {
            //change range to 0..1
            diamond[x][y] = (diamond[x][y] - minY) / (maxY - minY);
        }
    }

    /// Copy color float from create texture
    for(unsigned y = 0; y<width; y++)
    {
        for(unsigned x = 0; x<height; x++)
        {
            /// incremennt memory which seems to work
            int index = (y*width)+x;

            buffer[index]=diamond[x][y];
        }
    }

    return true;
[/code]

As to textures, maybe someone has a idea of how to deal with textures for randomly generated terrain.

-------------------------

vivienneanthony | 2018-03-05 19:44:56 UTC | #23

This is the latest code results. Once I get a smooth transistion function like ([libnoise.sourceforge.net/tutoria ... rial5.html](http://libnoise.sourceforge.net/tutorials/tutorial5.html)) it will be added to the mix of things. The function is made but needs to be coded for floats and the algorithm currently used.

https://www.youtube.com/watch?v=JW9qzqHlc-M

-------------------------

