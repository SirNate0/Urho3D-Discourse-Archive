rbnpontes | 2017-03-14 17:34:55 UTC | #1

Hi guys, i have a big problem. I make a simple Game Editor for my game in Urho3D, i need to process Input keys
but doesn't working
i have embed Urho3D window using **externalWindow**, mouse events will working but Keyboard key not.
I've tried everything like **Input->GetKeyDown()** and by Events **SubscribeToEvent()**

-------------------------

TheSHEEEP | 2017-03-15 07:53:10 UTC | #2

When you embed a window in Qt (or any UI lib for that matter), Qt takes care of all of the input events.
It kind of grabs the focus away from the original window.

I'm surprised that mouse is working, to be honest.

So what you will want to do is handle keyboard events within in Qt (which is pretty easy) and forward them to your game.

-------------------------

Eugene | 2017-03-15 08:34:58 UTC | #3

I had the same problem. Check this:
http://discourse.urho3d.io/t/editor-refactoring-lets-discuss-more-see-45/2407/52?u=eugene

-------------------------

rbnpontes | 2017-03-15 13:55:42 UTC | #4

Thank's for the help,I suspected that this was happening.

-------------------------

rbnpontes | 2017-03-15 14:09:46 UTC | #5

I have tried to Call SDL_Push event, but don't send event

-------------------------

Eugene | 2017-03-15 14:32:46 UTC | #6

Do you mean that this solution doesn't work? I haven't tried it, but wanted to.

-------------------------

rbnpontes | 2017-03-15 14:36:41 UTC | #7

[quote="Eugene, post:6, topic:2899, full:true"]
Do you mean that this solution doesn't work? I haven't tried it, but wanted to.
[/quote]

Yep, this function doesnt working, only working if i use Engine event, like SendEvent(E_KEYDOWN)

-------------------------

Eugene | 2017-03-15 14:59:12 UTC | #8

Then I must check it... I definetly need to make it work somehow.

-------------------------

