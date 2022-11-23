najak3d | 2020-11-11 08:20:40 UTC | #1

We've already done this via a kludge of putting a plane in front of the camera and projecting the whole scene onto this plane... and then exporting the Texture pixels.  This worked but was a hack.

What we really want to do is to just copy out the Screen Buffer itself (what you see on the Render Surface, verbatim).  Can anyone please point us in the direction of code that will accomplish this?

In short, we want the effect of a full-screen snapshot image, without the kludge I mentioned above.

-------------------------

Modanung | 2020-11-11 08:30:10 UTC | #2

[quote="najak3d, post:1, topic:6518"]
This worked but was a hack.
[/quote]

[You are a pizza box](https://www.youtube-nocookie.com/embed/hQY20gBlqqo?autoplay=true).   *[* ἆω]

[quote="najak3d, post:1, topic:6518"]
Can anyone please point us in the direction of code that will accomplish this?
[/quote]

Forward, _evar_ forward! 𐍉

-------------------------

1vanK | 2020-11-11 08:59:40 UTC | #3

Need a postprocess or screenshot?

-------------------------

JTippetts1 | 2020-11-11 18:06:52 UTC | #4

[Graphics::TakeScreenshot](https://github.com/urho3d/Urho3D/blob/f909775ca7d61e6291342b33921a22d837ac6b18/Source/Urho3D/Graphics/Graphics.h#L197)?

-------------------------

najak3d | 2020-11-11 18:07:24 UTC | #5

JTippetts1 - Thanks!  That was an easy solution.

-------------------------

Modanung | 2020-11-11 20:14:45 UTC | #6

Well done, @JTippetts1! :fish_cake:![24x23](https://upload.wikimedia.org/wikipedia/commons/1/12/Seme_denari_carte_spagnole.svg)

-------------------------

