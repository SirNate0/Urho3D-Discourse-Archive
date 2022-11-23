TrevorCash | 2019-04-23 15:24:04 UTC | #1

Has anyone implemented a simple way of showing text with the DebugRenderer?  Maybe drawing the text using lines?  

I searched the forums but couldn't find anything.

-------------------------

guk_alex | 2019-04-23 15:32:22 UTC | #2

Why DebugRenderer, is it a requirement for your case? You can add a temporary UI window with text object and update it every frame.

-------------------------

TrevorCash | 2019-04-23 15:36:05 UTC | #3

It would make things alot easier if text could be drawn on a frame by frame basis.  Using UI Text or 3D Text works, but you have to manage it's lifetime.  Would be nice if there was a DebugRenderer::AddText(...)

-------------------------

Leith | 2019-04-24 05:01:52 UTC | #4

Yes it would be nice, but it would also be convoluted: the existing DebugRenderer is relatively low-level and does not know about high-level UI stuff. I'm not saying it can't be done, but it would represent a fairly large hack in the topdown design paradigm.
A better alternative might be to create a new component deriving from DebugRenderer, which adds the desired functionality, and use that component in your scene instead of DebugRenderer. I've certainly done that kind of thing in the past.
[EDIT]
Gah the Render method is not virtual - you can still inject a Proxy object if you carefully duplicate the existing class structure, and add anything new to the end of the class - no typechecking will be done on your object type, but your proxy class has to have the same layout as the Urho component.

-------------------------

weitjong | 2019-04-24 05:08:04 UTC | #5

DebugHud not good enough for you?

-------------------------

Leith | 2019-04-24 05:26:55 UTC | #6

Not sure about the exact use-case, so can't conjecture :P

-------------------------

TrevorCash | 2019-04-24 22:39:00 UTC | #7

Ah! I will try using that - just skipped my mind.  Thanks!

-------------------------

WangKai | 2019-04-25 00:22:01 UTC | #8

I think we can introduce very simple text rendering into the DebugRenderer. Only ascii characters need to be supported and it will be very fast to render them from an atlas texture.

-------------------------

Leith | 2019-04-26 13:20:09 UTC | #10

DebugHud is not programmable - though it acts as a nice example for a place to start, it is not flexible enough for general purpose debugging. DebugHud is code-driven, and has no way to add new stuff at runtime.

-------------------------

guk_alex | 2019-04-26 13:47:19 UTC | #11

Generally DebugHud is just a wrapper for a Text in the UI that updates it in the PostUpdate.
And I see no issues creating the custom component that have some sort of ->SetOneFrameText() that will update the Text of it with its inner text lines queue collected during the frame time. But clearly it depends on required use-case.

-------------------------

