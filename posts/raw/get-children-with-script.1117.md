Bluemoon | 2017-01-02 01:05:33 UTC | #1

Have really been enjoying working with the AngelScript API of Urho3D, It makes prototyping very very fast  :smiley: . 
Can the GetChildrenWithScipt(scriptObjectName, true/false) method of nodes and scene be modified to return scriptObject interfaces of base class when the specified script object name is that of a base class. 
For example :
[code]
    class A : ScriptObject
    {
        ...
    }

    class B : A
    {
        ...
    }

    class C: A
    {
        ...
    }
[/code]
Then in your code you create script objects of B and C into Nodes. When you call
[code]
    scene.GetChildrenWithScript("A", true)
[/code]
the returned array contains class A handles (or interface) for both B and C

-------------------------

cadaver | 2017-01-02 01:05:33 UTC | #2

This code has been added to master branch with slight modifications. Thanks!

-------------------------

Bluemoon | 2017-01-02 01:05:34 UTC | #3

[quote="cadaver"]This code has been added to master branch with slight modifications. Thanks![/quote]

I tried again but it seems not to work  :confused:

-------------------------

Bluemoon | 2017-01-02 01:05:42 UTC | #4

Thanks Sinoid and Cadaver, I've tested it out and it works good  :smiley:

-------------------------

Bluemoon | 2017-01-02 01:05:51 UTC | #5

Okay, so I got a bit adventurous and realized that I needed a similar function at the C++ end which in this scenario is to get children with derived components  :wink: A little addition to Node.h did the trick

Add to Node.h the following methods (I figured out that using template was the easiest way to get it to work)
[code]
template <class T> bool Node::HasDerivedComponent() const 
{ 
	T* component = GetDerivedComponent<T>();
	if(component)
	   return true;
	else
	   return false;
}

template <class T> void Node::GetChildrenWithDerivedComponent(PODVector<Node*>& dest, bool recursive) const
{
    dest.Clear();

    if (!recursive)
    {
        for (Vector<SharedPtr<Node> >::ConstIterator i = children_.Begin(); i != children_.End(); ++i)
        {
            if ((*i)->HasDerivedComponent<T>())
                dest.Push(*i);
        }
    }
    else
        GetChildrenWithDerivedComponentRecursive<T>(dest);
}

template <class T> void Node::GetChildrenWithDerivedComponentRecursive(PODVector<Node*>& dest) const
{
	for (Vector<SharedPtr<Node> >::ConstIterator i = children_.Begin(); i != children_.End(); ++i)
    {
        Node* node = *i;
        if (node->HasDerivedComponent<T>())
            dest.Push(node);
        if (!node->children_.Empty())
            node->GetChildrenWithDerivedComponentRecursive<T>(dest);
    }
}
[/code]

In line with the "GetChildrenWithComponentRecursive" method "GetChildrenWithDerivedComponentRecursive" has private access

-------------------------

