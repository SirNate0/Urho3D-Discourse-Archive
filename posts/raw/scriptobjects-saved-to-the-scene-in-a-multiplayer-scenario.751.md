Xardas | 2017-01-02 01:02:39 UTC | #1

Hi guys.
Basically, I would like to keep the ability to assign, create, and play ScriptObjects (which are only meant to run on the server) inside the editor and include them in the scene, without having the client load and run them when it connects to the server.

The NinjaSnowWar sample solves the problem by exclusively creating ScriptObjects from within the code, as opposed to inside the editor. Therefore when the client loads the scene, it simply won't have have the ScriptObjects (which are intended for the server only). But that way you lose the ability to edit or view a meaningful portion of the game scene within the editor. And I assume saving and loading the multiplayer scene would cause trouble, since the client now also gets any existing ScriptObjects when it loads the scene.

I would prefer to have as much control over the development of the game from within the editor as possible.

Does anybody know how I can keep this flexibility while still being able to prevent the client from loading ScriptObjects that are intended for the server?

-------------------------

weitjong | 2017-01-02 01:02:40 UTC | #2

How about by creating those nodes or components using LOCAL CreateMode as opposed to REPLICATED (the default mode)? I believe with LOCAL mode, node/component will not be replicated. They should stay on either the server side or on the client side depends on where they are being created.

-------------------------

Xardas | 2017-01-02 01:02:41 UTC | #3

Of course it works if I create them in LOCAL mode in the server code. But like I said, I want to create them in the editor, which has no idea whether they are intended for the server or client. Maybe some sort of further distinction between server and client would be helpful, not just local and replicated.

-------------------------

cadaver | 2017-01-02 01:02:41 UTC | #4

Distinguishing between server and client objects would need the scene to know which mode it is in. On the other hand, a scene should care about networking as little as possible, as it should be just a hierarchy / storage for scene nodes, so I don't particularly like the idea as a core feature. Likely you can do some your own custom filtering, for example naming objects in a certain way ("Server" or "Client" prefix, for example), and then delete objects of the wrong mode after loading the scene.

Another way is to make all script components replicated but make them do nothing on the side (client or server) they're not intended for.

-------------------------

Xardas | 2017-01-02 01:02:42 UTC | #5

Ok, these are all good ideas, but would that still work in the editor?
For example, I have attached a rotation script to the sun's node (a replicated node with a directional light). And when I press play in the editor, I can see the lighting change in real time. I'm using attribute animation with keyframes to rotate (and also some other things, like changing the brightness) the node.
If the client loads that script and deletes it, the attribute animation will persist. Of course, I could remove it in Stop(), but I tried that and I had to use objectAnimation (since there is no RemoveAttributeAnimation function), and for some reason the node's objectAnimation was null in Stop() when I tried to access it...

Regarding you last suggestion, I suppose you mean I should, for example, add a bool member to the ScriptObject class, and only execute the ScriptObject's code if it was not toggled (remember I need the editor to be able to execute it). And the client code should search for all of those ScriptObjects in the scene and toggle the bool value, and not run the code. But there the problem is, the Start() function has already run before I could toggle the value!

But maybe I'm misunderstanding how the editor works when you press play? Maybe I don't even have to use the Start() function in my ScriptObjects for them to execute inside the editor?

-------------------------

