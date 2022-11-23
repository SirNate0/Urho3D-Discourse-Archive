wakko | 2018-05-07 20:53:07 UTC | #1

Starting from the DynamicGeometry sample I am trying to make a class that will add even more geometry to the scene. As far as I see everthing (except for the camera which looks like instantiated on the "context") all new nodes must be added to the "scene_" object. Unfortunately all samples create the entire scene in the CreateScene() function. I would like to add a bit more structure to this for my project and separate objects groups into their own classes.
My own class should have a "parent" Node* to which I add the new objects. However none of my approaches succeeds.
Attempt #1: Pass "scene_" as the parent node argument fails due to scene being a the shared_ptr. (Incomplete type...). Maybe my mistake since my experience with shared_ptrs is ... little. Same happens upon dereferencing the scene_ shared_ptr and passing this as a "normal" pointer.
Attempt #2: Add an empty Node* to the scene_ and pass this to my class as the parent: Upon calling "m_parent->CreateChild("MyOwnObject"); does nothing and simply crashes the application without any error message.
Can someone point out what I am doing wrong here? Am I mixing up Node and Component somehow?

Bonus question (before I have to start a new thread for this): Is it possible to manually create a Material in code using an arbitrary jpg/png anywhere on my harddisk? If so: How would I do this?

-------------------------

SirNate0 | 2018-05-05 17:00:47 UTC | #2

In general, do not subclass Node. As an alternative, my suggestion would be to just create custom components and you can search for them/have them do the custom logic, or use tags on the nodes, etc. If you just want to load nodes as groups, use Node's LoadXML (or similar) to load that set of objects.

As to creating your own material, consider loading one like what you need, Clone()ing it, and then replacing the texture with the other one (you can do the whole thing programmatically, but if your just changing textures you can see up the colors and stuff in the xml and then just replace the texture in code).

-------------------------

wakko | 2018-05-06 10:53:54 UTC | #3

Thanks for the reply. 
Apparently the texture loading thing will be easier now.

For the node-adding: I am not making a subclass of node, I am just trying to move stuff from the "CreateScene" function into a function of a scene-generator class to prevent the CreateScene function from getting excessively long and maintain a bit of readability and modularity. This requires passing a parent Node* as an argument to the generator function so that I can call CreateChild on this parent Node from inside my function. But none of the approaches mentioned above works...
As the scene will be generated dynamically considering many other parameters loading an XML is not an option.
Edit:
To clarify what I am trying to do: 
This fails at compilation time due to "Incomplete Type" (all variations of &/*  with and without shared_ptr as argument type tested)
    void SceneGenerator::generateScenePart(shared_ptr<Scene> parent_)
    {
      Node* testNode = parent_->CreateChild("testNode");
    }
This fails at runtime with no error message at all when the parent_ Node is created from within the GenerateScene function from the sample code:
    void SceneGenerator::generateScenePart(Node* parent_)
    {
      Node* testNode = parent_->CreateChild("testNode");
    }

-------------------------

Lumak | 2018-05-07 13:53:42 UTC | #4

Instead of using the *shared_ptr* Urho3d has SharedPtr<> template, but this is not the issue.  I think the issue in your case maybe due to the argument variable named the same as a member variable -- this:

*void SceneGenerator::generateScenePart*(Node* **parent_**)

Perhaps you already have the parent_ member var assigned some where else and thinking that's what you're actually using instead of the argument variable parent_.

-------------------------

wakko | 2018-05-07 18:17:02 UTC | #5

Thanks for pointing out the SharedPtr vs. shared_ptr difference. That was indeed a mistake and at least I can compile now (using the SharedPtr argument), but it has the same effect as passing just another Node* to my function: A crash without any error message.
I have noticed the trailing underscore in member variables in the sample code. In my own classes/functions the trailing underscore marks function arguments. This is not the problem here. 

The question remains: What is the recommended way to pass a parent Node/Component/whatever to a function to add children to it from there?
The simplest usecase I can imagine: A function to add multiple lights to the scene...
How would I do that?
The sole purpose of this is to limit the length of the CreateScene function.

-------------------------

Lumak | 2018-05-07 19:42:41 UTC | #6

Node::CreateChild() fn. returns Node*, so your argument to your fn. should be Node*. I'm not sure what's going on with your code, but here's a simple fn. that I wrote in 18_CharacterDemo to demonstrate instantiating a large model box.

[code]
void CharacterDemo::TestGenNode(Node* parentNode)
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Node *node = parentNode->CreateChild();
    node->SetPosition(Vector3(0,15,0));
    node->SetScale(10.0f);
    StaticModel *staticModel = node->CreateComponent<StaticModel>();
    staticModel->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
}
[/code]

And the call is made from CreateScene() fn.:
[code]
    Node *parentNode = scene_->CreateChild();
    TestGenNode(parentNode);
[/code]

-------------------------

wakko | 2018-05-07 20:57:04 UTC | #7

Thanks for the illustration. I am doing exactly the same.
I have reduced my own code to do only this:
I am creating a Node* in CreateScene (as a class member) and pass it to a function that looks almost identical to yours. It even shows commandline output after each line and the resulting Node* is not NULL. And then I end up with the game window closing and only seeing the terminal window. I have narrowed it down to the line
Node *node = parentNode->CreateChild();
When I comment this one line out I am back at the DynamicGeometry sample.
I will dig further.

EDIT:
Since Lumak confirmed that I was doing everything correct he encouraged me to check some other part of my code which was causing the error (premature delete....) :(
I have marked the topic as solved. Thanks.

-------------------------

