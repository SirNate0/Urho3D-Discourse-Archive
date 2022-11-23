TrevorCash | 2018-01-05 23:02:30 UTC | #1

Can someone shed some light on why I get a crash in the following test code:

> 	//temp tests
> 	Node* myNode = scene_->CreateChild();
> 	WeakPtr\<StaticModel> gridComp = WeakPtr\<StaticModel>(myNode->CreateComponent\<StaticModel>());
> 	
> 	URHO3D_LOGINFO(String(gridComp.Refs()));// 1
> 	gridComp->GetNode()->Remove();
> 	URHO3D_LOGINFO(String(gridComp.Refs()));// 0
> 	if (gridComp.NotNull()) {
> 		gridComp->GetNode()->Remove(); //crash here
> 	}

This does print 0 references:
> URHO3D_LOGINFO(String(gridComp.Refs()));// 0

But this is returning true:

> gridComp.NotNull()

I must be missing something simple.  I want to use the gridComp variable as a way of polling whether the staticmodel still exists or not which I thought was the reason to use weakptr.

-------------------------

TrevorCash | 2018-01-05 23:02:54 UTC | #2

Answered my own question - I should be using Expired() instead of NotNull().

Working Code:

> 	Node* myNode = scene_->CreateChild();
> 	WeakPtr\<StaticModel> gridComp = WeakPtr\<StaticModel>(myNode->CreateComponent\<StaticModel>());
> 	
> 	URHO3D_LOGINFO(String(gridComp.Refs()));// 1
> 	gridComp->GetNode()->Remove();
> 	URHO3D_LOGINFO(String(gridComp.Refs()));// 0
> 	if (!gridComp.Expired()) {
> 		gridComp->GetNode()->Remove();
> 	}

Appologies - This should be in the support section, not sure how to move it.

-------------------------

