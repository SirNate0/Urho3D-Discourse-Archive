entretoize | 2019-05-19 13:35:45 UTC | #1

Hello, I created a blank project from UrhoSharp template in visual studio 2019 and added these files in MyData folder :
 
    _ Textures
      |_ cube.png
    _ Materials
      |_ cube.xml
    _ Models
      |_ Cube.mdl
    _ techniques
      |_ Diff.xml

In the cube.xml there's : 

    <?xml version="1.0" ?>
    <material>
    	<technique name="techniques/Diff.xml" />
    	<texture name="textures/cube.png" unit="diffuse" />
    	<parameter name="MatDiffColor" value="1 1 1 1" />
    	<parameter name="MatSpecColor" value="0.5 0.5 0.5 50" />
    </material>

In my app I have : 

    cubemodel.Model = cache.GetModel("Models/Cube.mdl");
    var material = cache.GetMaterial("Materials/cube.xml").Clone("");
    cubemodel.SetMaterial(material);

In android the cubemodel loads fine, but the material fails to with an exception : 
`Could not find resource techniques/Diff.xml`

What I'm doing wrong ?

Thanks

-------------------------

entretoize | 2019-05-19 13:35:01 UTC | #2

I can add that the same thing works in desktop.

-------------------------

orefkov | 2019-05-19 18:14:24 UTC | #3

Android pathes is case sensitive. First check that all pathes is right.

-------------------------

Leith | 2019-05-20 07:31:42 UTC | #4

Yep, same for Linux - capitalization must match exactly.

-------------------------

Modanung | 2019-05-20 21:37:04 UTC | #5

[quote="entretoize, post:1, topic:5163"]
What I’m doing wrong ?
[/quote]
You're using UrhoSharp.

-------------------------

entretoize | 2019-05-21 06:53:04 UTC | #6

I created a new blank project and defined blender to export with only first letter cap, and it works even if I was unable to correct the initial project. Thanks for your help.

-------------------------

entretoize | 2019-05-21 06:53:56 UTC | #7

What do you mean ? That Urho is bad or that or that it must not been used in C# ? What do you suggest ?

-------------------------

JTippetts1 | 2019-05-21 06:58:41 UTC | #8

It was most likely a tongue in cheek reference to the fact that these are the Urho3D forums, not the UrhoSharp forums. UrhoSharp is a different downstream project.

-------------------------

entretoize | 2019-05-21 07:48:46 UTC | #9

As my problem appeared for android platform and not for desktop, you're probably true.

-------------------------

