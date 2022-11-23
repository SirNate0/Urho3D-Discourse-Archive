mayatforest | 2017-01-02 01:13:08 UTC | #1

Hi.
We working on application with Xamarin+Urho on Android.
And have strange problem with displaing sprites and terrarin textures.

Left side of image is screenshot geted from real device and sprite consists of pixel doted pattern over it. Right site is bitmap that copied to sprite.
[img]http://savepic.ru/10370017.png[/img]

What we do wrong?

Code that we use to draw on sprite.

[code]
const int cnt = 5;

        Sprite[] spriteList = new Sprite[cnt];
        Texture2D[] textureList = new Texture2D[cnt];

        private Texture2D GetTexture(int h , int w)
        {
            #region TestDrawTexture

            Texture2D texture=new Texture2D();
            texture.FilterMode = TextureFilterMode.Nearest;
            texture.SetNumLevels(1);
            texture.SetSize(w, h, Graphics.RGBAFormat, TextureUsage.Static);

            return texture;
            #endregion
        }

        public bool DrawOnSprite(int num, Bitmap bitmap)
        {
            #region DrawOnSprite
            try
            {
                if (num < 0 || num > cnt)
                {
                    return false;
                }

                if (textureList[num] == null)
                {
                    textureList[num] = GetTexture(bitmap.Height, bitmap.Width);
                }

                Texture2D texture = textureList[num];

                unsafe
                {
                    int psize = bitmap.Width * bitmap.Height * 4;
                    int[] pixels = new int[psize];


                    if (pixels == null)
                    {
                        log.WriteError("Error in DrawOnSprite, pixels == null");
                        return false;
                    }

                    {
                        bitmap.GetPixels(pixels, 0, bitmap.Width, 0, 0, bitmap.Width, bitmap.Height);

						MainModule.obj.SaveBitmap(bitmap,"bitmap_"+num.ToString()+".png");


                        fixed (void * data = &(pixels[0]))
                        {
                            if (data == null)
                            {
                                log.WriteError("Error in DrawOnSprite, data == null");
                                return false;
                            }

                            bool result_SetData = texture.SetData(0, 0, 0, texture.Width, texture.Height, (void *) data);

                            if (result_SetData == false)
                            {
                                log.WriteError("Error in DrawOnSprite, SetData to textute return false");
                                return false;
                            }


                            if (spriteList[num] == null)
                            {
                                spriteList[num] = new Sprite();
                            }

                            Sprite sprite = spriteList[num];

                            sprite.Texture = texture;
                            sprite.SetSize(128, 128);
                            sprite.BlendMode = BlendMode.Replace;

                            int x = (int) (840/6);
                            int y = (int) (480/8) + num * sprite.Height + 20;
                            sprite.Position = new IntVector2(x, y);

                            ApplicationIUHelperClass.obj.AppUI.Root.AddChild(sprite);
                        }
                    }

                    return true;
                }

            }
            catch (Exception ex)
            {
                log.WriteError("Error in DrawOnSprite", ex);
            }
            return false;
            #endregion
        }

[/code]

-------------------------

gawag | 2017-01-02 01:13:09 UTC | #2

The images look like the red and the blue color channel is switched. I guess one is RGB and the other BGR. Do you mean that by strange pattern?

Maybe switching
[code]
texture.SetSize(w, h, Graphics.RGBAFormat, TextureUsage.Static);
[/code]
to 
[code]
texture.SetSize(w, h, Graphics.BGRAFormat, TextureUsage.Static);
[/code]
helps?
Can't find anything in the code and I have no idea where RGBAFormat is even defined.

If this "chess pattern" with the red, green and blue dots is not supposed to be there: what is there in the image? A solid color? Is something being drawn on top of the image?

-------------------------

Modanung | 2017-01-02 01:13:10 UTC | #3

[quote="gawag"]The images look like the red and the blue color channel is switched. I guess one is RGB and the other BGR. Do you mean that by strange pattern?[/quote]
The pattern is very faint and maybe not even visible on some screens. Here's the same image with increased contrast:
[img]http://luckeyproductions.nl/images/DottedPattern.png[/img]

-------------------------

gawag | 2017-01-02 01:13:11 UTC | #4

Oh that I did not see at all. Now that you mentioned it I saw it also in the original image.

That looks really strange. Is that only when rendering the image? Is it also visible without an image (solid background color)? Does it also occur with other "3d rendering applications" like games? Do the Urho samples have that too?
Could be something really hard to find and solve like an OpenGL bug.

-------------------------

cadaver | 2017-01-02 01:13:11 UTC | #5

This looks like it could be output dithering on the device, if its framebuffer is just 16 bits. I think I encountered this on some Android devices but couldn't find out how you would reliably control the output bitdepth (on Android) in SDL library's runtime configuration.

-------------------------

mayatforest | 2017-01-02 01:13:11 UTC | #6

Hi, thanks for answers.

I got screenshot from urho samples/static scene example - to avoid problems in our code
[img]http://savepic.ru/10440625.png[/img]

On the left - screen from device
On the right - screen from genymotion emulator

As you can see for example Grey joystick on the left is filled by same pattern.

So if its 16 bit framebuffer, how i can change this ? Or may by test by another opengl application? Its device problem or urho?

-------------------------

mayatforest | 2017-01-02 01:13:11 UTC | #7

This screenshot from device using this test app [url]https://play.google.com/store/apps/details?id=com.rtsw.opengldemo&hl=en[/url] and no doted pattern

[img]http://savepic.ru/10423220.png[/img]

-------------------------

hdunderscore | 2017-01-02 01:13:11 UTC | #8

Maybe this is relevant: [forums.libsdl.org/viewtopic.php ... eea1e2a634](https://forums.libsdl.org/viewtopic.php?t=11915&sid=84b9b1355fa97daea83523eea1e2a634)

-------------------------

mayatforest | 2017-01-02 01:13:11 UTC | #9

Ok, how i can try call this function glDisable(GL_DITHER) under xamarin - urho ?

-------------------------

mayatforest | 2017-01-02 01:13:12 UTC | #10

Hi i googled, that our device with mali400 have GL_DITHER enabled by default
[url]http://stackoverflow.com/questions/11501514/opengl-es-2-0-artifacts-dithering-in-fbo-on-mali-400[/url]

So, i searched in code of urho and dont see any api to call to modify gl_dither. 

How i can change this value?

-------------------------

mayatforest | 2017-01-02 01:13:25 UTC | #11

Hi.
I found method to fix this call to Android.Opengl.GLES20.GlDisable(Android.Opengl.GLES20.GlDither); $)
BW in next release of urho will be added method to set Dither directly in properties.
See here [url]https://github.com/xamarin/urho/issues/137[/url] and [url]https://github.com/urho3d/Urho3D/issues/1489[/url]

Thanks to all.

-------------------------

