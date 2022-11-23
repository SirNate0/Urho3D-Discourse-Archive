Enhex | 2017-01-02 01:04:39 UTC | #1

I tried to search the source for supported format but unsigned leads to nowhere and the only BGRA stuff I find is in third party libs.
What values can "unsigned format" have?
Does it support BGRA?

-------------------------

cadaver | 2017-01-02 01:04:40 UTC | #2

The format is directly the API-specific format, on OpenGL it's GL_ values, on D3D11 it's from the DXGI format enum etc. This should be refactored at some point to share an internal pixelformat enum with both the Image & Texture classes.

If you use formats outside of what the static functions Graphics::GetXXXFormat() return, you run the risk of helper functions like Texture::GetRowDataSize() not working correctly, unless you also patch them to support the new formats.

-------------------------

thebluefish | 2017-01-02 01:04:41 UTC | #3

You could write a shader that swaps the channels. That would probably be the ideal way. Alternatively, you could swap them directly, though it would be slower doing it on CPU rather than GPU.

-------------------------

najak3d | 2020-09-17 06:48:28 UTC | #4

I am running into this issue now.

Because we render to more than one Surface/Control, we are using the Urho3D recommendation for "Render To Texture" and then using "GetData()" on the Texture2D to grab the image data, and then we are pushing this image data to a Skia Canvas View.

We have a conundrum on UWP - because the UrhoSurface has channel order BGRA, while the Skia Bitmap has channel order RGBA.    And so our Red and Blue channels are swapped.

Since we render BOTH WAYS (depending on if it's the main surface, or another surface) - we would then need to have TWO of each shader & technique, so that one would be used for rendering to the UrhoSurface (BGRA) while the other shader/technique would be used for exporting to Skia Canvas (RBGA format).

What I'd really rather do, if possible, is configure color channel order for the Urho Surface, so that it matches that of SkiaSharp.

Is there a way to toggle the Channel Order for an UrhoSurface?

(I already tried to swap the channel order for Skia bitmaps, but without any success.   When I set it to BGRA, it just locks up for some reason.)

-------------------------

Modanung | 2020-09-17 08:43:36 UTC | #5

[quote="najak3d, post:4, topic:991"]
UrhoSurface
[/quote]

What's an UrhoSurface? [spoiler]...can you eat that? :diving_mask: [/spoiler]

SkiaSharp just sounds like [Evil Shark](http://www.mikseri.net/artists/urho/evil-shark/362081/) to me. I'd get out of those waters if I were you.

:scroll:
[details=""]
> Emerge from the other side
With King still alive
This legendary object
Preserved for all time
[/details]

-------------------------

najak3d | 2020-09-17 16:55:56 UTC | #6

Ah, I see, UrhoSurface is a construct added by UrhoSharp.   It's the wrapper that starts the Urho.Application and hooks it up to a GUI control surface.  For WPF, it's a System.Windows.Forms.Panel.  We pass the Handle of this control to Urho, and it renders to that control surface.   I was wondering if there is some channel configuration that we can assign to the Urho3D engine that tells it to swap color channels on final render.

If not, I suppose another work around is post-processing of the entire Texture2D, which swaps the color with a shader.  That would be lightning fast, and I would assume is the best way to go.

From the UrhoSamples, I would assume this is best achieved by adding in a final step to the RenderPath of the Viewport that renders to this Texture.   (like Bloom or FXAA shaders are used)

Does this sound like the right solution for swapping color channels for a Viewport that Renders to Texture?

And SkiaSharp wraps Skia - and is now the standard Graphics Library to use with .NET/Xamarin, which supports all major platforms, using the same code.  With Xamarin, we "write once" then "run anywhere" without extra any extra code.

-------------------------

najak3d | 2020-09-17 17:09:58 UTC | #7

I think I answered my own question -- it looks to me like PostProcess effect method is the best way to handle this, and just attach it to the RenderPath of the Viewport that is rendering to Texture.   It will be very similar to the existing GreyScale.xml post processing effect.

-------------------------

Modanung | 2020-09-17 17:10:49 UTC | #8

It's like you're speaking a foreign language, I love it.

-------------------------

