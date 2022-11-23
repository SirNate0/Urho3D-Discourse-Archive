TheComet | 2018-05-24 21:08:09 UTC | #1

Is it possible to have a single server application manage multiple scenes, and select which client should synchronize with which scene?

Here is a diagram showing what I want:

![1|649x309](upload://7776HuylGUw8bRERKDFb7v0XDTp.png)

-------------------------

dev4fun | 2018-05-24 23:08:07 UTC | #2

I dont know if have something like this natively from Urho... 

Im doing a MMORPG and I have a system with multiple maps (firstly I thought to use multiple scenes), so the way that Im doing its use one scene for server and one scene for client and handle this (what data map i should send to player etc) with my own code.

-------------------------

TheComet | 2018-05-25 09:55:53 UTC | #3

What I find confusing is how does Urho know about the scene server-side? On the client it makes sense, you pass the scene to Network::Connect, but on the server, Network::StartServer doesn't take a scene as an argument...

-------------------------

Modanung | 2018-05-25 17:30:40 UTC | #4

@TheComet You can call `Connection::SetScene(Scene*)` serverside on `ClientConnected::P_CONNECTION`. I think that should do the trick.

EDIT: Which makes me wonder if this is also _the_ way to deal with fog-of-warlike situations?

-------------------------

