lazypenguin | 2017-01-02 01:14:06 UTC | #1

Hello all,

Looking for some clarification on the UMD2 custom file format. I don't have experience working directly with the lower level graphics API's so my questions may be obvious for some of the experts around here. 

1. If I have different vertex data (e.g. vertex positions/normals/tangents, uv data) for a single mesh would these need to be broken into separate vertex buffers? Would I need different index buffers?
2. What is the difference between a vertex and a vertex element?  I if I have 500 vertex positions (Vector3), is that 500 elements or 1500 (x,y,z) elements? 
3. What is the semantic index part of the vertex element bits?

Thank you!

-------------------------

cadaver | 2017-01-02 01:14:06 UTC | #2

Welcome to the forums!

1. As a rule of thumb you don't need separate buffers for separate elements, unless you for some reason want to optimize update (for example Ogre used to separate positions+normals for fast software skinning update, while keeping the rest like UV's untouched) or want to make dynamic combinations of buffers (for example instancing transforms are kept in a separate buffer, so that this buffer can be combined with different models' buffers as they get rendered)

2. A vertex element describes a part of the vertex format. If you had positions, normals and UVs in your model data format you would have 3 elements. The x,y,z coordinates are not counted as separate elements. The vertex element has only meaning for defining the format, so you would just have 500 vertices all containing the same elements as defined.

3. Semantic index comes into play when there are many of a specific element semantic in your vertex format. These are zero-based, for example if you had two UV channels they would be texcoord elements with semantic index 0 & 1.

-------------------------

lazypenguin | 2017-01-02 01:14:06 UTC | #3

Thank you for the welcome and the assistance :slight_smile:

-------------------------

