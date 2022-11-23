TikariSakari | 2017-01-02 01:03:32 UTC | #1

I've been asking a lot of questions, but I just couldn't find any example that would use tweens, nor anything was found with googleing. The only thing that I think could use tweening would be example 18, where the character moves from a to b, but that uses navmesh and it doesn't seem to be all purpose thing.

Anyways is there tweening engine or something similar in urho3d?

-------------------------

GoogleBot42 | 2017-01-02 01:03:32 UTC | #2

Yes it does!  Here's a link: [url]http://urho3d.github.io/documentation/1.32/_attribute_animation.html[/url]  :wink:

-------------------------

TikariSakari | 2017-01-02 01:03:32 UTC | #3

Hmm it seems quite close to what I was thinking a tween would be. Maybe my definition for tween isn't same, but something with different types of interpolations, although it might be doable with animations. I think the biggest thing that I am missing from the tweens that I've used is something with callback functions, when for example the tween has finished. With this it is easy to chain tweens / branch tweens, although just managing the keyframes manually should do it, but the ease of using tweens probably isn't there anymore or maybe this thing is in there already.

For example something I've used a tween for, which might be wrong way to use one, would be something where for example a level up happens after killing a monster and some level up screen comes. So chaining the tween of monster dying -> exp gain -> level up, with call backs its kind of easy, although it might not be the way tweens should be used. For example this whole sequence could be just fireing tweens in a sequence and let it go. [video]https://www.youtube.com/watch?v=TxmnQpTDpVk[/video]

Maybe my way of using tweens has been wrong to begin with. I've used them for adding exp to a character, where a visual number changes and stuff like that, where the tween isn't really a graphical element at all.

-------------------------

TikariSakari | 2017-01-02 01:03:33 UTC | #4

In the end I ended up trying to code one by myself. I feel that the lack of my knowledge from C++ in general made the whole implementation quite bad, for what I have now. There are no sequentical tweens nor parallel ones and the way I define the lambdas for linear and cubic interpolation are pretty horrible, since I couldn't figure out how to make static constant lambdas.

Here is what I have now in case someone is even mildly interested:
[url]http://pastebin.com/4m450frw[/url]

-------------------------

TikariSakari | 2017-01-02 01:03:36 UTC | #5

I finally managed to get something working. Although now that I looked again at the valueanimation, I should have just used that. Anyways I made some repositary for it:
[url]https://bitbucket.org/Kurahavi/tweenish/src[/url]

It requires c++11 in order to even compile and does it even work correctly, I am not sure. I managed to run it on android (nexus 5). I doubt that the thing is very light in terms of speed though.

I noticed that the splatting custom made images (decals) on ground doesn't work on android though.

Here is the video of my tweeningish test.
[video]https://www.youtube.com/watch?v=QZV9TKuIlWk&feature=youtu.be[/video]

For some reason the quality seems pretty bad.

Edit: I was thinking if I could make the parallel objects work as a threads, so the update could be spread among smaller pieces, or if it even has any impact. I figured out that parallel stuff should be truly parallel, as in they are not connected with each other in any way. I shall see how it goes, probably bad or crashes the whole system.

Edit2: 
Surprisingly, against everything I would have guessed (considering I am using templates and several function pointers ) somehow the mover that I made works faster when I tried 10k objects than using attribute animation on my desktop, unless I used it the wrong way somehow, which is highly likely. Although my "tweenish" thing only has run once thing.

-------------------------

