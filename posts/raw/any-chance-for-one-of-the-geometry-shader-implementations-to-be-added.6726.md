throwawayerino | 2021-02-23 09:44:37 UTC | #1

There are a couple of forks around that implement geometry shaders and rbfx has one if I remember correctly. Is there a possibility for turning one of them into a PR for main branch if the author agrees to? I've been thinking about trying to make one but didn't want to duplicate efforts.

-------------------------

Eugene | 2021-02-23 12:29:34 UTC | #2

Geometry shaders in corresponding rbfx branch are actually taken from closed Urho PR. If you are ready to finalize this work, go ahead.

-------------------------

throwawayerino | 2021-02-23 13:15:41 UTC | #3

It's this one I assume (Couldn't find the closed PR): https://github.com/rokups/rbfx/commits/ek/geometry/develop and you seem to be the author. What's missing about it so far, if you can remember?

-------------------------

Eugene | 2021-02-23 13:25:41 UTC | #4

I’m not the author, I just committed code. I didn’t check performance impact from this commit, and more importantly, there’s no sample. Without sample it is just dead code that is going to break silently at some point and no one will notice.

-------------------------

throwawayerino | 2021-02-23 13:38:48 UTC | #5

Who's the author then? JSandusky seems to be since I saw his name [in another branch](https://github.com/urho3d/Urho3D/compare/master...eugeneko:GeometryShaders) with similar code.
Samples should be easy, and the code seems to be complete and written by someone competent (but no editor support or angelscript bindings)

-------------------------

Eugene | 2021-02-23 16:15:24 UTC | #6

[quote="throwawayerino, post:5, topic:6726"]
and the code seems to be complete
[/quote]
I am not certain that the code is ready. I didn't merge it into fork, even after I removed most tricky code. It _wasn't_ merged into master, too.

I can remember one... "aspect". Vertex shader and G/H/D shaders share same uniform buffers, but use different shader defines. What would happen if you use defines to control uniforms? I have no idea.

-------------------------

JSandusky | 2021-02-23 23:27:58 UTC | #7

* Uniforms are shared with VS
    * this was more for simplicity than any "real" reason, there's no reason there couldn't be additional UBOs for each stage. In D3D11 you get a minimum of 7 CBOs per stage, GL has device varying limits on the max total number of UBOs for an entire linked shader as well as per stage IIRC.
    * Assuming that GS/HS/DS care about the same info as the VS felt like a reasonable compromise
* Element types are limited (no patch control at all, patches have to be triangle patches)
* No helpers for adjacency in index-buffers
* No stream-out
    * compute shader is a better choice than stream out almost all the time though
* The particle specific code for GS expansion of points isn't really a great use of it in practice (if it's even still there)
    * makes the already awkward shader combination that particles end up with more complex
    * pretty fat vertex data going into and out of the GS
* Dealing with clip-space transforms in the additional shader stages can be confusing
* If there isn't a sample material (I know there wasn't a sample scene) using the tessellation stage that's my bad and I should fix that
* At the time I couldn't really think of a decent GS example that wasn't insane but using it for outlines (flip and expand) would probably do as minimalist
    * again, using the GS on particles was stupid

All-in-all the HS/DS and CS stuff is probably more useful than the GS since the CS can deal with most of the things you'd want to use the GS for.

Edit: the only place I'm still using the GS is in debug draw with [IM3D](https://github.com/john-chapman/im3d) where nicer and quicker to "read" debug lines/points are worth any sane cost over 1px wide lines.

-------------------------

