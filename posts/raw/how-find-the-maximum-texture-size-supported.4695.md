Hideman | 2018-11-26 16:57:16 UTC | #1

Hi everyone,

I just want to known how we can get the maximum texture size to build a texture atlas on the fly and save it on disk?
Texture atlas need to be generate manually because I want to support modding with custom texture for additional game objects.
And finally if you have links to some discussions or anything about texture atlas creation on the fly with Urho3D I will be appreciate it very well.

Tks for your further response.

-------------------------

jmiller | 2018-11-30 21:09:50 UTC | #2

Hi,

Maximum texture size depends primarily on the graphics hardware.

Wildfire offered a dataset:
  https://feedback.wildfiregames.com/report/opengl/feature/GL_MAX_TEXTURE_SIZE

  https://stackoverflow.com/questions/19572659/is-1024x1024-a-widely-supported-opengl-maximum-texture-size-on-the-desktop
Maybe the 1024 is a bit outdated.
Other articles will go into more detail about specific devices..

Also, maybe some users have dropped some info on how they setup their [url=https://discourse.urho3d.io/search?q=texture%20atlas]texture atlas[/url].

If one need make engine modifications to check max size, I only speculate that the internal `SDLRenderer->info.max_texture_width` (+height) may hold the API-agnostic answer..

-------------------------

Sinoid | 2018-11-28 01:24:15 UTC | #3

**TL;DR:** What are you packing and why are you packing it? Packing just for the sake of it can easily be worse than not packing.

---

Your packed contents need to be consistently used for it to pay off. Given that Urho3D has an underlying batching mechanism what you're likely intending to do will just shoot you in the foot without investing time to understand the batch sorting and how to use *priority* wisely, realistically you're just going to cause texture swaps of massive textures like a musical tune, you're diving at a sonata without ever touching twinkle-twinkle.

Edit: most of the above paragraph is wrong. My wires were all crossed.

---

Urho3D has helpers for command-line program access, so you can use the texture-packing tool that already exists if you can settle for hooking the process. It also shows how to do it as the Urho3D things that are aware of packing expect.

-------------------------

