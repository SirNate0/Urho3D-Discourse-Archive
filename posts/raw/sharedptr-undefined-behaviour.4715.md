Sheridan | 2018-12-09 12:29:14 UTC | #1

Greetings! )
I'm trying to understand how to work with SharedPtr correctly and stumbled upon an indefinite behavior that put me in a dead end. It is expected that after deleting an object, the number of links will decrease, but this does not happen.
```
Urho3D::SharedPtr<Urho3D::Node>  m_rootNode;
...
#define DELETE_URHO_PTR(_name,_method) \
    LOG_DBG(#_name " isnull? " << _name.Null()) \
    if(_name.NotNull()) \
    { \
        LOG_DBG(#_name " before refs=" << _name.Refs()) \
        _method; \
        delete _name; \
        LOG_DBG(#_name " after refs=" << _name.Refs()) \
    }
#define DELETE_URHO_REMOVABLE(_name) DELETE_URHO_PTR(_name, _name->Remove())
...
DELETE_URHO_REMOVABLE(m_rootNode);
```
Logs:
```
[2018-12-09 13:53:37] {140326202556608} [Debg] m_rootNode isnull? false
[2018-12-09 13:53:37] {140326202556608} [Debg] m_rootNode before refs=3
[2018-12-09 13:53:37] {140326202556608} [Debg] m_rootNode after refs=-1411174928
```

I also often use the “create on access” technique. Do I understand correctly that the .Get() method will not change the number of refs count?
```
Urho3D::Node *CWorldObject::rootNode()
{
    if(m_rootNode.Null())
    {
        m_rootNode = ST->graphic()->scene()->CreateChild();
    }
    return m_rootNode.Get();
}
...
Urho3D::RigidBody *CWorldObject::body()
{
    if(m_body.Null())
    {
        m_body = rootNode()->CreateComponent<Urho3D::RigidBody>();
        m_body->SetCollisionEventMode(Urho3D::COLLISION_ALWAYS);
    }
    return m_body.Get();
}
```

In general, I would very much like not to use SharedPtr in my project, but to work with objects directly. But as I understand it, CreateChild/CreateComponent, in addition to constructing objects, also performs various bindings that are not performed in object constructors, that is, the part of object initialization is taken out of an object ...
How safe will it be to not use SharedPtr/CreateComponent?

-------------------------

S.L.C | 2018-12-09 12:55:00 UTC | #2

I still don't understand why you call `delete` on `m_rootNode`. That's not a pointer and I'm not even sure why the compiler let you do that. You're supposed to `Release()` your reference and let the smart pointer do it's job.

As for why the counters become that value. You should look at the destructor of `RefCounted`.

-------------------------

Sheridan | 2018-12-09 13:13:07 UTC | #3

[quote="S.L.C, post:2, topic:4715"]
Release
[/quote]

This method unavialable, but i think i should use delete or Reset() [because](https://github.com/urho3d/Urho3D/blob/17c4a1022d3342b6318fa095661a0ecba6306284/Source/Urho3D/Container/Ptr.h#L72)

-------------------------

S.L.C | 2018-12-09 14:13:34 UTC | #4

You would only use delete if the shared pointer itself would be dynamically allocated. Like `Urho3D::SharedPtr<Urho3D::Node>*  m_rootNode;` and not `Urho3D::SharedPtr<Urho3D::Node>  m_rootNode;`. Notice the `*`.

So based on that macro. I assume this line `delete _name;` becomes `delete m_rootNode;`. And `m_rootNode` is not a pointer.

Or maybe I got something wrong here. Who knows.

And yes. The method was `Reset()`. My mistake.

-------------------------

Sheridan | 2018-12-09 14:33:00 UTC | #5

oh, [operator delete](https://en.cppreference.com/w/cpp/memory/new/operator_delete) not overload in SharedPtr. It my mistake, right.

But when i show in code...
```
void Reset() { ReleaseRef(); }

void SharedPtr::ReleaseRef()
    {
        if (ptr_)
        {
            ptr_->ReleaseRef();
            ptr_ = nullptr;
        }
    }
```

`ptr_ = nullptr;` ???

of course,
```
void RefCounted::ReleaseRef()
{
    assert(refCount_->refs_ > 0);
    (refCount_->refs_)--;
    if (!refCount_->refs_)
        delete this;
}
```
but i think more right move deleting to SharedPtr from RefCounted

My question im my project begin from this point: i have a dynamic mesh and make model like this

```
Urho3D::Model *CDynamicMesh::dynamicModel()
{
    if(m_dynamicModel.Null())
    {
        m_dynamicModel = new Urho3D::Model(ST->graphic()->context());
    }
    return m_dynamicModel.Get();
}
...
m_parentBlock->collisionShape()->SetTriangleMesh(dynamicModel());
m_parentBlock->model()->SetModel(dynamicModel());
```
and in result i have 3 refs to pointer. But i can not rtemove my model from `m_parentBlock->collisionShape()` ( Urho3D::CollisionShape) and `m_parentBlock->model()` (Urho3D::StaticModel). How i can there reset refs?

-------------------------

Eugene | 2018-12-12 10:11:45 UTC | #6

[quote="Sheridan, post:5, topic:4715"]
How i can there reset refs?
[/quote]

When you reset m_dynamicModel and parent node for CollisionShape and StaticModel, m_dynamicModel would be gone

-------------------------

