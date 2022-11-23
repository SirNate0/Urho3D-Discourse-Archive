amit | 2017-01-02 01:03:39 UTC | #1

I have interated CEF in my app (mac) but am facin issue in transparency in sprite.

[code]void AnimatingScene::OnPaint(CefRefPtr<CefBrowser> browser, PaintElementType type, const RectList &dirtyRects, const void *buffer, int width, int height)
{
    unsigned char* dat = ipic->GetData();
    memcpy(dat, buffer, width*height*4);
//    for (int i=0; i<width*height; i++) {
//        dat[4*i] = 0xff;
//        dat[4*i + 1] = 0;
//        dat[4*i + 2] = 0xff;
//        dat[4*i + 3] = 100;
//    }
    le->SetData(ipic);
}[/code]

ipic = new Image(context_);
le = new Texture2D(context_);

since data is type char type, i tried set alpha 100, but the whole pixel is transparent not see throu...

any help!

-------------------------

amit | 2017-01-02 01:03:40 UTC | #2

HI, Here is a detail of what i am doin ...



[code]    le = new Texture2D(context_);
    //dyamic tex 640x480 with alpha
    le->SetSize(640, 480, Graphics::GetRGBAFormat(),TEXTURE_DYNAMIC);

    // A Image container for frame buffer
    ipic = new Image(context_);
    //resized internal buffer to 640 x 480
    ipic->SetSize(640, 480, 4);
    //white opaque
    memset(ipic->GetData(), 0xff, 640*480*4);
    
    //set data
    le->SetData(ipic,true);



    UI* ui = GetSubsystem<UI>();
    dynamic_sprite = ui->GetRoot()->CreateChild<Sprite>();    
    // Set logo sprite texture
    dynamic_sprite->SetTexture(le);
    int textureWidth = le->GetWidth();
    int textureHeight = le->GetHeight();
    // Set logo sprite size
    dynamic_sprite->SetSize(textureWidth, textureHeight);
    // Set logo sprite hot spot
    dynamic_sprite->SetHotSpot(0, textureHeight);
    // Set logo sprite alignment
    dynamic_sprite->SetAlignment(HA_CENTER, VA_BOTTOM);
[/code]

This all works, now I am tryin to update it runtime,

[code]    unsigned char* dat = ipic->GetData();
    for (int i=0; i<width*height; i++) {
        dat[4*i] = 0xff;  // RED
        dat[4*i + 1] = 0;
        dat[4*i + 2] = 0;

        dat[4*i + 3] = 128; //ALPHA
        //alpha is 128 ie half transparent, but it is opaque, if set to "0" it becomes completely transparent
        // I require alpha mapped sprite
    }
    le->SetData(ipic);
[/code]

        [color=#FF0000]//alpha is 128 ie half transparent, but it is seen opaque, if set to "0" it becomes completely transparent
        // I require alpha mapped sprite[/color]

is it possible in URHO3D ?

-------------------------

cadaver | 2017-01-02 01:03:40 UTC | #3

Try setting blendmode (UIElement::SetBlendMode) on the UI element to BLEND_ALPHA.

-------------------------

amit | 2017-01-02 01:03:40 UTC | #4

all done thanks,
finally I can have a HTML UI.

-------------------------

Bluemoon | 2017-01-02 01:03:41 UTC | #5

[quote="amit"]all done thanks,
finally I can have a HTML UI.[/quote]

Wow... I've been trying to implement something similar to this. If its an open information I wouldn't mind you sharing how you were able to do it  :smiley:

-------------------------

amit | 2017-01-02 01:03:42 UTC | #6

sure, what do you want to know.
I used CEF3 prebuilt libs. Its easy on windows, but I am usin MAC here.
What platform are you usin

-------------------------

Bluemoon | 2017-01-02 01:03:44 UTC | #7

[quote="amit"]sure, what do you want to know.
I used CEF3 prebuilt libs. Its easy on windows, but I am usin MAC here.
What platform are you usin[/quote]

My Platform is Windows. I want to know how you were able to integrate CEF into Urho3D's rendering process

-------------------------

amit | 2017-01-02 01:03:44 UTC | #8

download prebuild lib from,
[cefbuilds.com/](http://cefbuilds.com/)

and use cmake to build all sample and an additional lib libcef_dll_wrapper.

I used cefsimple source and foll code to init it

[code]    // SimpleApp implements application-level callbacks. It will create the first
    // browser instance in OnContextInitialized() after CEF has initialized.
    CefRefPtr<SimpleApp> app(new SimpleApp(this));
    
    // Specify CEF global settings here.
    CefSettings settings;
    
    // Initialize CEF for the browser process.
    CefInitialize(main_args, settings, app.get(), NULL);[/code]


additionally add    " window_info.SetAsWindowless(0, true);"

before

  CefBrowserHost::CreateBrowserSync(window_info, handler.get(), url, browser_settings, NULL);

in simple_app.cc

and add
 virtual CefRefPtr<CefRenderHandler> GetRenderHandler() {
    return renderhandle;
}
in simple_handler class

renderhandle is an implementation of CefRenderHandler with OnPaint implementation. see 1st post.

also see 2nd post for urho side impl.

let me know if u have any trouble

-------------------------

Bluemoon | 2017-01-02 01:03:45 UTC | #9

Thanks a lot, I will try it out right away :slight_smile:

-------------------------

