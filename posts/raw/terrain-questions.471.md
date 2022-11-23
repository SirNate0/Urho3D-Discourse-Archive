rogerdv | 2017-01-02 01:00:41 UTC | #1

Im trying to create a terrain and I have a few questions. Do I need a node for the terrain? I noticed that menu places terrain directly in Scene, but then I cant add a rigid body or collision shape to it. the same heightmap produces different results in bot cases. Second question is: there is any restrictions to the heightmap image? I have one here that I cant use.

-------------------------

weitjong | 2017-01-02 01:00:42 UTC | #2

For the first question. The Terrain class is a component. As all the other components, you would usually need it to be attached to other node rather than to the root scene node directly, although there are exception. The Editor does not know what is user intention when creating a new component, it simply attach the newly created component to the "current" node. If your current node happens to be a root "Scene" node then the Editor will just dutifully attach it there. That is, before creating components, you should create the node hierarchy first. RigidBody and CollisionShape are components too, so the above also apply to them. They can only be attached to a node and not to the "Terrain" itself. I hope I did not misinterpret your question and that my reply answers your question.

[quote="rogerdv"]the same heightmap produces different results in bot cases[/quote]

Not sure if I understand your statement. Are you saying that the results are different between having the component attached to a scene node and having it attached to any node? If so, then the difference could be caused by the relative position of that other node in respect to the scene node.

For the second question. The heightmap texture is being processed by STB third-party library. So, the restriction is more set by this library, such as it cannot handle progressive JPG. Below are what it can handle:

JPEG baseline (no JPEG progressive)
PNG 8-bit only
TGA (not sure what subset, if a subset)
BMP non-1bpp, non-RLE

-------------------------

rogerdv | 2017-01-02 01:00:42 UTC | #3

Sorry for not being explicit, becasue the effect is weird, and probably related to position. When added directly to scene, the terrain "looks good". If I create a node, seems as if I were looking to a panoramic picture, it seems curved and stretched in the vertical axis.

-------------------------

weitjong | 2017-01-02 01:00:42 UTC | #4

I cannot imagine or explain how "that" could happen, may be other can.

EDIT: make sure your node's scale is set to 1 or set to a same number of unit on all three axes.

-------------------------

rogerdv | 2017-01-02 01:00:42 UTC | #5

Hmm, probably my mistake, cant reproduce the effect now. I noticed soemthing, when you remove the terrain, the editor view is not refreshed and still shows the terrain.
I read in a post that a terrain editor was in the works, any estimated about when is it going to be integrated?

-------------------------

weitjong | 2017-01-02 01:00:43 UTC | #6

The "remnant" terrain is still being rendered because the generated temporary terrain patches (patch nodes and their TerrainPatch components) are not automatically removed as child nodes of the affected parent node. Probably the Editor should do this automatically, so I think we can consider this as a bug. You can see those generated temporary nodes + components by toggling an option in the Editor's preferences, "Show temporary objects" under "Hierarchy". It should remain off by default because showing temporary objects may slow down the Editor performance quite significantly.

-------------------------

