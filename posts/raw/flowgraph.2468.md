1vanK | 2017-01-02 01:15:38 UTC | #1

[github.com/1vanK/Urho3DFlowGraph](https://github.com/1vanK/Urho3DFlowGraph)

I try to make simple analogue Flow Graph (Crayengine) and Blueprints (Unreal engine)
Currently no interface. All FlowNodes created in code. But already exist correct order of execute of FlowNodes and sending data from one flownode to other.

Example do 2 things:

1) Control camera by separate FlowNode (see Game.cpp)

[code]flowGraphExample_ = new FlowGraph(context_);
SharedPtr<CameraControllerFlowNode> cameraController(new CameraControllerFlowNode(context_));
// Write data to input ports of flownode. In the final it shoud be doing throught UI in Editor
cameraController->inputs_["CameraNode"]->data_ = (void*)scene_->GetChild("Camera");
cameraController->inputs_["MouseSensitivity"]->data_ = 0.1f;
flowGraphExample_->nodes_.Push(cameraController);
[/code]

2) Creating cube on start demo shows connecting of 2 flounodes.
First flounode (starter) send signal to its output port when first update.
Second flounode (cubeCreator) create cube when has signal on input port.
[code]
// Create first flownode
SharedPtr<StarterFlowNode> starter(new StarterFlowNode(context_));
flowGraphExample_->nodes_.Push(starter);

// Second flow node
SharedPtr<CubeCreatorFlowNode> cubeCreator(new CubeCreatorFlowNode(context_));
// Write scene pointer to input port
cubeCreator->inputs_["Scene"]->data_ = (void*)scene_;
flowGraphExample_->nodes_.Push(cubeCreator);

// Connection
flowGraphExample_->Connect(starter->outputs_["Start"], cubeCreator->inputs_["Create!"]);[/code]

p.s. sorry for russians comments in code :)

-------------------------

sabotage3d | 2017-01-02 01:15:38 UTC | #2

Nice! Screens please.

-------------------------

1vanK | 2017-01-02 01:15:38 UTC | #3

No UI currently

-------------------------

godan | 2017-01-02 01:15:38 UTC | #4

Nice one! I certainly think that node graphs can make exploration and prototyping much easier. Having just spent 6 months in the [url=http://iogram.ca/]depths of node graph code (written entirely in Urho)[/url], here are some immediate thoughts:

- Some kind of topological sorting of the graph is a must for getting "correct" results (I see you are doing the classic "while node inputs are not ready: continue, otherwise, solve"). 
- Checking if the user has created a cycle or no is also necessary.
- I strongly suggest copying data rather than passing by reference in the nodes. This makes things tricky for component references. I don't have a good solution to this yet either :slight_smile:
- Along with what nodes can do, a really interesting question with node graphs is how data is presented to the node. For instance, node inputs can expect either items (i.e. A + B = C), or lists (create a single mesh out of a bunch of vertices). But what happens when an "item" access input is presented with a list of inputs? Things get tricky....

Anyway, great work! Keep it going!

-------------------------

1vanK | 2017-01-02 01:15:39 UTC | #5

Thanks! Any help is welcomed to make Urho better  ;)

-------------------------

boberfly | 2017-01-02 01:15:48 UTC | #6

Hey 1vanK great work! I didn't see this before until now.

Some resources which might be cool to see, if you haven't seen these already:
[url]http://bitsquid.blogspot.ca/2010/09/visual-scripting-data-oriented-way.html[/url]

'Breadboard' is a graph/node/flowgraph scripter in the same vein:
[url]http://google.github.io/breadboard/[/url]

In my head I was thinking what would be cool is also having a lower-level flowgraph editor which can output .cpp at the end, where nodes can't connect/disconnect at runtime but rather just encompass logic to one entity and only communicates to outside entities through events (using the actor model?). This might make things a lot more optimal in performance and due to communication being decoupled from other objects, this could mutli-thread quite well. The bitsquid article argues though that the parts you'd want to mutli-thread would be iterating over all components within the one system, while the flowgraph is high-level and needs to access multiple things obtusely and would cause sync hell, but if your scene representation is double-buffered then this might not be a sync problem.

Anyways food for thought I guess, great work regardless 1vanK!

-------------------------

