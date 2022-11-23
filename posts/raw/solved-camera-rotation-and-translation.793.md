syjgin | 2017-01-02 01:02:55 UTC | #1

Don't understand, how to move camera parallel to world's left, right, forward and backward vectors, but with camera's y rotation component(blue arrow on the image): [img]http://rghost.net/60529260/image.png[/img] 
Now I'm trying to multiply node rotation matrix with move vector and translate it in local space. But in result camera moves to north/south etc. regardless of it's rotation:
[code]if(input->GetMousePosition().y_ < BORDER_OFFSET)
    {
        Quaternion currentRot = _cameraNode->GetRotation();
        Vector3 rotated = currentRot.Inverse().RotationMatrix() * Vector3(0,0,CAMERA_VELOCITY);
        _cameraNode->Translate(rotated);
    }
    if(input->GetMousePosition().y_ >  graphics->GetHeight() - BORDER_OFFSET)
    {
        Quaternion currentRot = _cameraNode->GetRotation();
        Vector3 rotated = currentRot.Inverse().RotationMatrix() * Vector3(0,0,-CAMERA_VELOCITY);
        _cameraNode->Translate(rotated);
    }[/code]

-------------------------

syjgin | 2017-01-02 01:02:56 UTC | #2

Update: now camera works as expected, but there are strange slow down when yaw angle is near +/90:
[code]
void LevelCamera::VerticalTranslate(float amount)
{
    Quaternion currentRot = _cameraNode->GetRotation();
    Matrix3 rotation = currentRot.Inverse().RotationMatrix();

    rotation.m00_ = 1;
    rotation.m10_ = 0;
    rotation.m20_ = 0;
    rotation.m01_ = 0;
    rotation.m02_ = 0;
    LOGINFO(String(currentRot.YawAngle()));
    if(currentRot.YawAngle() < -90 || currentRot.YawAngle() > 90)
            amount *= -1;
    Vector3 rotated = rotation * Vector3(0,0,amount);
    _cameraNode->Translate(rotated);
}

void LevelCamera::HorizontalTranslate(float amount)
{
    Quaternion currentRot = _cameraNode->GetRotation();
    Matrix3 rotation = currentRot.Inverse().RotationMatrix();
    rotation.m00_ = 1;
    rotation.m10_ = 0;
    rotation.m20_ = 0;
    rotation.m01_ = 0;
    rotation.m02_ = 0;
    Vector3 rotated = rotation * Vector3(amount,0,0);
    _cameraNode->Translate(rotated);
}

void LevelCamera::Update()
{
    UI* ui = GetSubsystem<UI>();
    Input* input = GetSubsystem<Input>();
    Graphics *graphics = GetSubsystem<Graphics>();

    if (ui->GetFocusElement())
        return;

    if(input->GetMousePosition().y_ < BORDER_OFFSET)
        VerticalTranslate(CAMERA_VELOCITY);
    if(input->GetMousePosition().y_ >  graphics->GetHeight() - BORDER_OFFSET)
        VerticalTranslate(-CAMERA_VELOCITY);
    if(input->GetMousePosition().x_ < BORDER_OFFSET)
        HorizontalTranslate(-CAMERA_VELOCITY);
    if(input->GetMousePosition().x_ >  graphics->GetWidth() - BORDER_OFFSET)
        HorizontalTranslate(CAMERA_VELOCITY);
    if (input->GetMouseButtonDown(MOUSEB_RIGHT))
    {
        IntVector2 mouseMove = input->GetMouseMove();
        _yaw += MOUSE_SENSITIVITY * mouseMove.x_;
        _pitch += MOUSE_SENSITIVITY * mouseMove.y_;
        Vector3 hitPos;
        Drawable* hitDrawable;
        if(Raycast(250.0f, hitPos, hitDrawable, true))
        {
            _cameraNode->RotateAround(hitPos, Quaternion(_yaw, Vector3(0,1,0)), TS_WORLD);
            if(abs((int)_pitch) < 20 )
            {
                if(_cameraNode->GetRotation().PitchAngle() < 45 &&  _pitch < 0)
                    _cameraNode->RotateAround(hitPos, Quaternion(_pitch, _cameraNode->GetDirection().CrossProduct(Vector3(0,1,0))), TS_WORLD);
                if(_cameraNode->GetRotation().PitchAngle() > 10 && _pitch > 0)
                    _cameraNode->RotateAround(hitPos, Quaternion(_pitch, _cameraNode->GetDirection().CrossProduct(Vector3(0,1,0))), TS_WORLD);
            }
        }

        _yaw = 0;
        _pitch = 0;
    }
    int wheelMove = input->GetMouseMoveWheel();
    if( wheelMove != 0 && abs((int)wheelMove) < 2)
    {
        Camera *camera = _cameraNode->GetComponent<Camera>();
        float oldZoom = camera->GetZoom();
        if(oldZoom > 0.5f && wheelMove < 0)
            camera->SetZoom(oldZoom + wheelMove*WHEEL_SENSITIVITY);
        if(oldZoom < 4 && wheelMove > 0)
            camera->SetZoom(oldZoom + wheelMove*WHEEL_SENSITIVITY);
    }
}

[/code]

If I have to change matrixes itself, I'm doing something wrong:(

-------------------------

codingmonkey | 2017-01-02 01:02:56 UTC | #3

mb it helps


1. in editor setup
[img]http://savepic.su/4843793.png[/img]

2. runtime setup
[code]
//application public:
	SharedPtr<Node> playerNode;
	RigidBody* playerRigidbody;

	struct
	{
		SharedPtr<Node> node;
		Camera* component;
		Viewport* viewport;
		float yaw_;
		float pitch_;
		float roll_;

	} camera;
[/code]

[code]
//app:Start()
		playerNode = scene_->GetChild("player", true);
		playerRigidbody = playerNode->GetComponent<RigidBody>();
		camera.node = scene_->GetChild("camera", true);
		camera.component = camera.node->GetComponent<Camera>();
[/code]

3. updates

[code]
	void HandleUpdate(StringHash eventType, VariantMap& eventData)
	{
		using namespace Update;
		float timeStep = eventData[P_TIMESTEP].GetFloat();
		MoveCamera(timeStep);


		if (playerRigidbody) 
		{
			Input* input = GetSubsystem<Input>();
			Quaternion worldRotation = camera.node->GetWorldRotation();
			worldRotation.z_ = 0;

			Vector3 dir = Vector3::ZERO;

			if (input->GetKeyDown('W')) 
			{
				dir += Vector3::FORWARD;
			}

			if (input->GetKeyDown('S'))
			{
				dir += Vector3::BACK;
			}

			if (input->GetKeyDown('D'))
			{
				dir += Vector3::RIGHT;
			}

			if (input->GetKeyDown('A'))
			{
				dir += Vector3::LEFT;
			}

			if (input->GetKeyDown(KEY_SPACE))
			{
				dir += Vector3::UP;
			}


			const float speed = 1800.0f;

			if (dir.Length() > 0)
				playerRigidbody->SetLinearVelocity(speed * (worldRotation * dir) * timeStep);
		}
	}
[/code]

[code]
	void MoveCamera(float timeStep)
	{
		Input* input = GetSubsystem<Input>();
		const float MOUSE_SENSITIVITY = 0.1f;
		IntVector2 mouseMove = input->GetMouseMove();

		camera.yaw_ += MOUSE_SENSITIVITY * mouseMove.x_;
		camera.pitch_ += MOUSE_SENSITIVITY * mouseMove.y_;
		camera.pitch_ = Clamp(camera.pitch_, -90.0f, 90.0f);
		camera.node->SetWorldRotation(Quaternion(camera.pitch_, camera.yaw_, 0.0f));

	}
[/code]

-------------------------

rogerdv | 2017-01-02 01:02:57 UTC | #4

I can confirm that the previous approach works. I use it for my isometric like view.

-------------------------

syjgin | 2017-01-02 01:02:57 UTC | #5

[quote="codingmonkey"]mb it helps
...[/quote]
Thanks, now I found a right way to move camera:
[code]void LevelCamera::VerticalTranslate(float amount)
{
    float currentRot = _cameraNode->GetRotation().YawAngle();
    Quaternion distilledRot;
    distilledRot.FromAngleAxis(currentRot, Vector3(0,1,0));
    Vector3 rotated = distilledRot.RotationMatrix() * Vector3(0,0,amount);
    _cameraNode->Translate(rotated, TS_WORLD);
}

void LevelCamera::HorizontalTranslate(float amount)
{
    float currentRot = _cameraNode->GetRotation().YawAngle();
    Quaternion distilledRot;
    distilledRot.FromAngleAxis(currentRot, Vector3(0,1,0));
    Vector3 rotated = distilledRot.RotationMatrix() * Vector3(amount,0,0);
    _cameraNode->Translate(rotated, TS_WORLD);
}
[/code]
But your rotation code is about rotating camera itself, not around current screen center. I still can not understand, how to rotate camera around current viewport center projection, if camera ray can not intersect anything:
[code]
if(Raycast(hitPos, hitDrawable))//need some fallback
        {
            _cameraNode->RotateAround(hitPos, Quaternion(_yaw, Vector3(0,1,0)), TS_WORLD);
            if(abs((int)_pitch) < 20 )
            {
                if(_cameraNode->GetRotation().PitchAngle() < 45 &&  _pitch < 0)
                    _cameraNode->RotateAround(hitPos, Quaternion(_pitch, _cameraNode->GetDirection().CrossProduct(Vector3(0,1,0))), TS_WORLD);
                if(_cameraNode->GetRotation().PitchAngle() > 10 && _pitch > 0)
                    _cameraNode->RotateAround(hitPos, Quaternion(_pitch, _cameraNode->GetDirection().CrossProduct(Vector3(0,1,0))), TS_WORLD);
            }
        }

...

bool LevelCamera::Raycast(Vector3 &hitPos, Drawable *&hitDrawable)
{
    hitDrawable = 0;

    UI* ui = GetSubsystem<UI>();

    Graphics* graphics = GetSubsystem<Graphics>();
    Camera *camera = _cameraNode->GetComponent<Camera>();
    Ray cameraRay = camera->GetScreenRay(0.5f, 0.5f);
    // Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
    PODVector<RayQueryResult> results;
    RayOctreeQuery query(results, cameraRay, RAY_TRIANGLE, 1000, DRAWABLE_GEOMETRY);
    _sceneNode->GetComponent<Octree>()->RaycastSingle(query);
    if (results.Size())
    {
        RayQueryResult& result = results[0];
        hitPos = result.position_;
        hitDrawable = result.drawable_;
        return true;
    }

    return false;

}
[/code]

-------------------------

rogerdv | 2017-01-02 01:02:57 UTC | #6

Dont know if this helps: I use a dual node system: one node is the target, it is the one that gets rotations and displacements. The second is a child node with the camera, every time I update the first node, I use LookAt to keep the camera  facing the target node. Perhaps the target node it is not exactly at the center of the screen, but it is almost there. I see you have better math knowledge than I, maybe you can refine my method and find the correct center point.

-------------------------

codingmonkey | 2017-01-02 01:02:58 UTC | #7

>I still can not understand, how to rotate camera around current viewport center 

1. setup in editor with adding rollNode
[img]http://savepic.su/4819862.png[/img]

roll node has idenity transforms!

2. setup code
[code]
		playerNode = scene_->GetChild("player", true);
		playerRigidbody = playerNode->GetComponent<RigidBody>();
		camera.node = playerNode->GetChild("camera", true);
		camera.rollNode = playerNode->GetChild("roll", true);
		camera.component = camera.rollNode->GetComponent<Camera>();
		camera.viewport = new Viewport(context_, scene_, camera.component);
[/code]

3. mouse update fix (roll camera by middle mouse)
[code]
	void MoveCamera(float timeStep)
	{
		Input* input = GetSubsystem<Input>();
		const float MOUSE_SENSITIVITY = 0.1f;
		IntVector2 mouseMove = input->GetMouseMove();

		if (input->GetMouseButtonDown(2)) {
			Quaternion q = camera.rollNode->GetRotation(); // get local rotation in space of parent camera node

			// q_new = q_old * q_delta // quaternion angle add by multiply 
			camera.rollNode->SetRotation(q * Quaternion(0, 0, MOUSE_SENSITIVITY * mouseMove.x_));
		}
		else 
		{
			camera.yaw_ += MOUSE_SENSITIVITY * mouseMove.x_;
			camera.pitch_ += MOUSE_SENSITIVITY * mouseMove.y_;
			camera.pitch_ = Clamp(camera.pitch_, -90.0f, 90.0f);
		}

		camera.node->SetWorldRotation(Quaternion(camera.pitch_, camera.yaw_, 0.0f));

	}
[/code]

-------------------------

syjgin | 2017-01-02 01:03:01 UTC | #8

I have created node with camera coordinates(0,20,-30) and its child roll node with coordinates (0,0,0). And added camera component to roll node.

But when I activated yaw and pitch related code, camera just shakes at same place. When I disabled it and retain only roll related, camera was rotated around local Z axis.

-------------------------

codingmonkey | 2017-01-02 01:03:02 UTC | #9

try to add in Start() proc

[code]camera.yaw_ = camera.pitch_ = camera.roll_ = 0.0f;[/code]

-------------------------

syjgin | 2017-01-02 01:03:03 UTC | #10

But you are not using roll_ variable in your code. I have removed _yaw and _pitch nullification at the end of any update cycle, camera stops shake, but simply don't move

-------------------------

codingmonkey | 2017-01-02 01:03:03 UTC | #11

Yes. i'm calculate new roll and put it directly in method, but other variables also need to setup with zero.

>but simply don't move
you mean don't move like - walk or run, or you mean rotation move ?
if you want somekind of walk-move you need to move or translate playerNode in case of my example. 
i'm move playerNode by set velocity for rigidbody on keys.

-------------------------

syjgin | 2017-01-02 01:03:03 UTC | #12

[quote="codingmonkey"]Yes. i'm calculate new roll and put it directly in method, but other variables also need to setup with zero.

>but simply don't move
you mean don't move like - walk or run, or you mean rotation move ?
if you want somekind of walk-move you need to move or translate playerNode in case of my example. 
i'm move playerNode by set velocity for rigidbody on keys.[/quote]

No rotation applied to camera. In the evening I will post my complete code. But previous version (with raycast) works well if ray can intersect some geometry. Maybe I have to just create default point on this ray if raycast fails.

-------------------------

syjgin | 2017-01-02 01:03:03 UTC | #13

Now it works well: I have created camera node with (0, 20, -30) position with camera component, and child node with reverse position: (0,20,-30) - this is local center node.
[code]#include "LevelCamera.h"

#include "UI.h"
#include "Input.h"
#include "Ray.h"
#include "Graphics.h"
#include "OctreeQuery.h"
#include "Octree.h"
#include "Scene.h"
#include "Log.h"

LevelCamera::LevelCamera(Context *context) :Object(context)
{

}


void LevelCamera::VerticalTranslate(float amount)
{
    float currentRot = _cameraNode->GetRotation().YawAngle();
    Quaternion distilledRot;
    distilledRot.FromAngleAxis(currentRot, Vector3(0,1,0));
    Vector3 rotated = distilledRot.RotationMatrix() * Vector3(0,0,amount);
    _cameraNode->Translate(rotated, TS_WORLD);
    _centerPosition->Translate(rotated);
}

void LevelCamera::HorizontalTranslate(float amount)
{
    float currentRot = _cameraNode->GetRotation().YawAngle();
    Quaternion distilledRot;
    distilledRot.FromAngleAxis(currentRot, Vector3(0,1,0));
    Vector3 rotated = distilledRot.RotationMatrix() * Vector3(amount,0,0);
    _cameraNode->Translate(rotated, TS_WORLD);
    _centerPosition->Translate(rotated);
}

void LevelCamera::Update()
{
    UI* ui = GetSubsystem<UI>();
    Input* input = GetSubsystem<Input>();
    Graphics *graphics = GetSubsystem<Graphics>();

    if (ui->GetFocusElement())
        return;

    if(input->GetMousePosition().y_ < BORDER_OFFSET)
        VerticalTranslate(CAMERA_VELOCITY);
    if(input->GetMousePosition().y_ >  graphics->GetHeight() - BORDER_OFFSET)
        VerticalTranslate(-CAMERA_VELOCITY);
    if(input->GetMousePosition().x_ < BORDER_OFFSET)
        HorizontalTranslate(-CAMERA_VELOCITY);
    if(input->GetMousePosition().x_ >  graphics->GetWidth() - BORDER_OFFSET)
        HorizontalTranslate(CAMERA_VELOCITY);
    if (input->GetMouseButtonDown(MOUSEB_RIGHT))
    {
        IntVector2 mouseMove = input->GetMouseMove();
        _yaw += MOUSE_SENSITIVITY * mouseMove.x_;
        _pitch += MOUSE_SENSITIVITY * mouseMove.y_;

        Vector3 centerPos = _centerPosition->GetPosition();
        _cameraNode->RotateAround(centerPos, Quaternion(_yaw, Vector3(0,1,0)), TS_WORLD);
        if(abs((int)_pitch) < 20 )
        {
            if(_cameraNode->GetRotation().PitchAngle() < 65 &&  _pitch < 0)
                _cameraNode->RotateAround(centerPos, Quaternion(_pitch, _cameraNode->GetDirection().CrossProduct(Vector3(0,1,0))), TS_WORLD);
            if(_cameraNode->GetRotation().PitchAngle() > 30 && _pitch > 0)
                _cameraNode->RotateAround(centerPos, Quaternion(_pitch, _cameraNode->GetDirection().CrossProduct(Vector3(0,1,0))), TS_WORLD);
        }

        _yaw = 0;
        _pitch = 0;
    }
    int wheelMove = input->GetMouseMoveWheel();
    if( wheelMove != 0 && abs((int)wheelMove) < 2)
    {
        Camera *camera = _cameraNode->GetComponent<Camera>();
        float oldZoom = camera->GetZoom();
        if(oldZoom > 0.5f && wheelMove < 0)
            camera->SetZoom(oldZoom + wheelMove*WHEEL_SENSITIVITY);
        if(oldZoom < 4 && wheelMove > 0)
            camera->SetZoom(oldZoom + wheelMove*WHEEL_SENSITIVITY);
    }
}


void LevelCamera::Setup(Node *cameraNode, Node *centerNode, Scene *scene)
{
    _sceneNode = scene;
    _cameraNode = cameraNode;
    _centerPosition = centerNode;

    cameraNode->LookAt(_centerPosition->GetPosition());

}
[/code]

-------------------------

