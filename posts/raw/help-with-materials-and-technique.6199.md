btschumy | 2020-06-13 15:42:35 UTC | #1

I am taking a galaxy simulation that I have running on iOS and Mac using SceneKit, and porting it to UrhoSharp.  I'm having a problem with the material for the galaxy.  In SceneKit I could just set the diffuse component of the material to the galactic .png image and it would show up with no lights.

In Urho3D, I don't seem to be able to accomplish this although I'm sure it must be possible.  It I use this:

    <?xml version="1.0"?>
    <material>
        <technique name="Techniques/Diff.xml" />
    	<texture unit="diffuse" name="Data/Textures/Galaxy-North.dds" />
        <cull value = "none"/>
    </material>

Then the object doesn't show up unless I have a light defined.  Even then only one side of the Plane seems to be lit.

I tried making the material emissive, but that also doesn't work:

    <?xml version="1.0"?>
    <material>
        <technique name="Techniques/DiffEmissive.xml" />
    	<texture unit="emissive" name="Data/Textures/Galaxy-North.dds" />
        <cull value = "none"/>
    </material>

Even with a light, the object doesn't show up.

Can someone tell me what is needed to have the galaxy act as if it were emitting light?

-------------------------

SirNate0 | 2020-06-13 19:00:53 UTC | #2

You can use the DiffUnlit technique if you don't have any lights. Though I kind of wonder if you have some sort of other problem like a camera pointed in the wrong direction or an incorrect resource name since the emissive technique didn't work.

If suggest two things to address those: Create a model like a cube with one of the existing materials, like the Stone material from the samples. If you can see that, then change the material to your Galaxy one. Also, check the log to see if it was unable to find/load any resources (such as your texture, which you possibly should have `name="Textures/Galaxy-North.dds"` for depending on your actual directory structure).

-------------------------

btschumy | 2020-06-13 21:01:59 UTC | #3

Thanks for the response.

I'm quite sure I have the camera pointed correctly.  I can swap the two materials and the galaxy is visible with "diffuse" and a light source, but not with "emissive" and no light.  The image is definitely being loaded.

The "DiffUnlit" technique with the TextureUnit set to "diffuse" seems to work.  If I set it to "emissive", I get nothing visible.  Admittedly, I don't know much about this, but you would think that is what emissive is for.

While I have you (and others), I originally used a .png file for the galaxy texture.  It sort of worked, but the colors were wrong, almost inverted.  On a whim I tried converting to DDS and with that it looks fine.  I'd prefer the .png file because it is slightly smaller.  Any idea about why this doesn't work?  The file was created on a Mac if that matters.

-------------------------

lezak | 2020-06-13 21:30:24 UTC | #4

Your emissive material is missing:
`<parameter name="MatEmissiveColor" value="1 1 1" />`
(or any other desired value).

-------------------------

btschumy | 2020-06-13 21:47:32 UTC | #5

Lezak,

Are you saying this will fix the color inversion of the PNG?  Or is this why the "emissive" TextureUnit isn't woking?  If the latter, is this better in some way than using "diffuse" which is working with "DiffUnlit"?

-------------------------

btschumy | 2020-06-13 21:56:03 UTC | #6

I just tried this and it doesn't seem to affect the color inversion with the PNG file.  It also doesn't make the galaxy visible if I make the image emissive rather than diffuse.  So I guess I don' understand what you are suggesting.

-------------------------

lezak | 2020-06-13 22:05:48 UTC | #7

This was just a suggestion how to fix emmisive color, as for png problem I don't have idea what may be causing it.

-------------------------

SirNate0 | 2020-06-13 23:56:57 UTC | #8

Is it a 16 bit png or anything like that? If you can upload a screenshot and/or the file that might make it easier to determine what's going wrong.

-------------------------

btschumy | 2020-06-14 14:23:26 UTC | #9

No, it is an 8-bit png.

Here is what it looks like in Urho3D: http://www.otherwise.com/images/GalaxyPNG.png
Here is what the image converted to DDS looks like in Urho3D: http://www.otherwise.com/images/GalaxyDDS.png

[I guess I have to post the actual image in another reply.  I'm only allowed two links in a post as a new user]

I appreciate any help you can give in figuring this out.  I have tried exporting the PNG to another PNG in several image apps and the exported version do the same thing.

-------------------------

btschumy | 2020-06-14 14:24:02 UTC | #10

Here is the actual .png file: http://www.otherwise.com/images/Galaxy-North.png

-------------------------

SirNate0 | 2020-06-14 18:29:10 UTC | #11

Checking with GIMP it looks like it's flipped the R and the B channels. Not sure what that's from, though my guess is that somewhere it's loading it or passing it to the GPU or displaying it as BGRA instead of RGBA (or vice versa). Hopefully someone else can help you track down what's actually causing the problem.

It might be specifically a problem with iOS? It's showing up fine for me in the editor on Linux.![image|690x196](upload://6Hxi7do55IhFz8oqQsVyqd4G4cN.png)

-------------------------

btschumy | 2020-06-14 20:02:08 UTC | #12

I tried using some other random image I had to see if it would also swap R & B.  It was an image on a sunset and it came to with blue sunset colors rather than red.  When I exported the image I chose the color profile "Most Compatible".  I will play around with others to see if I can find one that works.

So I guess this is a Mac thing and it uses a format that Urho3D doesn't recognize correctly.  I've never heard of such a thing.  You would think this would be a widely reported problem Mac image apps were doing something non-standard.

Thanks for your help.

-------------------------

SirNate0 | 2020-06-14 20:55:35 UTC | #13

Do the Urho 3d samples/editor work fine for you or do they swap the colors as well? (You'll want to make sure you check with a material that doesn't use a DDS texture)

-------------------------

btschumy | 2020-06-15 15:39:14 UTC | #14

I didn't see any problems with the FeatureSamples apps.  I also tried SamplyGame and the colors seemed fine there.  As far as I can tell thy are using mostly .png textures.

However, I did discover a couple of things.  

1. I created a .png on Windows and used it unaltered on Mac.  The colors are again reversed there (always red/blue reversal).
2. If I run the app on Android, the colors are fine there.  So this seems to me to be some bug in the iOS implementation of Urho3D.  Note: I am using Xamarin and UrhoSharp to run this.

I think all I can do now is submit a bug report on this.

-------------------------

