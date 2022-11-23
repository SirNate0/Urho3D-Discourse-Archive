scorvi | 2017-01-02 01:04:26 UTC | #1

hey,

Does someone know how to create urho3d project in github that can be used for travis-ci ? 
I cloned a Urho3d and setup travis-ci for that. I had to add [code]sudo: required[/code] and removed the "after_success" part.  And travis-ci compiled it. 
So now i wanted to create a project that uses Urho3d as a lib (e.g. Urho3dIDE). How can i do it ?

-------------------------

weitjong | 2017-01-02 01:04:27 UTC | #2

Our CI build test harness setup puts Urho3D library at the center of the test across many target platforms that Urho3D supports. Although the setup also shows how to build samples and tools and external projects using Urho3D as a 3rd-party library, it may not be the best example of how you should setup CI build for your own project. For that, may be you should look at how tundra-urho3d project setup their CI build. In that project, the center of things is not Urho3D library anymore.

-------------------------

