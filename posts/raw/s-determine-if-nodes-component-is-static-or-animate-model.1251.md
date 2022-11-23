George | 2017-01-02 01:06:24 UTC | #1

Hello,
I want to determine if the first component in my Node use a Static or Animated node.
Is there a flag, enum, type or anything in the component to recognise this?

Thanks
George

-------------------------

1vanK | 2017-01-02 01:06:24 UTC | #2

If I understand the question

[code]
AnimatedModel* animatedModel = GetComponent<AnimatedModel>();
if (animatedModel)
{
}
else
{
    StaticModel* staticModel = GetComponent<StaticModel>();
    if (staticModel)
    {
    }
}
[/code]

-------------------------

George | 2017-01-02 01:06:24 UTC | #3

Thanks mate,
At the moment I'm using the same technique.
But that would slow down, because I'm trying to get to the bounding box in the update method.

Since I would later have more than 1k nodes and calculate their position based on bounding boxes.

I want to see if there is a flag for each of the component. So that I can directly point to the correct component by GetComponents[index].

Regards
George.

-------------------------

1vanK | 2017-01-02 01:06:24 UTC | #4

Maybe for nodes with the StaticModel set name "static" and for nodes with the AnimatedModel set name "animated" and then compare the names, although I do not think that this will give a significant performance boost

EDIT: maybe the code seems not enough fast, because you're testing a Debug build?

-------------------------

George | 2017-01-02 01:06:24 UTC | #5

At the moment the Component::GetTypeName() give similar to what you have mentioned.

I hope it to have something like an enum to differentiate different build in types.

But I guess flexibility way is the string method.

Regards,
George

-------------------------

jmiller | 2017-01-02 01:06:25 UTC | #6

I've also used code like [b]1vanK[/b] describes. GetComponent() compares by StringHash which is unsigned (fairly fast).

Node::SetVar() could store type info in advance, though I guess GetVar() would also be searching var names by StringHash.

*edit* for example,

[code]
  // Construct StringHash once
  const StringHash VAR_MODEL_TYPE("modelType");

  node_->SetVar(VAR_MODEL_TYPE, StaticModel::GetTypeStatic()); // or AnimatedModel, whatever

  StringHash modelType(node_->GetVar(VAR_MODEL_TYPE).GetStringHash());
  if (modelType == StaticModel::GetTypeStatic()) {
    //...
  } else /* if (modelType == AnimatedModel::GetTypeStatic()) */ {
    //...
  }[/code]

-------------------------

cadaver | 2017-01-02 01:06:25 UTC | #7

If you want maximum speed you could also maintain lists for static & animated objects separately, instead of continuously checking which object is which. If the lists are Vector<WeakPtr<Node> > they will not interfere by keeping the nodes alive unnecessarily, but you can safely check for destruction (the WeakPtr will return null when the node is destroyed)

-------------------------

George | 2017-01-02 01:06:26 UTC | #8

Thanks,
I'll keep these ideas in mind.
Regards
George

-------------------------

