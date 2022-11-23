Jimmy781 | 2017-01-05 18:52:06 UTC | #1


Hey guys , when i add the following code in my CreateScene() method , it works well and the object is created on the scene.

`addItem(box);`

However when the scene is loaded and i try to add items aftewards , they do not show up 

`UrhoApp?.addItem(box);` 


In my Urho Application 

    public async Task addItem(string tpe)
            {

                Node modelNode2 = scene.CreateChild(tpe);
                modelNode2.Position = new Vector3(5.0f, 1.0f, 5.0f);

                modelNode2.SetScale(10.0f);

                var obj2 = modelNode2.CreateComponent<StaticModel>();
                obj2.Model = cache.GetModel("Models/Box.mdl");
                obj2.SetMaterial(cache.GetMaterial("Materials/Stone.xml"));
                obj2.CastShadows = true;
            }

-------------------------

George1 | 2017-01-07 04:01:41 UTC | #2

If you add that inside the key event, inside the Update event or inside a component it will work. 
I'm not sure it will work, if you do that on a different thread. Are you execute that on a different thread?

-------------------------

