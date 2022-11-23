Lunarovich | 2021-03-14 17:34:04 UTC | #1

I instantiate a scene with 

```
    repository_ = new Node(context_);
    auto* xmlFile = GetSubsystem<ResourceCache>()->GetResource<XMLFile>("Scenes/Repository.xml");
    auto xmlElement = xmlFile->GetRoot();
    repository_->LoadXML(xmlElement);
```

and subsequently use 

```
Node* EntityCreator::Clone(const String& name, const Vector3& position, const Quaternion& rotation) {
    auto* node = repository_->GetChild(name)->Clone();
    node->SetPosition(position);
    node->SetRotation(rotation);
    GetSubsystem<SceneManager>()->GetScene()->AddChild(node);
    return node;
}
```

Now, it seems to me that components of the cloned nodes do not keep the values of the components of original nodes. For example, I have this value in the original node's `RigidBody`
```
		<attribute name="Angular Factor" value="0 1 0" />
```

However, cloned node rotates along all the axis.

If I export the node from the editor and use `InstantiateXML()` than everything works as expected. However, I want to be able to pick up nodes from the loaded scene, without the need to export every model from the editor to the xml describing node.

-------------------------

JSandusky | 2021-03-14 21:53:20 UTC | #2

A couple of the physics attributes read/write directly into the body. In the clone case there's no body being created because at clone time it's unable to find the PhysicsWorld.

Those attributes probably need to be mirrored in the components and applied with AddBodyToWorld() and so on as there are likely other cases where this can happen aside from just clone.

-------------------------

Lunarovich | 2021-03-15 07:56:53 UTC | #3

Thnx! The easiest solution for me was to set non cloned RigidBody params directly in code.

-------------------------

