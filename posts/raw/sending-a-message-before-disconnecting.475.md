thebluefish | 2017-01-02 01:00:44 UTC | #1

I want to enforce certain parameters via the ClientIdentity event, such as a username/password or other potential authentication parameters.

Currently I do the following:
[code]
bool allow = eventData[P_ALLOW].GetBool();

// Do some checking here

eventData[P_ALLOW] = allow;
[/code]

Which works fine for simply not allowing the connection. However what should I do if I want to send a disconnect reason to the client? Currently my work-around is by setting an identity parameter, and *not* disconnecting the connection. As follows:
[code]
if (allow)
	{
		eventData[CON_AUTHENTICATED] = true;
		
		// Assign to lobby
		RoomHandler* roomHandler = GetSubsystem<RoomHandler>();
		roomHandler->AssignRoom(connection, R_LOBBY);
	}
	else
	{
		eventData[CON_AUTHENTICATED] = false;
	}
[/code]

However this means that I have to check if the connection is authenticated on every RemoteEvent in order to ensure that a client doesn't try to send RemoteEvents without being authenticated. One option that I've thought about using would be:

[code]
connection->Disconnect(1000); // disconnects client after 1 second
[/code]

However the client technically could still send a RemoteEvent in this time, and AFAIK there's no guarantee that the client will get the server message before the connection terminates.

What would be the best way to handle this?

-------------------------

