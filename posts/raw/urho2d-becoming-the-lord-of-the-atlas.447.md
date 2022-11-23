zakk | 2017-01-02 01:00:29 UTC | #1

Hello,

After succesfully animated a sequence of images with the scml method, i'd like to use the atlas method. I think it's far better to load only one texture for a sequence of sprites than a lot of individuals files (for avoiding a waste of video memory and lot of i/o for each file).

I tried different things, but couldn't succeed in using atlas file.

According to the the documentation of Urho2D, here is what i understand:

- The atlas has the same name than the spriter file, only difference is the [b].xml[/b] suffix.
- If the atlas xml file (and matching texture file) is present, only the scml file must be present. Individuals textures files can be discarded (but should be keep somewhere, for further editing with spriter).
- With an atlas, the Urho cache resource is still an ?AnimationSet2D? , and [i]not[/i] a ?SpriteSheet2D? (as i thought at the beginning).

That said, and after i have failed to use correctly atlas (always errors with scml file loading, when an atlas file is present), i decided to experiment with GoldIcon sample data.

I've downloaded latest TexturePacker for Linux (version 3.4.0) and use the ?Generic XML? framework as a new project.
Then i add the 5 png, and chose a 128x128 texture file size.
Then i chose xml and png file name, and click on ?publish sprite sheet?.
All is exported without error or warning.

The xml format seems to have changed.
Here is what i got:

[code]
<TextureAtlas imagePath="GoldIcon_jseb.png" width="124" height="126">
    <sprite n="1.png" x="2" y="2" w="60" h="60" pX="0.5" pY="0.5" oX="2" oY="2" oW="64" oH="64"/>
    <sprite n="2.png" x="2" y="64" w="42" h="60" pX="0.5" pY="0.5" oX="11" oY="2" oW="64" oH="64"/>
    <sprite n="3.png" x="90" y="64" w="17" h="60" pX="0.5" pY="0.5"/>
    <sprite n="4.png" x="64" y="2" w="58" h="60" pX="0.5" pY="0.5" oX="3" oY="2" oW="64" oH="64"/>
    <sprite n="5.png" x="46" y="64" w="42" h="60" pX="0.5" pY="0.5" oX="11" oY="1" oW="64" oH="64"/>
</TextureAtlas>
[/code]

For reference, here is the xml format of the GoldIcon.xml in the samples:

[code]
<TextureAtlas imagePath="GoldIcon.png">
    <SubTexture name="1" x="2" y="2" width="60" height="60" frameX="-2" frameY="-2" frameWidth="64" frameHeight="64"/>
    <SubTexture name="2" x="64" y="2" width="42" height="60" frameX="-11" frameY="-2" frameWidth="64" frameHeight="64"/>
    <SubTexture name="3" x="108" y="2" width="17" height="60"/>
    <SubTexture name="4" x="2" y="64" width="58" height="60" frameX="-3" frameY="-2" frameWidth="64" frameHeight="64"/>
    <SubTexture name="5" x="62" y="64" width="42" height="60" frameX="-11" frameY="-1" frameWidth="64" frameHeight="64"/>
</TextureAtlas>
[/code]

Then, i launch my sample, and get the same errors i've got with my own sprites:

[quote]
[Sun Sep 21 01:00:10 2014] ERROR: Could not load sprite GoldIcon/2.png
[/quote]

So i think it's a format problem.
Which version of TexturePacker do you use, and if it's the same than me, what export framework should i use ?
Why this strange error message, related to a file use by scml loader ? Atlas loader should not care about scml files, and use only its own texture (well? at least, i think so :slight_smile: ).

Of course, if i remove/rename the xml file, all is working well. So, there's no problem with the file ?GoldIcon/2.png? (that means that it's not a problem with the scml file, anyway i did'nt change it at all).

Thank you for helping :slight_smile:

-------------------------

Mike | 2017-01-02 01:00:29 UTC | #2

zakk, example 33_SpriterAnimation already uses the atlas. You can test it by removing all the images in the imp folder, just keep the atlas (imp_all.png).
I will update the documentation, it is the material file (imp_all.xml) that must match the atlas name, not the spritesheet file (imp.xml). Sorry for confusion.

-------------------------

zakk | 2017-01-02 01:00:29 UTC | #3

Hello,

Thank you for answering.

I've found where the problem was.
I was exporting the atlas with TexturePacker, using [i]Generic XML[/i] framework.
That's bad. Reading again the Urho3D documentation, i've seen that the correct framework was [i]sparrow/starling[/i] (as the atlas is in starling format).

To sum up:

- TexturePacker : export with sparrow/starling.
- Individuals textures files are not required, as long as you've got atlas xml file, and (of course) the associated texture.
- The atlas xml file and the scml file must have the same prefix (foo.xml and foo.scml).

about the points you've mentionned:
- the texture file of the atlas and its associated material file must have the same prefix (foo_tex.png and foo_tex.xml).
- but material file is optionnal (i don't use it for now).

What do you call ?sprite sheet? ? Is it the atlas xml associated to the atlas texture ?
I guess it's related to the resource SpriteSheet2D. I wouldn't be surprised that cache:GetResource create it automatically when it finds an atlas, trying to load scml file.

-------------------------

Mike | 2017-01-02 01:00:29 UTC | #4

In fact documentation was accurate, I'll revert it back.
And yes, ?sprite sheet? is the atlas xml associated to the atlas texture.

-------------------------

seajackal | 2017-09-27 22:26:04 UTC | #5

Hi. What is the reason that "imp_all.png" and "imp.xml" where removed? 
It seem to still work anyway (retrieved them from the git history). 
Thanks

-------------------------

Mike | 2017-09-29 20:51:11 UTC | #6

I don't know why, it's been awhile.

-------------------------

