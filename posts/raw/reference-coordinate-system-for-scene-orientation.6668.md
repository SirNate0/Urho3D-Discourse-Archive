HJ2012 | 2021-01-20 06:44:22 UTC | #1

Hi all, I have created a dynamic geometry where I can display a scene and rotate and move the camera. Now I would like to display a reference coordinate system in one corner, where I can always see how the scene is currently oriented. That is, as it is displayed in CAD programs, for example. Is there an easy way in Urho3D to do this?
Thanks a lot to you!

-------------------------

WangKai | 2021-01-20 07:31:53 UTC | #2

Basically, what you need to do is to take the **inversed view matrix of the camera** and use it to rotate small axis set which has 3 arms and X, Y, Z texts (**axes rotate bacause you rotate the camera**), and finally draw the axes in the corner of your window viewport.

Try to implement **`AddLine`** and **`AddText`** with anything you can to do (Debug renderer, CustomGeometry, 2D, GUI elements, etc) to draw on the screen viewport (in screen space).

```c++
void DrawScreenAxes(const Vector2& axisOrig, float axisLen)
{
    if (!camera_)
        return;

    const Matrix3x4& viewInverse = camera_->GetView();

    Vector3 axisXVec = viewInverse * Vector4(Vector3::RIGHT, 0.0f) * axisLen;
    Vector3 axisYVec = viewInverse * Vector4(Vector3::UP, 0.0f) * axisLen;
    Vector3 axisZVec = viewInverse * Vector4(Vector3::FORWARD, 0.0f) * axisLen;

    Vector2 axisXEnd = axisOrig + Vector2(axisXVec.x_, -axisXVec.y_);
    Vector2 axisYEnd = axisOrig + Vector2(axisYVec.x_, -axisYVec.y_);
    Vector2 axisZEnd = axisOrig + Vector2(axisZVec.x_, -axisZVec.y_);

    ImGui::GetWindowDrawList()->AddLine(ImVec2(axisOrig.x_, axisOrig.y_), axisXEnd, ImColor(255, 0, 0));
    ImGui::GetWindowDrawList()->AddText(ImVec2(axisXEnd.x_ + 4.0f, axisXEnd.y_ - ImGui::GetFont()->FontSize * 0.5f), ImColor(255, 0, 0), "X");

    ImGui::GetWindowDrawList()->AddLine(ImVec2(axisOrig.x_, axisOrig.y_), axisYEnd, ImColor(0, 255, 0));
    ImGui::GetWindowDrawList()->AddText(ImVec2(axisYEnd.x_ + 4.0f, axisYEnd.y_ - ImGui::GetFont()->FontSize * 0.5f), ImColor(0, 255, 0), "Y");

    ImGui::GetWindowDrawList()->AddLine(ImVec2(axisOrig.x_, axisOrig.y_), axisZEnd, ImColor(0, 0, 255));
    ImGui::GetWindowDrawList()->AddText(ImVec2(axisZEnd.x_ + 4.0f, axisZEnd.y_ - ImGui::GetFont()->FontSize * 0.5f), ImColor(0, 0, 255), "Z");
}
```

This is what you get-
![image|370x262](upload://bgPZLf3XAwTMwTe9tik8fsMp0de.png)

-------------------------

JSandusky | 2021-01-20 23:18:27 UTC | #3

You can also setup another view containing a separate scene with axis model(s) and some Text3Ds with the viewport set to where you want it to be. That's more useful if you want an interactive coordinate-frame like you see in Unity/Blender/etc.

The camera for that scene being positioned along the -Z axis (arbitrary distance) and you as above use the view-matrix of the other camera to transform the node containing everything.

See 09_MultipleViewports sample, though there they're setup to view the same scene.

-------------------------

Modanung | 2021-01-21 00:22:17 UTC | #4

[quote="JSandusky, post:3, topic:6668"]
That’s more useful if you want an interactive coordinate-frame [...]
[/quote]

...or would want to avoid using (non-default) ImGui.

Depending on the usecase, you might also get away with using the debug rederer to draw some lines.

-------------------------

