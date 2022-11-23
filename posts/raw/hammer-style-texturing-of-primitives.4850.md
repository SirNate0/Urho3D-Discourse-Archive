smellymumbler | 2019-01-22 17:05:37 UTC | #1

I'm working on a very basic level editor which uses rectangles as the base for everything. I resize them to create walls, floors, etc. One thing I'm having a hard time with are the UVs. How can I do something like the Hammer editor, with per-face texturing?

https://www.youtube.com/watch?v=QgwiEmh9s78

-------------------------

Enhex | 2019-01-22 20:51:47 UTC | #2

I created a Hammer-like editor for my game. IIRC you need to have basis vectors and transformation for your texture which is "projected" on the face, and you use them to modify the texture coordinates.

Personal tip: keep in mind that making a level editor could be as much work as making the game itself, so personally I'd look for existing solutions first.

-------------------------

