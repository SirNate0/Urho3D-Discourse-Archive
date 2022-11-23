rogerdv | 2017-01-02 01:02:15 UTC | #1

I tried to test the method to attach a model to a bone. First I tried this:

[code]StaticModel@ item = player.model.skeleton.GetBone("Bip01_R_Hand").node.CreateComponent("StaticModel");
    if (item.Load(cache.GetFile("Models/longsword.mdl")))
      Print("model loaded ok");[/code]

The model is beign loaded, but it is not visible. I also tried creating a child noide, and then creating the model component there instead of the bone node, but the result is the same. Whats the correct method to do this?

-------------------------

Mike | 2017-01-02 01:02:15 UTC | #2

Use a node for each model and parent them using:
[code]childNode->SetParent(parentNode);[/code]

-------------------------

rogerdv | 2017-01-02 01:02:15 UTC | #3

[code]Node@ itn = player.model.skeleton.GetBone("Bip01_R_Hand").node.CreateChild("item");
		itn.parent = player.model.skeleton.GetBone("Bip01_R_Hand").node;

    StaticModel@ item = itn.CreateComponent("StaticModel");
    if (item.Load(cache.GetFile("Models/longsword.mdl")))
      Print("model loaded ok");[/code]

Negative, the model is not displayed. Tried adding position and scale:

[code]		
    itn.position = Vector3(0,0,0);
    itn.scale = Vector3(0.08,0.08,0.08);
  [/code]

But doesnt works neither.

-------------------------

szamq | 2017-01-02 01:02:15 UTC | #4

I'm guessing that you also need to set Material to the StaticModel

-------------------------

rogerdv | 2017-01-02 01:02:15 UTC | #5

Negative. Next guess?

-------------------------

codingmonkey | 2017-01-02 01:02:15 UTC | #6

1. new child node depends on parent scale, maybe you need to make - upscale or downscale your new node for several times to see it.
2. new node.setEnable(true)

-------------------------

rogerdv | 2017-01-02 01:02:16 UTC | #7

Still cant see it.

-------------------------

Mike | 2017-01-02 01:02:16 UTC | #8

To get the bone node, you don't need to access the skeleton, you can use:
[code]parentNode->GetChild("boneName", true);[/code]

Did you check in the Editor the result to help you debug (saving your scene and loading it in the Editor)?

-------------------------

rogerdv | 2017-01-02 01:02:16 UTC | #9

SAved the scene and checked with editor. The child node is created, but the StaticModel component is empty, no mesh is loaded on it.

-------------------------

Mike | 2017-01-02 01:02:17 UTC | #10

Create childNode + StaticModel component before parenting to parentNode.

-------------------------

rogerdv | 2017-01-02 01:02:21 UTC | #11

Found the problem. 
[code]item.Load(cache.GetFile("Models/longsword.mdl")[/code]
 doesnt works, the correct way is this:
[code]item.model = cache.GetResource("Model", "Models/Jack.mdl");[/code]

-------------------------

