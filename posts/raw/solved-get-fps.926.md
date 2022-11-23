GoogleBot42 | 2017-01-02 01:04:08 UTC | #1

I feel really stupid about asking this but... how you get the current fps?  I grep'ed the entire urho3d source code and it didn't help all I found is where Urho3D caps the fps limit but it doesn't use the current fps to do this as far as I can tell.

-------------------------

TikariSakari | 2017-01-02 01:04:08 UTC | #2

[quote="GoogleBot42"]I feel really stupid about asking this but... how you get the current fps?  I grep'ed the entire urho3d source code and it didn't help all I found is where Urho3D caps the fps limit but it doesn't use the current fps to do this as far as I can tell.[/quote]

On windows and linux at least you can press F2 to see the hud. The leftmost number is how many times each of the thing gets called per second. Then at the bottom is something called applyframelimit, which up to my understanding means how much it sleeps per second. So if you cap the fps to 60, and it shows 10ms, then it only takes 7ms to render + update the whole frame.

-------------------------

friesencr | 2017-01-02 01:04:08 UTC | #3

You want the debug hud. FPS is the number on the left.

[github.com/urho3d/Urho3D/blob/m ... e.inl#L175](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/Sample.inl#L175)
[github.com/urho3d/Urho3D/blob/m ... e.inl#L200](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/Sample.inl#L200)

-------------------------

Bluemoon | 2017-01-02 01:04:08 UTC | #4

I guess this should help...
[url]http://discourse.urho3d.io/t/solved-debughud-display-explanation/378/1[/url]

-------------------------

TikariSakari | 2017-01-02 01:04:08 UTC | #5

Like people said you can open hud with F2, if you use the samples.

You can see how many times something is being called per second. Also there is a thing called apply limit, which shows how much time per frame you are sleeping. So in my picture even with 200 fps there is almost 3 milliseconds (2.952) extra time per frame, meaning each frame takes only 2ms time to create+render, so the fps could be as high as 500 in theory.

[url]http://i.imgur.com/xP4glUc.png[/url]

Edit: The green fps-number on top is just a ui-text that I manually added. So it doesn't really exist there normally.

-------------------------

GoogleBot42 | 2017-01-02 01:04:08 UTC | #6

OK Thanks guys!  I cannot find fps on the debug hud but I can it is easy to look at the profiler and tell if the graphics is lagging thanks!

-------------------------

rogerdv | 2017-01-02 01:04:13 UTC | #7

I wrote my own  simple FPS calculator, just counting frames and adding the elapsed time each frame until it reaches 1 second, not strictly prceise, but I have a single number and not several rows of values.

-------------------------

