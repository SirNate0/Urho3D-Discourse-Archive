Jbonavita | 2019-02-16 05:18:27 UTC | #1

I have a pretty straightforward scene I need created. It's only a single screen with a slot machine and a few buttons and labels. The reels would need to be able to spin.

I was trying to figure out how to do it with a Editor but I can't seem to make any progress with it.

I can do all the coding, I just need the UI created.

Anyone interested?

-------------------------

Leith | 2019-02-16 05:27:56 UTC | #2

You'll need a 2D texture with all the reel symbols on it. The idea is that we are looking at several reels through a "slot" - the solution, for each reel, is to place a 2D textured quad behind that slot, and scroll the value of the V coordinates (texture UVs) on the vertices of the 2D quad, using floating point values, 0 to 1

-------------------------

Jbonavita | 2019-02-16 05:56:34 UTC | #3

I have all the textures. Each reel gets 27 textures.

I was able to build most of the scene in code but I'm unsure of how positioning works.

For example, I have a rectangle that I want to "anchor" to the bottom. It appears that the screen height goes 5 to -5. I haven't been able to get it exactly where I need it since it seems to have an anchor point in the middle.

-------------------------

Leith | 2019-02-16 06:23:42 UTC | #4

What you do, is create your reels as textured quads that "just fill" the size of the viewing "slot" on the machine - now you use UV Scrolling, without changing any Positions, to scroll the texture on each reel. In your case, you want to be scrolling the V coordinates, at the same rate, while leaving the U coordinates alone.

-------------------------

Jbonavita | 2019-02-16 15:46:25 UTC | #5

Thanks @Leith.

Could you explain positioning? How would I get a sprite to anchor to the top or to the bottom? Is there a way to change the anchor point on the sprite from the center to the top left or bottom left/bottom right?

-------------------------

Leith | 2019-02-17 03:17:11 UTC | #6

You need to hack the UV values - I'll try to explain.
Let's imagine for a moment, we had a texture with a single symbol on it, say a cherry.
And let's imagine that your quad is relatively square shaped.
To display the cherry, our UV coordinates for our four vertices would be (0,0) in one corner, and (1,1) in the diagonal opposite corner.

What if our texture had five symbols, so the texture is much taller than it is wide, and we only want to display one of the symbols?
To do that, we need the U coordinates to remain at the 0,1 extremes, but now we want to divide our V value by 5, so for example, to display the top symbol only, we'd use corner coordinates of (0,0) and (1, 0.2)
Given this set of coordinates, to scroll the texture, we want to increase the V (or Y if you prefer) coordinates, together, so lets say we increased V, and have coordinated (0,0.1) and (1, 0,3) - we are now looking at the bottom half of symbol 1, and the top half of symbol 2. continuing to scroll, at coordinates (0,0.2) and (1, 0.4) we see the second symbol.
When V coordinate > 1, we overflow, we subtract 1, so we're really back to 0. This last part might sound confusing, but works in practice.

UV scrolling is generally done using shader parameters, rather than modifying the actual vertex coordinates of the geometry, but I'm not very familiar with Urho3D's shaders and can't offer advice on it - still, either way works and is a valid solution.

-------------------------

Jbonavita | 2019-02-17 03:34:26 UTC | #7

Thanks @Leith. I'm starting to understand.

I wonder if I should use UI elements instead.

I might still be better off having someone else build this.

-------------------------

Leith | 2019-02-17 03:39:17 UTC | #8

My experience with Urho3D UI is very small, but I do use BorderImage ui elements to display textured quads - I don't think that's what you really want, as I don't think it supports scrolling the tex coords. I could be wrong, I would be asking a question in the Support section of the forum, specifically "how do I display a 2D textured quad with scrolling UVs"

-------------------------

Jbonavita | 2019-02-17 03:40:17 UTC | #9

Ok, I'll try that.

Thanks!

-------------------------

Modanung | 2019-02-17 09:00:22 UTC | #10

Wouldn't you rather have a 3D slot machine? Maybe just the spinners (and handle?).

-------------------------

Leith | 2019-02-17 09:42:03 UTC | #11

You're being lazy now too :stuck_out_tongue:

-------------------------

Modanung | 2019-02-17 09:47:10 UTC | #12

I meant making only the spinners (and handle) 3D, to save resources on increased immersion.

-------------------------

Leith | 2019-02-17 11:04:01 UTC | #13

yeah it would be easier, but seems like a lot of overkill for a 2d thing.
I get where you are coming from, but for new coders, 3D is scary, and 2D is easier to consume on low end devices. So I offered the "proper" way to scroll textures.
Hey, pretty sure we don't have any Sample that does it, and not entirely sure our shaders even support it.

-------------------------

I3DB | 2019-02-17 17:35:32 UTC | #14

[quote="Jbonavita, post:1, topic:4928"]
I have a pretty straightforward scene I need created. It’s only a single screen with a slot machine and a few buttons and labels. The reels would need to be able to spin
[/quote]

Is there any reason it cannot be a 3d scene? With some 2d buttons perhaps.
 [Rotation in the space.](https://urho3d.github.io/samples/05_AnimatingScene.html)

[You could put the spinner in a frame, and spin the frame ... so many possibilities.](https://urho3d.github.io/samples/10_RenderToTexture.html)

[There's an urhosharp version most of those samples here](https://github.com/xamarin/urho-samples). It's fairly straight forward to use that code and create nearly anything you need. There's some xamarin workbook examples that show from a beginners perspective [how to create an object,](https://github.com/xamarin/Workbooks/blob/master/graphics/urhosharp/compound-shapes/CreatingUrhoCompoundShapes.workbook/index.workbook) and rotate them too in a format that lets you read about the code and execute it in real time. [Video about it here](https://youtu.be/ayvk_sVO6GM). [Lots of sample code here](https://github.com/xamarin/Workbooks/tree/master/graphics/urhosharp). With this the editor isn't needed, you can quickly complete task entirely in code.

And you wrote ...

[quote="Jbonavita, post:1, topic:4928"]
I can do all the coding
[/quote]

-------------------------

Jbonavita | 2019-02-17 17:34:02 UTC | #15

No reason. If it can be done in 3D, then that’s fine.

-------------------------

I3DB | 2019-02-17 17:44:50 UTC | #16

C[heck out this. It explains 3d space and how to put a simple shape and manipulate it. All from beginners perspective. xamarin workbook on urhosharp](https://github.com/xamarin/Workbooks/blob/master/graphics/urhosharp/coordinates/ExploringUrhoCoordinates.workbook/index.workbook) using urho3d.

[Or just watch the video ..](https://youtu.be/ayvk_sVO6GM).

-------------------------

Jbonavita | 2019-02-17 18:10:14 UTC | #17

Thanks, I’ll take.a look at it,

-------------------------

