GoogleBot42 | 2017-01-02 01:04:56 UTC | #1

I get this strange bug with the water shaders in the water demo.  An image of the cube appears above the real cube...

This is emscripten:
[img]http://i.imgur.com/YorC73E.png[/img]

This is native:
[img]http://i.imgur.com/uqLjtyR.png[/img]

-------------------------

cadaver | 2017-01-02 01:04:57 UTC | #2

This is the same as on mobile GLES2. It doesn't implement clipping planes, so the objects under water will render also incorrectly in the reflection.

I'm not sure there's a good solution for this. One could clip manually in the pixel shader, by discarding the fragments, but this would be performance hell on mobiles at least.

-------------------------

GoogleBot42 | 2017-01-02 01:04:57 UTC | #3

[quote="cadaver"]This is the same as on mobile GLES2. It doesn't implement clipping planes, so the objects under water will render also incorrectly in the reflection.

I'm not sure there's a good solution for this. One could clip manually in the pixel shader, by discarding the fragments, but this would be performance hell on mobiles at least.[/quote]

:frowning:  There has to be a way to do it though that isn't bad for performance... I wonder how Unity and other engines do it.  But this is a known issue and it is just a minor one (note to self: avoid using water :stuck_out_tongue:).

EDIT: Maybe this will help show a better way to do it... [url]https://github.com/powervr-graphics/Native_SDK/tree/3.4/Examples/Advanced/Water[/url] [url]http://stackoverflow.com/questions/7408855/clipping-planes-in-opengl-es-2-0[/url]

-------------------------

friesencr | 2017-01-02 01:04:57 UTC | #4

If i had any performance issues on mobile, fancy water w/ reflections would be the first to die :slight_smile:

-------------------------

GoogleBot42 | 2017-01-02 01:04:57 UTC | #5

[quote="friesencr"]If i had any performance issues on mobile, fancy water w/ reflections would be the first to die :slight_smile:[/quote]
Lol  :laughing: Good point!  Agree that would probably be best.  :slight_smile:   Do you think the reflections could be disabled when using opengl es?

-------------------------

friesencr | 2017-01-02 01:04:57 UTC | #6

In the case of the water example the code is generating the material settings and not loading from a scene file.  Since the code has control I would check at runtime which material to use on the water plane and not generate the realtime reflection image.

-------------------------

cadaver | 2017-01-02 01:05:00 UTC | #7

I tested the Terathon oblique projection technique when initially implementing the water reflection; it's cool but I never managed to get an arbitrary clipping plane to work (let's say you wanted to clip either above a certain Y plane, or below it)

-------------------------

