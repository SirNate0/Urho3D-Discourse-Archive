Alexander | 2017-01-02 01:13:59 UTC | #1

Hi,

We are using Urho3D on a raspberry pi to animate planes with textures. As the pi has limited graphics memory we use the resource cache to load the textures in the background before they are needed, and unload them after they are used.
This works mostly fine.

We just noticed that even if the loading part is done in the background, it finishes with an [code]Texture2D::EndLoad()[/code], that is performed in the main thread.
In EndLoad, the function [code]bool success = SetData(loadImage_);[/code] is called, and on our platform that call takes between 20 ms to 50 ms. In our compilation on the PI, the code from [code]OGLTexture2D.cpp[/code] is used.
As this is done in the main thread, we currently struggel to come under the 16.66 ms per frame we need to rech a 60 fps target. Actually we can not even reach a 30 fps target when the texture loading behaves like this. The texture we use is about 1920*1080, and in RGBA.

Therefore i wonder what is done during this face of the process, and what we can do to make it faster. Can we use other picture formats? Currently we use PNG. Or is the time spent copying raw image data from memory to graphics memory?
Does this process really need to be in the main thread?

I guess this is something that is unique to the raspberry pi, or at least not a commom problem on other platforms. Or do we miss something basic in how we work with textures and texture loading?

Sincerely,
Alexander

-------------------------

cadaver | 2017-01-02 01:13:59 UTC | #2

Yes, the OpenGL call to upload texture data (glTexImage2D) needs to be on the main thread, as OpenGL contexts can only exist attached to one thread at a time. Even if it was on another thread, the upload would have to complete before the next frame can render correctly (assuming the image will be used on the next frame)

This is somewhat of a problem on all platforms, but more so on Raspberry Pi as it's so underpowered.

-------------------------

Alexander | 2017-01-02 01:13:59 UTC | #3

Hi there,

Thanks for the quick reply!

You mention that the data needs to be there before the next frame, as one can imagine :slight_smile:
But the fact is tha we load the textures many frames ahead of there usage, so for us it would be no broblem to spread this proces over multiple frames. That would be much prefered to the current situation where the engine halts.

Can this behaviour be acheved  by parameter configuration of the engine, or can we reprogram the engine to work like this?

Is there something else we can do to shorten the time used in SetData()?

Sincerely
Alexander

-------------------------

cadaver | 2017-01-02 01:13:59 UTC | #4

No, it's rather the behavior of the graphics driver and there's no direct control over it. Practically, what the driver offers to the application is "call glTexImage2D() to upload a texture" and it will take as long time as it needs. If the driver is smart then the function itself could complete fast (the graphics driver just stashes it to memory waiting for GPU upload) and avoid a graphics pipeline stall and a long frame in case you would not actually use the texture on the next frame. However the driver can just as well decide to not be that smart.

One thing you could try would be to load the Image (CPU-side copy only) first, then SetData() it to the Texture2D in small pieces, and see whether that is faster.

-------------------------

Alexander | 2017-01-02 01:13:59 UTC | #5

Ok.

We will se if we can chop the work in smaller peices, and perhaps even spread them out over multiple frames using multiple textures instead.

Can you give a short explenation of the variable levels_? Or tell me where i can read more about its usage?
I can se that my texture comes in 11 levels, but i dont understand why, and how that matters.

I se that levels_ are important in the loop:
[code]for (unsigned i = 0; i < levels_; ++i)
        {
            SetData(i, 0, 0, levelWidth, levelHeight, levelData);
            memoryUse += levelWidth * levelHeight * components;

            if (i < levels_ - 1)
            {
                image = image->GetNextLevel();
                levelData = image->GetData();
                levelWidth = image->GetWidth();
                levelHeight = image->GetHeight();
            }
        };[/code]

Would it be faster if the image had more or fever levels?
Forgive me for this question, as i am sure it is a stupid one.... :slight_smile:

-------------------------

cadaver | 2017-01-02 01:13:59 UTC | #6

Amount of mip levels. If you don't need them set amount of levels to 1, which means there's just one image at the full resolution. By default textures have mip levels down to 1x1. 

Actually you could try disabling mips as a first step if you don't need them, this could already speed up the upload. When ResourceCache is used to load textures, the texture configuration is specified by an accompanying .xml file, see for example bin\Data\Textures\UI.xml (accompanying UI.png)

-------------------------

