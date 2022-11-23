TheComet | 2019-07-02 21:42:53 UTC | #1

I'm new to Urho3D's networking code, so maybe I'm missing something obvious. Is there a way to tell the client why they were disconnected from the server?

Consider:

```cpp
void ServerUserRegistry::HandleClientIdentity(StringHash eventType, VariantMap& eventData)
{
    using namespace ClientIdentity;

    Connection* connection = static_cast<Connection*>(eventData[P_CONNECTION].GetPtr());
    String username = connection->GetIdentity()["Username"].GetString();

    // Username might be empty (or not exist)
    if (username.Empty())
    {
        URHO3D_LOGERROR("Empty username, rejecting");
        eventData[P_ALLOW] = false;

        connection->SendRemoteEvent(E_INVALIDUSERNAME, true);

        return;
    }
}
```

The client never receives E_INVALIDUSERNAME because it is disconnected before the event can effectively be transmitted.

What is the correct way to inform the client of an error message before they get disconnected?

-------------------------

Modanung | 2019-07-03 01:58:45 UTC | #2

Could `SendMessage` work? An error code would do.

-------------------------

TheComet | 2019-07-03 04:28:32 UTC | #3

That works. I don't know if I trust that the message is guaranteed to arrive or not before disconnecting, though, but it works for now.

-------------------------

TheComet | 2019-07-03 04:59:12 UTC | #4

Update: SendMessage() doesn't work

-------------------------

Miegamicis | 2019-07-03 07:50:12 UTC | #5

Just looking at the network code how it's done now I see that by setting `P_ALLOW` data client is immediately disconnected. So instead I wouldn't disconnect the user right away, I would send him a message and disconnect him manually after specific time has passed (maybe 100ms would do) just so there is enough time that the client can receive the message. To make it even better I would send the message explaining what wen't wrong and allow the client to disconnect by himself, but for the sake of safety would still set a delayed disconnect on the server just in case the client tries to do something silly after receiving refusal message.

-------------------------

Miegamicis | 2019-07-03 07:53:39 UTC | #6

One more thing that would be even better if we added a possible way to send a error/disconnect reason code when the server calls disconnect on a client (in the engine itself).

-------------------------

Leith | 2019-07-03 09:25:23 UTC | #7

Hey, are we talking about missing functionality? This could give me an excuse to get my hands dirty with Urho with respect to networking. Ultimately, Urho is using UDP based network model(s), so there never really was a proper connection, and the most common "Reason" we will be told, is "timed out".

-------------------------

Miegamicis | 2019-07-03 11:41:09 UTC | #8

Yes, this would be a new functionality but should be fairly easy to implement but of course, we can't always guarantee that the message will be retrieved by the client and I think that's ok in this case.

-------------------------

Leith | 2019-07-03 11:43:23 UTC | #9

Actually we CAN guarantee delivery, in all the "normal" cases of disconnection... our UDP tunnel is not really disconnected, because it was never connected, so we can certainly send a last message before our termination request.
But we can't in the case of unexpected disconnection, due to timeout as far as we are concerned.

-------------------------

