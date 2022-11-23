Lumak | 2017-01-02 01:12:14 UTC | #1

I wasn't familiar with this topic until I came across this blog post [url]http://aras-p.info/blog/2016/04/08/solving-dx9-half-pixel-offset/[/url].  Apparently, it's a common knowledge for graphics guys.

Couldn't this shader register value work better for us instead of using hardcoded:
    const Vector2 Graphics::pixelUVOffset(0.5f, 0.5f);

Just curious.

Edit: Let me clarify. I was aware there was a difference in the offset when using DX to OPENGL but thought the problem was in Urho3D. I had no idea it was a problem in DX9.

-------------------------

cadaver | 2017-01-02 01:12:15 UTC | #2

That value is not usable directly in a shader, as it needs to be divided by the texture's dimensions. Urho rather takes the approach that it's inserted into "derived" uniform values where necessary (or adjusting the actual UV coords or positions, like the UI subsystem does), and shaders don't pay an unnecessary performance price just for pixel offset adjustments.

If you want to check in a HLSL shader whether you're on D3D9, you can use the preprocessor check #ifndef D3D11

-------------------------

Lumak | 2017-01-02 01:12:15 UTC | #3

It makes sense about the performance hit when you only need the offset for UI.

Thanks for the feedback.

-------------------------

cadaver | 2017-01-02 01:12:16 UTC | #4

I think if we had the pixel offset in use in more places Aras' solution would certainly be more appealing. The performance difference is probably quite minimal. However having to ensure the offset adjustment in all shaders could be hard (unless we'd simply refactor to a function like GetClipSpacePos), and modifying the bytecode sounds like a somewhat dangerous hack.

-------------------------

Lumak | 2017-01-02 01:12:19 UTC | #5

I consider myself a novice graphics programmer and doubt I'll try to master it because I like all other aspect of game programming, so I'll leave that to you experts.  I brought up Aras' blog in case no one's seen it, but I think the way it is now works just fine.

-------------------------

