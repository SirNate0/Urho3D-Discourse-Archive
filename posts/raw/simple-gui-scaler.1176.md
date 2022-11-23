practicing01 | 2017-01-02 01:05:53 UTC | #1

Call RecursiveAddGuiTargets() on a UIElement to give it the stats then ElementRecursiveResize() on it (both after loading the gui).  I also stick it inside an E_RESIZED handler.
[code]
void Urho3DPlayer::ElementRecursiveResize(UIElement* ele)
{
	Vector3 targetRes, targetSize, targetPos;

	targetRes = ele->GetVar("targetRes").GetVector3();
	targetSize = ele->GetVar("targetSize").GetVector3();
	targetPos = ele->GetVar("targetPos").GetVector3();

	if (targetRes != Vector3::ZERO)
	{

		IntVector2 rootExtent;

		rootExtent.x_ = graphics_->GetWidth();
		rootExtent.y_ = graphics_->GetHeight();

		IntVector2 scaledExtent;

		scaledExtent.x_ = ( targetSize.x_ *  rootExtent.x_ ) / targetRes.x_;
		scaledExtent.y_ = ( targetSize.y_ *  rootExtent.y_ ) / targetRes.y_;

		ele->SetSize(scaledExtent);

		IntVector2 scaledPosition = IntVector2(
				( targetPos.x_ *  rootExtent.x_ ) / targetRes.x_,
				( targetPos.y_ *  rootExtent.y_ ) / targetRes.y_);

		ele->SetPosition(scaledPosition);

	}

	for (int x = 0; x < ele->GetNumChildren(); x++)
	{
		ElementRecursiveResize(ele->GetChild(x));
	}

}

void Urho3DPlayer::RecursiveAddGuiTargets(UIElement* ele)
{
	Vector3 targetRes, targetSize, targetPos;
	IntVector2 v2;

	targetRes = Vector3(800, 480, 0);
	ele->SetVar("targetRes", targetRes);

	v2 = ele->GetSize();

	if (v2 == IntVector2::ZERO)
	{
		v2 = IntVector2(800, 480);
	}

	targetSize = Vector3(v2.x_, v2.y_, 0.0f);
	ele->SetVar("targetSize", targetSize);

	v2 = ele->GetPosition();
	targetPos = Vector3(v2.x_, v2.y_, 0.0f);
	ele->SetVar("targetPos", targetPos);

	for (int x = 0; x < ele->GetNumChildren(); x++)
	{
		RecursiveAddGuiTargets(ele->GetChild(x));
	}
}
[/code]

-------------------------

