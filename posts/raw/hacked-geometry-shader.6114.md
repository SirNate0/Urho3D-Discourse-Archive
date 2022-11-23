najak3d | 2020-04-23 07:07:26 UTC | #1

Since we only need ONE geometry shader, and it appears that Urho3D doesn't really support Geometry Shaders--  I was wondering if there is some Hack method for getting geometry shaders to fit into the render path?    We'd like to feed a simple array of "Line Points" into the shader, and then have the Geometry Shader create the Width inside the GPU.

We change these line points often, and so want to remove work load and extra RAM requirements from the main program.  We are using UrhoSharp.

All seems to be going pretty well so far.   We have it rendering pretty nicely what we want, and are now wondering if we'll be able to optimize the logic via use of Geometry shaders.

-------------------------

rku | 2020-12-09 01:23:53 UTC | #2

You already know of this, just posting it as a reference for others.

Experimental geometry shader implementation is saved at https://github.com/eugeneko/Urho3D/commits/GeometryShaders

-------------------------

