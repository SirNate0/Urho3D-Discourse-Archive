dertom | 2020-11-30 12:27:00 UTC | #1

Hi there,
I'm working on and off on the blender exporter, also it is uptodate to work on latest blender 2.8. 

The new features are:
- live preview as blender render engine
- userdata/tag-creation
- lod-creation more comfortable using its own panel
- exporting collection and using them as instance (also linking is possible if doing it the right way)
- parenting to empties
- starting a runtime from within blender
- using a special runtime, which will create a json-file representing all exported components (e.g. all logiccomponents) and all materials/techniques/textures to be used in component- and material-trees.
- using multiple logicnodes per object

Download: https://github.com/dertom95/Urho3D-Blender/releases

**Info:** For some features to work you need to have some minor components registered in your project. (Those are included in the urho3d-minimal-new-project): [GroupInstance and RotationFix](https://github.com/dertom95/urho3d-minimal-new-project/tree/master/src/Components) 

Links:
* [How I used the exporter in my GGJ'20-Game](https://discourse.urho3d.io/t/dev-workflow-urho3d-blender-used-in-ggj2020/5883)

Videos:
- [Installation / Getting Started (Updated 2020/07/10)](https://www.youtube.com/watch?v=o-1RMIwQZMY) (from tag 0.2 onwards you can install the releases like any other blender addon)
- [Exporter Options](https://www.youtube.com/watch?v=VtZk6FipkdU)
- [runtime and material-nodes](https://www.youtube.com/watch?v=utLNqfxZ_KE)
- [materialnodes and textures](https://www.youtube.com/watch?v=13jslwWhUSk)
- [component nodes ](https://www.youtube.com/watch?v=Ni3nD5687aQ)
- [custom component workflow](https://www.youtube.com/watch?v=B37ZTa7mbpE)
- [Collection Instances](https://www.youtube.com/watch?v=Ut0HJYpvuFc)
- [Armature Animation](https://www.youtube.com/watch?v=h2NS348L8X0)

Repos:
Blender-Urho3D-Addon: https://github.com/dertom95/Urho3D-Blender.git
Blender-JSON-Nodes: https://github.com/dertom95/addon_jsonnodetree
Urho3D-Blender-Runtime: https://github.com/dertom95/urho3d-blender-runtime

urho3d-minimal-new-project: https://github.com/dertom95/urho3d-minimal-new-project

Changelog:
v0.8.1:
- blender-python: if pip is not installed, do so before installing pyzmq ( installation might take some time )
- stability, not so much crashes anymore
- material's texture-category entries are fixed now. Before adding new folders in could lead to problems with reassigning the right image 
- choose kind of export on save-types (scene with geometry,scene without geometry,material only)
- pack whole export path into one urho3d-pak-file
- export urho3d builtin components (none,lite(some subset),all). Those can be assigned via the 'urho3d-components'-nodetree (not all attributes are exposed,yet)
- added urho3d-tab in 3d-view with components:
  - urho3d-scene:
    - select RenderPath ( those are all renderpaths available in the resource-cache of the exportPath)
    - create default zone with optional cubemap.
    - create SkyBox (For this the urho3d Sphere.mdl is integrated into the runtime's data-folder. So you need to be sure to copy the Sphere.mdl as SkyboxSphere.mdl into your resourcepath)
  - urho3d-materials,components and userdata-assignment (nothing new here, just reused for this panel)
- lights now have a "Use Physical Values"-Option ( for more custom behaviour you can create a component-nodetree with a lightnode and assign this to the light)

-------------------------

QBkGames | 2019-06-19 10:00:58 UTC | #2

Using Blender as a level editor combined with an appropriate exporter could be a good alternative to creating a level editor from ground up.

-------------------------

johnnycable | 2019-06-19 14:49:15 UTC | #3

[quote="dertom, post:1, topic:5240"]
using a special runtime, which will create a json-file representing all exported components (e.g. all logiccomponents) and all materials/techniques/textures to be used in component- and material-trees.
[/quote]

Absolute best thing would be to mantain an instance of Blender open for level editing, and an instance or Urho running in parallel to see changes, both exchanging data, sort of networking-like but in place, by simply reading project data...

-------------------------

guk_alex | 2019-06-19 15:40:17 UTC | #4

If Blender plugin could have Urho3D instance inside - it can send corresponding updates like in client-server example, also that networking component could be removed if we already have Urho's viewport inside blender - but both of that features require major integration work to be done.

-------------------------

Modanung | 2019-06-19 16:45:06 UTC | #5

Interesting work! You may want add a link to your repo in the top post.

-------------------------

dertom | 2019-06-19 16:46:05 UTC | #6

[quote="QBkGames, post:2, topic:5240, full:true"]
Using Blender as a level editor combined with an appropriate exporter could be a good alternative to creating a level editor from ground up.
[/quote]

Yes, I'm a blender guy and always liked its handling and always wanted it to be my scene-editor. At the very beginning I added a shortcut for opening the Urho3d-Editor from within the runtime, which worked but crashed, once you select a component ;) (Didn't know it wasn't my fault and I kicked it out again).
Still I think both approaches(using an editor or a 'fat'-exporter) have its advantages...

[quote="johnnycable, post:3, topic:5240"]
Absolute best thing would be to mantain an instance of Blender open for level editing, and an instance or Urho running in parallel to see changes, both exchanging data, sort of networking-like but in place, by simply reading project data…
[/quote]

Yes, this is actually the plan. Having the runtime open to send the blender-instance component/materials/node-changes and the current render and blender sending its viewport position. 

Something like this: https://github.com/Kupoman/BlenderRealtimeEngineAddon 
Never really could make it run...

[quote="guk_alex, post:4, topic:5240, full:true"]
If Blender plugin could have Urho3D instance inside - it can send corresponding updates like in client-server example, also that networking component could be removed if we already have Urho’s viewport inside blender - but both of that features require major integration work to be done.
[/quote]
Yeah,...I actually thought so as well at the beginning. Blender 2.8 seems to have a better api for implementing custom render-engines, but I guess this would be overkill, and since I want my own components to be part of the engine, I would have to compile all of it everytime I change my components. (Well ok, you could think of shared-libs and hot-reloading, but I'm not skilled enough for fancy stuff like that ;) ) 

[quote="Modanung, post:5, topic:5240, full:true"]
Interesting work! You may want add a link to your repo in the top post.
[/quote]

Indeed :+1:

-------------------------

Modanung | 2019-06-19 20:26:24 UTC | #7

Additionally a name change for this project may provide more clarity concerning it's features. It would also set it apart from the exporter [sec]. It seems more like an *integration* instead of just an *exporter*?

-------------------------

johnnycable | 2019-06-20 15:02:47 UTC | #8

[quote="dertom, post:6, topic:5240"]
Yeah,…I actually thought so as well at the beginning. Blender 2.8 seems to have a better api for implementing custom render-engines, but I guess this would be overkill, and since I want my own components to be part of the engine, I would have to compile all of it everytime I change my components.
[/quote]

Agree. It's complicated and overkill. Moreover, it's not the way you would use Urho in a real setup, so no need.
And in the end you'll end up with something like [armory](https://armory3d.org/) for Blender...

-------------------------

dertom | 2019-06-22 15:54:32 UTC | #9

Ok, party people. I created some new videos (see first post). Still a bit confused ones but you will get used to it ;)

[quote="Modanung, post:7, topic:5240, full:true"]
Additionally a name change for this project may provide more clarity concerning it’s features. It would also set it apart from the exporter [sec]. It seems more like an *integration* instead of just an *exporter* ?
[/quote]

Hmm,...I actually always had in mind to do a pull request once the bugs are found and resolved....making it a project of my own, would feel like a ripoff, not?

[quote="johnnycable, post:8, topic:5240"]
Agree. It’s complicated and overkill. Moreover, it’s not the way you would use Urho in a real setup, so no need.
And in the end you’ll end up with something like [armory ](https://armory3d.org/) for Blender…
[/quote]
Yeah, we will see where it ends. But if it turns out to be like amory but with urho3d as background, would be nice as well. ;)

-------------------------

Modanung | 2019-06-22 20:14:09 UTC | #10

[quote="dertom, post:9, topic:5240"]
Hmm,…I actually always had in mind to do a pull request once the bugs are found and resolved…making it a project of my own, would feel like a ripoff, not?
[/quote]
The license allows for it, and there's nothing stopping you from thanking the main repo man. I don't mean to chase you away from @reattiva's project, at first glance it just seemed to me like you were going your own way somewhat with all the extra features. But maybe it's all welcome, I have only briefly looked into your efforts.

-------------------------

WangKai | 2019-06-23 10:12:04 UTC | #11

Very interesting projects. I'm still watching the videos, however, documents and pictures explaining the ideas behind the projects would be better for us to know.

-------------------------

WangKai | 2019-06-30 14:19:50 UTC | #12

Hi @dertom

I've watched all the videos on YouTube. I can see that you have spend a lot of time recording the videos. However, it is better if you could introduce your idea as words and images so people can get some of it better before digging into the videos.

The projects are impressive. We used to have similar plugins for 3ds max but call the "runtime" as "previewer". e.g. We used to extend 3ds max's particle system and use it as the particle editor for the game which has a similar logic for particles. In order to see the effect of the editing, we developed the previewer and export the config every time and spawn the particle in it.

I think it would be better if your Blender addon can live update/hot reload the changes so that the iteration can be much faster though there are challenges to design and implement to achieve this.

Additionally, I wonder if there is some way to map Urho's shader and material to Blender's so that we can see the image in Blender even before the previewer's. (There is no default Blinn-Phong in Blender and Urho's PBR is not complete.) Other aspects of the scene would be also the same if they have according representations in the Blender.

Generally, there are two ways of editing scenes. One of use the DCC tools (Maya/3ds max/Blender), the other is use scene editor (Unity/Unreal Engine/CryEngine...). I'm also very interested in this topic and have been thinking about the workflow of combining Blender and Urho3D a lot. There is also very good GDC session - https://www.youtube.com/watch?v=KRJkBxKv1VM&t=168s 

Again, nice topic and work.:wink:

-------------------------

dertom | 2019-06-30 15:42:14 UTC | #13

[quote="WangKai, post:12, topic:5240"]
I’ve watched all the videos on YouTube. I can see that you have spend a lot of time recording the videos. However, it is better if you could introduce your idea as words and images so people can get some of it better before digging into the videos.
[/quote]

Well,...I understand that. But writing this down would have taken too much time, As a matter of fact lots of things will be changes sooner or later and I guess I'm not writing down anything until it the final workflow gets obvious...

[quote="WangKai, post:12, topic:5240"]
I think it would be better if your Blender addon can live update/hot reload the changes so that the iteration can be much faster though there are challenges to design and implement to achieve this.
[/quote]
It acutally does every time to export the scene, it gets hot reloaded

[quote="WangKai, post:12, topic:5240"]
Additionally, I wonder if there is some way to map Urho’s shader and material to Blender’s so that we can see the image in Blender even before the previewer’s. (There is no default Blinn-Phong in Blender and Urho’s PBR is not complete.) Other aspects of the scene would be also the same if they have according representations in the Blender.
[/quote]

I actually gave it a try this weekend to create the corresponding urho-render of the blender's viewport and map it via blender's custom renderengine as a background. Actually it mostly works, **BUT** I don't get the blender right-handed viewport matrix properly converted to urho3d's lefthand one. I'm not so much in this kind of low level matrix calculation ;) It works at certain angles with my "naive" approach ;) This will be work in progress but I want this to happen. Atm it looks like this when the view-maps more or less:
![image|690x411](upload://tBK4QyPJhESlKdIHVbyu6dpWyFO.jpeg) 

Not sure when I find time to work on it again....

-------------------------

Modanung | 2019-06-30 18:28:08 UTC | #14

That's really cool that you got Urho Render into Blender! And simply awesome work in general - albeit not production ready - I wonder how long until the Blender Game Engine gets replaced by Urho3D entirely. :slight_smile:
I don't know if any of you have experience with the BGE, but in my opinion it could use a replacement.

-------------------------

dertom | 2019-06-30 20:41:57 UTC | #15

Well I guess as of blender 2.8 BGE is offically out of business. There is a fork of it. [UPBGE](https://upbge.org/). I was never really interested into BGE due to its gpl-licenses but was part of the [gamekit-project](https://github.com/gamekit-developers/gamekit/wiki/Blender-Addon) some years ago, which had a tight blender integration. It was actually a cool project but died...I always thought to put it on top of urho3d as it was designed as a middleware...but urho3d is so good in itself, it would be a waste to put some abstraction on top of it....

-------------------------

Modanung | 2019-06-30 20:57:40 UTC | #16

Ah, I was unaware they dropped it... but license aside, I think the logic node system was bad enough to help beginning game developers over their fear of coding but then the scripting API was equally uninviting. Whenever I saw anything made with BGE that looked like an actual game I was amazed at the patience of their creators and not so much the creations themselves. With BGE gone you might be able to inspire members of the Blender community to assist in your add-on's development.
My earlier notion has been confirmed after watching some more of your videos that what you are working on is more than (what I would call) an exporter. Rather this looks like the *Urho3D-Runtime Add-on* to me.

-------------------------

dertom | 2019-07-05 13:33:06 UTC | #17

Ok,..I took some work (motivated by @jmiller )  to revive multi-material meshes...first tests seem(!) to work:
![image|690x431](upload://xr1L4eBIPjbfPAe0s3xyG9ayGxx.jpeg) 

Just for info, all that is exported is vanilla urho3d-scenes (only if using collection-instances or bone-parenting you need two helper components) and materials
Have fun and nice weekend, Tom

-------------------------

Modanung | 2019-07-05 21:51:46 UTC | #18

@reattiva Have you seen this?

-------------------------

dertom | 2019-08-03 12:15:08 UTC | #19

Still working on this on and off. 
One new feature is 'filters for textures and techniques' and now I finally have a very very first draft of the urho3d-blender-renderer. I connected it via network to blender which tells the runtime/renderer that the viewport has changed, which will send the image via network to blender which will render it. Took me some time for the blender's view-matrix to work. I burnt lots of hours just because the texture on the blender-side was flipped :D Nontheless the result is a good first start. ~~There is still some offset between the blender-world and the urho3d-render....~~(EDIT: Got it right now. I calculate the fov on the blender side and send it along with screensize-changes)
![firstdraft_urho3d-blender-renderer|690x411](upload://rWoRYGBjS7IpfZEXnL9uyDTMBah.jpeg) 

And here a little [screen-cast](https://www.youtube.com/watch?v=N307c6mmKJo&feature=youtu.be) to see it in action.

-------------------------

suppagam | 2019-08-03 03:07:29 UTC | #20

The JSON thing is awesome! You made my workflow so much better. Thank you! Do you have a donation page somewhere?

-------------------------

dertom | 2019-08-03 07:13:51 UTC | #21

Oh thx, @suppagam. I have no donation-page. The knowledge someone is actually using it at all is payment enough. ;)  Everything is still very manual. But now with the my network-layer setup, I can automate much more

-------------------------

QBkGames | 2019-09-09 07:26:25 UTC | #22

I'm having a problem exporting meshes that have multiple (similar) materials from Blender 2.8 (official release version), they come in Urho as a single combined material.

I don't think it's a problem specific to the exporter, as I get the same issue if I export FBX and use Asset Importer tool. I think it might be a new way Blender manages materials for a mesh!? 

Does anyone else have this problem? Is there a work around?

-------------------------

dertom | 2019-09-09 12:41:30 UTC | #23

@QBkGames:  If you give me a sample-blend that I can use a template for this problem I will have a look....(obviously I only test for my exporter)

-------------------------

QBkGames | 2019-09-09 23:43:53 UTC | #24

Check out this sample blender file:
www.qbkgames.com/Dev/Issues/ShrineTest.zip

The "Shrine" mesh has 2 materials in Blender but when exported to Urho it comes over as a single combined material (in the past versions it used to come over as 2 separate materials, which is what I need). The materials are both based on vertex color painted over the mesh and there are no texture. When you export the mesh use these flags for the Geometry options: Position, Normal and Color (no UVs or anything else).

Thanks for your assistance.

-------------------------

dertom | 2019-09-10 20:03:52 UTC | #25

Hmm,...ok. I guess you are using the normal exporter(2.8 branch). Just looked into that code and I doubt that you should expect materials export to work properly. Still I'm unsure why only one material is created, I would have expected both to be generated but looking the same, as I don't think that the emission value is detected as it is "hidden" in a cycles node which is not processed by this exporter...what is the filename of the material that is created and what is the content? 

sry. can't do more. 

Btw, what technique would you have expected for your glow-material? Can't find any NoTextureVCol**Emissive** alike-techique.

-------------------------

Modanung | 2019-09-10 20:26:13 UTC | #26

[quote="dertom, post:25, topic:5240"]
Can’t find any NoTextureVCol **Emissive** alike-techique.
[/quote]

There _is_ `NoTexture`**`Unlit`**`VCol`.

-------------------------

QBkGames | 2019-09-11 01:43:19 UTC | #27

Just to clarify, I'm not interested in exporting the materials from Blender, I just need the mesh to have the correct number and order of materials, so I can assign them in code in Urho. In the case of the Shrine, I should have 2 materials to assign, but I only get 1.

The material created by exporter is, just a combined material:
>     <component id="16777216" type="StaticModel">
>   	  <attribute name="Model" value="Model;Shrine.mdl"/>
>     	<attribute name="Material" value="Material;"/>
>     </component>

And from FBX->AssetImporter is just get something called JoinedMaterial_#1.xml.

After playing around a bit more, I found that I can get the FBX exporter to work if I replace the materials with newly created Principled BSDF based materials, but the Urho exporter still only outputs a single material. I guess I can just use the FBX exporter for meshes with multiple materials, and the Urho exporter for meshes with single material, for now.
Thanks anyway for taking a look, maybe you can fix it later on when you have more time (if that day ever comes :) ).

BTY, I created a couple of custom techniques which are not part of Urho assets, to better suit the graphics style of my game, just a small variation of existing techniques, nothing fancy, but they do the job.

-------------------------

dertom | 2019-09-13 15:13:26 UTC | #28

Update:
![Screenshot%20at%202019-09-13%2017-02-33|690x411](upload://umCQON1Y49Dhd1LeZkhL9815orG.jpeg) 

Outline mapping to Urho3d-Render matches (that was a hard fight)
Multiple renderviews possible, multiple splits, textures hot reloaded to use in materials, mesh with multiplematerials (Obvisouly everything wip,experimental,proof of concept,you name it ;) )

Communication between blender and the runtime is done with pyzmq(zeromq), which needs to be installed via pip in blender's python. 

For people wanting to test the current state I created a [zip](https://github.com/dertom95/Urho3D-Blender/releases/download/custom-renderer-preview/urho3d-blender.zip) with everything needed inside and wrote an [wiki-page how to install and use it.](https://github.com/dertom95/Urho3D-Blender/wiki) Maybe later I will create a small video...no time left.

Here are the instructions. Questions welcome! ;)

-------------------------

dertom | 2020-07-09 23:53:58 UTC | #32

Ok, I just created a new video how to setup this exporter with the live-previewing the urho3d-scene inside blender. Have a look here:

https://www.youtube.com/watch?v=vyP0dXvh9Aw

-------------------------

joe | 2020-08-15 05:39:13 UTC | #33

So with your addon, is it like Armory where it treats Blender like a GUI game editor?

-------------------------

dertom | 2020-08-15 08:44:12 UTC | #34

Yes, kind of. See it like a scene-editior. The game itself still needs to be created in c++ in which you can load the created scene. But I warn you, the workflow is not super-smooth and I don't develop on it constantly.
 
But what you can do:  
1) Create Scenes, Create Urho3D-Materials(via nodetrees) and preview them in Viewport
2) If your application exports logic-components you can also export logic-components, load them and assign them to your blender-nodes. (If you know how to do this, some videos are (afaik) a bit outdated, because this is now a separate process. for a sample how to do this you can have a look at my [minimal-project](https://github.com/dertom95/urho3d-minimal-new-project) that already exposes some, every time you start you game): https://github.com/dertom95/urho3d-minimal-new-project/blob/master/src/StartupApplication.cpp#L111

if using my startup-application every time you execute it, it generates a file '...-urho3d_components.json' in the execution-folder. If you load this file as json-nodetree you can assign all exported(and registered) components)
![image|578x387](upload://iAX048tMbxEeYUixGSzEFAz0hFJ.jpeg) 
After loading you have this new blender-nodetree-type:
![image|422x212](upload://rse4sxxDEswrc31mtJ0fq6FsPVy.png)
(The blender runtime also exports some components. You can find the corresponding json-file along the runtime-executable)

if using my startup-application you can also toggle an ingame editor in/out. And if developing under linux you can also have some kind of (docker-based) one-click deployment (in theory ;) ) by just writing:
```
# build: native(linux),mingw(win),android,arm,rpi and web
./tools/build_all.sh

# build windows/linux
./tools/build_win_lin.sh

# package them in zips. (you need to specify a name that will be used for the zip-files resulting in: [gamename]-[os].zip):
./tools/export_game.sh [gamename]
```
I have also automatic apk-signing for android....(follow the following link for more details about this)  

(For more information also have a look here. Just saw that I was quite detailed about how I used this exporter in my GGJ20-Game: https://discourse.urho3d.io/t/dev-workflow-urho3d-blender-used-in-ggj2020/5883 )

ok, hope that helps a bit. cheers

-------------------------

dertom | 2020-11-16 23:21:57 UTC | #35

Just for info, I worked on the installation process. Before you had to install 3 addons (incl urho3d-blender) plus install pyzmq in blender's and select the urho3d runtime (win / linux). Ok,...everything was available in the release-package but still.... 

Now I packed everything into one (the dependency-addons are included as submodules, the runtimes are installed with the plugin and the runtime-path is set automatically, pyzmq is installed automatically if not present).

So using the current [release](https://github.com/dertom95/Urho3D-Blender/releases/tag/0.2) should(!) work out of the box.... (runtime only for linux and windows)

-------------------------

throwawayerino | 2020-11-17 06:01:04 UTC | #37

The exporter is really finicky and confusing, but has saved me countless hours of manual work once I wrote down the steps. Thanks a lot!

-------------------------

johnnycable | 2020-11-17 15:48:50 UTC | #38

Thank you so much for this!

-------------------------

GoldenThumbs | 2020-11-18 04:37:26 UTC | #39

What issues do you have with it?

-------------------------

vmost | 2020-11-18 13:12:33 UTC | #41

Why bother throwing shade if you can't back it up?

-------------------------

vmost | 2020-11-18 16:17:09 UTC | #46

Idk who 'gagged' you, however it seems a bit hypocritical since you exercise your moderator gagging power quite a bit. The point is just saying blender 2.8 sucks adds nothing. Who cares if _you_ don't like it? Maybe someone else does. Very unconstructive >_<

-------------------------

dertom | 2020-11-18 19:10:06 UTC | #49

![grafik|690x377](upload://lrNwoc5Fa3gMvcF1Vcqfc3afv2R.jpeg) 

;)

-------------------------

throwawayerino | 2020-11-19 07:25:49 UTC | #50

Just figured out how to make the thing detect my textures, and realised how simple the workflow is. Woooooooooo!

-------------------------

dertom | 2020-11-30 12:39:39 UTC | #51

Ok, I worked a bit more on the [urho3d-blender-addon](https://github.com/dertom95/Urho3D-Blender):
[v0.8.1:](https://github.com/dertom95/Urho3D-Blender/releases/tag/v0.8.1)
- blender-python: if pip is not installed, do so before installing pyzmq ( installation might take some time )
- stability, not so much crashes anymore
- material's texture-category entries are fixed now. Before adding new folders in Textures could lead to problems with reassigning the right image
- choose kind of export on save-types (scene with geometry,scene without geometry,material only)
- autoexport (scene without geometry) on movement (super slow updating at the moment)
- pack whole export path into one urho3d-pak-file
- export urho3d builtin components (none,lite(some subset),all). Those can be assigned via the 'urho3d-components'-nodetree (not all attributes are exposed,yet)
- added urho3d-tab in 3d-view with components:
  - urho3d-scene:
    - select RenderPath ( those are all renderpaths available in the resource-cache of the exportPath)
    - create default zone with optional cubemap.
    - create SkyBox (For this the urho3d Sphere.mdl is integrated into the runtime's data-folder. So you need to be sure to copy the Sphere.mdl as SkyboxSphere.mdl into your resourcepath)
  - urho3d-materials,components and userdata-assignment (nothing new here, just reused for this panel)
- lights now have a "Use Physical Values"-Option ( for more custom behaviour you can create a component-nodetree with a lightnode and assign this to the light)

Played a bit with PBR, still not sure about how everything works together and how to use the effects. I tried to integrate some too, but that does not work that well, yet. 
![image|690x371](upload://1Ktu00NSyPWlSs98sGafcen20kC.jpeg)

-------------------------

throwawayerino | 2020-12-10 08:20:48 UTC | #52

I think I found a bug in the exporter. I'm on blender 2.91.0 and enabling morphs in the export panel doesn't export shape keys with the mdl file (`AnimatedModel::GetNumMorphs()` gives out a zero). Going to the Object Data Properties panel and enabling morphs there give this error:

    \AppData\Roaming\Blender Foundation\Blender\2.91\scripts\addons\urho3d_blender\decompose.py", line 2297, in DecomposeMesh
        if len(shapeMesh.vertices) != len(mesh.vertices):
    ReferenceError: StructRNA of type Mesh has been removed
An ugly workaround (for those searching) is downloading Blender 2.80.0 rc3 and throwing reattiva's exporter on it. It does give an error about a newer version, but clicking export and exiting without saving shouldn't do anything bad

-------------------------

dertom | 2020-12-10 18:55:20 UTC | #53

Yes, that might be right. I never really used morphs and I'm not sure if I converted it to 2.8 at all....I reattiva's exported did the job :+1: 
Btw, for errors the issue-tracker on github in more suitable.

-------------------------

mcmordie | 2020-12-31 17:37:29 UTC | #54

Thank you for this important work-- this tool promises to make amazing things possible!

Have been having some issues trying to get up and running with 0.82b on Blender 2.90.1. The addon seems to install fine (thanks for the tip about running as admin the first time).  Export delivers models, but materials / textures missing under the geometries checkbox?  

![image|640x362](upload://mgKqOhhF8kdoWisIs3mj6JrvwhR.png) 

Aso the runtime previewer comes up black every time and stays that way, despite the scene being viewable in the editor in that path (under AppData ...)

![image|443x270](upload://57dft7cRso43OOsUsJAEVlIEAfv.png) 

Any tips for these issues?  Am I just using the wrong version of Blender for example, or am I doing something wrong?

-------------------------

mcmordie | 2020-12-31 19:39:13 UTC | #55

Okay just to say I think I figured out why the runtime previewer is black-- it appears that the preview is now in the viewport under material preview.  Still not getting the materials export working, will go back over the tutorial videos.

![image|690x409](upload://eXydCUKfB1R2z22gEvjPiTde6Tc.jpeg)

-------------------------

dertom | 2021-01-01 01:10:08 UTC | #56

Are you creating urho3d materials? 
If you have an Eevee material you can try (!) to use the experimental blender->urho3d-conversion.
- Check 'unstable features' bottom render-properties
- go to urho3d-material-view
- create new nodetree 
- select blender-material -> convert-button
- important: choose appropriate technique

....but I guess it is best to create the urho-material from scratch....

-------------------------

mcmordie | 2021-01-01 18:13:10 UTC | #57

Being new to both Blender and Urho3D I was not sure what level of sorcery was included with this plugin :slight_smile:.  

I am using cycles Principled BDSF for most materials in Blender and on the Urho3D side I am using PBR shaders (I guess these will need to be with textures to capture at least the normals).  The confusing question mark for me is what the workflow is to go from one to the other-- I assume I need to bake textures in Blender first, but then how to export these textures so that they will work with the PBR materials Urho's shaders support?  As this is a complex scene I will certainly try the experimental eevee -> urho support if I can get from cycles to eevee (looks like material definition is the same for both?).

[edit] Just tried this experimental material conversion.  Looks amazing-- seems to capture textures as well.  Question: do I need to create a separate node tree for each material and if so, how to ensure that the association between each material and the meshes that it is applied to is maintained during export?  Also, is there a way to batch convert all Eevee materials?  It looks like it is working and will save considerable effort, but there are about 100 materials in this scene.

-------------------------

dertom | 2021-01-01 18:52:01 UTC | #58

Yes,you need to create a material-nodetree for every blender-material. Then you need to assign the urho-material(s) to the object, which will ensure the material-assignment.

There is no batch-convertion at the moment...

-------------------------

jmiller | 2021-01-01 19:25:19 UTC | #59

There is an incredibly useful addon included with Blender (but not enabled by default) that can copy almost any editable attribute like Materials or transform to all selected objects. May it save time somewhere.
  https://docs.blender.org/manual/en/latest/addons/interface/copy_attributes.html

-------------------------

ChunFengTsin | 2021-03-19 01:14:25 UTC | #61

When I install the add-on, blender show this error:

```
Traceback (most recent call last):
  File "/home/tsin/.config/blender/2.91/scripts/addons/urho3d_blender/__init__.py", line 46, in <module>
    from PIL import Image,ImageDraw
ModuleNotFoundError: No module named 'PIL'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/snap/blender/65/2.91/scripts/modules/addon_utils.py", line 351, in enable
    mod = __import__(module_name)
  File "/home/tsin/.config/blender/2.91/scripts/addons/urho3d_blender/__init__.py", line 50, in <module>
    subprocess.check_call([pybin, '-m', 'ensurepip'])
  File "/snap/blender/65/2.91/python/lib/python3.7/subprocess.py", line 363, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['/snap/blender/65/2.91/python/bin/python3.7m', '-m', 'ensurepip']' returned non-zero exit status 1.


```

-------------------------

dertom | 2021-03-19 01:38:16 UTC | #62

Seems that the automatic pip installation doesn't work in this case. Not sure if that is connected to the snap-installation. You might need to install pip and PIL and pyzmq manually then.
You need to locate blender's python-executable (the script thinks it is at ' /snap/blender/65/2.91/python/bin/python3.7m' can you check ) and run:

```
./python3.7m -m ensurepip 
./python3.7m -m pip install --upgrade pip
./python3.7m -m pip install pyzmq
./python3.7m -m pip install Pillow
```

EDIT: If you some reason ensure pip doesn't work, have a look here: https://pip.pypa.io/en/stable/installing/

-------------------------

ChunFengTsin | 2021-03-19 01:42:04 UTC | #63

thanks for reply！ 
I install the blender by snap under ubuntu, the folder "/snap" seems read-only.
Now I reinstall blender by download at the website, it now works well!

-------------------------

ChunFengTsin | 2021-03-19 01:49:09 UTC | #64

Hi, a new error when I click "Start Runtime", it say:  runtime exited anormally.
And a black window will launched. Some Ideas?

-------------------------

dertom | 2021-03-19 01:58:47 UTC | #65

This is actually not an error (I guess blender don't like the way I start the runtime from within blender). This is just the engine that will render the Urho3d-stuff if in urho3d-renderengine using 'Viewport Shading'.

ps: *I'm afk now. Maybe the videos can help you (not sure how outdated they are)*

-------------------------

ChunFengTsin | 2021-03-19 02:02:24 UTC | #66

Thanks For The Great Job!

-------------------------

