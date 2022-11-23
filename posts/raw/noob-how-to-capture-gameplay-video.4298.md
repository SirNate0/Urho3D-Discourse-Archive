hhemken | 2019-11-07 08:44:41 UTC | #1

I just started making some test scenes in Urho3d for a visualization project.

Sorry to ask such a basic question, but I've searched this board and googled a variety of terms, but can't find the answer:

How do I capture gameplay audio and video from an Urho3d game to a video file on disk?

Thanks for your help and patience!

hhemken

-------------------------

hhemken | 2018-06-08 15:32:19 UTC | #2

BTW, I'm on Ubuntu 18.04 Linux

-------------------------

sirop | 2018-06-08 17:36:14 UTC | #3

As for video: you can capture each frame (snapshot)  similar to https://github.com/urho3d/Urho3D/blob/master/Source/Samples/Sample.inl#L341-L349
and then concatenate the snapshots with a tool like _ffmpeg_.

-------------------------

SirNate0 | 2018-06-08 19:18:23 UTC | #4

Google Ubuntu screen recorder and that will give you some options. I use simple screen recorder, personally.

-------------------------

slapin | 2018-06-09 09:25:14 UTC | #5

You will not be able to capture proper fullscreen in urho due to breakage. Use window. You can use standard tools like obs or ffmpeg or ffmpeg wrappers for actual capture.

-------------------------

TheComet | 2018-06-09 12:24:17 UTC | #6

I'm on linux and I use OBS for recording my desktop.

https://obsproject.com/download

-------------------------

1vanK | 2018-06-09 12:41:46 UTC | #7

I agree OBS best and universal solution

-------------------------

WangKai | 2018-06-10 12:40:58 UTC | #8

A cheap hardware device should be better :stuck_out_tongue:  ![capture_device|500x500](upload://1aeNO6hTaRAtbo7iv84bVsYnSiM.jpg)

-------------------------

Modanung | 2018-06-10 14:45:00 UTC | #9

OBS is great when you want to layer things as you record or broadcast. To just capture footage I prefer [SimpleScreenRecorder](https://en.wikipedia.org/wiki/SimpleScreenRecorder) though.
For the best result you'll probably want to go with @WangKai's solution.

-------------------------

TrevorCash | 2019-05-08 16:16:45 UTC | #10

The Xbox app on windows works well for me.

-------------------------

Leith | 2019-05-09 10:54:02 UTC | #11

The industry standard in gamedev is generally accepted to be "bink", but I also use SimpleScreenRecorder on Linux.

-------------------------

