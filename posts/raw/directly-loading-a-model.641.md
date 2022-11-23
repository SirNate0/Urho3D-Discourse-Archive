Vivek | 2017-01-02 01:01:50 UTC | #1

I see a custom file format for models, Can I import my own format directly to urho3d rather using .mdl format.
What api should i use to set vertices/normals/UVs and other attributes directly.

-------------------------

cadaver | 2017-01-02 01:01:50 UTC | #2

Welcome to the forums!

You can define a Model in code by filling vertex & index buffers with your data. As Urho doesn't support completely free-form vertex declarations, the data has to correspond to the Urho vertex element conventions, for example the Position element is always first in a vertex (if included) and it needs to be a Vector3. See the 34_DynamicGeometry example [github.com/urho3d/Urho3D/blob/m ... ometry.cpp](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp), which does two things:

- animating vertices of existing models 
- creating a model from scratch and assigning it to a StaticModel component

For a more involved example which loads an Ogre mesh file and stuffs it to a Model resource, see the tundra-urho3d project: (the function DeserializeFromData() at the end of the file is the top level function, which gets the Ogre .mesh file as a binary buffer and produces a Model object)
[github.com/realXtend/tundra-urh ... hAsset.cpp](https://github.com/realXtend/tundra-urho3d/blob/master/src/Plugins/UrhoRenderer/Ogre/OgreMeshAsset.cpp)

-------------------------

Vivek | 2017-01-02 01:01:50 UTC | #3

Thanks thats what i needed.

-------------------------

