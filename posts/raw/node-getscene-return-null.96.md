att | 2017-01-02 00:57:56 UTC | #1

hi,
I encountered a problem when I call the Node::GetScene() to get the Scene* value.
The code like following,
void BallMachine::ShootBall()
{
    Scene *scene = GetScene();
    assert(NULL != scene);
    SharedPtr<BaseBall> ball(new BaseBall(context_));
    scene->AddChild(ball);
    ball->Init();
    ...
}

When the first time I call this function, the function GetScene() can return the right value for Scene*, but when the second time it return a NULL value, anybody encountered this problem?
The BallMachine is a derived class from Node.

-------------------------

weitjong | 2017-01-02 00:57:56 UTC | #2

if the GetScene() return null it exactly means that the BallMachine node has somehow remove itself from the scene (somewhere it your code called Scene::NodeRemoved()) or your BallMachine node has been destructed. How do you keep your BallMachine node alive? I would set a breakpoint at Scene::NodeRemoved() and see at which point it is being invoked to troubleshoot the problem. HTH.

-------------------------

att | 2017-01-02 00:57:57 UTC | #3

I checked the code again, when the GetScene() return NULL value, the BallMachine's destruction function not called, and the NodeRemoved() also not called.

-------------------------

weitjong | 2017-01-02 00:57:57 UTC | #4

Note that I am kind of guessing here as I cannot see your code. My basic assumption is, there is no bug in the Urho3D game engine and the problem is with your code. With that assumption, GetScene() returns null could only happen in two cases.
[ol]
[li] You have a node that was previously part of the a scene and somehow it is not anymore. Or.[/li]
[li] Somehow your code acquire a new BallMachine node that is not yet added into any scene at later stage.[/li][/ol]
If you have ruled both of them out then it would be logical (as Mr Spock would say  :wink: - I hope you get the joke) that my basic assumption is wrong and you can log a bug in our GitHub.

Is it possible for you to post a snipet of your code on how you maintain BallMachine node?

-------------------------

cadaver | 2017-01-02 00:57:57 UTC | #5

It appears that you have subclassed Node as you're adding a BaseBall type of object as a child scene node.

If you subclass Node, you need to be quite well aware of Node's internal functionings. None of the examples do that as it's a *very* advanced topic, and for example the Editor will not know how to edit objects that are subclassed from Node, rather it assumes that all children of the Scene are of the type Node. Scene loading and saving holds the same assumption. The usual and recommended method of how you implement new functionality in Urho3D is creating new components instead.

What is the functionality that BaseBall adds? Could it be rather implemented as a component and added to an ordinary scene node? For examples of custom components check for example the 05_AnimatingScene sample, where a custom Rotator component is created and added to scene nodes.

EDIT: have added remark in the documentation that Node should not be subclassed.

-------------------------

att | 2017-01-02 00:57:57 UTC | #6

Thank you very much for your reply, and i carefully tracked the code and found that when I add a new ball node to scene, following code will be called,
    unsigned id = node->GetID();
    if (id < FIRST_LOCAL_ID)
    {
        HashMap<unsigned, Node*>::Iterator i = replicatedNodes_.Find(id);
        if (i != replicatedNodes_.End() && i->second_ != node)
        {
            LOGWARNING("Overwriting node with ID " + String(id));
            i->second_->ResetScene();
        }

 i->second_->ResetScene(); will be called.
So I think the problem is that Ball and BallMachine have the same id, I don't know whether it is the engine bug or I must guarantee different id for different object?
Thanks again.

-------------------------

cadaver | 2017-01-02 00:57:57 UTC | #7

The easiest way to create nodes is to call CreateChild(), which creates the node and adds an ID in one step. Obviously it doesn't work in your case as you have a custom Node subclass. I'll have to check what happens with the ID if you new() a node and add it to the scene afterward using AddChild(). This looks like an oversight in the engine; a non-duplicate ID should be assigned also in that case.

However the point still stands even if the ID problem is fixed, that subclassing Node will lead to trouble.

-------------------------

cadaver | 2017-01-02 00:57:57 UTC | #8

The ID problem was reproduced and fixed in github latest revision.

-------------------------

