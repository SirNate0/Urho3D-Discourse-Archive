AReichl | 2017-01-02 01:08:42 UTC | #1

Hi,

i would like to use Urho3D as a stand-alone viewer for .stl (CAD) data.

1:  how do i import .stl files?
2:  how can i reduce the vertex count without going through an external program?

-------------------------

rasteron | 2017-01-02 01:09:32 UTC | #2

Hey AReichl,

1. You can use AssetImporter to import stl files to Urho3D or via the Editor: File -> Import Model.
2. Afaik the current version does not support model decimation or vertex count reduction.

Hope that helps.

-------------------------

