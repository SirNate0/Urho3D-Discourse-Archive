Victor | 2017-01-02 02:11:00 UTC | #1

So recently I had been trying to figure out how to properly load in 16-bit heightmaps. Using a library called lodepng (and cadaver's help), I was able to solve this issue.

Problem:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b13f1b9a99ef54f409fc22419ea91eebdbf48c6b.png[/img]

Goal:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9b8b5355d283091df61a4cf910d5a7a83b0105f4.png[/img]

Code:

[b]Load in your 16bit png[/b]
[code]
std::vector<unsigned char> pngData;
std::vector<unsigned char> image;
unsigned width = 0, height = 0;
lodepng::State state;

unsigned error = lodepng::load_file(pngData, rawImageFilePath.CString());
if (!error) error = lodepng::decode(image, width, height, pngData, LCT_GREY, 16);

if (error) {
    URHO3D_LOGERROR(String("Unabled to load raw PNG file @ ") + rawImageFilePath);
    return nullptr;
}
[/code]

[b]Convert 16bit to 8bit by packing data into the R and G channels as told in the Terrain doc[/b]
[code]
// Storage for our 16bit pixel.
union uimage_data
{
    uint16_t s;
    uint8_t b[2];
};

Image* img = new Image(context_);
unsigned components = 2; // R & G channels.
unsigned dataLen = width * height * components;
unsigned char* pixelData = new unsigned char[dataLen];
img->SetSize(width, height, components);

unsigned imgDataIndex = 0;
unsigned index = 0;
unsigned imgSizeHalf = static_cast<unsigned>(image.size() / 2);
uimage_data* sData = new uimage_data[imgSizeHalf];

// Copy over the pixel data into our storage.
for (index = 0; index < imgSizeHalf; index += 2, imgDataIndex += 1) {
    // Store in big-endian which is what lodepng uses.
    sData[imgDataIndex].b[0] = image[index + 1];
    sData[imgDataIndex].b[1] = image[index];
}

// Update our pixel data for Urho3D.
imgDataIndex = 0;
for (index = 0; index < dataLen; index += components, imgDataIndex += 2) {
    pixelData[index] = sData[imgDataIndex].b[0];
    pixelData[index + 1] = sData[imgDataIndex].b[1];
}
[/code]

There are probably optimizations that can be done. I need to go over the code once more, but so far this works. I hope this helps anyone else that may have the same issue.

-------------------------

Ka-Wiz | 2017-10-23 22:29:09 UTC | #2

Hey there, first of all I've seen your Crown of Rulers project on the forums and I think it's awesome :smiley:

Anyway, I was just trying to solve this same problem. When I found this post I got super excited, but unfortunately your code did not work for me :( It did lead me in the right direction however!

I was able to go from
![terraced|690x492](upload://9yGucrWceWrYmJwJRLVN9mjE89P.png)
to
![fixed|690x491](upload://uMwOWhqnnbcZsfsSGBpfAi7r6Le.png)

with

    Image* img = new Image(context_);
	std::vector<unsigned char> pngData;
	std::vector<unsigned char> image;
	unsigned width = 0, height = 0, components = 2; // components = R&G channels
	unsigned error = lodepng::load_file(pngData, "YourHeightmapPathHere");
	if (!error) error = lodepng::decode(image, width, height, pngData, LodePNGColorType::LCT_GREY, 16);
	if (!error) {
		img->SetSize(width, height, components);
		img->SetData(reinterpret_cast<unsigned char*>(&image[0]));
	}
	else
		URHO3D_LOGINFO("Unabled to load raw PNG file in lodepng");

I'm not really sure why this works, or what changed in the engine (or lodepng?) since your code was written; I'm not doing any of the R&G packing that the SetHeight documentation specifies but hey, it works. It might have something to do with the way L3DT writes the heightmap data to PNG, but I don't know enough about PNG format to say definitively.

-------------------------

Victor | 2017-10-24 04:31:32 UTC | #3

Oh! Yeah I haven't checked back on this to see if anything has changed. I believe the code still works for me, although I do like how you have simplified the SetData part of your code. :) Nice work!

-------------------------

