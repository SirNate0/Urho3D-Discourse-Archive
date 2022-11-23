spegi | 2017-01-02 01:12:55 UTC | #1

Hi.

I'm having a problem in using the networking functionality in Urho3D.
I have two classes: 'App' and 'Server' in my program. App extends the Urho3D::Application class and hosts an instance of Server. My problem is, that my server keeps receiving messages even without me sending any of them. I'm calling Urho3D::Connection::SendMessage only once.

My code:
[code]
// SandboxApplication.cpp
#pragma once

#include "stdafx.h"
#include "SandboxServer.h"

class SandboxApp : public Urho3D::Application
{
public:
	SandboxApp(Urho3D::Context *context)
		: Application(context), _net(0), _connection(0)
	{}

	void Setup()
	{
		// Irrelevant
	}

	void Start()
	{
		_net = GetSubsystem<Urho3D::Network>();

		_server = new SandboxServer(context_);
		_server->Start();

		SubscribeToEvent(Urho3D::E_KEYUP, URHO3D_HANDLER(SandboxApp, HandleKeyUp));

		SubscribeToEvent(Urho3D::E_NETWORKMESSAGE, URHO3D_HANDLER(SandboxApp, HandleNetworkMessage));
		SubscribeToEvent(Urho3D::E_SERVERCONNECTED, URHO3D_HANDLER(SandboxApp, HandleServerConnected));
		SubscribeToEvent(Urho3D::E_SERVERDISCONNECTED, URHO3D_HANDLER(SandboxApp, HandleServerDisconnected));
		SubscribeToEvent(Urho3D::E_CONNECTFAILED, URHO3D_HANDLER(SandboxApp, HandleConnectFailed));
	}

	void Stop()
	{
		if (_connection)
			_connection->Disconnect();
		_server->Stop();
	}

	void HandleKeyUp(Urho3D::StringHash eventType, Urho3D::VariantMap &eventData)
	{
		if (eventData[Urho3D::KeyUp::P_KEY] == Urho3D::KEY_ESC)
		{
			engine_->Exit();
		}
		else if (eventData[Urho3D::KeyUp::P_KEY] == Urho3D::KEY_RETURN && _connection)
		{
			URHO3D_LOGDEBUGF("App::KeyUp(RETURN)");
			Urho3D::VectorBuffer data;
			Urho3D::String msg = "Message from client";
			data.WriteString(msg);
			URHO3D_LOGDEBUGF("Client sent a message to server: '%s'", msg.CString());
			_connection->SendMessage(1024, true, true, data);
		}
		else if (eventData[Urho3D::KeyUp::P_KEY] == Urho3D::KEY_SPACE && !_connection)
		{
			URHO3D_LOGDEBUG("App::KeyUp(SPACE)");
			if (!_net->Connect("localhost", 26000, 0))
			{
				URHO3D_LOGDEBUGF("Network::Connect failed");
			}
		}
	}

	void HandleNetworkMessage(Urho3D::StringHash eventType, Urho3D::VariantMap &eventData)
	{
		URHO3D_LOGDEBUGF("App::Networkmessage");
		if (eventData[Urho3D::NetworkMessage::P_MESSAGEID] == 1024)
		{
			const Urho3D::PODVector<uint8_t> &data = eventData[Urho3D::NetworkMessage::P_DATA].GetBuffer();
			Urho3D::MemoryBuffer msgFromServer(data);
			Types::String text = msgFromServer.ReadString();
			URHO3D_LOGDEBUGF("Client received a message from server: '%s'", text.CString());
		}
	}

	void HandleServerConnected(Urho3D::StringHash eventType, Urho3D::VariantMap &eventData)
	{
		_connection = _net->GetServerConnection();
		URHO3D_LOGDEBUG("App::Connected");
	}

	void HandleConnectFailed(Urho3D::StringHash eventType, Urho3D::VariantMap &eventData)
	{
		_connection = 0;
		URHO3D_LOGDEBUG("App::ConnectFailed");
	}

private:
	Urho3D::Network *_net;
	Urho3D::SharedPtr<SandboxServer> _server;
	Urho3D::Connection *_connection;
};
[/code]

[code]
// SandboxServer.h
#pragma once

#include "stdafx.h"

class SandboxServer : public Urho3D::Object
{
	URHO3D_OBJECT(SandboxServer, Object)

public:
	SandboxServer(Urho3D::Context *context)
		: Object(context)
	{

	}

	void Start()
	{
		_net = GetSubsystem<Urho3D::Network>();

		if (!_net->StartServer(26000))
		{
			URHO3D_LOGDEBUG("Network::StartServer failed");
			GetSubsystem<Urho3D::Engine>()->Exit();
		}

		SubscribeToEvent(Urho3D::E_NETWORKMESSAGE, URHO3D_HANDLER(SandboxServer, HandleNetworkMessage));
		SubscribeToEvent(Urho3D::E_CLIENTCONNECTED, URHO3D_HANDLER(SandboxServer, HandleClientConnected));
		SubscribeToEvent(Urho3D::E_CLIENTDISCONNECTED, URHO3D_HANDLER(SandboxServer, HandleClientDisconnected));
	}

	void Stop()
	{
		_net->StopServer();
	}

	void HandleNetworkMessage(Urho3D::StringHash eventType, Urho3D::VariantMap &eventData)
	{
		URHO3D_LOGDEBUGF("Server::Networkmessage");
		if (eventData[Urho3D::NetworkMessage::P_MESSAGEID] == 1024 && _net->IsServerRunning())
		{
			const Urho3D::PODVector<uint8_t> &data = eventData[Urho3D::NetworkMessage::P_DATA].GetBuffer();
			Urho3D::MemoryBuffer msgFromClient(data);
			Types::String text = msgFromClient.ReadString();
			URHO3D_LOGDEBUGF("Server received a message from client: '%s'", text.CString());

			Urho3D::VectorBuffer buf;
			Urho3D::String msg = "Broadcasted message from server";
			buf.WriteString(msg);
			URHO3D_LOGDEBUGF("Server broadcasted a message to the clients: '%s'", msg.CString());
			_net->BroadcastMessage(1024, true, true, buf);
		}
	}

	void HandleClientConnected(Urho3D::StringHash eventType, Urho3D::VariantMap &eventData)
	{
		URHO3D_LOGDEBUGF("Server::ClientConnected");
	}

	void HandleClientDisconnected(Urho3D::StringHash eventType, Urho3D::VariantMap &eventData)
	{
		URHO3D_LOGDEBUGF("Server::ClientConnected");
	}

private:
	Urho3D::Network *_net;
};
[/code]

My output log:
[code]
(Init stuff)
[Sat Jun 18 22:10:48 2016] INFO: Started server on port 26000
[Sat Jun 18 22:10:48 2016] DEBUG: Reloading shaders
[Sat Jun 18 22:10:49 2016] DEBUG: App::KeyUp(SPACE)
[Sat Jun 18 22:10:49 2016] INFO: Connecting to server 127.0.0.1:26000
[Sat Jun 18 22:10:49 2016] INFO: Client 127.0.0.1:54314 connected
[Sat Jun 18 22:10:49 2016] DEBUG: Server::ClientConnected
[Sat Jun 18 22:10:49 2016] INFO: Connected to server
[Sat Jun 18 22:10:49 2016] DEBUG: App::Connected
[Sat Jun 18 22:10:49 2016] DEBUG: App::KeyUp(RETURN)
[Sat Jun 18 22:10:49 2016] DEBUG: Client sent a message to server: 'Message from client'
[Sat Jun 18 22:10:49 2016] DEBUG: Server::Networkmessage
[Sat Jun 18 22:10:49 2016] DEBUG: Server received a message from client: 'Message from client'
[Sat Jun 18 22:10:49 2016] DEBUG: Server broadcasted a message to the clients: 'Broadcasted message from server'
[Sat Jun 18 22:10:49 2016] DEBUG: App::Networkmessage
[Sat Jun 18 22:10:49 2016] DEBUG: Client received a message from server: 'Message from client'
[Sat Jun 18 22:10:49 2016] DEBUG: Server::Networkmessage
[Sat Jun 18 22:10:49 2016] DEBUG: Server received a message from client: 'Broadcasted message from server'
[Sat Jun 18 22:10:49 2016] DEBUG: Server broadcasted a message to the clients: 'Broadcasted message from server'
[Sat Jun 18 22:10:49 2016] DEBUG: App::Networkmessage
[Sat Jun 18 22:10:49 2016] DEBUG: Client received a message from server: 'Broadcasted message from server'
[Sat Jun 18 22:10:49 2016] DEBUG: Server::Networkmessage
(This just keeps on going)
[/code]

Is it even possible to have a client and server in the same application or am I just doing something wrong?

-------------------------

Lumak | 2017-01-02 01:12:55 UTC | #2

Your message traffic is cyclic because the client echos server's broadcast message back to the server.

-------------------------

rasteron | 2017-01-02 01:12:58 UTC | #3

..and when in doubt, there's the demo examples for you to learn from or familiarize yourself with Urho3D networking. :slight_smile:

-------------------------

