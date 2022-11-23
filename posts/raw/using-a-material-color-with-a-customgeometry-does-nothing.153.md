gasp | 2017-01-02 00:58:26 UTC | #1

Hello, another stupid question,
what i try to do :
--> Create a cube (composed of triangle)
--> put a color / material on them

the first part seem Ok to me, the second  does nothing.
(Polyhedron is a usable class to build mesh ?)


[u]here is the relevant part of my Angel Script  :[/u]
[code]
		//Create a node and a Custom Geometry component inside
	Node@ icoNode = scene_.CreateChild("CustomBox");
	CustomGeometry@ icosahedron = icoNode.CreateComponent("CustomGeometry");
	icosahedron.BeginGeometry(0, TRIANGLE_LIST);

		float baseZ = 2.0f;
		float baseY = 0.5f;
			//Sens des aiguilles d'une montre pour voir la face
		Vector3 pt1= Vector3 ( 0.0f, 0.0f + baseY, 0.0f + baseZ );
		Vector3 pt2= Vector3 ( 0.0f, 1.0f + baseY, 0.0f + baseZ );
		Vector3 pt3= Vector3 ( 1.0f, 1.0f + baseY, 0.0f + baseZ );
		Vector3 pt4= Vector3 ( 1.0f, 0.0f + baseY, 0.0f + baseZ );
		Vector3 pt5= Vector3 ( 0.0f, 0.0f + baseY, 1.0f + baseZ );
		Vector3 pt6= Vector3 ( 0.0f, 1.0f + baseY, 1.0f + baseZ );
		Vector3 pt7= Vector3 ( 1.0f, 1.0f + baseY, 1.0f + baseZ );
		Vector3 pt8= Vector3 ( 1.0f, 0.0f + baseY, 1.0f + baseZ );
		
		createRectangle(icosahedron,pt1,pt2,pt3,pt4);
		createRectangle(icosahedron,pt4,pt3,pt7,pt8);
		createRectangle(icosahedron,pt8,pt7,pt6,pt5);
		createRectangle(icosahedron,pt5,pt6,pt2,pt1);
		
		createRectangle(icosahedron,pt2,pt6,pt7,pt3);	//Up
		createRectangle(icosahedron,pt1,pt4,pt8,pt5);	//Down
		icosahedron.Commit();
                              /*File saveFile(fileSystem.programDir + "Data/moncube.mdl", FILE_WRITE);
                     		icosahedron.Save(saveFile);*/
		icosahedron.castShadows=true;
		icosahedron.DefineColor(Color(15.0f,15.0f,150.0f));
		icosahedron.material = cache.GetResource("Material", "Materials/Terrain.xml");
[/code]

the 2 last lines does nothing (DefineColor and material ) , if i set an inexistant material, no error.

for reference the createRectangle used in the code:

[code]
//Sens des aiguilles d'une montre pour voir la face
void createRectangle(CustomGeometry@ icosahedron,Vector3 pt1,Vector3 pt2,Vector3 pt3,Vector3 pt4)
{
		icosahedron.DefineVertex(pt1);icosahedron.DefineVertex(pt2);icosahedron.DefineVertex(pt4);
		icosahedron.DefineVertex(pt4);icosahedron.DefineVertex(pt2);icosahedron.DefineVertex(pt3);
}
[/code]

the actual visual result :
[url=http://imgdrop.net/viewer.php?id=bwy1395160143t.png][img]http://imgdrop.net/thumbs/bwy1395160143t.png[/img][/url]

-------------------------

cadaver | 2017-01-02 00:58:26 UTC | #2

If you want your CustomGeometry to show a texture correctly and respond to lighting, you need to define normals and UV coords for each vertex. Call DefineNormal() & DefineTexCoord() after each DefineVertex().

DefineColor() is meant for defining the vertex color for each vertex, it does nothing after a commit.

-------------------------

