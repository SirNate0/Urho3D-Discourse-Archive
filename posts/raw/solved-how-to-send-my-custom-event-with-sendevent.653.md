codingmonkey | 2017-01-02 01:01:54 UTC | #1

Hi folks!

I'm trying to send global event from blasts or boom fx then it's almoust end;

and i'm don't know how to pack Vector3 to my event.

i'm write something but it's dosen't work.

this happen then blast must remove, i'm send event.
[code]
		SharedPtr<VariantMap> v;

		v["BlastPos"] = GetNode()->GetWorldPosition();
		
		SendEvent(StringHash("Blast"), v);

		GetNode()->Remove();
[/code]

Then player got this message he check radius to blast. and if it's near then player add some shake(noise movements) for your's camera;

-------------------------

codingmonkey | 2017-01-02 01:01:54 UTC | #2

ok now i resolved this, 
i'm going to source of engine for looking code like - how to create eventmap parameter and there i found some kind of method - GetEventDataMap();
i'm use it and its works now.

[code]
void ScriptFireFx::FixedUpdate(float timeStep)
{

	float t = animState_->GetTime();
	float l = animState_->GetLength(); 
	
	if  ( t > l ) 
	{
		using namespace AnimationTrigger;
		animState_->SetTime(0.0f);

		VariantMap& eventData = GetNode()->GetEventDataMap();

		eventData[P_DATA] = GetNode()->GetWorldPosition();
		
		SendEvent(StringHash("Blast"), eventData);

		GetNode()->Remove();

	}
}
[/code]

-------------------------

thebluefish | 2017-01-02 01:01:54 UTC | #3

You can actually change:
[code]
SendEvent(StringHash("Blast"), eventData);
[/code]
to:
[code]
SendEvent("Blast", eventData);
[/code]

There is already implicit conversion, so you don't need to do the conversion to StringHash yourself.

You can also define your own events like so:
[code]
#ifndef _GAME_EVENTS_H
#define _GAME_EVENTS_H

#include "Object.h"

EVENT(E_SERVER_CHATMESSAGE, ServerChatMessage)
{
	PARAM(P_CHANNEL, Channel);  //int
	PARAM(P_SENDER, Sender);  //string    
	PARAM(P_MESSAGE, Message);  //string   
}

#endif
[/code]

If I include this, I can call an event like so:
[code]
Urho3D::VariantMap map;
map[ServerChatMessage::P_CHANNEL] = channel;
map[ServerChatMessage:] = sender;
map[ServerChatMessage::P_MESSAGE] = message;
//connection->SendRemoteEvent(E_SERVER_CHATMESSAGE, true, map);
SendEvent(E_SERVER_CHATMESSAGE, map);
[/code]

-------------------------

codingmonkey | 2017-01-02 01:01:55 UTC | #4

thank you! it's very useful example

-------------------------

