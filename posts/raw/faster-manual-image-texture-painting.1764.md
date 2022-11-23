gawag | 2017-01-02 01:09:57 UTC | #1

I'm trying to draw 2D stuff onto the screen. I used the sample GUI code with the Urho logo as a base and I'm drawing the pixel into an Image and this is then converted into a Texture2D which is used by a Sprite. The problem is the big FPS impact from ~200 to 40-60.
[code]
// init code
        _image=new Urho3D::Image(_context);
        _sprite=_context->GetSubsystem<Urho3D::UI>()->GetRoot()->CreateChild<Urho3D::Sprite>();
        _texture=new Urho3D::Texture2D(_context);
        _texture->SetFilterMode(Urho3D::TextureFilterMode::FILTER_NEAREST);
        _texture->SetNumLevels(1);
...
    void redraw() // this is currently called each update() call
    {
        // redraw my image, this does take ~0.003s
        lfgui::widget::redraw();
        // only resize if necessary, 0s
        if(_texture->GetWidth()!=width()||_texture->GetHeight()!=height())
            _texture->SetSize(width(),height(),Urho3D::Graphics::GetRGBAFormat(),Urho3D::TEXTURE_STATIC);
        // only resize if necessary, 0s
        if(_image->GetWidth()!=width()||_image->GetHeight()!=height())
            _image->SetSize(width(),height(),4);

        // copy pixel from my image to the Urho Image (my image has the pixel in a weird format (separated color channels) so that I have to copy each pixel on it's own. This takes 0.01s.
        auto h=height();
        auto w=width();
        uint32_t* data=(uint32_t*)_image->GetData();
        for(int y=0;y<h;y++)
            for(int x=0;x<w;x++)
            {
                lfgui::color p=this->img.get_pixel(x,y);
                *data=p.value;    // this is a bit faster as SetPixelInt(...)
                data++;
            }

        // fill texture from image, 0.003s
        _texture->SetData(_image);

        // only resize if necessary, 0s
        if(_sprite->GetWidth()!=_texture->GetWidth()||_sprite->GetHeight()!=_texture->GetHeight())
            _sprite->SetSize(_texture->GetWidth(),_texture->GetHeight());
    }
[/code]
Is there a more direct way to draw on the screen (over a 3D scene)? Any other optimization idea? The performance impact seems kinda high for such a simple thing. I guess I could redraw my image and copy the pixels in another thread but that seems kinda odd.

Also these Sprites in the GUI don't seem to draw semi transparent pixel? (even with _texture->SetData(_image,true);)

-------------------------

codingmonkey | 2017-01-02 01:09:57 UTC | #2

I think the method with using of two RTT (or more) will be much faster (than manipulating with data on cpu side)

RTT1 for color (do not clear it every frame with clear command in RenderPath)
RTT2 for erase (use it for clear RTT1 when left mouse button released, if pressed and eraser are selected somewhere draw into it white color for example)

combine RTT1 into Viewport RTT in someway, probably just full direct copy or some small part/area of it (for painting only on some widgets surface ).

The drawing into RTT1: you just render into this RTT some object(for example : sphere ) in ortho projection by mouse coords when you pressing left mouse button 

also you will needed add some stuff for dynamically control RenderPath.

I guess you got my POV of this )

-------------------------

gawag | 2017-01-02 01:09:57 UTC | #3

Oh I think I know what you mean. The image I want to draw is not a rendered image like a viewport (no render to texture). It's actually a drawn image with for example text, or paths, or gradients or other images. So this image is drawn by the CPU not by the GPU.

I also thought of somehow copying my CPU drawn image to the GPU and use a shader to actually draw it in the proper way with correct colors (without using the CPU to transform the data to an Image and then a Texture2D). The colors are not RGBARGBARGBA..., they are RRR...GGG...BBB...AAA.... Can that be done? Applying a shader to a Sprite/Texture2D on screen? The color/texture lookup should be easy. Or would that be also relative expansive but on the GPU side?

-------------------------

codingmonkey | 2017-01-02 01:09:57 UTC | #4

>The image I want to draw is not a rendered image like a viewport 
actually, this is will be similar to 2d Canvas, where you might draw your various textured objects by hand(mouse).

>they are RRR...GGG...BBB...AAA.... Can that be done?
I think at first of all you need convert this RRR...GGG... to something loadable as usual texture (on cpu side) and then use it on some textured quad as paint brush (in case painting with RTTs)

-------------------------

gawag | 2017-01-02 01:09:58 UTC | #5

[quote="codingmonkey"]>The image I want to draw is not a rendered image like a viewport 
actually, this is will be similar to 2d Canvas, where you might draw your various textured objects by hand(mouse).
[/quote]
Oh I can draw directly on a texture? How?

[quote="codingmonkey"]
>they are RRR...GGG...BBB...AAA.... Can that be done?
I think at first of all you need convert this RRR...GGG... to something loadable as usual texture (on cpu side) and then use it on some textured quad as paint brush (in case painting with RTTs)[/quote]
That conversion is done at that part. No idea what you mean with "texture quad as paint brush". I guess the Sprite is already a texture quad? It has the Texture2D assigned.

Update: I managed to greatly optimize my pixel copy code:
[code]
...
// copy pixel from my image to the Urho Image (my image has the pixel in a weird format (separated color channels) so that I have to copy each pixel on it's own
int h=height();
int w=width();
int count=w*h;
int countx2=count*2;
int countx3=count*3;
// due to the channel separation in the first image, the pixel have to be copied byte/color vise
uint8_t* data_target=_image->GetData();
uint8_t* data_source=this->img.data();
for(;data_source<data_source_end;)
{
    *data_target=*data_source;
    data_target++;
    *data_target=*(data_source+count);
    data_target++;
    *data_target=*(data_source+countx2);
    data_target++;
    *data_target=*(data_source+countx3);
    data_target++;
    data_source++;
}

// fill texture from image, 0.003s
...
[/code]
This is so fast that I can't really measure it with my usual method. I takes around 0.001 or 0.002 seconds and my FPS are at 90! (I started at 16!)
So I got rid of all multiplications, unnecessary operations and object creations. Now only pointer increments, additions and byte movements (the CPU loves that).

Still any other idea to the rest of the code/approach? The FPS drop is still significant from ~190 to ~90.

I wrote an article (unpublished) with all the optimization steps I took and the reasons behind. Still no idea where I should publish such things. There could be also an Urho article about this manual painting an Image to get a Texture2D. Is that the proper approach or is there a better one?

-------------------------

OvermindDL1 | 2017-01-02 01:09:59 UTC | #6

Are copying the entire thing over every frame, or are you only sending updates to locations that have changed as they change?

-------------------------

gawag | 2017-01-02 01:09:59 UTC | #7

[quote="OvermindDL1"]Are copying the entire thing over every frame, or are you only sending updates to locations that have changed as they change?[/quote]
Currently I'm doing all that every frame. Yes that could be optimized as it usually doesn't have to be running at the full FPS and that is planned.
I could also update only regions where stuff has changed and that's also planned (if you mean that with "sending updates to locations that have changed").

My main question now is: Is this drawing into an Urho3D::Image and then telling a Texture2D to use that Image and then using a Sprite to display that data on the screen (over a 3D scene) the best way?
Codingmonkey mentioned drawing directly on a texture but I can't see any way to do that: [urho3d.github.io/documentation/1 ... re2_d.html](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_texture2_d.html)

Oh. I just tried replacing Texture2D::SetData (SharedPtr< Image > image, bool useAlpha=false) with Texture2D::SetData(unsigned level, int x, int y, int width, int height, const void *data) and that function is a bit faster. The first took around 0.0043 seconds and the second around 0.0031 seconds (though my time measurement is not that precise for such short periods). My FPS are around 95 (+-7) now.

There's also this TextureUsage in the SetSize, what does that do? I'm currently using TEXTURE_STATIC but also tried TEXTURE_DYNAMIC which didn't seem to change anything in my case.

-------------------------

codingmonkey | 2017-01-02 01:10:01 UTC | #8

>Oh I can draw directly on a texture? How?
bind Texture as output for some scenepass in RenderPath
for example I use "handpaint" scenepass to rendering colored plane onto canvas1 RTT
[github.com/MonkeyFirst/urho3d-r ... dPaint.xml](https://github.com/MonkeyFirst/urho3d-rtt-paint/blob/master/bin/CoreData/RenderPaths/ForwardPaint.xml)

there is common example : [github.com/MonkeyFirst/urho3d-rtt-paint](https://github.com/MonkeyFirst/urho3d-rtt-paint) with using RTT for painting

-------------------------

