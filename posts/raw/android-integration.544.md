hakkis | 2017-01-02 01:01:17 UTC | #1

Hi,

I have started to get familiar with Urho3D for Android. My plan is to use Urho3D as part of my existing app, but I have faced some problems.

In my app I have GLSurfaceView with Renderer. Currently I do some OpenGL  (ES 2) rendering (just a 3D model) in Java side. In native side I do some image processing and also opengl rendering stuff. Now I try to replace java side model rendering with Urho3D, but I would like to keep GLSurfaceView with renderer in java side (mainly because of the onDrawFrame() method in Renderer). It this approach possible? 

I pass the Surface (from java side) to the native side and I use the ANativeWindow_fromSurface() function to get ANativeWindow pointer (not null). However, the Graphics always fails in SetMode() method (LOGERROR("Could not open window")).  I have tried with and without Graphics's SetExternalWindow. 

I basically would need only Urho3D::Graphics, Urho3D::Renderer and Urho3D::Scene. Is it possible to use Urho3D without Urho3D::Engine?

So, is my approach even possible? Any hints how to achieve this? Thanks!

-------------------------

cadaver | 2017-01-02 01:01:17 UTC | #2

Using Urho as part of existing Android application like you describe is not something we plan for, or have tests for. Originally Urho was written as a strict hierarchy of libraries so in theory nothing should depend on Engine, as long as you setup your required subsystems. Usually about everything will require FileSystem & ResourceCache at least.

I'm not sure if SDL on Android can tolerate using any other surface than the one that SDL Java code setups. You will have to look at SDL's code to be sure.

-------------------------

