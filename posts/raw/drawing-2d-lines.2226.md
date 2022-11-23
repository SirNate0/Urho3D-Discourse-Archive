rku | 2017-01-02 01:14:02 UTC | #1

Isnt there a way to draw some 2D lines on the screen? I want that for some debugging graphs but cant find.

-------------------------

godan | 2017-01-02 01:14:02 UTC | #2

You can use the CustomGeometry class:

[code]
CustomGeometry* cg = lineNode->CreateComponent<CustomGeometry>();
cg->SetNumGeometries(1);
cg->BeginGeometry(0, PrimitiveType::LINE_LIST);
cg->DefineGeometry(0, PrimitiveType::LINE_LIST, 3, false,false, false, false);
cg->DefineVertex(Vector3(1,0,0));
cg->DefineVertex(Vector3(0,1,0));
cg->DefineVertex(Vector3(0,0,0));
cg->Commit();
[/code]

You can also pass different kinds of PrimtiveTypes to the StaticModel class, but that one takes a bit more setup. CustomGeometry is easier for basic stuff.

-------------------------

godan | 2017-01-02 01:14:02 UTC | #3

Ah, perhaps you mean 2D lines in screen space? You can use the same code but map the points to screen space via Camera::ScreenToWorldPoint or something. Or just position the camera to look at the XY plane.

-------------------------

zedraken | 2017-01-02 01:14:07 UTC | #4

You can also use the debug renderer. For that, you first create a component DebugRenderer, like that:

[code]scene_->CreateComponent<DebugRenderer>();[/code]

This is usually done in your "create scene" function.

Then, when you want to draw a line, you can do the following:

[code]DebugRenderer* dbgRenderer = scene_->GetComponent<DebugRenderer>();
dbgRenderer->AddLine(start point, end point, color);[/code]

Start and End points are of type Vector3.

Just check the DebugRenderer documentation for a detailed description.

-------------------------

