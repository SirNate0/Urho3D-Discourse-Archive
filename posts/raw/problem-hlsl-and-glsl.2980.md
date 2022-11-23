SteveU3D | 2017-04-04 17:28:18 UTC | #1

Hi,
I have a very very weird problem with my application.
When I build it with Visual C++, I get the following : 

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/cb95f9b0af152cd1451a1fa54a6ffde103b0b842.png" width="638" height="500"> 

But when I build it with Qt Creator, I get : 

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/893f2c77f12e01ed22634eb0a24b37a7bb66c9c0.png" width="637" height="500">

As you can see, the head and the glasses are completely black :confused:
It's exactly the same code for the two results, and the CoreData and Data folders are the same too.

While I was writing this, I checked the console output and we can see the difference : GLSL used in Qt and HLSL in Visual.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a25bbe7ba46b9f8775e91da1c5bbef85f6307c17.png" width="690" height="434">
   
I don't know a lot about GLSL, HLSL so I don't know why it does that and how to correct it. I only know that Qt used openGL.
Any ideas?
Thanks.

-------------------------

SteveU3D | 2017-04-04 17:28:28 UTC | #2

I solved it. In fact, the model I use for the head and the glasses come from a .fbx and a .obj files respectively. And I converted them into .mdl with AssetImporter but without any option.

I converted the .fbx and .obj into .mdl again with -t (generate tangents), -cm (check and do not overwrite if material exists) and -ct (check and do not overwrite if texture exists)  options, and I get the good result in Qt, same as Visual, so same for GLSL and HLSL.

-------------------------

