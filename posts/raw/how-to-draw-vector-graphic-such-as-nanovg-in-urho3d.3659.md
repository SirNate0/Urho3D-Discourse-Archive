Taymindis | 2017-10-15 03:26:07 UTC | #1

I am integrating nanovg with urho3d, but it seemed quite hard for me to compile it successfully. I wonder is there any built in drawing api in urho3d? for gradient, rectangular, polygon and etc?

-------------------------

Mike | 2017-10-15 07:05:03 UTC | #2

https://github.com/scorvi/Urho3DSamples

-------------------------

Taymindis | 2017-10-15 07:12:06 UTC | #3

@Mike

I have tried this example 2 days ago,  it produced erros below when rendering 
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill
Error 00000502 after convex fill


I am not sure whether it is still workable due to not maintaining anymore

-------------------------

johnnycable | 2017-10-15 09:42:24 UTC | #4

I confirm the errors. Last time I tried it, only the nanosvg (rendering on texture) part seems to be working...
Ifaik there's no drawing api except debug one. UrhoSharp integrated [skia library](https://skia.org/) for that.

-------------------------

Taymindis | 2017-10-15 11:57:55 UTC | #5

[quote="johnnycable, post:4, topic:3659"]
UrhoSharp integrated skia library for that.
[/quote]

I am sorry that I am only implementing by C/C++ only. I've tried many engine found that Urho3D is more suitable for me to go for 2D and 3D implementing in future. But I am wondering has anyone integrated Skia C Api  with urho3d.

-------------------------

Taymindis | 2017-10-19 03:19:39 UTC | #6

I found the good Source https://github.com/rokups/Urho3D-nuklear-ui, 

which integrate urho3d with nuclear :)

-------------------------

johnnycable | 2017-10-19 08:42:48 UTC | #7

I know that. But that's an UI not a painter, afaik...
You could use Blender GP or Curves, then export as mesh, or you could integrate st like [Spline Library](https://github.com/ejmahler/SplineLibrary) or the more scientifical [Splinter](https://github.com/bgrimstad/splinter) if you need st procedural...

-------------------------

