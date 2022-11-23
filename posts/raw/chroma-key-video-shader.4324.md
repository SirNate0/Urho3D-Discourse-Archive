robyava | 2018-06-16 15:07:18 UTC | #1

Hi,
I'm trying to develop a shader (glsl) for Chroma Key (green screen) video player on a Urho3D Texture2D. Could you please give some advice about or a example inside Urho3D GitHub samples? 
Thanks
Regards
Roberto Avanzi

-------------------------

jmiller | 2018-06-19 10:42:30 UTC | #2

Hello Roberto, and welcome to the forum!

There have been a few informative threads on video streaming:
  https://discourse.urho3d.io/search?q=streaming+texture2d

Perhaps 10_RenderToTexture is not a bad sample to study? most are similar.

-------------------------

robyava | 2018-06-19 13:38:34 UTC | #3

Hello Justine,
yes, I'm started from RenderToTexture example for our video player implementation, thank you very much for your suggest. At this time, I've got  a chromaKey shader, starting from LitSolid.glsl prefab shader and introducing the green screen removing logic.
But my iOS app is frequently killed from a CPU Usage watchdog...
I've following advices from this topic https://github.com/urho3d/Urho3D/issues/578 without success.
I would like to ask another question: it is possible that at each InvokeOnMain or InvokeOnMainAsync called outside the onUpdate callback a new rendering thread is started?

Regards
Roberto

-------------------------

jmiller | 2018-06-20 07:59:44 UTC | #4

CPU:  Engine::SetMaxFps() or similar is suggested in that issues thread, but I guess you have tried?
 https://urho3d.github.io/documentation/HEAD/_main_loop.html#MainLoop_ApplicationState
Someone must be more familiar with InvokeOnMain() than I. :)

Regards

-------------------------

