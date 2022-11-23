Sir_Nate | 2017-01-02 01:12:35 UTC | #1

When trying a Debug build on Emscripten (changed from what was originally a Release (the default) build), it has been failing on trying to build the Urho3DPlayer with:
[code]error: unresolved symbol: _ZN6Urho3D6ObjectD2Ev
error: unresolved symbol: _ZN6Urho3D12Constraint2DD2Ev
error: unresolved symbol: _ZN6Urho3D8DrawableD2Ev
error: unresolved symbol: _ZN6Urho3D10SerializerD2Ev
error: unresolved symbol: _ZN6Urho3D10AnimatableD2Ev
error: unresolved symbol: _ZN18btTriangleCallbackD2Ev
error: unresolved symbol: _ZN6Urho3D9ComponentD2Ev
error: unresolved symbol: _ZN31btInternalTriangleIndexCallbackD2Ev
error: unresolved symbol: _ZN6Urho3D10RefCountedD2Ev
error: unresolved symbol: _ZN6Urho3D12DeserializerD2Ev
error: unresolved symbol: _ZN30btActivatingCollisionAlgorithmD2Ev
error: unresolved symbol: _ZN23btStridingMeshInterfaceD2Ev
error: unresolved symbol: _ZN6Urho3D11BorderImageD2Ev
[/code]
Any suggestions?

-------------------------

weitjong | 2017-01-02 01:12:35 UTC | #2

I am able to reproduce this problem. However, there is no reason I can think of for it to behave that way. It looks like a bug in the emcc, although I could be wrong.  I am using 1.36.0 on Linux in my test. What is yours? 

Below is the reason why I believe it is emcc's bug. What weird is that the symbols are actually there. It's just that they all have some number suffix when built using Debug build configuration.

Release build configuration
[code]-------- T _ZN6Urho3D6ObjectD0Ev
-------- T _ZN6Urho3D6ObjectD1Ev
-------- T _ZN6Urho3D6ObjectD2Ev[/code]
Debug build configuration
[code]-------- T _ZN6Urho3D6ObjectD0Ev
-------- T _ZN6Urho3D6ObjectD1Ev
         U _ZN6Urho3D6ObjectD2Ev
-------- T _ZN6Urho3D6ObjectD2Ev.22994[/code]

The above is tested using SHARED lib type (bitcode).

-------------------------

Sir_Nate | 2017-01-02 01:12:35 UTC | #3

The same (1.36.0 on Linux), but with a STATIC build.

I noticed the same thing, with the .#####, though in my case it was .10170, appended, and likewise I have no idea of the cause. 

I can say, though, that if you build your project, or the Urho3DPlayer for example, dropping the release build library in place of the debug libUrho3D.a, it did compile, and it still contained some useful debugging information, like a stack trace on various errors (though it is possible that this is always the case with Emscripten -- I haven't used it enough to know).

-------------------------

weitjong | 2017-01-02 01:12:35 UTC | #4

Perhaps we should try their "incoming" branch first, before raise it as an issue to Emscripten issue tracker. I recall Debug build was fine with one of their older versions. And in debug mode, we can actually see the C++ source code when stepping thru in the browser's debugger, so it is quite useful.

-------------------------

