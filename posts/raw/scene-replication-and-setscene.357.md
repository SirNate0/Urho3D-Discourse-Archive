Firegorilla | 2017-01-02 00:59:51 UTC | #1

Hello,

I was trying to get scene replication to work, but I cant quite figure it out. I have the client and server side on the same application. I can connect and receive a message just fine, but from before I connect to after, my scene stays the same, and the data from the scene node doesn't transfer over. Based on the documentation, I figured it would be automatic. However, I noticed in the scene replication sample, there is a call to SetScene(). I included it in the server side, right before I send the confirmation message to the client, but it doesn't seem to make a difference. Anyone have any idea as to why it is able to connect and receive messages, but is not replicating the scene? I am completely stumped.

-------------------------

weitjong | 2017-01-02 00:59:51 UTC | #2

How do you create your nodes and components in your scene? Are they created using 'replicated' mode?

-------------------------

Firegorilla | 2017-01-02 00:59:51 UTC | #3

I am loading them from an XML file, which has no attributes for local or replicated. I figured that, because the default in the code is replicated, it would create replicated nodes. Additionally, to test it, I create a zone component to the child of the scene with fog color white, but when I render, it is still black. I think that it is all on replicated, but still not working

-------------------------

weitjong | 2017-01-02 00:59:51 UTC | #4

There is no such attribute. The mode is determined by the node/component ID range. Here is the snippet of the documentation regarding 'scene replication' found in [urho3d.github.io/documentation/a00036.html](http://urho3d.github.io/documentation/a00036.html).

[quote]The CreateMode translates into two different node and component ID ranges - replicated ID's range from 0x1 to 0xffffff, while local ID's range from 0x1000000 to 0xffffffff. This means there is a maximum of 16777215 replicated nodes or components in a scene.[/quote]

-------------------------

Firegorilla | 2017-01-02 00:59:51 UTC | #5

All of my node IDs (serverside) are in the 1-60 ish range. Moreover, I save the scene elsewhere, and it keeps all node ID's in the 1-60ish range, which would mean they are all replicated I think?

I did some more testing. I have it set up so that the client scene, before connecting, starts white, and the server scene has a blue zone (zones with fog color). However, when I connect to the server, it turns the scene black. When I comment out SetScene(), it stays white. Perhaps there is something wrong in the way it connects, or how set scene is used?

-------------------------

weitjong | 2017-01-02 00:59:51 UTC | #6

Sorry for not being more helpful but since you did not attach any of your code or sample of your XML scene, it is difficult to forum reader to help to troubleshoot. I assume you have checked out the Scene Replication demo in the samples. I suppose you can easily modify it to load your XML scene instead and see if the network replication still work. If it does then you have problem with your code.

-------------------------

Firegorilla | 2017-01-02 00:59:51 UTC | #7

Yeah, sorry about that. I will try and make it work with the sample now. The code is a bit messy, but here it is:
Client.cpp
[code]#include "Client.h"

#include "Camera.h"
#include "CoreEvents.h"
#include "NetworkEvents.h"
#include "Octree.h"
#include "Renderer.h"
#include "Zone.h"

Client::Client(Context * context) : Object(context), context_(context), network_(new Network(context)), clientScene_(new Scene(context))
{
	clientScene_->Clear(true, false);
	connected_ = false;
	SubscribeToEvent(E_NETWORKMESSAGE, HANDLER(Client, HandleNetworkMessage));
	clientScene_->CreateComponent<Octree>();
	Zone * temp = clientScene_->CreateChild()->CreateComponent<Zone>();
	temp->SetFogColor(Color::WHITE);
	input_ = context->GetSubsystem<Input>();
	Camera * cam = clientScene_->CreateChild()->CreateComponent<Camera>();
	//	Camera * cam = controlledNode_->CreateComponent<Camera>(LOCAL);
	//	Renderer * r = GetSubsystem<Renderer>();

	GetSubsystem<Renderer>()->SetViewport(0, new Viewport(context_, clientScene_, cam));
}


Client::~Client()
{
}

bool Client::Connect(String IP, int port = 7346)
{
	connected_ = network_->Connect(IP, port, clientScene_);
	connection_ = network_->GetServerConnection();
	if (connection_)
	{
		//connection_->SetScene()
	}
	//clientScene_->CreateComponent<Octree>(LOCAL);
	//Zone * temp = clientScene_->CreateChild()->CreateComponent<Zone>();
	//temp->SetFogColor(Color::WHITE);
	return connected_;
}
void Client::Disconnect()
{

}

void Client::HandleNetworkMessage(StringHash eventType, VariantMap& eventData)
{
	//assigning node
	//connection_->SetScene()
	if (eventData[NetworkMessage::P_MESSAGEID].GetInt() == 31)
	{
		VectorBuffer b = eventData[NetworkMessage::P_DATA].GetBuffer();
		controlledNode_ = clientScene_->GetNode(b.ReadUInt());
		//CreateCamera();
	}
}

void Client::CreateCamera()
{
	Camera * cam = clientScene_->CreateChild()->CreateComponent<Camera>();
//	Camera * cam = controlledNode_->CreateComponent<Camera>(LOCAL);
//	Renderer * r = GetSubsystem<Renderer>();
	GetSubsystem<Renderer>()->SetViewport(0, new Viewport(context_, clientScene_, cam));
}[/code]

Server.cpp
[code]#include "Server.h"

#include "CoreEvents.h"
#include "File.h"
#include "FileSystem.h"
#include "NetworkEvents.h"
#include "Octree.h"
#include "PhysicsWorld.h"
#include "Zone.h"

Server::Server(Context * context) : Object(context), context_(context), network_(new Network(context)), serverScene_(new Scene(context))
{
	SubscribeToEvent(E_UPDATE, HANDLER(Server, HandleInput));
	SubscribeToEvent(E_CLIENTCONNECTED, HANDLER(Server, HandleConnection));
	Zone * temp = serverScene_->CreateChild()->CreateComponent<Zone>();
	temp->SetFogColor(Color::BLUE);
}


Server::~Server()
{
}

void Server::InitializeScene(XMLElement Scene, bool CreateOtherComponents)
{
	if (CreateOtherComponents)
	{
		serverScene_->CreateComponent<Octree>();
		serverScene_->CreateComponent<PhysicsWorld>();
	}
	serverScene_->InstantiateXML(Scene, Vector3::ZERO, Quaternion());
	File saveFile(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "SERVERSCENE.xml", FILE_WRITE);
	serverScene_->SaveXML(saveFile);
}

bool Server::InitializeServer(int port = 7346)
{
	return network_->StartServer(port);
}

void Server::HandleInput(StringHash eventType, VariantMap& eventData)
{
	Vector<SharedPtr<Connection>>& connections = network_->GetClientConnections();
	for (int i = 0; i < connections.Size(); ++i)
	{
		Connection * currentConnection = connections[i];
		PlayerController * currentController = controllernodes[currentConnection]->GetComponent<PlayerController>();
	}
}

void Server::HandleConnection(StringHash eventType, VariantMap& eventData)
{
	//This creates the player controller and adds the connection to it.
	Node * controllernode = PlayerController::CreatePlayer(Vector3::ZERO, serverScene_);
	//PlayerController * controller = controllernode->GetComponent<PlayerController>();
	Connection * connection = static_cast<Connection*>(eventData[ClientConnected::P_CONNECTION].GetPtr());
//	connection->SetScene(serverScene_);
	controllernodes[connection] = controllernode;
	VectorBuffer message;
	message.WriteUInt(controllernode->GetID());
	connection->SendMessage(31, true, true, message);
}[/code]

Edit: Just checked, it loads fine in the scene replication demo. I guess its a problem with my code then.

-------------------------

