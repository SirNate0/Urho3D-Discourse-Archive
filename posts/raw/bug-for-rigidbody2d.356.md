att | 2017-01-02 00:59:51 UTC | #1

[code]void RigidBody2D::ApplyLinearImpulse(const Vector2& impulse, const Vector2& point, bool wake)
{
    if (body_ && impulse != 0)
        body_->ApplyLinearImpulse(ToB2Vec2(impulse), ToB2Vec2(point), wake);
}[/code]

should be

[code]void RigidBody2D::ApplyLinearImpulse(const Vector2& impulse, const Vector2& point, bool wake)
{
    if (body_ && impulse != Vector2::ZERO)
        body_->ApplyLinearImpulse(ToB2Vec2(impulse), ToB2Vec2(point), wake);
}[/code]

because vector2 not offered int to vector2 construction.

-------------------------

aster2013 | 2017-01-02 00:59:51 UTC | #2

thanks,I will fix it.????????????

-------------------------

