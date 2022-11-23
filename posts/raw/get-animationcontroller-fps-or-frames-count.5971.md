Askhento | 2020-03-06 20:37:19 UTC | #1

I'have animated model and need to know how many frames in the track. I found AnimationController.GetLength() method which gives me seconds, but I need current frame.
In my example I get 1.3333 sec length and I know that track have 40 frames, which is equal to 30 fps. So does it mean that Urho always use this number?

-------------------------

Dave82 | 2020-03-08 19:28:04 UTC | #3

Since number of frames can vary for each bone (track) in the animation this data is not stored. Not to mention each time you add remove keyframes to an animation you should always recalculate this value...
If you need the num keyframes in the animation you could use : 

[code]
yourAnimatedModel->GetAnimationState("yourAnimationFileName")->GetAnimation()
->GetTrack("boneName")->GetNumKeyFrames();
[/code]

And check this for all bones in the animation file and store the highest value : 
[code]
int GetNumFrames(const String& animationName)
{
    int numFrames = 0;
    Animation * yourAnimation = yourAnimatedModel->GetAnimationState(animationName)->GetAnimation();
    for (int x = 0; x < yourAnimation->GetNumTracks(); x++)
    {
        int trackFrames = yourAnimation->GetTrack(x)->GetNumKeyFrames();
        if (trackFrames > numFrames)  numFrames = trackFrames;
    }
 return numFrames;
}
[/code]
Please note this will only work in a keyframe per frame situation only ! So if your bone has 2 frames , 1st at time 0 and 2nd at time 100 you should check the time of the last keyframe of the bones instead.

[code]
float lastKeyframeTime= yourAnimation->GetTrack(x)->GetKeyFrame(lastFrameId)->time_;
[/code]

-------------------------

Askhento | 2020-03-07 16:35:00 UTC | #4

Thanks!

So as I understand we only have keyframes not frames? 
For example is I will make a 360 rotation of bone with only 2 keyframes at first and last frames, and in blender the 250 frames is default. So the only thing I could get is duration and 2 keyframes, but not 250 frames?

-------------------------

Dave82 | 2020-03-07 19:31:57 UTC | #5

I don't know how blender exports animation data but i export my animations keyframe per frame. I guess blender exports keyframe per frame as well. If you make a 2 frame animation one at time 0 and one frame at 250 then most likely you will have 250 frames in your animation file. But maybe people will show up who actually use and know better the blender exporter than me.

-------------------------

