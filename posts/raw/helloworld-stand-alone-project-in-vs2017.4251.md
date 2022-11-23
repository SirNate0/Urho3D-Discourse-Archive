capelenglish | 2018-05-22 21:00:45 UTC | #1

First, I'm trying to get up to speed on Urho3D using C++. I'm a C# developer and have minimal C++ experience.

I've followed [this process](https://discourse.urho3d.io/t/new-blank-project-in-vs2017-set-up-for-urho3d-solved/4071) and created a new VS2017 project. Now I'm trying to re-create the HelloWorld project from the samples as a stand alone project. In the HelloWorld example Solution Explorer there is a reference to Urho3D that is not in the blank project I created. I tried to add a reference to it, but can't seem to navigate to it. Did I miss something? 

Also, there is an #include "Sample.h" in HelloWorld.h. Do I need this in order to get a simple HelloWorld example up and running? My apologies for the newbe questions, but your help is greatly appreciated.

-------------------------

Miegamicis | 2018-05-22 21:21:47 UTC | #2

All the samples include the `Sample.h` file to avoid duplicate code in the repo. If you wan't to set up your project from those, copy `Sample.h` file in your project.

To use Urho3D as an external project, set environment variable URHO3D_HOME which should lead to Urho3D build tree. If you downloaded compiled binaries, this variable should point to a place, where you extracted this library.

-------------------------

capelenglish | 2018-05-23 14:48:10 UTC | #4

That worked. Thanks!

-------------------------

Sehlit | 2018-05-23 15:00:51 UTC | #5

Haha, I'm a C# developer too, and I'm going to use C++ in Urho because unfortunately there is no good C# scripting support :(. I know how to link libraries, and I don't understand why you have to set an environment variable (Path?)... can't you just link Urho statically or so?

-------------------------

