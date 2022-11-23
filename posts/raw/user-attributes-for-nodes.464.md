cin | 2017-01-02 01:00:38 UTC | #1

I need to add custom info for nodes on server and lets clients read it. How I can do this?

-------------------------

cadaver | 2017-01-02 01:00:38 UTC | #2

The node's custom vars VariantMap can be used for this. Node::SetVar() & Node::GetVar(). It's not a terribly efficient mechanism, because whenever any var in a node changes, the whole VariantMap is transmitted.

-------------------------

cin | 2017-01-02 01:00:39 UTC | #3

Client send command to server ?Create object Cube?. Server create object and send ID to client. Client find this object and set variable to it. When client reconnect to server and try get user variable, but it missing.

-------------------------

cadaver | 2017-01-02 01:00:39 UTC | #4

Scene replication flows only from server to client, which means that if you set a variable on a client it remains on that client only. You can make your own command mechanism with network messages or remote events (similar like you already have for object creation), which will instruct the server to set the var, at which point it gets copied to all clients.

-------------------------

thebluefish | 2017-01-02 01:00:39 UTC | #5

Is it possible to have vars -not- get replicated, or is that only available by setting vars on a local node/component?

-------------------------

cadaver | 2017-01-02 01:00:39 UTC | #6

The vars are a single replicated attribute, so it's not possible for a replicated node. You could either create a local child node for the vars, or create a local component which stores the data you don't want replicated.

-------------------------

