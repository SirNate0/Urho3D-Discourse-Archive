sejin | 2018-01-16 09:35:17 UTC | #1

HI.
I am using QT5 based URHO_OPENGL.
sample of URHO3D(vs2015) works normally with the opengl shader (test.glsl).
But ... using the shader in the development QT project (test.hlsl).
ERROR: Could not find resource Shaders/HLSL/test.hlsl
How do I use .glsl in a new QT project?
Anything I missed?

os: window10
urho3d / 1.7

Sorry .. I used Google Translator.

-------------------------

jmiller | 2018-01-17 06:56:06 UTC | #2

Hi,

No problem, I think.
You may want to symlink or copy Urho/CoreData and Urho/Data folders (which Urho automatically uses) to your application's working directory. (A similar step is performed when building Urho, which puts those resource directory symlinks into bin/ where they will be found by samples).

Some references for resources
  https://urho3d.github.io/documentation/HEAD/_resources.html
  https://github.com/urho3d/Urho3D/blob/master/Source/Samples/Sample.inl#L57
  https://urho3d.github.io/documentation/HEAD/_main_loop.html


[quote="sejin, post:1, topic:3948"]
How do I use .glsl in a new QT project?
[/quote]

GLSL shaders are used by default except on MS Windows platform, in which case you can run cmake (or cmake_*.sh) with -D URHO3D_OPENGL=1

-------------------------

