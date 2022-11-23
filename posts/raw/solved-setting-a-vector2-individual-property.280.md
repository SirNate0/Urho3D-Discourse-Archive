Mike | 2017-01-02 00:59:22 UTC | #1

Trying to scale a sprite (healthBar) in lua using one of these lines of code, I experience a weird behavior:

[code]
		healthBar.scale.x = healthBar.scale.x - 1 / 10
		healthBar.scale = healthBar.scale - Vector2(1 / 10, 0)
[/code]
Both lines return the correct scale but only the last one 'updates' the UIElement's scale.

Same code in AngelScript complains that scale.x is read-only.

-------------------------

aster2013 | 2017-01-02 00:59:22 UTC | #2

[code]healthBar.scale.x[/code]
It look like:
[code]
    Vector2& scale = healthBar->GetScale();
    scale.x = scale.x - 1.0f / 10.0f;
[/code]

But when you call:
[code]healthBar.scale = healthBar.scale - Vector2(1 / 10, 0)[/code]]
It look like:
[code]
    Vector2& scale = healthBar->GetScale();
    healBar->SetScale(scale - Vector2(1.0f / 10.0f, 0.0f));
[/code]

    

It will call healthBar:GetScale(), then set the scale's x value.

-------------------------

Mike | 2017-01-02 00:59:22 UTC | #3

Thanks Aster, now I understand what's going on.

-------------------------

