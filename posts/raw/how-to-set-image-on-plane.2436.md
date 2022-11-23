Jimmy78 | 2017-01-02 01:15:23 UTC | #1

Hey guys ,

i have an image 500*500 px  (.png)

I want to set it as the background for my plane . 

This is my plane : 

planeNode.Scale = new Vector3 (1000, 1, 1000);

I want it to expand accordingly and take the full size of the plane .

How can i achieve this ?

I'm using c# in Xamarin

-------------------------

jmiller | 2017-01-02 01:15:24 UTC | #2

Hi Jimmy,

To change texture mapping, you can use [url=https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_material.html#a2470fc628c1bbdb6b52054076714ff41]Material::SetUVTransform()[/url] or the material properties in the editor.

[urho3d.github.io/documentation/ ... rials.html](https://urho3d.github.io/documentation/HEAD/_materials.html)

-------------------------

