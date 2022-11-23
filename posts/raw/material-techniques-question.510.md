rogerdv | 2017-01-02 01:00:58 UTC | #1

I was looking at material files and editor yesterday at home, where I still dont have a decent video card. I was wondering if I can have 2 techniques in the same material, like DiffNormalAO and DiffNormal as fallback, and have the engine use the one that the video hardware supports. Is that the current behaviour of the engine? AO techniques are for deferred rendering?

-------------------------

cadaver | 2017-01-02 01:00:58 UTC | #2

If you're targeting also ancient SM2 cards you can use the "sm3" define in technique XML's (check the documentation) to cause SM3-requiring techniques to be skipped. Note that this is Direct3D only, for OpenGL a higher hardware level that corresponds to SM3 is required in any case. Probably another define that could be added is "gles" or similar for skipping expensive or unsupported techniques on mobile hardware.

(as a sidenote, I believe at some point the SM2 support path should just simply be removed, as it's getting very hard to test due to limited availability of real SM2 hardware :wink: )

AO techniques are usable both in forward and deferred rendering. Note that they're not about dynamic AO, but simply are intended to supply a precalculated texture which darkens the ambient level.

-------------------------

rogerdv | 2017-01-02 01:00:59 UTC | #3

Then, whats the way to enable deferred rendering?

-------------------------

