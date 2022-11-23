glebedev | 2020-11-01 23:52:47 UTC | #1

From what I know main Urho3D doesn't accept new heavy samples content (models, textures, etc) to prevent main repository from bloat. Why not to cut sample content into separate repository like for sample gltf viewer does?
https://github.com/KhronosGroup/glTF-Sample-Viewer/blob/master/.gitmodules

-------------------------

weitjong | 2020-11-02 00:39:19 UTC | #2

Yes, it makes perfect sense for full blown sample games to be in separate repository, whether it is still in the "urho3d" org on GitHub or under its main author personal account on GitHub. However, the current basic samples should stay where they are. Maintaining them separately will have extra overhead if we have 50 repos for 50 basic samples. My two cents.

-------------------------

glebedev | 2020-11-02 07:38:20 UTC | #3

Why would you have a repository per sample?

From my point of view an advantage of separate repository would be an ability to squash git history to minimize repository size. In this case a user will download only actual sample content.

-------------------------

weitjong | 2020-11-02 08:15:28 UTC | #4

If you have plan to contribute a new more elaborate sample with its own assets and that it does not fit the definition of basic samples that I was referring to earlier then I agree with you that it can be in a separate repo too. It does not have to be under “urho3d” org. But we could make exception if its author, you or any other person, promise to maintain it. Not a one time drop, please take it and gone.

The existing basic samples are really intended to show one or two simple concepts at a time. Using the same shared assets. There is really not much change to those throughout the change history.

-------------------------

1vanK | 2020-11-02 08:49:27 UTC | #5

I agree that the repository should have a minimum number of examples that simply serve to test the engine code. It makes no sense to drag all examples, games and even components into the engine repository. We already have a page where users can post links to their components: https://github.com/urho3d/Urho3D/wiki

I also agree that the engine repository is ALREADY bloated. We can create a separate repository with squashed commits for each new major version of Urho.

-------------------------

weitjong | 2020-11-02 09:04:50 UTC | #6

Perhaps I should mention that I have a plan to revamp the main website. The new one will have more prominent place to list the good samples out here using Urho3D library. So it does not really matter where the repo will be, if it is good then it will be linked and easily discoverable.

That was the original plan anyway, before I got interrupted. The new CI/CD workflow does not update the site documentation anymore. This part has not actually completed yet. But yeah, otherwise the plan is/was to make the workflow somehow update to a new parallel website before cut over. That’s the other fish that I wanted to fry in one of my comment in other thread.

-------------------------

weitjong | 2020-11-02 09:13:09 UTC | #7

I actually don’t like the idea. There are countless of time I find the history is so useful. You just clone once. Yes, it is slow for the first time. But after that, subsequent pulls are fast as per normal regardless of how long the history is. What’s inside the history is the real treasure. I can see and study the rationale behind Lasse original work since the inception of this project. We have not lost a single bit of the history when I helped him to migrate from SVN to GIT. And, I am sure I will not agree to do that intentionally now.

-------------------------

Eugene | 2020-11-02 09:16:27 UTC | #8

[quote="1vanK, post:5, topic:6494"]
It makes no sense to drag all examples, games and even components into the engine repository
[/quote]

I mostly agree.

However, it's also bad to have engine code that is not used in samples.
Samples provide some basic way to test things. Without samples or tests, these parts of engine would be just dead code that could stay broken for years without anyone noticing.

Just a random example, Urho supports per-vertex lights (in theory). But there's no sample for this feature. In practice, point vertex lights have obviously wrong lighting that depends on light orientation.
I don't know how long ago it was broken, or if it even worked, ever.

And this is just one place that I found randomly while playing around with Urho renderer.

PS: I _think_ it should be enough to just replace -1 with -2 here, but it's just my wild guess and I didn't properly test this change.
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Batch.cpp#L559

-------------------------

weitjong | 2020-11-02 09:32:55 UTC | #9

I am not confirming nor rejecting, but I can easily check and see that the line has not changed since the project inception. And I could know that precisely because the historical is still there.

-------------------------

weitjong | 2020-11-02 09:34:41 UTC | #10

I think we have to get back to the main topic. And I need to get back to work. 😁

-------------------------

1vanK | 2020-11-02 09:34:57 UTC | #11

[quote="weitjong, post:7, topic:6494, full:true"]
I actually don’t like the idea. There are countless of time I find the history is so useful. You just clone once. Yes, it is slow for the first time. But after that, subsequent pulls are fast as per normal regardless of how long the history is. What’s inside the history is the real treasure. I can see and study the rationale behind Lasse original work since the inception of this project. We have not lost a single bit of the history when I helped him to migrate from SVN to GIT. And, I am sure I will not agree to do that intentionally now.
[/quote]

The history will not be lost anywhere, the history will remain in the repository of the previous version of the engine

-------------------------

weitjong | 2020-11-02 09:35:53 UTC | #12

But then it is not as useful. Because you have to jump one tag to the next to get to the bottom of it.

-------------------------

glebedev | 2020-11-02 09:43:13 UTC | #13

Let's use terrain shader update as an example.

I have an update for terrain shader to support up to 5 textures. @1vanK ask me to create a sample for it. This means I have to make a scene with 5 terrains each representing different number or textures. I can probably reuse textures that already exist in the project but I'll need at least 2 blendmaps for terrain because for 5 textures I'll need unnormalized RGBA weights as fifth weight is calculated as (1-R-G-B-A).

Another example would be a character controller. For a proper test of a character controller there should be a scene that represents a game-like environment with stairs, gaps to jump across, etc. Boxes and mushrooms are not enough.

-------------------------

Eugene | 2020-11-02 09:43:39 UTC | #14

[quote="weitjong, post:9, topic:6494"]
I am not confirming nor rejecting, but I can easily check and see that the line has not changed since the project inception
[/quote]
*sorry for offtopic</>* It's a bit more complicated than just checking this specific line, one would need to review all the shaders that use this variable in order to get full picture. Still doable with git history, tho.

I cannot imagine myself doing bug investigation without repository history, to be honest.
Squashing works fine for periodically updated 3rdparties, but squashing main repo?.. Ew, sounds terrible.

-------------------------

1vanK | 2020-11-02 09:47:42 UTC | #15

I asked for a test scene to test the shader before the merge. I didn't plan to include the scene in the engine. Although you're right, this is a scene that should check if the engine is working.

-------------------------

1vanK | 2020-11-02 09:50:05 UTC | #16

Another question is whether shaders are part of the engine. In fact, I think shaders are resources for a game, not part of the engine. Each game often has its own shaders. If some shader requires a change in the engine, then it makes sense to consider it essential.

-------------------------

1vanK | 2020-11-02 09:55:01 UTC | #17

Look it: https://discourse.urho3d.io/t/basic-material-effects-for-rendering/2953

It's cool but should we include this to the engine?

-------------------------

glebedev | 2020-11-02 10:01:15 UTC | #18

No, but the whole shader system requires a rework.

-------------------------

Eugene | 2020-11-02 10:01:36 UTC | #19

[quote="1vanK, post:16, topic:6494"]
In fact, I think shaders are resources for a game, not part of the engine. Each game often has its own shaders.
[/quote]
The engine (any, not just Urho) has very specific requirements about shaders.
The engine expects shader to receive certain input data in certain format, and it expects shader to deliver output data in some other format.
These requirements are huge and they are not documented directly (at least in Urho): one have to look at existing shaders (and likely reuse them) in order to make custom shader.

So, at least the interface part of shaders is a part of engine.
So it's better be reasonably covered with samples (and sample shaders) so we don't get dead code.

-------------------------

glebedev | 2020-11-02 10:03:00 UTC | #20

Ugh.. Then I misunderstood the request. If the sample won't be part of the engine repo how would you test any changes to the shader?

Shall shader have a reference to github repo then with a test scene?

-------------------------

1vanK | 2020-11-02 10:06:13 UTC | #21

I already mentioned in my post about shaders that require an engine change. But we are talking about shaders that are nice, but do not require changing the engine. This is not the first attempt to improve the ground shader. Somewhere there was already a shader with trilinear texturing of terrain.

-------------------------

1vanK | 2020-11-02 10:11:25 UTC | #22

I would prefer to leave the shader in a separate repository along with the test scene. I can test the shader on my pc, but cannot test on a mobile device which will impose additional restrictions.

-------------------------

1vanK | 2020-11-02 10:35:41 UTC | #23

 https://urho3d.fandom.com/wiki/Expand_default_terrain_material_to_4_textures_using_alpha_channel
 https://urho3d.fandom.com/wiki/Expand_default_terrain_material_to_7_textures_using_the_six_primary%26secondary_colors_and_black
 https://urho3d.fandom.com/wiki/Height_Mapping
 https://urho3d.fandom.com/wiki/Terrain_Shader_with_normal,_specular_and_height_mapping

-------------------------

