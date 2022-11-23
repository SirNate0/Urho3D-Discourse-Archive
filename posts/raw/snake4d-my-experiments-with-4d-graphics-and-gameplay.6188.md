Eugene | 2021-06-20 17:38:41 UTC | #1

This is classic snake game in four spatial dimensions.

This is not really a game meant to be played by a person. Unless you have basic understanding of 4D geometry, you probably won't understand much in this "game" as well.

I mostly wanted to experiment with true 4D graphics and animation, without making 3D slices and other 4D-to-3D hacks.

If you want to see it in action, check this out: [<10MB web demo](https://eugeneko.itch.io/snake4d)
The game will play itself by default, so you don't have to do anything.

I would have recorded a video, but video compression completely ruins wireframe graphics.
I have a screenshot just in case, but static pictures doesn't really show much:
[details="Screenshot"]
![image|690x335](upload://2nX1h9WYAY84uuCT6AflY8252xB.png)
[/details]
 
Finally, there's a document that explains underlying math and logic, to certain degree:
[Snake4D/README.md](https://github.com/eugeneko/Snake4D/blob/master/README.md)

This is technically made with Urho, so I feel like sharing it here.

-------------------------

SirNate0 | 2020-06-01 15:01:16 UTC | #2

That's really cool!

Unrelated to the 4 dimensional part of it - what did you do for the wall when it was between the camera and the snake?

-------------------------

Eugene | 2020-06-01 15:19:22 UTC | #3

[quote="SirNate0, post:2, topic:6188"]
what did you do for the wall when it was between the camera and the snake?
[/quote]

I hide "backward" wall unconditionally.
It doesn't really contribute and only makes visual noise (and this "game" already has a lot of visual noise).

I also mostly hide "top" wall and draw only a few transparent quads right above the snake.

I tried to use 4D walls in previous versions, but there are 24 walls in hypercube. Too much visual noise, not helpful for navigation at all. So I decided to use simple 3D walls of the current 3D slice.

-------------------------

throwawayerino | 2020-06-01 15:41:34 UTC | #4

I only play games with at least a 5D UI.
On the other hand, this is really mind-boggling. You should share this with more people!

-------------------------

elix22 | 2020-06-02 07:23:38 UTC | #5

Cool demo 
Under which license is the source code ?

-------------------------

Eugene | 2020-06-02 09:44:32 UTC | #6

[quote="elix22, post:5, topic:6188"]
Under which license is the source code ?
[/quote]
MIT, I guess. Updated repo to clarify it.

-------------------------

Eugene | 2021-06-19 12:59:13 UTC | #7

For last month I have been lazily polishing this "game" and now I have finally posted it on itch.
I added in-game pause and some camera movement (when paused).

https://eugeneko.itch.io/snake4d

I hope it's not broken too much...

-------------------------

