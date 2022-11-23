Bananaft | 2017-07-02 21:11:38 UTC | #1

I need a way to pass some numbers from GPU back to CPU. First I tried:
<code>
Image@ img =logTex.GetImage();
Color px = img.GetPixel(0,0);
</code>

It worked great for single pixel and I was able to pass four 8-bit numbers back into AngelScript. Problem is, If I try to read more pixels, performance will drop very fast. As I understand, code above stops whole pipeline (both CPU and GPU) for a moment to read a single pixel. And more pixels I read, the longer pipeline stays idle. Not cool.

I know, there should be a better way to do it. Copy image? I don't mind it to lag a few frames, I just want to pass more data from GPU without stalling whole render pipeline.

Thanks in advance for any thoughts and suggestions.

-------------------------

kostik1337 | 2017-07-03 08:23:11 UTC | #2

Are you doing GetImage() for each pixel?

-------------------------

1vanK | 2017-07-03 08:48:39 UTC | #3

 https://github.com/1vanK/Urho3DBitmapFontGenerator

 https://github.com/1vanK/Urho3DBitmapFontGenerator/blob/master/Source/BFGenerator.cpp
see BFGenerator::CalcField() how send texture with packed data to shaders and calc heavy matematics on GPU
After it you always can use GetImage() for rendered Texture2D

p.s. I read the question carefully and do not understand why img.GetPixel() is slow, image already on CPU

-------------------------

Bananaft | 2017-07-03 20:38:11 UTC | #4

[quote="kostik1337, post:2, topic:3312, full:true"]
Are you doing GetImage() for each pixel?
[/quote]
No, here what I do for performance test:
<code>		
Image@ img =logTex.GetImage();
Array<Color> px(256);
for(int i=0; i<256; i++)
{
	px[i] = img.GetPixel(i,0);
}
</code>

and numbers I'm getting (update):
16   4.5ms
32   7ms
64   16ms
128 20ms
256 35ms

[quote="1vanK, post:3, topic:3312"]
do not understand why img.GetPixel() is slow
[/quote]

well, maybe I'm wrong, and it's just AngelScrip does it slow. But since even smaller numbers affect frame time, I assumed it stalls whole pipeline.

I should probably try C++. (Oh no! :confused:  )

-------------------------

Eugene | 2017-07-03 20:53:44 UTC | #5

[quote="Bananaft, post:4, topic:3312"]
256 35ms
[/quote]
This is surprisingly slow even for AS.

-------------------------

Bananaft | 2017-07-24 21:10:41 UTC | #6

Hello again. So, I spent couple weeks learning C++. I added this code to to 10_RenderToTexture.cpp, it takes texture just rendered, copies it into image, and then converts image into Vector4 array.
<code>
    	texImg = new Image(renderTexture->GetContext());
	texImg->SetSize(txSize, txSize, 4);
	renderTexture->GetData(0, texImg->GetData());
		for (int i = 0; i < txSize; i++)
	{
		for (int j = 0; j < txSize; j++)
			texData[i][j] = texImg->GetPixel(i, j).ToVector4();
	}
</code>

It works insanely fast, 256x256 10ms 512x512 30ms in Debug, 1024x1024 (million pixels) 25ms in Release.
 Ad I guess 2k pixels (32x64) should cover all my needs and some more.

I now just need a way to pass it into AS without loosing momentum. :)

-------------------------

