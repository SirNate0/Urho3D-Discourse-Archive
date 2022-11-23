szamq | 2017-01-02 00:58:22 UTC | #1

Urho editor is great for tweaking some values, but when it comes to design all scene, modify certain triangles in mesh, it is better to use blender or other modeling program. 

Urho3d has great option to import scene and it saves all node structure,scale,position etc. But by default after importing to urho, it creates only StaticModel and Lights. And all other data you need to set manually in urho like collision shapes, custom scripts. Each time you modify the scene!

I was thinking about extending this so we could import scene with additional data. Right now I tested probably the easiest one which looks at node names and perform action basing on switches in names, for example like:

node name:
Suzanne__cm__dd

__cm -add collision mesh
__dd - delete drawable (invisible walls, triggers)

It works nice and saves time. The only minus of that solution is that the nodes have ugly and long names (you can imagine switch like __s_FlickeringLight which means to add custom script called FlickeringLight). So i will expand this and share but first I would like to know your opinions about that. Maybe there is a better way to achieve it than putting everything in the names (tried with custom properties but they are not exported with collada).

The positive of including switches in names is that it is very easy to implement. Just one edit in EditorImport.as after importing the scene which iterates over all nodes, like this:
[code]           
			skipMruScene = true; // set to avoid adding tempscene to mru
			LoadScene(tempSceneName);
			
			//Here goes additional code
			//Iterate over all nodes and search for tweaks

			Array<Node@> nodes=editorScene.GetChildren(true);
			for (uint i = 0; i < nodes.length; ++i)
			{
				if(nodes[i].name.Contains("__cm",false)) //Collision Mesh
				{
				    RigidBody@ body = nodes[i].CreateComponent("RigidBody");
					CollisionShape@ shape = nodes[i].CreateComponent("CollisionShape");
					StaticModel@ model=nodes[i].GetComponent("StaticModel");
					shape.SetTriangleMesh(model.model, 0);
				}
				
				if(nodes[i].name.Contains("__dd",false)) //Delete Drawable
				{
					nodes[i].RemoveComponent("StaticModel");
				}
			
			}
[/code]

Let me know what you think

-------------------------

Hevedy | 2017-01-02 00:58:22 UTC | #2

Yes this need
- Triggers
- Collisions
Some like Hammer / Radiant for add that with basic vertex modeler to give the form to the zones. 
And logics using c++/as/lua declared functions (like in hammer) entities types and others.

-------------------------

cadaver | 2017-01-02 00:58:23 UTC | #3

The editor lends itself better to a workflow where you create and import 3D models as building blocks to your scene but use the editor to compose the scene.

We'll have to be careful with node name based component creation "hacks". It's good if they work for you, but it'd be preferable to use eg. metadata inside the nodes. Assimp includes a metadata structure, but the support for it is varying according to file format, and it's under heavy development right now. To benefit from it, we'll need to upgrade to a newer assimp once the support gets more stable and homogenized across the assimp file loaders.

-------------------------

