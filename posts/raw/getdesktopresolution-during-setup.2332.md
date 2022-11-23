TheComet | 2017-01-02 01:14:48 UTC | #1

The following doesn't work because SDL is not initialised yet by this stage.

[code]void InGameEditorApplication::Setup()
{
    IntVector2 desktopResolution = GetSubsystem<Graphics>()->GetDesktopResolution();

    engineParameters_["WindowWidth"] = desktopResolution.x_;
    engineParameters_["WindowHeight"] = desktopResolution.y_;
}[/code]

What other options do I have? How does the editor make the window the correct size for that matter?

-------------------------

