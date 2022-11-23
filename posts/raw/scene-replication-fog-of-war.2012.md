Deveiss | 2017-01-02 01:12:16 UTC | #1

Is it possible to implement a sort of "fog of war" with Urho's stock scene replication? Where their client is only sent data about nodes which that they're supposed to have knowledge of? In some strategy games, you can only see real-time information of the map in areas that you're units have "vision" in. It would be easy in the client to say "alright, do I have units that can see this part of the map? No? Then disregard any data we get about enemy movements in this area." However, sending the entire game state to all clients opens the door to severe cheating. So...

Assume one server and two clients, where the server receives commands from both clients, who can order their units to move, attack, or idle. The server then takes those orders and executes them. All of the movement of nodes and simulation of damage is done on the server. Is there a way to relay the outcomes back to only those nodes that have "vision" on those units? There currently isn't any simulation done on the client, the client just sends events and receives the current game state to display.

On the IRC it was suggested that I look into the MarkNetworkUpdate function, however this seems to be applied to replicated nodes automatically by the engine, and appears to not be able to discriminate between connections. Ideally, I'd be able to set an owner for each node, and then when the time comes to update each client, check to see what nodes they have ownership of, and only send updates for other units within their own unit's circle of vision.

Bonus question: Are shader parameters replicated? Because modifying the diffusion color on the server appears to have no effect on the client.

-------------------------

cadaver | 2017-01-02 01:12:17 UTC | #2

Realistically I believe you have to modify the engine. Check the function Connection::ProcessExistingNode() where it does a simple interest management priority accumulation check using the NetworkPriority component, and just returns if the component says the node shouldn't be replicated yet. You could for example insert some kind of interceptor callback, or make NetworkPriority subclassable. If you do it cleanly and it doesn't hurt performance when not used, a pull request is welcome.

Shader parameters aren't replicated. Look either into custom messaging or storing parameters into node user vars, which do replicate, and apply from the node var to the material.

-------------------------

Deveiss | 2017-01-02 01:12:17 UTC | #3

[quote="cadaver"]You could for example insert some kind of interceptor callback, or make NetworkPriority subclassable. If you do it cleanly and it doesn't hurt performance when not used, a pull request is welcome.[/quote]
Could be a fun experiment. I'll play around with it, see what I can do.

[quote="cadaver"]Shader parameters aren't replicated. Look either into custom messaging or storing parameters into node user vars, which do replicate, and apply from the node var to the material.[/quote]
Thank you. Before getting confirmation that this was how I'd have to do it, I added a networked Color attribute to my PlayerUnit component, and I'm working on a way to notify the clients when a new unit joins the scene or changes color, so they know to clone the material and apply the color change.

-------------------------

