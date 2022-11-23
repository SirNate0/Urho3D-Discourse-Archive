rasteron | 2017-01-02 01:06:53 UTC | #1

[img]http://i.imgur.com/Z6JOYP5.png[/img]

[gist]https://gist.github.com/dd9762e1a429da9b6a88[/gist]
[gist]https://gist.github.com/aceec4f3e9525269ddbe[/gist]

-------------------------

codingmonkey | 2017-01-02 01:06:53 UTC | #2

cool fx ) did you planned create distortion post-fx based on normal map shifting? I guessing it named exactly that or maybe i mistaken.
however I mean this blades effect
[video]http://www.youtube.com/watch?v=BYEebRNb0ag[/video]

-------------------------

rasteron | 2017-01-02 01:06:53 UTC | #3

Thanks codingmonkey :slight_smile: I'm still into postprocess as I'm still learning how to do object or material effects next.

By Blades Effect I think you're talking about Ribbon Trails. The effect on that game looks really smooth and cool! I guess we need to start searching for a compatible shader solution.  :wink:

-------------------------

rasteron | 2017-01-02 01:06:53 UTC | #4

Something like this?

[ogre3d.org/forums/viewtopic. ... 7&start=25](http://www.ogre3d.org/forums/viewtopic.php?f=2&t=34737&start=25)

[ogre3d.org/forums/viewtopic.php?f=4&t=68391](http://www.ogre3d.org/forums/viewtopic.php?f=4&t=68391)

[img]http://img546.imageshack.us/img546/2149/screenshot20av.jpg[/img]

-------------------------

codingmonkey | 2017-01-02 01:06:53 UTC | #5

>Something like this?
Yes, but this tail only must be absolutely transparent I guess.
I think that it also must have a very huge specular in material to shine like water.

-------------------------

TikariSakari | 2017-01-02 01:06:54 UTC | #6

[quote="rasteron"]Something like this?

[ogre3d.org/forums/viewtopic. ... 7&start=25](http://www.ogre3d.org/forums/viewtopic.php?f=2&t=34737&start=25)

[ogre3d.org/forums/viewtopic.php?f=4&t=68391](http://www.ogre3d.org/forums/viewtopic.php?f=4&t=68391)

[img]http://img546.imageshack.us/img546/2149/screenshot20av.jpg[/img][/quote]

I was just today wondering about something like this, how to achieve. I was thinking if adding particle emitter would do the trick, but I suppose the particles live in the container of the emitter, and thus follow the emitter instead of having their own life. I was mostly thinking about casting / attack animations and skill/spell effects.

It is nice to know that there exists some sort of solution, that I can try to figure out with my limited understanding/knowledge, when I have finished most of the basics for my game and can focus on polishing things up.

I do have to say that I do like the shaders you've shared and they provide really good examples on how to write shaders for Urho.

-------------------------

codingmonkey | 2017-01-02 01:06:54 UTC | #7

i also remember that there are exist some post-effect and it probably will be useful for pixel painted games or something like this - the effect name is [en.wikipedia.org/wiki/Color_quantization](https://en.wikipedia.org/wiki/Color_quantization)

quantize example effect under first spoiler [gamedev.ru/projects/forum/?i ... age=8#m109](http://www.gamedev.ru/projects/forum/?id=198632&page=8#m109)

source, I guess this : [github.com/ddionisio/MateImageE ... ize.shader](https://github.com/ddionisio/MateImageEffects/blob/master/Shaders/Quantize.shader)

-------------------------

rasteron | 2017-01-02 01:06:54 UTC | #8

[quote="TikariSakari"]
I was just today wondering about something like this, how to achieve. I was thinking if adding particle emitter would do the trick, but I suppose the particles live in the container of the emitter, and thus follow the emitter instead of having their own life. I was mostly thinking about casting / attack animations and skill/spell effects.

It is nice to know that there exists some sort of solution, that I can try to figure out with my limited understanding/knowledge, when I have finished most of the basics for my game and can focus on polishing things up.

I do have to say that I do like the shaders you've shared and they provide really good examples on how to write shaders for Urho.[/quote]

Hey thanks and sure thing. I'm glad to "demystified" some Urho3D shaders for you and for other starters who would want to deal with writing their own or porting existing shaders. I'm not up to par yet, but I'm getting there.. one step at a time. :slight_smile:

-------------------------

rasteron | 2017-01-02 01:06:54 UTC | #9

[quote="codingmonkey"]i also remember that there are exist some post-effect and it probably will be useful for pixel painted games or some thing like this - the effect name is [en.wikipedia.org/wiki/Color_quantization](https://en.wikipedia.org/wiki/Color_quantization)

quantize example effect under first spoiler [gamedev.ru/projects/forum/?i ... age=8#m109](http://www.gamedev.ru/projects/forum/?id=198632&page=8#m109)

source, I guess this : [github.com/ddionisio/MateImageE ... ize.shader](https://github.com/ddionisio/MateImageEffects/blob/master/Shaders/Quantize.shader)[/quote]

hmmm.. I did have some sort of that quantize or toon snippet that I saved up some time ago. I can't remember where I pulled that from but I could try and find it again and perhaps produce a decent toon shader and add it to the mix.  :smiley:  :bulb:

-------------------------

