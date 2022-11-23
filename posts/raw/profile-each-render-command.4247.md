Unick | 2018-05-21 16:46:09 UTC | #1

I want to profile my render in my code (without external profiles). Ideally, i want to know how many time takes rendering of each object or each render command. I found Profile class but looks like it is useful to profile separate functions and CPU code. 
But i can insert command event after each render command:

`<command type="sendevent" name="profile" tag="profile" />`

I will catch it and save time between commands. But GPU works async and this time will not be the render time of the command. I can insert GPU sync (like glFinish) to get correct time value. Is there better way or maybe Urho3D already has good rendering profile?

-------------------------

Eugene | 2018-05-21 17:20:28 UTC | #2

GPU profiling isn't easy. It's better to use 3rdparty tools or play with enabling and disabling features.

On the other hand, Unity and UE4 somehow do it...
https://docs.unity3d.com/Manual/ProfilerGPU.html
http://reedbeta.com/blog/gpu-profiling-101/
Maybe it's possible to do the same thing here.

-------------------------

