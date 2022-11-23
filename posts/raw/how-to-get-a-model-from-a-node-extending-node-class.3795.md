Tahri | 2017-11-27 13:57:48 UTC | #1

Hello Urho3D Community.

I'm working on a project that is like a copy and paste of objects. Where the mouse click will copy an object and the next mouse click will paste the object.  Except I'm using several different models / geometries that are never at fixed locations. 

My first instinct was to extend the node class and add a function for getModel() but after reading it seems extending the Node class is not advised or easily done.

What is the best way to accomplish this? GetComponent() doesn't seem to do what I need. 

Thanks in advance!

-------------------------

Eugene | 2017-11-27 14:00:23 UTC | #2

[quote="Tahri, post:1, topic:3795"]
What is the best way to accomplish this? GetComponent() doesn’t seem to do what I need.
[/quote]

Could you show code that doesn't work for you?
You should be able to get your components via `GetComponent` and pick any component, then just grap from the component whatever you want.

-------------------------

Tahri | 2017-11-27 15:39:19 UTC | #3

Thanks for responding Eugene,

Probably I'm not good at using the getComponent() function properly. If getCompoent() will work, my goal is to return my model from the node. When you say "pick any component" do you have an example?

I was thinking something like:

> Urho3D::Model * copiedModel =  targetNode->getComponent(); // do I need to typecast the component? 
 copy(copiedModel);

My copy method
> void copy(Urho3D::Model * data)
{
	//copy target node
	clipboard.push(data);
}

Maybe I'm thinking about this incorrectly is the component what I should be using instead of the model? I can try doing the copy and paste directly with that.

-------------------------

Eugene | 2017-11-27 15:59:37 UTC | #4

[quote="Tahri, post:3, topic:3795"]
When you say “pick any component” do you have an example?
[/quote]

There are plenty of Urho samples, have you checked them?
`GetComponent` is template function that gives you the component that you previously created or loaded at the Node.
How do you create components?

-------------------------

Modanung | 2017-11-27 18:20:48 UTC | #5

If you want to get all the `Model`s from a `Node` and its children you could do something like:
```
PODVector<Model*>models{};
PODVector<StaticModel*> modelComponents{};

node_->GetDerivedComponents<StaticModel>(modelComponents, true);

for (StaticModel* modelComponent : modelComponents) {

    models.Push(modelComponent->GetModel());
}
```
In case of a single component:
```
if (node_->HasComponent<StaticModel>()) {

    Model* model{ node_->GetComponent<StaticModel>()->GetModel() };
}
```

Is that what you were looking for?
There's also `Node::Clone()`, which might also be useful in your situation.

-------------------------

Tahri | 2017-11-27 22:57:25 UTC | #6

**Eugene:**

Thanks I started reading more in to components and looking at examples. I didn't read or learn them more than just createComponent<component>() and move on. Its more clear now how they operate.

**Modanung:**

This is exactly what I was looking for! Thank you. It seems very obvious now. I'll move on with my implementation with what you've posted. 

Much appreciated for the quick responses and support!

-------------------------

