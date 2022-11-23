sabotage3d | 2017-01-02 01:05:42 UTC | #1

I came across this articles yesterday about stack allocated containers:  [tuxedolabs.blogspot.co.uk/2015/0 ... iners.html](http://tuxedolabs.blogspot.co.uk/2015/02/stack-allocated-containers.html)
I wonder if Urho3d containers have something similar.
Is it safe to be used with existing Urho3d containers ?

-------------------------

GoogleBot42 | 2017-01-02 01:05:42 UTC | #2

[quote="sabotage3d"]I came across this articles yesterday about stack allocated containers:  <a rel="nofollow" href="http://tuxedolabs.blogspot.co.uk/2015/02/stack-allocated-containers.html" class="vglnk"><span>http</span><span>://</span><span>tuxedolabs</span><span>.</span><span>blogspot</span><span>.</span><span>co</span><span>.</span><span>uk</span><span>/</span><span>2015</span><span>/</span><span>02</span><span>/</span><span>stack</span><span>-</span><span>allocated</span><span>-</span><span>containers</span><span>.</span><span>html</span></a>
I wonder if Urho3d containers have something similar.
Is it safe to be used with existing Urho3d containers ?[/quote]

There is no reason why it shouldn't be as long as you are still using pointers to urho3d objects that urho3d needs to keep track of.  But for anything that the urho3d won't need to keep track of such as temporary objects can be allocated on the stack.  It should work just fine but you will run into problems that the blog post shows when you try to pass such values.  :wink:

-------------------------

sabotage3d | 2017-01-02 01:05:42 UTC | #3

I also found this as a more complete production code: [code.google.com/p/chrome-browse ... ontainer.h](https://code.google.com/p/chrome-browser/source/browse/trunk/src/base/stack_container.h)
And it can be used in conjunction with STL containers. Let me know your thoughts if there is something better out there.

-------------------------

