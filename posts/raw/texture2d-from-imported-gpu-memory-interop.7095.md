ange | 2021-12-09 10:52:31 UTC | #1

Hi all. I would like to construct a Texture2D (to be used as a render target) that uses GPU memory which has already been allocated by some other API (Vulkan in my case). It is relatively simple to do with a few raw OpenGl calls like: glGenTextures, glCreateMemoryObjectsEXT, glImportMemory***EXT. I suppose it is not so hard to do with D3D either.

I can see that Texture2D inherits from GPUObject which provides GetGPUObjectName() for OpenGl and GetGPUObject() for D3D. So the underlying memory seems to be not so far away under the hood. A perfect solution would be some new Texture2D constructors taking a texture handle (Gluint or void* for D3D).

Is there any work done to allow such interoperability ?
If not, is it a lot of work ?
What would be the main steps to implement it in Urho3D ?
Is there any predictable issues head ?

Thanks a lot.

-------------------------

Eugene | 2021-12-09 11:30:57 UTC | #2

[quote="ange, post:1, topic:7095"]
Is there any work done to allow such interoperability ?
[/quote]
Nope. Somewhat similar approach used to connect Urho3D app to existing window, but it won't help in your specific case.

[quote="ange, post:1, topic:7095"]
If not, is it a lot of work ?
[/quote]
If you just want something that works, nope. A day of work?

[quote="ange, post:1, topic:7095"]
What would be the main steps to implement it in Urho3D ?
[/quote]
Make a public function for Texture2D and just do your magic there.

[quote="ange, post:1, topic:7095"]
Is there any predictable issues head ?
[/quote]
Watch for resource destruction. You should either keep Texture2D responsible for resource deletion (no need for extra work) or manage it manually (you will need separate flag in Texture2D to prevent deletion then).

Watch for resource invalidation on context loss. You will need to manually handle it and recreate your stuff there.

-------------------------

ange | 2021-12-09 11:40:22 UTC | #3

Hi Eugene, thanks for the quick reply. I am no expert in that field, but you seems to be confident about this not requiring to much work, so I will give it a try ;)
Thanks again !

-------------------------

ange | 2021-12-13 14:12:52 UTC | #4

It was indeed easy to get it work. For now I just did a rough draft, if someone is interested:
https://github.com/ange63/Urho3D/commit/4c01dbdf08f15503b59a0d5935c5c440b8a9afc1
If I have the time I will make something cleaner.
Thanks for the support.

-------------------------

SirNate0 | 2021-12-13 15:24:56 UTC | #5

I'm glad you got it working! I added a few comments to your code - I don't think your code would compile for D3D as you seem to have an undefined `hr` variable. You should probably just use `URHO3D_LOGERROR` instead of `URHO3D_LOGD3DERROR`.

Additionally, what is the purpose of `bool Texture2D::Import()`? Why not just have `bool Texture2D::SetData(unsigned handle, int width, int height, unsigned format, TextureUsage usage, int multiSample, bool autoResolve)` deal with all the import behavior?

-------------------------

ange | 2021-12-13 15:40:35 UTC | #6

I missed the hr variable, thanks. I did not run the code on Windows yet :sweat_smile:

About Import(), I tried to match how SetSize(...) and Create() was built. It seemed to me that the split was making sense.

Anyway this is a very rough draft, context loss is not handled and I saw things about compressed textures I know nothing about so I let that aside for now.

-------------------------

