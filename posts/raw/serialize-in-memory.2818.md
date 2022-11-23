dakilla | 2017-02-23 14:57:13 UTC | #1

I'd like to save and load some objects in memory at runtime (not in files) and without cloning, to manage some prefabs and instancing.

this xml version does not work : 

    Node* node = m_scene->CreateChild("MyNode");
    node->SetPosition(Vector3(-2,0,10));
    StaticModel* staticModel = node->CreateComponent<StaticModel>();
    staticModel->SetModel(cache->GetResource<Model>("Models/Mushroom.mdl"));
    staticModel->SetMaterial(cache->GetResource<Material>("Materials/Mushroom.xml"));

    XMLElement xmlElement;
    node->SaveXML(xmlElement);

    Node* node2 = m_scene->InstantiateXML(xmlElement, Vector3(2,0,10), Quaternion(0, Vector3(0,0,0)));


However json version works :

> Node* node = m_scene->CreateChild("MyNode");
> node->SetPosition(Vector3(-2,0,10));
> StaticModel* staticModel = node->CreateComponent<StaticModel>();
> staticModel->SetModel(cache->GetResource<Model>("Models/Mushroom.mdl"));
> staticModel->SetMaterial(cache->GetResource<Material>("Materials/Mushroom.xml"));

> JSONValue jsonElement;
> node->SaveJSON(jsonElement);

> Node* node2 = m_scene->InstantiateJSON(jsonElement, Vector3(2,0,10), Quaternion(0, Vector3(0,0,0)));


What i'm missing in xml version ?
Thnaks

-------------------------

Eugene | 2017-02-23 20:31:43 UTC | #2

[quote="dakilla, post:1, topic:2818"]
What i'm missing in xml version ?
[/quote]

You shan't use XMLElement since it doesn't store anything. Use XMLFile.

-------------------------

dakilla | 2017-02-23 20:11:36 UTC | #3

thanks that worked. :thumbsup:

-------------------------

