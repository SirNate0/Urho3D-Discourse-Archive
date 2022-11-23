Taymindis | 2017-11-17 08:26:02 UTC | #1

Hi, 

Did anyone has any idea how to create a 9 Patch Sprite or Helper? 

Thanks,

-------------------------

Eugene | 2017-11-17 09:19:43 UTC | #2

UI BorderImage works exactly this way. I hope it won't be a problem to reproduce the logic for 2D graphics.

-------------------------

Taymindis | 2017-11-17 22:45:23 UTC | #3

Hi Eugene,

What is the limitation of BorderImage, can this do exactly same with what sprite2d do?

-------------------------

Eugene | 2017-11-17 22:55:22 UTC | #4

[quote="Taymindis, post:3, topic:3748"]
What is the limitation of BorderImage, can this do exactly same with what sprite2d do?
[/quote]

The limitation is that BorderImage is UI element and not designed to be a part of the scene.
So I don't recommend to use it as is. You will have more problems than benefits.

However, you could check the code (that is pretty simple) and tune Sprite2D to allow it be 9-stretchable (it would be great to get this feature in Urho core).
You could also ask somebody on forums (e.g. me) to implement this feature, but keep in mind that we are all volunteers here. I could investigate a bit this weekend.

-------------------------

Taymindis | 2017-11-17 23:23:36 UTC | #5

Noted with thanks.  :slight_smile:

-------------------------

Eugene | 2017-11-19 12:05:17 UTC | #6

FYI. Just checked code.

It's pretty easy to change `StaticSprite2D::UpdateSourceBatches` so it will make nine quads instead of one.
If you are familiar with C++, you could do it on your own. If you are not, please make an issue on GitHub tracker.
However, there is some design complexity. How to specify inner rectangle for `StaticSprite2D`?
It could be

1. UV rectangle same as _Draw Rectangle_;
2. Relative UV rectangle in fractions of actual _draw rectangle_;
3. Pixel offset from rectangle edge;
4. Something else;
5. Some combination of 1-4.

Any ideas?

-------------------------

Taymindis | 2017-11-20 07:28:23 UTC | #7

Hi Eugene,

Thanks for the suggestion, I’m new to urho3d, it is complicated for me to create my own. ( afraid causing other feature issue but I don’t know )

However, how can I avoid this issue when using normal 
StaticSprite2D?

For instance,
Don’t make square image to be long rect image
and?

-------------------------

Modanung | 2017-11-20 08:55:27 UTC | #8

To keep things simple - but not ideal - you could make an `Object` or `Component` that simply creates and keeps track of nine separate sprites.
From there it may be easier to turn it into a single `Drawable`.

-------------------------

Eugene | 2017-11-20 09:43:40 UTC | #9

[quote="Taymindis, post:7, topic:3748"]
However, how can I avoid this issue when using normal

StaticSprite2D?
[/quote]

The simplest workaround is to use fixed-size sprites.
Then, you could create a component (as @Modanung suggested) for 9-sprite that uses 9 StaticSprite2D-s.
But such feature is better to be in Urho core IMO.

-------------------------

