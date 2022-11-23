zedraken | 2017-07-31 07:19:22 UTC | #1

Hello,

I encountering a quite strange issue. I have create an object model under Blender and I would like to use that single model to create several objects within my application.
I create N nodes and for each one, I create a static model from the resource related to the model file "Models/Gate.mdl".
Here is the code snippet I use…

    for(i = 0; i < 10; i++)
    {
      Node *myNode = mScene->CreateChild("Gate" + String(i));
      myNode->SetPosition(Vector(…, …, …));
      StaticModel *myModel = myNode->CreateComponent<StaticModel>();
      myModel->SetModel(mResourcesCache->GetResource<Model>("Models/Gate.mdl"));
      myModel->ApplyMaterialList();
    }

However, when I execute that code, I have some strange behaviors when I look at the objects. It seems that sometimes or depending on my camera position, some are visible and other are not, and they appear and disappear in a random fashion.
So my main question is : is it possible (and maybe relevant) to create several objects from the same unique resource ? Do I have to duplicate the model resource to have one duplicated resource associated with one node ? I mean that if I create 10 nodes, do I have to create 10 different resources of the same model ?
It is a little bit confusing to me, so any clarifications would be very welcome.

My best regards !

-------------------------

Dave82 | 2017-07-31 09:42:41 UTC | #2

[quote="zedraken, post:1, topic:3398"]
is it possible (and maybe relevant) to create several objects from the same unique resource ?
[/quote]

Absolutely !.See example20  huge object count.The whole point of resources are to share them whenever possible.

" I have some strange behaviors when I look at the objects. It seems that sometimes or depending on my camera position, some are visible and other are not, and they appear and disappear in a random fashion."

This is more likely a bounding box issue.Can you debug your geometry aabb ?

-------------------------

zedraken | 2017-07-31 09:41:21 UTC | #3

Hi Dave,
thanks for your quick answer. I had a look at the "HugeObjectCount.cpp" file and it gives a clear answer to my question.
I should have had a look at it first before posting my question on the forum, I apologize ;) I will take care of the provided examples for next times.
Anyway, this really helps and I did not know about the StaticModelGroup class. It seems to be very useful.
Thanks !

-------------------------

slapin | 2017-07-31 10:35:56 UTC | #4

Also some people encounter issue similar to yours with auto-instancing. Try to disable it and see
if that fixes your problem. Instancing from resources should work without StaticModelGroup too
and without side-effects.

-------------------------

