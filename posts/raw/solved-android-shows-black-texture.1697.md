victorfence | 2017-01-02 01:09:33 UTC | #1

Hello Everyone,

One of my android device shows black texture, even BorderImage of UI shows black rectangle.
After digging in google, someone using unity met the same problem said this may fixed by set ant-aliasing off. 
[url]http://forum.unity3d.com/threads/black-textures-on-some-devices-android-versions.195328/[/url]

I wonder if the similar thing caused the problem in urho3d? any hints? thanks a lot.

-------------------------

rasteron | 2017-01-02 01:09:33 UTC | #2

Yes it does seem to happen to Urho3D as well with shaders which points to shader errors or if the feature is not supported (in GLES, i think). I had a similar encounter and discussed it here [topic1189.html?hilit=black#p7806](http://discourse.urho3d.io/t/iterative-parallax-mapping-shader/1151/7)

-------------------------

victorfence | 2017-01-02 01:09:36 UTC | #3

[quote="rasteron"]Yes it does seem to happen to Urho3D as well with shaders which points to shader errors or if the feature is not supported (in GLES, i think). I had a similar encounter and discussed it here [topic1189.html?hilit=black#p7806](http://discourse.urho3d.io/t/iterative-parallax-mapping-shader/1151/7)[/quote]

Thanks for reply, but I did not create my own material, even the texture of defalut material shows black color.

How can I solve this kind of problem?  Maybe hard?

-------------------------

rasteron | 2017-01-02 01:09:36 UTC | #4

[quote="victorfence"][quote="rasteron"]Yes it does seem to happen to Urho3D as well with shaders which points to shader errors or if the feature is not supported (in GLES, i think). I had a similar encounter and discussed it here [topic1189.html?hilit=black#p7806](http://discourse.urho3d.io/t/iterative-parallax-mapping-shader/1151/7)[/quote]

Thanks for reply, but I did not create my own material, even the texture of defalut material shows black color.

How can I solve this kind of problem?  Maybe hard?[/quote]

I see and this could be an issue. Are you using the latest Urho3D version? You could post your game project apk and android hardware specs or emulator details for reference.

-------------------------

victorfence | 2017-01-02 01:09:39 UTC | #5

[quote="rasteron"]
I see and this could be an issue. Are you using the latest Urho3D version? You could post your game project apk and android hardware specs or emulator details for reference.[/quote]

Hi Rasteron, 

I use latest version of urho3d from github.

sorry for I can't upload my project and device details very soon because I am not skilled for this (I'll try it).

And I found a new hint, I saw the textures when I assign textures using dds images to material instead png file (I use png textures before).

I think this is a important hint, can you take a look about this? thanks!

[color=#008040]
Update:
I found new hint, the real reason dds image works is because it in size of 256?256, 512?512, etc. [/color]

-------------------------

thebluefish | 2017-01-02 01:09:39 UTC | #6

OpenGL ES 2.0 and earlier require textures to be a power-of-2. There is an extension available that would allow these, but it is not available on every device and thus limits compatibility options. GL ES 3.0+ does not have this requirement, but Urho3D is not yet compatible with GL ES 3.0.

-------------------------

victorfence | 2017-01-02 01:09:40 UTC | #7

[quote="thebluefish"]OpenGL ES 2.0 and earlier require textures to be a power-of-2. There is an extension available that would allow these, but it is not available on every device and thus limits compatibility options. GL ES 3.0+ does not have this requirement, but Urho3D is not yet compatible with GL ES 3.0.[/quote]

Thanks for explaination, glade to know more about urho3d and OpenGl ES :slight_smile:

-------------------------

