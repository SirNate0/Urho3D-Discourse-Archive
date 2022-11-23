GoogleBot42 | 2017-01-02 01:04:09 UTC | #1

Yep another question.   :wink:

By default Urho3D make an image blury when up close to an image when there is no more detail.  I want each pixel to be preserved.

Here is a screenshtot I made with irrlicht.  To enable this I did this to the mesh:
[code]mesh->setMaterialFlag(video::EMF_BILINEAR_FILTER, false);[/code]

[img]https://www.dropbox.com/s/5wzfcsjmyg3oxvb/Screenshot_2015-03-13_18-57-21.png?raw=1[/img]

How do I do this in Urho3D?

Yes I am planning on making a minecraft clone. :slight_smile:

-------------------------

GoogleBot42 | 2017-01-02 01:04:09 UTC | #2

Never mind I figured it out...

[code]someTexture->SetFilterMode(FILTER_NEAREST);[/code]

-------------------------

weitjong | 2017-01-02 01:04:09 UTC | #3

I think you can also do that declaratively instead of programmatically. See this section of the documentation [urho3d.github.io/documentation/H ... s_Textures](http://urho3d.github.io/documentation/HEAD/_materials.html#Materials_Textures).

-------------------------

GoogleBot42 | 2017-01-02 01:04:11 UTC | #4

[quote="weitjong"]I think you can also do that declaratively instead of programmatically. See this section of the documentation [urho3d.github.io/documentation/H ... s_Textures](http://urho3d.github.io/documentation/HEAD/_materials.html#Materials_Textures).[/quote]

Hmmm I am going to make a game that is modable and the mods will load their own textures... can I load a material that doesn't have a texture specified and load the texture later?

EDIT: Here's a pic of the same textures rendered in Urho3D.  :smiley: 

[spoiler][img]https://www.dropbox.com/s/kpcls5lcwq83uf0/Screenshot_2015-03-14_15-05-44.png?raw=1[/img][/spoiler]

-------------------------

thebluefish | 2017-01-02 01:04:12 UTC | #5

Yes you can change the texture in the material. Just know that all geometry that uses that material will have the new texture, but you can clone it if you need to.

-------------------------

GoogleBot42 | 2017-01-02 01:04:12 UTC | #6

[quote="thebluefish"]Yes you can change the texture in the material. Just know that all geometry that uses that material will have the new texture, but you can clone it if you need to.[/quote]

Thanks! Just what I needed to know!  I think am am begining to get Urho3D's structure. :slight_smile:

EDIT: I just realized how silly it is that irrlicht allows for one to change the texture filtering mode in the mesh... it just doesn't make sense and it is confusing for those who don't understand what the difference is between a mesh, material, and texture...

-------------------------

