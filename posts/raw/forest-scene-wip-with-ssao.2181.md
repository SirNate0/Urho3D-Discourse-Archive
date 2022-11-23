krstefan42 | 2017-01-02 01:13:43 UTC | #1

Here's a peek at a forest scene I've been working on. Right now I only have one tree model (made in Blender), but I plan to add a a lot more stuff. It uses an SSAO shader I wrote, which uses temporal reprojection to blend with the previous frame's AO result to reduce noise (sadly it only takes into account the camera's velocity, so fast moving objects will still have noise). I also wrote a higher-quality PCF shadow implementation, and made some other tweaks to the lighting code. I'll upload the SSAO code when finished (right now the temporal reprojection is using a weird hack involving a magic constant. Since I don't know why the hack fixes my code, I don't know if it will work for other scenes with different scale parameters, FOV, etc. If anyone wants to help me figure it out I can show you the code tomorrow).

[img]https://s4.postimg.org/o4ny928lp/Forest1.jpg[/img]


The tree model might look on the heavy side, but really fill rate is far more likely to be a bottleneck than triangle count on modern hardware, and I used some tricks to make them look more detailed than they really are (plus LOD models). The scene contains 500 trees, but I still get 60FPS thanks to the LODs.

Here's a shot of the raw AO term:


[img]https://s4.postimg.org/afb3q2s5p/Forest6.jpg[/img]

Here's some more screenshots, click to open.

[url=https://postimg.org/image/vmbuqo67j/][img]https://s3.postimg.org/vmbuqo67j/Forest2.jpg[/img][/url]

[url=https://postimg.org/image/od5fhdxl5/][img]https://s4.postimg.org/od5fhdxl5/Forest3.jpg[/img][/url]

[url=https://postimg.org/image/ub1gx8uj3/][img]https://s3.postimg.org/ub1gx8uj3/Forest5.jpg[/img][/url]

[url=https://postimg.org/image/90bcvijgp/][img]https://s4.postimg.org/90bcvijgp/Forest4.jpg[/img][/url]

-------------------------

yushli | 2017-01-02 01:13:43 UTC | #2

That looks amazing. look forward to your sample project so that I can try it out.

-------------------------

franck22000 | 2017-01-02 01:13:43 UTC | #3

Looking forward for the SSAO shader release :slight_smile: Nice work !

-------------------------

zedraken | 2017-01-02 01:13:44 UTC | #4

It is really a very nice work, very impressive !

-------------------------

dragonCASTjosh | 2017-01-02 01:13:44 UTC | #5

awesome work and im happy to help iv been looking to do AO but hadent gotten round to it :slight_smile:

-------------------------

Lumak | 2017-01-02 01:13:44 UTC | #6

This looks great!

-------------------------

codingmonkey | 2017-01-02 01:13:44 UTC | #7

nice!  :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:13:44 UTC | #8

There is already SSAO by reattiva, but it is quite old now. I think it was AngelScript and I ported it to back C++. This is my repo: [github.com/sabotage3d/UrhoSSAO](https://github.com/sabotage3d/UrhoSSAO)

-------------------------

krstefan42 | 2017-01-02 01:13:44 UTC | #9

Thanks guys!

Hmm, I didn't know someone had already done SSAO. I wonder why it hasn't been merged into master? His implementation seems fairly similar to mine, but he uses a bilateral blur instead of temporal reprojection to reduce noise (reprojection is better and faster in theory, but my implementation is flawed because it doesn't account for per-object velocity (which is not even possible without changes to the engine)). I figured out why I need the "magic constant" of around 500, and how to calculate the value properly from the FOV, thanks to a comment in his code. I'll see if I can learn anything else from his implementation.

-------------------------

Bananaft | 2017-01-02 01:13:45 UTC | #10

Looks lovely. Can you tell a bit more about your changes in lighting and shadows?

-------------------------

