ucupumar | 2017-01-02 00:59:20 UTC | #1

On this [url=http://discourse.urho3d.io/t/depthmode-and-reconstruct-position-using-linear-depth/273/1]thread[/url], I have reconstruct view space position using linear depth.
The problem is I want to transform view space position back to world space but I couldn't get/find View Inverse matrix on Urho. How to get that one on Urho?

Thanks in advance.

-------------------------

ucupumar | 2017-01-02 00:59:21 UTC | #2

Nevermind, I just found it. On C++ code:
[code]Matrix4 viewInverseMatrix = Matrix4() * MainCamera->GetView(); // GetView() returns Matrix3x4, so on default it cannot do transpose
viewInverseMatrix = viewInverseMatrix.Transpose().Inverse();[/code]
I've tested on my shader and it works. So, viewMatrix is transpose of Camera->GetView() and viewInverseMatrix is transpose inverse of Camera->GetView(). 
I'm not math expert but why we need to transpose to get real view matrix?  :question:

-------------------------

