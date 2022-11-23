practicing01 | 2017-01-02 01:02:03 UTC | #1

[google.com/get/cardboard/](https://www.google.com/get/cardboard/)

I don't have one so I don't know how well it works but I do have a Nintendo 3DS and if it looks somewhat like that I would love to buy one.  How difficult would it be to add support for it (it's an android sdk)?

-------------------------

aster2013 | 2017-01-02 01:02:03 UTC | #2

It is just a toy.

-------------------------

weitjong | 2017-01-02 01:02:03 UTC | #3

It does not work like a Nintendo 3DS. It is more like a poor-man version of Oculus Rift VR kit. I have tested to install the demo app into my Galaxy Tab 3 and I can swear I could fool my eyes to see images in actual 3D by putting my Tab 3 close to my face minus the cardboard. :laughing:  Actually the most crucial thing is the lenses on the cardboard. Without them, the image from the demo is hard to focus on. To support it, your app needs to be able to render two split viewports (one for each eye). It also needs post-processing to correct the lens distortion (assuming you want to test the app on the cardboard with lenses on). I believe the SDK provides a library to perform this lens distortion correction, however, I am not sure whether it is easier to integrate that or just use a custom post-processing effect in Urho3D renderpath.

-------------------------

thebluefish | 2017-01-02 01:02:30 UTC | #4

[quote="weitjong"]I believe the SDK provides a library to perform this lens distortion correction, however, I am not sure whether it is easier to integrate that or just use a custom post-processing effect in Urho3D renderpath.[/quote]

The Android SDK provides a DistortionRenderer which provides automatic correction. We would have to ensure the parameters are set properly and be able to call the appropriate Java code with our OpenGL context. Otherwise Urho3D-specific support would be preferred.

-------------------------

