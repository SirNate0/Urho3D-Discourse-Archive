mayatforest | 2017-01-02 01:13:40 UTC | #1

Hi.
I have some problems with getting screenshot from scene using Graphics.ResolveToTexture (Xamarin,Android,Mali400).

This code work fine in genymotion bad generate bad texture on real hardware

[code]
				int width = graphics.Width;
				int height =graphics.Height;
				
/////////
				Urho.Urho2D.Texture2D renderTexture = new Urho.Urho2D.Texture2D();
				renderTexture.SetSize(width, height, Graphics.RGBAFormat, TextureUsage.Rendertarget);
				renderTexture.FilterMode = TextureFilterMode.Bilinear;
				Graphics.ResolveToTexture(renderTexture, new IntRect(0, 0, width, height));

				///adding to sprite to see what getted
				sprite = new Sprite();
				Root.AddChild(sprite);
			         sprite.Texture = texture;
			sprite.SetSize(256, 256);
			sprite.BlendMode = BlendMode.Replace;
			sprite.Position = new IntVector2(0, 0);

//saving to png
int size = width * height * 4;
				IntPtr ptr = Marshal.AllocHGlobal(size);

				bool res = renderTexture.GetData(0, ptr);
		
					byte[] barr = ptr.ToBytesArray(size);

					Java.Nio.ByteBuffer byteBuffer = Java.Nio.ByteBuffer.Wrap(barr);

					Android.Graphics.Bitmap newBitmap = Android.Graphics.Bitmap.CreateBitmap(width, height, Android.Graphics.Bitmap.Config.Argb8888);

					newBitmap.CopyPixelsFromBuffer(byteBuffer);

					System.IO.FileStream stream = new System.IO.FileStream(filepath, System.IO.FileMode.Create, System.IO.FileAccess.Write);
					rotatedBitmap.Compress(Android.Graphics.Bitmap.CompressFormat.Png, 100, stream);
					stream.Close();

[/code]

///resulting image from real hardware
[img]http://savepic.ru/10902002.png[/img]

//genymotion
[img]http://savepic.ru/10895861.png[/img]

-------------------------

cadaver | 2017-01-02 01:13:40 UTC | #2

Have you tried Graphics::TakeScreenshot()? It has less moving parts, since it does just glReadPixels() from the backbuffer.

-------------------------

mayatforest | 2017-01-02 01:13:40 UTC | #3

Yes, i tryed TakeScreenShot it get just black image on real device.

-------------------------

cadaver | 2017-01-02 01:13:41 UTC | #4

I reproduced the black screenshot issue for TakeScreenshot() on Android device. Should be fixed in the master branch, now it takes the image as RGBA on OpenGL ES. ResolveTexture() I didn't touch.

-------------------------

mayatforest | 2017-01-02 01:13:54 UTC | #5

Hi, while im waiting for bump version of urho in xamarin, i tryed this code directly from app

[code]
				int GL_RGBA                           =0x1908;
				int GL_UNSIGNED_BYTE                  =0x1401;
			
					int sizeb = width * height * 4;
					IntPtr ptri = Marshal.AllocHGlobal(sizeb);

					byte[] barr1 = ptri.ToBytesArray(sizeb);

					Java.Nio.ByteBuffer byteBuffer = Java.Nio.ByteBuffer.Wrap(barr1);

					Android.Opengl.GLES20.GlReadPixels(0, 0, width, height,GL_RGBA, GL_UNSIGNED_BYTE, byteBuffer);
					int err=Android.Opengl.GLES20.GlGetError();
[/code]

Code calls in OnUpdate loop, err return 0, but barr1 is filled with zero. What may be wrong with this code?

-------------------------

