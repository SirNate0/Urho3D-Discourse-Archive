kyawkyawwin18 | 2017-01-02 01:01:49 UTC | #1

I have tried to generate the mdl file by using AssetImporter tools in MacOS.

Case 1:
======
I used samuzai_animation_ok.FBX (free 3D model package from Unity Assetstore).
I got the following errors.

[quote]Skeleton with multiple root nodes found, not supported[/quote]

Case 2:
======
I used my own 3D model and I got this error message because I have more than 64 bones.

[quote]Geometry has too many bone influences[/quote]

My questions are:
1. How should I prepare the 3D model with multiple meshes to use in Urho3D?
2. Is there any guideline for preparing the models in 3D Authoring Tools, such as Maya Lite, 3DS Max, to use in Urho3D?
3. Can somebody share me the proper working fbx file?

PS: I have double checked with my using fbx files with "Autodesk FBXViewer (From FBXConverterUI Tools)" and "Autodesk FBXReview Tools". There is no issue with my fbx files.

With Best Regards,
Win

-------------------------

codingmonkey | 2017-01-02 01:01:50 UTC | #2

>Skeleton with multiple root nodes found, not supported
you must connect (make keep offset relation) these separeted bones to one Master bone or Root bone.

>Geometry has too many bone influences
no more then 4-bones on one vertex influence i suppose. 
to limit count of influents on vertex it's work for your 3d editor.

-------------------------

cadaver | 2017-01-02 01:01:50 UTC | #3

The bone influence error message is a bit poorly worded. What it means is that there's a maximum of 64 bones per submesh. This means that if for example your model has a complex face rig, its face should be a separate submesh (in modeling programs this is usually be achieved by using another material on it) to not overshoot the limit. Meanwhile the body submesh could use another 64 bones.

If there are more than 4 bones influencing a single vertex, the extra influences (starting from lowest weights) will be dropped and that isn't a fatal error.

-------------------------

kyawkyawwin18 | 2017-01-02 01:01:53 UTC | #4

Dear codingmonkey and cadaver,

Thanks for your answers.

Please allow me to clarify one more question.
Is there any maximum meshes per model?

Regards,
Kyaw Kyaw Win

-------------------------

cadaver | 2017-01-02 01:01:53 UTC | #5

Not really, but the more you have, the more inefficient rendering will be (more draw calls).

-------------------------

devrich | 2017-01-02 01:02:33 UTC | #6

[quote="cadaver"]The bone influence error message is a bit poorly worded. What it means is that there's a maximum of 64 bones per submesh. This means that if for example your model has a complex face rig, its face should be a separate submesh (in modeling programs this is usually be achieved by using another material on it) to not overshoot the limit. Meanwhile the body submesh could use another 64 bones.

If there are more than 4 bones influencing a single vertex, the extra influences (starting from lowest weights) will be dropped and that isn't a fatal error.[/quote]


I'm new here and i have two questions if I may:

1:  is the 64 bones per submesh limit still 64 in the github master branch?

and 2: I downloaded the ver 1.32 "release" and prefer to use release versions versus using w.i.p respositories -- around the Urho3D community forums here; which version is the standard to use?  I ask this rather odd question because another engine i had been using for the past year prefers users to use the next version repositiry after it has reached a certain level of development even though its official release stage is still months away.  So I just want to make sure to follow with the community but i also much prefer to use "official releases" as they usually will be considered "production-ready" and I am very eager to get my game going :smiley:

-------------------------

jmiller | 2017-01-02 01:02:33 UTC | #7

[quote="devrich"]1:  is the 64 bones per submesh limit still 64 in the github master branch?[/quote]
Yes, seems so.
I think there is the same limit in [b]reattiva[/b]'s Blender exporter: [github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender)
It refers to this as a limitation of HW-skinning? In any case it's really nice.

[quote="devrich"]and 2: I downloaded the ver 1.32 "release" and prefer to use release versions versus using w.i.p respositories -- around the Urho3D community forums here; which version is the standard to use?  I ask this rather odd question because another engine i had been using for the past year prefers users to use the next version repositiry after it has reached a certain level of development even though its official release stage is still months away.  So I just want to make sure to follow with the community but i also much prefer to use "official releases" as they usually will be considered "production-ready" and I am very eager to get my game going :smiley:[/quote]

I'm not sure about usage statistics. Many do work with and discuss the master branch, including those working on Urho3D, other projects, or both.
I stick with the master branch for various reasons; it's always worked great for me, slips in new features, and I'm constantly impressed with how smooth updates are. ..due to good design and management, not a lack of development.  :slight_smile: 

On the other hand, since the API seems fairly well-defined, it should not be difficult to update only releases and you should find most of the discussion relevant.
Just my 2 cents.

-------------------------

devrich | 2017-01-02 01:02:33 UTC | #8

Thanks Carnalis, i appreciate your insight and i think you're right  :slight_smile:

-------------------------

