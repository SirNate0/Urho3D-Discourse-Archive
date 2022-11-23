crisx | 2017-09-15 11:20:18 UTC | #1

Hi

I tried to create an object animation on a Text element, but it doesn't seem to work. Is it possible to use object animations on UI elements?

Here's the code I've used:

    candyText_ =(new Text(context_));
	candyText_->SetText(std::to_string(candyAmount).c_str());
	candyText_->SetFont(cache->GetResource<Font>("Fonts/comicbd.ttf"), 50);
	candyText_->SetColor(Color(211.0f / 255, 87.0f / 255, 254.0f / 255));
	candyText_->SetPosition(180.0, -342.0);
	candyText_->SetOpacity(0.75);
	candyText_->SetTextEffect(TE_SHADOW);
	// Align Text center-screen
	candyText_->SetHorizontalAlignment(HA_CENTER);
	candyText_->SetVerticalAlignment(VA_CENTER);
	// Add Text instance to the UI root element

	// Create animation
	SharedPtr<ObjectAnimation> candyTextAnimation(new ObjectAnimation(context_));
	SharedPtr<ValueAnimation> positionAnimation(new ValueAnimation(context_));
	// Use spline interpolation method
	positionAnimation->SetInterpolationMethod(IM_SPLINE);
	// Set spline tension
	positionAnimation->SetSplineTension(0.7f);
	positionAnimation->SetKeyFrame(0.0f, Vector2(180.0,-342.0));
	positionAnimation->SetKeyFrame(1.0f, Vector2(180.0, -350.0));
	positionAnimation->SetKeyFrame(2.0f, Vector2(180.0, -342.0));
	positionAnimation->SetKeyFrame(3.0f, Vector2(180.0, -350.0));
	positionAnimation->SetKeyFrame(4.0f, Vector2(180.0, -342.0));
	// Set position animation
	candyTextAnimation->AddAttributeAnimation("Position", positionAnimation);

	SharedPtr<ValueAnimation> rotationAnimation(new ValueAnimation(context_));
	rotationAnimation->SetKeyFrame(0.0f, 20.0);
	rotationAnimation->SetKeyFrame(1.0f, -10.0);
	rotationAnimation->SetKeyFrame(2.0f, 20.0);
	candyTextAnimation->AddAttributeAnimation("Rotation", rotationAnimation);

	candyText_->SetObjectAnimation(candyTextAnimation);

	GetSubsystem<UI>()->GetRoot()->AddChild(candyText_);

Also tried to apply the animation on the UIElement:

    UIElement * candyTextElement = GetSubsystem<UI>()->GetRoot()->GetChild(GetSubsystem<UI>()->GetRoot()->GetNumChildren()-1);
	candyTextElement->SetObjectAnimation(candyTextAnimation);

Edit: It seems to work for Position (not Rotation) on Sprite objects but not on Text objects.

-------------------------

