itisscan | 2017-01-02 01:09:22 UTC | #1

I found one problem when window is minimized and then restored. So after window's minimizing camera start wrong behave. (Very fast rotate) 

I have captured this moment. 

 [url]https://www.youtube.com/watch?v=ZAqciLK8XVU&feature=youtu.be[/url]


Code that is responsible for camera rotation is following - 

[code]   
if (input_->GetMouseButtonDown(MOUSEB_RIGHT) || input_->GetMouseButtonDown(MOUSEB_MIDDLE))
{
        IntVector2 mouseMove = input_->GetMouseMove();
        if (mouseMove.x_ != 0 || mouseMove.y_ != 0)
        {
                activeView->cameraYaw_ += mouseMove.x_ * cameraBaseRotationSpeed;
                activeView->cameraPitch_ += mouseMove.y_ * cameraBaseRotationSpeed;

                if (limitRotation)
                    activeView->cameraPitch_ = Clamp(activeView->cameraPitch_, -90.0, 90.0);

                Quaternion q = Quaternion(activeView->cameraPitch_, activeView->cameraYaw_, 0);
                cameraNode_->SetRotation(q);
        }
}
[/code]

It seems that [b]input_->GetMouseMove()[/b] returns incorrect value after window's minimizing. 

May be someone already had this problem ? How can fix it ? Thanks.

-------------------------

rasteron | 2017-01-02 01:09:22 UTC | #2

I'm not sure but everything seems to be working on my end without any mouse or editor issues. Any console errors? You should post your specs and probably submit an issue @ github.

-------------------------

itisscan | 2017-01-02 01:09:23 UTC | #3

I have checked Urho3D samples. The same problem was occurred. 

Look,  [url]https://www.youtube.com/watch?v=trORkNlIyyQ[/url]

Errors did not appear in console output.

-------------------------

rasteron | 2017-01-02 01:09:23 UTC | #4

Great but then again, posting your specs would be better so others can replicate or might have some ideas with this problem. If you're just new to Urho3D, I suggest downloading the latest (v1.5) "release" sources for issues like this one:

[github.com/urho3d/Urho3D/releases](https://github.com/urho3d/Urho3D/releases)

-------------------------

itisscan | 2017-01-02 01:09:23 UTC | #5

I compile urho3d projects under Win7 64bit and Visual Studio 2013. I will try the latest version.

-------------------------

rasteron | 2017-01-02 01:09:23 UTC | #6

Just post an issue here: [github.com/urho3d/Urho3D/issues/new](https://github.com/urho3d/Urho3D/issues/new)

if you think you found a problem with the latest build. I still suggest trying out the 1.5 release version or with other versions of VS. I'm only using VS2k8 express and MinGW and it works great.

-------------------------

itisscan | 2017-01-02 01:09:23 UTC | #7

I have compiled Urho3D 1.5 release version under Visual Studio 2013 and get the same problem. I am going to write issue.

-------------------------

cadaver | 2017-01-02 01:09:25 UTC | #8

This was an SDL bug related to non-Aero mode. Should be fixed now.

-------------------------

