UrhoIsTheBest | 2020-01-15 06:29:01 UTC | #1

I use Blender plugin to export animation into Urho3d type. But I found all my imported animations have an extra last key frame, which is exactly identical duplicate as the 2nd last frame.

For example, I have an animation with 51 key frames in Blender.
I loaded that resource file into animation with
```c++
  auto* animation = cache->GetResource<Animation>("Models/MB/attacks_single_lefttoright.ani");
  DebugTrack(*animation->GetTrack(String("abdomen")));
```
where the `DebugTrack` function is:
```c++
void DebugTrack(const AnimationTrack& track) {
  PrintLine("animation track: " + track.name_);
  for (int i = 0; i < track.keyFrames_.Size(); ++i) {
    PrintLine("key frame " + String(i) + " pos: " + track.keyFrames_.At(i).position_.ToString() + ", rot: " + track.keyFrames_.At(i).rotation_.ToString());
  }
}
```
I see the following result:
```
animation track: abdomen
key frame 0 pos: 0.047244 0.817212 -0.121344, rot: 0.719543 0.0866898 0.0628616 0.686142
key frame 1 pos: 0.049948 0.814553 -0.123273, rot: 0.718406 0.0579996 0.0458512 0.691684
key frame 2 pos: 0.05383 0.81108 -0.127207, rot: 0.715048 0.0373502 0.0348826 0.697205
key frame 3 pos: 0.058338 0.806711 -0.131129, rot: 0.711603 0.0235224 0.0302292 0.701537
key frame 4 pos: 0.062191 0.802427 -0.133876, rot: 0.71112 0.0182607 0.0345174 0.701985
key frame 5 pos: 0.066442 0.798546 -0.134944, rot: 0.711619 0.0205478 0.039172 0.701171
...
key frame 47 pos: 0.031947 0.843907 -0.147635, rot: 0.672488 0.23856 0.221741 0.66459
key frame 48 pos: 0.037744 0.842606 -0.156338, rot: 0.673297 0.235059 0.220076 0.665571
key frame 49 pos: 0.040926 0.841488 -0.162534, rot: 0.674536 0.232992 0.219924 0.665093
key frame 50 pos: 0.043037 0.840866 -0.166271, rot: 0.674937 0.232295 0.222164 0.664185
key frame 51 pos: 0.043037 0.840866 -0.166271, rot: 0.674937 0.232295 0.222164 0.664185
```

The last two key frames are exactly identical! And there are 0-51 = 52 total key frames (extra one).

Is this a problem in Urho3d or a problem of the Blender plugin?

-------------------------

JTippetts | 2020-01-16 06:13:00 UTC | #2

Try un-ticking the check box in the exporter menu in Blender that is labeled "Ending extra frame".

-------------------------

UrhoIsTheBest | 2020-01-16 06:12:58 UTC | #3

Thanks for reminding! I think that's the reason. Although I still don't understand why the duplicate keyframe is the last one, while it should duplicate the first keyframe according to [Blender plugin doc](https://github.com/reattiva/Urho3D-Blender/blob/master/guide.txt). But anyway, it's a plugin issue.

-------------------------

Modanung | 2020-01-16 12:07:11 UTC | #4

[quote="UrhoIsTheBest, post:3, topic:5818"]
...while it should duplicate the first keyframe according to [Blender plugin doc](https://github.com/reattiva/Urho3D-Blender/blob/master/guide.txt).
[/quote]
That's not how I read it.

-------------------------

SirNate0 | 2020-01-16 14:17:08 UTC | #5

I agree that technically the plugin doc doesn't state that it is the first frame that the track is extended with, but for it to be a useful feature I would argue that it is probably a bug and that it should be the first frame. Assuming that it is one of the forms of animations that the feature was created for (timeline and NLA-Tracks?).

-------------------------

JTippetts1 | 2020-01-16 21:17:56 UTC | #6

The way I read it, it's intended for looping animations where the first and last key frames in blender are identical, so in that use case it hardly matters.

-------------------------

SirNate0 | 2020-01-17 03:49:37 UTC | #7

I could be misunderstanding, but as I read it the purpose is to add the keyframe that Urho requires but blender doesn't. For example, assuming we want a looking sequence `12321232123212...`, blender wants the animation frames to be `1232`, while Urho wants `12321`. If the behavior described above was the result in the plug-in, we get `12322` in Urho, which would be wrong. I also haven't worked with the animation stuff for a year or two, so I could be completely wrong...

-------------------------

Modanung | 2020-01-18 13:19:50 UTC | #8

I'd say it's more like `1234(5)` where `1 == 5` for looping animations, in which case you would _not_ want the "extra frame" in order to avoid a jagged animation cycle.

-------------------------

