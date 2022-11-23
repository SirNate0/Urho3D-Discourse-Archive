Modanung | 2021-12-25 23:55:43 UTC | #1

Seems to work pretty well.

```
GUI::GUI(Context* context): Object(context),
    guiScene_{ new Scene{ context } },
    guiCamera_{ guiScene_->CreateChild("Camera")
                         ->CreateComponent<Camera>() },
    guiRenderer_{ guiScene_->CreateComponent<DebugRenderer>() }
{
    guiScene_->CreateComponent<Octree>();

    SharedPtr<Viewport> viewport{
        new Viewport{ context_, guiScene_, guiCamera_ } };
    SharedPtr<RenderPath> renderPath{
        viewport->GetRenderPath()->Clone() };
    renderPath->RemoveCommand(0);
    viewport->SetRenderPath(renderPath);
    GetSubsystem<Renderer>()->SetViewport(1, viewport);

    guiCamera_->GetNode()->SetWorldPosition(Vector3::BACK);
    guiCamera_->SetOrthographic(true);
    guiCamera_->SetOrthoSize(GRAPHICS->GetHeight());

    SubscribeToEvent(E_POSTRENDERUPDATE, DRY_HANDLER(GUI, Draw));
    SubscribeToEvent(E_SCREENMODE, DRY_HANDLER(GUI, HandleScreenModeChanged));
}

void GUI::HandleScreenModeChanged(StringHash eventType, VariantMap &eventData)
{
    guiCamera_->SetOrthoSize(GRAPHICS->GetHeight());
}
```

And of course I'm trying it out with some harmonic elements. :slight_smile:

```
void GUI::DrawElipse(const Vector2& center,
                     const Vector2& size, const Color& color)
{
    TypedPolynomial<Vector2> ellipse{};
    ellipse.SetPolynomialType(0, PT_HARMONIC_SIN);
    ellipse.SetPolynomialType(1, PT_HARMONIC_COS);
    ellipse.SetCoefficient(0, center);
    ellipse.SetCoefficient(1, size * .5f);

    const int segments{ 100 };
    const float dt{ 1.f / segments };
    for (int i{ 0 }; i < segments; ++i)
    {
        guiRenderer_->AddLine({ ellipse.Solve((i) * dt) },
                              { ellipse.Solve((i + 1.f) * dt) }, color);
    }
}
```

-------------------------

Modanung | 2021-12-17 11:20:15 UTC | #2

Because who doesn't want [hypocycloids](https://en.wikipedia.org/wiki/Hypocycloid) as GUI elements? :grin:

![hypocycloids|690x388](upload://wLsjJpqlrg9swmsDXaucRsx6i5W.png)

Each defined by a single `TypedPolynomial<Vector2>`.

-------------------------

GodMan | 2021-12-18 00:07:09 UTC | #3

So what does this do exactly?

-------------------------

Modanung | 2021-12-18 01:09:27 UTC | #4

It draws shapes. :slight_smile: 

Could you be more specific?

-------------------------

