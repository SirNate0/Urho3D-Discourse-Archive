vivienneanthony | 2017-01-02 00:59:52 UTC | #1

Hello,

I want to integrate libnoise as either as part of the engine extensively for terrain. Do anybody know any licensing issue? I was thinking in the Engine adding a subfolder Noise or add Libnoise as a Thirdparty.

I'm looking at [libnoise.sourceforge.net/index.html](http://libnoise.sourceforge.net/index.html)
 
If I can get it added. FIrst create a custom function to transfer the generated to a Image object. (Thinking a libnoise can use a util function like RendererWriteUrhoImage)

Vivienne

-------------------------

weitjong | 2017-01-02 00:59:52 UTC | #2

[quote]LGPL libraries are not OK for Urho3D, as we need to be able to compile into static libraries on iOS, and embed into .apk's on Android, and both scenarios don't readily allow the user to replace the library in question. We can take only permissive licenses with no restriction on static linking (BSD/MIT/Apache etc.)[/quote]

This was Lasse's respond on other topic regarding allowed licenses for Urho3D.

-------------------------

friesencr | 2017-01-02 00:59:53 UTC | #3

Does stb_perlin work? [github.com/nothings/stb/blob/ma ... b_perlin.h](https://github.com/nothings/stb/blob/master/stb_perlin.h) for your needs?

-------------------------

weitjong | 2017-01-02 00:59:53 UTC | #4

Just want to add that, of course, there is nothing prevent you from using any libraries in your own project :slight_smile:.

-------------------------

vivienneanthony | 2017-01-02 00:59:53 UTC | #5

[quote="friesencr"]Does stb_perlin work? [github.com/nothings/stb/blob/ma ... b_perlin.h](https://github.com/nothings/stb/blob/master/stb_perlin.h) for your needs?[/quote]

I don't know. I have to look at the code and do the following. 

1. Add a function to create a array in memory that holds the value for a image size
2. Find a way to convert that array to a image.
3. Then add Terrain function that uses that image to a Image object 
4. Add ability to save image to a file

4. Figure out code to add a lot more functions ability. (Note: Make code assembly or gpu performance based so it's dirt fast!!!)

So, hopefully it ends up to something lik.

[youtube.com/watch?v=R8XsRYsc7Nk](https://www.youtube.com/watch?v=R8XsRYsc7Nk)
[youtube.com/watch?v=OQu73MNvx48](https://www.youtube.com/watch?v=OQu73MNvx48)

-------------------------

vivienneanthony | 2017-01-02 01:00:01 UTC | #6

[quote="weitjong"]Just want to add that, of course, there is nothing prevent you from using any libraries in your own project :slight_smile:.[/quote]

I'm going try this.

[topic326.html#p2057](http://discourse.urho3d.io/t/procedural-generated-worlds/335/6)

-------------------------

