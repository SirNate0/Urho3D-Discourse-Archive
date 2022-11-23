Xardas | 2017-01-02 00:59:01 UTC | #1

Specifically, a ScriptInstance with a script object. Is this somehow possible?

-------------------------

thebluefish | 2017-01-02 00:59:02 UTC | #2

You can move a component from one node to another with:
[code]GetNode()->AddComponent(item, 0, Urho3D::REPLICATED);[/code]

This assigns the component to the new node and marks it as dirty for the network. Afterwards you're free to do whatever you want with the old Node, it no longer references this component. I'm not 100% sure how this affects ScriptInstance, but I don't see any reason why it wouldn't work.

-------------------------

Xardas | 2017-01-02 00:59:02 UTC | #3

Yes, I've actually tried that method before, but then I get the following warning messages:

"Node is detached from scene, can not subscribe script object to update events" (this is located in ScriptInstance::UpdateEventSubscription())

"Unknown attribute name in XML data"

"Unknown attribute value in XML data"

-------------------------

cadaver | 2017-01-02 00:59:02 UTC | #4

Moving a component after creation is not supported, so if you attempt to do it you'll run into various problems such as the above. I recommend to rethink the program so that moving is not needed, for example simply destroy/recreate the component, though that will cause it to lose state. Another way is to create the component in both nodes in the beginning but disable/enable it as needed.

-------------------------

Xardas | 2017-01-02 00:59:02 UTC | #5

I wouldn't necessarily mind destroying and recreating the component, but if that will still cause it to lose state then there is no point in doing that.

I guess another option would be to keep the component in a separate node, and then just move the node? Although that probably won't be too good for performance if I expect to have a lot of these. By the way, are there any performance penalties of disabled nodes vs no nodes, except for maybe recursive searches?

-------------------------

cadaver | 2017-01-02 00:59:03 UTC | #6

If moving the node in the hierarchy is an appropriate solution logic-wise, then I would say to go ahead. Except for the added workload in world transform matrix concatenation, the engine itself should not induce more overhead due to a more complex scene node hierarchy, ie. it's never the engine that does for example recursive searches, but the application.

Whether disabled nodes induce overhead depends on the components contained in the node. For example Drawable components remove themselves from the Octree when disabled, so for the rendering subsystem it's roughly like they didn't exist at all, except for their memory footprint. Disabled nodes / components remain in the node's child & component containers just like enabled ones, so they will affect iteration and search times when you call Node's GetChildren(), GetComponent() etc. functions.

-------------------------

Xardas | 2017-01-02 00:59:03 UTC | #7

Thanks for the clarification.

I did solve the problem without using nodes, be just recreating the component and then setting the new component's attributes based on the old one. I just used the code from Node::CloneRecursive():

[code]
const Vector<AttributeInfo>* compAttributes = component->GetAttributes();
for (unsigned j = 0; j < compAttributes->Size(); ++j)
{
    const AttributeInfo& attr = compAttributes->At(j);
    if (attr.mode_ & AM_FILE)
        cloneComponent->SetAttribute(j, component->GetAttribute(j));
}
[/code]

-------------------------

thebluefish | 2017-01-02 00:59:03 UTC | #8

That brings me to wonder why we don't have a way to directly clone a component in the first place. Since "moving" components isn't directly supported, it means half my code is being done wrong. I added a Node::CloneComponent function and created a pull request to the master branch. That should make it a bit easier in the future  :stuck_out_tongue:

-------------------------

Xardas | 2017-01-02 00:59:03 UTC | #9

That's great, although in my case where I create a script object with the script instance, I still have to do it like this:

[code]
ScriptInstance* newInstance = newNode->CreateComponent<ScriptInstance>();
newInstance->CreateObject(oldInstance->GetScriptFile(), oldInstance->GetClassName());

const Vector<AttributeInfo>* compAttributes = oldInstance->GetAttributes();
for (unsigned j = 0; j < compAttributes->Size(); ++j)
{
	const AttributeInfo& attr = compAttributes->At(j);
	if (attr.mode_ & AM_FILE)
		newInstance->SetAttribute(j, oldInstance->GetAttribute(j));
}
[/code]

Otherwise, the changes made to a script object aren't preserved.

So maybe we could check if the component to be cloned is a ScriptInstance with a script object. If that's the case, then call CreateObject on it before copying the attributes?

-------------------------

thebluefish | 2017-01-02 00:59:04 UTC | #10

Hm, maybe I approached it the wrong way then. The attributes certainly get duplicated, but that's as far as it goes. The internal state outside of the attributes will not exist.

How does this ScriptInstance object behave across serialization/deserialization?

On another idea, it might be better to have a virtual Component::Clone that could then be overridden. Then complex components like ScriptInstance could override it with any special needs. Use would be something like:
[code]node->AddComponent(item->Clone());[/code]

-------------------------

cadaver | 2017-01-02 00:59:04 UTC | #11

The idea in Urho3D serialization is that setting all the attributes and calling ApplyAttributes() at the end should be all that's necessary (ApplyAttributes was missing from the pull request btw.) Cloning should be just the same as loading, no need to add special-case functions.

However what needs to be verified is that when a script object defines public variables that should appear as editable/serializable attributes, that those are copied correctly when cloning. In that case the ScriptInstance component modifies its own attribute list on the fly once the script object has been created. I can check that later today.

-------------------------

thebluefish | 2017-01-02 00:59:04 UTC | #12

Node::CloneRecursive doesn't appear to call ApplyAttributes(), which is why I missed it. Does that then need to be changed as well?

-------------------------

cadaver | 2017-01-02 00:59:04 UTC | #13

Node::Clone() should call Node::ApplyAttributes() at the very end, which propagates to call ApplyAttributes() on all components and child nodes.

-------------------------

thebluefish | 2017-01-02 00:59:04 UTC | #14

Ah, OK that makes sense now.

-------------------------

cadaver | 2017-01-02 00:59:04 UTC | #15

There was a little over-eager optimization which caused the unique script object attributes to not get cloned. It is fixed in the master branch now.

-------------------------

