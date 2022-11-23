vivienneanthony | 2017-01-02 01:06:10 UTC | #1

Hi

I have some quick questions.. If anyone can help. I resolved must of my other problems.


A) Problem 1 (Think I resolved this. Testing.)

What is the quickest method to set a variantmap for identity in networking?

Basically, I want to have a client make a connection to a server. The server sets a identity like anonymous and saving the connection ip, address, or whatever. 

1. If the server don't get a identity from a client in a set time. It's kicked.
2. If the server gets a identity from non-matching IP or port when the client sends authentication information. It's kicked

Killing of anonymous connections. Either the client I make or a game client to be able to work because it would at least be able to send the server needed information authentication information  before the timer is out.

B) Problem 2

If the communication is UDP for networking. If a server connects for example and the client sends a message. What's the best way on the server side to know how to send a message back with (Connection *).Sendmessage without the general broadcast.

I'm assuming I have to pass the sender down through the functions as a reference, then the actual one that input. Use the connection information and pass that to a send output.

Sounds logical?

Vivienne.


[quote]bool 	Connect (const String &address, unsigned short port, Scene *scene, const VariantMap &identity=Variant::emptyVariantMap)
 	Connect to a server using UDP protocol. Return true if connection process successfully started. 
[/quote]

-------------------------

vivienneanthony | 2017-01-02 01:06:10 UTC | #2

Hello

I made this code I think it effectively sets up a client type and time of arrival. I'm thinking of  making a update that loops through all connections to determine good or bad connections, and verified connections.

I'm not sure? This is the base attach a identity to a connection.

Vivienne

[code]
void GameEconomicServer::NewConnection(StringHash eventType, Urho3D::VariantMap& eventData)
{

    /// Get Connection
    Urho3D::Connection * newConnection = (Urho3D::Connection *) eventData[ClientConnected::P_CONNECTION].GetPtr();

    /// Output to screen
    cout << "New connection established {Clent}" << newConnection->ToString().CString() <<endl;

    /// Get currenttime
    Urho3D::Time systemtime(context_);
    unsigned int currenttime = systemtime.GetSystemTime();

    /// Get eventmap and time
    Urho3D::VariantMap NetworkClientIdentity(GetEventDataMap());

    NetworkClientIdentity[NetworkClientIdentity::NETWORK_CLIENTYPE]=Unauthenticated;
    NetworkClientIdentity[NetworkClientIdentity::NETWORK_CLIENTARRIVAL]= currenttime;

    /// Set Identity
    newConnection->SetIdentity(NetworkClientIdentity);

    return;
}[/code]

-------------------------

