amit | 2017-01-02 01:01:58 UTC | #1

I do not know if its the place to request,
i am lookin for a basic phon material like,
[upload.wikimedia.org/wikipedia/c ... sion_4.png](http://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Phong_components_version_4.png/800px-Phong_components_version_4.png)
 some how i am not able to find one in samples too, nor was editor any help
I am still not very used to urho Material system so am quite stuck  
should work on mobile too

-------------------------

codingmonkey | 2017-01-02 01:01:58 UTC | #2

have you tried: lowpoly model(with smooth normals) + color texture + normal map from hipoly ? 
material with std diff tech + and a bit of light in scene

-------------------------

amit | 2017-01-02 01:01:58 UTC | #3

only color and smooth normal are there, do we req normal map? diff map?

-------------------------

codingmonkey | 2017-01-02 01:01:59 UTC | #4

>do we req normal map?
only if geometry is lowpoly and you want to make it  more smooth - yes.

>diff map?
you can do this and without texture. If you do not needed the texture on the object. Use only color (MatDiffColor) in material inspector.


I tried to do the same as your picture.
Really i do not know if it looks like on the plastic?
And normal maps I think it is not correct baked. My xNormal lost some lib's. 
In general, it is possible and without the normal map.

[video]http://youtu.be/pqnaK9rkGCs[/video]

-------------------------

hdunderscore | 2017-01-02 01:01:59 UTC | #5

To get those really defined specular highlights in urho, increase the specular power (alpha value in MatSpecColor) to something really high.

-------------------------

amit | 2017-01-02 01:01:59 UTC | #6

@codingmonkey 
This community is awesome, thanks you it is the look i need.

-------------------------

