1vanK | 2017-01-02 01:11:00 UTC | #1

Jack has damaged walk animation. I wanted to fix it, but I have not found a way to open it in Blender. It seems that Jack converted from Ogre3D format, but I have not found any workable importer. Where can I find an original model?

-------------------------

cadaver | 2017-01-02 01:11:00 UTC | #2

In Urho's SourceAssets directory there are mesh.xml & skeleton.xml Ogre originals. The actual original art files were in some old version of 3DS Max, Stinkfist maybe has/had the link (?) When played with Ogre, the walk animation indeed looks better, so maybe it's just a matter of fixing OgreImporter to convert the animation right, if there's something missing/changed.

-------------------------

1vanK | 2017-01-02 01:11:01 UTC | #3

[quote="cadaver"]When played with Ogre, the walk animation indeed looks better, so maybe it's just a matter of fixing OgreImporter to convert the animation right, if there's something missing/changed.[/quote]

[code]// Transform from bind-pose relative into absolute
pos = bone->bindPosition_ + pos;
rot = bone->bindRotation_ * rot;[/code]

give more accurate animation, but still little deformation in foots. Was there something like that in the original animation?

[img]http://savepic.ru/9038025.png[/img]

-------------------------

weitjong | 2017-01-02 01:11:01 UTC | #4

Hi 1VanK, while you are on it, could you also see if it is possible to do something about this. Jack has been running around naked in our samples for far too long  :wink: . But seriously now, what I really hope to see is to reduce the number of bones it uses because as it is now Jack cannot be animated correctly on RPI platform, perhaps we need two versions of it if we still want to use model with many bones to showcase the engine. Even better, could we have something cuter as the model?

-------------------------

1vanK | 2017-01-02 01:11:01 UTC | #5

[quote="weitjong"]Even better, could we have something cuter as the model?[/quote]

I think we can use something from blendswap

-------------------------

1vanK | 2017-01-02 01:11:01 UTC | #6

[quote="weitjong"]Jack has been running around naked in our samples for far too long  ;)[/quote]

By the way it has textures :)

Textures\Jack_body_color.jpg
Textures\Jack_face.jpg

-------------------------

weitjong | 2017-01-02 01:11:01 UTC | #7

[quote="1vanK"][quote="weitjong"]Jack has been running around naked in our samples for far too long  :wink:[/quote]

By the way it has textures :slight_smile:

Textures\Jack_body_color.jpg
Textures\Jack_face.jpg[/quote]
In certain sample where we are constantly looking at Jack's back and bottom, my eyes get hurt due to shininess of his skin complexion  :laughing:

-------------------------

Modanung | 2017-01-02 01:11:17 UTC | #8

I started working on [url=http://discourse.urho3d.io/t/ahab/1895/5]Ahab[/url] inspired by this thread.

-------------------------

Stinkfist | 2017-01-02 01:11:45 UTC | #9

Here are the realXtend avatar files I've gathered some years ago:
[dl.dropboxusercontent.com/u/164 ... vatars.zip](https://dl.dropboxusercontent.com/u/16413694/rex/Naali-ExtraAvatars.zip)
[dl.dropboxusercontent.com/u/164 ... 3dsmax.zip](https://dl.dropboxusercontent.com/u/16413694/rex/realxtend_avatars_3dsmax.zip)
[dl.dropboxusercontent.com/u/164 ... rs_obj.zip](https://dl.dropboxusercontent.com/u/16413694/rex/realxtend_avatars_obj.zip)

-------------------------

