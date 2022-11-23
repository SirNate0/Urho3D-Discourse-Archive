dev4fun | 2018-02-15 21:16:57 UTC | #1

Hey, my skinned meshes on 3ds max uses biped skeleton as Editable Mesh (have nothing to do about it), this way, when I export to FBX and use AssetImporter from Urho3D, the skeleton is considered a normal mesh, and render this normally.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/9/9ff5c39163ea7254b2c1d0f5c4883da110d8fc69.png'>

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/e/eed114f86d52ddf86e2cbda40515cd2273b68f5a.png'>

What can I do to hide this skeleton?
Thanks!

-------------------------

Eugene | 2018-02-15 21:35:21 UTC | #2

I don't really know solution, but I suggest you to try Collada DAE format instead of FBX.
If it doesn't help... IDK
https://answers.unity.com/questions/34141/bones-are-visible-would-like-them-not-to-be-.html

-------------------------

dev4fun | 2018-02-15 21:35:31 UTC | #3

Works perfectly, thanks man.

-------------------------

Dave82 | 2018-02-16 02:19:06 UTC | #4

I usually export skinned meshes in x format from max and had the same issue.IDK if it helps but try to hide all your biped parts before export.It works with x

-------------------------

