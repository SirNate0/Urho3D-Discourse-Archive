Enhex | 2017-01-02 01:11:22 UTC | #1

Normal Offset seems like a better way to eliminate self-shadowing with much less to virtually no peter panning:
[dissidentlogic.com/old/image ... Offset.png](http://www.dissidentlogic.com/old/images/NormalOffsetShadows/GDC_Poster_NormalOffset.png)

[dissidentlogic.com/old/](http://www.dissidentlogic.com/old/) (has [url=http://www.dissidentlogic.com/old/video/Techniques/NormalOffsetShadows_0001.wmv]explanation video[/url])
[digitalrune.com/Blog/Post/1765/Shadow-Acne](https://www.digitalrune.com/Blog/Post/1765/Shadow-Acne)
[ndotl.wordpress.com/2014/12/19/ ... adow-bias/](https://ndotl.wordpress.com/2014/12/19/notes-on-shadow-bias/)
[mynameismjp.wordpress.com/2013/ ... adow-maps/](https://mynameismjp.wordpress.com/2013/09/10/shadow-maps/)
[c0de517e.blogspot.co.il/2011/05/ ... notes.html](http://c0de517e.blogspot.co.il/2011/05/shadowmap-bias-notes.html)

-------------------------

Bananaft | 2017-01-02 01:11:26 UTC | #2

Aren't there already "Depth Slope Bias" aka slopeScaledBias parameter ?

-------------------------

Enhex | 2017-01-02 01:11:26 UTC | #3

[quote="Bananaft"]Aren't there already "Depth Slope Bias" aka slopeScaledBias parameter ?[/quote]
It's kinda confusing, but slope scale bias is something else, it's about scaling the constant depth offset according to the angle of the slope, and that causes severe peter panning.

[img]http://i.imgur.com/vXwjqC1.jpg[/img]

I recommend watching the video, it explains the difference between constant & slope bias and normal offset bias:
[dissidentlogic.com/old/video ... s_0001.wmv](http://www.dissidentlogic.com/old/video/Techniques/NormalOffsetShadows_0001.wmv)

Daniel Holbert also uploaded a tech demo on that [url=http://www.dissidentlogic.com/old]website[/url] that works with Nvidia FX Composer.

-------------------------

cadaver | 2017-01-02 01:12:13 UTC | #4

Normal offset shadow bias is in. See added normalOffset_ member in BiasParameters.

According to my tests this is most useful on desktops, as on mobile devices the shadow coordinate interpolation is rather low precision.

-------------------------

1vanK | 2017-01-02 01:12:13 UTC | #5

Oh, Slope Bias + Normal offset works perfect!

Some tests:

1)  Without bias
[url=http://savepic.ru/9680018.htm][img]http://savepic.ru/9680018m.png[/img][/url]
2) Constant bias
[url=http://savepic.ru/9667730.htm][img]http://savepic.ru/9667730m.png[/img][/url]
3) Slope bias
[url=http://savepic.ru/9657490.htm][img]http://savepic.ru/9657490m.png[/img][/url]
4) Normal offset
[url=http://savepic.ru/9671826.htm][img]http://savepic.ru/9671826m.png[/img][/url]
5) SlopeBias + Normal offset
[url=http://savepic.ru/9661586.htm][img]http://savepic.ru/9661586m.png[/img][/url]

-------------------------

rikorin | 2017-01-02 01:12:13 UTC | #6

Huge Thank You for this, it works amazing! No more detached shadows.
Though now it became apparent that physics objects are not touching the surface :slight_smile:  
How can I change the distance of contact for physics objects? (figured it out, have to change margin for the floor, not the object )

-------------------------

Enhex | 2017-01-02 01:12:13 UTC | #7

So glad it's been added!

[quote="rikorin"]Huge Thank You for this, it works amazing! No more detached shadows.
Though now it became apparent that physics objects are not touching the surface :slight_smile:  
How can I change the distance of contact for physics objects? (figured it out, have to change margin for the floor, not the object )[/quote]

With Bullet physics you have a default collision margin that for most shapes extrudes outwards. You'll just have to take it into account when matching the size of the model and collision shape.
Good video about it: [youtube.com/watch?v=BGAwRKPlpCw](https://www.youtube.com/watch?v=BGAwRKPlpCw)

-------------------------

rikorin | 2017-01-02 01:12:13 UTC | #8

Thanks for the video, you've probably saved me a lot of time and nerves in the future :3
And Bullet is really good.

-------------------------

