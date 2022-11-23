Jimmy781 | 2017-01-06 20:04:22 UTC | #1

Hey guys , 

I have a bunch of objects on my scene and i want to animate them on selecting them . 

i think i need to set an id for each and maybe add them to a list . Not sure to implement this yet but the first issue would be how to select them on the scene .

var mushroom = scene.CreateChild ("Mushroom" , id);

In my createScene() function , i subscribed to touch events -
 
Input.SubscribeToTouchEnd(onObjSelected); 

however i have no idea to check if an object was selected and how to process it .

E.g : 

    var rand = new Random();
    			for (int i = 0; i < 200; i++)
    			{
    				var mushroom = scene.CreateChild ("Mushroom");
    				mushroom.Position = new Vector3 (rand.Next (90)-45, 0, rand.Next (90)-45);
    				mushroom.Rotation = new Quaternion (0, rand.Next (360), 0);
    				mushroom.SetScale (0.5f+rand.Next (20000)/10000.0f);
    				var mushroomObject = mushroom.CreateComponent<StaticModel>();
    				mushroomObject.Model = cache.GetModel ("Models/Mushroom.mdl");
    				mushroomObject.SetMaterial (cache.GetMaterial ("Materials/Mushroom.xml"));
    			}

-------------------------

1vanK | 2017-01-06 21:04:49 UTC | #2

https://github.com/1vanK/Urho3DOutlineSelectionExample

-------------------------

George1 | 2017-01-07 04:18:45 UTC | #3

The easiest way is to use RayCast to find the hit drawable. Then get the node source or component, dependent on how you code it, and add that node or component to the list. 

After that just turn the DrawDebugGeometry(true, false) for the selected components. This show the selected component by boundingbox lines.

Or use 1vanK example for fancy outline.

-------------------------

