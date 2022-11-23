jeremyjh | 2017-01-02 01:13:28 UTC | #1

The documentation for Urho2D mentions the possibility of using various Physics editors to create the definitions for physics shapes so they fit sprite images consistently. I'm familiar with the use of these tools in other 2D game engines. However, I do not see any functionality for loading definitions produced with these tools; I would expect to see something similar to what I do see implemented for the sprite sheets and Tilemap; loading definitions from XML format of some kind. Does this exist - if not in Urho has anyone written a loader (for any tool) they can share?

-------------------------

hdunderscore | 2017-01-02 01:13:33 UTC | #2

Without being familiar with other 2d physics editors, I'll point out that Urho has it's own editor that you could use to set up some basic shapes. From a quick look at the documentation, it seems like the external editors export polygons/hulls.

It looks like CollsiionPolygon2D might have some ability to load a shape from a file, but not in a very accessible format: [github.com/urho3d/Urho3D/blob/m ... ygon2D.cpp](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Urho2D/CollisionPolygon2D.cpp)

-------------------------

jeremyjh | 2017-01-02 01:13:36 UTC | #3

Thanks for the reply!

Are you referring to the CollisionPolygon2D::SetVertices ? I agree that would be helpful in writing a loader, but looks like I need to load a vector myself.

I think I will write my own loader for Physics Engine when the time comes, probably using the box2d generic plist format as it does look like there is good plist support in Urho3D.

-------------------------

Mike | 2017-01-02 01:14:01 UTC | #4

I've had a look at it yesterday and made a json loader for [url=http://www.aurelienribon.com/blog/projects/physics-body-editor/]Physics Body Editor[/url], that creates node + sprite + rigid body + collision shape for each object in the file:

[spoiler][code]
    // Read Physics Body Editor defs from a JSON file
    String jsonName = "Assets/Urho2D/PhysicsBodyEditor/test.json";
    JSONFile@ jsonFile = cache.GetResource("JSONFile", jsonName);
    if (jsonFile !is null)
    {
        JSONValue rigidBodies = jsonFile.root.Get("rigidBodies");

        for (uint i = 0; i < rigidBodies.size; ++i)
        {
            // Create node and rigid body
            JSONValue body = rigidBodies[i];
            String name = body.Get("name").GetString();
            Node@ n = scene_.CreateChild(name);
            RigidBody2D@ rigidBody = n.CreateComponent("RigidBody2D");

            // Create sprite
            String imagePath = body.Get("imagePath").GetString();
            StaticSprite2D@ staticSprite = n.CreateComponent("StaticSprite2D");
            Sprite2D@ sprite =  cache.GetResource("Sprite2D", GetParentPath(jsonName) + imagePath);
            staticSprite.sprite = sprite;

            // Set scale
            IntVector2 spriteSize = sprite.rectangle.size;
            Vector2 scale = Vector2(spriteSize.x, spriteSize.y) / 100.0f;

            // Set node position
            //JSONValue origin = body.Get("origin");
            //n.position2D = Vector2(origin.Get("x").GetFloat(), origin.Get("y").GetFloat());

			// Create polygons
			JSONValue polygons = body.Get("polygons");
			for (uint p = 0; p < polygons.size; ++p)
			{
				JSONValue polygon = polygons[p];
				CollisionPolygon2D@ shape = n.CreateComponent("CollisionPolygon2D");
				shape.vertexCount = polygon.size;

				for (uint v = 0; v < polygon.size; ++v)
				{
					JSONValue point = polygon[v];
					shape.SetVertex(v, (Vector2(point.Get("x").GetFloat(), point.Get("y").GetFloat()) - Vector2(0.5f, 0.5f)) * scale);
				}
			}

			// Create circles
			JSONValue circles = body.Get("circles");
			for (uint p = 0; p < circles.size; ++p)
			{
				JSONValue circle = circles[p];
				CollisionCircle2D@ shape = n.CreateComponent("CollisionCircle2D");
				shape.SetCenter((circle.Get("cx").GetFloat() - 0.5f) * scale.x, (circle.Get("cy").GetFloat() - 0.5f) * scale.y);
				shape.radius = circle.Get("r").GetFloat() * scale.x;
			}
		}
    }
[/code][/spoiler]
It works fine with the supplied [url=https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/box2d-editor/physics-body-editor-2.9.2.zip]sample test file[/url].
It can be added to master, however I don't see where it can fit well.

-------------------------

Mike | 2017-01-02 01:14:01 UTC | #5

XML loader for [url=https://www.codeandweb.com/physicseditor]PhysicsEditor[/url], that creates node + sprite + rigid body + collision shape for each object in the file:
[spoiler][code]
	// Read PhysicsEditor defs from an xml file
	String fileName = "Assets/Urho2D/PhysicsEditorXml/shapes.xml";
	XMLFile@ xmlFile = cache.GetResource("XMLFile", fileName);
	if (xmlFile is null)
	{
		log.Info("Cannot access file " + fileName);
		return;
	}

	XMLElement rootElem = xmlFile.GetRoot("bodydef");
	XMLElement bodies = rootElem.GetChild("bodies");
	XMLElement body = bodies.GetChild("body");
	while (!body.isNull)
	{
		// Create node and rigid body
		String name = body.GetAttribute("name");
		Node@ n = scene_.CreateChild(name);
		RigidBody2D@ rigidBody = n.CreateComponent("RigidBody2D");
		rigidBody.bodyType = body.GetBool("dynamic") ? BT_KINEMATIC : BT_STATIC;

		// Create sprite
		String imagePath = name + ".png";
		StaticSprite2D@ staticSprite = n.CreateComponent("StaticSprite2D");
		Sprite2D@ sprite =  cache.GetResource("Sprite2D", GetParentPath(fileName) + imagePath);
		staticSprite.sprite = sprite;

		// Get collision shape settings
		XMLElement fixture = body.GetChild("fixture");
		while (!fixture.isNull)
		{
			float density = fixture.GetFloat("density");
			float friction = fixture.GetFloat("friction");
			float restitution = fixture.GetFloat("restitution");
			int categoryBits = fixture.GetInt("filter_categoryBits");
			int groupIndex = fixture.GetInt("filter_groupIndex");
			int maskBits = fixture.GetUInt("filter_maskBits");
			bool trigger = fixture.GetBool("isSensor");

			// Create collision shape
			String type = fixture.GetAttribute("type"); // POLYGON or CIRCLE
			if (type == "POLYGON")
			{
				XMLElement polygon = fixture.GetChild("polygon");
				while (!polygon.isNull)
				{
					CollisionPolygon2D@ shape = n.CreateComponent("CollisionPolygon2D");
					shape.vertexCount = polygon.GetUInt("numVertexes");

					shape.density = density;
					shape.friction = friction;
					shape.restitution = restitution;
					shape.categoryBits = categoryBits;
					shape.groupIndex = groupIndex;
					shape.maskBits = maskBits;
					shape.trigger = trigger;

					// Create polygon shape from vertices
					XMLElement vertex = polygon.GetChild("vertex");
					for (uint v = 0; v < shape.vertexCount; ++v)
					{
						shape.SetVertex(v, Vector2(vertex.GetFloat("x"), 0.5f - vertex.GetFloat("y")) * PIXEL_SIZE);
						vertex = vertex.GetNext("vertex");
					}
					polygon = polygon.GetNext("polygon");
				}
			}
			else if (type == "CIRCLE")
			{
				XMLElement circle = fixture.GetChild("circle");
				while (!circle.isNull)
				{
					CollisionCircle2D@ shape = n.CreateComponent("CollisionCircle2D");

					shape.density = density;
					shape.friction = friction;
					shape.restitution = restitution;
					shape.categoryBits = categoryBits;
					shape.groupIndex = groupIndex;
					shape.maskBits = maskBits;
					shape.trigger = trigger;

					// Create circle shape from position and radius
					XMLElement position = circle.GetChild("position");
					shape.SetCenter(position.GetFloat("x") * PIXEL_SIZE, 0.5f - position.GetFloat("y") * PIXEL_SIZE);
					shape.radius = circle.GetFloat("radius") * PIXEL_SIZE;

					circle = circle.GetNext("circle");
				}
			}
			else
				log.Error("Unsupported fixture type");

			fixture = fixture.GetNext("fixture");
		}
		body = body.GetNext("body");
	}[/code][/spoiler]
Tested with these [url=https://github.com/CodeAndWeb/PhysicsEditor-AndEngine/tree/master/assets]sample files[/url].

While testing, I noticed that when polygon shapes are too tiny, a 1 unit square is created instead. Don't know if this is a Box2D limitation. Slightly increasing the node size fixes the issue, but this may not be desirable.

-------------------------

