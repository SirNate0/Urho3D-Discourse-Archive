att | 2017-01-02 01:12:01 UTC | #1

Hi, mouse does  not correctly work on mac, when the demo is running, the mouse can not be grabbed.

-------------------------

hdunderscore | 2017-01-02 01:12:01 UTC | #2

Which demo? Is this with retina display enabled?

-------------------------

att | 2017-01-02 01:12:01 UTC | #3

[quote="hd_"]Which demo? Is this with retina display enabled?[/quote]

I do not know how to enable retina, all demo has problem with mouse on my mac book pro.
And the editor does not work correctly, all buttons are very small, clicked position is away from the button. :cry:

-------------------------

weitjong | 2017-01-02 01:12:01 UTC | #4

Yes, that sounds like a retina problem after SDL 2.0.4 upgrade. The issue has been tracked here. [github.com/urho3d/Urho3D/issues/1252](https://github.com/urho3d/Urho3D/issues/1252). Since your MBP has a retina display, you can help us to debug the problem. But if you don't have time and just want to get on with your own project then you can just disable the SDL_WINDOW_ALLOW_HIGHDPI flag in the OGLGraphics.cpp.

-------------------------

weitjong | 2017-01-02 01:12:02 UTC | #5

In the master branch, the High DPI mode is now disabled by default.

-------------------------

att | 2017-01-02 01:12:05 UTC | #6

[quote="weitjong"]Yes, that sounds like a retina problem after SDL 2.0.4 upgrade. The issue has been tracked here. [github.com/urho3d/Urho3D/issues/1252](https://github.com/urho3d/Urho3D/issues/1252). Since your MBP has a retina display, you can help us to debug the problem. But if you don't have time and just want to get on with your own project then you can just disable the SDL_WINDOW_ALLOW_HIGHDPI flag in the OGLGraphics.cpp.[/quote]

The problem seems to be due to the window size and draw size(graphics size).
[code]
void Input::CenterMousePosition()
{
    int w, h;
    SDL_GetWindowSize(window_, &w, &h);
    const IntVector2 center(w / 2, h / 2);
    if (GetMousePosition() != center)
    {
        SetMousePosition(center);
        lastMousePosition_ = center;
    }
}[/code]

[code]IntVector2 Input::GetMousePosition() const
{
    IntVector2 ret = IntVector2::ZERO;

    if (!initialized_)
        return ret;

    SDL_GetMouseState(&ret.x_, &ret.y_);
    
    int w, h;
    SDL_GetWindowSize(window_, &w, &h);
    float scale = graphics_->GetWidth() / w;
    ret.x_ *= scale;
    ret.y_ *= scale;
    return ret;
}
[/code]

-------------------------

weitjong | 2017-01-02 01:12:06 UTC | #7

This is what I understood, in high DPI window mode the "screen coordinates" measurement is not equal to the "pixels", so some of our existing scaling logic in the code may not work as expected. I am not sure if these are the only places that have such scaling logic. However, I have commented in the issue tracker that I don't think correcting the mouse movement is enough. Instead, I believe it is the UI subsystem that needs to be enhanced to properly support the high DPI mode. Currently our UI subsystem does not rescale itself accordingly in its E_SCREENMODE event handler. I (and Lasse too) don't have retina display to perform this work and validate the change. PR is welcome.

-------------------------

cadaver | 2017-01-02 01:12:06 UTC | #8

There was a PR some time ago which added UI scaling possibility (UI::SetScale / UI::GetScale) so using it would be an easy way to adapt the UI, if you don't care about losing the pixel-perfect sharpness, or don't want to design a separate UI for retina. That together with fixing Input to report all positions and events in the Graphics pixel dimensions should fix the issue, at least to a basic degree.

-------------------------

hdunderscore | 2017-01-02 01:12:06 UTC | #9

I think when I looked the UI::Scale also changes the rendering size? Might need to add a new private member similar to scale. I don't have a retina mac to test with, but maybe something like this could work:

[code]int wX, wY, rX, rY;
SDL_Window* window = GetSubsystem<Graphics>()->GetWindow();
SDL_GL_GetDrawableSize(window, rX, rY);
SDL_GetWindowSize(window, wX, wY);
Vector2 inputScale_ ((float)rX / (float)wX, (float)rY/ (float)wY);[/code]

-------------------------

cadaver | 2017-01-02 01:12:07 UTC | #10

Yes, UI scale changes rendering, resizes the root element (smaller if scale is > 1) and inversely scales the event coordinates that are received from Input. Would probably need a new member function in Graphics to tell the window size / pixel ratio, so that application can make an informed decision of UI scaling.

-------------------------

