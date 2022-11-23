godan | 2017-01-02 01:05:42 UTC | #1

I was wondering what the logic behind the name "StaticModel" is? As a user coming from Unity, I keep expecting the MeshFilter (the asset you want to display), MeshRenderer (the class that handles materials, and other rendering options) pattern. Would this pattern make sense in Urho?

Some other specific questions:

- What is "static" about a StaticModel? For instance, the DynamicGeometry sample implies that the way to create procedural geometry is to modify the vertex/index buffers of a StaticModel, which to me seems counter intuitive.
- I should probably just test this on my own, but is the Model easily swapped out of the StaticModel? That is, can I simply point the StaticModel component to a different Model and have it render it?
- If yes to the above, then what is "model"-ish about a StaticModel?

This is pretty minor point, but it's something I've been thinking about. My usage of Urho involves lots of runtime geometry creation/user control of what's on screen, so this comes up often.

-------------------------

cadaver | 2017-01-02 01:05:43 UTC | #2

Static as in not skinning or morphing. The class names talk about built-in Urho functionality; if you use access on the vertex buffer level you can animate a StaticModel as much as you wish.

The filter / renderer separation is not really needed in Urho, as the "filter" part in Unity is basically just storing the mesh resource attribute. Call StaticModel::SetModel() if you want to change the model resource being rendered.

-------------------------

godan | 2017-01-02 01:05:44 UTC | #3

Thanks, makes sense!

-------------------------

