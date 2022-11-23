minek | 2017-01-02 00:59:55 UTC | #1

Hello, thanks for great engine.
I'm trying to create worms like dynamic terrain and I would like to change pixels (even each frame). Using nodes for each pixel is overkill because even on small terrain like 1000x1000 you get 1kk nodes. So I will make the terrain on the texture. I'm using Set data function in Texture2D class but it is quite slow. Is there any faster method of changing pixel colors of the texture each frame? What would you suggest?

Thank for help

-------------------------

cadaver | 2017-01-02 00:59:55 UTC | #2

Welcome to the forum!

I believe the best you can do currently and in a cross-platform manner is to SetData() the whole texture at once, so you would retain a whole copy in system RAM in which you edit the single pixels. Make sure to create the texture in dynamic usage mode (TEXTURE_DYNAMIC when calling SetSize()) so that frequent updates are faster.

Another way is to use the GPU to render pixels to the texture. Because you're not rendering an actual scene, and don't want the texture to be cleared each frame, you'll need to use the low-level functions of the Graphics subsystem directly, eg. Graphics::SetRenderTarget(), Graphics::SetShaders(), Graphics::Draw() etc.

-------------------------

DavTom | 2017-01-02 01:12:15 UTC | #3

Any one has some example code on this or some links to how this could be implemented?

-------------------------

Victor | 2017-01-02 01:12:15 UTC | #4

I'm pretty new to Urho3D so I'm not sure what the correct answer would be. My first naive approach would be the following however:

(Pseudo code...)
[code]
Image texImg;
Texture2D* someTex = <grab texure>
char* imgData = new char[someTex->GetWidth()*someTex->GetHeight()];

if (someTex->GetData(0, imgData)) {
    texImg.SetData(imgData);
    texImg.SetPixel(0, 0, Color(1,1,1));

    someTex->SetData(&texImg);
}
[/code]

Something like that perhaps? So I guess the approach I would take is using a reference to an Image object, update the image object and set the data of the texture with it. I have not tested this, it's just what I though of when looking through the Urho3D code...

-------------------------

DavTom | 2017-01-02 01:12:16 UTC | #5

Victor, thanks for sharing the code. 
I have extended the discussion to a new use case of combining Urho2D and Urho3D. 
[topic2106.html](http://discourse.urho3d.io/t/combine-samples-rendertotexture-materialanimation-urho2d/2010/1)

-------------------------

