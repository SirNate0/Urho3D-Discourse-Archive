dvan | 2017-01-02 01:10:07 UTC | #1

Hopefully it's just me, but their seems to be a delay in the sound system. Anyone else seen this?

I've got a simple 2D app with a bouncing ball (tweak of # 27 sample). When it hit's the floor it should beep. What I'm seeing is it bouncing about 1/4+- up the screen till the sound is made (more noticed on the first bounce). I've tried a few different ways to make sound, preloading, .wav vs .ogg, etc., and nothing seems to mater much.

Played with sample #29 a bit via taking setting down to the bottom 0.01, and then when the tone starts to move hit the up key. The delay seems to be evident to me there also.

Seemed to be evident in a 3D example I tried also, but it's harder to tell there (imaging is more distracting).

All these tests are somewhat subjective so would like any feedback. I've tried a few different environments and it seems to be evident in all of them (Android being the worse).

 I'm stuck at this point.

-------------------------

cadaver | 2017-01-02 01:10:07 UTC | #2

You could try to control the engine's startup parameters for smaller sound buffer size. On the default setting it's on purpose conservatively large to avoid glitches / dropouts. However it may not help all the way - in this regard Urho is at the mercy of SDL, which in turn is at the mercy of the operating system. Android especially is notorious with its audio latency.

-------------------------

weitjong | 2017-01-02 01:10:08 UTC | #3

You may also want to find our more about recent audio API improvement in SDL 2.0.4. I have quoted relevant bullet points from WhatsNew.txt below

[quote]* Added an API to queue audio instead of using the audio callback: SDL_QueueAudio(), SDL_GetQueuedAudioSize(), SDL_ClearQueuedAudio()
* Added events for audio device hot plug support: SDL_AUDIODEVICEADDED, SDL_AUDIODEVICEREMOVED[/quote]
The SDL-2.0.4-upgrade branch should be merged into master branch shortly. Having said that, Urho3D game engine has not taken advantage of this new API yet. So, you will have to experiment with it yourself and if it works then probably you can submit your changes back as PR. Probably we should have audio mode enumeration declaration to support both callback and queue audio.

-------------------------

cadaver | 2017-01-02 01:10:08 UTC | #4

If I understand right how it works like, the queue audio mode can have its own drawbacks; I remember the original Quake working in such manner (instead of IRQ driven playback), and it would get dropouts or audio buffer repeats when the FPS was low.

-------------------------

weitjong | 2017-01-02 01:10:08 UTC | #5

I have not experiment with the new queue API myself but from the SDL wiki: [wiki.libsdl.org/SDL_QueueAudio](https://wiki.libsdl.org/SDL_QueueAudio) then I reckon when the audio buffer is under-run then it will just play silence. I think there is nothing we could do about it in such cases.

-------------------------

cadaver | 2017-01-02 01:10:08 UTC | #6

Yeah, I believe it would be fine as an option. There would be quite minimal changes to Audio; in queue mode it would listen to a per-frame event and push a suitable amount of audio each frame from the main thread. This is btw. safer since there are no potential threading issues like with the audio callback.

-------------------------

dvan | 2017-01-02 01:10:09 UTC | #7

Thanks for giving this some consideration. Looks like there may be some improvement to be had with 2.0.4. Doesn?t sound like a quick fix though (especially for me).

Thanks!

-------------------------

George | 2017-01-02 01:10:13 UTC | #8

I played with sound recently. I think it works just right.

How big is your music file?

Do you use Audacity? Try to remove any delay at the beginning of the music file. 

Regards

-------------------------

dvan | 2017-01-02 01:10:14 UTC | #9

George, you must have a really fast machine!   I decided to run some further tests with a somewhat stripped version of the code I've been playing with and it is still apparent to me.

Interestingly, I created a quick bouncy ball app using Unity on a Virtual Machine to compare (amplifies issues like this) and the issue was Not there with Unity. The differences between Unity and Urho3D in this regard is black/white apparent to me on the VM (more subjective on my i7 main environment).

Here's the code I've used, should anyone want to look at it. I'd be happy to find out I was doing something stupid here!

[code]// CyBall.h

//#define ANDROID_TEST true  //screen diffs. Android fonts display about 1/2 size also, so may need to 2x those.

#ifndef __CYBALL_H_
#define __CYBALL_H_


#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/IO/Log.h>

#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Scene/SceneEvents.h>
#include <Urho3D/Graphics/Octree.h>
#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/RenderPath.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Graphics/DebugRenderer.h>
#include <Urho3D/Core/Timer.h>	//for randomizer

#include <Urho3D/Core/CoreEvents.h>	//E_UPDATE
#include <Urho3D/Graphics/GraphicsEvents.h>	//E_SCREENMODE

#include <Urho3D/Urho2D/CollisionBox2D.h>
#include <Urho3D/Urho2D/CollisionCircle2D.h>
#include <Urho3D/Urho2D/Drawable2D.h>
#include <Urho3D/Urho2D/PhysicsWorld2D.h>
#include <Urho3D/Urho2D/RigidBody2D.h>
#include <Urho3D/Urho2D/Sprite2D.h>
#include <Urho3D/Urho2D/StaticSprite2D.h>

#include <Urho3D/Audio/Sound.h>
#include <Urho3D/Audio/SoundSource3D.h>

#include <Urho3D/Urho2D/PhysicsEvents2D.h>

#include <Urho3D/Physics/CollisionShape.h>
#include <Urho3D/Physics/PhysicsWorld.h>
#include <Urho3D/Physics/RigidBody.h>
#include <Urho3D/Physics/Constraint.h>


using namespace Urho3D;


class CyBall : public Application
{

    URHO3D_OBJECT(CyBall,Application);


public:
    CyBall(Context* context);

    virtual void Setup();
    virtual void Start();
    virtual void Stop();

    Graphics* graphics;
	ResourceCache* cache;
	
	bool drawDebug_;	//testing render

	float r_width_, p_width_; //rendering / display(game screen pix) window size as floats
    float r_height_, p_height_;
	float x_scale_, y_scale_, s_scale_;	//x, y, and min(x,y) ratio scale for position and resonable size's
	float pad_psizeH2_;		//1/2 paddle in pix after scaled

	// min/max movment of paddel on screen, in pix
	float pad_VposMax_;
	float pad_VposMin_;

	float pad_Hsizefactor_;	//make it wider (todo: through UI)

    SharedPtr<Scene> scene_;
    Node* cameraNode_;
	Camera* camera_;

	// play area frame sprites
	Node* BottomFrame_;
	Node* TopFrame_;
	Node* LeftFrame_;
	Node* RightFrame_;

	Node* paddle_;
	Node* ball_;

	//global sounds
	Node* sound_hit_Node_;
	SoundSource* sound_source_;
	SharedPtr<Sound> sound_;


	void HandleKeyDown(StringHash eventType,VariantMap& eventData);
	void HandleUpdate(StringHash eventType,VariantMap& eventData);
	void HandleScreenMode(StringHash eventType, VariantMap& eventData);
	void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData);
	void HandleCollision(StringHash eventType, VariantMap& eventData);

	void PlayMySound(String soundFileName);

private:
	float PAD_PSIZEV;
	float PAD_PSIZEH;
	float PAD_PSIZEH2;

    void CreateScene();
    void SetupViewport();
	void ScaleScreen();
	void DropTarget();

};


#endif // #ifndef __CYBALL_H_[/code]

[code]#include "CyBall.h"


using namespace Urho3D;

CyBall :: CyBall(Context* context) : Application(context)
{	//full application global stuff

}


void CyBall::Setup()
{	// Called before engine initialization. engineParameters_ member variable can be modified here
	drawDebug_ = false;

	engineParameters_["WindowTitle"] = "SoundDelay";
	engineParameters_["FullScreen"] = false;

	engineParameters_["WindowWidth"] = 900;
	engineParameters_["WindowHeight"] = 720;
	engineParameters_["WindowResizable"] = true;
	engineParameters_["PauseMinimized"] = true;

	engineParameters_["MaxFps"] = 60;

	//inital set some things as origonal constants..
	PAD_PSIZEV = 0.16f;	//real(or expected) size of sprite - Vertical;
	PAD_PSIZEH = 0.32f;	//real(or expected) size of sprite - Horz.;
	PAD_PSIZEH2 = 0.16f;	//1/2 real(or expected) size of sprite - Horz.;

	//set some things to test for..
	scene_ = NULL;
	ball_ = NULL;

	//init setups
	pad_Hsizefactor_ = 2;

}


void CyBall::Start()
{

	cache = GetSubsystem<ResourceCache>();
	graphics = GetSubsystem<Graphics>();


	//get rendering window size as floats
	r_width_ = (float)graphics->GetWidth();
	r_height_ = (float)graphics->GetHeight();
	p_width_ = r_width_ * PIXEL_SIZE;
	p_height_ = r_height_ * PIXEL_SIZE;

	// Called after engine initialization. Setup application & subscribe to events here
	SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(CyBall, HandleKeyDown));
    SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(CyBall, HandleUpdate));

    SubscribeToEvent(E_SCREENMODE, URHO3D_HANDLER(CyBall, HandleScreenMode));
	SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(CyBall, HandlePostRenderUpdate));	//debug geometry

	SubscribeToEvent(E_PHYSICSBEGINCONTACT2D, URHO3D_HANDLER(CyBall, HandleCollision));

	GetSubsystem<Input>()->SetMouseVisible(false);
	GetSubsystem<Input>()->SetMouseGrabbed(true);

    CreateScene();
    SetupViewport();
	DropTarget();
}


void CyBall::Stop()
{
	// Perform optional cleanup after main loop has terminated
}

void CyBall::HandleCollision(StringHash eventType, VariantMap& eventData)
{
	PlayMySound("Ding1.wav");
}

/* Just Sprints in 2D */
void CyBall::HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
	// If draw debug mode is enabled, draw viewport debug geometry. This time use depth test, as otherwise the result becomes
	// hard to interpret due to large object count
	if (drawDebug_) {
		PhysicsWorld2D* physicsWorld = scene_->GetComponent<PhysicsWorld2D>();
		physicsWorld->DrawDebugGeometry();
	}
}


void CyBall::HandleKeyDown(StringHash eventType, VariantMap& eventData)
{
	using namespace KeyDown;
	// Check for pressing ESC. Note the engine_ member variable for convenience access to the Engine object
	int key = eventData[P_KEY].GetInt();

	// Toggle debug geometry with space
	if (key == (KEY_SPACE))
		drawDebug_ = !drawDebug_;

    else if (key == KEY_TAB)
	//else if (key == KEY_ESC)
	{
        GetSubsystem<Input>()->SetMouseVisible(!GetSubsystem<Input>()->IsMouseVisible());
        GetSubsystem<Input>()->SetMouseGrabbed(!GetSubsystem<Input>()->IsMouseGrabbed());
		PlayMySound("Ding1.wav");
	}
    else if (key == KEY_ESC)
		engine_->Exit();
	else if (key == KEY_P)
		scene_->SetUpdateEnabled(!scene_->IsUpdateEnabled());

}

//  Hit each frame.
void CyBall::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    float timeStep=eventData[Update::P_TIMESTEP].GetFloat();    //Current frame timestep as seconds.
    // Movement speed as world units per second
    float MOVE_SPEED=10.0f;
    // Mouse sensitivity as degrees per pixel
	float MOUSE_SENSITIVITY = 0.01f;

    // camera movement
    Input* input=GetSubsystem<Input>();

	//need to do these key's here since we need timeStep
	// TO DO: faster while key is held down.
	if (input->GetKeyDown('W'))
	{
		Vector2 oldpostion = paddle_->GetPosition2D();
		oldpostion.y_ += (MOVE_SPEED * timeStep);
		if (oldpostion.y_ > pad_VposMax_) oldpostion.y_ = pad_VposMax_;
		paddle_->SetPosition2D(oldpostion);
	}
	if (input->GetKeyDown('S'))
	{
		Vector2 oldpostion = paddle_->GetPosition2D();
		oldpostion.y_ -= (MOVE_SPEED * timeStep);
		if (oldpostion.y_ < pad_VposMin_) oldpostion.y_ = pad_VposMin_;
		paddle_->SetPosition2D(oldpostion);
	}
	else if(input->GetKeyDown('A'))
	{
		Vector2 oldpostion = paddle_->GetPosition2D();
		oldpostion.x_ -= (MOVE_SPEED * timeStep);
		if (oldpostion.x_ < pad_psizeH2_) oldpostion.x_ = pad_psizeH2_;
		paddle_->SetPosition2D(oldpostion);
	}
	else if (input->GetKeyDown('D'))
	{
		Vector2 oldpostion = paddle_->GetPosition2D();
		oldpostion.x_ += (MOVE_SPEED * timeStep);
		if (oldpostion.x_ > p_width_ - pad_psizeH2_) oldpostion.x_ = p_width_ - pad_psizeH2_;
		paddle_->SetPosition2D(oldpostion);
	}

	// do Mouse stuff...
	if (!GetSubsystem<Input>()->IsMouseVisible())
	{
		IntVector2 mouseMove = input->GetMouseMove() ;

		// handle mouse paddle movment
		if ((mouseMove.x_!= 0 && mouseMove.x_>-2000000000) || (mouseMove.y_ != 0 && mouseMove.y_>-2000000000))
		{
			Vector2 oldpostion = paddle_->GetPosition2D();

			// Horz movement
			oldpostion.x_ += (MOUSE_SENSITIVITY*mouseMove.x_);
			if (oldpostion.x_ < pad_psizeH2_) oldpostion.x_ = pad_psizeH2_;
			if (oldpostion.x_ > p_width_ - pad_psizeH2_) oldpostion.x_ = p_width_ - pad_psizeH2_;

			// Vert Movement
			oldpostion.y_ -= (MOUSE_SENSITIVITY*mouseMove.y_);
			if (oldpostion.y_ < pad_VposMin_) oldpostion.y_ = pad_VposMin_;
			if (oldpostion.y_ > pad_VposMax_) oldpostion.y_ = pad_VposMax_;

			paddle_->SetPosition2D(oldpostion);
		}
	}

}


void CyBall::HandleScreenMode(StringHash eventType, VariantMap& eventData)
{
	//get rendering window size as floats
	float new_r_width_ = (float)graphics->GetWidth();
	float new_r_height_ = (float)graphics->GetHeight();

	if (new_r_width_ != r_width_ || new_r_height_ != r_height_)
	{
		if (new_r_width_ < 300 || new_r_height_ < 300) {
			new_r_width_ = ( new_r_width_ < 300 ? 300 : new_r_width_ );
			new_r_height_ = (new_r_height_ < 300 ? 300 : new_r_height_);
			graphics->SetMode((int)new_r_width_, (int)new_r_height_);
		}

		//screen size changed.
		r_width_ = new_r_width_;
		r_height_ = new_r_height_;

		p_width_ = r_width_ * PIXEL_SIZE;
		p_height_ = r_height_ * PIXEL_SIZE;

		ScaleScreen();
	}
}




void CyBall::ScaleScreen()
{

	cameraNode_->SetPosition(Vector3(p_width_/2, p_height_/2, -10.0f));
	camera_->SetOrthoSize(Vector2(p_width_, p_height_));

	x_scale_ = 1.2f * (r_width_ / 1280.0f);
	y_scale_ = 1.2f * (r_height_ / 800.0f);
	s_scale_ = Min(x_scale_, y_scale_);

	//x_scale_ = y_scale_ = s_scale_ = 1;

	//position these at center, scale outward
	BottomFrame_->SetPosition(Vector3(p_width_/2, 0.0f, 0.0f));
	BottomFrame_->SetScale(Vector3((r_width_/32), 0.24f, 0.0f));

	TopFrame_->SetPosition(Vector3(p_width_ / 2, p_height_ , 0.0f));
	TopFrame_->SetScale(Vector3((r_width_ / 32), 0.24f, 0.0f));

	LeftFrame_->SetPosition(Vector3(0.0f, p_height_ / 2, 0.0f));
	LeftFrame_->SetScale(Vector3(0.24f, (r_height_ / 32) ,  0.0f));

	RightFrame_->SetPosition(Vector3(p_width_, p_height_/2, 0.0f));
	RightFrame_->SetScale(Vector3(0.24f, (r_height_ / 32), 0.0f));

	// Vertical postion limits
	pad_VposMin_ = ((PAD_PSIZEV / 2)  * y_scale_) + 0.05f;	//offset a little above ground
	pad_VposMax_ = ((PAD_PSIZEV / 2)  * y_scale_) + (p_height_ * 0.25f);	//bottom 1/4 of scren

	paddle_->SetPosition(Vector3(p_width_ / 2, pad_VposMin_, 0.0f));
	paddle_->SetScale2D(Vector2(x_scale_ * pad_Hsizefactor_, PAD_PSIZEV * y_scale_));
	pad_psizeH2_ = PAD_PSIZEH2 * x_scale_ * pad_Hsizefactor_;

	if(ball_ != NULL)
		ball_->SetScale2D(s_scale_, s_scale_);

}

void CyBall::DropTarget()
{
	ball_ = scene_->CreateChild("Ball");
	ball_->SetPosition(Vector3((p_width_ / 2), (p_height_ - 0.32f) , 0.0f));

	// Create rigid body
	RigidBody2D* body = ball_->CreateComponent<RigidBody2D>();
	body->SetBodyType(BT_DYNAMIC);
	body->SetLinearDamping(0.0f);
	body->SetAngularDamping(0.0f);

	StaticSprite2D* staticSprite = ball_->CreateComponent<StaticSprite2D>();
	Sprite2D* ballSprite = cache->GetResource<Sprite2D>("Urho2D/Ball.png");
	staticSprite->SetSprite(ballSprite);


	// Create circle collistion shape
	CollisionCircle2D* shape = ball_->CreateComponent<CollisionCircle2D>();
	shape->SetRadius(0.16f);	// Set radius	//1/2 of 32bit sprint
	shape->SetDensity(0.20f);	// Set shape density (kilograms per meter squared) Effects rolling, etc.
	shape->SetFriction(0.5f);	// Set friction.
	shape->SetRestitution(0.990f);	// Set restitution: bounce factor	// <1 smaller = less bounce, >1 additive bounce to infinity

	ball_->SetScale2D(Vector2(s_scale_, s_scale_));

}

void CyBall::CreateScene()
{
    if(scene_ != NULL) {
        return;
    }
    scene_ = new Scene(context_);
    scene_->CreateComponent<Octree>();
	scene_->CreateComponent<PhysicsWorld>();//for debugging
	scene_->CreateComponent<DebugRenderer>();	//for debugging

    // Create camera node
    cameraNode_ = scene_->CreateChild("Camera");
    camera_ = cameraNode_->CreateComponent<Camera>();
    camera_->SetOrthographic(true);

    // Create 2D physics world component
    scene_->CreateComponent<PhysicsWorld2D>();

    Sprite2D* boxSprite = cache->GetResource<Sprite2D>("Urho2D/Box.png");
    Sprite2D* ballSprite = cache->GetResource<Sprite2D>("Urho2D/Ball.png");
	Sprite2D* paddleSprite = cache->GetResource<Sprite2D>("Urho2D/Box.png");

    // Create frame bixground.
	BottomFrame_= scene_->CreateChild("FrameB");
	TopFrame_ = scene_->CreateChild("FrameT");
	LeftFrame_ = scene_->CreateChild("FrameL");
	RightFrame_ = scene_->CreateChild("FrameR");
    // Create 2D rigid body for gound
	BottomFrame_->CreateComponent<RigidBody2D>();
	TopFrame_->CreateComponent<RigidBody2D>();
	LeftFrame_->CreateComponent<RigidBody2D>();
	RightFrame_->CreateComponent<RigidBody2D>();

	StaticSprite2D* FrameSprite = BottomFrame_->CreateComponent<StaticSprite2D>();
	FrameSprite->SetSprite(boxSprite);
	FrameSprite->SetLayer(5);	// in front of Paddle

	FrameSprite = TopFrame_->CreateComponent<StaticSprite2D>();
	FrameSprite->SetSprite(boxSprite);
	FrameSprite = LeftFrame_->CreateComponent<StaticSprite2D>();
	FrameSprite->SetSprite(boxSprite);
	FrameSprite = RightFrame_->CreateComponent<StaticSprite2D>();
	FrameSprite->SetSprite(boxSprite);

    // Create box collider for Frame
    CollisionBox2D* groundShape = BottomFrame_->CreateComponent<CollisionBox2D>();
	groundShape->SetSize(Vector2(0.32f, 0.32f));
	groundShape->SetFriction(0.5f);

	groundShape = TopFrame_->CreateComponent<CollisionBox2D>();
    groundShape->SetSize(Vector2(0.32f, 0.32f));
    groundShape->SetFriction(0.5f);

	groundShape = LeftFrame_->CreateComponent<CollisionBox2D>();
	groundShape->SetSize(Vector2(0.32f, 0.32f));
	groundShape->SetFriction(0.5f);

	groundShape = RightFrame_->CreateComponent<CollisionBox2D>();
	groundShape->SetSize(Vector2(0.32f, 0.32f));
	groundShape->SetFriction(0.5f);

	paddle_ = scene_->CreateChild("Paddle");
	// Create rigid body
	paddle_->CreateComponent<RigidBody2D>();
	paddle_->GetComponent<RigidBody2D>()->SetBodyType(BT_STATIC);

	FrameSprite = paddle_->CreateComponent<StaticSprite2D>();
	FrameSprite->SetSprite(paddleSprite);
	groundShape = paddle_->CreateComponent<CollisionBox2D>();
	groundShape->SetSize(Vector2(PAD_PSIZEH, PAD_PSIZEV));

	FrameSprite->SetLayer(1);

	ScaleScreen();

	//some sound setup...
	sound_hit_Node_ = scene_->CreateChild("HitSound");
	sound_source_ = sound_hit_Node_->CreateComponent<SoundSource>();
	sound_source_->SetSoundType(SOUND_EFFECT);

	sound_ = cache->GetResource<Sound>("Ding1.wav");

}

void CyBall::PlayMySound(String soundFileName)
{
	//some sound setup...
	//sound_hit_Node_ = scene_->CreateChild("HitSound");
	//sound_source_ = sound_hit_Node_->CreateComponent<SoundSource>();
	//sound_source_->SetSoundType(SOUND_EFFECT);


	//ignore what's passed in for now. JUST PLAY THE DING...
	//sound_ = cache->GetResource<Sound>(soundFileName);
	sound_source_->Play(sound_);

}

void CyBall::SetupViewport()
{
    Renderer* renderer = GetSubsystem<Renderer>();

    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);
}

URHO3D_DEFINE_APPLICATION_MAIN(CyBall)[/code]

You'll have to add a sound beep file of your choosing, called "Ding1.wav".

-------------------------

dvan | 2017-01-02 01:10:23 UTC | #10

Finally got around to trying the startup params in a more controlled setting.

Set the SoundBuffer down to 10, and it helped a lot. Probably at least a 50% improvement in response in my various windows environments. Haven?t tried Android yet (it was unusable before), but would think it would help.

Not sure how this might effect a busy sound system down the road (can't think it's all good)?  None of the other sound settings had any noticeable effect.

Thanks for the feedback.

-------------------------

