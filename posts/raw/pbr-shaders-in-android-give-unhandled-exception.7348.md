Jens | 2022-11-10 09:25:50 UTC | #1

The unhandled error message below looks to be due to using GLSL ES versions below 3.00. Was discussed in this post from 2017:
 [PBR sample build problems on Android - Discussions / Support - Urho3D](https://discourse.urho3d.io/t/pbr-sample-build-problems-on-android/3837)

Is there any way round this? And if there were, is there any point trying to use PBR on  Android, or will the performance hit make it pretty useless?

```
Failed to compile pixel shader PBRLitSolid(IBL PBR):
ERROR: 0:20030: '-' : wrong operand types - no operation '-' exists that takes a left-hand operand of type 'const int' and a right operand of type 'mediump float' (or there is no acceptable conversion)
ERROR: 0:20030: 'pow' : no matching overloaded function found
ERROR: 0:20030: '*' : wrong operand types - no operation '*' exists that takes a left-hand operand of type 'const int' and a right operand of type 'const mediump float' (or there is no acceptable conversion)
ERROR: 0:20030: '+' : wrong operand types - no operation '+' exists that takes a left-hand operand of type 'mediump float' and a right operand of type 'const int' (or there is no acceptable conversion)
ERROR: 0:109: '1.0f' : Floating-point suffix unsupported prior to GLSL ES 3.00
ERROR: 0:109: '1.0f' : syntax error
```

-------------------------

SirNate0 | 2022-11-10 12:26:26 UTC | #2

1. Make sure the types are the same. I haven't looked at the code, but my guess is that it's something like `afloat - 1` and it needs to be `afloat - 1.0`.
2. Remove the `f` suffix or use gles 3.

-------------------------

Jens | 2022-11-10 18:26:20 UTC | #3

Right. I've never messed with shaders before, and don't have much of a clue.

Searched for litsolid.glsl file and could only find it in blender and UrhoSamples. So, I assume it is internal to Urho, but can be overriden somehow?
Do you know if there is any documentation about this? I've searched forums and come up blank.

-------------------------

orefkov | 2022-11-12 09:39:35 UTC | #4

Imho for PBR you need GLES 3.0 as minimum. Stock Urho3D support only GLES 2.0.
You may try use my patch for GLES 3.0 - https://discourse.urho3d.io/t/support-gles3-in-engine/5688/1

-------------------------

