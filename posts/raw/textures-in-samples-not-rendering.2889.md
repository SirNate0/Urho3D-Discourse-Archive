bmcorser | 2017-03-17 19:51:37 UTC | #1

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a3df266e6999d5d7ff76ce0c52f96cd1288eb436.png" width="690" height="388">

There don't seem to be textures in this sample (see above) on a fresh build of 48a1f3dcddb4e5a29006b2264d29e7e8b9be4725

Are there some issues with high DPI? I managed to build and run samples on OSX, but that was Urho3D 1.5 I think.

Is there anything I can look at to debug?

Cheers,

Ben

-------------------------

bmcorser | 2017-03-17 19:12:37 UTC | #2

Damn I should have used the search before posting:
http://discourse.urho3d.io/t/linux-all-dds-textures-are-black/1268

Adding the `-gl2` switch when running the samples works for me.

-------------------------

