practicing01 | 2017-01-02 01:03:26 UTC | #1

Urho is missing high-level helper functions that would be usable for most game types such as moving a node to a position over time.  With the help of people from the IRC channel and the interwebs, I'm trying to create some of those components and have put them here: [github.com/practicing01/Urho3DTemplate](https://github.com/practicing01/Urho3DTemplate)  They may have bugs or be unoptimized as they're a work-in-progress. Example for moving a node to a position over time:

[code]

#include "SceneObjectMoveTo.h"
#include "Scene.h"
#include "SceneEvents.h"
#include "Variant.h"

#include "DebugNew.h"

SceneObjectMoveTo::SceneObjectMoveTo(Context* context) :
		LogicComponent(context)
{
	isMoving_ = false;
	// Only the scene update event is needed: unsubscribe from the rest for optimization
	SetUpdateEventMask(USE_UPDATE);
}

void SceneObjectMoveTo::OnMoveToComplete()
{
	VariantMap vm;
	vm[SceneObjectMoveToComplete::P_NODE] = node_;
	SendEvent(E_SCENEOBJECTMOVETOCOMPLETE,vm);
}

void SceneObjectMoveTo::MoveTo(Vector3 dest, float speed, bool stopOnCompletion)
{
	moveToSpeed_ = speed;
	moveToDest_ = dest;
	moveToLoc_ = node_->GetWorldPosition();
	moveToDir_ = dest - moveToLoc_;
	moveToDir_.Normalize();
	moveToTravelTime_ = (moveToDest_ - moveToLoc_).Length() / speed;
	moveToElapsedTime_ = 0;
	moveToStopOnTime_ = stopOnCompletion;
	isMoving_ = true;
}

void SceneObjectMoveTo::Update(float timeStep)
{
	if (isMoving_ == true)
	{
		inderp_ = timeStep * moveToSpeed_;
		remainingDist_ = (node_->GetWorldPosition() - moveToDest_).Length();
		node_->SetWorldPosition(node_->GetWorldPosition().Lerp(moveToDest_, inderp_ / remainingDist_));
		moveToElapsedTime_ += timeStep;
		if (moveToElapsedTime_ >= moveToTravelTime_)
		{
			isMoving_ = false;
			if (moveToStopOnTime_ == true)
			{
			}
			OnMoveToComplete();
		}
	}
}

[/code]

-------------------------

GoogleBot42 | 2017-01-02 01:03:27 UTC | #2

I think that you are right although I think I should mention Urho3D does have support for tweening variables...

See here [url]http://urho3d.github.io/documentation/1.32/_attribute_animation.html[/url]

-------------------------

