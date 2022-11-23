smellymumbler | 2018-01-05 15:52:24 UTC | #1

I was looking for a Hello World sample that integrates an Urho instance with Qt 5. I've seen that some people use ExternalWindow, but then how do you control the engine without Urho's Application class? Is it possible to draw Qt widgets on top of Urho's rendering screen?

-------------------------

Eugene | 2018-01-05 16:33:12 UTC | #2

[quote="smellymumbler, post:1, topic:3916"]
but then how do you control the engine without Urho’s Application class?
[/quote]

I used `Application` with Qt, so..

[quote="smellymumbler, post:1, topic:3916"]
Is it possible to draw Qt widgets on top of Urho’s rendering screen?
[/quote]
It is. Like any other window on top of another window. Don't expect it to be very nice tho.

-------------------------

Sinoid | 2018-01-06 03:38:00 UTC | #3

Aster's old particle editor is concise: https://github.com/aster2013/ParticleEditor2D I used it ages ago to figure out how to make it all work.

It's old though so expect to do some fixing for an older version of Urho3D.

-------------------------

