ppsychrite | 2017-10-30 23:52:58 UTC | #1

Saving screenshots to .png on file works fine but the background color is saved too, is there any built in Urho3D way of making the background transparent?
If no is there any possible libraries I could use?

-------------------------

jmiller | 2017-10-28 20:44:15 UTC | #2

You can render to texture, like this but with GetRGBAFormat() instead.
  https://github.com/urho3d/Urho3D/blob/master/Source/Samples/10_RenderToTexture/RenderToTexture.cpp#L184

RenderPath related things (fog)
  https://discourse.urho3d.io/t/how-to-save-alpha-information-by-using-render-surface/2723

Some code here to save a PNG with alpha from Texture2D:
  https://discourse.urho3d.io/t/saving-scene-to-2d-texture-with-transparency/3523/4

HTH

-------------------------

ppsychrite | 2017-10-28 20:31:57 UTC | #3

I'll look into it!
Many Thanks :smiley:

-------------------------

ppsychrite | 2017-10-28 21:26:01 UTC | #4

Hmm. Some interesting stuff came out of me adding it to the RTT sample. 
   
        SharedPtr<Image> image(new Image(context_));
		image->SetSize(tex->GetHeight(), tex->GetWidth(), tex->GetComponents());
		tex->GetData(0, image->GetData());

		image->SavePNG("test.png");

Looks perfectly find but the file created is this: ![test|375x500](upload://umpBWNdCokPU21GEcZNrx1BRDD8.jpg)
You can *kind of* see the cubes but nothing to what I was projecting for. (Yes I did try RGBA)

-------------------------

jmiller | 2017-10-29 19:49:59 UTC | #5

Your code seems to be typical with regard to getting the image components.

I have not seen this before, but maybe someone can identify what's going on, based on the artifacts...

-------------------------

SirNate0 | 2017-10-30 21:03:49 UTC | #6

I'm not sure what's going on with the artifacts -- I assume the cubes are not supposed to be stripes, correct? Also, I assume you converted the image to a jpg from a png later in another program?
I will say, make sure you set the clear color to transparent when you render it. I use a custom render path when I'm trying to save transparent images: (note the clear command)
```xml
<!--Forward-->
<renderpath>
    <command type="clear" color="0 0 0 0" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>
```

-------------------------

ppsychrite | 2017-10-30 12:30:39 UTC | #7

No, I call SavePNG() directly instead of JPG.
hmm thanks for the RenderPath I'll try it after school. :smile:

-------------------------

t.artikov | 2017-10-30 21:03:49 UTC | #8

Width and height are passed in the wrong order into image->SetSize(...).

-------------------------

jmiller | 2017-10-30 14:51:36 UTC | #9

Nice spot. :slightly_smiling_face:

-------------------------

ppsychrite | 2017-10-30 21:06:12 UTC | #10

@t.artikov How foolish of me :man_facepalming:
Always the simple things that I mess up on
Many thanks!

@SirNate0
Thank you a ton for your example xml file, I do not know how to make material/etc xml files but this will provide great reference I hope :smiley:

-------------------------

