evolgames | 2020-02-23 08:49:48 UTC | #1

I've been trying to get models from Mixamo to work with U3D. I know some of the samples use those models, like the mutant.

I've been able to use AssetImporter to convert an .fbx/.dea/.fbx (for unity) to .mdl. All of them are having issues with the UV Mapping (I guess) causing the material to wrap totally wrong. Tried this with different models. I have NO problems with animation or character creation as I've followed the Character Demo. The problem is strictly the material. I also only really need a simple Diffuse, but it'd be nice to get everything working.

I tried [this](https://github.com/fredakilla/UrhoTournament/wiki/Import-mixamo-3D-model-to-Urho3D), as well as [this](https://github.com/reattiva/Urho3D-Blender), and am still getting the same issues.

In the Editor, importing the .fbx, unconverted to .mdl, brings it up perfectly with no extra steps. I want to programatically create my project by instancing objects/models/light/etc, so I'm assuming the Editor is not going to be much use, but it does pull things up correctly. (I'm aiming to make a simple dungeon crawler with procedural areas/spawns). Here's how it appears immediately:

![Screenshot|690x369, 75%](upload://fwZB71qQKXs120lAB9E1BMqFIc5.png) 

And here is what I keep getting from all of the other methods (some of which are up to 5 years old):
![Screenshot-1|690x369](upload://h4NFHvaUEMzIOcIbLZBbfkDKzbx.jpeg) 

Mind you, those other methods require many more steps, and I'm not getting results with them. The video accompanying one of them references a model that is not longer on Mixamo and the hierarchy seems to be different as well.

I'm a noob but it looks like the Editor is just an U3d program being run by the player?
If that is the case, how is it importing an .fbx perfectly?
Mixamo's license disallows this, but could I potentially load .fbx's rather than .mdls?
Is the editor *creating* an .mdl when the .fbx is imported using AssetImporter?
Is there a way to export what the editor has done to a .mdl?

I took a look at some of the .as scripts for the editor, but I wasn't able to make sense of them.

Assuming the Editor does use AssetImporter, is there a way I can just use the same exact commands/methods to produce a .mdl with correctly mapped materials? 

Because the Editor gets everything set up automatically and that's what I'm after. Mixamo models need to be scaled by a factor of .001, by the way.

-------------------------

George1 | 2020-02-23 02:55:55 UTC | #2

I remembered there used to be a step by step procedure on the forum.  You need to search for it.

-------------------------

evolgames | 2020-02-23 03:00:41 UTC | #3

@George1  I've seen that thread and it didn't help. It has steps for Maya. Otherwise porting directly from Mixamo all it says is to use the AssetImporter and then fix it up in Blender. There is no step-by-step for the material.

Either way, how is the Editor doing everything without using Blender/Maya and getting a perfect model loaded from just the unaltered .fbx? I'd much prefer to find out if there is a way to do what the Editor is doing, rather than follow years old instructions for using third-party applications and Add-ons (which are not updated).

-------------------------

evolgames | 2020-02-23 04:24:09 UTC | #4

Ok nevermind I figured it out.

Here are the steps:

1. Download .fbx for unity from Mixamo
2. Import into Editor (if there are spaces in the filename it will say: "failed to execute assetimporter to import model", so rename to something convenient) 
3. It'll make everything for you. Find your .mdl in bin/Data/Models, your Materials in /bin/Data/Materials and Textures in /bin/Data/Textures
4. With the models I've tried, it'll give you two materials with the character index (from mixamo), so you'll get something like: Ch25_Body.xml and Ch25_body1.xml. They are different. I don't know why it's split in two but you need both.
5. When loading model via code, do the following (for Lua):

```
mat1 = cache:GetResource("Material", "Materials/Ch25_Body.xml")
mat2 = cache:GetResource("Material", "Materials/Ch25_body1.xml")

object:SetMaterial(0, mat1)
object:SetMaterial(1, mat2)
```

6. If you want animations, add them to the Mixamo model before downloading, and the Editor will produce .ani files for you with the model. Use the CharacterDemo as a guide to playing the animations. It looks like it will create a .ani even if there is no animation.

I guess you could import to Blender to adjust the geometry (Decimate, optimize the mesh, whatever) and then import the resulting .fbx into the Editor and follow the steps above. But the main thing is that to get your .mdl and everything working from Mixamo there is absolutely no need for Blender, the Urho3d-Blender add-on (not available past ver. 2.79 anyway), or even the AssetImporter.

This makes things much easier. Fire up Editor. Import. Everything is ready.

P.S. I can't say this works for models/formats from anywhere besides Mixamo. But if you want to use the large collection of models and animations they have, this seems like the best way. Also, the wall below is a placeholder lol.

![Screenshot-2|690x369, 75%](upload://uMI8qb96AH9j8yoQrc2UjYzpAzI.jpeg)

-------------------------

George1 | 2020-02-23 06:07:12 UTC | #5

https://github.com/fredakilla/UrhoTournament/wiki/Import-mixamo-3D-model-to-Urho3D

http://discourse.urho3d.io/t/ready-to-use-models-with-animations/2147/1

Scroll down under the same thread.  There is a direct way...
You have to spin the model by 180 degree.

-------------------------

evolgames | 2020-02-23 06:47:33 UTC | #6

Oh alright I see. I noticed the Z forward was backwards.

Yeah so from what I understand I was just missing that I needed to apply both materials (Ch25_Body.xml and Ch25_body1.xml) to the mesh. It seems obvious now, but with the exporter add-on and the one [video](https://www.youtube.com/watch?v=moiUS0TK6Vk&t=207s) it really makes it seem like there needs to be some UV work to get anything right. And so I was chasing ghosts. Everything is fine as is.

You're right. AssetImporter works great. Here's what I just did:

1. Download Mixamo .fbx
2. Open in Blender. Did nothing. Export to .fbx but switch to Z forward (I'm pretty sure I can just do an adjNode here, though)
3. Run AssetImporter for the model, then for the animation
4. Load like normal but set both materials

Luckily this is a very simple process afterall. Looks like the Editor is just automatically apply both of those materials after importing.

-------------------------

