shu | 2017-01-02 01:00:50 UTC | #1

Hi!

I'm working on a space game and want to create spaceship trails (like the yellow trails [url=http://icdn.computec.de/videos/img/medium/2014/1/55644.jpg?t=1388658056]here in this Enemy Starfighter example[/url]). For now I use an interval to cache the positions and orientations for the trail in a list and use it like a ringbuffer, so that it doesn't get too long. That part works. 

But now I need to generate some geometry for it. The effect I have in mind is to make it look as if I would extrude a quad with the trail positions. So I guess I have to generate the additional vertices in every frame. What is the best way to do this in Urho? Do I have to generate the geometry and set it in a model on a separate node in every frame? Or can I feed the trail position samples to a shader and generate the geometry on the GPU?

-------------------------

weitjong | 2017-01-02 01:00:51 UTC | #2

Any particular reason why you don't use ParticleEmitter for the trail?

-------------------------

cadaver | 2017-01-02 01:00:51 UTC | #3

There is no particular inbuilt feature in Urho for dynamic trail effects, but creating a programmatic model and updating its vertex buffers every frame should not create undue performance loss. After all, that's what the particle emitters are using.

You can look into the 34_DynamicGeometry sample (C++ only) to see how to create models programmatically.

If you can think of a shader-based solution that wouldn't require to modify geometry buffers every frame, that will possibly yield better performance. The drawables don't have the concept of their own shader data, so in this case you would have to have an unique material on the trail object and update its shader parameters. But note that you only have access to vertex and pixel shaders, not geometry.

-------------------------

shu | 2017-01-02 01:00:51 UTC | #4

[quote="weitjong"]Any particular reason why you don't use ParticleEmitter for the trail?[/quote]

Because I have no experience with graphics programming and effects, I guess. :slight_smile: The trail-effect in the screenshot I posted earlier looks more like some 'solid' geometry to me, so that was my first idea. But when that doesn't work out, I'll try particles!

[quote="cadaver"]There is no particular inbuilt feature in Urho for dynamic trail effects, but creating a programmatic model and updating its vertex buffers every frame should not create undue performance loss.[/quote]

Ok, then I will do that. I just needed reassurance, that this is a good way to do this. 

Thanks! :slight_smile:

-------------------------

thebluefish | 2017-01-02 01:00:52 UTC | #5

There's plenty of implementations of Ribbon Trail effect if you look around. For example, Ogre3D has a fairly straight-forward implementation that you could look into.

-------------------------

Modanung | 2017-01-02 01:06:21 UTC | #6

The [url=https://github.com/MonkeyFirst/urho3d-component-tail-generator]TailGenerator Component[/url] by codingmonkey does exactly that.
Here was a screenshot from [url=https://github.com/LucKeyProductions/heXon]heXon[/url] utilizing it for the trail behind the [b][color=#40CF00]player[/color][/b].

-------------------------

