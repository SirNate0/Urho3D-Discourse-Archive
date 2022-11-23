namkazt | 2017-01-02 01:14:03 UTC | #1

Hi,

here is a simple example with openGL
[code]

// ortho to display 2d background
glMatrixMode(GL_PROJECTION);
glPushMatrix();
glLoadIdentity();

//... my code

// restore previous proj and cam pos
glMatrixMode(GL_PROJECTION);
glPopMatrix();
glMatrixMode(GL_MODELVIEW);
glPopMatrix();


// display 3D model
glMatrixMode(GL_MODELVIEW);
glLoadMatrixd(Model matrix4 )

// other code
[/code]

How can i do this with Urho3D and how can i set iModelMatrix in shader.


Edit: Addition informations
i'm working on an ARLib and using Urho3D as render lib and input lib.
i need to pass Matrix4 that is Pose of model to display it as AR model.

thank you

-------------------------

cadaver | 2017-01-02 01:14:03 UTC | #2

It depends on whether you work with the high level rendering (have a scene and define a viewport to Renderer) or low-level (using Graphics class directly)

If using high-level, use a recent master branch revision to be able to set custom projection matrix to Camera. Model and view matrices are defined by a scene node's world transform, and the camera's world transform.

If using low-level, you can set all shader parameters explicitly. See e.g. the UI rendering code (UI.cpp) and SetCameraShaderParameters in View.cpp.

-------------------------

namkazt | 2017-01-02 01:14:03 UTC | #3

thank you, i'm keep researching on it.

-------------------------

