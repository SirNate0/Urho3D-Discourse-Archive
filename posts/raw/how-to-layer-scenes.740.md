practicing01 | 2017-01-02 01:02:35 UTC | #1

Hello, I've got two scenes with a camera in each (1 ortho 1 perspective).  I'd like to have the scene with the ortho camera on top of the scene with the perspective camera (like if they were 2d layers).  Is this possible?  If so how would I go about doing this?  Thanks for your time.

-------------------------

cadaver | 2017-01-02 01:02:35 UTC | #2

This question is similar to [topic753.html](http://discourse.urho3d.io/t/render-3d-model-in-orthographic-mode/737/1). Make 2 viewports (check the MultipleViewports sample) that have the same screen region, point each to the respective scene and camera, then use a different renderpath for the "on-top" scene, where you omit the "clear" command. If you get trouble with Z-buffering, then you can make the second renderpath clear depth but not color.

-------------------------

practicing01 | 2017-01-02 01:02:35 UTC | #3

I've made two viewports/cams/scenes but I'm not seeing both scenes, just whichever is viewport 0.  Did I do something wrong with the renderpath stuff?
[code]
SpaceSimulationMenuSelect::SpaceSimulationMenuSelect(Context* context, Urho3DPlayer* main) :
    Object(context)
{
	main_ = main;
	elapsedTime_ = 0.0f;

	main_->cameraNode_->RemoveAllChildren();
	main_->cameraNode_->RemoveAllComponents();
	main_->cameraNode_->Remove();

	scene_ = new Scene(main_->GetContext());
	cameraNode_ = new Node(main_->GetContext());

	Renderer* renderer = GetSubsystem<Renderer>();
	ResourceCache* cache = GetSubsystem<ResourceCache>();

	renderer->SetNumViewports(2);

	File loadFile(context_,
			GetSubsystem<FileSystem>()->GetProgramDir()
			+ "Data/Scenes/MSNMenu.xml", FILE_READ);
	main_->scene_->LoadXML(loadFile);

	main_->cameraNode_ = main_->scene_->GetChild("camera");
	main_->viewport_->SetCamera(main_->cameraNode_->GetComponent<Camera>());

	renderer->SetViewport(0, main_->viewport_);

	File loadFile2(context_,
			GetSubsystem<FileSystem>()->GetProgramDir()
			+ "Data/Scenes/spaceSimulationMenu.xml", FILE_READ);
	scene_->LoadXML(loadFile2);

	cameraNode_ = scene_->GetChild("camera");

	SharedPtr<RenderPath> colorUnclearRenderPath = SharedPtr<RenderPath> (new RenderPath());
	colorUnclearRenderPath->Load(cache->GetResource<XMLFile>("RenderPaths/BackgroundLayer.xml"));
	viewport_ = new Viewport(main_->GetContext(), scene_, cameraNode_->GetComponent<Camera>());
	viewport_->SetCamera(cameraNode_->GetComponent<Camera>());
	viewport_->SetRenderPath(colorUnclearRenderPath);
	renderer->SetViewport(1, viewport_);

	SubscribeToEvent(E_UPDATE, HANDLER(SpaceSimulationMenuSelect, HandleUpdate));
}
[/code]
[code]
<renderpath>
    <command type="clear" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>
[/code]

-------------------------

codingmonkey | 2017-01-02 01:02:35 UTC | #4

there is my trying to make sceneB( mushrooms + light+ ortho camera) as overlay on sceneA (ground and boxes+ light+ camera).
and seems it works correctly
[url=http://savepic.ru/6604446.htm][img]http://savepic.ru/6604446m.png[/img][/url]


the first of all you need copy RenderPath/Forward.xml named it like as RenderPath/ForwardTest.xml  and delete first commad with clear command.
[code]
<renderpath>
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>
[/code]


then make two scenes, with cameras and some objects.
in sceneA you have usual perspective camera, 3d world...
in sceneB you must setup camera as ortho and adjust scale, locate some objects before view of camera they will be render as images, add some light
save this two scenes.

this my code for setup example:
[code]
#include "common.h"
#include "main.h"

DEFINE_APPLICATION_MAIN(MyApp);

MyApp::MyApp(Context* context) : Application(context)
{
		engineParameters_["WindowTitle"] = GetTypeName();
		engineParameters_["FullScreen"] = false;
		engineParameters_["Headless"] = false;
		engineParameters_["WindowWidth"] = 1280;
		engineParameters_["WindowHeight"] = 720;
		engineParameters_["LogName"] = GetSubsystem<FileSystem>()->GetAppPreferencesDir("urho3d", "logs") + GetTypeName() + ".log";
		engineParameters_["RenderPath"] = "Bin\CoreData\RenderPaths\Forward.xml";
}

void MyApp::Setup()
{
        // Called before engine initialization. engineParameters_ member variable can be modified here
}

void MyApp::Start()
{
	Graphics* graphics = GetSubsystem<Graphics>();
	Renderer* renderer = GetSubsystem<Renderer>();
	ResourceCache* cache = GetSubsystem<ResourceCache>();
    // Called after engine initialization. Setup application & subscribe to events here
    SubscribeToEvent(E_KEYDOWN, HANDLER(MyApp, HandleKeyDown));
	
	scene1 = SharedPtr<Scene>(new Scene(context_));
	File sceneFile(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Scenes/SceneA.xml", FILE_READ);
	scene1->LoadXML(sceneFile);
	
	scene2 = SharedPtr<Scene>(new Scene(context_));
	File sceneFile2(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Scenes/SceneB.xml", FILE_READ);
	scene2->LoadXML(sceneFile2);

	camera1Node = scene1->GetChild("cameraNode", true);
	camera2Node = scene2->GetChild("cameraNode", true);

	camera1 = camera1Node->GetComponent<Camera>();
	camera2 = camera2Node->GetComponent<Camera>();

	viewport1 = new Viewport(context_, scene1, camera1);
	viewport2 = new Viewport(context_, scene2, camera2);


	overlayRenderPath = SharedPtr<RenderPath>(new RenderPath());
	overlayRenderPath->Load(cache->GetResource<XMLFile>("RenderPaths/ForwardTest.xml"));
	viewport2->SetRenderPath(overlayRenderPath);


	renderer->SetNumViewports(2);
	renderer->SetViewport(0, viewport1);
	renderer->SetViewport(1, viewport2);	
}

void MyApp::Stop()
{
        // Perform optional cleanup after main loop has terminated
}
    
void MyApp::HandleKeyDown(StringHash eventType, VariantMap& eventData)
{
        using namespace KeyDown;

        // Check for pressing ESC. Note the engine_ member variable for convenience access to the Engine object
        int key = eventData[P_KEY].GetInt();
        if (key == KEY_ESC)
            engine_->Exit();
}
[/code]

-------------------------

practicing01 | 2017-01-02 01:02:36 UTC | #5

Thanks, deleting the entire clear command line worked.  Just incase though, when cadaver  said "If you get trouble with Z-buffering, then you can make the second renderpath clear depth but not color.", how would I go about doing that?

-------------------------

codingmonkey | 2017-01-02 01:02:36 UTC | #6

i guess like that
<command type="clear" color="fog" depth="1.0" stencil="0" />
you just preserve in clear command only depth & stencil clearning
<command type="clear" depth="1.0" stencil="0" />

-------------------------

practicing01 | 2017-01-02 01:02:36 UTC | #7

If it's supposed to be like that then it's bugged cus it didn't work.  No worries though, for this project what worked is enough, perhaps in the future I'll revisit the problem.  Thanks for the help.

-------------------------

cadaver | 2017-01-02 01:02:36 UTC | #8

When I do <command type="clear" depth="1.0" stencil="0" /> in Forward.xml renderpath I observe the background not getting cleared (ghost effect), so it should work. Not sure if it can fail in a more complex case though. You could examine the clearing RenderPathCommand in code and make sure its clearFlags_ don't have CLEAR_COLOR bit set.

-------------------------

Enhex | 2017-01-02 01:10:37 UTC | #9

How can it be achieved with deferred rendering? Disabling color clear just results in a black background.

It does work with forward.

Also I noticed that having Bloom effects adds a black tint where it should be transparent.

-------------------------

dakilla | 2017-01-02 01:11:09 UTC | #10

Hi

I'm trying to achieve the same thing, it works using previous example, but how deal blending (add, substract, mul, etc...) or add transparency between viewports ?

thanks

-------------------------

codingmonkey | 2017-01-02 01:11:09 UTC | #11

I suppose in your case you don't need set second viewport to renderer instead this you probably need add second(overlay RT) to cache.AddManualResource() to allow use it in RenderPath. 
Then you add quad command with lines like this:
[code]    <command type="quad" vs="YourCustomShaderOrJustCopyBufferShader" ps="YourCustomShaderOrJustCopyBufferShader" blend="add/substract/alpha" output="viewport">
        <texture unit="diffuse" name="camera2RT" /> // same name that put into cache.AddManualResource() 
    </command> [/code]

and doing blending overlay scene with main scene. May be you also need create custom shader for quad command to discard pixels by some reason to avoid blending in empty areas of overlay RT or by some another mask RT(or free color channel in already existing RTs).

-------------------------

dakilla | 2017-01-02 01:11:12 UTC | #12

Thanks, It works as you said.

[code]
SharedPtr<Texture2D> renderTexture(new Texture2D(context_));
renderTexture->SetSize(graphics->GetWidth(), graphics->GetHeight(), Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
renderTexture->SetFilterMode(Urho3D::FILTER_DEFAULT);
renderTexture->SetName("myrt");
cache->AddManualResource(renderTexture);    

SharedPtr<RenderSurface> surface(renderTexture->GetRenderSurface());
SharedPtr<Viewport> rttViewport(new Viewport(context_, scene2, camera2));
surface->SetViewport(0, rttViewport);
surface->SetUpdateMode(SURFACE_UPDATEALWAYS);
[/code]

and renderpath :

[code]
<command type="quad" vs="CopyFramebufferFlipped" ps="CopyFramebufferFlipped" blend="add" output="viewport">
  <texture unit="diffuse" name="myrt" />
</command>[/code]

I used CopyFramebuffer shader but I had to flip uv vertically (opengl).

-------------------------

codingmonkey | 2017-01-02 01:11:13 UTC | #13

>I used CopyFramebuffer shader but I had to flip uv vertically (opengl).
You need flip TexCoords in case using of gl renderer in shader with help something like this: 
[code]vScreenPos = vec2 ( vScreenPos.x, 1 - vScreenPos.y )[/code]

-------------------------

1vanK | 2017-01-02 01:11:13 UTC | #14

[quote="dakilla"]
I used CopyFramebuffer shader but I had to flip uv vertically (opengl).[/quote]

[urho3d.github.io/documentation/H ... ences.html](http://urho3d.github.io/documentation/HEAD/_a_p_i_differences.html)

[quote]To ensure similar UV addressing for render-to-texture viewports on both APIs, on OpenGL texture viewports will be rendered upside down.[/quote]

-------------------------

dakilla | 2017-01-02 01:12:41 UTC | #15

Hi

I 'm still not comfortable with renderpath, I would like an advice, please.
I'm trying to use a custom blending shader for layering scenes (rendered each in rendertargets) but result is not as I expected.

I thought to use the 'mixed' rendertarget as blend cascaded result  (output for the 2 first quads) and to use it also as an input in the second quad (in the first quad it will be empty).
The final quad, is for copying final 'mixed' to the viewport.

MergingShader just do some math operations using samplers 0 & 1 (texture unit 0 and 1).

But sampler 0 (texture unit="0" name="mixed) always seems to return a black color, why ??

My renderpath  :

[code]<renderpath>
    
   <rendertarget name="mixed" sizedivisor="1 1" format="rgba" /> 

    <command type="quad" tag="mytag" vs="MergingShader" ps="MergingShader" blend="replace" output="mixed">
        <texture unit="0" name="mixed" />
        <texture unit="1" name="rt1" />
        <parameter name="BlendRatio" value="0 0.5" />"
        <parameter name="ClearColor" value="0 0 0 1" />"
        <parameter name="MergeMode" value="5" />"
        <parameter name="FlipUV" value="true" />"
    </command>
  
    <command type="quad" tag="mytag" vs="MergingShader" ps="MergingShader" blend="replace" output="mixed">
        <texture unit="0" name="mixed" />
        <texture unit="1" name="rt2" />
        <parameter name="BlendRatio" value="0.5 0.5" />"
        <parameter name="ClearColor" value="0 0 0 1" />"
        <parameter name="MergeMode" value="0" />"
        <parameter name="FlipUV" value="true" />"
    </command> 
	
   <command type="quad" tag="mytag" vs="CopyFramebuffer" ps="CopyFramebuffer" blend="replace" output="viewport">
        <texture unit="0" name="mixed" />
    </command>	

</renderpath>[/code]


Note : In this example I only have two senes, but in real case it is generated programmaticcally and I can have up to 16 scenes or more (why I blend  cascaded result in mixed instead of using a single quad with multiple texture units)

thanks

-------------------------

cadaver | 2017-01-02 01:12:41 UTC | #16

You cannot sample and render to an RT at the same time. 

There's a difference of handling the final destination rendertarget "viewport" and named texture rendertargets you have created yourself. The viewport RT will be pingponged automatically by creating an extra texture, since it's so common and often needed by postprocess effects chains. But for your named RT's the engine won't guess how you want this handled. Rather you will have to manage the pingponging (if any is needed) manually by e.g. creating a "mixed2" RT and ensuring you never sample and render the same RT simultaneously.

-------------------------

dakilla | 2017-01-02 01:12:41 UTC | #17

Ok I see. 
It works using a mixed2 RT and switching alternately.
Thanks :wink:

-------------------------

OMID-313 | 2017-02-12 12:19:43 UTC | #18

Thanks @codingmonkey for this helpful post.

Would you please help converting this code to actionscript code?
Because I'm using Urho on Raspberry Pi.

Thanks for your time and help.

-------------------------

