Bananaft | 2017-01-02 01:05:42 UTC | #1

According to documentation:
[urho3d.github.io/documentation/1 ... paths.html](http://urho3d.github.io/documentation/1.4/_render_paths.html)

using HWDepth is a bit faster, but it won't work on some GPUs. What kind of GPUs is that? I'm not sure if I'm googling it right, but it seems like pre-2006 ones.

Should I even bother about supporting them?

-------------------------

thebluefish | 2017-01-02 01:05:42 UTC | #2

[quote]INTZ is for recent (DX10+) hardware. With recent drivers, all three major IHVs expose this. According to ATI [1], it also allows using stencil buffer while rendering. Also allows reading from depth texture while it?s still being used for depth testing (but not depth writing). Looks like this applies to NV & Intel parts as well.[/quote]
[url=http://aras-p.info/texts/D3D9GPUHacks.html#depth]source[/url]

So it looks like generally hardware from before 2010 might not have it. Also I know some versions of Intel HD graphics don't support it. So at this point it's worth keeping support, or you'll get people like me who still can't run those particular Render paths.

-------------------------

