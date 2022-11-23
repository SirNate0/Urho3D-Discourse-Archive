Sheridan | 2018-12-19 18:49:19 UTC | #1

I have classes like this:
```
class CWorldObject
{
public: 
CWorldObject() :
    m_body(nullptr),
    m_collisionShape(nullptr)
{
    m_rootNode = EING_ST.graphic().scene()->CreateChild();
}

~CWorldObject()
{
    m_rootNode->UnsubscribeFromAllEvents();
    m_rootNode->Remove();
}

Urho3D::Node *rootNode()
{
    return m_rootNode;
}

Urho3D::RigidBody *body()
{
    if(!m_body)
    {
        m_body = rootNode()->CreateComponent<Urho3D::RigidBody>();
        m_body->SetCollisionEventMode(Urho3D::COLLISION_ALWAYS);
    }
    return m_body;
}

Urho3D::CollisionShape *collisionShape()
{
    if(!m_collisionShape)
    {
        m_collisionShape = rootNode()->CreateComponent<Urho3D::CollisionShape>();
    }
    return m_collisionShape;
}
private:
    Urho3D::Node            *m_rootNode;
    Urho3D::RigidBody       *m_body;
    Urho3D::CollisionShape  *m_collisionShape;
};
```

I do not understand how to free memory when removing such classes.
I understand that it is necessary to delete each created object. But when I try to do it - the application crashes. Moreover, it abnormally terminates even with such a destructor as it is now.

-------------------------

Sinoid | 2018-12-19 19:09:22 UTC | #2

- Node
- RigidBody
- CollisionShape

are all `RefCounted` objects.

> I do not understand how to free memory when removing such classes.

Use `SharedPtr<T>` and `WeakPtr<T>`, they will take care of the clean up for you (call reset when you want your local reference to be reset to null, which will **not** destroy the object it was referring to it unless it is no longer referenced anywhere).

Everything that derives from `Urho3D::Component`, `Urho3D::Resource`, and `Urho3D::Node` is reference counted - you don't delete them outside of unusual circumstances.

You're deleting objects that are already being referenced elsewhere which is circumventing the smart pointer reference counting and mangling the program's expected state resulting in it misusing memory when it attempts a function-call / member-access with one of those objects you deleted.

Outside of exceptional circumstances you should not be using raw pointers in any situation where you keep them around stored in a type (or anywhere), learn to use the smart pointer types.

> Moreover, it abnormally terminates even with such a destructor as it is now.

That's going to be a matter of how the sequence of termination plays out. If the scene containing those objects is destroyed before your CWorldObject then that destructor will crash because the scene already freed all of those objects leaving you with dangling addresses because you used raw pointers.

That same sequence of events will also mean that trying to delete them will crash because you're attempting to delete already freed memory.

-------------------------

Sheridan | 2018-12-19 19:28:09 UTC | #3

Well, let's say I go to smart pointers (although I really, really don't like them). How, then, to free up memory? Is it enough to call Remove () only for the m_rootNode, or do I need to call Remove () for each object that I explicitly create?
Can I be sure that the memory is really free? How can I check this?

-------------------------

Sheridan | 2018-12-19 21:52:46 UTC | #4

I am rewrite class as
```
Urho3D::SharedPtr<Urho3D::Node>            m_rootNode;
Urho3D::SharedPtr<Urho3D::RigidBody>       m_body;
Urho3D::SharedPtr<Urho3D::CollisionShape>  m_collisionShape;
...
CWorldObject::CWorldObject()
{
    m_rootNode = EING_ST.graphic().scene()->CreateChild();
    m_body = m_rootNode->CreateComponent<Urho3D::RigidBody>();
    m_body->SetCollisionEventMode(Urho3D::COLLISION_ALWAYS);
    m_collisionShape = m_rootNode->CreateComponent<Urho3D::CollisionShape>();
}

CWorldObject::~CWorldObject()
{
    m_rootNode->UnsubscribeFromAllEvents();
    m_collisionShape->Remove();
    m_body->Remove();
    m_rootNode->Remove();
}
// ...
// EING_ST - singleton (singleton::instance())
```
Now the application crashes when the pointer is released inside Ptr.h
[Here](http://paste.org.ru/?ly7dcv) call stack, and [here](http://paste.org.ru/?6xtnlv) full stack (crash in thread 1). 
Please help me understand what I am doing wrong.

-------------------------

Dave82 | 2018-12-19 22:30:03 UTC | #5

Theoretically if you use smart pointers you dont need node->Remove(). You can safely remove everything from destructor.The nodes will be removed when when CWorldObject is deleted

Change

[code]
CWorldObject::~CWorldObject()
{
    m_rootNode->UnsubscribeFromAllEvents();
    m_collisionShape->Remove();
    m_body->Remove();
    m_rootNode->Remove();
}
[/code]

to 
[code]
CWorldObject::~CWorldObject()
{

}
[/code]

-------------------------

Sheridan | 2018-12-19 22:33:27 UTC | #6

[quote="Dave82, post:5, topic:4766"]
to

```
CWorldObject::~CWorldObject()
{

}
```
[/quote]

Maybe to
```
CWorldObject::~CWorldObject()
{
  scene()->RemoveChild(m_rootNode);
}
```
?
Smart pointers really free memory? ...

-------------------------

Sheridan | 2018-12-19 22:38:47 UTC | #7

Just checked. If i leave the destructor empty, then the nodes are not removed from the scene. And if in the destructor, leave even just `scene()->RemoveChild(m_rootNode);`, then the application crashes.

-------------------------

Dave82 | 2018-12-19 22:44:16 UTC | #8

[quote="Sheridan, post:6, topic:4766"]
Smart pointers really free memory? …
[/quote]
Smart pointers are allocated on the stack within your class like any stack variable so if they go out of scope (delete your CWorldObject) all members of the object will be removed as well.
So to answer your question : Yes. You doun't need to do anything with smart pointers. They will remove themselves.That's the whole purpose of their existence

[quote="Sheridan, post:6, topic:4766"]
CWorldObject::~CWorldObject() { scene()-&gt;RemoveChild(m_rootNode); }
[/quote]
You don't need to do that. The bahavior is undefined in this case. If you remove the node from the scene your object's smart pointer still holds a reference to that node.Only devs know what will happen during the release the ref on the object which is not part of the scene.

-------------------------

Sheridan | 2018-12-19 22:43:21 UTC | #9

[quote="Dave82, post:8, topic:4766"]
(delete your CWorldObject)
[/quote]

My class CWorldObject is not inherited from anything from Urho3D. It controls the node, but is not part of the scene itself.

```
class CWorldObject
{
public:
    explicit CWorldObject();
    virtual ~CWorldObject();
protected:
    Urho3D::SharedPtr<Urho3D::Node>           &rootNode();
    Urho3D::SharedPtr<Urho3D::RigidBody>      &body();
    Urho3D::SharedPtr<Urho3D::CollisionShape> &collisionShape();
    void subscribeToEvent(const EEvent &event, TUpdateFunction method, Urho3D::Node *targetNode = nullptr);
private:
    Urho3D::SharedPtr<Urho3D::Node>            m_rootNode;
    Urho3D::SharedPtr<Urho3D::RigidBody>       m_body;
    Urho3D::SharedPtr<Urho3D::CollisionShape>  m_collisionShape;
// ... other methods and mrmbers

};
```

-------------------------

Dave82 | 2018-12-19 22:51:51 UTC | #10

[quote="Sheridan, post:7, topic:4766"]
Just checked. If i leave the destructor empty, then the nodes are not removed from the scene
[/quote]

Yes you're right.I was a bit confused what you are actually doing.

m_rootNode->Remove();

Should be perfectly ok without using smart pointers. Since All components are ref counted in nodes you don't need to release them one by one.Just Remove your node and let your node remove al it's components.I

So change
[code]

CWorldObject::~CWorldObject()
{
      m_node->Remove();
}

[/code]
And remove smart pointers and use regular pointers instead.

-------------------------

Sheridan | 2018-12-19 22:59:46 UTC | #11

Still crash in 
```
1  Urho3D::RefCounted::ReleaseRef()                                                                                                           0x7ffff731dc44 
2  Urho3D::Geometry::~Geometry()                                                                                                              0x7ffff73ac40d 
3  Urho3D::Geometry::~Geometry()                                                                                                              0x7ffff73ac4c9 
4  Urho3D::Model::~Model()                                                                                                                    0x7ffff73cbcd5 
5  Urho3D::Model::~Model()                                                                                                                    0x7ffff73cbe59 
6  Urho3D::CollisionShape::~CollisionShape()                                                                                                  0x7ffff74f5611 
7  Urho3D::CollisionShape::~CollisionShape()                                                                                                  0x7ffff74f5689 
8  Urho3D::Node::RemoveComponent(Urho3D::RandomAccessIterator<Urho3D::SharedPtr<Urho3D::Component>>)                                          0x7ffff758f241 
9  Urho3D::Node::RemoveComponents(bool, bool)                                                                                                 0x7ffff758f38e 
10 Urho3D::Node::~Node()                                                                                                                      0x7ffff758f448 
11 Urho3D::Node::~Node()                                                                                                                      0x7ffff758f679 
12 Urho3D::Node::RemoveChild(Urho3D::RandomAccessIterator<Urho3D::SharedPtr<Urho3D::Node>>)                                                   0x7ffff758eb1c 
13 eing::graphic::world::CWorldObject::~CWorldObject                                                                    cworldobject.cpp  57  0x4c835a       
14 eing::graphic::world::CStaticObject::~CStaticObject                                                                  cstaticobject.cpp 26  0x4cde58       
15 eing::graphic::world::CBlock::~CBlock                                                                                cblock.cpp        55  0x4993de       
16 eing::graphic::world::CBlock::~CBlock                                                                                cblock.cpp        41  0x499489       
17 eing_helper::cube::AppCubeHelper::redrawTestCube                                                                     main.cpp          351 0x45e6d5       
18 eing_helper::cube::AppCubeHelper::HandleUpdate                                                                       main.cpp          289 0x45f92f       
19 Urho3D::EventHandlerImpl<eing_helper::cube::AppCubeHelper>::Invoke                                                   Object.h          315 0x463337       
20 Urho3D::Object::OnEvent(Urho3D::Object *, Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)                       0x7ffff732d642 
21 Urho3D::Object::SendEvent(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)                                       0x7ffff732e93f 
22 Urho3D::Engine::Update()                                                                                                                   0x7ffff734d1d7 
23 Urho3D::Engine::RunFrame()                                                                                                                 0x7ffff735013a 
24 Urho3D::Application::Run()                                                                                                                 0x7ffff7342e45 
25 main                                                                                                                 main.cpp          378 0x45faca       

```
I try with `m_node->Remove();` or `scene()->RemoveChild(m_rootNode); ` in destrunctor 
:frowning:

-------------------------

Dave82 | 2018-12-19 23:07:44 UTC | #12


Your first example should work perfectly without any crash.

-------------------------

Sheridan | 2018-12-19 23:08:38 UTC | #13

Thank you so much anyway. I will try to look for errors in another place.

-------------------------

Modanung | 2018-12-20 16:31:07 UTC | #14

[quote="Sheridan, post:9, topic:4766"]
My class CWorldObject is not inherited from anything from Urho3D. It controls the node, but is not part of the scene itself.
[/quote]

Why not make `CWorldObject` inherit from `Urho3D::Object`?

-------------------------

Sheridan | 2018-12-20 16:34:57 UTC | #15

Because I want to use smart pointers as little as possible, since I know exactly the lifetime of my objects. Moreover, CWorldObject is just the first brick in the inheritance tree of objects and, in addition to describing world objects, is also a proxy between the world and graphics.

-------------------------

