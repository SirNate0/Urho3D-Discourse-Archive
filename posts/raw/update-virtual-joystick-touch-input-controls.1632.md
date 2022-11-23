rasteron | 2017-01-02 01:09:06 UTC | #1

More of an enhancement, as the current onscreen joystick functions more like a D-Pad with little space and you have to make sure you press up and right (for example) to trigger/move diagonally. Maybe something similar with other toolkits and mobile engine implementation that has a circle restriction and pulls back to the center when you let go of the virtual stick.

Example:
[activetuts.s3.amazonaws.com/tuts ... pp_006.swf](http://activetuts.s3.amazonaws.com/tuts/236_virtualJoystick/tutorial/tutorial/swfs/JoystickApp_006.swf)


[img]http://jayanam.com/wp-content/uploads/2015/04/touch_2.jpg[/img]

-------------------------

Kyle00 | 2017-01-02 01:09:08 UTC | #2

Gameplay3D has that exact implementation, [url]https://github.com/gameplay3d/GamePlay[/url] - see src/JoystickControl.cpp

-------------------------

rasteron | 2017-01-02 01:09:09 UTC | #3

[quote="Kyle00"]Gameplay3D has that exact implementation, [url]https://github.com/gameplay3d/GamePlay[/url] - see src/JoystickControl.cpp[/quote]

Yes, I also have seen a lot of ActionScripts that can be converted to Angelscript, perhaps using Urho2D sprites on top or just built-in UI button and drag..

-------------------------

Sir_Nate | 2017-01-02 01:09:20 UTC | #4

If you're mostly just after using actual axes instead of a simulated hat, I wrote this class to do that (it shows a joystick centered where you touch within the specified area, which disappears after you release):
It needs some cleaning up, as you can see, but I've not (yet) noticed any problems in the results.

Note that the joystick you use should have the given number of axes (i.e. create the needed [code]
    <element type="UIElement">
        <attribute name="Name" value="Axis2" />
        <attribute name="Visible" value="false" />
    </element>[/code] elements in the screen joystick file) (the "Name" attributes must start with "Axis")
Try testing it with a file with 3 joysticks, running something like:
[code]new Stick(context_->GetSubsystem<UI>()->GetRoot(), GetSubsystem<Input>()->AddScreenJoystick(GetSubsystem<ResourceCache>()->GetResource<XMLFile>("UI/TestAxes.xml")), 0, {0,200,800,600}, false);
[/code]
[code]
#include <Core/Object.h>
#include <UI/BorderImage.h>
//#include <UI/Sprite.h> I was going to make the knob a sprite, so it could be rotated for a skewing effect, as if you were tilting it, but as you can see that didn't happen
#include <Resource/ResourceCache.h>
#include <Graphics/Texture2D.h>
#include <ThirdParty/SDL/SDL_events.h>

using namespace Urho3D;

class Stick: public Object
{
	bool fixed_;//TODO: implement this (a fixed position joystick, that doesn't appear where you touch)
	IntVector2 position_;
	IntVector2 direction_; //x, y, pressure
	float pressure_;
	IntRect allowedArea_;

	int size_;

	SharedPtr<BorderImage> base_;
	SharedPtr<BorderImage> knob_;
//	SharedPtr<UIElement> area_;

	int touchID_;

	//Implementation details relating to the input events
	SDL_JoystickID joystickID_;
	int axisOffset_;
	bool pressureAsZ_;
public:
	URHO3D_OBJECT(Stick, Object)
	Stick(UIElement* root, SDL_JoystickID id, int axisOffset, IntRect area,  bool pressureAsZAxis = true):
		Object(root->GetContext()), size_(40), fixed_(false), touchID_(-1), pressure_(0), allowedArea_(area),
		joystickID_(id), axisOffset_(axisOffset), pressureAsZ_(pressureAsZAxis)
	{
		SubscribeToEvent(E_TOUCHBEGIN, HANDLER(Stick, TouchStart));
		SubscribeToEvent(E_TOUCHMOVE, HANDLER(Stick, Touch));
		SubscribeToEvent(E_TOUCHEND, HANDLER(Stick, TouchFinish));


//		area_ = root->CreateChild<UIElement>("StickArea");
		base_ = root->CreateChild<BorderImage>("StickBase");
		knob_ = base_->CreateChild<BorderImage>("StickKnob");
//		area_->SetOpacity(0.5);
//		area_->SetPosition(allowedArea_.left_,allowedArea_.top_);
//		area_->SetFixedSize(allowedArea_.Size());
//		area_->SetSize(allowedArea_.Size());

//		base_->SetPosition(allowedArea_.left_,allowedArea_.top_);
		base_->SetFixedSize(size_*2, size_*2);
		base_->SetSize(size_*2, size_*2);

		knob_->SetFixedSize(size_, size_);
		knob_->SetSize(size_, size_);

		base_->SetTexture(GetSubsystem<ResourceCache>()->GetResource<Texture2D>("Textures/JoystickBase.png"));
		base_->SetFullImageRect();
		base_->SetOpacity(0.7);
		knob_->SetTexture(GetSubsystem<ResourceCache>()->GetResource<Texture2D>("Textures/JoystickKnob.png"));
		knob_->SetFullImageRect();
		knob_->SetOpacity(0.9);

		SetVisible(false);

//		XMLFile* style = GetSubsystem<ResourceCache>()->GetResource<XMLFile>("UI/DefaultStyle.xml");
//		base_->SetStyleAuto(style);

	}

	void SetVisible(bool val)
	{
		base_->SetVisible(val);
		knob_->SetVisible(val);
	}
	void SetPosition(const IntVector2& pos)
	{
		position_ = pos;
		base_->SetPosition(pos - IntVector2(size_,size_));
	}
	void SetDirection(const IntVector2& dir)
	{
		direction_ = dir;
		Vector2 d = {dir.x_, dir.y_};
		if (d.Length() > size_)
		{
			d.Normalize();
			d = d * size_;
			knob_->SetPosition(IntVector2{d.x_, d.y_} - (knob_->GetSize() / 2) + IntVector2(size_, size_));
		}
		else
			knob_->SetPosition(dir - (knob_->GetSize() / 2) + IntVector2(size_, size_));

	}
	void TouchStart(StringHash eventType, VariantMap& eventData)
	{
		if (touchID_ != -1)
			return;
		using namespace TouchBegin;

		int x = eventData[P_X].GetInt();
		int y = eventData[P_Y].GetInt();

		if (allowedArea_.IsInside({x,y}))
		{
			pressure_ = eventData[P_PRESSURE].GetFloat();
			touchID_ = eventData[P_TOUCHID].GetInt();
			SetPosition({x,y});
			SetDirection({0,0});
			SetVisible(true);
			UpdateAndSendEvents();
		}
	}
	void Touch(StringHash eventType, VariantMap& eventData)
	{
		using namespace TouchMove;

		if (touchID_ != eventData[P_TOUCHID].GetInt())
			return;

		int x = eventData[P_X].GetInt();
		int y = eventData[P_Y].GetInt();

//		if (allowedArea_.IsInside({x,y}))
//		{
			pressure_ = eventData[P_PRESSURE].GetFloat();
//			SetPosition({x,y});
			SetDirection(IntVector2{x,y} - position_);
//		}
		UpdateAndSendEvents();
	}
	void TouchFinish(StringHash eventType, VariantMap& eventData)
	{
		if (touchID_ == -1)
			return;
		using namespace TouchEnd;

		pressure_ = 0;
		touchID_ = -1;
		SetDirection({0,0});
		SetVisible(false);
		UpdateAndSendEvents();
	}
	float GetX()
	{
		//this would result in ~ .7 for x and y, so scale and clip it
//		return direction_.x_;
		return Clamp(direction_.x_ * sqrtf(2) / size_,-1.0f, 1.0f);

	}
	float GetY()
	{
//		return direction_.y_;
		return Clamp(direction_.y_ * sqrtf(2) / size_,-1.0f, 1.0f);
	}
	float GetPressure()
	{
		return pressure_;
	}
	void UpdateAndSendEvents()
	{
		using namespace JoystickAxisMove;
		//X axis
		JoystickState* state = GetSubsystem<Input>()->GetJoystick(joystickID_);
		if (!state)
			return;

		if (!state->controller_)
		{
			VariantMap& eventData = GetEventDataMap();
			eventData[P_JOYSTICKID] = joystickID_;
			eventData[P_AXIS] = axisOffset_;//evt.jaxis.axis;
			eventData[P_POSITION] = GetX();//Clamp((float)evt.jaxis.value / 32767.0f, -1.0f, 1.0f);

			if (axisOffset_ < state->axes_.Size())
			{
				// If the joystick is a controller, only use the controller axis mappings
				// (we'll also get the controller event)
				if (!state->controller_)
					state->axes_[axisOffset_] = eventData[P_POSITION].GetFloat();
				SendEvent(E_JOYSTICKAXISMOVE, eventData);
			}
		//Y axis
			//re-assign all values in case they were changed
			eventData[P_JOYSTICKID] = joystickID_;
			eventData[P_AXIS] = axisOffset_ + 1;//evt.jaxis.axis;
			eventData[P_POSITION] = GetY();//Clamp((float)evt.jaxis.value / 32767.0f, -1.0f, 1.0f);

			if (axisOffset_ + 1 < state->axes_.Size())
			{
				// If the joystick is a controller, only use the controller axis mappings
				// (we'll also get the controller event)
				if (!state->controller_)
					state->axes_[axisOffset_ + 1] = eventData[P_POSITION].GetFloat();
				SendEvent(E_JOYSTICKAXISMOVE, eventData);
			}

		//Pressure/Z axis
			if (pressureAsZ_)
			{
				//re-assign all values in case they were changed
				eventData[P_JOYSTICKID] = joystickID_;
				eventData[P_AXIS] = axisOffset_ + 2;//evt.jaxis.axis;
				eventData[P_POSITION] = GetPressure();

				if (axisOffset_ + 1 < state->axes_.Size())
				{
					// If the joystick is a controller, only use the controller axis mappings
					// (we'll also get the controller event)
					if (!state->controller_)
						state->axes_[axisOffset_ + 1] = eventData[P_POSITION].GetFloat();
					SendEvent(E_JOYSTICKAXISMOVE, eventData);
				}
			}
		}
	}

//	Vector<SDL_Event> GetEvent()
//	{
//		// Dragging past the directional boundary will cause an additional key up event for previous key symbol
//		SDL_Event axisEvent;
//		axisEvent.type = SDL_JOYAXISMOTION;
//		axisEvent.jaxis.axis = 0 + area_->GetVar("AxisOffset").GetInt();
//		axisEvent.jaxis.value = GetX() * 32767.0f;
//
//				0 + area_->GetVar("AxisOffset").GetInt();
//				element->GetVar(VAR_LAST_KEYSYM).GetInt();
//		if (keyEvent.key.keysym.sym)
//		{
//			keyEvent.key.keysym.scancode = SDL_SCANCODE_UNKNOWN;
//			HandleSDLEvent(&keyEvent);
//		}
//
//		element->SetVar(VAR_LAST_KEYSYM, 0);
//	}
};[/code]

-------------------------

rasteron | 2017-01-02 01:09:21 UTC | #5

Cool. Do you have any completed examples that we can try out?  :slight_smile:

-------------------------

