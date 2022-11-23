rogerdv | 2017-01-02 01:01:38 UTC | #1

I have a Window with 2 child elements: one Text and one BorderImage, created in Editor. I load the layout successfully, but I cant access the BorderImage with this code:

[code]Text@ targetName = ui.root.GetChild("selname", true);
					targetName.text = ent.Find(result.drawable.node.name).Name;
					BorderImage@ tex = ui.root.GetChild("portrait", true);
					if (tex !is null)
							tex.texture = ent.Find(result.drawable.node.name).portrait;
						else
							Print("Element is null!");[/code]

I can access the Text element and change its value, but when I try to access the borderImage, I get a null value. If I change element order, placing the Text second in the child hierarchy, I can still access Text element and I dont get the null value for BorderImage , but neither can set its texture. What Im doing wrong here?

-------------------------

hdunderscore | 2017-01-02 01:01:41 UTC | #2

I tried to reproduce the error, but couldn't. Maybe share a simple scene + script demonstrating it ?

For the texture issue, you might need to set the texture coordinates after you change the texture, eg: SetImageRect or SetFullImageRect ([url=http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_border_image.html#a6b690e13125601d6e4b4fca5b4761035]doc link[/url]).

-------------------------

rogerdv | 2017-01-02 01:01:42 UTC | #3

Found another weird error, now I get a red texture, but not all the time, it appears and dissapears when Im scrolling or rotating the scene.
This is the layout: [pastebin.com/0Tc01Bna](http://pastebin.com/0Tc01Bna)
I think Im doing something wrong with the texture, because I can access the rest of the widgets, even child of a child.

-------------------------

hdunderscore | 2017-01-02 01:01:42 UTC | #4

In your code you are searching for 'portrait', but in the xml it's named 'port'. Using yours, I still didn't get the error with that name correction.

What is 'ent.Find(result.drawable.node.name).portrait' ? You need to give the texture attribute a Texture@ resource ([url=http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_border_image.html#a6d362a60f796ef51fa4238e12e4f7bcd]doc link[/url]), eg: cache.GetResource("Texture2D", "Textures/void.png").

-------------------------

rogerdv | 2017-01-02 01:01:42 UTC | #5

Yes, perhaps I changed the names, trying to find a solution, right now I confirmed that the name in code matches the name in layout. Entity.portrait is a Texture@ and it seems to be loaded correctly (at least it returns true). As I said, something is being assigned, but definitely it is not the texture Im loading, and it appears and dissapears, but only if Im displacing the camera.

-------------------------

