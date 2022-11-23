Mike | 2017-01-02 00:57:55 UTC | #1

I'd like to build a GUI (window, text, images, sliders...) that auto-resize according to screen size.
What are the settings/functions to use to achieve this?

-------------------------

weitjong | 2017-01-02 00:57:56 UTC | #2

The UI subsystem is designed to do the calculation and positioning in a pixel-perfect manner. It does not support auto-resizing according screen resolution/size (yet). This has been briefly discussed in [github.com/urho3d/Urho3D/issues/42](https://github.com/urho3d/Urho3D/issues/42).

-------------------------

Mike | 2017-01-02 00:57:56 UTC | #3

OK, thanks, I thought I was missing something.

-------------------------

TiZ | 2017-01-02 00:58:19 UTC | #4

Hi. I apologize if it's bad tact to bump a thread that dropped to the second page, but I am interested in finding some way, any way, to pull this off. I am potentially interested in using Urho3D, but if this kind of thing isn't possible in any way, it's unfortunately going to be a deal breaker for me.

Issue #42 seemed to imply that UI elements can be scaled; can elements actually be *scaled*, or can you just change their size when the resolution changes? Failing that, would it be possible to render the UI to a texture and just draw that texture scaled as necessary? I know that 2D support in Urho3D was very recent; does that change anything for this issue?

-------------------------

friesencr | 2017-01-02 00:58:19 UTC | #5

Its pretty easy to add a resize event listener and only need to set the top level parent elements dimensions and let the auto layout take care of the rest.  Its a bit manual but I think its pretty manageable.  If you wanted to do it more automagically you could use a var on the UIElement,  something like ["AUTO_WIDTH_PERCENT"] and detect if that var exists on the top level elements in an iterator and set it based on the graphics.width;

-------------------------

TiZ | 2017-01-02 00:58:19 UTC | #6

I can "set the size", sure, but that's not the same as *scaling*. For example, between 640x480 and 1920x1080, for example, a list-view would not appear to be the same size, but would instead show more elements. Changing the font size with each resolution change goes a long way toward fixing this, sure. But that doesn't fix all the problems. Like... for the default UI theme, the borders would look huge at 480p, and tiny at 1080p. I know it sounds finicky, but I'd like all the details to be right, which means either the ability to scale the graphics of these UI elements or the ability to render the UI to a texture. I'd still have to change the texture whenever there is an aspect ratio change, but I'm okay with that. It's not about convenience, it's about visual consistency.

-------------------------

weitjong | 2017-01-02 00:58:19 UTC | #7

The default UI theme is just that, a default. I suppose you can create a different DefaultStyle.xml file and UI.png file that match the resolution you want to target. You can use different style files in one application. You can even apply different style files at different UIElement in the UI root hierarchy, if it makes sense for your app. My point is, you are not limited to just ship with one style file. Having said that, I agree that this may not address all the issues.

-------------------------

aster2013 | 2017-01-02 00:58:21 UTC | #8

In CEGUI, It use offset and scale for UI Element's size and position. The real value of size and position can calculate in following formula:

value = offset + parent.value * factor.

I think it is good for auto layout.

-------------------------

cadaver | 2017-01-02 00:58:21 UTC | #9

To work properly, I believe it needs changing UIElement positions and sizes to floats. A flag to ensure the existing pixel perfect behavior (only integer sizes / positions) would be required. Finally it'd need a positioning mode enum for the UIElement, either the existing (absolute) or the parent-relative.

I don't think I will begin such rework, but anyone is free to contribute. Just as long as the existing functionality isn't broken. In fact this would simplify the "Sprite" UIElement's code, as that is using float position + size already as a sort of an exception.

-------------------------

TiZ | 2017-01-02 00:58:27 UTC | #10

Okay, so you can't render the UI to a texture, and there's no in-built support for scalable UIs. So the easy ways are out. How about resizing the textures programmatically? Let's say I design an interface for 1280x720, and use a bunch of BorderImages with 4px borders. at 800x600, they'd need to be scaled such that the borders are 3px, 2px at 640x480, and then upward, like, at 1920x1080, the borders would be 6px. So resize the texture that comprises the border image such that its borders end up the desired size, and programmatically adjust the dimensions. Is that possible?

-------------------------

cadaver | 2017-01-02 00:58:27 UTC | #11

It's probably easier if you hack BorderImage so that the screen pixel size of the borders, and the UV coordinates they use can be decoupled (for example border is 4 pixels on screen but uses 2 pixels of texture, or vice versa.) This would be a good feature even before any other auto-resizing is implemented, so if you'd get that done and it works nicely it would be a valuable pull request.

-------------------------

TiZ | 2017-01-02 00:58:28 UTC | #12

I agree, that would probably be the ideal way to do it, theoretically speaking. I can't program in C++ worth a damn though, unfortunately... The ability to use AngelScript and/or Lua is part of what makes this engine appealing to me. So as much as I'd like to implement this myself, I can't. :/

-------------------------

cadaver | 2017-01-02 00:58:28 UTC | #13

We can put it on the issue tracker, but of course no promises how long it will take to do that :smiling_imp:

-------------------------

cadaver | 2017-01-02 00:58:29 UTC | #14

The decoupling should be done now in the head revision.

-------------------------

