gasp | 2017-01-02 00:58:43 UTC | #1

Hello,
i wanted to play with Urho3d to create a simple game, i've created a tictactoe with the base assets :
use UrhoPlayer with this .as script :
[code]
// TicTacToe 3D scene example.
// This sample demonstrates:
//     - Creating a 3D scene with static content
//     - Raytracing to select a node and use "vars" to store data
//     - a simple who win algorithm
#include "Scripts/Utilities/Sample.as"

	//You can play with this values
const float FLOOR_ELEMENT_SIZE = 4.0f;	// Change scale of the game
const int ROW_FLOW_NUMBER=13;	        // Play area is a square, so row = column
const int REQUIRED_TO_WIN=6;	        // Number of aligned piece to win
const bool DISABLE_ROTATION=true;		//If true, all the cell a aligned, and not moved on click

// ## Code is below
//Global var
Scene@ scene_;
Node@ cameraNode;
Controls camControl;
float yaw = 10.0f;
float pitch = 30.0f;
Array<Node@> tblPlateau;
Node@ plateauParent;
Text@ activePlayerText ;
const int OWNED_BY_NO_ONE=0;
bool gameCreated=false;	//if you leave "e" or "s" it doens't spam the commande
bool drawDebug = false;
int activePlayer=1;	// 1st played is the first to play :p
int numCasePlayed =0;
void Start()
{
	// Execute the common startup for samples
	SampleStart();

	// Create the scene content
	CreateScene();

	
	// Create the UI content
	CreateUI();
	
	
	// Setup the viewport for displaying the scene
	SetupViewport();

	// Hook up to the frame update events
	SubscribeToEvents();
	
	// Start the game
	startOfGame();	
	   

     
}

void CreateUI()
{
	// Create a Cursor UI element because we want to be able to hide and show it at will. When hidden, the mouse cursor will
	// control the camera, and when visible, it will point the raycast target
	XMLFile@ style = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
	Cursor@ cursor = Cursor();
	cursor.SetStyleAuto(style);
	ui.cursor = cursor;
	// Set starting position of the cursor at the rendering window center
	cursor.SetPosition(graphics.width / 2, graphics.height / 2);

	// Construct new Text object, set string to display and font to use
	Text@ instructionText = ui.root.CreateChild("Text");
	instructionText.text =
	    "Use up,down,left,right arrow keys to move\n"
		"Use \"e\" End the game, \"s\" re-start a game\n"
	    "LMB to place ticTacToe Element, RMB to rotate view\n"
		"You need : "+REQUIRED_TO_WIN+" aligned to win \n"
	    "Space to move Up\n";

	instructionText.SetFont(cache.GetResource("Font", "Fonts/Anonymous Pro.ttf"), 15);
	// The text has multiple rows. Center them in relation to each other
	instructionText.textAlignment = HA_CENTER;

	// Position the text relative to the screen center
	instructionText.horizontalAlignment = HA_CENTER;
	instructionText.verticalAlignment = VA_CENTER;
	instructionText.SetPosition(0, ui.root.height / 4);

	activePlayerText = ui.root.CreateChild("Text");
	activePlayerText.text ="player "+activePlayer;
	activePlayerText.textAlignment = HA_CENTER;
	activePlayerText.horizontalAlignment = HA_CENTER;
	activePlayerText.verticalAlignment = VA_BOTTOM;
	activePlayerText.SetPosition(0, 1);
	activePlayerText.SetFont(cache.GetResource("Font", "Fonts/Anonymous Pro.ttf"), 30);
	activePlayerText.color = Color(0.0f, 1.0f, 0.0f);

}

void CreateScene()
{
	scene_ = Scene();

	// Create the Octree component to the scene. This is required before adding any drawable components, or else nothing will
	// show up. The default octree volume will be from (-1000, -1000, -1000) to (1000, 1000, 1000) in world coordinates; it
	// is also legal to place objects outside the volume but their visibility can then not be checked in a hierarchically
	// optimizing manner
	scene_.CreateComponent("Octree");
	scene_.CreateComponent("DebugRenderer");
	// Create a directional light to the world so that we can see something. The light scene node's orientation controls the
	// light direction; we will use the SetDirection() function which calculates the orientation from a forward direction vector.
	// The light will use default settings (white light, no shadows)
	Node@ lightNode = scene_.CreateChild("DirectionalLight");
	lightNode.direction = Vector3(0.6f, -1.0f, 0.8f); // The direction vector does not need to be normalized
	Light@ light = lightNode.CreateComponent("Light");
	light.lightType = LIGHT_DIRECTIONAL;




	// Create a scene node for the camera, which we will move around
	// The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
	cameraNode = scene_.CreateChild("Camera");
	cameraNode.CreateComponent("Camera");

	// Set an initial position for the camera scene node above the plane
	cameraNode.position = Vector3((FLOOR_ELEMENT_SIZE*ROW_FLOW_NUMBER)/2, 10.0f, -15.0f);
	cameraNode.Pitch(pitch);
	cameraNode.Yaw(yaw);
}



void SetupViewport()
{
	// Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
	// at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
	// use, but now we just use full screen and default render path configured in the engine command line options
	Viewport@ viewport = Viewport(scene_, cameraNode.GetComponent("Camera"));
	renderer.viewports[0] = viewport;
}

void MoveCamera(float timeStep)
{
	// Right mouse button controls mouse cursor visibility: hide when pressed
	ui.cursor.visible = !input.mouseButtonDown[MOUSEB_RIGHT];

	// Do not move if the UI has a focused element (the console)
	if (ui.focusElement !is null)
		return;

	// Movement speed as world units per second
	const float MOVE_SPEED = 20.0f;
	// Mouse sensitivity as degrees per pixel
	const float MOUSE_SENSITIVITY = 0.1f;

	// Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
	// Only move the camera when the cursor is hidden
	if (!ui.cursor.visible) {
		IntVector2 mouseMove = input.mouseMove;
		yaw += MOUSE_SENSITIVITY * mouseMove.x;
		pitch += MOUSE_SENSITIVITY * mouseMove.y;
		pitch = Clamp(pitch, -90.0f, 90.0f);

		// Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
		cameraNode.rotation = Quaternion(pitch, yaw, 0.0f);
	}

	// Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
	//Currently setted for french keyboard
	if (input.keyDown[KEY_UP])
		cameraNode.TranslateRelative(Vector3(0.0f, 0.0f, 1.0f) * MOVE_SPEED * timeStep);
	if (input.keyDown[KEY_DOWN])
		cameraNode.TranslateRelative(Vector3(0.0f, 0.0f, -1.0f) * MOVE_SPEED * timeStep);
	if (input.keyDown[KEY_LEFT])
		cameraNode.TranslateRelative(Vector3(-1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
	if (input.keyDown[KEY_RIGHT])
		cameraNode.TranslateRelative(Vector3(1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
	if (input.keyDown[KEY_D])
		cameraNode.TranslateRelative(Vector3(0.0f, 2.0f, 0.0f) * MOVE_SPEED * timeStep);
	//Check what is  clicked, and if game engine need to react
	if (ui.cursor.visible && input.mouseButtonPress[MOUSEB_LEFT])
		whatHaveYouCLicked();
	if (input.keyDown[KEY_E])
		endOfGame();
	if (input.keyDown[KEY_S])
		startOfGame	();
	//Active / Desactive debug
	if (input.keyPress[KEY_SPACE])
		drawDebug = !drawDebug;

}
void startOfGame()
{
	if (gameCreated)
		return;
	plateauParent  = scene_.CreateChild("damier");
	//Create the "floor" with a list of node who will be valid target for raycasting
		for (uint j = 0; j < ROW_FLOW_NUMBER; ++j) {
			for (uint i = 0; i < ROW_FLOW_NUMBER; ++i) {
			Node@ floorNode = plateauParent.CreateChild("damier");
			//Setting vars who will help up to track what is doable and what is not
			floorNode.vars["x"]=i;
			floorNode.vars["y"]=j;
			floorNode.vars["playedBy"]=OWNED_BY_NO_ONE;	//Case not played
			floorNode.position = Vector3(i*FLOOR_ELEMENT_SIZE+(FLOOR_ELEMENT_SIZE/2), 0.0f, j*FLOOR_ELEMENT_SIZE+(FLOOR_ELEMENT_SIZE/2));
				//We re-use already present materials, they use 99% of the FLOOR_ELEMENT_SIZE
			floorNode.scale=Vector3(FLOOR_ELEMENT_SIZE-(FLOOR_ELEMENT_SIZE/100),-(FLOOR_ELEMENT_SIZE/100),FLOOR_ELEMENT_SIZE-(FLOOR_ELEMENT_SIZE/100));
				//create the static model
			StaticModel@ floorStaticModel = floorNode.CreateComponent("StaticModel");
			floorStaticModel.model = 	cache.GetResource("Model", "Models/Box.mdl");
			floorStaticModel.material = cache.GetResource("Material", "Materials/Stone.xml");
				//Save in an Array of Node@
			tblPlateau.Push(floorNode);
		}
	}
	/**
	 * Sample for iterating the plateau lineary and accessing each part
	 */ 
	 if (!DISABLE_ROTATION){
	 for (uint i = 0; i < tblPlateau.length; ++i) {
		tblPlateau[i].Rotate(Quaternion(0.0f, 30.0f, 0.0f));
		Print(tblPlateau[i].vars["x"]);
	
	 }
	 }
	 
		//Define somes vars
	gameCreated=true;
	activePlayer=1;
	activePlayerText.text ="player "+activePlayer;
}
void endOfGame()
{
	//Need to add a test not to erase 50  times the game
	tblPlateau.Clear();
	plateauParent.RemoveAllChildren();
	gameCreated=false;
}
void whatHaveYouCLicked()
{
	Vector3 hitPos;
	Drawable@ hitDrawable;
	if (Raycast(250.0f, hitPos, hitDrawable)) {
		// search with floor coords what cell is touched by the ray vector3 impact point
		int caseXpos = (hitPos.x/FLOOR_ELEMENT_SIZE);
		int caseYpos = (hitPos.z/FLOOR_ELEMENT_SIZE);
			//2nd method : Selected Node
		Node@ selectedNode = hitDrawable.node;
			//Online node named "damier" are valide target
		if (selectedNode.name =="damier") {
			if (selectedNode.vars["playedBy"].GetUInt()==0) {
				//search area by vector3D coordinates
				int caseX = selectedNode.vars["x"].GetUInt();
				int caseY = selectedNode.vars["y"].GetUInt();
				int indice=caseY*ROW_FLOW_NUMBER+caseX;	//linearize the coordonnates
				
				if (!DISABLE_ROTATION && indice<=tblPlateau.length) {
					tblPlateau[indice].Rotate(Quaternion(0.0f, -30.0f, 0.0f));
					//Print(tblPlateau[indice].vars["x"]);
				}
					//we link the game element (Cross/Cicle normally) to it's node to be able to remove it within the game
				Node@ gameElementNode = plateauParent.CreateChild("player"+activePlayer+" gameElement");
					//we center the element  in the dalle
				gameElementNode.position = Vector3(caseX*FLOOR_ELEMENT_SIZE+(FLOOR_ELEMENT_SIZE/2), 0.2f, caseY*FLOOR_ELEMENT_SIZE+(FLOOR_ELEMENT_SIZE/2));
				StaticModel@ staticModel = gameElementNode.CreateComponent("StaticModel");
				log.Info("Player " + activePlayer +" have play in ["+selectedNode.vars["x"].GetUInt()+"]["+selectedNode.vars["y"].GetUInt()+"]");
					//set node local vars
				selectedNode.vars["playedBy"]= activePlayer ;
					//easy way to know it's an end of play ^^
				numCasePlayed++;
				if (activePlayer==1) {
					staticModel.model = cache.GetResource("Model", "Models/Sphere.mdl");
					staticModel.material = cache.GetResource("Material", "Materials/Terrain.xml");
					//We scale object according to the floor size
					gameElementNode.SetScale(FLOOR_ELEMENT_SIZE/4.0f);
				}
				else {
					staticModel.model = cache.GetResource("Model", "Models/Torus.mdl");
					staticModel.material = cache.GetResource("Material", "Materials/Terrain.xml");
					gameElementNode.SetScale(FLOOR_ELEMENT_SIZE/4.0f);
				}
				// Did we have a winner ?
				if (didWeHaveAWinner(caseX,caseY)) {
					activePlayerText.text ="player "+activePlayer +" Win!" ;
					showMenu();
				}
				else
					//all area fill & no winner
					if (numCasePlayed == ROW_FLOW_NUMBER*ROW_FLOW_NUMBER) {
						activePlayerText.text="End Of Game, it's a draw !";
						//showMenu();
					}
					else {
						//game continue, change current player
						if (activePlayer==1)
							activePlayer=2;
						else
							activePlayer=1;
						activePlayerText.text ="player "+activePlayer;
					}
			}
			else {
				log.Info ("!! Node Already played by player "+selectedNode.vars["playedBy"].GetUInt()+"["+selectedNode.vars["x"].GetUInt()+"]["+selectedNode.vars["y"].GetUInt()+"]");
			}
		}

	}
}
	/**
	 * Maybe we need a menu here :p
	 * */
void showMenu()
{
	endOfGame();
}
/**
 * Detection of a winner
 * */
bool didWeHaveAWinner(int x_,int y_)
{
	int nbFound=0;
	int i=0;
	int indice=0;
	// ## Horizontal Search
	while (x_+i<ROW_FLOW_NUMBER && activePlayer==tblPlateau[y_*ROW_FLOW_NUMBER+x_+i].vars["playedBy"].GetUInt()) i++;
	nbFound=i;i=0;
	while (x_-i>=0 && activePlayer==tblPlateau[y_*ROW_FLOW_NUMBER+x_-i].vars["playedBy"].GetUInt()) i++;
	nbFound+=i-1;	//we doesn't count 2 time the originate cell
	log.Info("Horizontale : "+nbFound+" ");	
	if (nbFound>=REQUIRED_TO_WIN)//have we a horizontal winner ?
		return true;
	// ## Vertical search
	i=0;
	while (y_+i<ROW_FLOW_NUMBER && activePlayer==tblPlateau[(y_+i)*ROW_FLOW_NUMBER+x_].vars["playedBy"].GetUInt()) i++;	
	nbFound=i;i=0;//go "Down"
	while ((y_-i)>=0 && activePlayer==tblPlateau[(y_-i)*ROW_FLOW_NUMBER+x_].vars["playedBy"].GetUInt()){
			//If you want to be able to trace the algo : 
		// indice=(y_-i)*ROW_FLOW_NUMBER+x_;
	   	 //log.Info("up "+tblPlateau[indice].name+" x: "+tblPlateau[indice].vars["x"].GetUInt()+" y: "+tblPlateau[indice].vars["y"].GetUInt()+
				//" Player: "+tblPlateau[indice].vars["playedBy"].GetUInt()+" Player : "+activePlayer);		
				i++;	
	}
	nbFound+=i-1;
	log.Info("Verticale : "+nbFound);
	if (nbFound>=REQUIRED_TO_WIN)
		return true;
	// ## Diagonal Search
	i=0;while (y_+i<ROW_FLOW_NUMBER && x_+i<ROW_FLOW_NUMBER && activePlayer==tblPlateau[(y_+i)*ROW_FLOW_NUMBER+x_+i].vars["playedBy"].GetUInt()) i++; 
	nbFound=i;
	i=0;while ( (y_-i)>=0 && (x_-i)>=0 && activePlayer==tblPlateau[(y_-i)*ROW_FLOW_NUMBER+x_-i].vars["playedBy"].GetUInt()) i++; 
	nbFound+=i-1;	
	log.Info("Diagonal / : "+nbFound+" ");	
	if (nbFound>=REQUIRED_TO_WIN)//have we a horizontal winner ?
		return true;				
	i=0;while (y_+i<ROW_FLOW_NUMBER && x_-i>=0 && activePlayer==tblPlateau[(y_+i)*ROW_FLOW_NUMBER+x_-i].vars["playedBy"].GetUInt()) i++; 
	nbFound=i;
	i=0;while ( (y_-i)>=0 && (x_+i)<ROW_FLOW_NUMBER && activePlayer==tblPlateau[(y_-i)*ROW_FLOW_NUMBER+x_+i].vars["playedBy"].GetUInt()) i++; 
	nbFound+=i-1;	
	log.Info("Diagonal \\ : "+nbFound+" ");	
	if (nbFound>=REQUIRED_TO_WIN)//have we a horizontal winner ?
		return true;						
	return false;
}
/**
 * Cast a Ray and store the 3D pos in hitPos, and the node in hitDrawable (stolen from 08_decals)
  * */
bool Raycast(float maxDistance, Vector3& hitPos, Drawable@& hitDrawable)
{
	hitDrawable = null;
	IntVector2 pos = ui.cursorPosition;
	// Check the cursor is visible and there is no UI element in front of the cursor
	if (!ui.cursor.visible || ui.GetElementAt(pos, true) !is null)
		return false;
	Camera@ camera = cameraNode.GetComponent("Camera");
	Ray cameraRay = camera.GetScreenRay(float(pos.x) / graphics.width, float(pos.y) / graphics.height);
	// Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
	// Note the convenience accessor to scene's Octree component
	RayQueryResult result = scene_.octree.RaycastSingle(cameraRay, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY);
	if (result.drawable !is null) {
		hitPos = result.position;
		hitDrawable = result.drawable;
		return true;
	}
	return false;
}

void SubscribeToEvents()
{
	// Subscribe HandleUpdate() function for processing update events
	SubscribeToEvent("Update", "HandleUpdate");
	// debug geometry
	SubscribeToEvent("PostRenderUpdate", "HandlePostRenderUpdate");
}

void HandleUpdate(StringHash eventType, VariantMap& eventData)
{
	// Take the frame time step, which is stored as a float
	float timeStep = eventData["TimeStep"].GetFloat();
	// Move the camera, scale movement with time step
	MoveCamera(timeStep);

}
void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
	// If draw debug mode is enabled, draw viewport debug geometry. This time use depth test, as otherwise the result becomes
	// hard to interpret due to large object count
	if (drawDebug)
		renderer.DrawDebugGeometry(true);
}
[/code]

you can change number of cell, number of object to align and size of a cell, simple look at the start of the script.

next step is to clean the code, add an IA, maybe a menu with the UI

and after a LUA / C++ version to understand more stuff.
(i know using a fine 3D engine for Urho3d is really OVERKILL, apport nothing but it's for testing somes concepts with Urho3D

-------------------------

Canardian | 2017-01-02 00:58:44 UTC | #2

[quote="gasp"](i know using a fine 3D engine for Urho3d is really OVERKILL, apport nothing but it's for testing somes concepts with Urho3D[/quote]
I wouldn't say so, because I started to make any kind of apps with Urho3D now, even simple office tools. Urho3D's GUI system is so much more flexible and convenient to use than Windows GUI system, especially when you need lots of custom functionality. It's kinda like .NET, but has more useful features, and full source code in C++. And of course it's cross-platform too.

-------------------------

cadaver | 2017-01-02 00:58:44 UTC | #3

Yeah, it's good to have several kinds of examples; I don't think there's things that shouldn't be done with Urho, if it only supports them well enough. I did a text adventure :smiling_imp:

-------------------------

gasp | 2017-01-02 00:58:45 UTC | #4

a more evolued version, witch work in a touch device :

[code]
// TicTacToe 3D scene example.
// This sample demonstrates:
//     - Creating a 3D scene with static content
//     - Raytracing to select a node and use "vars" to store data
//     - Next is a  integrated way to check who win

#include "Scripts/Utilities/Sample.as"
#include "Scripts/Utilities/Touch.as"
//You can play with this values
const float FLOOR_ELEMENT_SIZE = 4.0f;	// Change scale of the game
const int ROW_FLOW_NUMBER=12;	        // Play area is a square, so row = column
const int REQUIRED_TO_WIN=4;	        // Number of aligned piece to win
const bool DISABLE_ROTATION=true;		//If true, all the cell a aligned, and not moved on click

// Needed for touch.as
const uint CTRL_FORWARD = 1;
const uint CTRL_BACK = 2;
const uint CTRL_LEFT = 4;
const uint CTRL_RIGHT = 8;
const uint CTRL_JUMP = 16;


// ## Code is below
//Global var
Scene@ scene_;
Node@ cameraNodeScene;
Controls camControl;
float yaw = 10.0f;
float pitch = 30.0f;
Array<Node@> tblPlateau;
Node@ plateauParent;
Text@ activePlayerText ;
const int OWNED_BY_NO_ONE=0;
bool gameCreated=false;	//if you leave "e" or "s" it doens't spam the commande
bool drawDebug = false;
int activePlayer=1;	// 1st played is the first to play :p
int numCasePlayed =0;
//Used for touch settings

void Start()
{
	// Execute the common startup for samples
	SampleStart();

	// Create the scene content
	CreateScene();

	//NEW : for touch stuff
	if (GetPlatform() == "Android" || GetPlatform() == "iOS")
		InitTouchInput();
	// Create the UI content
	CreateUI();

	// Setup the viewport for displaying the scene
	SetupViewport();

	// Hook up to the frame update events
	SubscribeToEvents();

	// Start a game
	startOfGame();

}

void CreateUI()
{
	// Create a Cursor UI element because we want to be able to hide and show it at will. When hidden, the mouse cursor will
	// control the camera, and when visible, it will point the raycast target
	XMLFile@ style = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
	Cursor@ cursor = Cursor();
	cursor.SetStyleAuto(style);
	ui.cursor = cursor;
	// Set starting position of the cursor at the rendering window center
	cursor.SetPosition(graphics.width / 2, graphics.height / 2);

	// Construct new Text object, set string to display and font to use
	Text@ instructionText = ui.root.CreateChild("Text");
	instructionText.text =
	    "Use up,down,left,right arrow keys to move\n"
	    "Use \"e\" End the game, \"s\" re-start a game\n"
	    "LMB to place ticTacToe Element, RMB to rotate view\n"
	    "You need : "+REQUIRED_TO_WIN+" aligned to win \n"
	    "Space to move Up\n";

	instructionText.SetFont(cache.GetResource("Font", "Fonts/Anonymous Pro.ttf"), 15);
	// The text has multiple rows. Center them in relation to each other
	instructionText.textAlignment = HA_CENTER;
	// Position the text relative to the screen center
	instructionText.horizontalAlignment = HA_CENTER;
	instructionText.verticalAlignment = VA_CENTER;
	instructionText.SetPosition(0, ui.root.height / 4);
	//Define the green text who permit to follow the game stat
	activePlayerText = ui.root.CreateChild("Text");
	activePlayerText.text ="player "+activePlayer;
	activePlayerText.textAlignment = HA_CENTER;
	activePlayerText.horizontalAlignment = HA_CENTER;
	activePlayerText.verticalAlignment = VA_BOTTOM;
	activePlayerText.SetPosition(0, 1);
	activePlayerText.SetFont(cache.GetResource("Font", "Fonts/Anonymous Pro.ttf"), 30);
	activePlayerText.color = Color(0.0f, 1.0f, 0.0f);

}

void CreateScene()
{
	scene_ = Scene();

	// Create the Octree component to the scene. This is required before adding any drawable components, or else nothing will
	// show up. The default octree volume will be from (-1000, -1000, -1000) to (1000, 1000, 1000) in world coordinates; it
	// is also legal to place objects outside the volume but their visibility can then not be checked in a hierarchically
	// optimizing manner
	scene_.CreateComponent("Octree");
	scene_.CreateComponent("DebugRenderer");
	// Create a directional light to the world so that we can see something. The light scene node's orientation controls the
	// light direction; we will use the SetDirection() function which calculates the orientation from a forward direction vector.
	// The light will use default settings (white light, no shadows)
	Node@ lightNode = scene_.CreateChild("DirectionalLight");
	lightNode.direction = Vector3(0.6f, -1.0f, 0.8f); // The direction vector does not need to be normalized
	Light@ light = lightNode.CreateComponent("Light");
	light.lightType = LIGHT_DIRECTIONAL;

	// Create a scene node for the camera, which we will move around
	// The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
	cameraNodeScene = scene_.CreateChild("Camera");
	cameraNodeScene.CreateComponent("Camera");

	// Set an initial position for the camera scene node above the plane
	cameraNodeScene.position = Vector3((FLOOR_ELEMENT_SIZE*ROW_FLOW_NUMBER)/2, 10.0f, -15.0f);
	cameraNodeScene.Pitch(pitch);
	cameraNodeScene.Yaw(yaw);
}



void SetupViewport()
{
	// Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
	// at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
	// use, but now we just use full screen and default render path configured in the engine command line options
	Viewport@ viewport = Viewport(scene_, cameraNodeScene.GetComponent("Camera"));
	renderer.viewports[0] = viewport;
}
/**
 * Modified version to allow Touch Events
 */
void MoveCamera(float timeStep)
{
	zoom = false;
	// Right mouse button controls mouse cursor visibility: hide when pressed
	ui.cursor.visible = !input.mouseButtonDown[MOUSEB_RIGHT];

	// Do not move if the UI has a focused element (the console)
	if (ui.focusElement !is null)
		return;

	// Movement speed as world units per second
	const float MOVE_SPEED = 20.0f;
	// Mouse sensitivity as degrees per pixel
	const float MOUSE_SENSITIVITY = 0.1f;

	// Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
	// Only move the camera when the cursor is hidden


	if (!touchEnabled) {
		if (!ui.cursor.visible) {
			IntVector2 mouseMove = input.mouseMove;
			yaw += MOUSE_SENSITIVITY * mouseMove.x;
			pitch += MOUSE_SENSITIVITY * mouseMove.y;
			pitch = Clamp(pitch, -90.0f, 90.0f);

		}
	}
	else {
		//We will use the touch move with 1 finger to move camera
		// Touch Inputs
		int sens = 0;
		
		if (touchEnabled) {
			//1 finger = rotate the cam & click on a floor area
			if (input.numTouches == 1) {
				TouchState@ touch1 = input.touches[0];
				if  (Abs(touch1.delta.x)>5)
					yaw += MOUSE_SENSITIVITY * touch1.delta.x;
				else if  (Abs(touch1.delta.y) > 5 )
					pitch += MOUSE_SENSITIVITY * touch1.delta.y;
				else {
					whatHaveYouCLicked();
				}
			}
			//2 finger : zomm In / Out ( script taken from touch.as, but different finality
        if (input.numTouches == 2)
        {
            TouchState@ touch1 = input.touches[0];
            TouchState@ touch2 = input.touches[1];
            // Check for zoom pattern (touches moving in opposite directions)
            if ((touch1.delta.y > 0 && touch2.delta.y < 0) || (touch1.delta.y < 0 && touch2.delta.y > 0))
                zoom = true;
            else 
                zoom = false;

            if (zoom)
            {
                int sens = 0;
                // Check for zoom direction (in/out)
                if (Abs(touch1.position.y - touch2.position.y) > Abs(touch1.lastPosition.y - touch2.lastPosition.y))
                    sens = -1;
                else
					
                    sens = 1;
				cameraNodeScene.TranslateRelative(Vector3(0.0f, 0.0f, sens*1.0f) * Abs(touch1.delta.y - touch2.delta.y)* TOUCH_SENSITIVITY / 50);					
            }
        }

		}
	}
// Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
	pitch = Clamp(pitch, -90.0f, 90.0f);
	cameraNodeScene.rotation = Quaternion(pitch, yaw, 0.0f);


	// Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
	if (input.keyDown[KEY_UP])
		cameraNodeScene.TranslateRelative(Vector3(0.0f, 0.0f, 1.0f) * MOVE_SPEED * timeStep);
	if (input.keyDown[KEY_DOWN])
		cameraNodeScene.TranslateRelative(Vector3(0.0f, 0.0f, -1.0f) * MOVE_SPEED * timeStep);
	if (input.keyDown[KEY_LEFT])
		cameraNodeScene.TranslateRelative(Vector3(-1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
	if (input.keyDown[KEY_RIGHT])
		cameraNodeScene.TranslateRelative(Vector3(1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
	if (input.keyDown[KEY_D])
		cameraNodeScene.TranslateRelative(Vector3(0.0f, 2.0f, 0.0f) * MOVE_SPEED * timeStep);
	//Check what is  clicked, and if game engine need to react
	if (ui.cursor.visible && input.mouseButtonPress[MOUSEB_LEFT])
		whatHaveYouCLicked();
	//end the game
	if (input.keyDown[KEY_E])
		endOfGame();
	//restart a game
	if (input.keyDown[KEY_S])
		startOfGame	();
	//Active / Desactive debug
	if (input.keyPress[KEY_SPACE])
		drawDebug = !drawDebug;

}
void startOfGame()
{
	//we don't recreate an already started game
	if (gameCreated)
		return;
	plateauParent  = scene_.CreateChild("damier");
	//Create the "floor" with a list of node who will be valid target for raycasting
	for (uint j = 0; j < ROW_FLOW_NUMBER; ++j) {
		for (uint i = 0; i < ROW_FLOW_NUMBER; ++i) {
			Node@ floorNode = plateauParent.CreateChild("damier");
			//Setting vars who will help up to track what is doable and what is not
			floorNode.vars["x"]=i;
			floorNode.vars["y"]=j;
			floorNode.vars["playedBy"]=OWNED_BY_NO_ONE;	//Case not played
			floorNode.position = Vector3(i*FLOOR_ELEMENT_SIZE+(FLOOR_ELEMENT_SIZE/2), 0.0f, j*FLOOR_ELEMENT_SIZE+(FLOOR_ELEMENT_SIZE/2));
			//We re-use already present materials, they use 99% of the FLOOR_ELEMENT_SIZE
			floorNode.scale=Vector3(FLOOR_ELEMENT_SIZE-(FLOOR_ELEMENT_SIZE/100),-(FLOOR_ELEMENT_SIZE/100),FLOOR_ELEMENT_SIZE-(FLOOR_ELEMENT_SIZE/100));
			//create the static model
			StaticModel@ floorStaticModel = floorNode.CreateComponent("StaticModel");
			floorStaticModel.model = 	cache.GetResource("Model", "Models/Box.mdl");
			floorStaticModel.material = cache.GetResource("Material", "Materials/Stone.xml");
			//Save in an Array of Node@
			tblPlateau.Push(floorNode);
		}
	}
	// rotate the floor for a poorly visual effect
	if (!DISABLE_ROTATION) {
		for (uint i = 0; i < tblPlateau.length; ++i) {
			tblPlateau[i].Rotate(Quaternion(0.0f, 30.0f, 0.0f));
			Print(tblPlateau[i].vars["x"]);

		}
	}

	//Define somes vars
	gameCreated=true;
	activePlayer=1;
	activePlayerText.text ="player "+activePlayer;
}
void endOfGame()
{
	//Need to add a test not to erase 50 times the game
	//When we remove node, we reset the local var so no need to reset them
	tblPlateau.Clear();
	plateauParent.RemoveAllChildren();
	gameCreated=false;
}
void whatHaveYouCLicked()
{
	Vector3 hitPos;
	Drawable@ hitDrawable;
	if (Raycast(250.0f, hitPos, hitDrawable)) {
		// search with floor coords what cell is touched by the ray vector3 impact point
		/** not used for reference only
		int caseXpos = (hitPos.x/FLOOR_ELEMENT_SIZE);
		int caseYpos = (hitPos.z/FLOOR_ELEMENT_SIZE);
		 */
		//2nd method : Selected Node
		Node@ selectedNode = hitDrawable.node;
		//Only node named "damier" are valide target
		if (selectedNode.name =="damier") {
			if (selectedNode.vars["playedBy"].GetUInt()==0) {

				int caseX = selectedNode.vars["x"].GetUInt();
				int caseY = selectedNode.vars["y"].GetUInt();
				int indice=caseY*ROW_FLOW_NUMBER+caseX;		//linearize the coordonnates
				if (!DISABLE_ROTATION && indice<=tblPlateau.length) {
					tblPlateau[indice].Rotate(Quaternion(0.0f, -30.0f, 0.0f));
				}
				//we link the game element (Cross/Cicle normally) to it's node to be able to be removed when game end
				Node@ gameElementNode = plateauParent.CreateChild("player"+activePlayer+" gameElement");
				//we center the element  in the dalle
				gameElementNode.position = Vector3(caseX*FLOOR_ELEMENT_SIZE+(FLOOR_ELEMENT_SIZE/2), 0.2f, caseY*FLOOR_ELEMENT_SIZE+(FLOOR_ELEMENT_SIZE/2));
				StaticModel@ staticModel = gameElementNode.CreateComponent("StaticModel");
				log.Info("Player " + activePlayer +" have play in ["+selectedNode.vars["x"].GetUInt()+"]["+selectedNode.vars["y"].GetUInt()+"]");
				//set node local vars
				selectedNode.vars["playedBy"]= activePlayer ;
				//easy way to know if all case are full
				numCasePlayed++;
				if (activePlayer==1) {
					staticModel.model = cache.GetResource("Model", "Models/Sphere.mdl");
					staticModel.material = cache.GetResource("Material", "Materials/Terrain.xml");
					//We scale object according to the floor size
					gameElementNode.SetScale(FLOOR_ELEMENT_SIZE/4.0f);
				}
				else {
					staticModel.model = cache.GetResource("Model", "Models/Torus.mdl");
					staticModel.material = cache.GetResource("Material", "Materials/Terrain.xml");
					gameElementNode.SetScale(FLOOR_ELEMENT_SIZE/4.0f);
				}
				// Did we have a winner ?
				if (didWeHaveAWinner(caseX,caseY)) {
					activePlayerText.text ="player "+activePlayer +" Win!" ;
					showMenu();
				}
				//all area fill & no winner
				else if (numCasePlayed == ROW_FLOW_NUMBER*ROW_FLOW_NUMBER) {
					activePlayerText.text="End Of Game, it's a draw !";
				}
				else {
					//game continue, change current player
					if (activePlayer==1)
						activePlayer=2;
					else
						activePlayer=1;
					activePlayerText.text ="player "+activePlayer;
				}
			}
			else {
				log.Info ("!! Node Already played by player "+selectedNode.vars["playedBy"].GetUInt()+"["+selectedNode.vars["x"].GetUInt()+"]["+selectedNode.vars["y"].GetUInt()+"]");
			}
		}
	}
}
/**
 * Maybe we need a menu here :p
 * */
void showMenu()
{
	endOfGame();
	//TODO : a menu :p
}
/**
 * Detection of a winner
 * */
bool didWeHaveAWinner(int x_,int y_)
{
	int nbFound=0;
	int i=0;
	int indice=0;
	/*
			//If you want to be able to trace the algo, replace "i++;" with :
		 {
		indice=(y_-i)*ROW_FLOW_NUMBER+(x_-i);
	   	 log.Info("Trace:"+tblPlateau[indice].name+"["+tblPlateau[indice].vars["x"].GetUInt()+"]["+tblPlateau[indice].vars["y"].GetUInt()+
				"] CaseOwner: "+tblPlateau[indice].vars["playedBy"].GetUInt()+" activePlayer : "+activePlayer);
		 i++;
		 }
				*/
	// ## Horizontal Search
	while (x_+i<ROW_FLOW_NUMBER && activePlayer==tblPlateau[y_*ROW_FLOW_NUMBER+x_+i].vars["playedBy"].GetUInt()) i++;
	nbFound=i;
	i=0;
	while (x_-i>=0 && activePlayer==tblPlateau[y_*ROW_FLOW_NUMBER+x_-i].vars["playedBy"].GetUInt()) i++;
	nbFound+=i-1;	//we doesn't count 2 time the originate cell
	log.Info("Horizontale : "+nbFound+" ");
	if (nbFound>=REQUIRED_TO_WIN)	//have we a winner ?
		return true;
	// ## Vertical search
	i=0;
	while (y_+i<ROW_FLOW_NUMBER && activePlayer==tblPlateau[(y_+i)*ROW_FLOW_NUMBER+x_].vars["playedBy"].GetUInt()) i++;
	nbFound=i;
	i=0;//go "Down"
	while ((y_-i)>=0 && activePlayer==tblPlateau[(y_-i)*ROW_FLOW_NUMBER+x_].vars["playedBy"].GetUInt())	i++;
	nbFound+=i-1;
	log.Info("Verticale : "+nbFound);
	if (nbFound>=REQUIRED_TO_WIN)
		return true;
	// ## Diagonal Search
	i=0;
	while (y_+i<ROW_FLOW_NUMBER && x_+i<ROW_FLOW_NUMBER && activePlayer==tblPlateau[(y_+i)*ROW_FLOW_NUMBER+x_+i].vars["playedBy"].GetUInt()) i++;
	nbFound=i;
	i=0;
	while ( (y_-i)>=0 && (x_-i)>=0 && activePlayer==tblPlateau[(y_-i)*ROW_FLOW_NUMBER+x_-i].vars["playedBy"].GetUInt())  i++;
	nbFound+=i-1;
	log.Info("Diagonal / : "+nbFound+" ");
	if (nbFound>=REQUIRED_TO_WIN)
		return true;
	i=0;
	while (y_+i<ROW_FLOW_NUMBER && x_-i>=0 && activePlayer==tblPlateau[(y_+i)*ROW_FLOW_NUMBER+x_-i].vars["playedBy"].GetUInt()) i++;
	nbFound=i;
	i=0;
	while ( (y_-i)>=0 && (x_+i)<ROW_FLOW_NUMBER && activePlayer==tblPlateau[(y_-i)*ROW_FLOW_NUMBER+x_+i].vars["playedBy"].GetUInt()) i++;
	nbFound+=i-1;
	log.Info("Diagonal \\ : "+nbFound+" ");
	if (nbFound>=REQUIRED_TO_WIN)
		return true;
	return false;
}
/**
 * Cast a Ray and store the 3D pos in hitPos, and the node in hitDrawable (stolen from 08_decals)
  * */
bool Raycast(float maxDistance, Vector3& hitPos, Drawable@& hitDrawable)
{
	IntVector2 pos;
	hitDrawable = null;
	if (touchEnabled) {
		TouchState@ touch1 = input.touches[0];
		pos = touch1.lastPosition;
	}
	else {
		pos = ui.cursorPosition;

	}


	// Check the cursor is visible and there is no UI element in front of the cursor
	if (!ui.cursor.visible || ui.GetElementAt(pos, true) !is null)
		return false;
	Camera@ camera = cameraNodeScene.GetComponent("Camera");
	Ray cameraRay = camera.GetScreenRay(float(pos.x) / graphics.width, float(pos.y) / graphics.height);
	// Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
	// Note the convenience accessor to scene's Octree component
	RayQueryResult result = scene_.octree.RaycastSingle(cameraRay, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY);
	if (result.drawable !is null) {
		hitPos = result.position;
		hitDrawable = result.drawable;
		return true;
	}
	return false;
}

void SubscribeToEvents()
{
	// Subscribe HandleUpdate() function for processing update events
	SubscribeToEvent("Update", "HandleUpdate");
	// debug geometry
	SubscribeToEvent("PostRenderUpdate", "HandlePostRenderUpdate");
	//Touch Events :
	SubscribeToTouchEvents();
}

void HandleUpdate(StringHash eventType, VariantMap& eventData)
{
	// Take the frame time step, which is stored as a float
	float timeStep = eventData["TimeStep"].GetFloat();
	// Move the camera, scale movement with time step
	MoveCamera(timeStep);

}
/*
 * Needed for the debug geometry
 */
void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
	// If draw debug mode is enabled, draw viewport debug geometry. This time use depth test, as otherwise the result becomes
	// hard to interpret due to large object count
	if (drawDebug)
		renderer.DrawDebugGeometry(true);
}
[/code]

The major "bug" currently is to differentiate :
--> A touch witouth more that 5 of move to place piece
--> A touch + move to define a rotate camera

You can use 2 fingers to zoom in/out of the scene

-------------------------

aster2013 | 2017-01-02 00:58:46 UTC | #5

:smiley: You can create a 2D tic tac toe sample, if you like.

-------------------------

gasp | 2017-01-02 00:58:50 UTC | #6

better touch & general feeling :
Scripts\00_morpion.as :
[code]
// TicTacToe 3D scene example.
// This sample demonstrates:
//     - Creating a 3D scene with static content
//     - Raytracing to select a node and use "vars" to store data
//     - using touch / mouse controle to play the game

#include "Scripts/Utilities/Sample.as"
#include "Scripts/Utilities/Touch2.as"

const float FLOOR_ELEMENT_SIZE = 6.0f;	// Change scale of the game
const int ROW_FLOW_NUMBER=3;	        // Play area is a square, so row = column
const int REQUIRED_TO_WIN=3;	        // Number of aligned piece to win
const bool DISABLE_ROTATION=true;		//If true, all the cell a aligned, and not moved on click

// Movement speed as world units per second
const float MOVE_SPEED = 20.0f;
// Mouse sensitivity as degrees per pixel
const float MOUSE_SENSITIVITY = 0.1f;

Scene@ scene_;
Node@ cameraNodeScene;
//Camera Controles
float yaw = 0.0f;
float pitch = 30.0f;
float moveSens = 0.0f;
float moveStep = 0.0f;

IntVector2 tokenPosition;
bool tokenNeeded = false;

Array<Node@> tblMenu;
Node@ menu;
Array<Node@> tblPlateau;
Node@ plateauParent;

Text@ activePlayerText ;
const int OWNED_BY_NO_ONE=0;
bool gameActive=false;	
bool drawDebug = false;
uint activePlayer=1;	// 1st played is the first to play :p
int numCasePlayed =0;

void Start()
{
	// Execute the common startup for samples
	SampleStart();

	// Create the scene content
	CreateScene();

	//Detect Touch Device
	InitTouchInput();

	// Create the UI content
	CreateUI();

	// Setup the viewport for displaying the scene
	SetupViewport();

	// Hook up to the frame update events
	SubscribeToEvents();
	
	//Show the game menu
	showMenu();
}

void SubscribeToEvents()
{
	// Subscribe HandleUpdate() function for processing update events
	SubscribeToEvent("Update", "HandleUpdate");
	// debug geometry
	SubscribeToEvent("PostRenderUpdate", "HandlePostRenderUpdate");
	// touch Events :
	SubscribeToTouchEvents();
	//Is this the proper way ?
	SubscribeToEvent("menuEventStartGame","createNewGame");
	SubscribeToEvent("menuEventExit","exitProgramme");
}
void exitProgramme()
{
	engine.Exit();
}
void HandleUpdate(StringHash eventType, VariantMap& eventData)
{
	// Take the frame time step, which is stored as a float
	float timeStep = eventData["TimeStep"].GetFloat();
	//Update the touchControl from touch2.as
	UpdateTouches();
	//Update the global var to feed ReactToInput()
	manageTouchDevice();
	manageMouseDevice();
	// Move the camera, scale movement with time step, place a token
	ReactToInput(timeStep);
}
void manageTouchDevice()
{
	if (touchControl.zoom) {
		moveStep=Abs(touchControl.zoomSpeed) ;
		moveSens=touchControl.zoomSens;
	} else {
		yaw+=touchControl.dragX;
		pitch+=touchControl.dragY;
	}
	if (touchControl.singleTouch) {
		tokenPosition = touchControl.touchlastPos;
		// We don't want to go more than once
		touchControl.singleTouch=false;
		tokenNeeded=true;
	}
}
void manageMouseDevice()
{
	// Right mouse button controls mouse cursor visibility: hide when pressed
	ui.cursor.visible = !input.mouseButtonDown[MOUSEB_RIGHT];
	// Do not move if the UI has a focused element (the console)
	if (ui.focusElement !is null)
		return;
	if (!ui.cursor.visible) {
		IntVector2 mouseMove = input.mouseMove;
		if (Abs(mouseMove.x) > MOUSE_SENSITIVITY)
			yaw+= mouseMove.x * MOUSE_SENSITIVITY;
		if (Abs(mouseMove.y) > MOUSE_SENSITIVITY)
			pitch +=  mouseMove.y * MOUSE_SENSITIVITY;
	}
	moveStep=MOVE_SPEED;
	if (input.keyDown[KEY_DOWN])
		moveSens = -1.0f;
	if (input.keyDown[KEY_UP])
		moveSens = 1.0f;
	//Check what is  clicked, and if game engine need to react
	if (ui.cursor.visible && input.mouseButtonPress[MOUSEB_LEFT]) {
		tokenNeeded=true;						//we want to place a token
		tokenPosition = ui.cursorPosition;		//at this position (see RayCast)
	}
	//The following is for information
	//for the end of the game
	if (input.keyDown[KEY_E])
		endCurrentGame();
	//restart a game
	if (input.keyDown[KEY_S])
		createNewGame	();
	//Active / Desactive debug geometry
	if (input.keyPress[KEY_SPACE])
		drawDebug = !drawDebug;
}

/**
 * what the engine need to do
 */
void ReactToInput(float timeStep)
{
	//cameraNodeScene.rotation = Quaternion(playerControls.pitch, playerControls.yaw, 0.0f);
	if (moveSens!=0.0f)
		cameraNodeScene.Translate(Vector3(0.0f, 0.0f, moveSens) * moveStep * timeStep);
	moveSens=0.0f;
	// Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
	pitch = Clamp(pitch, -90.0f, 90.0f);
	cameraNodeScene.rotation = Quaternion(pitch, yaw, 0.0f);
	if (tokenNeeded)
		whatHaveYouCLicked();

}

void CreateUI()
{
	// Create a Cursor UI element because we want to be able to hide and show it at will. When hidden, the mouse cursor will
	// control the camera, and when visible, it will point the raycast target
	XMLFile@ style = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
	Cursor@ cursor = Cursor();
	cursor.SetStyleAuto(style);
	ui.cursor = cursor;
	// Set starting position of the cursor at the rendering window center
	cursor.SetPosition(graphics.width / 2, graphics.height / 2);
if (touchEnabled)
	ui.cursor.visible=false;
	// Construct new Text object, set string to display and font to use
	Text@ instructionText = ui.root.CreateChild("Text");
	instructionText.text =
	    "Use up,down to move\n"
	    //"Use \"e\" End the game, \"s\" re-start a game\n"
	    "LMB to place ticTacToe Element, RMB to rotate view\n"
	    "You need : "+REQUIRED_TO_WIN+" token aligned to win \n"
	    "Space to show debug geometry\n";

	instructionText.SetFont(cache.GetResource("Font", "Fonts/Anonymous Pro.ttf"), 15);
	// The text has multiple rows. Center them in relation to each other
	instructionText.textAlignment = HA_CENTER;
	// Position the text relative to the screen center
	instructionText.horizontalAlignment = HA_CENTER;
	instructionText.verticalAlignment = VA_CENTER;
	instructionText.SetPosition(0, ui.root.height / 4);
	//Define the green text who permit to inform the player the status of the game
	activePlayerText = ui.root.CreateChild("Text");
	activePlayerText.text ="player "+activePlayer;
	activePlayerText.textAlignment = HA_CENTER;
	activePlayerText.horizontalAlignment = HA_CENTER;
	activePlayerText.verticalAlignment = VA_BOTTOM;
	activePlayerText.SetPosition(0, 1);
	activePlayerText.SetFont(cache.GetResource("Font", "Fonts/Anonymous Pro.ttf"), 30);
	activePlayerText.color = Color(0.0f, 1.0f, 0.0f);

}

void CreateScene()
{
	scene_ = Scene();
	// Create the Octree component to the scene. This is required before adding any drawable components, or else nothing will
	// show up. The default octree volume will be from (-1000, -1000, -1000) to (1000, 1000, 1000) in world coordinates; it
	// is also legal to place objects outside the volume but their visibility can then not be checked in a hierarchically
	// optimizing manner
	scene_.CreateComponent("Octree");
	scene_.CreateComponent("DebugRenderer");
	// Create a directional light to the world so that we can see something. The light scene node's orientation controls the
	// light direction; we will use the SetDirection() function which calculates the orientation from a forward direction vector.
	// The light will use default settings (white light, no shadows)
	Node@ lightNode = scene_.CreateChild("DirectionalLight");
	lightNode.direction = Vector3(0.6f, -1.0f, 0.8f); // The direction vector does not need to be normalized
	Light@ light = lightNode.CreateComponent("Light");
	light.lightType = LIGHT_DIRECTIONAL;

	// Create a scene node for the camera, which we will move around
	// The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
	cameraNodeScene = scene_.CreateChild("Camera");
	cameraNodeScene.CreateComponent("Camera");

	// Set an initial position for the camera scene node above the plane
	cameraNodeScene.position = Vector3((FLOOR_ELEMENT_SIZE*ROW_FLOW_NUMBER)/2, 10.0f, -15.0f);
	cameraNodeScene.Pitch(pitch);
	cameraNodeScene.Yaw(yaw);


}



void SetupViewport()
{
	// Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
	// at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
	// use, but now we just use full screen and default render path configured in the engine command line options
	Viewport@ viewport = Viewport(scene_, cameraNodeScene.GetComponent("Camera"));
	renderer.viewports[0] = viewport;
}

/**
 * basic menu
 * */
void showMenu()
{
	gameActive=false;
	menu = scene_.CreateChild("menu");
	addMenuItem(graphics.width/3,80.0f,"CreateNewGame","menuEventStartGame");
	addMenuItem(graphics.width/3,80.0f + graphics.height/100*5,    "option 1","menuEventNotMapped");
	addMenuItem(graphics.width/3,80.0f + graphics.height/100*5 * 2,"option 2","menuEventNotMapped");
	addMenuItem(graphics.width/3,80.0f + graphics.height/100*5 * 3,"option 3","menuEventNotMapped");
	addMenuItem(graphics.width/3,80.0f + graphics.height/100*5 * 4 ,"Exit the program","menuEventExit");
}
/*
 * Add an item to the game menu, function name used to call the related event
 * */
void addMenuItem(float x,float y,String libelle,String function)
{
	Node@ textNode = menu.CreateChild("menuOption");
	textNode.vars["function"]=function;	//will be used to know which function needed to rtun (funcdef ...)
	//Place the text
	Camera@ camera = cameraNodeScene.GetComponent("Camera");
	textNode.position = camera.ScreenToWorldPoint(Vector3(x / graphics.width, y / graphics.height, 10.0f));
	//define texte attribut
	Text3D@ text3D = textNode.CreateComponent("Text3D");
	Font@ font = cache.GetResource("Font", "Fonts/BlueHighway.ttf");
	text3D.SetFont(font, graphics.height/100*5);
	text3D.color = Color(1, 1, 0);
	text3D.text = libelle;
	text3D.faceCamera = false;
	tblMenu.Push(textNode);
}
void createNewGame()
{
	//we don't recreate a game if we already have an active game
	if (gameActive)
		return;
	numCasePlayed=0;
	endCurrentGame();
	//Remove the menu
	tblMenu.Clear();
	menu.RemoveAllChildren();
	//we need a parent node
	plateauParent  = scene_.CreateChild("damier");
	//Create the "floor" with a list of node who will be valid target for raycasting
	for (uint j = 0; j < ROW_FLOW_NUMBER; ++j) {
		for (uint i = 0; i < ROW_FLOW_NUMBER; ++i) {
			Node@ floorNode = plateauParent.CreateChild("damier");
			//Setting vars who will help up to track what is doable and what is not
			floorNode.vars["x"]=i;
			floorNode.vars["y"]=j;
			floorNode.vars["playedBy"]=OWNED_BY_NO_ONE;	//Case not played
			floorNode.position = Vector3(i*FLOOR_ELEMENT_SIZE+(FLOOR_ELEMENT_SIZE/2), 0.0f, j*FLOOR_ELEMENT_SIZE+(FLOOR_ELEMENT_SIZE/2));
			//We re-use already present materials, they use 99% of the FLOOR_ELEMENT_SIZE
			floorNode.scale=Vector3(FLOOR_ELEMENT_SIZE-(FLOOR_ELEMENT_SIZE/100),-(FLOOR_ELEMENT_SIZE/100),FLOOR_ELEMENT_SIZE-(FLOOR_ELEMENT_SIZE/100));
			//create the static model
			StaticModel@ floorStaticModel = floorNode.CreateComponent("StaticModel");
			floorStaticModel.model = 	cache.GetResource("Model", "Models/Box.mdl");
			floorStaticModel.material = cache.GetResource("Material", "Materials/Stone.xml");
			//Save in an Array of Node@
			tblPlateau.Push(floorNode);
		}
	}
	// rotate the floor for a poorly visual effect
	if (!DISABLE_ROTATION) {
		for (uint i = 0; i < tblPlateau.length; ++i) {
			tblPlateau[i].Rotate(Quaternion(0.0f, 30.0f, 0.0f));
			Print(tblPlateau[i].vars["x"]);
		}
	}
	gameActive=true;
	activePlayer=1;
	activePlayerText.text ="player "+activePlayer;
}
void endCurrentGame()
{
	// When we remove node, the local var are delete
	// so we do not need to reset them
	if (tblPlateau  !is null && plateauParent !is null) {
		tblPlateau.Clear();
		plateauParent.RemoveAllChildren();
	}
	gameActive=false;
}
void whatHaveYouCLicked()
{
	tokenNeeded=false;
	Vector3 hitPos;
	Drawable@ hitDrawable;
	if (Raycast(250.0f, hitPos, hitDrawable)) {
		// search with floor coords what cell is touched by the ray vector3 impact point
		/** not used for reference only
		int caseXpos = (hitPos.x/FLOOR_ELEMENT_SIZE);
		int caseYpos = (hitPos.z/FLOOR_ELEMENT_SIZE);
		 */
		//2nd method : Selected Node
		Node@ selectedNode = hitDrawable.node;

		if (selectedNode.name == "menuOption") {
			// apparently if the event don't exist, no warning, no error
			selectedNode.SendEvent(selectedNode.vars["function"].GetString());
		}
		if (selectedNode.name =="damier" &&	gameActive) {	// only active when "game" is active
			if (selectedNode.vars["playedBy"].GetUInt()==0) {
				int caseX = selectedNode.vars["x"].GetUInt();
				int caseY = selectedNode.vars["y"].GetUInt();
				uint indice=caseY*ROW_FLOW_NUMBER+caseX;		//linearize the coordonnates
				if (!DISABLE_ROTATION
				    && indice<=tblPlateau.length) {
					tblPlateau[indice].Rotate(Quaternion(0.0f, -30.0f, 0.0f));
				}
				//we link the game element (Cross/Cicle normally) to it's node to be able to be removed when game end
				Node@ gameElementNode = plateauParent.CreateChild("player"+activePlayer+" gameElement");
				//we center the element  in the dalle
				gameElementNode.position = Vector3(caseX*FLOOR_ELEMENT_SIZE+(FLOOR_ELEMENT_SIZE/2), 0.2f, caseY*FLOOR_ELEMENT_SIZE+(FLOOR_ELEMENT_SIZE/2));
				StaticModel@ staticModel = gameElementNode.CreateComponent("StaticModel");
				log.Info("Player " + activePlayer +" have play in ["+selectedNode.vars["x"].GetUInt()+"]["+selectedNode.vars["y"].GetUInt()+"]");
				//set node local vars
				selectedNode.vars["playedBy"]= activePlayer ;
				//easy way to know if all case are full
				numCasePlayed++;
				if (activePlayer==1) {
					staticModel.model = cache.GetResource("Model", "Models/Sphere.mdl");
					staticModel.material = cache.GetResource("Material", "Materials/Terrain.xml");
					//We scale object according to the floor size
					gameElementNode.SetScale(FLOOR_ELEMENT_SIZE/4.0f);
				} else {
					staticModel.model = cache.GetResource("Model", "Models/Torus.mdl");
					staticModel.material = cache.GetResource("Material", "Materials/Terrain.xml");
					gameElementNode.SetScale(FLOOR_ELEMENT_SIZE/4.0f);
				}
				// Did we have a winner ?
				if (didWeHaveAWinner(caseX,caseY)) {
					activePlayerText.text ="player "+activePlayer +" Win!" ;
					showMenu();
				}
				//all area fill & no winner
				else if (numCasePlayed == ROW_FLOW_NUMBER*ROW_FLOW_NUMBER) {
					activePlayerText.text="End Of Game, it's a draw !";
					showMenu();
				} else {
					//game continue, change current player
					if (activePlayer==1)
						activePlayer=2;
					else
						activePlayer=1;
					activePlayerText.text ="player "+activePlayer;
				}
			} else {
				log.Info ("!! Node Already played by player "+selectedNode.vars["playedBy"].GetUInt()+"["+selectedNode.vars["x"].GetUInt()+"]["+selectedNode.vars["y"].GetUInt()+"]");
			}
		}
	}
}

/**
 * Detection of a winner
 * */
bool didWeHaveAWinner(int x_,int y_)
{
	int nbFound=0;
	int i=0;
	int indice=0;
	// ## Horizontal Search
	while (x_+i<ROW_FLOW_NUMBER && activePlayer==tblPlateau[y_*ROW_FLOW_NUMBER+x_+i].vars["playedBy"].GetUInt()) i++;
	nbFound=i;
	i=0;
	while (x_-i>=0 && activePlayer==tblPlateau[y_*ROW_FLOW_NUMBER+x_-i].vars["playedBy"].GetUInt()) i++;
	nbFound+=i-1;	//we doesn't count 2 time the originate cell
	log.Info("Horizontale : "+nbFound+" ");
	if (nbFound>=REQUIRED_TO_WIN)	//did we have we a winner ?
		return true;
	// ## Vertical search
	i=0;
	while (y_+i<ROW_FLOW_NUMBER && activePlayer==tblPlateau[(y_+i)*ROW_FLOW_NUMBER+x_].vars["playedBy"].GetUInt()) i++;
	nbFound=i;
	i=0;//go "Down"
	while ((y_-i)>=0 && activePlayer==tblPlateau[(y_-i)*ROW_FLOW_NUMBER+x_].vars["playedBy"].GetUInt())	i++;
	nbFound+=i-1;
	log.Info("Verticale : "+nbFound);
	if (nbFound>=REQUIRED_TO_WIN)
		return true;
	// ## Diagonal Search
	i=0;
	while (y_+i<ROW_FLOW_NUMBER && x_+i<ROW_FLOW_NUMBER && activePlayer==tblPlateau[(y_+i)*ROW_FLOW_NUMBER+x_+i].vars["playedBy"].GetUInt()) i++;
	nbFound=i;
	i=0;
	while ( (y_-i)>=0 && (x_-i)>=0 && activePlayer==tblPlateau[(y_-i)*ROW_FLOW_NUMBER+x_-i].vars["playedBy"].GetUInt())  i++;
	nbFound+=i-1;
	log.Info("Diagonal / : "+nbFound+" ");
	if (nbFound>=REQUIRED_TO_WIN)
		return true;
	i=0;
	while (y_+i<ROW_FLOW_NUMBER && x_-i>=0 && activePlayer==tblPlateau[(y_+i)*ROW_FLOW_NUMBER+x_-i].vars["playedBy"].GetUInt()) i++;
	nbFound=i;
	i=0;
	while ( (y_-i)>=0 && (x_+i)<ROW_FLOW_NUMBER && activePlayer==tblPlateau[(y_-i)*ROW_FLOW_NUMBER+x_+i].vars["playedBy"].GetUInt()) i++;
	nbFound+=i-1;
	log.Info("Diagonal \\ : "+nbFound+" ");
	if (nbFound>=REQUIRED_TO_WIN)
		return true;
	return false;
}
/**
 * Cast a Ray and store the 3D pos in hitPos, and the node in hitDrawable (stolen from 08_decals)
  * */
bool Raycast(float maxDistance, Vector3& hitPos, Drawable@& hitDrawable)
{
	IntVector2 pos;
	hitDrawable = null;
	pos = tokenPosition;
	// Check the cursor is visible and there is no UI element in front of the cursor
	if (!ui.cursor.visible || ui.GetElementAt(pos, true) !is null)
		return false;
	Camera@ camera = cameraNodeScene.GetComponent("Camera");
	Ray cameraRay = camera.GetScreenRay(float(pos.x) / graphics.width, float(pos.y) / graphics.height);
	// Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
	// Note the convenience accessor to scene's Octree component
	RayQueryResult result = scene_.octree.RaycastSingle(cameraRay, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY);
	if (result.drawable !is null) {
		hitPos = result.position;
		hitDrawable = result.drawable;
		return true;
	}
	return false;
}

/*
 * Needed for the debug geometry
 */
void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
	// If draw debug mode is enabled, draw viewport debug geometry. This time use depth test, as otherwise the result becomes
	// hard to interpret due to large object count
	if (drawDebug)
		renderer.DrawDebugGeometry(true);
}

[/code]
a second file to manage the touch input, put it in Utilities\Touch2.as:
[code]
// Mobile framework for Android/iOS

// Setup:
// - On init, call this script using '#include "Scripts/Utilities/Touch2.as"' 
//   then 'InitTouchInput()' to detect touchEnbled engine on mobile platforms 
// - Subscribe to touch events  using 'SubscribeToTouchEvents()'
// - Call the update function 'UpdateTouches()' from HandleUpdate or equivalent update handler function

// Usage : 
// Gyroscope : disabled not tested for now
// after updateTouches() you can test the following states :
// Touches patterns:
//     - 1 finger  touch  = touchControl.singleTouch' set to true and IntVector2 touchControl.touchlastPos can be used to raycast stuff / ui
//							you need to use 'touchControl.singleTouchReset();' after you have used the 1 finger touch value
//     - 1 or 2 finger  drag  = touchControl.dragX/touchControl.dragY : the value slide (> or <0)
//     - 2 fingers sliding in opposite direction = touchControl.zoom true and touchControl.zoomSens : 1 or -1 (0 if not used)
//     - 3,4 fingers touch = read touchControl.numberOfFinger, not inplemented 



//Constant
const float TOUCH_SENSITIVITY = 0.1f;
const bool  TOUCH_GYROSCOPE_ENABLED = false;
const float TOUCH_GYROSCOPE_THRESHOLD = 0.1;

//Global Vars
bool touchEnabled = false;
TouchControls touchControl;



void SubscribeToTouchEvents()
{
	SubscribeToEvent("TouchBegin", "HandleTouchBegin");
	SubscribeToEvent("TouchEnd", "HandleTouchEnd");
}

/*
void UpdateDeprecated()
{
		// Clamp to screen
	if (helloText.position.x+touchControl.dragX >0 && helloText.position.x+touchControl.dragX < graphics.width - helloText.size.x &&
		helloText.position.y+touchControl.dragY >0 && helloText.position.y+touchControl.dragY < graphics.height - helloText.size.y) 
	helloText.SetPosition(helloText.position.x+touchControl.dragX,helloText.position.y+touchControl.dragY);
	/* *
	* Point you'r update() function who can :
	* 	--> Move the camera, player ...
	*  --> Use the touchControl.singleTouch like below to use it as a single touch without move,
	* 		don't forget to set singleTouch to false, if you don't want to launch the function 10 times
	/
	if (input.numTouches==0 && touchControl.singleTouch) {
		log.Info("Tadam On ray !!!");
			//Clamp top screen
		if (touchControl.touchlastPos.x > graphics.width - helloText.size.x-(helloText.size.x)/2)
			touchControl.touchlastPos.x=graphics.width - helloText.size.x;
		if (touchControl.touchlastPos.y > graphics.height - helloText.size.y-(helloText.size.y)/2)
			touchControl.touchlastPos.y=graphics.height- helloText.size.y;			
			
		helloText.SetPosition(touchControl.touchlastPos.x-(helloText.size.x)/2,touchControl.touchlastPos.y-(helloText.size.y)/2);
		//We only want this 1 times
		touchControl.singleTouchReset();		
	}
}
*/

/*
 * the code below is exclusivly for the touch feature
 * */

void InitTouchInput()
{
	if (GetPlatform() == "Android" || GetPlatform() == "iOS") {
		touchEnabled = true;
		log.Info("Touch Enabled");
	}
}
/**
 * Event handlers
 */
void HandleTouchBegin(StringHash eventType, VariantMap& eventData)
{
	// Get touch coordinates of the 1st point
	touchControl.touchInitPos = IntVector2(eventData["X"].GetInt(), eventData["Y"].GetInt());
	// Get #touches or dragging value
	int touchID = eventData["TouchID"].GetInt();
	log.Info("HandleTouchBegin "+touchID);
	// We need to reset the 1 finger touch
	touchControl.singleTouch=false;
}
void HandleTouchEnd(StringHash eventType, VariantMap& eventData)
{
	log.Info(touchControl.touchlastPos.x+"/"+touchControl.touchlastPos.y);
		
	touchControl.resetBeforeUpdate();
	log.Info("HandleTouchEnd");
	//Did we have a single touch or a drag
	touchControl.release();
}
/**
 * Handle continuous usage a finger (aka when the finger is posed)
 */
void UpdateTouches()
{
	if (!touchEnabled)
		return;
	//if any finger on the update panel, don't try to update something !
	if (input.numTouches==0)
		return;
	
	//Reset current values
	touchControl.resetBeforeUpdate();
	TouchState@ touch1 = input.touches[0];
	touchControl.touchlastPos.x=touch1.position.x;
	touchControl.touchlastPos.y=touch1.position.y;

		
	//  ## 2 finger ##  Zoom in/out
	if (input.numTouches == 2) {
		TouchState@ touch1 = input.touches[0];
		TouchState@ touch2 = input.touches[1];
		// Check for zoom pattern (touches moving in opposite directions)
		if ((touch1.delta.y > 0 && touch2.delta.y < 0) || (touch1.delta.y < 0 && touch2.delta.y > 0))
			touchControl.zoom = true;
		else
			touchControl.zoom = false;

		if (touchControl.zoom) {
			// Check for zoom direction (in/out)
			if (Abs(touch1.position.y - touch2.position.y) > Abs(touch1.lastPosition.y - touch2.lastPosition.y))
				touchControl.zoomSens = 1;
			else
				touchControl.zoomSens = -1;
		//Experimental
		
		touchControl.zoomSpeed=(Abs(touch1.delta.y)+Abs(touch2.delta.y) + Abs(touch1.delta.x)+Abs(touch2.delta.x))*TOUCH_SENSITIVITY;
		log.Info(touchControl.zoomSpeed);
		}
	}
	//  ## 1 finger or 2 finger not zooming ##
	if (input.numTouches == 1 ||(input.numTouches == 2 && touchControl.zoom==false)) 
		{
		TouchState@ touch1 = input.touches[0];
		if  (Abs(touch1.delta.x)>TOUCH_SENSITIVITY)
			touchControl.dragX=touch1.delta.x * TOUCH_SENSITIVITY;	//TODO : Test sensitiviy
		if  (Abs(touch1.delta.y) > TOUCH_SENSITIVITY )
			touchControl.dragY=touch1.delta.y * TOUCH_SENSITIVITY;
	}	
	//Not tested for now
	if (TOUCH_GYROSCOPE_ENABLED) {
		// Gyroscope (emulated by SDL through a virtual joystick)
		if (input.numJoysticks > 0) { // numJoysticks = 1 on iOS & Android
			JoystickState@ joystick = input.joysticks[0];
			if (joystick.numAxes >= 2) {
				if (Abs(joystick.axisPosition[0]) > TOUCH_GYROSCOPE_THRESHOLD)
					touchControl.gyroscopeX=joystick.axisPosition[0];
				if (Abs(joystick.axisPosition[1]) > TOUCH_GYROSCOPE_THRESHOLD)
					touchControl.gyroscopeY=joystick.axisPosition[1];
			}
		}
	}
}

class TouchControls
{
	//used in UpdateTouches
	int dragX,dragY=0;				// Current drag movment
	float gyroscopeX,gyroscopeY=0;	// Gyroscope movement
	bool zoom = false;
	int zoomSens = 1 ;	//Sense of the zoom -1 / 1
	int numberOfFinger=0;
	float zoomSpeed = 0 ;
	
	//used in HandleTouchBegin
	IntVector2 touchInitPos(0,0);
	//updated in HandleTouchEnd
	IntVector2 touchlastPos(0,0);
	bool singleTouch = false; //1 finger touch

	//Constructor
	TouchControls() 
	{
		log.Info("Calling TouchControls Constructor");
	}
	void release() 
	{
		TouchState@ touch1 = input.touches[0];
		if ( Abs(touchControl.touchInitPos.x-touchControl.touchlastPos.x) > TOUCH_SENSITIVITY ||
		     Abs(touchControl.touchInitPos.y-touchControl.touchlastPos.y) > TOUCH_SENSITIVITY) {
			singleTouch=false;
//			log.Info("move it !"+Abs(touchControl.touchInitPos.x-touchControl.touchlastPos.x) +" "+ Abs(touchControl.touchInitPos.y-touchControl.touchlastPos.y) );
//			log.Info(helloText.position.x+"@"+helloText.position.y);
		} else {
			singleTouch=true;
			log.Info("singleTouch !");
		}
	}
	
	void resetBeforeUpdate() 
	{
		numberOfFinger=input.numTouches;
		zoomSpeed=dragX=dragY=zoomSens=0;
		gyroscopeX=gyroscopeY=0.0f;
		zoom=false;
	}
}

[/code]
tested in windows , android. need a polish on the touch feature, goal is to learn to use Urho3D, not to do the pretty best stuff for now :p

[img]http://i.imgur.com/i49sfB7.png[/img]
[img]http://i.imgur.com/AQRO0mE.png[/img]

-------------------------

