rogerdv | 2017-01-02 01:01:30 UTC | #1

I started playing with AngelScript yesterday and of course, found my first problem:

[code][Tue Nov 25 07:49:46 2014] ERROR: Scripts/keyw.as:11,2 - Exception 'Null pointer access' in 'void Start()'
AngelScript callstack:
	Scripts/keyw.as:void Start():11,2
[/code]

This is the main code:

[code]#include "Scripts/Engine/IsoCamera.as"

Scene@ gameScene;
IsoCamera@ cam;

void Start()
{
	gameScene = Scene("castle-gates");
	gameScene.LoadXML(cache.GetFile("Scenes/NinjaSnowWar.xml"));
	cam = IsoCamera(); <----- This is the error line

    if (!engine.headless)
    {
        renderer.viewports[0] = Viewport(gameScene, cam.gameCamera);
    }
}
[/code]

This is the camera creation code:

[code]class IsoCamera
{
	IsoCamera()
	{
		target = Node();
		camNode = target.CreateChild("camnod");
		gameCamera = camNode.CreateComponent("Camera");
		camNode.position = Vector3(0, 55, 52);
		camNode.LookAt(target.position);
	}

	void SetPosition(Vector3 pos)
	{
		target.position = pos;
	}
	Node@ target;
	Node@ camNode;
	Camera@ gameCamera;
}[/code]

Can somebody seee where is my mistake?

-------------------------

Azalrion | 2017-01-02 01:01:31 UTC | #2

Since IsoCamera is a class defined in the script and so can be value assigned as well you need to put:

[code]
   @cam = IsoCamera();
[/code]

Instead.

-------------------------

rogerdv | 2017-01-02 01:01:31 UTC | #3

Hmm, I tried removing @ from IsoCamera@ cam; and worked too. Is that correct too?

-------------------------

Azalrion | 2017-01-02 01:01:31 UTC | #4

Yes. An @ symbol is a handle see: [angelcode.com/angelscript/sd ... andle.html](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_script_handle.html).

Its only not needed for urho defined c++ (or custom defined c++ classes) that don't support value assignment (using certain asBEH_ when defining the class in c++), any classes you declare in scripts and have a variable declaration using the handle will need to be assigned @varname = Var();. If you're not passing the variable around lots no need to use a handle, if you are you'd probably prefer it, its a wierd mix of c++ reference and pointer.

-------------------------

