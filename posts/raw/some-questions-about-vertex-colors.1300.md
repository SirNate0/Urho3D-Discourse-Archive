Modanung | 2017-01-02 01:06:41 UTC | #1

I made a model in Blender and painted its vertices in several layers. When loading the model with a vCol material in Urho3D it shows the vertex color channel that was selected during export. This suggests only one layer is exported. Is this assumption correct? The exporter doesn't mention vertex colors in its report.

What I would like to do is mix the layers into any colour by adding up the vertex color layers and then multiplying with a dark layer. How should I access and write these colours?

-------------------------

friesencr | 2017-01-02 01:06:41 UTC | #2

I think urho only supports 1 color channel for vertex data.  Custom vertex attributes would be a nice add.

-------------------------

