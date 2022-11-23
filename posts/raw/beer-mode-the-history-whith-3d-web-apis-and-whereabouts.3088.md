slapin | 2017-05-01 11:17:13 UTC | #1

Well, I was drinking and suddenly I thought of I really don't know anything about how come
web and 3D met. I remember there was Unity plugin, something called WebGL,
and other thing called VRML. There were more in this. These all things were packaged quite well,
mature tech, lots of adverticement, the thing to win a world. But I never ever visited a site which
featured this technologies and/ or could actually use any. I tried to check if anything really works,
exported some ragdoll stuff from Unity to web and it works (actually got my PC to almost unbearable state, but it still works), I wonder what technology is used there (only development unity web player export works under Linux,
release version can't produce output, probably release version was smoother). but anyway, it was first time i seen something 3Dish in my browser (not ounting youtube, these are recorded videos). So I wonder what is going next from here? Or what I miss? What happened to all that modern technology, and what actually wins? Where is future?
Will 3D stay in web, or we'll be happy watching out .htmls with pics forever?

-------------------------

Modanung | 2017-05-02 14:12:20 UTC | #2

Both Urho3D and Unity use WebGL for the 3D web part. Urho manages to do this without plugins through Emscripten.
Stuff you missed (apparently):

- [Blend4Web](https://www.blend4web.com/)
- [Bananabread](http://kripken.github.io/misc-js-benchmarks/banana/game.html)
- [HeNe Webgl tutorials](http://learningwebgl.com/blog/?page_id=1217)

-------------------------

Modanung | 2017-05-02 14:15:35 UTC | #3

See also:
http://caniuse.com/webgl

-------------------------

slapin | 2017-05-02 14:19:03 UTC | #4

But what happened to the rest like VRML?

Also Unity no longer use plugins either...

-------------------------

KonstantTom | 2017-05-02 14:47:54 UTC | #5

Unity now uses Emscripten and WebGL, same as Urho3D.

-------------------------

Modanung | 2017-05-02 20:00:13 UTC | #6

[quote="slapin, post:4, topic:3088"]
Also Unity no longer use plugins either...
[/quote]
[quote="KonstantTom, post:5, topic:3088, full:true"]
Unity now uses Emscripten and WebGL, same as Urho3D.
[/quote]
Apparently I missed something too. :slight_smile:

-------------------------

