ucupumar | 2017-01-02 01:00:25 UTC | #1

I want to get view projection matrix on Angel script with this code:[code]Camera@ camera = cameraNode.GetComponent("Camera");
Matrix4 viewProj = camera.projection * camera.view;[/code]but it gives me error due to Matrix4 multiplied by Matrix3x4. The error messege is:[code]"No matching operator that take types 'const Matrix4&' and 'const Matrix3x4&' found"[/code]
It doesn't gives me error if I do exact multiplication on C++ code.
 I'm still learning Angelscript, how I'm supposed to do?

-------------------------

cadaver | 2017-01-02 01:00:25 UTC | #2

The multiply in question should work now if you pull the latest master.

-------------------------

ucupumar | 2017-01-02 01:00:26 UTC | #3

Thanks! 
I didn't realize it was a bug.  :stuck_out_tongue:

-------------------------

