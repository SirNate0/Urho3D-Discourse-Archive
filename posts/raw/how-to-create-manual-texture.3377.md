ppsychrite | 2017-07-24 16:58:10 UTC | #1

For some reason Urho3D's image loader is unable to load my .png file, so I used lodePNG. It worked fine but I'm having a hard to creating a texture over it.
I Make an Urho3D::Image Set the image's pixels based on the unsigned char array (lodePNG repeats array as RGBARGBARGBA)
This works fine as I have some pixel colors logged and they seem to be unique.

I then make a new Texture2D and set it's data to the image.
This is where it breaks I believe. 
In the logs it says 

    ERROR: No texture created, can not set data

and if it's concerning this is how I make the texture (Seems right)

    ur::Texture2D *tex = new ur::Texture2D(context_);
	tex->SetNumLevels(1);
	tex->SetData(0,0,0, width, height, image->GetData());

Am I doing it wrong possibly?

-------------------------

Victor | 2017-07-23 00:51:26 UTC | #2

Hmm, try doing tex->SetSize before doing SetData.

-------------------------

ppsychrite | 2017-07-23 13:23:44 UTC | #3

Doing 

    tex->SetSize(width, height, 0);

Before SetData gives me an error "Failed to create texture" 
Attempting to do Texture2D's SetData function with only an image as an arg throws an exception at OGLTexture2D.cpp too.

-------------------------

1vanK | 2017-07-23 14:45:52 UTC | #4

texture->SetData(image)

-------------------------

Victor | 2017-07-23 14:46:22 UTC | #5

With SetSize you'll want to not give it 0 components. Try setting that last parameter to 3 (RGB)

-------------------------

Victor | 2017-07-23 14:48:48 UTC | #6

I was a bit hesitant to give that solution. I recently had an issue where I had to set the size first.  :( Not sure if that's a new issue or not.

-------------------------

1vanK | 2017-07-23 14:51:53 UTC | #7

Urho3D\Graphics\OpenGL\OGLTexture2D.cpp

```
bool Texture2D::SetData(Image* image, bool useAlpha)
{
...
SetSize(levelWidth, levelHeight, format);
...
SetData(i, 0, 0, levelWidth, levelHeight, levelData);
...
}
```

-------------------------

ppsychrite | 2017-07-24 15:21:51 UTC | #8

Calling that specifically is what throws the exception.

    ur::Texture2D *tex = new ur::Texture2D(context_);
	tex->SetNumLevels(1);
	//tex->SetSize(width, height, 0);
	tex->SetData(texture);
			
This for some reason throws an exception on line 227 of OGLTexture2D.cpp (on the "switch (components)")

EDIT: After trying to call  SavePNG to the image and being unable to open it, it looks like the problem lies in the image itself :thinking:

If it matters this is how I get the pixels

    	std::vector<unsigned char> imgData;
			unsigned width, height;
			unsigned error = lodepng::decode(imgData, width, height, "Data/image.png");

			ur::Image *texture = new ur::Image(context_);
			texture->SetSize(width, height, 0);
			
			for (unsigned x = 0; x < width; ++x) {
				for (unsigned y = 0; y < height; ++y) {
					unsigned int iter = x * width + y;
					ur::Color color = RGBToColor(imgData[iter], ///RGBToColor converts unsigned char to 0.0-1.0
						imgData[iter + 1],
						imgData[iter + 2]);

					texture->SetPixel(x, y, color);
				
			
				}
			}

-------------------------

1vanK | 2017-07-24 16:44:11 UTC | #9

```
unsigned int iter = x * width + y;
```
may be 
```
unsigned int iter = y * width * 3 + x * 3 ;
```

or *4 ?

-------------------------

ppsychrite | 2017-07-24 16:58:01 UTC | #10

Still doesn't seem to work. :confused:
The png file created is 73 bytes long, when the actual file is around 21 kb.
 
Alright. I'm confused now, I tried using ResourceCache to get the http requested image and now it works perfectly fine. I'm not sure how it started working fine now. Just yesterday it was complaining that it couldn't read the .png.

Anyways, thanks for your help guys!

-------------------------

