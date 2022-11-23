practicing01 | 2017-01-02 01:04:54 UTC | #1

Edit: Solved with the latest merge and Mike's suggestion to differentiate the filenames.

Hello, I've loaded an AnimatedSprite2D in the editor and it has artefacts (white lines at the bottom edges in the pic).  How can I get rid of these and how can I disable the filter so that it looks pixelated?  Thanks for any help.

[img]http://img.ctrlv.in/img/15/04/29/554139ac12f7d.png[/img]

-------------------------

TikariSakari | 2017-01-02 01:04:54 UTC | #2

I think Texture-class had something like set filter-mode to set to Nearest to change the Filtering from Linear to Nearest. Without actually trying, I would guess that would solve the problem of making the texture "pixelated".

Also for sprites it seems that you can set the parameter to texture according to this: [url]http://urho3d.github.io/documentation/HEAD/_urho2_d.html[/url]
[code]<texture>
    <filter mode="nearest" />
</texture>
[/code]

-------------------------

piltwort | 2017-01-02 01:04:54 UTC | #3

the lines at the bottom look like the texture is repeating.

-------------------------

GoogleBot42 | 2017-01-02 01:04:54 UTC | #4

[quote="piltwort"]the lines at the bottom look like the texture is repeating.[/quote]

Yeah I agree.  This would happen if the UV's are greater than 1.0

-------------------------

practicing01 | 2017-01-02 01:04:54 UTC | #5

I haven't set any UV's, it's an old fashioned 8x8 png.  If I place an xml with the same name as the png and the filter settings inside that, the editor cannot load the png: ERROR: Invalid sprite sheet.

-------------------------

practicing01 | 2017-01-02 01:04:57 UTC | #6

BTW the sprite animation was done with Spriter.  This means that the output is an scml file.  Perhaps this is confusing urho.

-------------------------

GoogleBot42 | 2017-01-02 01:04:57 UTC | #7

That might be it... I haven't ever heard of spriter but is looks like the error is because you are using a spritesheet and Urho3D is reading the UV's incorrectly.  I don't think that Urho3D was designed to parse this kind of file... If you are packing textures you might want to consider using the tool that Urho3D comes with (you will need to enable the building of tools when building Urho3D). :wink:

-------------------------

practicing01 | 2017-01-02 01:04:58 UTC | #8

If Urho wasn't designed to parse Spriter files then the documentation should be fixed to state which program is used for animated sprites. [urho3d.github.io/documentation/H ... ho2_d.html](http://urho3d.github.io/documentation/HEAD/_urho2_d.html)

-------------------------

Mike | 2017-01-02 01:04:58 UTC | #9

@ GoogleBot42, you can check sample 33_Urho2DSpriterAnimation to see Urho+Spriter in action
@ practicing01, I can have a look at it if you upload your files

-------------------------

practicing01 | 2017-01-02 01:04:58 UTC | #10

Thanks Mike: [url=http://wikisend.com/download/499824/kitsuneMask.7z]kitsuneMask.7z[/url]

-------------------------

GoogleBot42 | 2017-01-02 01:04:58 UTC | #11

[quote="practicing01"]If Urho wasn't designed to parse Spriter files then the documentation should be fixed to state which program is used for animated sprites. [urho3d.github.io/documentation/H ... ho2_d.html](http://urho3d.github.io/documentation/HEAD/_urho2_d.html)[/quote]

I was not aware... my mistake.

-------------------------

Mike | 2017-01-02 01:04:58 UTC | #12

The 'Invalid sprite sheet' error is due to the fact that all files have the same name.
Currently:
- if an xml file has the same name as an image file in the same repository, it is assumed that it is a texture parameter file
- if an xml file has the same name as a Spriter scml file in the same repository, it is assumed that it is a spritesheet file
So for now you have to rename your scml file differently to not confuse Urho2D.

For the not-pixelated issue, I can't reproduce. This is what I get:
[img]http://i.imgur.com/MYca7nN.png[/img]

-------------------------

