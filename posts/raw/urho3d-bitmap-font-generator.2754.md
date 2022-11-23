1vanK | 2017-01-28 15:29:22 UTC | #1

  https://github.com/1vanK/Urho3DBitmapFontGenerator

In the beginning, I just wanted to make a sprite font generator for https://github.com/1vanK/Urho3DSpriteBatch but after it I added a SDF generator also.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ea70529e9eb3eaa1b6ca9ba5364af98c9ee5f323.png" width="690" height="482">

1) Press "Pick Font..." and select font (You can type c:\windows\fonts in path and use system fonts)
2) Press "Generate"
3) Press "Save"

P.S.

SDF fonts render with large scale and after it downscaled to required size. You can decrease "Scale" parameter for fast generation or increase for improve quality

SDF generator uses true brutforce on GPU for maximal quality, so it compiled only for OpenGL

Do not use large radius for thin fonts: stroke effect will look bad

-------------------------

1vanK | 2017-01-30 18:06:35 UTC | #2

SpriteBatch updated for latest version of engine. also added some examples:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/f1f61cbb85400f55c39ec3c4e360f9828edcb6bd.png" width="222" height="91">

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/046e52fa379cc45733a710cb41fab67609d2d919.png" width="250" height="86">

-------------------------

