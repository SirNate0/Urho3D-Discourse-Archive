vivienneanthony | 2017-01-02 01:09:55 UTC | #1

Hi, 

I would like to create a preview view 3D editor in ImGui. I would have to somehow get the render output scene from the camera to a texture. Then point ImGui to the texture. Any thoughts or help appeciated.


I can then switch view modes for the preview easily also

Viv

-------------------------

thebluefish | 2017-01-02 01:09:55 UTC | #2

Any reason this isn't in [url=http://urho3d.prophpbb.com/forum8.html]Support[/url] or the existing Imgui discussion?

Your existing editor code, based off Scorvi's work and my small additions, demonstrates how to render a scene to the texture and then assign that texture to a UI element. You would essentially do the same, but assign the texture to Imgui's element instead.

-------------------------

vivienneanthony | 2017-01-02 01:09:55 UTC | #3

Ah. Actually I meant to ask in support.

If anyone can move this thread, please.

-------------------------

