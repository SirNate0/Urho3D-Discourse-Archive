elmer | 2019-04-20 12:10:45 UTC | #1

Hi, can anybody tell me how to export .mdl file using blender2.8?  thanks very much..

-------------------------

JTippetts | 2019-02-20 13:58:03 UTC | #2

The Blender exporter hasn't been updated for 2.8 yet, so your best option is to export to FBX or Collada, and use the asset importer to convert.

-------------------------

Modanung | 2019-02-20 19:13:13 UTC | #3

See also:
https://github.com/reattiva/Urho3D-Blender/issues/90

Despite the change from layers to collections, objects - in a 2.80 file - can still be linked to files creates in earlier versions.

-------------------------

dertom | 2019-02-21 00:13:48 UTC | #4

Just stay on 2.7 if developing for Urho3D
Edit: And yes I know I didn't answer the question.
Edit2: Btw, I'm actually working on the exporter and try to add some features (not 2.8 yet. No priority to me)

-------------------------

elmer | 2019-02-21 01:31:20 UTC | #5

ok,thank you for your advice.

-------------------------

QBkGames | 2019-03-04 02:27:49 UTC | #6

[quote="dertom, post:4, topic:4946"]
Just stay on 2.7 if developing for Urho3D
[/quote]

The only problem is that once you start getting used to Blender 2.8, going back to 2.7 is like going back to a horse and carriage after getting used to driving a car :stuck_out_tongue:.

-------------------------

Modanung | 2019-05-30 10:01:02 UTC | #8

The Urho3D exporter add-on for Blender 2.80 is available from a dedicated branch in its main repository:
https://github.com/reattiva/Urho3D-Blender/tree/2_80

If it doesn't load correctly read [this comment](https://github.com/reattiva/Urho3D-Blender/issues/90#issuecomment-483549844) by @dertom.

-------------------------

Leith | 2019-04-26 13:35:42 UTC | #9

step 1: export from blender to fbx (using blender)
step 2: import model file from fbx (using AssetImporter)

animations are handled separately usually, but the skinned model, we do this in two steps and avoid all version conflicts

-------------------------

QBkGames | 2019-05-30 09:01:55 UTC | #10

I think the latest Blender 2.8 build broke the exporter again :cry:

-------------------------

Leith | 2019-05-30 13:11:10 UTC | #11

Just as well I don't use it

-------------------------

Modanung | 2019-05-30 14:08:54 UTC | #12

@Leith Yes, you are **import**ant.  ;)

Seems like it did, I had a quick look (without fixing the problem) and mentioned it in the GitHub issue.

-------------------------

Leith | 2019-05-30 14:23:39 UTC | #13

It's good that we have more than one pathway in our asset pipeline, when things go wrong there is still another way

-------------------------

Modanung | 2019-05-30 15:31:28 UTC | #14

Well it's not like all other versions of the involved software *splatted*, nor does the Blender Foundation force the very latest version on its users. The add-on still works with the earlier 2.80 Beta and 2.79b versions of Blender. Indeed fallbacks are good to have.

-------------------------

QBkGames | 2019-05-31 05:14:15 UTC | #15

I use it all the time, and for me going through any alternative option (especially fbx->assimp) is just too time consuming.
Really looking forward to it working again :slight_smile:.

-------------------------

Leith | 2019-05-31 06:25:15 UTC | #16

I accept that focused solutions are easier and work well in any production workflow, and I am sorry that Erwin broke our plugin (which I don't use) but let's look into what changed, why it broke, and I can even act as an intermediate to talk to Erwin about future game breaking changes.
Erwin tends to use an interface-based approach to his code design, and the interface tends not to change over time, he's one of the best coders and design engineers I have known. If he changed something, and it broke stuff, I think we can expect that not to happen often at all.

-------------------------

dertom | 2019-06-19 00:40:10 UTC | #17

Just for info. I uploaded my current blender 2.8-exporter a bit diverged from the main-repo:

https://discourse.urho3d.io/t/blender-2-8-exporter-with-addional-features-e-g-urho3d-materialnodes-and-components/5240

-------------------------

