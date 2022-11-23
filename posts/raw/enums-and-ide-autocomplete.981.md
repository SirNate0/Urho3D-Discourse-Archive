GoogleBot42 | 2017-01-02 01:04:35 UTC | #1

Autocomplete works just fine but it is very hard to use with enums and other constants...

Here is what I mean...

This is from Render.cpp
[code]void Renderer::SetShadowQuality(int quality)
{
    if (!graphics_)
        return;
    
    quality &= SHADOWQUALITY_HIGH_24BIT;
    
    // If no hardware PCF, do not allow to select one-sample quality
    if (!graphics_->GetHardwareShadowSupport())
        quality |= SHADOWQUALITY_HIGH_16BIT;
    if (!graphics_->GetHiresShadowMapFormat())
        quality &= SHADOWQUALITY_HIGH_16BIT;
    
    if (quality != shadowQuality_)
    {
        shadowQuality_ = quality;
        shadersDirty_ = true;
        ResetShadowMaps();
    }
}[/code]

Here is one example of the function being called from Engine.cpp
[code]...
        renderer->SetDrawShadows(GetParameter(parameters, "Shadows", true).GetBool());
        if (renderer->GetDrawShadows() && GetParameter(parameters, "LowQualityShadows", false).GetBool())
            renderer->SetShadowQuality(SHADOWQUALITY_LOW_16BIT);
        renderer->SetMaterialQuality(GetParameter(parameters, "MaterialQuality", QUALITY_HIGH).GetInt());
        renderer->SetTextureQuality(GetParameter(parameters, "TextureQuality", QUALITY_HIGH).GetInt());
...[/code]

Because the definition accepts an int it is not clear what is supposed to be passed into "SetShadowQuality".
If I start typing "quality" in an ide it won't list "SHADOWQUALITY_LOW_16BIT"...
So to use enums you need to remember the exact name of everything...

This is really frustrating when I don't know what the function wants to be input as the int.
I then have to grep the entire Urho3D source and find an example where the constant was used in the function.
With one of the constants now I then grep the entire source again and find where all of the constants were defined and find
the name of the constant value that I am looking for...

This takes a lot of time.

Here is another snip from GraphicsDefs.h:
[code]/// Texture units.
enum TextureUnit
{
    TU_DIFFUSE = 0,
    TU_ALBEDOBUFFER = 0,
    TU_NORMAL = 1,
    TU_NORMALBUFFER = 1,
    TU_SPECULAR = 2,
    TU_EMISSIVE = 3,
    TU_ENVIRONMENT = 4,
#ifdef DESKTOP_GRAPHICS
    TU_VOLUMEMAP = 5,
    TU_CUSTOM1 = 6,
    TU_CUSTOM2 = 7,
    TU_LIGHTRAMP = 8,
    TU_LIGHTSHAPE = 9,
    TU_SHADOWMAP = 10,
    TU_FACESELECT = 11,
    TU_INDIRECTION = 12,
    TU_DEPTHBUFFER = 13,
    TU_LIGHTBUFFER = 14,
    TU_ZONE = 15,
    MAX_MATERIAL_TEXTURE_UNITS = 8,
    MAX_TEXTURE_UNITS = 16
#else
    TU_LIGHTRAMP = 5,
    TU_LIGHTSHAPE = 6,
    TU_SHADOWMAP = 7,
    MAX_MATERIAL_TEXTURE_UNITS = 5,
    MAX_TEXTURE_UNITS = 8
#endif
};[/code]

This is useful.
If I have some func:
[code]int Foo(TextureUnit textureUnit)
{
   /// Do somthing
}[/code]

I can just type "Foo(TU_" and most of the possible values are listed.

Here is an example where this isn't done in GraphicsDefs.h:
[code]enum RenderSurfaceUpdateMode
{
    SURFACE_MANUALUPDATE = 0,
    SURFACE_UPDATEVISIBLE,
    SURFACE_UPDATEALWAYS
};[/code]

Here instead of following the camelcase the it just uses "SURFACE_"   This seems really inconsistent to me.

I think camelcase enums like TextureUnit's should be used everywhere for consistency.  Including constants that are treated as enums.  I hope I made sense. :\

-------------------------

thebluefish | 2017-01-02 01:04:36 UTC | #2

What IDE are you using? It works for me in both Visual Studio 2013 and Eclipse.

-------------------------

GoogleBot42 | 2017-01-02 01:04:36 UTC | #3

[quote="thebluefish"]What IDE are you using? It works for me in both Visual Studio 2013 and Eclipse.[/quote]
I am using qt creator...
But I am not sure if you understand my post... Autocomplete does work.  The inconsistencies of Urho3D's enum and constant naming makes autocomplete a pain to use because autocomplete generally only works when you know the beginning of what you are looking for.  But there is no single standard used in the naming of values of an enum and names of constants treated as enums.

-------------------------

cadaver | 2017-01-02 01:04:36 UTC | #4

There are some things which are actually bit combinations, in those cases enums are not used. Though I agree that the specific case of shadow quality (and probably others) could be converted to enum.

-------------------------

GoogleBot42 | 2017-01-02 01:04:37 UTC | #5

Could we also use a camelcase standard for naming of members of enums and for constants that are being used like enums?

For example:
[code]enum TestEnum
{
  TE_OPTION0 = 0,
  TE_OPTION1 = 1,
  TE_OPTION2 = 2,
};[/code]

And this:

[code]enum RenderSurfaceUpdateMode
{
    SURFACE_MANUALUPDATE = 0,
    SURFACE_UPDATEVISIBLE,
    SURFACE_UPDATEALWAYS
};[/code]

Could be changed to:

[code]enum RenderSurfaceUpdateMode
{
    RSUM_MANUALUPDATE = 0,
    RSUM_UPDATEVISIBLE,
    RSUM_UPDATEALWAYS
};[/code]

That way if you see a func that wants a value from the enum "RenderSurfaceUpdateMode", in an ide you can just type the first letter of each word and have all of the options.  Most of the time the names of the values of the enums are good enough.

-------------------------

cadaver | 2017-01-02 01:04:38 UTC | #6

After a bit more reviewing the quality & shadowQuality settings, I don't think I will be converting them to enums after all:

- shadow quality is used internally as a bitmask, and if it was an enum, clumsy code and casts between int <> enum would be necessary
- for material quality, you can actually define arbitrary quality levels up to QUALITY_MAX, which works better if it's an int, no need to define an enum values for all the in-between levels (which are not used by the engine btw.)
- for things like cycling through quality levels, like the samples do, it's easier if the quality levels are not enums, but integer math can be used throughout without casts.

-------------------------

