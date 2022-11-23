vivienneanthony | 2017-04-28 19:17:04 UTC | #1

Have anyone tried implementing render output to images? Meaning something.

Camera::OutputStreamFile(filename, fps)

Or similiar using render

-------------------------

Enhex | 2017-04-28 21:15:21 UTC | #2

What's your use case? Seems like you want to record a video?

-------------------------

vivienneanthony | 2017-04-28 22:06:18 UTC | #3

Rudimentary images that can easily merge with a video editing program. Im assuming anything with a skybox would have a full image, then something without a transparent background unless specified full.

-------------------------

Enhex | 2017-04-29 07:20:21 UTC | #4

There's [Graphics::TakeScreenShot()](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_graphics.html#aba8bc69f7cae9251dbf3dc99d771ed30).

In case you just want to record a video, why not use external video recording software?

-------------------------

