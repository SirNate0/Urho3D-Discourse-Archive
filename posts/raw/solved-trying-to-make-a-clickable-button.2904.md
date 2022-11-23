noals | 2017-03-16 02:22:37 UTC | #1

hi,
i'm trying to make a clickable button following the helloGUI exemple  but it seem i don't have the click recognized by my program.

even if i try 
<code>    if (clicked)
            {
                engine_->Exit();
            }</code>
nothing happens.

here is my code :
<code>
#include stuff...

using namespace Urho3D;
using namespace KeyDown;

class projet : public Application
{

    URHO3D_OBJECT(projet, Application)

public:

////______________________
////    DEFINITION    

    SharedPtr<Scene> my_scene;

    //about camera
    SharedPtr<Node> camNode;

    SharedPtr<Node> floorNode;
    AnimatedModel* floorObject;
    RigidBody* floorBody;
    CollisionShape* floorBBox;

    //physic
    bool drawDebug_;

    //about UI
	SharedPtr<UIElement> uiRoot_;

	SharedPtr<Window> MenuWindows_;

	SharedPtr<Button> NewGame_;
	SharedPtr<Button> Continue_;
	SharedPtr<Button> Options_;
	SharedPtr<Button> Quit_;
	
	SharedPtr<Window> OptionWindow_;
	SharedPtr<CheckBox> FullScreen_;


    projet(Context* context) : Application(context)
    {

    }

    virtual void Setup()
    {
        engineParameters_["FullScreen"]=true;
        engineParameters_["WindowWidth"]=1920;
        engineParameters_["WindowHeight"]=1080;
        engineParameters_["WindowResizable"]=true;
    }

    virtual void Start()
    {

        ResourceCache* cache=GetSubsystem<ResourceCache>();

        my_scene=new Scene(context_);
        my_scene->CreateComponent<Octree>();
        my_scene->CreateComponent<DebugRenderer>();
//physic
        PhysicsWorld* physicWorld = my_scene->CreateComponent<PhysicsWorld>();
        //physicWorld->SetInternalEdge(true);




//UI

	uiRoot_=GetSubsystem<UI>()->GetRoot();

        // Load XML file containing default UI style sheet
        cache = GetSubsystem<ResourceCache>();
        XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");

        // Set the loaded style as default style
        uiRoot_->SetDefaultStyle(style);

//menu window
        MenuWindows_ = new Window(context_);

        // Set Window size and layout settings
        MenuWindows_->SetLayout(LM_VERTICAL, 0, IntRect(140, 260, 30, 30));  //  x>, yv,  spacing interne
        MenuWindows_->SetPosition(110, 650);
        MenuWindows_->SetName("Menu");
	MenuWindows_->SetStyleAuto();
        MenuWindows_->SetColor(Color(0,128,128,0.5));

	
	    NewGame_ = new Button(context_);  
            NewGame_->SetTexture(cache->GetResource<Texture>("Textures/floor_texture.png"));
            NewGame_->SetName("NewGame");
            NewGame_->SetStyleAuto();
            NewGame_->SetLayout(LM_HORIZONTAL, 0, IntRect( 150, 40, 0, 0));
            NewGame_->SetPosition(120, 700);
            NewGame_->SetColor(Color(255,0,0,1));

	    Continue_ = new Button(context_);
            Continue_->SetName("Continue");
	    Continue_->SetStyleAuto();
            Continue_->SetLayout(LM_HORIZONTAL, 0, IntRect( 150, 40, 0, 0));
            Continue_->SetPosition(120, 750);
            Continue_->SetColor(Color(255,0,0,1));

	    Options_ = new Button(context_);
            Options_->SetName("Options");
	    Options_->SetStyleAuto();
            Options_->SetLayout(LM_HORIZONTAL, 0, IntRect( 150, 40, 0, 0));
            Options_->SetPosition(120, 800);
            Options_->SetColor(Color(255,0,0,1));

	    Quit_ = new Button(context_);
            Quit_->SetName("Quit");
	    Quit_->SetStyleAuto();
            Quit_->SetLayout(LM_HORIZONTAL, 0, IntRect( 150, 40, 0, 0));
            Quit_->SetPosition(120, 850);
            Quit_->SetColor(Color(255,0,0,1));


// to UI root
	uiRoot_->AddChild(MenuWindows_);
        uiRoot_->AddChild(NewGame_);
        uiRoot_->AddChild(Continue_);
	uiRoot_->AddChild(Options_);
        uiRoot_->AddChild(Quit_);



////__________________
////    CAMERA        


        camNode=my_scene->CreateChild("camNode");
        Camera* camObject=camNode->CreateComponent<Camera>();
        camObject->SetFarClip(2000);
	camNode->SetWorldPosition(Vector3(0,15,-15));     //x =blender y //y =blender z hauteur //z =blender x profondeur
	camNode->LookAt(Vector3::ZERO);   //torsoNode->GetPosition()); //

        //camera light
        {
            Light* light=camNode->CreateComponent<Light>();
            light->SetLightType(LIGHT_POINT);
            light->SetRange(25);
            light->SetBrightness(2.0);
            light->SetColor(Color(.8,1,.8,1.0));
        }


////__________________
////    RENDER    


        Renderer* renderer=GetSubsystem<Renderer>();
        SharedPtr<Viewport> viewport(new Viewport(context_,my_scene,camNode->GetComponent<Camera>()));
        renderer->SetViewport(0,viewport);


//////////////////////
////    EVENTS    ////
//////////////////////

    //SubscribeToEvent(E_BEGINFRAME,URHO3D_HANDLER(projet,HandleBeginFrame));
    //SubscribeToEvent(E_KEYDOWN,URHO3D_HANDLER(projet,HandleKeyDown));
    //SubscribeToEvent(E_UIMOUSECLICK,URHO3D_HANDLER(projet,HandleControlClicked));
        SubscribeToEvent(E_UPDATE,URHO3D_HANDLER(projet, HandleUpdate));
    //SubscribeToEvent(E_POSTUPDATE,URHO3D_HANDLER(projet,HandlePostUpdate));
    //SubscribeToEvent(E_RENDERUPDATE,URHO3D_HANDLER(projet,HandleRenderUpdate));
        SubscribeToEvent(E_POSTRENDERUPDATE,URHO3D_HANDLER(projet,HandlePostRenderUpdate));
    //SubscribeToEvent(E_ENDFRAME,URHO3D_HANDLER(projet,HandleEndFrame));
        SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(projet, HandleKeyDown));
        SubscribeToEvent(E_MOUSEBUTTONDOWN, URHO3D_HANDLER(projet, HandleMouseClick));
    }

    virtual void Stop()
    {
    }

////________


    void HandleUpdate(StringHash eventType,VariantMap& eventData)
    {
        float timeStep=eventData[Update::P_TIMESTEP].GetFloat();
	float MOVE_SPEED=50.0f;
        Input* input=GetSubsystem<Input>();

	if(input->GetQualifierDown(1))  // 1 is shift, 2 is ctrl, 4 is alt
            MOVE_SPEED*=4;

        if(input->GetKeyDown('D')) //rotate sens inverse horizontal
            camNode->Translate(Vector3(1,0, 0)*MOVE_SPEED*timeStep);
        if(input->GetKeyDown('Q')) //sens montre horizontal
            camNode->Translate(Vector3(-1,0,0)*MOVE_SPEED*timeStep);
        if(input->GetKeyDown('Z')) //zoom avant
            camNode->Translate(Vector3(0,0,1)*MOVE_SPEED*timeStep);
        if(input->GetKeyDown('S')) //zoom arriere
            camNode->Translate(Vector3(0,0,-1)*MOVE_SPEED*timeStep);
	if(input->GetKeyDown('E')) //rotate sens inverse vertical
            camNode->Translate(Vector3(0,1,0)*MOVE_SPEED*timeStep);
        if(input->GetKeyDown('A')) //sens montre vertical
            camNode->Translate(Vector3(0,-1,0)*MOVE_SPEED*timeStep);
        if (input->GetKeyPress(KEY_SPACE)) // Toggle physics debug geometry with space
            drawDebug_ = !drawDebug_;

	if(!GetSubsystem<Input>()->IsMouseGrabbed())
	{
	    IntVector2 mouseMove=input->GetMouseMove();
	    
	    if(mouseMove.x_>-2000000000&&mouseMove.y_>-2000000000)
            {
		camNode->LookAt(Vector3(0,0,0)); //torsoNode->GetPosition()); 
            }
	}
    }

    void HandleKeyDown(StringHash eventType, VariantMap& eventData)
    {

        Graphics* graphics=GetSubsystem<Graphics>();
        int key = eventData[P_KEY].GetInt();

        if (key == KEY_ESC) //ESC to quit
        {
            engine_->Exit();
        }
        else if(key == KEY_TAB) //TAB to toggle mouse cursor
        {
            GetSubsystem<Input>()->SetMouseVisible(!GetSubsystem<Input>()->IsMouseVisible());
            GetSubsystem<Input>()->SetMouseGrabbed(!GetSubsystem<Input>()->IsMouseGrabbed()); 
        }
	else if(key == 'W') //W for fullscreen
	{
	    graphics->ToggleFullscreen();
	}
        else if(key == 'I')
        {
            //GetSubsystem<UI>()->menu->ShowPopup ();
        }
    }

    void HandleMouseClick(StringHash eventType, VariantMap& eventData)
    {
        using namespace MouseButtonDown;
        UIElement* clicked = static_cast<UIElement*>(eventData[E_MOUSEBUTTONDOWN].GetPtr());

        if (clicked == Quit_)
        {
            engine_->Exit();
        }
    }

////________

    void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
    {
    // If draw debug mode is enabled, draw physics debug geometry. Use depth test to make the result easier to interpret
        if (drawDebug_)
            my_scene->GetComponent<PhysicsWorld>()->DrawDebugGeometry(true);
    }


};
URHO3D_DEFINE_APPLICATION_MAIN(projet)</code>

-------------------------

Eugene | 2017-03-15 17:58:27 UTC | #2

What is
[quote="noals, post:1, topic:2904"]
eventData[E_MOUSEBUTTONDOWN]
[/quote]
?
There is no such parameter

-------------------------

noals | 2017-03-15 19:02:15 UTC | #3

ha yes, it is an event instead of a parameter thx , but it doesn't work either with the parameter.
<code>UIElement* clicked = static_cast<UIElement*>(eventData[P_BUTTON].GetPtr());</code>

i will try with this method : 
<code>SubscribeToEvent(buttonClose, E_RELEASED, URHO3D_HANDLER(HelloGUI, HandleClosePressed));</code>

if it work i could make one for each button i think.

edit: it doesn't work the way i do it and it's kinda hard with the examples that aren't up to date.
i don't understand why it doesn't work with the mouse.

-------------------------

noals | 2017-03-15 19:10:33 UTC | #4

i have the mouse working with that :  (like for the keys ><)
<code>
    void HandleMouseClick(StringHash eventType, VariantMap& eventData)
    {
        int mouse = eventData[P_BUTTON].GetInt();
        if (mouse)
        {
                engine_->Exit();
        }
    }
</code>
but i don't see how to link it with the button since the other method doesn't work.

-------------------------

Eugene | 2017-03-15 19:56:28 UTC | #5

`02_HelloGUI` works fine for me, at least C++ version. Does it work for you?

-------------------------

lezak | 2017-03-15 20:57:41 UTC | #6

First of all, You have subscribed to wrong event:
[quote="noals, post:1, topic:2904"]
SubscribeToEvent(E_MOUSEBUTTONDOWN, URHO3D_HANDLER(projet, HandleMouseClick));
[/quote]

This only detects mouse click and not UIElement.
This function is subscribed to right event:
[quote="noals, post:1, topic:2904"]
//SubscribeToEvent(E_UIMOUSECLICK,URHO3D_HANDLER(projet,HandleControlClicked));
[/quote]

Next thing:
[quote="noals, post:3, topic:2904"]
UIElement* clicked = static_cast(eventData[P_BUTTON].GetPtr());
[/quote]

should be: "eventData[P_ELEMENT]".

-------------------------

noals | 2017-03-15 21:52:06 UTC | #7

@Eugene yes, every examples works fine but i forgot an include in my code so i though there was some kind of update between the example and the actual source since sometime it happens in tutorials from the net but the examples are from the source... i'm dumb lol kinda tired those days.. ><

@lezak
thx but it still doesn't work. it makes better sense through since i wanted a pointer from an int. 

i needed to include Urho3D/UI/UIEvents.h
then using namespace UIMouseClick;

SubscribeToEvent(E_UIMOUSECLICK, URHO3D_HANDLER(projet, HandleMouseClick));

    void HandleMouseClick(StringHash eventType, VariantMap& eventData)
    {

        //int mouse = eventData[P_BUTTON].GetInt();
	UIElement* clicked = static_cast<UIElement*>(eventData[P_ELEMENT].GetPtr());

        if (clicked == Quit_)
        {
            engine_->Exit();
        }
    }

but nothing happens.

-------------------------

lezak | 2017-03-15 23:45:05 UTC | #8

So I quickly reproduced Your code (only ui part) and there was a problem with MenuWindows_ being brought to front, add "MenuWindows_->SetBringToFront(false);" after creation to fix it (also You could think about making menu window parent to buttons). 

Another problem was caused by:
>`GetSubsystem<Input>()->SetMouseGrabbed(!GetSubsystem<Input>()->IsMouseGrabbed());`

 in "HandleKeyDown". Commenting it out will fix that or if You want some other solution just search for other topics about cursor toggling.

After that:
`SubscribeToEvent(Quit_, E_RELEASED, URHO3D_HANDLER(Main, HandleCloseButton));
    void Main::HandleUIMouseClick(StringHash eventType, VariantMap & eventData)
    {
        using namespace UIMouseClick;
        UIElement* clicked = static_cast<UIElement*>(eventData[P_ELEMENT].GetPtr());
        if (clicked == Quit_)
        {
            GetSubsystem<Engine>()->Exit();
        }
    }`
worked fine, but personally I prefer to use (this is also working solution):

    SubscribeToEvent(Quit_, E_RELEASED, URHO3D_HANDLER(Main, HandleCloseButton));
    void Main::HandleCloseButton(StringHash eventType, VariantMap & eventData)
    {
        GetSubsystem<Engine>()->Exit();
    }

-------------------------

noals | 2017-03-16 02:31:34 UTC | #9

yes, that's weird, i just added <code>GetSubsystem<Input>()->SetMouseVisible(true);</code> to start with a visible cursor and it fixed it. it works to quit the program, i hope it will work to do others stuff ^^.

for the button parenting, i tryed but it was kinda hard to place things as i wanted with templates, border and stuff so i gave up on it, i guess i can use isVisible() on everything with my UIElement pointer.

for the SetBringToFront(), yes i had this problem too while trying to place my buttons on the screen but that's ok, i can use SetPriority() to control the visibility order of my layers.
edit: my bad, it goes in front if i click on it so i better use SetBringToFront(), i didn't understand what it is for at first. ^^;

thank you.

-------------------------

