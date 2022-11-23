friesencr | 2017-01-02 01:01:49 UTC | #1

I noticed this and had similar thoughts when working on the SpritePacker.  I don't think I could have made a 2d animation from the api alone.

-------------------------

aster2013 | 2017-01-02 01:01:49 UTC | #2

You are right, we need to refactor these 2d animation classes, make more 2d animation format file can added.  I will figure out it later.

-------------------------

aster2013 | 2017-01-02 01:01:52 UTC | #3

Hi, @Sinoid. I have finished the refactor of 2D animation. I think it is more clear and decouple from Spriter.
Now a 2D animation includes some animation tracks, and animation tracks includes some animation key, it sames as 3D animation.
Please check out the refactor-animation2d branch. I hope you enjoy it.

-------------------------

