Elendil | 2019-09-24 15:41:54 UTC | #1

I am calling function from secondary thread without any problem until I saw this on console:

> ERROR: Sending events is only supported from the main thread

this is function called from second thread
     
    void Player_LightOnOff(bool OnTrue)
    {
    	if (Urho3D::Player::Player_Instance != nullptr)
    	{
    		Urho3D::Player::Player_Instance->LightOnOff(OnTrue);
    	}
    }


    void Urho3D::Player::LightOnOff(bool OnTrue)
    {
    	if (OnTrue)
    	{
    		m_light->SetEnabled(true);
    	}
    	else
    	{
    		m_light->SetEnabled(false);
    	}
    }

code is working I have no crashes, but should I call it really from main thread?

-------------------------

Modanung | 2019-09-24 15:51:07 UTC | #2

Are you using `SendEvent(StringHash)` somewhere?

-------------------------

Elendil | 2019-09-24 15:59:38 UTC | #3

No, as I remember and from quick check, and if yes, I am 100% sure that not from second thread.

EDIT: No I am not use SendEvent

-------------------------

weitjong | 2019-09-24 16:58:51 UTC | #4

If the `m_light` is an object instance derived from `Urho3D::Component` class then that would explain it. The `Component::SetEnabled()` method will send an event before it returns, but in your case instead of sending the event, the engine simply logging it as a programming error and bailing out.

https://github.com/urho3d/Urho3D/blob/fda628912d3ba7b0059e26135521f6a285d2dcae/Source/Urho3D/Scene/Component.cpp#L139

https://github.com/urho3d/Urho3D/blob/fda628912d3ba7b0059e26135521f6a285d2dcae/Source/Urho3D/Core/Object.cpp#L299-L303

I think you should move that logic to the main thread if you would like to take advantage of Urho3D event handling, specifically the `E_COMPONENTENABLEDCHANGED` event of your light component.

-------------------------

Elendil | 2019-09-24 17:03:57 UTC | #5

Thanks, m_light is Urho3D component and your answer describe it what cause that error.

-------------------------

