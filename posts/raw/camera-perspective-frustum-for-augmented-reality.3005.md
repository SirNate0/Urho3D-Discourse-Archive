SteveU3D | 2017-04-20 10:38:19 UTC | #1

Hi,

I made a long time ago an application in openGL to do augmented reality, and I want to do it with Urho3D now.
I have the intrinsic parameters of my camera, optic center (cx, cy) and focal (fx, fy).
In openGL, I set the camera with : 

    glFrustum(-_near*cx/(GLfloat)fx,_near*(FRAMEWIDTH-cx)/(GLfloat)fx,_near*(cy-FRAMEHEIGHT)/(GLfloat)fy,_near*cy/(GLfloat)fy,_near,_far);

The prototype is : 

    glFrustum(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar);

What's the equivalent in Urho3D? I saw that there is a frustum class in Urho3D but in the camera class, there is no "SetFrustum" function, only GetFrustum(). So how to assign a frustum to a scene?

I tried : 

    camera->SetAspectRatio((float)FRAMEWIDTH/(float)FRAMEHEIGHT);
    camera->SetFov(CV_MAT_ELEM( *intrinsic_matrix, float,0,0));
    camera->SetNearClip(0.1f);
    camera->SetFarClip(1000.0);

but it doesn't give the expected result.

-------------------------

kostik1337 | 2017-04-14 12:50:35 UTC | #2

Maybe, you can use Camera::SetProjection, which sets custom projection matrix?

-------------------------

SteveU3D | 2017-04-14 14:21:16 UTC | #3

Indeed, I was looking to it and the post : 
http://discourse.urho3d.io/t/set-custom-project-matrix-in-camera/2195/8

It should do what I need, I'll try.
Thansk!

-------------------------

SteveU3D | 2017-04-19 14:55:43 UTC | #4

So I tried different things, also following the answer of cadaver here http://discourse.urho3d.io/t/how-to-dynamic-switch-gl-projection-and-gl-modelview/2229/2 where he explains projection, model and view matrices that must be applied to the camera and the scene, but I still can't have the good result for augmented reality.
I put a box in the scene and it must translate and rotate the same way as a chessboard. I get the rotation (matrice and vector) and translation (vector) of the chessboard with openCV.


Here is my openGL code that works. I want to convert it to Urho3D.

    //rotation and translation matrix
    GLfloat RTMat[16]={
			CV_MAT_ELEM( *rotMat, float, 0,0),
			-CV_MAT_ELEM( *rotMat, float, 1,0),
			-CV_MAT_ELEM( *rotMat, float, 2,0),
			0.0f,
			CV_MAT_ELEM( *rotMat, float, 0,1),
			-CV_MAT_ELEM( *rotMat, float, 1,1),
			-CV_MAT_ELEM( *rotMat, float, 2,1),
			0.0f,
			CV_MAT_ELEM( *rotMat, float, 0,2),
			-CV_MAT_ELEM( *rotMat, float, 1,2),
			-CV_MAT_ELEM( *rotMat, float, 2,2),
			0.0f,
			tX,    //translation onX
			tY,    // ... Y
			tZ,    // ... Z
			1.0f
		};

    glViewport(0,0,FRAMEWIDTH,FRAMEHEIGHT);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    float _near=0.1f, _far=1000.0;

    //(fx, fy) focal length on X and Y, (cx, cy) optical center		
    glFrustum(-_near*cx/(GLfloat)fx,_near*(FRAMEWIDTH-cx)/(GLfloat)fx,_near*(cy-FRAMEHEIGHT)/(GLfloat)fy,_near*cy/(GLfloat)fy,_near,_far);
    
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glMultMatrixf(RTMat);


Does anybody know the good "conversion" to Urho3D?
Thanks.

-------------------------

SteveU3D | 2017-04-20 10:38:31 UTC | #5

It's OK, I just used SetPosition and SetRotation on my object node. My first tests had some errors in the computed vlaues :unamused:.

-------------------------

