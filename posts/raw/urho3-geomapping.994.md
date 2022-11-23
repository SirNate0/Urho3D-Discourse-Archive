vivienneanthony | 2017-01-02 01:04:40 UTC | #1

Hi

how does Urho geomapping and terrain work? Does it take a RGB like .1,.1,.1 as the height value or something Red as height then maybe Blue or Green as something more finite value.

Vivienne

Or can I  modify the height map function to maybe use r as height then blue.as normal.

-------------------------

vivienneanthony | 2017-01-02 01:04:40 UTC | #2

If I think about it if the range of array is 0 to 1 convert it to 256*256 possibities with i use two channels. color * 8192 So, Red  would be (color/256) that would produce the first value then reminder would be the Green channel. Hmmm. 

I tried this but its not working. If I read your message correctly.

[code]/// generate perlin output
bool Procedural::GenerateBuild(float * inputData1, unsigned * output)
{
    /// loop through all the floats then convert to grayscale setting the color basis to .5 (forcing values 0 to 1)
    for(unsigned x = 0; x<width_; x++)
    {
        for(unsigned y = 0; y<height_; y++)
        {

            /// incremennt memory which seems to work
            int index = x+(y*height_);

            unsigned int color = inputData1[index]*8192;

            /// If elevation is over .5
            unsigned int heightscale=color/256;
            unsigned int heightprecision=color%256;

             /// test
            unsigned colr = heightscale;
            unsigned colg = heightprecision;
            unsigned colb = 0;

            unsigned int col = rgba32ToUInt(colr,colg,colb, 255);
            output[index] = col;      /// set grayscale - rgba is not needed. it seems to be screwy with this type of code.
        }
    }

    return true;
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:04:40 UTC | #3

The first idea did not work so I basically wiped it out.

I thought maybe I can scale the float 0 to 1 the heightmap to 0 to 255. Basically muiltplying that with the col. I thought leaves me with a reminder that can be the precision.

For example, scaled at one point is value 128 but there is a reminder of .124 which I think would be the precision. I simply muiltplied that by 255. Creating the second value the Green in the channels.

The result looked smooth when I used the method without the minecraft looking stuff. I am leaving the code here maybe you have a better idea.
[code]
/// generate perlin output
bool Procedural::GenerateBuild(float * inputData1, unsigned * output)
{
    /// loop through all the floats then convert to grayscale setting the color basis to .5 (forcing values 0 to 1)
    for(unsigned x = 0; x<width_; x++)
    {
        for(unsigned y = 0; y<height_; y++)
        {

            /// incremennt memory which seems to work
            int index = x+(y*height_);

            unsigned col = inputData1[index]* 255;  /// create color value

            float precision = ((float)inputData1[index]* 255)-col;

            col = rgba32ToUInt(col,precision*255, 0, 255);

            output[index] = col;      /// set grayscale - rgba is not needed. it seems to be screwy with this type of code.
        }
    }

    return true;
}
[/code]

Sorry. It's late my time. It's the only thing I can think off.

-------------------------

TikariSakari | 2017-01-02 01:04:40 UTC | #4

Thank you for the code. I might need something like this at some point, if I need to generate random battle maps. I was also considering of using the terrain with procedural map generation, so this will potentially save me a bit of time in the future.

This is not something that actually matters, but still good thing to know/do. You should probably have the for loops x and y the opposite way to avoid possible cache misses when indexing the array.

So instead of:
[code]    
    for(unsigned x = 0; x<width_; x++)
    {
        for(unsigned y = 0; y<height_; y++)
        {

            /// incremennt memory which seems to work
            int index = x+(y*height_);

            unsigned col = inputData1[index]* 255;  /// create color value
[/code]

swapping x and y around
[code]
    for(unsigned y = 0; y<height_; y++)
    {
        for(unsigned x = 0; x<width_; x++)
        {

            /// incremennt memory which seems to work
            int index = x+(y*height_);

            unsigned col = inputData1[index]* 255;  /// create color value
[/code]

But since you are most likely only building this once and if the width/height isn't a huge number there is a possibility that not that many misses even happen or even if they do, it might not matter.

-------------------------

Bananaft | 2017-01-02 01:04:41 UTC | #5

[quote="Sinoid"]all terrain tools I know / have used will let you spit out R+G as height.[/quote]

Can you please name some? If I'll get 16bit heightmap TIFFs, what is the best way to split em on two channels?

-------------------------

vivienneanthony | 2017-01-02 01:04:41 UTC | #6

No problem. 

The code I modified to account for y scale. 

The thing about the code its  part of several procedual generation class and components not in the native code. Its something I put together.

It needs to be faster in general and unload the computation on a GPU. I want the base computation to less then a second. 

 I welcome anyone who want to assist getting the code more feature rich, faster, and preppef to be added


Vivienne

 [quote="TikariSakari"]Thank you for the code. I might need something like this at some point, if I need to generate random battle maps. I was also considering of using the terrain with procedural map generation, so this will potentially save me a bit of time in the future.

This is not something that actually matters, but still good thing to know/do. You should probably have the for loops x and y the opposite way to avoid possible cache misses when indexing the array.

So instead of:
[code]    
    for(unsigned x = 0; x<width_; x++)
    {
        for(unsigned y = 0; y<height_; y++)
        {

            /// incremennt memory which seems to work
            int index = x+(y*height_);

            unsigned col = inputData1[index]* 255;  /// create color value
[/code]

swapping x and y around
[code]
    for(unsigned y = 0; y<height_; y++)
    {
        for(unsigned x = 0; x<width_; x++)
        {

            /// incremennt memory which seems to work
            int index = x+(y*height_);

            unsigned col = inputData1[index]* 255;  /// create color value
[/code]

But since you are most likely only building this once and if the width/height isn't a huge number there is a possibility that not that many misses even happen or even if they do, it might not matter.[/quote]

-------------------------

Bananaft | 2017-01-02 01:04:42 UTC | #7

[quote="Sinoid"]
Now that I think about it, it's really not that many (stupid me). Just L3DT, Terragen (plugin IIRC), and Grome. I probably botched that because when I wrote a heightmap loader/sculpter/painter for libgdx R+G was the first thing I did (I could drop that onto github if need be for you - it's messy and java, but it works). My bad.

No idea on your TIFF issue. It'd be easier if it was RAW, everyone can write a RAW loader. What formats can you output (or what are you using)?
[/quote]

Thank you for reply.

From this thread I've just found out about two channel system, and want to know how to use it, given, I have some 16bit heightmap. Let's say, I can output any format, tiff, raw, whatever. I need a way to process them into R+G image, that Urho3d can read (PNG or such).

I've checked free version of L3DT, and didn't found two channel R+G output.

If your java thingy may help me with that, then I sure want to check it.

-------------------------

Bananaft | 2017-01-02 01:04:43 UTC | #8

[quote="Sinoid"]
I'll write a TIFF converter. Will take a day or two.[/quote]

Whoa! ok, cool. Can't wait to try.

I also found out, that PNG has 16bit support, but Urho3d crashes trying to load it.

-------------------------

TikariSakari | 2017-01-02 01:04:43 UTC | #9

I tried using 8bit monochrome pngs, but I think it treats them differently somehow, altho it did work for the heightmap. The picture did work though, but maybe it counts 2 pixels in a row for one 16bit data.

-------------------------

Bananaft | 2017-01-02 01:04:44 UTC | #10

[quote="Sinoid"]
I might be almost done with this packer but I could use more test files that came from different programs. Can you toss up a TIFF file of yours onto dropbox or someplace and PM me a link, tell me where the TIFF came from, and even better if you've got some screenshots (like from inside the tool the tiff was generated from, for height/feature-point reference)?[/quote]

Just PM'd you two test images.

-------------------------

friesencr | 2017-01-02 01:04:44 UTC | #11

For nix users just use image magick

sudo apt-get install imagemagick
convert input.tiff output.png

-------------------------

Bananaft | 2017-01-02 01:04:48 UTC | #12

Hey, Sinoid.

I finally got my hands on your Tiff packer.

Thank you very much for this awesome tool!

[url=http://i.imgur.com/iKjJnAs.png][img]http://i.imgur.com/iKjJnAsl.png[/img][/url]

-------------------------

