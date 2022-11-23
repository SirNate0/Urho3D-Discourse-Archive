Mike | 2017-01-02 00:59:23 UTC | #1

I'm trying to create a skybox from a dds cubemap using this material resource file:

[code]
<material>
    <technique name="Techniques/DiffSkybox.xml" />
    <texture unit="diffuse" name="Textures/Cube.dds" />
    <cull value="none" />
</material>
[/code]
I've also tried many other solutions but can't get it to work.

-------------------------

cadaver | 2017-01-02 00:59:24 UTC | #2

The engine does not at the moment support loading a cubemap directly from one dds file, rather the individual faces must exist as separate images (with same size and format, obviously) and an xml file that points to the face files. The cube texture resource is loaded using that xml file. See the example Skybox.xml and the BrightDay1_xxxx.dds textures in the Textures folder.

-------------------------

Mike | 2017-01-02 00:59:24 UTC | #3

OK, thanks, will continue to use current xml files.

-------------------------

Mike | 2017-01-02 01:00:23 UTC | #4

Mant thanks cadaver for adding cubemap support.

This is a great improvement for me as previously skyboxes often failed to render on my old graphic card.  :slight_smile: 

I've done some tests (on android and linux) with ATI CubeMapGen (vertical cross) - OGL - DXT1 and everything works perfecly, except for negative Z which is flipped.

I've tried to:
- comment the VerticalFlip() in OGLTextureCube.cpp but then the face turns white.
- perform the vertical flip inside CubeMapGen: it then works (the face is accurately rendered) but the seams become obvious for this face.
I've also tried to alter various settings in CubeMapGen, especially the layout.

-------------------------

cadaver | 2017-01-02 01:00:23 UTC | #5

Can you supply an example vertical cross file?
Also, are you using ETC1 format on Android? For ETC & PVRTC, the vertical flip is not implemented yet.

EDIT: never mind, what I didn't realize is that the negative Z needs to be rotated 180 degrees instead of flipping.

-------------------------

cadaver | 2017-01-02 01:00:23 UTC | #6

Vertical cross layout loading should be fixed now.

-------------------------

Mike | 2017-01-02 01:00:24 UTC | #7

Awesome! Everything works perfectly, thanks again  :stuck_out_tongue:

-------------------------

