abforce | 2017-01-02 01:12:56 UTC | #1

I'm new in Urho3D and Blender. I want to export a simple model and its materials which have textures from Blender to Urho3D. I'm using the Blender add-on to do this.

This add-on only exports my model (in .mdl) and its materials (in xml), but doesn't export textures. Despite of this, it also doesn't export the armature and its animations.

Can anyone help me?

-------------------------

1vanK | 2017-01-02 01:12:56 UTC | #2

[url=http://savepic.ru/10168194.htm][img]http://savepic.ru/10168194m.png[/img][/url]

-------------------------

abforce | 2017-01-02 01:12:57 UTC | #3

[quote="1vanK"][url=http://savepic.ru/10168194.htm][img]http://savepic.ru/10168194m.png[/img][/url][/quote]

Thanks for your reply. 
Both options are enabled, still nothing... :frowning:

This is an example of exported material: (in Blender, this material has a texture, but in exported material it doesn't.)

[code]
<material>
	<technique name="Techniques/NoTexture.xml"/>
	<parameter name="MatDiffColor" value="0.64 0.64 0.64 1"/>
	<parameter name="MatSpecColor" value="0.5 0.5 0.5 50"/>
</material>
[/code]

-------------------------

1vanK | 2017-01-02 01:12:57 UTC | #4

May be u used Cycles instead Internal render?

-------------------------

1vanK | 2017-01-02 01:12:57 UTC | #5

Can u show your .blend file?

-------------------------

rasteron | 2017-01-02 01:12:57 UTC | #6

Are your textures packed (File -> External Data -> Pack.. ) ? This is a common issue that is mostly overlooked on any exporter afaik.

-------------------------

abforce | 2017-01-02 01:12:57 UTC | #7

[quote="1vanK"]Can u show your .blend file?[/quote]

My .blend file is here at this link:
[url]https://mega.nz/#!DkcmhbKL!omhJ3gCY_xHuMoxUrnzoQk-cwiR1Axee8Ky7wfzvQ_0[/url]

-------------------------

rasteron | 2017-01-02 01:12:57 UTC | #8

Yep, checked out your file and just as I have assumed. Try unpacking your textures files first then it should be good to go.

-------------------------

abforce | 2017-01-02 01:12:57 UTC | #9

[quote="rasteron"]Yep, checked out your file and just as I have assumed. Try unpacking your textures files first then it should be good to go.[/quote]

Thank you for reply. I unpacked all files, but it still doesn't copy textures to the export destination. (It only unpacked textures in the directory where my .blend file is)

Still the exported material has NoTexture technique. :frowning:

-------------------------

1vanK | 2017-01-02 01:12:57 UTC | #10

Enable "File overwrite" for rewriting old exproted materials

-------------------------

1vanK | 2017-01-02 01:12:57 UTC | #11

Also u use cycles render instead blender internal

-------------------------

rasteron | 2017-01-02 01:12:57 UTC | #12

Ok another thing and as 1vank mentioned earlier, there might be an issue in building/exporting with Cycles Render mode. Just play around with the exporter first on simple models before you move into complex stuff, and use Game Engine or Blender mode as much as possible.

To confirm that, I just tested with a ready to export blend file and textures are copied properly.

-------------------------

