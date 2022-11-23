Bluemoon | 2017-01-02 01:01:58 UTC | #1

In Scripts the Node class has the GetChildrenWithScript() methods with an overloaded one that even takes the ScriptObjects name, but in C++ this very useful method is missing. Is there any particular reason why it was implemented in Scripts and not in the C++ code.

-------------------------

codingmonkey | 2017-01-02 01:01:59 UTC | #2

i'm not use scripts at all. but i guess it's can taked like that, as filter component
[code]PODVector<Node*> objects; 
scene_->GetChildrenWithComponent<ScriptInstance>(objects, true);
[/code]

it would be cool
if it introduced a system of tags and for them to take the lists of objects, and do raycasts by tags.
but at now had to take all objects of scene and manualy filtered by node.vars("tag or type") == "some my tag or type"

-------------------------

