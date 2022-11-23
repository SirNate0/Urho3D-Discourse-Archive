vivienneanthony | 2017-01-02 01:06:26 UTC | #1

Hello

I'm trying to get the networking setup but getting this message. Do anybody know whats wrong?

Vivienne

[b][Thu Aug 13 10:02:03 2015] ERROR: Can not send message with reserved ID[/b]


Info: Database Maps table found.
[code]Info: Loading network configuration .
Info: Loading network configuration failed. Using 127.0.0.1 and port 3632 as default.
Headless Server Model 
Programmer Vivienne Anthony
 
Info : Starting networking on localhost(127.0.0.1)
[Thu Aug 13 10:01:37 2015] INFO: Started server on port 3632
[Info]Starting scene.
Debug: Creating trader node with parameters (P'tiauc,0,0,0) 
Debug: Creating trader node with parameters (Agtika,0,0,0) 
Debug: Creating trader node with parameters (Shyeth,0,0,0) 
Debug: Creating trader node with parameters (Itis,0,0,0) 
Debug: Pusing new trader to market subsystem with parameters (Orin Open,0,0,0,100) 
Debug: Pusing new trader to market subsystem with parameters (Suzu Exchange,0,1,0,0) 
Debug: Pusing new trader to market subsystem with parameters (ArSoft Corp Black,0,2,0,0) 

Enter Command >> [Thu Aug 13 10:02:00 2015] INFO: Client 127.0.0.1:50661 connected
Network: New connection established Client(127.0.0.1:50661)
[Thu Aug 13 10:02:00 2015] INFO: Client 127.0.0.1:50661 disconnected
[Thu Aug 13 10:02:03 2015] INFO: Client 127.0.0.1:44824 connected
Network: New connection established Client(127.0.0.1:44824)
[Thu Aug 13 10:02:03 2015] ERROR: Can not send message with reserved ID

Network: SentNetworkMessage ("aisha") to (127.0.0.1:44824)
Network: Poll (127.0.0.1:44824 Type 1 Arrival 660479152)
[/code]

Related Functions

[code]void GameEconomicServer::SendNetworkMessage(NetworkMessageTypes NetworkMessageType, bool flag1, bool flag2, String MessageText, Urho3D::Connection * SenderTo)
{

    /// A VectorBuffer object is convenient for constructing a message to send
    VectorBuffer msg;
    msg.WriteString(MessageText);

 	/// Get current system time
    Urho3D::Time SystemTime(context_);
    unsigned int currentTime = SystemTime.GetSystemTime();

    SenderTo->SendMessage(NetworkMessageType,flag1,flag2, msg, currentTime);

    cout << "\r\nNetwork: SentNetworkMessage (\"" << MessageText.CString() <<"\") to (" << SenderTo->ToString().CString() <<")" << endl;

    return;
}
void GameEconomicServer::HandleNetworkMessage(StringHash eventType, Urho3D::VariantMap& eventData)
{
    Network* network = GetSubsystem<Network>();

    using namespace NetworkMessage;

    int msgID = eventData[P_MESSAGEID].GetInt();

    /// Urho related variables
    String PromptInput;
    Vector<String> SplitPromptInput;

    if (msgID == 999)
    {
        const PODVector<unsigned char>& data = eventData[P_DATA].GetBuffer();
        // Use a MemoryBuffer to read the message data so that there is no unnecessary copying
        MemoryBuffer msg(data);


        String text = msg.ReadString();

        Urho3D::Connection* sender = static_cast<Urho3D::Connection*>(eventData[P_CONNECTION].GetPtr());

        /// parse command
        SplitPromptInput = ParseCommand(text.Trimmed());

        /// First command
        String FirstCommand = SplitPromptInput[0];

        /// Check sisze for arguments
        if(SplitPromptInput.Size()>0)
        {
            /// Remove first element since its not needed
            SplitPromptInput.Erase(0);
        }

        /// ExecuteCommand
        ExecuteCommand(FirstCommand, SplitPromptInput, sender);
    }
    if (msgID == NetMessageAuthenticateSend)
    {
        const PODVector<unsigned char>& data = eventData[P_DATA].GetBuffer();
        // Use a MemoryBuffer to read the message data so that there is no unnecessary copying
        MemoryBuffer msg(data);

        String text = msg.ReadString();

        /// Get Sender
        Urho3D::Connection* sender = static_cast<Urho3D::Connection*>(eventData[P_CONNECTION].GetPtr());

        /// Parse received message
        SplitPromptInput = ParseCommand(text.Trimmed());

        /// Verify password - case sensitive
        bool authorized = VerifyIdentityDB(DBAccount, SplitPromptInput.At(0),SplitPromptInput.At(1));

        cout << "Client to authorize  " << SplitPromptInput.At(0).CString() << " " <<SplitPromptInput.At(1).CString() << " with server response " << authorized << endl;

        /// Send a response for authorized user or not
        if(authorized)
        {
            /// Send a message saying authorized
            SendNetworkMessage(NetMessageAuthenticatedApproved,true,true,"",sender);
        }else
        {
            /// Send a message saying denied
            SendNetworkMessage(NetMessageAuthenticatedDenied,true,true,"",sender);
        }
    }
}
[/code]

-------------------------

thebluefish | 2017-01-02 01:06:26 UTC | #2

What message ID are you trying to use?

[url=http://urho3d.github.io/documentation/1.4/_network.html]Per the documentation[/url]:

[quote]The first ID you can use for custom messages is 22 (lower ID's are either reserved for kNet's or the Network subsystem's internal use.)[/quote]

-------------------------

vivienneanthony | 2017-01-02 01:06:26 UTC | #3

[quote="thebluefish"]What message ID are you trying to use?

[url=http://urho3d.github.io/documentation/1.4/_network.html]Per the documentation[/url]:

[quote]The first ID you can use for custom messages is 22 (lower ID's are either reserved for kNet's or the Network subsystem's internal use.)[/quote][/quote]

Its higher the 22 but I can change it easy

-------------------------

cadaver | 2017-01-02 01:06:26 UTC | #4

Note also that ID's higher than 0x3ffffffe are kNet reserved.

-------------------------

vivienneanthony | 2017-01-02 01:06:27 UTC | #5

[quote="cadaver"]Note also that ID's higher than 0x3ffffffe are kNet reserved.[/quote]

Thanks. Worked like a charm.

-------------------------

