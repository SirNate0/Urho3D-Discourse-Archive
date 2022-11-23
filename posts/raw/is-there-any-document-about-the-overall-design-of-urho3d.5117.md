carlcc | 2019-05-30 06:17:34 UTC | #1

Hi,

I am new to Urho3D, and I have tried some samples, really nice!

I'm really interested in rendering, and want to know how the engine works, so I tried to study the engine, but it is a little complex for me. And unfortunately,  the only document I found about the engine [overall structure](https://urho3d.github.io/documentation/1.7/_structure.html) is kind of too simple.

May I know if there are more detailed document about the overall design of Urho3D, such as the design philosophy, how the engine works, relationship between classes, how each subsystems and data interact with each others and etc...

Regards.
carlcc.

-------------------------

Modanung | 2019-04-23 20:27:36 UTC | #3

Hi there and welcome! :confetti_ball: :slightly_smiling_face:

How does browsing the source code work for you?

-------------------------

jmiller | 2019-04-23 23:26:35 UTC | #4

Hi, and welcome!  :confetti_ball:

  https://urho3d.github.io/documentation/HEAD/index.html (with some topics in 'Related pages' section) is a wide view.
'Further reference': Scene model, Events, and preceding sections should be informative... Perhaps some things can still be clarified?

[quote="Modanung, post:3, topic:5117"]
How does browsing the source code work for you?
[/quote]
The [source](https://github.com/urho3d/Urho3D/tree/master/Source) and samples are very nice. :)

-------------------------

Leith | 2019-04-24 04:45:22 UTC | #5

I found the single most useful things to understand with respect to Urho3D are the Frame Update https://urho3d.github.io/documentation/1.7/_main_loop.html and the Event system https://urho3d.github.io/documentation/1.5/_events.html

While the documentation is incredibly useful, it is by no means the only useful source of information, and in some respects could be improved and/or clarified.

-------------------------

carlcc | 2019-04-24 14:34:52 UTC | #6

Thank you all!

I found these materials before, maybe I should read these materials more carefully!:relaxed:

-------------------------

Leith | 2019-04-29 09:32:29 UTC | #7

I would be happy to attempt to explain anything you don't understand - I don't pretend to understand Urho entirely, I am fairly new here, but I have a knack for rapidly smashing my way to a common understanding, and a gift for teaching, and explaining complex things in simple terms. In short, I am a born reverse engineer, and a gifted teacher.
You are welcome to ask me for help, or simply my opinion on some topic. Hopefully I can be of some use. I'm not sure how qualified everyone here is, but I have already indicated that I hold a bachelor of games and virtual worlds. I may be of some use.

-------------------------

