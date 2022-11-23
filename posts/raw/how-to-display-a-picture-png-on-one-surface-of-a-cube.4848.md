majhong | 2019-01-22 10:02:35 UTC | #1

i have a model with three Material slot,
index  0  is green
index  1 is white
index  2 is a surface with a picture ( i need modify the picture dynamic!)

-------------------------

Leith | 2019-01-22 13:02:19 UTC | #2

First, you need to describe the texture using UV coordinates, then, you need to maintain the texture that is being expressed via those UV coordinates. I am assuming your picture is changing. So if that is the case, you need to update the texture object.

-------------------------

Dave82 | 2019-01-22 14:29:05 UTC | #3

Use :
YourModel->SetMaterial(0 , greenMaterial);
YourModel->SetMaterial(1 , whiteMaterial);
YourModel->SetMaterial(2 , pngPictureMaterial);

Normally your model must have 3 geometries and must have texture coords.
For creating the above mentioned materials see the Urho examples or just copy one of the materials that comes with urho and change it to your needs.
(Or use CoreData/DefaultGrey.xml and change it to white and greenetc)

>  i need modify the picture dynamic!

How much dynamic ? if it is just few frames , load them all and change the textures using a timer , but if it is a avi file or other video then it is another story. Serach the forum there are couple video players floating around.

-------------------------

Modanung | 2019-01-22 14:28:59 UTC | #4

Welcome to the forums! :confetti_ball: :slightly_smiling_face:

This thread may help you in the right direction to get the texture painting working:
https://discourse.urho3d.io/t/dynamically-change-texture-or-paint-on-texture/2372

-------------------------

majhong | 2019-01-23 03:01:06 UTC | #5

I have already use SetMaterial(index , Material) ,the index 0 and index 1 is normal .but the index 3 need a picture, i export from blender (Blender to Urho3D Guide)  
export texture only support uv coordinate, i need use the picture fill the entire surface.

i need like this
https://tse3.mm.bing.net/th?id=OIP.jyUK6KOSDwwkQF6oo2kncQHaEq&pid=Api

my state is this 
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/b/b3187a35f7236b11b2cc6dfed1ed5be3874135ad.jpeg'>

how to define a xml which use picture(texture) fill the entire surface.

thank you  everyone！

-------------------------

I3DB | 2019-01-23 02:33:19 UTC | #6

One way is to use two cubes, so a smaller picture cube is inside a larger container cube, except one face is slightly outside the container cube.

Then you don't have to worry about just putting material on just one side.

-------------------------

Dave82 | 2019-01-23 02:45:30 UTC | #7

Just create a file like this : 

[code]
<material>
    <technique name="Techniques/Diff.xml" />
    <texture unit="diffuse" name="YourPath/YourTexture.png" />
</material>
[/code]

-------------------------

majhong | 2019-01-23 03:43:33 UTC | #8

it is not work!

my code is:
//test load dynamic
boxObject->SetModel(cache-&gt;GetResource&lt;Model&gt;("Models/majhong/mj.mdl"));
boxObject->SetMaterial(1,cache->GetResource&lt;Material&gt;("Models/majhong/mj_1.xml"));
boxObject->SetMaterial(2,cache->GetResource&lt;Material&gt;("Models/majhong/mj_2.xml"));
//load face
boxObject->SetMaterial(0,cache-&gt;GetResource&lt;Material&gt;("Models/majhong/mj_0.xml"));
//boxObject->SetMaterial(0,cache-&gt;GetResource&lt;Material&gt;("Materials/Stone.xml"));
//boxObject->SetMaterial(0,cache-&gt;GetResource&lt;Material&gt;("Materials/Skybox.xml"));

the result is :
mj_0.xml
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/a/a57508f99fe3c6c9bc5dbe166c3db36306717a63.jpeg'>
Stone.xml
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/3/324887396ffebddc65f69cd8cea630411d8c18c0.jpeg'>
Skybox.xml
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/d/d87a9768e59b17e99108ea746b59cc591f14a1b4.jpeg'>

my picture (41.png) is:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/d/dde879e679468ff57a06ca4c983742b232459366.png'>

-------------------------

majhong | 2019-01-23 03:31:07 UTC | #9

mj_0.xml   content:

**&lt;material&gt;**

  **&lt;technique** name **=** "Techniques/Diff.xml" **/&gt;**

  **&lt;texture** unit **=** "diffuse" name **=** "Textures/41.png" **/&gt;**

**&lt;/material&gt;**

-------------------------

majhong | 2019-01-23 03:43:10 UTC | #10

how to describe the texture using UV coordinates?  please give me a  tools!

-------------------------

Dave82 | 2019-01-23 03:58:23 UTC | #11

The second picture shows that you don't have UV coords defined properly. It's like a planar map. The easiest way o set UV coords is to edit them in blender.

-------------------------

majhong | 2019-01-23 05:26:11 UTC | #12

i think i need a planar mapping ,but i can not find anything in  documents

or perhaps a decal is another way!

-------------------------

Modanung | 2019-01-24 02:38:00 UTC | #13

For the UVs a simple _Cube Projection_ should work. In Blender, select your piece then enter _Edit Mode_ [**Tab**] and:
- _Select All_ [**A**] (or at least the face that needs texturing)
- _UV Mapping_ [**U**]
- _Cube Projection_ [**C**]

In the _UV/Image Editor_ you can improve the fit by grabbing, rotating and scaling faces or vertices, just like in the _3D View_.

-------------------------

