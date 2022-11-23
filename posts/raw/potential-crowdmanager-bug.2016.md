Deveiss | 2017-01-02 01:12:18 UTC | #1

Copied from the IRC, let me know if I need more details or code snippets.

[code]<Deveiss> So, in my code, I call several times GetScene()->GetComponent<CrowdManager>(), and then call SetCrowdTarget or DrawDebugGeometry, etc.
<Deveiss> The weird thing? It doesn't work. At least, not like you'd expect.
<Deveiss> If I do everything as I should, I can't control the units, and the debug geometry doesn't even show them as crowd agents. I've got no control.
<Deveiss> If I DON'T add a CrowdManager component to the scene node, then not only do the units show as crowd agents in the debug renderer, but if I call GetComponent<CrowdManager>()->SetCrowdTarget(), the units actually move to where they're supposed to go!
<Deveiss> I'm beyond confused right now.[/code]

-------------------------

JTippetts | 2017-01-02 01:12:20 UTC | #2

Without seeing code, it's hard to say. My suspicion is that you already have a crowd manager in place, and when you create a new one, that new one stays empty because everything is already added to the existing one. But when you call GetComponent, it's getting the most recently created one rather than the one already in place. Other than that theory, without seeing code it's hard to tell.

-------------------------

Deveiss | 2017-01-02 01:12:21 UTC | #3

It appears that the DynamicNavigationMesh must not be empty when the component is created. When I was having the issue, I created the Octree, Camera, Lights, and DynamicNavigationMesh. I then built the NavMesh with nothing in it. Then, I added the CrowdManager. When a player joined and it was time to actually build the world. I add a plane and some boxes, and then rebuilt the NavMesh. However, I don't touch the CrowdManager again. Then, the player's units are created, include a CrowdAgent component.

In the first setup, the CrowdManager was initialized with an empty NavMesh, which resulted in none of the CrowdAgents being controllable, or even recognized.

When I (purely out of frustration) removed the line creating the CrowdManager component in the root scene node when the scene is first created, the game actually worked as expected. Through the VS debugger, I found out that my first call to CreateComponent<CrowdAgent> when the connected player's ships are created actually creates a CrowdManager for the scene if one does not already exist. The CrowdManager was then initialized after the NavMesh was populated, however without my explicit knowledge.

Moving the creation of the CrowdManager component to  after the second time the NavMesh is built works perfectly, while still allowing me to pass the CrowdManager parameters on initialization.

-------------------------

