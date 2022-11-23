Leith | 2019-05-30 03:15:31 UTC | #1


I have exported a static object "by node" to an xml file.
When I instantiate the object using Scene::InstantiateXML, I get an error message in the console about my xml file not being a valid model.
The call returns successfully - the returned node has a staticmodel component with a valid model resource which works in the scene perfectly...

[code]
        if(ModelName.EndsWith(".xml"))
        {
            auto e = cache->GetResource<XMLFile>(ModelName)->GetRoot();
            Node* newnode = node_->GetScene()->InstantiateXML(e,Vector3::ZERO, Quaternion::IDENTITY);
[/code]

-------------------------

Leith | 2019-06-09 02:32:34 UTC | #2

This issue was resolved - it was a simple logical error in the code I use to instantiate models.
My code was attempting to locate named models in the resourcecache even when the filepath indicated that it should be loading from xml. Since my code was returning a valid object, I failed to notice the bug which resided early in the function in question.

-------------------------

