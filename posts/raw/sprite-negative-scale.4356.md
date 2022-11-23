Pihozamo | 2018-06-27 00:43:44 UTC | #1

I am trying to make a unit selection box similar to any RTS game, so what I've created a Sprite UIElement that updates its scale and size based on mouse position:

    if (mouseMoved_) {
		if (mouseLftDwn_) {
			const IntVector2 quadrant = boxSprite_->GetScreenPosition() - GetSubsystem<Input>()->GetMousePosition();
			if (quadrant.x_ >= 0 && quadrant.y_ >= 0) {
				boxSprite_->SetScale(-1, -1);
			} else if (quadrant.x_ >= 0 && quadrant.y_ < 0) {
				boxSprite_->SetScale(-1, 1);
			} else if (quadrant.x_ < 0 && quadrant.y_ < 0) {
				boxSprite_->SetScale(1, 1);
			}
			else {
				boxSprite_->SetScale(1, -1);
			}

			boxSprite_->SetSize(Abs(quadrant.x_), Abs(quadrant.y_));
		}
		mouseMoved_ = false;
	}

The problem is that it seems the Sprite cannot flip around a single axis only, it only works with SetScale(-1, -1) and SetScale(1, 1). Is there a solution to this? I don't understand why it can't have only of its axis negative.

-------------------------

