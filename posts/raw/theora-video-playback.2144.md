codingmonkey | 2017-10-31 21:11:08 UTC | #1

Hi folks!
There is my adaptation for Urho3D of the Orange's example with Theora playback on textures 

github.com/MonkeyFirst/Urho3DTheora/

https://www.youtube.com/watch?v=Wap1Ye5-qsY

* previous CPU color decoding was removed
* last version have only OpenGL shader for GPU color decoding

-------------------------

sabotage3d | 2017-01-02 01:13:27 UTC | #2

Nice work. I am thinking of doing the same for OpenCV.

-------------------------

Modanung | 2017-01-02 01:13:27 UTC | #3

Cool! :smiley:

-------------------------

Mike | 2017-01-02 01:13:27 UTC | #4

Awesome  :stuck_out_tongue:

-------------------------

codingmonkey | 2020-02-16 02:40:05 UTC | #5

Thanks )
I guess it still working only for the one movie, that i testing. So there are a lot of work in future 

[quote]
I am thinking of doing the same for OpenCV.
[/quote]
computer vison + urho3d you mean? for what ?

-------------------------

Enhex | 2017-01-02 01:13:27 UTC | #6

Nice work.
Could be very useful for games, playing intro's, cut-scenes, and such.

-------------------------

codingmonkey | 2017-01-02 01:13:28 UTC | #7

[quote]Could be very useful for games, playing intro's, cut-scenes, and such.[/quote]
Yes, that's is common case of usage.

Previously I'm also locking on FFmpeg, but i suppose it has bad licence for urho3d ? (GPL)

Theora has BSD licence

-------------------------

TheSHEEEP | 2017-01-02 01:13:30 UTC | #8

FFmpeg itself is LGPL, which is fine as long as you link dynamically.
Some libraries that FFmpeg can be built with (most known, x264) are GPL licensed.
But if you have full control of assets, there is no reason not to use OGG video / theora instead.

-------------------------

miz | 2017-01-02 01:15:30 UTC | #9

Firstly, nice work!

Secondly, I'm trying to make this work in a BorderImage but having trouble converting properly to RGB from YUV. Any idea how i could do this? At the moment I've got the black and white from the Y element of the video displaying on a BorderImage by doing:

[code]((BorderImage*)GetSubsystem<UI>()->GetRoot()->GetChild(String("tvwindow"))->GetChild(String("tv Y")))->SetTexture(outputTexture[i])[/code]

At the bottom of UpdatePlaneTextures(). This works. (I've taken away the code that renders it to a material in the scene)

-------------------------

Lumak | 2020-01-25 20:30:39 UTC | #10

Awesome work! Finally getting around to testing this and the video works great but missing sound.

edit: maybe it's not supposed to have audio?

-------------------------

Lumak | 2020-02-16 01:39:55 UTC | #11

Playing audio using Urho3D's BufferedStreamAudio:
https://youtu.be/0GCDoQaBR4I

-------------------------

Dave82 | 2020-02-16 23:21:20 UTC | #12

Excellent work !This would be a nice addon for Urho3d ! Do you plan to make it open source ?

-------------------------

Lumak | 2020-02-17 01:27:21 UTC | #13

The video/audio player that you see is literally this example, https://github.com/Lumak/Urho3D-Theora/blob/master/Source/ThirdParty/libtheora/examples/player_example.c in the repo.
Instead of using AUDIO_DEVICE and ioctrl fns, use the BufferedStreamAudio, the video conversion from yuv420 to rgba is already there. I'm still having trouble with audio synchronization, as you can hear some skipping in the video, and studying the process.

-------------------------

Lumak | 2020-02-18 02:53:11 UTC | #14

Audio should be in sync now, https://github.com/Lumak/Urho3D-Theora

-------------------------

Dave82 | 2020-03-05 20:57:21 UTC | #15

Just found some time to test it ! Works perfectly ! Even CPU decoding is really fast (No serious impact on CPU usage).

Excellent work ! Thank you !
Definitely will use this for my cutscenes !

-------------------------

Dave82 | 2020-03-06 17:18:26 UTC | #16

I found a small issue with the player. If i run the app in windowed mode and the window loses focus the video and audio start going out of sync the audio starts to crackle and the video just freezes randomly. (the same issue as in your video)
Also limiting the fps affects the video playback speed which makes sense but is there any solution to run updates independently of fps ? Maybe the whole update procedure should be in an other thread ?

The cpu usage is below 20% while playing the video so its not a hardware issue

EDIT : Tried it with my own video (1280 * 768) and even with maximum fps the audio goes out of sync after 7-8 seconds...

-------------------------

Pencheff | 2020-03-06 19:05:21 UTC | #17

Looking at the code, I think HandleUpdate() should do multiple UpdateTheora() calls until decoding is up to date with latest possible data. I would recommend doing the decoding in separate thread and signaling the main thread when a video/audio frame data is ready, then doing texture blit on the main thread.

-------------------------

Lumak | 2020-03-07 00:41:46 UTC | #18

At the bottom of the UpdateTheora() fn, there's a loop correction section:
```
      // correction loops
      // note: audioTime_ will remain negative (-1000) until vorbis actually acquires a vorbis packet
      audioOffset = audioTime_ - elapsedTime_;

      if (audioOffset < 0)
      {
          if (++numLoops > MAX_CORRECTIVE_LOOPS)
          {
              break;
          }
      }
      else
      {
          break;
      }
```
Check the audioOffset and see how far it lags behind, and instead of using MAX_CORRECTIVE_LOOPS, you might consider a fixed desirable offset value.

Pseudo code might look something like:
```
      if (audioTime_ != -1000LL && audioOffset < -5LL)
         then continue looping
     else
        break
```

-------------------------

Lumak | 2020-03-07 01:06:32 UTC | #19

Updated the repo with the corrective audio loop fix.

-------------------------

Dave82 | 2020-06-01 22:30:57 UTC | #20

I turned Vsync on and it totally ruined the playback (extreme stuttering and frame freezes)... 
Seems it really needs a separate thread for decoding.

-------------------------

Lumak | 2020-06-02 00:10:09 UTC | #21

That's something that I didn't test. I'll take a look at it soon.

-------------------------

Dave82 | 2020-06-22 22:37:03 UTC | #22

Any news about this ? Just found some info about similar issues in Unity. Maybe it helps.
https://answers.unity.com/questions/119236/jerky-fullscreen-video-playback.html

-------------------------

Dave82 | 2020-07-06 18:10:38 UTC | #23

Tried to convert some cutscenes to ogv and the videoplayer can't play them (crash at entering the decode loop)... Tried literally all possible settings (kbit/sec / audio format , bitrate etc) in free ogv video converter and all settings result in crash... i suspect there's something wrong with the audio but right now i'm just need to calm down because otherwise  i'll pull my hair out...
Also started to write my own ffmpeg player but building that crap on windows is so ridiculously convoluted 
 that it just doesn't worth the time and energy to fiddle with a bloated mess like that.

Situations like these can turn the wonderful world of "open sourceness" into a smelly devastated landfill...
Just giving few more tries and if it doesn't work i will try to switch to a Windows only solution where i can at least step over this make|rake|cmake|download this tool|install package | install another package | set home environment | download a library which after you build will download another library that is required to build the 3rd library...

Time for coffee and beer.

-------------------------

Lumak | 2020-12-19 16:23:26 UTC | #24

I'm on my Christmas break now and decided to tackle some unfinished projects, starting with this one since I promised to do it.

I created another theora video using VLC (ffmpeg didn't work), and here's the sample video.
https://www.youtube.com/watch?v=mCp-i4PB9us&feature=youtu.be

I'll update the repo shortly.

-------------------------

Bluemoon | 2020-12-19 16:48:51 UTC | #25

I don't know which to comment on; the fact that this works or the awesome drummer :smile:

Okay back on point, this is amazing.

-------------------------

Batch | 2022-03-02 22:44:50 UTC | #26

I played around with this and it works well, but I'm having trouble determining when playback is complete. Does anyone know how to go about doing that? I tried implementing cutscenes with it, but I didn't know when to remove the UI elements that were rendering it.

-------------------------

