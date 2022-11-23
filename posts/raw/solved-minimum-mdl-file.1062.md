sabotage3d | 2017-01-02 01:05:08 UTC | #1

Hi I am trying to write MDL from python. And I started using bits and pieces from the Urho3d Blender exporter.
I am following the docs: [urho3d.github.io/documentation/H ... rmats.html](http://urho3d.github.io/documentation/HEAD/_file_formats.html)
So far I have something like this:

byte[4]    Identifier "UMDL"
uint       Number of vertex buffers

  For each vertex buffer:
  uint       Vertex count
  byte[]     Vertex data (vertex count * vertex size)

uint    Number of index buffers
  For each index buffer:
  uint       Index count
  byte[]     Index data (index count * index size)

But the Editor just crashes when I write only this data. What is the absolute mandatory information needed for an MDL to work properly ?
Thanks in advance,

Alex

-------------------------

cadaver | 2017-01-02 01:05:09 UTC | #2

You cannot leave anything out from the "per-vertex buffer" or "per-index buffer" data blocks. Also you need to specify at least 1 geometry if you want anything to render. The rest of the file, including the bounding box, needs to be properly written too, but you can specify 0 bones and 0 morphs. I recommend looking at Model::Save() from Model.cpp as the primary reference.

-------------------------

sabotage3d | 2017-01-02 01:05:09 UTC | #3

Thank you very much. Is there any existing tool that can convert existing MDL format to ASCII ? It would be a lot easier for debugging .

-------------------------

cadaver | 2017-01-02 01:05:09 UTC | #4

None that I know of. I'd recommend either looking at a .mdl file with hex editor, looking into a model in debugger at runtime (may not yield all the data you need), or inserting debug log prints into Urho as it loads a model.

-------------------------

sabotage3d | 2017-01-02 01:05:11 UTC | #5

Thanks guys, seems to work.

-------------------------

