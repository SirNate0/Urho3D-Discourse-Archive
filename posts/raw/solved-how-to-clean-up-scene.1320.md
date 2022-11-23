Dar13 | 2017-01-02 01:06:48 UTC | #1

Hello all,

I'm trying out Urho3D for a project, but some aspects of it are perplexing. The documentation seems fairly sparse and digging through source hasn't produced a definitive answer. I'm attempting to use the RAII idiom in my design, which means that the destructor is responsible for the clean up of resources used by the class. My question is: does the Urho3D::Scene class destroy the nodes that are attached to it, or does it simply orphan them? And if they orphan them, is there an accepted way to completely destroy a Scene and all its children nodes that doesn't involve iterating through the hierarchy and manually calling "delete" on those nodes?

I'd really like to avoid both iterating through the tree manually or maintaining a separate list of Node pointers to call delete on.

Thanks for your time.  :slight_smile:

-------------------------

thebluefish | 2017-01-02 01:06:48 UTC | #2

Urho3D uses reference counting. That means that there's a WeakPtr and SharedPtr that can refer to these Nodes. The Scene (which is actually just a fancy Node) will create a SharedPtr to all children Nodes. As long as another SharedPtr to that Node still exists when the Scene is destroyed, then the Node will still exist. However if you don't explicitly create a SharedPtr to a Node, then that Node will be deleted when its parent Node is deleted.

-------------------------

codingmonkey | 2017-01-02 01:06:49 UTC | #3

[urho3d.github.io/documentation/H ... scene.html](http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_scene.html)
Scene.RemoveAllChildren ()
Node.RemoveAllChildren ()
Node.Remove();
[quote]Remove from the parent node. If no other shared pointer references exist, causes immediate deletion.[/quote]

also if you use your custom logic component there are exist some std virtual methods
[urho3d.github.io/documentation/H ... onent.html](http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_logic_component.html)
 
class MyLogic : public LogicComponent()

void Start() 
{
// init logic
}
...
void Stop() 
{
// logic cleanup
}

Node.CreateComponent<MyLogic>() -> call MyLogic::Start() 
On Node.Remove() I guess MyLogic::Stop() will be called )

-------------------------

Dar13 | 2017-01-02 01:06:54 UTC | #4

Thank you for the replies. Seems I need to be a bit more awake before judging a project's documentation.  :laughing:

-------------------------

Enhex | 2017-01-02 01:06:55 UTC | #5

I do
[code]scene->Clear();
CreateScene();[/code]
CreateScene is a function for setting up the scene, for resetting.

-------------------------

