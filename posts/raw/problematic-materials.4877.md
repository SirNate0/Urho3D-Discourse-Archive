Leith | 2019-01-29 08:37:12 UTC | #1

I have just used AssetExporter to export an FBX model to Urho's file format.
When I load it into my sandbox application, which has a single Directional Light and a single Zone with soft ambient lighting, the character's materials all appear somewhat dark.
Now when I rotate or move my character away from the world origin, it flickers very dark, and then becomes completey black!

So I tried hacking the material(s) to disable lighting, and sure enough, the problem disappeared.
Then I narrowed the problem down to the NormalMaps.

They are 2048x2048 pixel PNG images.
I tried using GIMP to convert them to DDS with DXT1 compression as advised in the Docs, and adjusted my material files to account for the change in filepath, but this failed to remedy the issue.

I've uploaded the exported files, and the original fbx file, hoping someone is willing to help me out, or at least confirm the issue with regards to normal maps :slight_smile:
 
https://www.dropbox.com/s/3r6xdfkv6gsnnk5/Female.zip?dl=0

-------------------------

Leith | 2019-01-29 08:37:22 UTC | #2

Never mind, I found the answer.

AssetExporter does not by default generate or export vertex tangent data - even if the Material(s) specify a normal map. The solution is to provide the -t argument when performing the export. 

[quote]Models using a normal-mapped material need to have tangent vectors in their vertex data; the easiest way to ensure this is to use the switch -t (generate tangents) when using either AssetImporter or OgreImporter to import models to Urho3D format. If there are no tangents, the light attenuation on the normal-mapped material will behave in a completely erratic fashion.[/quote]

The model DID have tangent information - it did not need to be generated by the exporter - yet the exporter by default will silently drop that information from the vertex data.

It would be nice if the exporter was clever enough to notice that one or more materials required tangents, and provided them on that basis?

-------------------------
