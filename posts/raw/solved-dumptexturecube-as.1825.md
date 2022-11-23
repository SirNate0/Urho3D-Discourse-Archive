codingmonkey | 2017-01-02 01:10:28 UTC | #1

Hi, there!
I trying to save cube map into image *.png  files.
for code example I use [b]carnalis[/b] ProcSky.cc (void ProcSky::DumpTexCubeImages) also I look into [b]Sinoid[/b] code for cubemap baking.
so, I have this code and it's no working (

[code]
void ProcSkyPostRenderUpdate()
{
    if (input.keyPress[KEY_T] ) 
    {
        DumpTextureCube(procSkyCubeTexture, "C:/Urho3D/bin/Data/Textures/");
    }
    
    if (!procSkyRenderQueued) return;
    
    //
}

void DumpTextureCube(TextureCube@ texCube, String filePath) 
{
    if (texCube is null) return;
     
    for (int i = 0; i < MAX_CUBEMAP_FACES; i++) 
    {
        Texture2D@ faceTex = cast<Texture2D>(texCube.renderSurfaces[CubeMapFace(i)].parentTexture);
        if (faceTex !is null)
        {
            MessageBox("OK - get Texture2D from cubemap face" + String(i));
            Image@ texImage = faceTex.GetImage();
            fileSystem.CreateDir(filePath);
            String path(filePath + String(i) + ".png");
            if (texImage !is null) 
            {
                texImage.SavePNG(path);
                MessageBox(path);
            }
        }
        else 
        {
            MessageBox("Failure get Texture2D from cubemap face" + String(i));
        }
    }
}
[/code]

Every time then I pressing on T-key I got this message - "Failure get Texture2D from cubemap face" and no one time "Sucessed msg"
What i'm doing wrong ?

-------------------------

jmiller | 2017-01-02 01:10:29 UTC | #2

Hi codingmonkey,

May be texture component compatibility? I think for that reason I created a new Image.

[code]
void ProcSky::DumpTexCubeImages(TextureCube* texCube, const String& pathName) {
  URHO3D_LOGINFO("Save TextureCube: " + pathName + "[0-5].png");
  for (unsigned j = 0; j < MAX_CUBEMAP_FACES; ++j) {
    Texture2D* faceTex(static_cast<Texture2D*>(texCube->GetRenderSurface((CubeMapFace)j)->GetParentTexture()));

    SharedPtr<Image> faceImage(new Image(context_));
    faceImage->SetSize(faceTex->GetWidth(), faceTex->GetHeight(), faceTex->GetComponents());

    FileSystem* fs(GetSubsystem<FileSystem>());
    fs->CreateDir(pathName);
    String filePath(pathName + String(j) + ".png");

    if (!texCube->GetData((CubeMapFace)j, 0, faceImage->GetData())) {
      URHO3D_LOGERROR("...failed GetData() for face " + filePath);
    } else {
      faceImage->SavePNG(filePath);
    }
  }
}
[/code]

-------------------------

codingmonkey | 2017-01-02 01:10:30 UTC | #3

Hi carnalis, thank for reply.
But, this of all you probably got a "good ptr to texture" on this lines:

>Texture2D* faceTex(static_cast<Texture2D*>(texCube->GetRenderSurface((CubeMapFace)j)->GetParentTexture()));

and only then you create new image

>SharedPtr<Image> faceImage(new Image(context_));

in my case I got always - faceTex = null 
So, I think the - texCube.renderSurfaces[CubeMapFace(i)].parentTexture do not store within any valid data, or mb I'am doing something wrong.

-------------------------

cadaver | 2017-01-02 01:10:31 UTC | #4

TextureCube has 6 rendersurfaces, but their parentTexture isn't a Texture2D per face, instead each of their parentTexture points to the same TextureCube instance.

In C++ you'd use TextureCube::GetData(). In AS there isn't currently a way to get a face image from an existing TextureCube, since script cannot support the GetData function(). This should be fairly simple to add though, there's already a "fake" function in the AS API to get an image from Texture2D.

-------------------------

cadaver | 2017-01-02 01:10:31 UTC | #5

There is now a TextureCube::GetImage() in the AngelScript API.

[github.com/urho3d/Urho3D/commit ... 63591d3084](https://github.com/urho3d/Urho3D/commit/633a6fa512800e3bf3903a21b7484663591d3084)

-------------------------

codingmonkey | 2017-01-02 01:10:32 UTC | #6

Thanks! Now it's working well
[code]
void DumpTextureCube(TextureCube@ texCube, String filePath) 
{
    if (texCube is null) return;
    for (int i = 0; i < MAX_CUBEMAP_FACES; i++)
    {
        Image@ texImage = texCube.GetImage(CubeMapFace(i));
        fileSystem.CreateDir(filePath);
        String path(filePath + String(i) + ".png");
        if (texImage !is null)
        {
            MessageBox("OK - get Texture2D from cubemap face" + String(i));        
            texImage.SavePNG(path);
            MessageBox(path);
        }
    }
}
[/code]

-------------------------

