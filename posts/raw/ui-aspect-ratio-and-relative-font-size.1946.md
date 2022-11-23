Enhex | 2017-01-02 01:11:44 UTC | #1

As far as I understand the way to have scaling UI in Urho is to use the automatic layout modes.
But it isn't possible to have elements that maintain their aspect ratio, for example icon images.

Aspect ratio is relative to the height or width of the parent, this way it can work with the layout modes.
Parent needs to be in free layout mode so the element can be resized? (or maybe implement horizontal/vertical aspect ratio as a new layout modes, if that makes sense?)

Having the font size relative to its parent's height (similar to aspect ratio) is also needed to have scaling UI.

With both aspect ratio and font size relative to parent, I think it would be possible to make fully scaling UI layouts.

-------------------------

Enhex | 2017-01-02 01:11:46 UTC | #2

[img]http://i.imgur.com/AhUSu1N.jpg[/img]
[img]http://i.imgur.com/ZACirMp.jpg[/img]
Square maintains its 1:1 aspect ratio.
Text maintains its relative height to the square.
Bars don't maintain aspect ratio, which is changed because the screen aspect ratio changed.

I implemented it these as "external components" to the UI elements, which resize the element on the parent's E_RESIZE event.
Code available here: [gist.github.com/Enhex/e618ee4d3 ... 80305a7556](https://gist.github.com/Enhex/e618ee4d3c92e26e11a52380305a7556)

It would be nice to see these features added to Urho, so Urho will have a complete solution for scalable UI.

-------------------------

cadaver | 2017-01-02 01:11:46 UTC | #3

I'd recommend reworking that as UIElement's feature and submitting a PR. It doesn't have to be perfect, can be improved by others later.

-------------------------

Enhex | 2017-01-02 01:11:50 UTC | #4

I already had some changes, so I want to use these more before making them part of Urho.

-------------------------

ucupumar | 2017-01-02 01:12:55 UTC | #5

Is there any updates for this?

-------------------------

Enhex | 2017-01-02 01:12:55 UTC | #6

[quote="ucupumar"]Is there any updates for this?[/quote]
I think I have more recent revision if you're interested.
It's still usable as is though very messy.
There are many things on my TODO list before integrating it to Urho, so I won't be able to do it anytime soon.

-------------------------

ucupumar | 2017-01-02 01:13:13 UTC | #7

[quote="Enhex"]I think I have more recent revision if you're interested.
It's still usable as is though very messy.
There are many things on my TODO list before integrating it to Urho, so I won't be able to do it anytime soon.[/quote]
Where's the code? Let me take a look.  :slight_smile:
Anyway, if you don't mind, can you share the TODO list?

-------------------------

Enhex | 2017-01-02 01:13:14 UTC | #8

[quote="ucupumar"][quote="Enhex"]I think I have more recent revision if you're interested.
It's still usable as is though very messy.
There are many things on my TODO list before integrating it to Urho, so I won't be able to do it anytime soon.[/quote]
Where's the code? Let me take a look.  :slight_smile:
Anyway, if you don't mind, can you share the TODO list?[/quote]
Here's my current version:
[gist.github.com/Enhex/357c0fe02 ... 8d677326f4](https://gist.github.com/Enhex/357c0fe028afe086c976688d677326f4)

By TODO list I meant general TODO list of my projects, not a specific TODO list for these UI things, if that's what you understood.
It's ready to be integrated in the sense that it works, and integrating it will make using it much nicer.

-------------------------

ucupumar | 2017-01-02 01:13:15 UTC | #9

I see, thanks for the code! I'll look into it.  :slight_smile:

-------------------------

