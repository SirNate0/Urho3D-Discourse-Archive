Leith | 2019-06-12 06:01:57 UTC | #1

It's been raining all day and night here.
I decided to spend some time playing with lezak's BehaviorTree codebase.
After doing that for some time, I decided to find a decent editor I could use to create my trees, rather than using hardcode or handcrafting xml/json.

I came across "owl-bt" today. <https://www.npmjs.com/package/owl-bt>
I've fallen in love with its simple approach and engine-agnostic design.
Super easy to add new custom node types and even declare custom data types...
Saves to json. Hotloads your changes. Runs in your web browser.

I can see myself putting together code to load that json into lezak's codebase, which is also highly flexible, and seems to be well thought out, other than one small issue... it's a classical implementation of BT, and so there is no thought to data oriented design or re-use of existing subtrees...

Behaviour tree nodes that contain dynamic data are a no-no.... (nodes that use constant or statically shared data are ok)...
If we do that, and by that, I mean store any dynamic values in our nodes, then we can't easily reference entire subtrees at runtime, which means that every actor that needs a BT has to have a whole unique copy of said tree instantiated at runtime.

A perfect example is a repeater node, that holds a counter. We need to store that data outside the node, and pass it in our calling context, then we are "sweet".

Just my two cents worth.

-------------------------

johnnycable | 2019-06-12 14:50:11 UTC | #2

Interesting find. I was searching for s.t. like it without the hassle of putting together an editor... Thx

-------------------------

jmiller | 2019-06-12 16:58:05 UTC | #3

[quote="Leith, post:1, topic:5228"]
lezak’s codebase
[/quote]

https://discourse.urho3d.io/t/behavior-tree-for-urho3d/2947

-- referencebot

-------------------------

Leith | 2019-06-13 02:25:51 UTC | #4

Have started writing code to load the json saved by owl-bt
I thought I'd mention a couple of things I've noticed so far:

1. Any node can have a Name - but the editor does not display them or let you set them.
2. Node properties are not serialized if they bear the value we specified to be default (similar to Urho attributes).
3. Manual editing of the owl-bt.json file usually (but not always) is hotloaded by the editor.
4. Manual editing of mytree.json file is never hotloaded (refresh your browser to reload the tree)

I am still very happy with this editor because it is so easy to adapt to your custom bt node types.

-------------------------

Leith | 2019-06-13 06:05:14 UTC | #5

Since I have access to class names, I've decided to let the parser attempt to construct node instances by name via class object factory method. Since I use scripting little if at all, I've been searching for a while for a good reason to register object factories, in a context where I could take advantage of name-based instantiation. It's a shame we can't register factory functions with arguments.

-------------------------

Leith | 2019-06-13 06:46:51 UTC | #6

What is the proper way to cast a shared pointer in Urho? If I am using factory instantiation, then I get a SharedPtr<Object>, which is not really what my object type is.

-------------------------

Leith | 2019-06-13 07:08:04 UTC | #7

@johnnycable, yeah, "something like it" was what I needed too - something that was not dedicated to an existing codebase or engine, and was easily configurable for my nefarious purposes.
I certainly wanted to avoid writing a full fledged editor, though there is some sourcecode floating around that I could have used to do so - it's just not a good use of my time, for my project, to create custom editor solutions, when I can just rely on established stuff like xml and json, and deal with that at my end.

-------------------------

jmiller | 2019-06-13 13:54:24 UTC | #8

[quote="Leith, post:6, topic:5228"]
What is the proper way to cast a shared pointer in Urho?
[/quote]

What I see in Urho (and what I often do) is cast the raw pointer. `SharedPtr::Get()` et al.

-------------------------

Leith | 2019-06-14 04:55:06 UTC | #9

[WARNING: WORKAROUND HACK CODE AHEAD! Also - this code is not complete...]

What I was looking for was Detach()...

Urho's object factory implementation returns a shared pointer, but deep in my recursive json parser it was not necessary or even desirable to have my object pointers wrapped at all, let alone by the insidious shared pointer (hey - I DO use them, but I want to decide when and where something gets wrapped in one of those...)

I did need to perform an upcast from Urho3D::Object to my baseclass prior to calling Detach in order to ensure I was returned the correct object type.
Also, I think I'll rename my classes to avoid the following ugly name-mangling... owl-bt calls its classes "Sequence", "Selector" etc., while lezak's classes are called "SequenceNode", "SelectorNode", and so on - and its the C++ class name that matters when instantiating class objects by name via factory.

[code]
    BehaviorTreeNode* BehaviorTree::ParseNodeFromJSON(const Urho3D::JSONValue& jvalue){
        String nodetype =jvalue.Get("type").GetString();
        String nodename =jvalue.Get("name").GetString();

        /// Instantiate the node by typename
        SharedPtr<BehaviorTreeNode> newNode(context_->CreateObject(nodetype+"Node")->Cast<BehaviorTreeNode>());

        /// If that failed, we probably forgot to register a node class with Urho!
        if(newNode==nullptr){
            URHO3D_LOGERROR("JSON PARSER - UNHANDLED NODE TYPE: "+nodetype);
            return nullptr;
        }

        /// Process node properties (if any)
        Urho3D::JSONArray props=jvalue.Get("properties").GetArray();
        for(auto it=props.Begin(); it!=props.End(); it++)
            ParseNodePropertyFromJSON(*it);

        /// Process node decorators (if any)
        Urho3D::JSONArray decorators=jvalue.Get("decorators").GetArray();
        for(auto it=decorators.Begin(); it!=decorators.End(); it++)
            ParseNodeDecoratorFromJSON(*it);

        /// If the node we just created is a Composite type?
        CompositeNode* n=newNode->Cast<CompositeNode>();
        if(n){
            /// Call initializer method on composite type
            n->OnFactoryConstruct(this, false, nodename);

            /// Process child nodes (only Composite Nodes should have children!)
            Urho3D::JSONArray children=jvalue.Get("childNodes").GetArray();
            for(auto it=children.Begin(); it!=children.End(); it++)
                n->AddChild(ParseNodeFromJSON(*it));
        }
        else
        {
            /// TODO:
            /// Node is some kind of Leaf node...
            /// Set a breakpoint here!
            int x=0;
        }

        /// HACK:
        /// Node Factory Function gave us a SharedPtr, but we did not really want one.
        /// We know there's no other "owners" of the shared pointer...
        /// Let's detach the raw pointer from the shared pointer :)
        return newNode.Detach();

    }
[/code]

My code now returns raw pointers to the caller, who is in turn responsible for storing them in smart pointer objects. This is somewhat better than trying to pass / return shared pointers across call boundaries, and all the needless construction, copying and destruction that involves.
It would be nice if the Context class / Factory implementation provided a constructor that returned a raw pointer... is there something I missed?

-------------------------

Leith | 2019-06-14 04:33:24 UTC | #10

The reason that I have chosen to use factory instantiation is just this: once written, the same parser/loader code will still work, even if we register new node class types to Urho, with no further changes needed in the loader (99 percent of the time).

-------------------------

Leith | 2019-06-15 06:14:38 UTC | #11

I tried to get my JSON parser to register new class attributes - this turned out to be a fizzer for several reasons, but I found an amicable workaround in the UIElement class - it implements a serializable attribute (variantmap type) called "Variables" (vars_ membername). I could easily add such an attribute to my base BT node class, so ANY node can potentially own an arbitrary list of properties / named and typed variables which would serialize easily.
I realized quickly that I could just add "node properties" as typed variants in a serialized map - this way, my classes did not need to express any details pertaining to properties.
Now dealing with some small issues involving an incomplete typemapping between JSON and Urho.

-------------------------

Leith | 2019-06-16 08:53:25 UTC | #12

There are a bunch of "gotchas" when working with lezak's behaviortree code.
I'll try to put together some kind of documentation, as the owl-bt editor has very few limitations, while lezak's code has a number of limitations where it comes to tree topology and execution.

One example is that the (owl-bt) editor will let you add multiple Decorators to any node in the tree, while the current codebase only allows one decorator per node.

It took me most of a day to completely implement and test the following node types:

Composites: Selector, Sequence, Parallel
Actions: LogAction, WaitStepsAction
Decorators: Invert, Loop, Success, Failure, IsBlackboardValueSet, IsBlackboardValueEqual

I found testing difficult, mainly because my understanding of how a BT works is fairly different to this (stack-based) re-entrant implementation. I am trying to cope, docs on the way ("it's a man page")

-------------------------

Leith | 2019-06-18 10:25:45 UTC | #13

The first "gotcha" is that lezak's BT nodes only support ONE Decorator. If you make more in the editor, they will not be loaded by my code (room to address this).

The second "gotcha" is that Decorators are only executed by nodes whose child reported that they completed (ie, not running).

The third, is that there are corner cases where Decorators won't run at all.
I will try to elaborate on this as my understanding increases.

My next step is to implement something missing from lezak's codebase: Service nodes... these basically execute a script... my first real foray into a reason to use script at all, coming right up..

Since decorators only "run late", I may also introduce the notion of "guard node" - where one decorator node may prevent the execution of the node to which it is attached.

This is not immediately a good fit with the owl-bt editor, but I can work with it, given the flexibility in the editor, and possibly petition the author to extend their work.

-------------------------

Leith | 2019-06-19 06:46:04 UTC | #14

Here's a screenshot showing some customizing of Owl-BT ... I can load and run this behaviortree, not that it does much yet - it's just a testing ground to help me verify my custom node implementations and to help me to perform sanity-checking.
![OwlBT|690x374](upload://4O10SrVXY5SopnpZe3klTUDYQSw.png)

Most nodes can be annotated with comments, and composite nodes support random or ordered child execution. Owl-bt has no support for testing tree logic inside the editor, but I've never seen a BT editor that did - it has no idea how our implementation works!

My loader code attempts to automatically deal with new node types and node properties, which makes life pretty easy for the coder to support new node types should new requirements emerge.

-------------------------

Leith | 2019-06-19 06:53:59 UTC | #15

I've implemented "SetVariable" and "IsSetVariable" as "action nodes" (aka leaf nodes).

SetVariable stores a named and typed value in the context of the owner tree (for now).
Currently supported types are string, number (evaluates to a float) or bool.
Unsupported types generate suitable debug spew.

IsSetVariable just tells us if some named variable has been set at all.

Action nodes can return Success, Failure or Running.
My "LogAction" node always returns Success - unless explicitly decorated to return something else.

"SetVariable" likewise, always succeeds, unless decorated.

But "IsSetVariable" can return Success (variable exists) or Failure (no such variable).

The variables of which I speak currently reside in a VariantMap (aka Blackboard) held by the BehaviorTree container object, but more correctly belong in a visiting Agent, or at least a Calling Context. These are not global variables, they represent the "knowledge" of the AI Agent who is the chief subject of the tree execution.

-------------------------

Leith | 2019-06-20 07:23:46 UTC | #16

Today I extended lezak's BT codebase to support Subtree recursion. The changes should allow us to do two important things:
- be able to construct complex behaviors by referencing more simple ones ... building blocks
- be able to share one behaviortree instance across any number of actors ... persistent data is not stored in the tree

The concept is that we have a special kind of Leaf node which holds a weak reference to another behaviortree, and acts as a proxy by executing the subtree and returning the result of the subtree execution to the parent node (of the proxy node) in the usual way (for behavior tree nodes).
One instance of such a node in a behaviortree is representative of an entire nested copy of some other tree. Of course, no such cloning of subtrees is actually done... instead, we can rely on a little logic: the execution-sensitive variables owned by the nodes in one subtree are safe for the entire execution of that subtree - and if we prevent subtree nesting, then they are safe across subtree executions, as they exist in a single "frame of tree execution". In order to deliberately share data across subtrees, I chose a Blackboard approach...

I began by changing the return value of BehaviorTree::Process() to return the BTNodeState value from the root node execution all the way back to the caller of Process method.
This would allow a subtree to return its result to a caller node in a parent tree.

Secondly, I introduced the notion of a BehaviorTreeContext object which is passed down during subtree recursion - this acts as a "Blackboard" that nodes can read and write to, which contextually is "owned by the actor who is the subject of tree execution". This mechanism allows data variables to persist and be shared by multiple subtrees, while remaining the property of the caller, and not the property of any individual node or subtree.

Thirdly, I added a guard stack to the BTContext object, so that it can remember which subtrees it has previously recursed during a single execution of the entire tree, and will trigger an error if an attempt is made to recurse a previously-visited subtree (to prevent the possibility of infinite recursion).

Fourthly, I added a static HashMap<String, SharedPtr<BehaviorTree>> BehaviorTree::SubTreeLibrary and static methods to add your loaded behaviortree objects to the library, and to locate existing subtrees by name.
This mechanism will allow the JSON loader to locate previously-loaded behaviors by name alone.

The code all compiles and looks to be complete and logically sound... I'll test it soon, need to modify owl-bt to support my new Subtree proxy node.

[EDIT]
All tested and working!
I'm loading two behaviortrees, and storing them as named behaviors. One of these two trees represents the root, and it contains a proxy node that references the other subtree. When that proxy node is reached, it executes the child tree, then returns the result from the child tree.

I've only tested a single depth-level of subtree recursion, but it works fine, and I can't imagine why it would fail at deeper levels (ie, subtrees referencing even finer subtrees).
You just need to be mindful of a few things (time to write some docs?) - some are: subtrees must be loaded before attempting to load any higher behavior that references them, and we need to think more carefully about how the return value from a subtree is interpreted by the parent tree.

From now on, I don't have to deal with large, sprawling, complex trees in the owl-bt editor - I can concentrate on one small sub-behavior at a time.

-------------------------

Leith | 2019-06-20 07:17:01 UTC | #17

Here's what the code looks like now for proxy-execution of a Subtree... We can see the implementation of the new signature for the execution entrypoint ... BTNodeState BehaviorTree::Process(float, BehaviorTreeContext*)

[code]
    BTNodeState SubTree::HandleStep(){
        if(tree_->btContext_==nullptr)
        {
            URHO3D_LOGERROR("Behavior Subtree cannot execute with no Context!");
            return NS_ERROR;
        }
        return subTreeRef_->Process(tree_->timeStep_, tree_->btContext_);

    }
[/code]

It is vital to note the use of a cascading execution context argument, this is our "persistent data container, per calling agent". It's the blackboard which allows us to share both subtrees and entire trees across multiple game entities, and it also implements my safety code to prevent problems associated with subtree nesting.

Each behaviortree has members to hold the calling BTContext and the deltatime - these values are set when a subtree is about to be processed, and so become available to all nodes in that tree, including those belonging to subtrees, since these values are passed from parent tree to child subtree in the Process() entrypoint call. These values are NOT passed during node-stepping within a single subtree, including the root subtree - they are simply retained and shared for the duration of the frame of execution.

Here's what the class definition looks like for SubTree node.
[code]
    class SubTree:public LeafNode
    {
        /// All BehaviorTree nodes derive from Urho3D::Serializable
        /// The reason is that we support full serialization (to file) of node-local properties.
        URHO3D_OBJECT(SubTree, LeafNode)
        
    public:
    
        /// Registers this class with Urho3D (required for factory-based instantiation)
        static void RegisterObject(Context* context);

        /// Called by JSON Loader to "unpack Properties" associated with this class
        /// The only property for this Node that matters is the SubTreeName string.
        /// It will never change again for this object instance, so this is a good place for Loader to set that member
        virtual void OnFactoryConstruct();

        /// Factory Constructor: This is what the JSON Loader uses
        SubTree(Context*);

        /// Set this node's subtree reference to the given BehaviorTree instance
        void SetSubTree(BehaviorTree* subtree){ subTreeRef_ = subtree; }

        /// Set this node's subtree reference from Behavior Library, according to the subTreeName_ member
        void SetSubTree();

    protected:
        /// We redefine the execution behavior for this node.
        /// Basically we just execute this node's subtree reference, and return what it gives back to us.
        virtual BTNodeState HandleStep() override;

        /// Set by JSON Loader
        /// Unique Name of the Behavior that this node will attempt to execute
        String subTreeName_;
        
        /// See SetSubTree methods
        /// Holds reference to a BehaviorTree
        WeakPtr<BehaviorTree> subTreeRef_;

    };
[/code]
Love to hear your thoughts, though it's probably ready to upload somewhere for proper evaluation.

-------------------------

Leith | 2019-06-20 07:29:08 UTC | #18

For the sake of completion, and sorry if this is a lot to take in!
[code]
    /// Execution Context for processing a BehaviorTree:
    /// The calling AI Agent should implement this class!
    ///
    class BehaviorTreeContext{
    public:
        /// Used to store variables during tree execution
        VariantMap blackboard_;

        /// Used to guard against subtree re-entrancy (infinite recursion)
        /// BehaviorTree::Process() is responsible for this safety mechanism
        Vector<WeakPtr<BehaviorTree>> subtreeStack_;
    };
[/code]

Here is the per-game-actor container we hand in when we execute our root ai behavior.
It has two members: one is the blackboard of shared variables for this agent, representing what this agent "knows" about the game world, and the other is a guard stack, used to stop bad things happening due to re-entrancy.

This guy should probably be a struct, but thus far, my code is still only in the testing phase, so I am not too worried about the fact there's no code in this class.

-------------------------

Leith | 2019-06-20 09:36:50 UTC | #19

Sorry for belated thanks, your reply
 helped me get back on track

-------------------------

Leith | 2019-06-20 14:46:11 UTC | #20

For anyone who is experimenting with owl-bt, or is interested in doing so, here is the json I use to modify the editor for my purposes so far. Maybe you will see something in here you can use too.
This replaces the "owl-bt.json" configuration file... you'll figure it out if you haven't already :)

[code]
{
    "nodes": [
        {
            "name": "Selector",
            "icon": "question",
            "isComposite": true,
            "description": "{{Name}}: isRandom = {{isRandom}}",
            "properties": [
                {
                    "name": "isRandom",
                    "type": "bool",
                    "value": false,
                    "default":false
                },
                {
                    "name": "Name",
                    "value":"SelectorNode",
                    "default":"[nameless]"
                }
            ]

        },
        {
            "name": "Sequence",
            "icon": "arrow-right",
            "isComposite": true,
            "description": "{{Name}}: isRandom = {{isRandom}}",
            "properties": [
                {
                    "name": "isRandom",
                    "type": "bool",
                    "value": false,
                    "default":false
                },
                {
                    "name": "Name",
                    "value":"SequenceNode",
                    "default":"[nameless]"
                }
            ]
        },
        {
            "name": "Something",
            "icon": "question",
            "isComposite":true,
            "description": "Is blackboard value \"{{Field}}\" set",
            "properties": [
                {
                    "name": "Field",
                    "type": "string",
                    "default":"set me"
                }
            ]
        },{
            "name": "LogAction",
            "icon": "arrow-up",
            "isComposite": false,
            "description": "Log << \"{{Text}}\"",
            "properties": [
                {
                    "name": "Text",
                    "type": "string",
                    "default":"set me",
                    "value": "something"
                }
            ]
        },
        {
            "name": "WaitStepsAction",
            "icon": "arrow-",
            "isComposite":false,
            "description" : "Wait for \"{{Counter}}\" ticks",
            "properties": [
                {
                    "name": "Counter",
                    "type" : "number",   
                    "default":0,                 
                    "value": 2                    
                }
            ]        
        },
        {
            "name": "SetVariable",
            "icon": "arrow-down",
            "isComposite":false,
            "description" : "Set \"{{VarName}}\" to {{Type}}  \"{{Value}}\"",
            "properties": [
                {
                    "name": "VarName",
                    "default":"[not set]",                 
                    "value": "varName"           
                },
                {
                    "name": "Value",
                    "default":"[not set]",                 
                    "value": "value"           
                },
                {
                      "name": "Type",
                      "default": "None",
                      "type": "enum",
                      "values": [
                        "string",
                        "number",
                        "bool",
                        "Panic"
                      ]
                }
            ]        
        },
        {
            "name":"IsSetVariable",
            "icon": "arrow-up",
            "isComposite":false,
            "description" : "Does \"{{VarName}}\" exist?",
            "properties": [
                {
                    "name": "VarName",
                    "default":"[not set]",                 
                    "value": "varName"           
                }
            ]
        },{
            "name":"SubTree",
            "icon":"cog",
            "isComposite":false,
            "description":"Runs Behavior: \"{{SubTreeName}}\" ... Please Note, {{description}}",
            "properties": [
                {
                    "name": "SubTreeName",
                    "default":"[not set]",                 
                    "value": "subTree"           
                },{
                    "name": "description",
                    "default":"[not set]",
                    "value":"description"
                }
            ]
        }
    ],
    "decorators": [
        {
            "name": "Failure",
            "icon": "thumbs-o-down"
        },
        {
            "name": "Invert",
            "icon": "exchange"
        },
        {
            "name": "Success",
            "icon": "thumbs-o-up"
        },
        {
            "name": "RepeatUntilFailure",
            "icon": "arrow-up",
            "description":"Execute child until Failure"
        }

    ],
    "services": [
        {
            "name": "Sample service",
            "icon": "cog",
            "description": "sample service",
            "properties": [
                {
                    "name": "BlackboardKey",
                    "default": "Target",
                    "type": "string"
                },
                {
                    "name": "BlackboardKey2",
                    "default": "1",
                    "type": "string"
                }
            ]
        },
        {
            "name": "ScriptFunction",
            "icon": "cog",
            "description": "Execute a scripted function \"{{FunctionName}}\" with arg1=BBKey \"{{BlackboardKey}}\" and arg2=BBKey \"{{BlackboardKey2}}\" and arg3=number  \"{{ConstantNumber}}\"",
            "properties": [
                {
                    "name": "FunctionName",
                    "default": "TakeDamage",
                    "type": "string"
                },
                {
                    "name": "BlackboardKey",
                    "default": "Target",
                    "type": "string"
                },
                {
                    "name": "BlackboardKey2",
                    "default": "SomeArg2",
                    "type": "string"
                },
                {
                    "name": "ConstantNumber",
                    "default": "1",
                    "type": "number"                
                }
            ]
        }
    ]
}
[/code]

-------------------------

Leith | 2019-06-21 05:01:56 UTC | #21

So far, I have a mechanism whereby I can create rich behaviors using references to (not copies of)  more primitive behaviors - Agents can share the same behaviors without new objects being created ... I can store data per agent and query it back again, but agents can't query the state of the world.

I plan on using the GlobalVars (owned by Urho Context) to act as a global blackboard, and I'll devise a couple more node types that will allow me to copy variables between blackboards.

The idea is to let the ai "observe" its world, and record its most recent knowledge of its environment, which is then used in decision-making. When the AI decides not to eat an apple because it is not hungry, it may go off to do other things. When it gets hungry, it may remember where it saw an apple - and set off to retrieve it. But when it arrives, the apple may no longer be there. This is plausible ai.

-------------------------

SirNate0 | 2019-06-21 10:12:56 UTC | #22

Have you thought about how to handle node position and similar constantly updating variables? Will they just have to be copied to the blackboard hash map every time the tree, or will there be special methods for observing position and the like?

-------------------------

Leith | 2019-06-21 10:17:22 UTC | #23

so far, updating the logic tree of an ai informs the parent node what to do - it "just works"
I can see some situations where this may not work, but so far, so good
agent position is not something we need to store in the agent blackboard, its a world blackboard thing, i will cover this in the next day or two - and hopefully it will become more clear

-------------------------

Leith | 2019-06-21 10:20:08 UTC | #24

I have not yet cut any pieces of meat out of the original codebase, I have merely extended it, I have loads of respect for the OP

-------------------------

Leith | 2019-06-21 10:23:55 UTC | #25

i should be more clear, since this is my thread after all .... we can ask an AI Agent about what it knows, or we can ask the world about what it knows - these two concepts are entirely separated.
The AI may recall things it has seen recently, but it will not have access to the world data... it has its own data! It may perform a visibility test to see what it can see, but it may not see what it likes.

-------------------------

Leith | 2019-06-22 05:09:24 UTC | #26

I added some more action (aka task) nodes today, involving blackboard variables.
There's now a clear concept that the game world represents a global blackboard (implemented via the GlobalVars stored in the Urho3D context), while each Actor has its own blackboard.

There are now task nodes which can set both global and actor-owned variables by name, supporting variant type, and nodes to check for the existence of both global and actor-owned vars.
Next will come some simple nodes to copy named variables between agent-local and global blackboards, and then a node or nodes to perform conditional testing, which will allow me to implement "guard conditions" that allow or disallow the execution of logical subtrees.
I also need to implement support for VariantVector based stack variables, and nodes to "push and pop" nameless member values.

With respect to design, I must credit Chris Simpson for some brilliant ideas with regard to utility nodes.
[https://www.gamasutra.com/blogs/ChrisSimpson/20140717/221339/Behavior_trees_for_AI_How_they_work.php]


Here is the full set of nodes I have implemented so far, minus a few test ones that didn't end up fitting with my use-case:
[code]
    void BehaviorTree::RegisterCommonNodeTypes(Context* context){

        /// Special Case: we're registering an attribute in the base class
        /// but we don't register an object factory for the base class
        BehaviorTreeNode::   RegisterObject(context);

        /// Register Composite node types:
        SelectorNode::       RegisterObject(context);
        SequenceNode::       RegisterObject(context);
        ParallelNode::       RegisterObject(context);

        /// Register Action node types:
        LogAction::          RegisterObject(context);
        WaitStepsAction::    RegisterObject(context);
        SetVariable::        RegisterObject(context);
        IsSetVariable::      RegisterObject(context);
        SetGlobalVariable::  RegisterObject(context);
        IsSetGlobalVariable::RegisterObject(context);
        SubTree::            RegisterObject(context);

        /// Register Decorator node types:
        InvertDecorator::    RegisterObject(context);
        LoopDecorator::      RegisterObject(context);
        SuccessDecorator::   RegisterObject(context);
        FailureDecorator::   RegisterObject(context);
        RepeatUntilFailure:: RegisterObject(context);

    }
[/code]

-------------------------

Leith | 2019-06-22 05:42:06 UTC | #27

There will be "service nodes" which are used to observe runtime state - I have not yet supported the owl-bt concept of service nodes at all, but this is how we will get our state updates - and where I get to implement "ai sensory input and memory" in terms of writing observed information to the per agent blackboard representing its knowledge of the world, as opposed to the actual world state.

In my own previous work, I had nodes with "input and output pins" that could be used to pass input args and return values during node execution, on top of the usual state return value... but the practical design and testing of these kinds of trees, even with a decent visual editor, turned out to be counter-productive.

Anyway, before I experiment with observer patterns, I need to implement support for stack variables.

-------------------------

Leith | 2019-06-22 06:32:50 UTC | #28

I'm currently experimenting with a kind of "guard condition" node.
It can perform one of six kinds of logical compare operation, using two input variables.
The inputs can sourced from one of three places: constant value, agent blackboard variable, world blackboard variable.

The tests it can do are:
- IsNull
- IsEqual
- IsGreater
- IsGreaterOrEqual
- IsLess
- IsLessOrEqual

We don't need so many flag bits to encode all those operations, do we?
Well, the encoding I propose below has some degenerate states (IsGreaterOrLess, IsNullOrGreater, so on), and in truth, I could reduce this flag set further based on the fact that we have an Inverter decorator node... anyway, let's move on!

[code]
    enum ConditionalOperator{
        COND_NULL=0,
        COND_EQUAL=1,
        COND_GREATER=2,
        COND_LESS=4
    };

    enum ConditionalValueSource{
        Constant,
        Actor,
        World
    };

    class VariableCompare:public LeafNode {
        URHO3D_OBJECT(VariableCompare, LeafNode)
    public:
        static void RegisterObject(Context* context);
        VariableCompare(Context*);
        virtual void OnFactoryConstruct();
    protected:
        virtual BTNodeState HandleStep() override;

        ConditionalOperator conditionOperator_;

        ConditionalValueSource Type_A;
        ConditionalValueSource Type_B;
        
        String NameOrValue_A;
        String NameOrValue_B;

    };
[/code]

This node lets us perform logical compares using values that can come from the actor doing the query, or from the game world. What is missing, is the ability to query a target agent. But a target agent is just a blackboard variable, so I feel I am getting warmer.

-------------------------

Leith | 2019-06-23 07:04:46 UTC | #29

The following is a double post.... I realized too late that I had posted this in the wrong thread.
I'll sort that out, here it is:
Here's the owl-bt config for my new "guard condition node".
[code]
        {
            "name":         "VariableCompare",
            "icon":         "question",
            "isComposite":  false,
            "description":  "Is {{SourceA}}:{{VarA}} {{CondOp}} {{SourceB}}::{{VarB}} ?",
            "properties": [


                {
                    "name": "SourceA",
                    "type": "enum",
                    "values": [
                        "Constant",
                        "Agent",
                        "World"
                    ]
                },
                {
                    "name": "VarA",
                    "default": "[not set]",
                    "source": "string"
                },
                {
                    "name": "CondOp",
                    "type": "enum",
                    "values": [
                        "==",
                        ">",
                        ">=",
                        "Panic"
                    ]
                },
                {
                    "name": "SourceB",
                    "type": "enum",
                    "values": [
                        "Constant",
                        "Agent",
                        "World"
                    ]
                },
                {
                    "name": "VarB",
                    "default": "[not set]",
                    "source": "string"
                }
            ]
        },
[/code]

Here's what it looks like in owl-bt right now:
![VariantCompare|622x500](upload://zpnBrPO52EEQBaBoWSoZsiNhNCR.png) 

and here's the code to drive the compare logic:
[code]
    BTNodeState VariableCompare::HandleStep(){

        Urho3D::Variant vA, vB;
                 double dA, dB;


        switch(SourceType_A){
            case ConditionalValueSource::Actor:
                vA=tree_->btContext_->blackboard_[NameOrValue_A];
                break;
            case ConditionalValueSource::World:
                vA=context_->GetGlobalVar(NameOrValue_A);
                break;
            case ConditionalValueSource::Constant:
                vA.FromString(ValueType_A,NameOrValue_A);
                break;
            default:
                URHO3D_LOGERROR("Unhandled SourceType A in VariableCompare");
                return NS_ERROR;
        }


        switch(SourceType_B){
            case ConditionalValueSource::Actor:
                vB=tree_->btContext_->blackboard_[NameOrValue_B];
                break;
            case ConditionalValueSource::World:
                vB=context_->GetGlobalVar(NameOrValue_B);
                break;
            case ConditionalValueSource::Constant:
                vB.FromString(ValueType_B,NameOrValue_B);
                break;
            default:
                URHO3D_LOGERROR("Unhandled SourceType B in VariableCompare");
                return NS_ERROR;
        }

        switch(this->conditionOperator_){
            case ConditionalOperator::COND_EQUAL:
            if(vA==vB)
                return NS_SUCCESS;
            else
                return NS_FAILURE;
            break;

            case COND_GREATER:
                double dA, dB;
                switch(ValueType_A){
                    case VAR_BOOL:
                        dA=static_cast<double>(vA.GetBool());
                        break;
                    case VAR_FLOAT:
                    case VAR_INT:
                    case VAR_DOUBLE:
                    case VAR_INT64:
                        dA=vA.GetDouble();
                    default:
                        URHO3D_LOGERROR("Unhandled Variant Type A detected in VariableCompare node");
                        return NS_ERROR;
                }
                switch(ValueType_B){
                    case VAR_BOOL:
                        dB=static_cast<double>(vB.GetBool());
                        break;
                    case VAR_FLOAT:
                    case VAR_INT:
                    case VAR_DOUBLE:
                    case VAR_INT64:
                        dB=vB.GetDouble();
                    default:
                        URHO3D_LOGERROR("Unhandled Variant Type B detected in VariableCompare node");
                        return NS_ERROR;
                }

                if(dA>dB)
                    return NS_SUCCESS;
                else
                    return NS_FAILURE;
                break;

            case (COND_GREATER | COND_EQUAL):
                switch(ValueType_A){
                    case VAR_BOOL:
                        dA=static_cast<double>(vA.GetBool());
                        break;
                    case VAR_FLOAT:
                    case VAR_INT:
                    case VAR_DOUBLE:
                    case VAR_INT64:
                        dA=vA.GetDouble();
                    default:
                        URHO3D_LOGERROR("Unhandled Variant Type A detected in VariableCompare node");
                        return NS_ERROR;
                }
                switch(ValueType_B){
                    case VAR_BOOL:
                        dB=static_cast<double>(vB.GetBool());
                        break;
                    case VAR_FLOAT:
                    case VAR_INT:
                    case VAR_DOUBLE:
                    case VAR_INT64:
                        dB=vB.GetDouble();
                    default:
                        URHO3D_LOGERROR("Unhandled Variant Type B detected in VariableCompare node");
                        return NS_ERROR;
                }
                if(dA>=dB)
                    return NS_SUCCESS;
                else
                    return NS_FAILURE;
                break;

            default:
                URHO3D_LOGERROR("Unhandled Operator in VariableCompare");
                return NS_ERROR;
        }
    }
[/code]

The only thing I have not shown is the code that "unpacks" the property values during loading from JSON. The loader is universal - it can load property values for node types without having any idea what kind of node it is - each concrete node class provides code to "unpack" the property values that the loader has retrieved.

Note that this is still just a draft, it's incomplete but good enough to test how well a generic compare node works in my use-case. If you have any experience in low level BT design, I would love to hear your thoughts on what I've done, and what I could possibly do to improve on it, including desirable new node types.

-------------------------

SirNate0 | 2019-06-23 15:34:56 UTC | #30

I have essentially no experience with behavior trees, but I do have a little experience with node based editors. While it's certainly up to you, as I have little idea about the complexity involved vs perceived gain, I think adding support for more complicated expressions would be desirable, beyond just comparisons. For example, how would you implement (a + 20 > b) or the like? As such, (and do to my own personal opposition to construction potentially complicated mathematical expressions through a series of nodes), I would propose implementing something similar to [ExprTk](https://archive.codeplex.com/?p=fastmathparser) for your logic/arithmetic. Basically, allow an arbitrary expression specified as a string with some number of variables (ideally very large, perhaps due to editor constrains more limited). It's up to you (of course), but for now that's my only suggestion.

-------------------------

Leith | 2019-06-24 06:53:21 UTC | #31

Thanks for your response!

Yes I did think about supporting more complex expressions - but so far have resisted the urge to implement a "general logical expression" node.

For nodes that implement "canned logic" - where the logic is complex enough to warrant it - I plan to implement Script Nodes which can execute a named script function, pass arguments, and to some degree, handle return values. Currently there is essentially no support for scripting, but that would be my ideal way to deal with complex general expressions, as well as expert behaviors such as detecting what an agent can "see", or whether a valid path to a given target exists. The most expensive canned behaviors can be promoted to c++ in order to reduce computational cost at runtime.

Tonight, I plan to spend some time planning exactly how the AI will determine its current goal. This should help inform future design decisions with respect to BT.

I like the idea of canned task nodes a lot - along with subtree ref nodes, they give us a way to wrap up what would otherwise be a sprawling mess of primitive nodes, and greatly assist us mere humans in understanding what the BT is actually doing at any moment.

-------------------------

Leith | 2019-06-24 13:46:25 UTC | #32

I studied game programming at a fancy new-age place with connections to the game and movie industries. It cost me a lot of money, but I got a discount on the time I had to study based on the fact that I could code asm shaders that made the test machines scream audibly, with frame rates around 3000 fps on custom render tech.
One of my teachers was an asian guy called Ted. He was a pretty bad teacher to be honest, but he did have street cred - he worked on the AI for star wars - kotor, and the sims series. He explained to me how the AI worked in his games. I will at some point try to express what he told me.
One of the reasons I say that Ted was a bad teacher, is that he left me stranded, and went back into the industry, when I needed him the most. I am just lucky to have met him.
Ted had an amazing grasp of higher mathematics, including set theory, and I only wish I had more time to get to know him and his amazing brain.

-------------------------

Leith | 2019-06-24 14:37:51 UTC | #33

How NOT to use behavior trees for decision making!
https://miro.medium.com/max/500/1*2jnsFCe0YmRjb8EvVAo93w.gif

Apparently, if you earn under 30k, and have a criminal record, you qualify for a loan.

-------------------------

Virgo | 2019-06-25 07:39:55 UTC | #34

:rofl: first of all pardon my laziness
**this thread is too long and has too many replies** and i dont wanna read them
just post this link here and i will leave :thinking:

https://github.com/BehaviorTree/BehaviorTree.CPP

hope this will help?

-------------------------

johnnycable | 2019-06-25 14:29:55 UTC | #35

> ...It provides a type-safe and flexible mechanism to do  **Dataflow**  between Nodes of the Tree.

Hmm... I like it. This reminds me every application is a behaviour tree...

-------------------------

Leith | 2019-06-26 02:17:13 UTC | #36

I like to think of behavior trees as being like a well-structured functional program - we have a bunch of dedicated functions that are well-insulated and reusable, and which by themselves don't do anything, and we have some control logic which guides the execution of the program based partly on the return values of the island functions, effectively "stringing them together" - just like the edges in a tree of nodes. Conceptually, there's nothing different happening other than how the logic is being represented. When I think of the number of times I have rewritten the same code over the years, the idea of a visual programming library, where the building blocks represent code I actually wrote, seems attractive, even a seasoned programmer can benefit from modern approaches to design and development.

-------------------------

Leith | 2019-06-26 07:46:33 UTC | #37

Thanks for the input!
I do appreciate your effort, and I took the time to examine the sourcecode.
Unfortunately, the model is not "immediately" useful to me, however I have taken onboard some of the ideas (some are new, some are old to me) and I will bring them into my next evaluation iteration.

Whether or not I end up actually using any of it, I am grateful that others are willing to take the time to throw me a bone occasionally.

-------------------------

Virgo | 2019-06-26 17:02:25 UTC | #38

i have been wanting to do a behavior tree for a long time, but due to my lack of knowledge and poor understanding & imagination i just keep procrastinating.
we talked about bullet implementation before, and i havent started writing it neither :joy:

-------------------------

Modanung | 2019-06-26 20:03:53 UTC | #39

When I try to think about designing AI I imagine something more like a (designed) neural net, with a set of inputs processed through some graph resulting in a set of weighted actions. Any nodes in between would *exactly* be arithmetic nodes. For instance the decision to flee should take health, remaining potions and distance to enemy into account, I believe these values can be multiplied and added in a way that relatively realistic behaviour can be designed. Factors instead of if-statements would form the network, and not orders but motivation would be the logic behinds its structure. Slight variations in these factors would be like introducing neurodiversity to your entities.

-------------------------

green-zone | 2019-06-26 19:57:12 UTC | #40

Also, for learn BT you can see:
https://github.com/LeegleechN/libbehavior
https://code.google.com/archive/p/libbehavior
It easy learn code.

-------------------------

Leith | 2019-06-27 07:58:13 UTC | #41

I worked on GPU-accelerated neural networks for game AI for my final bachelor paper.
Basically I wanted to prove that realtime neural AI was possible using consumer grade hardware, we simply needed to format our data to suit the gpu pipeline. I used OpenCL 1.0 - the simulation involved three species in competition: herbivores (rabbits), carnivores (wolves), and omnivores (humans). The emphasis of the experiment was to highlight emergent behaviours, such as pack-hunting behaviours, which were completely unrehearsed and never coded.

-------------------------

Virgo | 2019-06-27 09:04:07 UTC | #42

:bowing_man:the thing is i dont have enough knowledge to start investing in neural network thing, and i suppose it require much more power than behavior tree to simulate game AIs? we dont need AIs in game to be that super intelligent anyway (**just excuses**)

-------------------------

Leith | 2019-06-28 05:13:21 UTC | #43

Behavior trees, and other kinds of decision trees such as GOAP, are better for game development (than neural solutions) generally, and the reason that I say this is because we can develop solutions that do exactly what we want and no more, while neural solutions tend to veer off course and produce behaviors which, although successful according to our rules of engagement, were not at all what we had in mind.
We as game developers are control freaks.
We design our logic based on variable input and desirable output.
Neural networks, on the other hand, simply want to find the best way to make our "fitness function" happy.

Basically I am stating that those neural networks for games which can learn at all times, are unpredictable and therefore present a real business risk.

-------------------------

Modanung | 2019-06-28 09:42:24 UTC | #44

Indeed the *self-learning* element that people think of when mentioning neural nets introduces complex math and unpredictable evolution towards potentially godlike opponents. The constituent neurons, on the other hand, are quite simple. What I *imagine* is a neural net *designer* that allows its users to design static comprehensible brains using math nodes. Something like a behaviour tree, but one weighing out factors instead of checking conditions.

-------------------------

Leith | 2019-06-29 09:29:06 UTC | #45

there is a lot of current debate about how we can't easily analyze modern neural networks - in order to take advantage of gpu acceleration, I was forced to provide a regular structure in each genome - that is to say, all members of a given SPECIES shared the same neural network topology, differing only in terms of neuron weights.. but the networks which learn the most rapidly, and which do best at avoiding getting trapped in local minima, are those that can adapt their network topology and complexity, and not just twiddle with the neural weights and biases. One great example for games is NEAT - neural evolution of adaptive topologies (think I got that right)

-------------------------

Leith | 2019-06-29 10:57:15 UTC | #46

Today I extended lezak's BT codebase to support "precondition decorators".

The codebase had previously supported "traditional decorators", which execute after the logic update for a BT node, and are typically used to hack the return value for that node.
Preconditions on the other hand, execute BEFORE the node's usual logic, and are typically used to allow or disallow execution of that node, and the entire subtree beneath it.
It's possible to construct such a "guard node" using several more primitive nodes, but that does not scale well with the complexity of our ai behaviors, and quickly becomes ugly to look at as well as potentially ambiguous.

My implementation reflects the fact that my current preferred BT editor (owl-bt) does not distinguish between decorator types. Preconditions are implemented as decorator nodes, while the JSON data for these node types contains a special markup to identify them to the loader/parser code. Owl-bt can show nodes as different colors and with different icons to identify them visually, but it actually has no concept of how decorators work, it's just a visual editor.

I also eliminated the blackboard variantmap from the btContext structure, opting instead to provide a weakptr to the node that acts as root node for the actor / agent. I'm now using the node user variables member to store agent blackboard information. I sense these will be serialized automatically, though I doubt that object handles will be automatically serialized using scene ids.. I'm not done yet, but I'm certainly in a happier place with respect to sharing data between c++ and angelscript!

Next steps may include support for multiple cascading decorators, both as preconditions and as postconditions... "Any BT node, including leaf nodes, can have exactly one precondition node, and exactly one postcondition node - but any decorator node can have zero or one child nodes of the same decorator node major type, and so cascading test logic can be easily implemented"

[code]
    BTNodeState BehaviorTreeNode::OnStep()
    {

        /// If this node is in "inactive" state, we should "wake it up".
        if (state_ == NS_INACTIVE)
            Initialize();

        /// If this node is in "error" state, we should "bail out"...
        else if (state_ == NS_ERROR){
            URHO3D_LOGERROR(GetTypeName()+" "+name_ + "is in error state");
            return NS_ERROR;
        }

        /// Check for PRECONDITION decorator (these allow or deny execution of the node's logic)
        if(precondition_) {
            state_=precondition_->Decorate(state_);
            if(state_!=NS_SUCCESS){
                Terminate(state_);
                return state_;
            }
        }

        /// Execute the node logic (virtual method)
        state_ = HandleStep();

        /// After executing the node logic, we observe the new state of the node...
        /// If the node is "still running", do nothing..
        /// But if the node is in any other state, we need to act.
        if (state_ != NS_RUNNING)
        {
            /// Check for postcondition decorator (these manipulate the node's return value)
            if (decorator_)
            {
                state_ = decorator_->Decorate(state_);
                if (state_ == NS_INACTIVE)
                    Initialize();
            }
            /// Don't terminate if post-op decorator changed state to running
            if (state_!= NS_RUNNING)
                Terminate(state_);

        }
        return state_;
    }
[/code]

-------------------------

Leith | 2019-06-29 11:06:37 UTC | #47

My new chartreuse favourite colour, is "#bada55"

-------------------------

Leith | 2019-07-03 09:19:06 UTC | #48

I took a major change of direction with BT work today.
This involved entirely getting rid of my recently-added "btContext", and implementing an Actor  angelscript class that can interact with the c++ behaviortree node classes, and effectively provide a shared data store.

-------------------------

Leith | 2019-07-07 09:17:11 UTC | #49

```
class Zombie:Actor
{

	void Update(float dT){
		Print("Update ZOMBIE: "+actorName);

		// Execute a named (presumably root-level) behavior: all the "magic" happens in here...
		btNodeState result = RunBehavior("testbehave",dT,@self);
	}

}
```

-------------------------

Leith | 2019-07-07 08:32:42 UTC | #50

So, I have reached a new "understanding" with my latest BT work.

Basically, I don't need a "BTContext" to represent the calling agent anymore.
In the latest work, all Actors are script objects, represented in Urho via ScriptInstance components.
Each ScriptInstance component "scrapes" the angelscript object it creates for attributes/properties, the node it is attached to provides further storage for named variables, and there is also access to context-global variables.

This arrangement makes life a lot easier for me, in terms of "hooking up" behavior tree nodes to named methods at runtime!

I also figured out a solution for getting return values from script methods without having to explicitly add an output argument to my script functions/methods and hand that in during executions... I now have a clean way to get return values from ScriptInstance::Execute :)

-------------------------

Leith | 2019-07-08 04:36:20 UTC | #51

*All the world's an actor, too* , And all the men and women merely blackboards;

So far, I am using global variables to represent world knowledge... but scene knowledge makes more sense. The game world could be an Actor too... in theory.

What is an Actor?

To me, it is currently defined as, some instance of some script class, which has a blackboard hanging from its neck. Every actor has a blackboard, containing the sum of its knowledge, of its own state, and of world state too. But what of the world? :)

An actor is simply the owner of a blackboard, and the caller of a behavior.

-------------------------

Leith | 2019-07-09 13:14:33 UTC | #52

I've added two new kinds of BT node.

The first kind is called "ScriptAction" - it is an Action node (ie a leaf node) which can execute an angelscript method (in the script class of the caller agent), with up to two input arguments, and returnvalues are fully supported too.

The second kind is called "ScriptService" - its my first (and only) "service node" so far.
Service nodes are similar to decorator nodes, in that they can be attached to any other node type.
Service nodes, if present, execute just after any "preconditions", and prior to the node logic for the container node. They have a timer that controls how often their logic fires.
ScriptService nodes can call an AngelScript method at a fixed (typically low) frequency.

Both of these node types can dictate what to do with return values: ignore them, or store them according to a storage type hint (ie, as a named property, variable, or global value).

It took a fair bit of time to get these nodes working as intended, mostly spent in testing.

-------------------------

Leith | 2019-07-10 07:37:24 UTC | #53

Today's new node type is an action node called PopFromStack.

Assuming we have "some way of querying for a stack"..ie,  of shoving a Vector<Variant> into a named variable (with the usual caveat about storage qualifiers), this node can grab a Variant from a named stack (storage qualifiers again), and shove it into another named variable (storage qualifiers again).

This gives us a way to perform "foreach" logic within our behavior logic.
I'll post a screen shot soon, showing how this looks in the owl-bt behavior editor.

There's currently some pain in passing vectors to/from angelscript...
You see, our current script implementation does not support Template Types to be exposed to AngelScript... even though AngelScript can theoretically deal with template types.
Instead, we have a situation where array proxy containers are used to pass vectors / lists back and forth to angelscript, involving much copying, which is not ideal in my opinion.

-------------------------

Leith | 2019-07-10 07:42:56 UTC | #54

![popstack|690x417](upload://ybiKhw1U8w0G09cZ2ESMnTjbKmL.png)

-------------------------

Leith | 2019-07-10 08:01:42 UTC | #55

There are now effectively four kinds of concrete node class: sequence, selector, actions and decorators.
The base node class provides for three kinds of decorators: preconditions, postconditions and services.
This implies that any node can be decorated in one of three ways.
Despite deriving from LeafNode, decorators support Chaining through the base node class.

I have started to document - and not using doxygen!

-------------------------

