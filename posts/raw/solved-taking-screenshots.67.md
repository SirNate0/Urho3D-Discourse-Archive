Mike | 2017-01-02 00:57:44 UTC | #1

I'd like to implement the take screenshots feature.
From previous discussion forum I've found that there are TakeScreenShot and SavePNG functions, but I didn't find the way to use them.

-------------------------

Azalrion | 2017-01-02 00:57:44 UTC | #2

Its pretty simple, the docs are useful for working things out for functions like these.

[code]Image screenshot(context_);
GetSubsystem<Graphics>()->TakeScreenShot(screenshot);
screenshot->SavePNG(path/to/dest/file.png);[/code]

[url=http://urho3d.github.io/documentation/a00138.html#aba8bc69f7cae9251dbf3dc99d771ed30]Graphics::TakeScreenShot(Image&)[/url]
[url=http://urho3d.github.io/documentation/a00149.html#aec598c56642beffb3cc345878e1af32f]Image::SavePNG(String&)[/url]

-------------------------

Mike | 2017-01-02 00:57:44 UTC | #3

Thanks for reply, I'm still missing something, I can't get it to work in script.

EDIT: many thanks to JTippetts for exposing Image constructor to lua  :stuck_out_tongue:

-------------------------

JTippetts | 2017-01-02 00:57:44 UTC | #4

It's something I've been meaning to do for awhile, but this thread reminded me. :smiley: I use a custom executable and until this change, I have been taking screenshots inside the .exe in response to a custom event. Having Image exposed to Lua makes it so much easier.

-------------------------

Mike | 2017-01-02 00:57:44 UTC | #5

Everything works fine for script (angel and lua).

But for C++, I get this error for screenshot->SavePNG(...):
error: base operand of '->' has non-pointer type 'Urho3D::Image'

-------------------------

cadaver | 2017-01-02 00:57:45 UTC | #6

When the image is a locally constructed object instead of pointer to image, you need to use . instead of ->

-------------------------

Xardas | 2017-01-02 00:57:45 UTC | #7

When I try to resize the image before saving it, the image file it produces is screwed up (grey image).

screenshot.SetSize(160, 90, screenshot.GetComponents());

Am I missing something?

-------------------------

cadaver | 2017-01-02 00:57:45 UTC | #8

SetSize() destroys the existing data. There is currently no function to arbitrarily resample an image to a new size.

-------------------------

Azalrion | 2017-01-02 00:57:45 UTC | #9

If anyone would like the functionality we have a bilinear interpolating and nearest-neighbour scaling function we added as a utility but could fold into the image class.

-------------------------

cadaver | 2017-01-02 00:57:45 UTC | #10

I'm sure that would be appreciated, and should fit well into the Image class.

-------------------------

Xardas | 2017-01-02 00:57:45 UTC | #11

Yes, that would be great!

-------------------------

