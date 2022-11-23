Krathoon | 2017-01-02 01:00:40 UTC | #1

I am running into problems loading this free art into the Urho3D editor:

[opengameart.org/content/free-3d- ... art-pack-1](http://opengameart.org/content/free-3d-platformer-art-pack-1)

I am loading the example file.

I have tried exporting in different formats. It seems like the textures are not loading properly in the Urho3d editor, I get bright colors and the grass will be white.

Could somebody try it with 3ds and fbx exports from Blender and see if they can tell what the problem is? I am using Blender 2.71.

-------------------------

Krathoon | 2017-01-02 01:00:40 UTC | #2

Looking at the import from fbx, it looks like textures did not import properly and the techniques are off. I will see if I can find some simpler models to import.

-------------------------

friesencr | 2017-01-02 01:00:40 UTC | #3

I just tried importing a scene of a exported fbx.  The images didn't copy over.  I can't remember the rules for when it copies textures on import.  So I manually copied over the images to the Textures folder and reimported.  However some of the images are progressive jpg.  STB images, our image encoder/decoder, doesn't support progressive jpg.  Batch saving the images should fix that problem.  I can look more into the rules for copying textures later but don't have time this exact moment.

-------------------------

Krathoon | 2017-01-02 01:00:40 UTC | #4

Ah. I forgot to mention that. I did get the progressive jpeg problem as well and fixed it by saving them in MS Paint.
Could you point me to where the texture rules are at? Is it the assimp docs? I can check into it as well.

-------------------------

Krathoon | 2017-01-02 01:00:40 UTC | #5

I notice that, if I switch the techniques on some of the materials on some of the models to diffunlit, the textures look closer to what is in Blender. There seems to be some lighting issue here that I don't understand.

-------------------------

Krathoon | 2017-01-02 01:00:40 UTC | #6

I am now getting the majority of the models to match up with blender. I had to set their materials to DiffNormalEmissive and add their normal texture and add the diff texture to their emissive entries. It can't get the punch blocks to look right, however. There is also a metal material on the bright colored bridges the looks like it needs to be removed.

-------------------------

cadaver | 2017-01-02 01:00:40 UTC | #7

The conversion path from Assimp materials to Urho materials is far from perfect; it's based on quite simple rules like "if there is both diffuse and normal map, choose DiffNormal technique".

Concrete suggestions (based on similar concrete rules) to improve it are welcome, you can for example submit an issue of them. If doing so, please include link(s) to the asset/scene files and pictures of how it should look. In some cases Assimp gets faulty input data, for example normal texture goes to specular channel, in which case Urho can do little to correct the situation.

-------------------------

Krathoon | 2017-01-02 01:00:41 UTC | #8

After playing around with the exports some more, it seems like COLLADA works the best. The rest did not export all the pipe models. Still, with COLLADA, I have to manually set the textures.

Since COLLADA is an older format, it is kinda funny.


Edit: It turns out that the missing pipes were actually there. They were just hidden. I set them to NoTextureAlpha and they popped up. So, fbx is still the champion.

-------------------------

Mike | 2017-01-02 01:00:42 UTC | #9

I've checked the blend files, issues come from them as they have many flaws: images not linked to materials, 'Normal map' not checked in 'Image Sampling', junk materials and images, incorrect texture paths here and there..., so results may vary depending on the way blender exporters are dealing with these flaws (garbage in, garbage out).

When using blend files from the net, I would recommend:
- thoroughly cleaning the files before exporting them, this can save headaches later
- using Urho3D Blender add-on for export, will be faster and more accurate

-------------------------

Krathoon | 2017-01-02 01:00:43 UTC | #10

Ok. I'll see if I can find some better quality files.

Is there a fast way to clean the files, or would it all be manual?

-------------------------

thebluefish | 2017-01-02 01:00:43 UTC | #11

From my experience, there's really no automated way to clean files from the internet. These flaws typically come from other artists not doing things properly. While there is much freedom in creating a model to look decent in Blender, the settings needed to make the same model look good in Urho3D (as well as pretty much any other game engine) are a bit more restrictive. 

Your best bet is to create a list of things that need to be checked before export. If you can identify common issues, you can better streamline the process of cleaning up the project before export.

-------------------------

Krathoon | 2017-01-02 01:00:46 UTC | #12

Anyone know of some free blender test scenes that would import properly in Urho3d? There are some scenes from the examples, but I was looking for something more elaborate, something that would cover everything that could be imported into Uroho3d from a blender scene.

It would be great to have something to work from.

I have been looking at the guide with the Urho3d exporter to get a better idea of what pulls over. I'll take a look at the code as well.

-------------------------

Mike | 2017-01-02 01:00:46 UTC | #13

Blender test scenes that you will find on the web, like the Yo Frankie project or Blendswap scenes for example, are designed for the Blender Game Engine (all settings for materials, shaders, physics... work in this context, not outside of Blender). Any asset will need some cleaning and tweaking. If you follow the guide from the exporter add-on, you will have a basic idea of what to check/modify to achieve the expected results (most of the settings take place in the 'Material' and 'Texture' properties).

-------------------------

