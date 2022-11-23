BananaIguana | 2017-01-02 01:09:37 UTC | #1

I'm trying to port an old iOS game across to Urho3D to make it multi-platform.

One thing I need to hook into is the mobile device orientation. On iOS it's 'UIDeviceOrientation' or 'UIInterfaceOrientation'. Does Urho3D offer a way to hook in to events where these values change in a platform independent way?

-------------------------

rasteron | 2017-01-02 01:09:37 UTC | #2

Hey BananaIguana,

Welcome to the forums :slight_smile:

I'm not sure about cross-platform so it looks like it only supports iOS atm:

[code]
SetOrientations (const String &orientations)
Set allowed screen orientations as a space-separated list of "LandscapeLeft", "LandscapeRight", "Portrait" and "PortraitUpsideDown". Affects currently only iOS platform. 
[/code]

Reference link:
[urho3d.github.io/documentation/1 ... ab796d09bb](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_graphics.html#ab376231d9cf6828eb33cc1ab796d09bb)

-------------------------

cadaver | 2017-01-02 01:09:41 UTC | #3

For Android you would control the allowed orientations through the app manifest, I believe.

Getting the current orientation depends on whether SDL supports it. Haven't looked into it myself. Typical hack way would be to detect whether current screen width is greater than height, but it doesn't tell the difference between LandscapeLeft & LandscapeRight for instance.

-------------------------

BananaIguana | 2017-01-02 01:09:42 UTC | #4

Thanks for the info all.

I've had a good look into this now and it seems I can hack it quite easily. The downside is that I just have to specifics per-platform.

I'm loving Urho3D so far :wink:

-------------------------

majhong | 2020-01-06 12:08:53 UTC | #5

```
void VideoChat::Setup()
{
    // Modify engine startup parameters
    Sample::Setup();
    engineParameters_[EP_SOUND] = true;
    engineParameters_[EP_ORIENTATIONS] = "Portrait";
}
```
hi!
it work on android

-------------------------

