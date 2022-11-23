GoldenThumbs | 2019-08-04 02:37:12 UTC | #1

So I found [SetShadowMapFilter](https://urho3d.github.io/documentation/1.7/class_urho3_d_1_1_renderer.html#a4d500a70c61963017f40b2948cd27fef) and I'm not sure how I'm supposed to use it. From what I can see (the seemingly obvious) the first parameter needs the game context and the second is the actual blurring function. Thing is, I'm not sure what kind of output the blurring function needs to give. My assumptions would be vec3 or float, but I notice that the type for the parameter is "ShadowMapFilter". I'm not sure I entirely understand what that is. From my limited knowledge it looks like an enum, but an enum wouldn't work for that kind of thing. If now one wants to explain it can I get a link to the relevant parts of the code from Github?

-------------------------

Modanung | 2019-08-04 03:27:32 UTC | #2

Have you seen this line? It might help you try out some things.

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Renderer.h#L178-L179

-------------------------

Leith | 2019-08-04 08:33:08 UTC | #3

Ah, its a callback function pointer placeholder for a custom implementation - you provide a matching function, and hand a pointer to the api - interesting, have not messed with this.

-------------------------

Leith | 2019-08-04 08:34:15 UTC | #4

I'm not used to seeing "using" being used in this way - we'd usually use "typedef" here.

-------------------------

GoldenThumbs | 2019-08-04 20:14:34 UTC | #5

Is there any reason no one seems to use this?

-------------------------

Modanung | 2019-08-05 00:10:43 UTC | #6

Other priorities :woozy_face:

...and maybe it's simply a little known and puzzling feature because of lacking documentation and current implementation. *Do* share any findings. :slight_smile:

-------------------------

GoldenThumbs | 2019-08-05 00:12:07 UTC | #7

I'll figure it out. Will share anything I find

-------------------------

Leith | 2019-08-05 13:17:43 UTC | #8

No one seems to use "what"? I mentioned something was unusual, but people do learn their own habits, and I won't tell them it's wrong, if their code still runs rock solid.

-------------------------

Sinoid | 2019-08-06 01:50:31 UTC | #9

The filter is used for VSM blurring.

Three other use-cases that immediately come to mind:
- ESM/EVSM, for blurring again
- Imperfect Shadow Maps, for filling the *void* gaps.
- Compositing a multi-channel shadowmap into a final singular map or more narrow one (ie. composite per shadow-pixel not sampled pixel)

-------------------------

GoldenThumbs | 2019-08-06 20:42:18 UTC | #10

Found out that I could blur shadows in the shader so I've been working on that. Now I'm having issues with seams appearing in omni-directional shadows (point light shadows). If anyone comes across this and know how I can fix them the help is appreciated. In the mean time I'm gonna make a new topic on it since it's not related to this C++ shadow filter.

-------------------------

Modanung | 2019-08-06 22:01:10 UTC | #11

Could you share the code you used to make it work?

-------------------------

GoldenThumbs | 2019-08-06 22:29:41 UTC | #13

I didn’t use this, the blurring is done entirely in shader. Didn’t even need to touch C++. Might rework the shadowing code later when I feel like both my skills in C++ are good enough and there’s an advantage to doing it in C++ rather than shaders. (I meant to make this a reply the first time I posted it but pressed the wrong thing.)

-------------------------

