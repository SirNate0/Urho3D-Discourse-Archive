Lumak | 2017-06-15 22:01:27 UTC | #1

2D texture Facial expressions using Claire model from Mixamo.  Maybe some might find it useful.

Repo: https://github.com/Lumak/Urho3D-Claire

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9e88bc97fa2a5c35f04324cdfac4aff92a2a05c0.jpg[/img]

-------------------------

yushli1 | 2017-06-16 03:31:28 UTC | #2

Thank you for sharing this.

-------------------------

johnnycable | 2017-06-16 15:13:34 UTC | #3

Wonderful, this is exactly what I'm looking of! (Searching for various ways of doing facial animation...):slightly_smiling_face::slightly_smiling_face:
A couple of things I don't understand...
I guess this is UV animation... the spritesheet is juxtaposed on the girls face... the face is flat and this does the trick... is it?
1. the spritesheet is part of mixamo export? Or did you make it yourself?
2. why you do:
>     matEyes = matOrig->Clone();
>     matEyeBrows = matOrig->Clone();
>     matMouth = matOrig->Clone();
>     object->SetMaterial(0, matEyeBrows);
>     object->SetMaterial(1, matEyes);
>     object->SetMaterial(2, matMouth);

extracting material of geometry part for uv animation...? I tried to open the model with the editor, but I didn't find any material subdivision tied to the face of the model (anyway i had problem loading another composite model in the past, so i think it's me or the editor not showing material slots for body parts... in blender it's easier) 
UV animation is then done in update with, I guess:
>             eyesIdx_ = ++eyesIdx_ % eyesIdxMax_;
>             int row = eyesIdx_ % eyesMaxRows_;
>             int col = eyesIdx_ / eyesMaxRows_;
>             float u = (float)col * eyesCellWidth_;
>             float v = (float)row * cellHeight_;
>             matEyes->SetShaderParameter("UOffset", Vector4(1.0f, 0.0f, 0.0f, u));
>             matEyes->SetShaderParameter("VOffset", Vector4(0.0f, 1.0f, 0.0f, v));

and so on for every body part. But what's this in create scene?

>     // int uv indeces
>     eyesIdx_ = 0;
>     eyesIdxMax_ = 30;
>     eyesMaxRows_ = 10;

>     eyeBrowsIdx_ = 0;
>     eyeBrowsIdxMax_ = 10;

>     mouthIdx_ = 0;
>     mouthIdxMax_ = 30;
>     mouthMaxRows_ = 10;

>     // cell dims
>     cellWidth_ = 0.1f;
>     cellHeight_ = 0.1f;
>     eyesCellWidth_ = 0.2f;

looks like mapping the spritesheet...
Thank you so much for sharing!

-------------------------

Lumak | 2017-06-16 17:38:17 UTC | #4

A:
1 - came with the model
2 - right, you only need one material to render all three at once but because I have to change the uv offsets three separate cloned materials are required as not to affect the other uv offsets.
3 - I looked at the Girl01_FacialAnimMap.png and determined that there are 10x10 cells (size=0.1 x 0.1 ea) and eyes are 1x2 cells, other two 1x1 cells, and counted num expressions for each.

-------------------------

johnnycable | 2017-06-16 17:57:14 UTC | #5

I see. So 

            matMouth->SetShaderParameter("UOffset", Vector4(1.0f, 0.0f, 0.0f, u));
            matMouth->SetShaderParameter("VOffset", Vector4(0.0f, 1.0f, 0.0f, v));
maps the sprite in the spritesheet (u,v) over the material, and Vector4 tells (x=1, y=1, no z) the shader to set the sprite all over the material surface?

-------------------------

Lumak | 2017-06-16 18:18:54 UTC | #6

Yes, that's correct and z is not used in the shader.

-------------------------

johnnycable | 2017-06-16 18:31:20 UTC | #7

Very well. Thank you!

-------------------------

