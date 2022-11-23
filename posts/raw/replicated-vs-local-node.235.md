ucupumar | 2017-01-02 00:59:04 UTC | #1

Hello there Urho3D folks.  :slight_smile: 

I've been searching about replicated node on Urho documentation and Google, but I couldn't find any explanation.
What is actually the difference between local and replicated node?

-------------------------

thebluefish | 2017-01-02 00:59:04 UTC | #2

Quite simply, this is only for networking. networking is based off the client-host model, so the host has its own copy of the scene, and the clients have their own copies.

Replicated means that the node or component will be sent over the network and synchronized from host to client. So if a replicated node has a light, then all clients will see that light.

On the flip side, Local nodes and components only exist on the game that created them. A server-side node may need to keep track of information that it doesn't necessarily want to send to clients. A client may have a local node with a local camera that it uses to view the scene.

-------------------------

ucupumar | 2017-01-02 00:59:04 UTC | #3

Thanks for the answer, I'll save the other question for another thread.  :slight_smile:

-------------------------

