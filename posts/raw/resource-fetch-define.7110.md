Modanung | 2022-01-01 18:39:13 UTC | #1

Just a quick one-line tip: I found fetching resources to be a bit tedious and spacy. This simple define seems like the best solution I've found so far.
```
#define RES(x, y) GetSubsystem<ResourceCache>()->GetResource<x>(y)
```
----
Turning...
```
boxModel->SetModel(GetSubsystem<ResourceCache>()->GetResource<Model>("Models/Box.mdl"));
```
...into:
```
boxModel->SetModel(RES(Model, "Models/Box.mdl"));
```

-------------------------

lebrewer | 2021-12-27 17:00:37 UTC | #2

That is a nice tip. Always found a few things to be quite verbose with Urho.

-------------------------

