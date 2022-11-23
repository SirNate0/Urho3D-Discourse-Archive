scaled | 2021-05-16 14:08:08 UTC | #1

I'm trying to integrate Urho3D into OBS Studio. I originally planned to render to a texture and send it to OBS Studio, but everything went wrong.
First, I didn't find a method to export the texture from Urho3D to render to an external application.
Secondly, it turned out that I can render directly in OBS Studio, but it works very strange and I do not know why or how to fix it.

What Urho3D must render:
`Urho3D Expected.gif`
What was expected:
`OBS Expected.png`
What i got somehow (just flashing background from Urho3D):
`OBS Result.png`
(Sorry, new users can attach only 2 links in the post)
https://github.com/scaledteam/Urho3D-plugin-for-OBS-Studio/tree/main/Images

I created the Urho3DModule class based on the Urho3D::Object class and created functions for initializing and rendering frames on command.
Inside the plugin code, I initialize Urho3D outside of the OBS Studio OpenGL context:
```
vtb->context = (new Urho3D::Context());
vtb->myApp = new Urho3DModule(vtb->context, NULL);
vtb->myApp->Setup();
vtb->MyApp->Start ();
```
Then I call a function that renders the image inside the OBS Studio OpenGL context of OBS Studio:
```
spv->myApp->UrhoFrame();
```
In total, I get an empty Urho3D window and a blinking background from Urho3D (the blinking background is intended), but there are no 3d objects. Other initialization combinations (initialize only inside the opengl context or partially) give a segmentation error or no image inside OBS Studio, just in Urho3D window.

I attach a repository with my code. Please help me figure out why it worked at all, and how to do it properly.

https://github.com/scaledteam/Urho3D-plugin-for-OBS-Studio

-------------------------

Eugene | 2021-05-16 21:51:23 UTC | #2

How exactly do you combine two renderers? Do they use the same context, or use separate shared contexts?

-------------------------

scaled | 2021-05-17 05:46:34 UTC | #3

I don't know, probably same context. I was very surprised when urho3d background color just appeared in OBS Studio. It also updating, but without 3d objects. I tried to create renderpath xml file without "clean" step, or edit clean color. It works outside OBS Studio, but inside OBS Studio it just ignored. You probably notice on screenshots that objects behind Urho3D on OBS scene just disappeared.

In OBS Studio plugin code you can draw textures or other objects using API or OpenGL commands (i didn't tried OpenGL commands). I initialised Urho3D in `obs_source_info.create` function, that don't entered in graphics context by default, and run `engine_->RunFrame();` inside `obs_source_info.video_render` function, which entered in graphics context by default. It even initialized Urho3D window, but it renders into OBS Studio window.

<https://obsproject.com/docs/graphics.html> 
Using graphics functions isn’t possible unless the current thread has entered a graphics context, and the graphics context can only be used by one thread at a time. To enter the graphics context, use obs_enter_graphics(), and to leave the graphics context, use obs_leave_graphics().

Certain callback will automatically be within the graphics context: obs_source_info.video_render, and the draw callback parameter of obs_display_add_draw_callback(), and obs_add_main_render_callback().

-------------------------

Eugene | 2021-05-18 07:16:28 UTC | #4

If you use same context for OBS and Urho3D rendering, you have to make sure that 100% of OpenGL state is preserved inbetween frames, i.e. Gl context setup is the same when Urho frame finished and when next frame begins.

-------------------------

scaled | 2021-05-18 07:37:48 UTC | #5

It sounds very complex. I don't understand why this works, so maybe I should try rendering to a texture? Are there any methods to make Urho3D render only to the texture, without its own window? I've seen different examples of rendering to a texture, but none of them allowed it to be exported outside of Urho3D.

-------------------------

Eugene | 2021-05-18 07:46:10 UTC | #6

[quote="scaled, post:5, topic:6849"]
It sounds very complex
[/quote]
It is quite complex, but not overly so. E.g. it is done by ImGUI to allow easy integration into existing apps w/o changing their code:
https://github.com/ocornut/imgui/blob/master/backends/imgui_impl_opengl3.cpp#L329

[quote="scaled, post:5, topic:6849"]
maybe I should try rendering to a texture?
[/quote]
Unless you somehow use two spearate OpenGL contexts, render to texture will not help you.

[quote="scaled, post:5, topic:6849"]
Are there any methods to make Urho3D render only to the texture, without its own window?
[/quote]
Use "external window" feature and make this external window invisible, I guess.

-------------------------

scaled | 2021-05-18 07:53:29 UTC | #7

I can use 2 separate OpenGL contexts. I can launch Urho3D app in thread with it own window, and Urho3D app can me controlled by OBS Studio. But i don't know, how to link Urho3D::Texture class and and gs_texture_t class from OBS Studio. Live2D plugin do it using pointer and linesize (texture pitch), but i don't see anything similar into Urho3D Texture class.

https://github.com/a1928370421/Obs-Live2D-Plugin/blob/master/VtuberPlugin.cpp#L84

-------------------------

Eugene | 2021-05-18 08:13:42 UTC | #8

Urho exposes internal OpenGL texture id.

If you cannot use it in OBS-thingy directly, you can try to create two textures (Urho one and OBS one) and copy it on GPU in OBS thread. It won't be a problem if you run it in desktop app.

But if these textures are in different threads, it may be challenging to synchronize.
You cannot use _one_ dynamic texture in two threads anyway.

-------------------------

scaled | 2021-05-18 08:27:18 UTC | #9

I thought it would be much easier =) Thank you very much, I will explore this issue further.

-------------------------

Eugene | 2021-05-18 09:07:50 UTC | #10

If I were you I would have gone ImGUI-way with one extra texture copy.
I don't think you will manage three-way synchronization "Urho Thread ~ OBS Thread ~ GPU".

-------------------------

scaled | 2021-05-18 09:33:30 UTC | #11

Also, why it was so easy to draw Urho3D background into OBS Studio? Why after engine initialization it starts to render inside OBS Studio, not in Urho3D window?
And why it ignoring my renderpath, which works perfectly outside OBS Studio?

-------------------------

Eugene | 2021-05-18 09:37:41 UTC | #12

Current OpenGL context (which defines _where_ to render) is global thread-local entity. Since Urho doesn't explictly reset current context to its own, it works with current one. And the current one is apparently OBS context.

-------------------------

Eugene | 2021-05-18 09:40:31 UTC | #13

[quote="scaled, post:11, topic:6849"]
And why it ignoring my renderpath, which works perfectly outside OBS Studio?
[/quote]
I missed this part. Well, Urho expects OpenGL context state to stay the same unless it's changed by the engine itself. If OBS alters it even slightly, Urho behaviour is undefined.

-------------------------

scaled | 2021-05-18 09:42:37 UTC | #14

Also, for some reason, i can't initialize Urho3D inside 'obs_source_info.video_render' function, it cause segfault. I initialise it into ' obs_source_info.create' function, which don't have graphics context in it.

-------------------------

Eugene | 2021-05-18 09:46:16 UTC | #15

[quote="scaled, post:14, topic:6849"]
Also, for some reason, i can’t initialize Urho3D inside ‘obs_source_info.video_render’ function, it cause segfault
[/quote]
My best bet would be that it's the same reason but in the opposite direction.
OBS doesn't expect that user will reset global OpenGL context during rendering callback. I don't know how it's even supposed to work.

-------------------------

scaled | 2021-05-18 09:49:43 UTC | #16

How many new things, I'm very lucky that I got something =D Thank you very much, I will experiment with the OpenGL context.

-------------------------

