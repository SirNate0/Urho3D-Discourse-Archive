GGibson | 2017-01-02 01:01:22 UTC | #1

Hi everyone,

I'm trying to make a simple graph. Did I miss an example or post somewhere? My first attempts are using DebugRenderer.AddLine(). It works in the normal scene, but I would like to display this in a UI window (through a renderTexture or directly on the UI). Because the UI is rendered to the backbuffer then I'm using a View3D control to display content rendered to a texture. I have the basic rotating gold coin icon scene rendered okay to this texture (also the rotating cubes example works), but still can't seem to draw lines on it, probably because of the render/access order. I'm drawing the line to my offscreen scene in the HandleUpdate fn. Is this the way to go about it? Is there a GL_LINE_STRIP and glLineWidth() equivalent? Thanks for the help!

-------------------------

weitjong | 2017-01-02 01:01:22 UTC | #2

Have you tried to use CustomGeometry class? You can create a 2D or 3D graph this way. I think this is as close as the "immediate mode" you can get.

-------------------------

GGibson | 2017-01-02 01:01:29 UTC | #3

Thanks weitjong, that's just what I needed. Here's my simple example for posterity. It handles graph repositioning based on window resizing, and data addition.

[img]https://dl.dropboxusercontent.com/u/9392583/Screenshot%202014-11-23%20at%202.32.22%20PM.png[/img]

There's a Figure.as containing a Figure class, and I use that to create and update one complete figure.

snippet from main .as file
[spoiler][code]
// global
Figure@ fig1;
// in setup
fig1 = Figure(IntVector2(400,300), "Figure1");
ui.root.AddChild(fig1.window); // use a window to manage drag and size of view3D
// in an updating function such as handleUpdate
fig1.Push(Sin(scene_.elapsedTime*200)*3); // record new value to figure
[/code][/spoiler]


Figure.as
[spoiler][code]
/*
 * Figure.as
/*

class Figure
{
	Window@ window;
	View3D@ view3d;
	Scene@ scene_;
	Camera@ camera_;
	bool isopen;
	Array<float>@ data = Array<float>();
	int xtick=0;
	CustomGeometry@ graph;
	Node@ graphNode;
	Button@ buttonClose_;

	void Toggle()
	{
		if (isopen) {
			isopen = false;
			window.visible = false;
			view3d.visible = false;
		} else {
			isopen = true;
			window.visible = true;
			view3d.visible = true;
		}
	}

	void Redraw()
	{
		graph.BeginGeometry(0, LINE_STRIP);
		for (int i=0; i<data.length; i++)
		{
			graph.DefineVertex(Vector3(0.01f*i, data[i], -1.0f));
		}
		graph.Commit();
		xtick=data.length+1;
		
	}

	void Push(float value) /// Updates graph for each push
	{
		graph.DefineVertex(Vector3(0.01f*xtick++, value, -1.0f));
		graph.Commit();
		Vector2 pos = graphNode.position2D;
		float dist = camera_.GetDistance(Vector3(0.0f, 0.0f, 0.0f));
		graphNode.SetPosition2D(((dist*0.33333f)*camera_.aspectRatio)-0.01f*xtick, pos.y); // 0.333 assumes fov=45
	}

	void UseHandler(String handler)
	{
		SubscribeToEvent(buttonClose_, "Released", handler);
	}

	Figure(IntVector2 dimensions = IntVector2(400,300), String title = "Figure")
	{
		// Set the loaded style as default style
		isopen = true;
		XMLFile@ style = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
		// Set the loaded style as default style

		window = Window();
		window.defaultStyle = style;
		window.visible = false;

		window.resizable = true;
		window.movable = true;

		// Set Window size and layout settings
		window.SetSize(dimensions.x, dimensions.y);
		window.SetLayout(LM_VERTICAL, 4, IntRect(2, 2, 2, 2));
		window.SetPosition(graphics.width / 2 - 400 / 2, graphics.height / 2 - 300 / 2);

		// Create Window 'titlebar' container
		titleBar = UIElement();
		titleBar.SetMinSize(0, 24);
		titleBar.SetMaxSize(9999, 24);
		titleBar.SetLayout(LM_HORIZONTAL, 6, IntRect(6, 6, 6, 6));

		// Create the Window title Text
		Text@ windowTitle = Text();
		windowTitle.text = title;

		// Create the Window's close button
		Button@ buttonClose_ = Button();

		// Add the controls to the title bar
		titleBar.AddChild(windowTitle);
		titleBar.AddChild(buttonClose_);

		// Add the title bar to the Window
		window.AddChild(titleBar);

		// Apply styles
		window.SetStyleAuto();
		windowTitle.SetStyleAuto();
		buttonClose_.style = "CloseButton";

		SetupScene(); // creates scene and camera

		view3d = View3D();
		view3d.verticalAlignment = VA_TOP;
		view3d.SetView(scene_, camera_);
		window.AddChild(view3d);
		SubscribeToEvent(buttonClose_, "Released", "HandleClosePressed");
	}

	void HandleClosePressed(StringHash eventType, VariantMap& eventData)
	{
		UIElement@ element = eventData["Element"].GetPtr();
		element.parent.parent.visible = false; // close button pressed (element), set window visibility
	}

	private void SetupScene()
	{
		// Create the scene which will be rendered to a texture
		scene_ = Scene();

		// Create octree, use default volume (-1000, -1000, -1000) to (1000, 1000, 1000)
		scene_.CreateComponent("Octree");

		// Create a camera for the render-to-texture scene. Simply leave it at the world origin and let it observe the scene
		rttCameraNode = scene_.CreateChild("Camera");
		rttCameraNode.position = Vector3(0.0f, 0.0f, -10.0f);
		camera_ = rttCameraNode.CreateComponent("Camera");
		camera_.farClip = 100.0f;
		camera_.orthographic = true;
		camera_.orthoSize = graphics.height * PIXEL_SIZE;

		// graph
		graphNode = scene_.CreateChild("CustomGeometry");
		graph = graphNode.CreateComponent("CustomGeometry");
		Material@ renderMaterial = cache.GetResource("Material", "Materials/WhiteUnlit.xml");
		graph.material = renderMaterial;
		graph.dynamic = true;
		Redraw();
	}
}
[/code][/spoiler]

I had to make a new material to do what I wanted (suggestions how to do this better?)
White.png is a 1 pixel white texture.
[spoiler][code]
<material>
    <technique name="Techniques/DiffUnlit.xml" />
    <texture unit="0" name="Textures/White.png" />
</material>
[/code][/spoiler]

-------------------------

weitjong | 2017-01-02 01:01:29 UTC | #4

[quote="GGibson"]I had to make a new material to do what I wanted (suggestions how to do this better?)
White.png is a 1 pixel white texture.[/quote]

You can use material with one of the no-texture technique to save your shader from doing a texture sampling.

-------------------------

