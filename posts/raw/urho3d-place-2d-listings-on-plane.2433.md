Jimmy78 | 2017-01-02 01:15:22 UTC | #1

Hey guys , 

I just started using urho and i have never worked with graphics / game engines before . 

I had a question . i created a scene and placed a plane on it . Now i want to populate the place with some models but i'm unsure how to proceed .

I know the models can have a texure image but i want basically want to display an image and some text programmatically.


I have not chosen the shape / material yet but it will probably be a box unless someone has a better solution . 

I'm trying to mimic a 2D material on a 3D plane . This is a rough example : 

imgur.com/a/c8A4k


Any suggestions would be highly appreciated

-------------------------

jmiller | 2017-01-02 01:15:22 UTC | #2

Hey Jimmy, and welcome to the forum. :smiley:

If you have not seen the samples... they cover a lot of stuff beyond the [url=http://urho3d.github.io/documentation/HEAD/index.html]documentation[/url].

Several of them create a scene with a plane and add objects to it.
[url=https://github.com/urho3d/Urho3D/blob/master/Source/Samples/35_SignedDistanceFieldText/SignedDistanceFieldText.cpp]SignedDistanceFieldText.cpp[/url]

Seeing Text3D in use may give you some ideas (you can use any container UIElement):
[github.com/urho3d/Urho3D/search ... 3&q=Text3D](https://github.com/urho3d/Urho3D/search?utf8=%E2%9C%93&q=Text3D)

If you wanted the UI element to activate on mouseover, Samples/08_Decals has an example of raycasting ('picking') and there are others: [github.com/urho3d/Urho3D/search ... =%E2%9C%93](https://github.com/urho3d/Urho3D/search?q=RaycastSingle&utf8=%E2%9C%93)  and a number of topics around on that.

Just my 2 cents, let us know how things are going...

-------------------------

