noals | 2017-01-02 01:10:22 UTC | #1

hi,

first i installed ubuntu, i though it could be a good idea to use a linux distribution for some programming.
then i was able to compile urho3D through glew-utils was needed. (i say it because it wasn't in the tutorial on the wiki)
then i was able to compile an empty project.

then i made a little textured model with blender and i exported it using the urho3D export plugin in hope i checked the right options.
i tryed to load it but i don't think i used the right method. i'm not familiar with urho3D so if you could tell what i'm missing or the right way to do it, that would be cool.

here is my code :
[code]
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/InputEvents.h>

#include <string>
#include <sstream>
 
#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Resource/XMLFile.h>
#include <Urho3D/IO/Log.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/UI/Button.h>
#include <Urho3D/UI/UIEvents.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Scene/SceneEvents.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/Geometry.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Graphics/DebugRenderer.h>
#include <Urho3D/Graphics/Octree.h>
#include <Urho3D/Graphics/Light.h>
#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Graphics/StaticModel.h>
#include <Urho3D/Graphics/Material.h>
#include <Urho3D/Graphics/Skybox.h>

using namespace Urho3D;

class projet : public Application
{

public:

    //can put definitions here  ex: "int machin;"
	SharedPtr<Scene> scene_;
	SharedPtr<Node> boxNode_;
	Node* cameraNode_;


    projet(Context* context) : Application(context)
    {

    }

    virtual void Setup()
    {
	// See http://urho3d.github.io/documentation/1.32/_main_loop.html
	engineParameters_["FullScreen"]=false;
        engineParameters_["WindowWidth"]=1280;
        engineParameters_["WindowHeight"]=720;
        engineParameters_["WindowResizable"]=true;
    }

    virtual void Start()
    {

	// We will be needing to load resources.
        // All the resources used in this example comes with Urho3D.
        // If the engine can't find them, check the ResourcePrefixPath. <-- http://urho3d.github.io/documentation/1.5/_running.html
        ResourceCache* cache=GetSubsystem<ResourceCache>();

	// Let's setup a scene to render.
        scene_=new Scene(context_);
        // Let the scene have an Octree component!
        scene_->CreateComponent<Octree>();
        // Let's add an additional scene component for fun.
        scene_->CreateComponent<DebugRenderer>();
	// octree ? debugrender ?

	// Let's put a box in there.
        boxNode_=scene_->CreateChild("Box");  //can i change it ?
        boxNode_->SetPosition(Vector3(0,0,0));
        StaticModel* boxObject=boxNode_->CreateComponent<StaticModel>();
        boxObject->SetModel(cache->GetResource<Model>("Models/cor5x20x1/cor5x20x1.mdl"));
        boxObject->SetMaterial(cache->GetResource<Material>("Models/cor5x20x1/cor_5x20x1.xml"));

	 // We need a camera from which the viewport can render.
        cameraNode_=scene_->CreateChild("Camera");
        Camera* camera=cameraNode_->CreateComponent<Camera>();
        camera->SetFarClip(2000);

	// Create two lights
	{
            Node* lightNode=scene_->CreateChild("Light");
            lightNode->SetPosition(Vector3(-5,0,10));
            Light* light=lightNode->CreateComponent<Light>();
            light->SetLightType(LIGHT_POINT);
            light->SetRange(50);
            light->SetBrightness(1.2);
            light->SetColor(Color(1,.5,.8,1));
            light->SetCastShadows(true);
        }
        {
            Node* lightNode=scene_->CreateChild("Light");
            lightNode->SetPosition(Vector3(5,0,10));
            Light* light=lightNode->CreateComponent<Light>();
            light->SetLightType(LIGHT_POINT);
            light->SetRange(50);
            light->SetBrightness(1.2);
            light->SetColor(Color(.5,.8,1,1));
            light->SetCastShadows(true);
        }
	// add one to the camera node as well
        {
            Light* light=cameraNode_->CreateComponent<Light>();
            light->SetLightType(LIGHT_POINT);
            light->SetRange(10);
            light->SetBrightness(2.0);
            light->SetColor(Color(.8,1,.8,1.0));
        }
 


 // Now we setup the viewport. Ofcourse, you can have more than one!
        Renderer* renderer=GetSubsystem<Renderer>();
        SharedPtr<Viewport> viewport(new Viewport(context_,scene_,cameraNode_->GetComponent<Camera>()));
        renderer->SetViewport(0,viewport);

// events
//SubscribeToEvent(E_BEGINFRAME,URHO3D_HANDLER(MyApp,HandleBeginFrame));
//SubscribeToEvent(E_KEYDOWN,URHO3D_HANDLER(MyApp,HandleKeyDown));
//SubscribeToEvent(E_UIMOUSECLICK,URHO3D_HANDLER(MyApp,HandleControlClicked));
//SubscribeToEvent(E_UPDATE,URHO3D_HANDLER(MyApp,HandleUpdate));
//SubscribeToEvent(E_POSTUPDATE,URHO3D_HANDLER(MyApp,HandlePostUpdate));
//SubscribeToEvent(E_RENDERUPDATE,URHO3D_HANDLER(MyApp,HandleRenderUpdate));
//SubscribeToEvent(E_POSTRENDERUPDATE,URHO3D_HANDLER(MyApp,HandlePostRenderUpdate));
//SubscribeToEvent(E_ENDFRAME,URHO3D_HANDLER(MyApp,HandleEndFrame));

        SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(projet, HandleKeyDown));
    }
    virtual void Stop()
    {

    }

    void HandleKeyDown(StringHash eventType, VariantMap& eventData)
    {
        using namespace KeyDown;
        // Check for pressing ESC. Note the engine_ member variable for convenience access to the Engine object
        int key = eventData[P_KEY].GetInt();
        if (key == KEY_ESC)
            engine_->Exit();
    }
};
URHO3D_DEFINE_APPLICATION_MAIN(projet)[/code]

it compile fine but my application just show  a black screen.

here is the log :
[code][Thu Feb 25 09:26:39 2016] INFO: Opened log file Urho3D.log
[Thu Feb 25 09:26:39 2016] INFO: Created 3 worker threads
[Thu Feb 25 09:26:39 2016] INFO: Added resource path /home/noname/Bureau/projet_build/bin/Data/
[Thu Feb 25 09:26:39 2016] INFO: Added resource path /home/noname/Bureau/projet_build/bin/CoreData/
[Thu Feb 25 09:26:39 2016] DEBUG: Skipped autoload path 'Autoload' as it does not exist, check the documentation on how to set the 'resource prefix path'
[Thu Feb 25 09:26:39 2016] INFO: Set screen mode 1280x720 windowed resizable
[Thu Feb 25 09:26:40 2016] INFO: Initialized input
[Thu Feb 25 09:26:40 2016] INFO: Initialized user interface
[Thu Feb 25 09:26:40 2016] DEBUG: Loading resource Textures/Ramp.png
[Thu Feb 25 09:26:40 2016] DEBUG: Loading temporary resource Textures/Ramp.xml
[Thu Feb 25 09:26:40 2016] DEBUG: Loading resource Textures/Spot.png
[Thu Feb 25 09:26:40 2016] DEBUG: Loading temporary resource Textures/Spot.xml
[Thu Feb 25 09:26:40 2016] DEBUG: Loading resource Techniques/NoTexture.xml
[Thu Feb 25 09:26:40 2016] DEBUG: Loading resource RenderPaths/Forward.xml
[Thu Feb 25 09:26:40 2016] INFO: Initialized renderer
[Thu Feb 25 09:26:40 2016] INFO: Set audio mode 44100 Hz stereo interpolated
[Thu Feb 25 09:26:40 2016] DEBUG: Loading resource UI/MessageBox.xml
[Thu Feb 25 09:26:40 2016] DEBUG: Loading UI layout UI/MessageBox.xml
[Thu Feb 25 09:26:40 2016] INFO: Initialized engine
[Thu Feb 25 09:26:40 2016] DEBUG: Loading resource Models/cor5x20x1/cor5x20x1.mdl
[Thu Feb 25 09:26:40 2016] DEBUG: Loading resource Models/cor5x20x1/cor_5x20x1.xml
[Thu Feb 25 09:26:40 2016] DEBUG: Loading resource Techniques/Diff.xml
[Thu Feb 25 09:26:40 2016] DEBUG: Loading resource Models/cor5x20x1/cor5x20x1_texture.png
[Thu Feb 25 09:26:40 2016] DEBUG: Reloading shaders
[Thu Feb 25 09:26:40 2016] DEBUG: Loading resource Shaders/GLSL/LitSolid.glsl
[Thu Feb 25 09:26:40 2016] DEBUG: Compiled vertex shader LitSolid(PERPIXEL POINTLIGHT)
[Thu Feb 25 09:26:40 2016] DEBUG: Compiled pixel shader LitSolid(AMBIENT DIFFMAP PERPIXEL POINTLIGHT SPECULAR)
[Thu Feb 25 09:26:40 2016] DEBUG: Linked vertex shader LitSolid(PERPIXEL POINTLIGHT) and pixel shader LitSolid(AMBIENT DIFFMAP PERPIXEL POINTLIGHT SPECULAR)
[Thu Feb 25 09:26:40 2016] DEBUG: Compiled pixel shader LitSolid(DIFFMAP PERPIXEL POINTLIGHT SPECULAR)
[Thu Feb 25 09:26:40 2016] DEBUG: Linked vertex shader LitSolid(PERPIXEL POINTLIGHT) and pixel shader LitSolid(DIFFMAP PERPIXEL POINTLIGHT SPECULAR)[/code]


am i loading my model correctly in the main.cpp ?
maybe the camera don't look in the right direction or the lights aren't set properly or did i forgot something ? i can't tell.

thx

-------------------------

1vanK | 2017-01-02 01:10:22 UTC | #2

Camera inside box?

try
[code]cameraNode_->SetWorldPosition(Vectro3(5, 5, 5));
cameraNode_->LookAt(boxNode_->GetWorldPosition());[/code]

-------------------------

hdunderscore | 2017-01-02 01:10:22 UTC | #3

Welcome !

First guess: You didn't set the camera position.

Since you are new I will point out there is a scene editor you can use (when you build Urho3DPlayer, run 'Editor.sh') which will help you quickly figure out things like whether your model actually loads in Urho or not. Plus you can then save and load scene files instead of hard coding them.

-------------------------

noals | 2017-01-02 01:10:22 UTC | #4

[quote="1vanK"]Camera inside box?

try
[code]cameraNode_->SetWorldPosition(Vectro3(5, 5, 5));
cameraNode_->LookAt(boxNode_->GetWorldPosition());[/code][/quote]

it works but it doesn't seem my model is well loaded, it shows a cube, the texture is applied on it through.

[quote="hd_"]Welcome !

First guess: You didn't set the camera position.

Since you are new I will point out there is a scene editor you can use (when you build Urho3DPlayer, run 'Editor.sh') which will help you quickly figure out things like whether your model actually loads in Urho or not. Plus you can then save and load scene files instead of hard coding them.[/quote]

this is what the editor tell me when i try to import my model to it :
[code]ERROR: Failed to execute AssetImporter to import model[/code]
AssetImporter is compiled as well in the tool directory so i don't know, maybe i didn't exported the model well.
i used the same options as on the tutorial screen shot. (i just didn't copied the texture...)
[urho3d.wikia.com/wiki/Blender_to_Urho3D_Guide](http://urho3d.wikia.com/wiki/Blender_to_Urho3D_Guide)

edit:  i exported my model from blender using windows 7 and then i compiled my program using ubuntu. it don't think it should be a problem, it's still a .mdl file, but i say it just in case.

-------------------------

rasteron | 2017-01-02 01:10:23 UTC | #5

You only need to export once, it's either using AssetImporter or Blender Exporter. If you're using the AssetImporter, try converting it via command line so you can toggle necessary options to export them properly (ie. tangents, material list, etc..)

-------------------------

Modanung | 2017-01-02 01:10:24 UTC | #6

[quote="noals"]it works but it doesn't seem my model is well loaded, it shows a cube, the texture is applied on it through.[/quote]
Since you are loading the correct model I'm guessing you may have scaled a default cube in Blender in the Object Mode. If this is the case [i]either[/i] redo the scaling in Edit Mode [i]or[/i] apply the scale by selecting the object in Object Mode and hitting [b]Ctrl+A, S[/b]. With the latter solution you should see the Scale parameters change in the [b]N[/b] menu of the 3D View.

-------------------------

noals | 2017-01-02 01:10:25 UTC | #7

[quote="Modanung"]Since you are loading the correct model I'm guessing you may have scaled a default cube in Blender in the Object Mode. If this is the case [i]either[/i] redo the scaling in Edit Mode [i]or[/i] apply the scale by selecting the object in Object Mode and hit [b]Ctrl+A, S[/b] to apply its scaling. With the latter solution you should see the Scale parameters change in the [b]N[/b] menu of the 3D View.[/quote]
my model is ok, i did more complex things with blender in the past so i don't think i did something wrong. i can't tell where the problem come from. here a screenshot
[i64.tinypic.com/x7nrs.png](http://i64.tinypic.com/x7nrs.png)
i just build simple stuffs like that, i'm interested in procedural 3D dungeon generation actually so it's just about making some simple parts for the dungeon but i guess i will ask more about it later on the forum if needed.

[quote="rasteron"]You only need to export once, it's either using AssetImporter or Blender Exporter. If you're using the AssetImporter, try converting it via command line so you can toggle necessary options to export them properly (ie. tangents, material list, etc..)[/quote]
i didn't know i was able to import the model directly from the .blend file in the editor. the model show fine with it but it doesn't seem i can export the model in .mdl from the editor anyway.
i wasn't able to use the assetImporter, i tryed a little script to make it easier for me : (link to the doc : [urho3d.github.io/documentation/1.5/_tools.html](http://urho3d.github.io/documentation/1.5/_tools.html))
[code]/home/noname/Documents/urho3D_build/bin/tool/AssetImporter /home/noname/Bureau/blend/cor5x20x1.blend /home/noname/Bureau/blend_export/cor5x20x1.mdl -l[/code]
but i'm still unfamiliar with ubuntu so maybe i make a mistake in the script, it doesn't work and say "[b]unrecognized command /home/noname/Bureau/blend/cor5x20x1.blend[/b]"

i will retry the blender exporter plugin under linux, i re-saved my blend on blender 2.76 on linux, i'm about to add the plugin.

-------------------------

noals | 2017-01-02 01:10:25 UTC | #8

well, same result. it just show a textured cube. i don't understand what i do wrong.
[i63.tinypic.com/25fiomo.png](http://i63.tinypic.com/25fiomo.png)

-------------------------

Modanung | 2017-01-02 01:10:25 UTC | #9

[quote="noals"]well, same result. it just show a textured cube. i don't understand what i do wrong.[/quote]
Would you mind sharing the Blend file?

-------------------------

noals | 2017-01-02 01:10:25 UTC | #10

the .blend file : [s000.tinyupload.com/index.php?fi ... 8315073504](http://s000.tinyupload.com/index.php?file_id=00088359488315073504)
and the texture you will surely have to reassign : [s000.tinyupload.com/index.php?fi ... 9746748319](http://s000.tinyupload.com/index.php?file_id=94110352619746748319)

edit: thinking about it, it's maybe because i didn't merged all vertex. i collapsed some to help me with the uv map unwrapping. could it be it ? i will check that later, thx for help anyway.

-------------------------

Modanung | 2017-01-02 01:10:26 UTC | #11

I'm quite convinced now following the instruction I provided earlier will solve this problem.
Scroll up in the right panel of the 3D view to see the Scale being set to (5, 20, 1), [b]Ctrl+A, S[/b] will apply this scale. To [i]clear[/i] the scaling instead of applying it hit [b]Alt+S[/b], this reveals how the exporter handles the object and will in your case turn the slab back into a cube.
Regards

-------------------------

noals | 2017-01-02 01:10:26 UTC | #12

[quote="Modanung"]I'm quite convinced now following the instruction I provided earlier will solve this problem.
Scroll up in the right panel of the 3D view to see the Scale being set to (5, 20, 1), [b]Ctrl+A, S[/b] will apply this scale. To [i]clear[/i] the scaling instead of applying it hit [b]Alt+S[/b], this reveals how the exporter handles the object and will in your case turn the slab back into a cube.
Regards[/quote]

yes you were right, i'm sorry, i guess i didn't pay attention enough, thx to point it out again. when i first tryed to follow your advice, i entered the mode to scale manually with the mouse so at this point i was wondering why you wanted me to scale my model. ^^; i didn't know the dimension you put when you create the object was just scaling, usually i follow some tutos so thats the first time it happen to me lol.

thx again anyway, i just tested it, it solve my problem as you though. i'm glad i can continue.

-------------------------

Modanung | 2017-01-02 01:10:26 UTC | #13

[quote="noals"]thx again anyway, i just tested it, it solve my problem as you though. i'm glad i can continue.[/quote]
You're welcome, I'm glad I could help out.

[quote="noals"]i didn't know the dimension you put when you create the object was just scaling[/quote]
It isn't. When creating a cube, the only size parameter you can enter is its radius, which does not affect the scale. The scaling must have happened through a separate operation.
Again, this would not have caused any trouble had this happened in Edit Mode (easily toggled with [b]Tab[/b]).

-------------------------

noals | 2017-01-02 01:10:26 UTC | #14

i was puting the values in the N menu. i don't use much shortcuts usually, just the shift + S for the cursor.
the model was so simple i didn't even though about the edit mode lol.

my next step is making more simple models like that, add bones where i want those models to connect so i should be able to get the "connector" positions with urho3D.

-------------------------

Modanung | 2017-01-02 01:10:26 UTC | #15

Learning the [url=http://www.luckeyproductions.nl/blenderhotkeys.html]hotkeys[/url] as you go does greatly improve your workflow.

-------------------------

noals | 2017-01-02 01:10:27 UTC | #16

thx for the list.

-------------------------

Modanung | 2017-01-02 01:10:27 UTC | #17

[quote="noals"]i was puting the values in the N menu.[/quote]
Apparently that's called the Properties Panel. Not to be confused with the Properties Editor. :unamused:
The panel on the [i]left[/i] is called the Object Tools panel. The visibility of this panel is toggled with [b]T[/b]. The bottom of this panel shows options for the last operation, like the radius when adding a cube or the number of cuts for subdivisions. Note that this part may be rolled up.

-------------------------

