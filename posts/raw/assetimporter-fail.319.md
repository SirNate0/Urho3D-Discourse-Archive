Serge | 2017-01-02 00:59:35 UTC | #1

Hi, Someone can tell me what wrong with this blend file: [url]https://bitbucket.org/ptw/share/downloads/TdTest.blend[/url] ???
AssetImporter can't import it in any format (.blend or .fbx or .3ds or .dae) but it import easily any simple scenes which contains simple meshes like few cubes or spheres. I use Ubuntu x64 14.04 and Blender 2.70 and 2.69

-------------------------

misspianoforte | 2017-01-02 00:59:35 UTC | #2

The newest version of Blender (2.71) has massive fbx exporting updates. If you download the release candidate, the fbx exporter works fine. However, cycles is not yet compatible, so you will need to switch to blender render and convert your materials to not use data.

For older versions of blender, including the latest official (2.70a), a run through the Autodesk FBX Converter fixes most issues. Unfortunately, there is not a linux version of this.

I have not experimented with other export options, but the cycles materials do seem to be overall problematic. If the simple scenes you successfully imported did not have materials yet assigned, that could be an indication of where your problem was.

Hope this helps.

-------------------------

Serge | 2017-01-02 00:59:35 UTC | #3

Thank you for your answer. It's my fault with cycles. I've deleted all materials and switch to Blender render, save file, quit Blender and start it again, load my scene and export it to .fbx format. Blender 2.71 (release candidate). But in Editor this scene looks like just one big plane rotated 90 degree by X axes and absolutely empty. The problem still exist :frowning:

-------------------------

