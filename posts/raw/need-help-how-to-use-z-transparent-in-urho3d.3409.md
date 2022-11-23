chenjie199234 | 2019-05-23 13:20:01 UTC | #1

In diffnormal,there is no z transparent.
I want to import a tree into my scene,the leaf in blender is right,but it is wrong in Urho3D.

![wrong|492x499](upload://3vf1Aw0iVvLCnnBEkjPMcjTb2Qh.png)

-------------------------

Modanung | 2017-08-02 08:47:14 UTC | #2

The technique DiffNormalSpec does not support alpha.Try replacing it by DiffNormalSpecAlpha.

And welcome to the forums! :slight_smile:

----------

As a more general question: What happened to the _AlphaMask_ techniques? And how could one recreated them?

-------------------------

Mike | 2017-08-02 08:58:41 UTC | #3

If the Blender exporter did not pick the right technique (assuming you're using the addon), then your settings are not as expected by the exporter.

Ensure that 'Transparency' is enabled in Blender's Material panel and optionally check 'Mask' if need be.

-------------------------

1vanK | 2017-08-02 08:58:00 UTC | #4

Do not use Alpha for leaves (alpha required sorting - slow perfomance and errors for densely located objects) only AlphaMask

-------------------------

Mike | 2017-08-02 09:07:21 UTC | #5

'ALPHAMASK' is now a psdefines

See [here](https://github.com/urho3d/Urho3D/commit/48f779e234b4cf6f2429e1456935412731950ef8)

-------------------------

Mike | 2017-08-02 09:01:05 UTC | #6

Sorry for typo, I intended to say 'Mask' (instead of default 'Z Transparency').

-------------------------

chenjie199234 | 2019-05-23 13:20:01 UTC | #7

What is this in blender!
If i use the Z Transparency in blender,then it is ok.
If i dont use the Z Transparency in blender,then it is wrong.
![image|690x367](upload://jT8OmgscxJMAOCSY7Yqu7TzYWp2.jpg)

-------------------------

Modanung | 2019-05-23 13:20:01 UTC | #8

![image|622x52](upload://7qNZpP4FMHEns4dHIDnc7MtNB6i.png)

-------------------------

Mike | 2017-08-02 10:01:44 UTC | #9

Checking 'Transparency' in Blender is the way to tell the exporter that you want to use transparency.

Checking 'Mask' in Blender is the way to tell the exporter that you want to use alpha mask instead of Z transparency ('Raytrace' is not supported).

Maybe this info is missing in the guide.

-------------------------

Mike | 2017-08-02 10:19:01 UTC | #10

BTW, are you using the [Blender exporter](https://github.com/reattiva/Urho3D-Blender) or not ?

-------------------------

