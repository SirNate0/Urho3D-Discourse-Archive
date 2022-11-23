lezak | 2019-08-21 08:17:32 UTC | #1

I've started working on PhysX implementation some time ago, but due to lack of time progress is much slower then I would like it to be and because this situation propably won't change in the next few months, I've decided to release this addon in it's current unfinished state:
https://github.com/lezak/Urho3DPhysX
Basic functionality is already there, and I will be adding more features (articualtions, terrain colliders etc.) in the future. I'm also planning to provide AngelScript bindings.
Besides the PhysX wrapper, there's also modified Urho3DPlayer that allows to use this addon in the editor (use modified script files from PhysXData folder!) and some simple samples. 
I need to point out that there's no debug rendering for the editor so that's a big inconvenience. There's possibility to use PhysX build-in debug rendering (joints sample demonstrate how to enable it) or to use PhysX Visual Debugger by uncommenting all 'pvd' stuff in Physics.h and Physics.cpp files.

Since the addon recreates physx inheritance hierarchy, for now use <a href="https://gameworksdocs.nvidia.com/PhysX/4.1/documentation/physxguide/Index.html">PhysX documentation</a> and <a href="https://gameworksdocs.nvidia.com/PhysX/4.1/documentation/physxapi/files/index.html">API documentation</a> for details, later on I will try to provide proper comments in the code. 

There are some issues that I'm aware of:
<del>1. building debug executable will make previously created release executable unusable and vice-versa, so it's not possible to have both release and debug exes working - it's necessary to build in proper mode when switching between release/debug.</del>
2. sometimes there is an assertion failure when scene is released.

-------------------------

