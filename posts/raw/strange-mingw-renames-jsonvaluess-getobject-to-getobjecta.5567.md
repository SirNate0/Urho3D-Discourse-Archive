dertom | 2019-09-12 08:40:06 UTC | #1

Hiho,...atm I'm trying to cross-compile my testgame to windows using mingw. Most of the stuff compiles, but one thing does not:
```
/var/sample/src/game/serverObjects/MasterServerCommunication.cpp: In member function 'void MasterServerCommunication::HandleBeginFrame(Urho3D::StringHash, Urho3D::VariantMap&)':
/var/sample/src/game/serverObjects/MasterServerCommunication.cpp:46:40: error: 'const class Urho3D::JSONValue' has no member named 'GetObject'; did you mean 'GetObjectA'?
                 JSONObject data = root.GetObject();
                                        ^~~~~~~~~
                                        GetObjectA

```
The thing is, I use identical code at other classes without a problem 
```
                JSONFile jsonFile(context_);
                jsonFile.FromString(String(json.c_str()));
                const JSONValue root = jsonFile.GetRoot();
                JSONObject data = root.GetObject();
```

I found the suggestion strange '**did you mean GetObjectA**'. Just out of curiosity I tried GetObjectA() and it compiled!? :laughing:  I'm actually not sure what I made wrong. Is that a known behaviour and what would be a keyword to search for. I refuse to use an #ifdef MINGW and use GetObjectA :smiley: (for now). 

(btw, on linux it compiles with GetObject as intended)

Here the complete cpp-file. Maybe someone see something, beside ugly code:
```
#include "MasterServerCommunication.h"
//#include "Server/SaalisServer.h"
//#include <game/gameObjects/SaalisServer.h>
#include <Urho3D/Scene/Scene.h>
#include <zmq_addon.hpp>
#include <game/SaalisEvents.h>
#include <game/serverObjects/SaalisServer.h>
#include <Urho3D/Resource/JSONFile.h>
//#include <Urho3D/Resource/JSONValue.h>

MasterServerCommunication::MasterServerCommunication(Context* context)
    : Object(context),
      state_(FLAG_SEND_READY_INFO)

{
    saalisServer = GetSubsystem<SaalisServer>();
    SubscribeToEvent(E_BEGINFRAME,URHO3D_HANDLER(MasterServerCommunication,HandleBeginFrame));
}


void MasterServerCommunication::Connect(const String &masterUrl, int masterPort)
{
    reqSocket_ = zmq::socket_t(ctx, zmq::socket_type::req);
    reqSocket_.connect( (String("tcp://")+masterUrl+":"+String(masterPort)).CString());
}


void MasterServerCommunication::HandleBeginFrame(StringHash eventType, VariantMap &eventData)
{
    if (state_ == FLAG_SEND_READY_INFO){
        msg.clear();
        msg.addstr(saalisServer->GetServerName().CString());
        msg.addstr( ((String("ready,"+saalisServer->GetServerName()+",")+String(saalisServer->MatchSlotsLeft()))).CString()) ;
        msg.send(reqSocket_);
        state_ = FLAG_RECEIVE_REQUEST;
    }
    else if (state_ == FLAG_RECEIVE_REQUEST){
        bool success = msg.recv(reqSocket_,ZMQ_NOBLOCK);
        if (success){
            auto type = msg.popstr();
            if (type == "create_match"){
                auto json = msg.popstr();
                JSONFile jsonFile(context_);
                jsonFile.FromString(String(json.c_str()));
                const JSONValue root = jsonFile.GetRoot();
                JSONObject data = root.GetObjectA();
                using namespace MasterEventCreateMatch;
                VariantMap masterEventData;

                String matchId = data["match_id"].GetString();
                String token = data["token"].GetString();

                auto jsonUsers = data["users"].GetArray();
                StringVector users;
                for (auto u : jsonUsers){
                    users.Push(u.GetString());
                }

                if (saalisServer->IsNewSessionAllowed()){
                    saalisServer->CreateNewSession(matchId,token,users);
                    // TODO: send via pubsubcom about creation

//                    msg.clear();
//                    msg.addstr(saalisServer->GetServerName().CString());
//                    msg.addstr((String("created-match,"+saalisServer->GetServerName()+",")+matchId).CString());
//                    msg.send(reqSocket_);
                } else {
                    // TODO: send via pubsubcom about fail in creation

//                    msg.clear();
//                    msg.addstr(saalisServer->GetServerName().CString());
//                    msg.addstr((String("not_created-match,"+saalisServer->GetServerName()+",")+matchId).CString());
//                    msg.send(reqSocket_);
                }
                if (saalisServer->IsNewSessionAllowed()){
                    state_=FLAG_SEND_READY_INFO;
                } else {
                    state_=FLAG_WAIT_FOR_RESOURCES;
                }
            }
        }
    }

}



void MasterServerCommunication::RegisterObject(Context* context) {
}



```

-------------------------

JTippetts | 2019-09-12 08:40:15 UTC | #2

Are you including the windows.h header anywhere? That is a thing that happens sometimes, because windows.h includes wingdi.h, which defines a GetObject as a macro, and defines a function called GetObjectA, which then ends up in suggestions. It is a good idea to avoid including windows.h if at all possible because of this.

-------------------------

dertom | 2019-09-12 00:02:11 UTC | #3

@JTippetts, thx dude! You gave me the right direction. I'm using ZeroMQ for networking and this includes at some point windows.h. I located the 'evil' include and just added JSONValue-include before that. 
```
#include <Urho3D/Resource/JSONValue.h> 
#include <3rd/cppzmq/zmq.hpp> // <---including windows.h
```
That did the trick. Thx again. Didn't expect to solve that so quickly ;)

-------------------------

JTippetts | 2019-09-12 00:06:34 UTC | #4

You're welcome. This thing has bitten me in the ass quite a few times over the years, and not just in Urho3D. Imagine being the kind of nefarious human being who pollutes the global namespace with a macro named GetObject. :laughing:

-------------------------

jmiller | 2019-09-13 12:49:43 UTC | #5

Years ago I, when compiling Urho on mingw, had evolved this bit of code for the issues encountered.

[code]
#pragma once

// Including <windows.h> typically means introducing thousands of macros and types. Somewhat limit win32 pollution...
#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN
#define NOSERVICE
#define NOMCX
#define NOIME
#define NONLS
#include <windows.h>
#undef CreateDirectory
#undef GetClassName
#undef GetProp
#undef RemoveProp
#undef SetProp
#endif
[/code]

-------------------------

