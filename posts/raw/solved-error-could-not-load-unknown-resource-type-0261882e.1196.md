gawag | 2017-01-02 01:06:00 UTC | #1

Hi,

I'm trying to set a shape texture for a spot light:
[code]light->SetShapeTexture(globals::instance()->cache->GetResource<Texture>("Textures/flashlight.png"));[/code]
And get his error:
[code]ERROR: Could not load unknown resource type 0261882E[/code]
Is it supposed to work like that?
I tried loading the file also as a JPG, but that gives the same error and the SetShapeTexture has also no effect.

I'm using a freshly build Urho just updated from Git.
Loading other files like materials and sounds works.
I guess a shape texture is an image that manipulates or customizes the spot light light spread like a projection or decal. But what's a ramp texture? That can be also set for lights.

-------------------------

friesencr | 2017-01-02 01:06:00 UTC | #2

Don't know if this is it but Texture is abstract try Texture2D

-------------------------

weitjong | 2017-01-02 01:06:00 UTC | #3

I think you intend to use a concrete class instead like Texture2D.

EDIT: Looks like someone else beat me to it.

-------------------------

gawag | 2017-01-02 01:06:01 UTC | #4

[quote]Don't know if this is it but Texture is abstract try Texture2D[/quote]
Ah *facepalm*. "ERROR: Could not load unknown resource type 0261882E" is a fancy way of saying "Dude that's an abstract base class, use a concrete one".
Oh, just looked at the Texture in OGLTexture.h (as I'm using OpenGL), that class is not abstract. Is that intended?
> still waiting for C++ concepts... C++11 they said, C++14 they said, C++17 they say...

[quote]http://urho3d.github.io/documentation/1.4/_lights.html "Both point and spot lights in per-pixel mode use an attenuation ramp texture to determine how the intensity varies with distance." It's a 1px tall image (however many pixels wide). The left-most pixel is the intensity right at the light's center, and the right-most pixel is intensity at the very edge of the light's radius. Controls light falloff basically.[/quote]
Ah didn't see that text as I only looked into the API reference. I already thought that, but I was thinking about 2D textures, which confused me. I think Ogre has a Texture1D, that would have also made it more obvious.

Can these two functions also use 3D textures? Why is it Texture and not Texture2D?

This is how it looks now (for a flashlight):
[img]http://i.imgur.com/4c2jaeT.jpg[/img]
(I drew the colored lines after not really seeing a difference, but it works basically.) I pasted the texture image in a red rectangle to the top left of this screenshot.
The texture is repeated to the right and the bottom but also weirdly cut off at the right side as you can see. Is this supposed to be like that and to be manually fixed with a [texturname].xml next to the image?

-------------------------

thebluefish | 2017-01-02 01:06:01 UTC | #5

[quote="gawag"][quote]
Oh, just looked at the Texture in OGLTexture.h (as I'm using OpenGL), that class is not abstract. Is that intended?
[/quote][/quote]

Yes. Texture is technically just a base class. Thing is, Texture is not a Resource. Therefore when it tries to find a Resource type with the name "Texture", it's not finding anything. However Texture2D [b]is [/b]a resource, and can be loaded just fine.

-------------------------

