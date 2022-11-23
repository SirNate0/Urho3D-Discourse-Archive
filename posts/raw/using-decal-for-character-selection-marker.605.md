rogerdv | 2017-01-02 01:01:38 UTC | #1

I want to use an RTS like marker for selected entities in my game. In the Entity constructor I have this:

[code]Entity(Scene@ scn, String id)
	{
		node = scn.CreateChild(id);
		model = node.CreateComponent("AnimatedModel");
		decal = node.CreateComponent("DecalSet");
		decal.material = cache.GetResource("Material", "Materials/SelectDecalAlpha.xml");
		animCtrl = node.CreateComponent("AnimationController");

	}[/code]

And this is the called function when entity is clicked:

[code]void Select()
	{
        decal.AddDecal(model, node.position, Quaternion(0.0f,90.0f,0.0f), 0.5f, 1.0f, 1.0f, Vector2(0.0f, 0.0f), Vector2(1.0f, 1.0f));
	}[/code]

The problem is that I cant find the correct rotation for the decal, it is painted in the legs of the model (Im using Jack), and of cource, I want it on the floor. Tried many angle combinations in Quaternion(), but none worked. how can I do this?

-------------------------

codingmonkey | 2017-01-02 01:01:38 UTC | #2

mb something like that: DecalNode -> SetWorldRotation ( ParentObjectNode->GetWorldRotation() ) ?

Or you may create model prefabs (or dynamic add) child node with plane mesh with ring texture (alpha test tech). 
And then you select your unit you just enable ring-child node.

-------------------------

rogerdv | 2017-01-02 01:01:38 UTC | #3

Negative. Still painted in the legs.

-------------------------

