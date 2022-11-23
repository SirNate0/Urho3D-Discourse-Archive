Lumak | 2017-01-02 01:13:25 UTC | #1

I created a repository for a simplified sponza scene with Urho3D .mdl models here [url]https://github.com/Lumak/Urho3D-Assets[/url] derived from Crytek's obj file.
For a full version, there's a link on the respository to Crytek's obj file which you can download.
The scene file is SponzaSimple/SceneSponzaSimple.xml file.

Probably useful if you're doing any kind of GI testing.

-------------------------

Egorbo | 2017-01-02 01:13:25 UTC | #2

Looks great, Lumak!!

Screenshot:
[img]https://habrastorage.org/files/3ae/328/335/3ae328335fa34814ad0f55e8ea411146.png[/img]

-------------------------

Lumak | 2017-01-02 01:13:26 UTC | #3

I hope you find it useful.

-------------------------

weitjong | 2017-01-02 01:13:26 UTC | #4

Thanks for that! Keep it up. I think it will be even more useful for newcomer if you add a short description on how it was done, i.e. through which importer tool and using what parameters, etc.

-------------------------

dragonCASTjosh | 2017-01-02 01:13:26 UTC | #5

Any chance for a PBR version :slight_smile:

-------------------------

Lumak | 2017-01-02 01:13:26 UTC | #6

[quote="weitjong"]I think it will be even more useful for newcomer if you add a short description on how it was done, i.e. through which importer tool and using what parameters, etc.[/quote]

That might be useful.

[size=150][b]AssetImporter - how to import scene asset:[/b][/size]
[b]Setup:[/b] using Crytek's sponza.obj model as an example.
-create a bin\Sponza folder
-copy sponza.obj to bin\Sponza folder along with *.mtl and all its *.tga files
-open a command line in your build project\bin\tools folder
-type:

  AssetImporter.exe [b]scene [/b] ..\Sponza\sponza.obj ..\Sponza\SceneSponza.xml

[b]note*[/b] the use of the [color=#0000FF][b]scene [/b][/color] option.
-open Editor (bin/Editor.bat), open SceneSponza.xml and verify the scene and make any adjustments.


[quote="dragonCASTjosh"]Any chance for a PBR version :slight_smile:[/quote]
Not interested in doing this. I just wanted to provide a common, prevalent scene typically used for gi testing.

-------------------------

weitjong | 2017-01-02 01:13:26 UTC | #7

Thanks for the quick response. Although I was actually hoping the brief notes to be somewhere in your asset repo instead of this forum post, for the benefit of your reader who may visit your repo first and not this forum.

-------------------------

Lumak | 2017-01-02 01:13:28 UTC | #8

[quote="weitjong"]Thanks for the quick response. Although I was actually hoping the brief notes to be somewhere in your asset repo instead of this forum post, for the benefit of your reader who may visit your repo first and not this forum.[/quote]

Also not interested in doing this.  I did, however, added a link to this thread on the repository.

-------------------------

