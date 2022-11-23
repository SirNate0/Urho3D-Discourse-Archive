dev4fun | 2018-02-16 20:01:12 UTC | #1

Hey, Im importing some FBX models on Urho editor to test somethings, and I noted that cast shadows of directional light, just works on hidden faces (as Im using Cull Mode none, the face appears on editor, otherwise, wouldnt show). Check the pictures:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/1/14216e0a413dfebe737f54e672fcced95607e2e1.jpg'>

This way, to test, I flipped the others faces to test if cast shadows would works:
(more one time, if not have cull mode = none, the face would be hidden on urho editor)
https://puu.sh/zpd4q/af98e8f472.gif

And... cast shadows works
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/4/4f64084835602f4af5059afdf5620abb1ef4a204.jpg'>

Material Settings:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/1/146f21b972ac25aa4e7729c173cba62a8d571fa0.png'>

Some notes:
All materials its using the technique DiffAlphaMask.xml, and all uses cullmode=none, I've already tried to use Diff.xml and uses cullmode normally, but nothing works.

Anyone knows what can be? 
Thanks.

-------------------------

Lumak | 2018-02-16 21:23:53 UTC | #2

Looks like you'll need to generate **tangents** by using the **-t** option for AssetImport.

-------------------------

dev4fun | 2018-02-17 00:17:41 UTC | #3

Hmmm... Didnt work :(

@Was need triangulate mesh on 3ds max, reset pivot and export FBX again to fix it.

-------------------------

