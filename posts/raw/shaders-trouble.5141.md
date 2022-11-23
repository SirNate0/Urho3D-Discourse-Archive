franck22000 | 2019-05-07 18:13:45 UTC | #1

Hello I have some trouble to convert a glsl shader to hlsl. 

I don't know how to translate this into hlsl: 

camVec = transpose(tbn) * camVec;

Could someone help me on this issue ? Thanks a lot !

-------------------------

GodMan | 2019-05-07 21:33:47 UTC | #2

Well for `camVec` that is either a ` float3` or `float4`, transpose is a function and `tbn` is `Tangent BiNormal "Some call it Bitangent"`, and `n` is usually just the `normal` multiplied by the variable `camVec`.

.

-------------------------

GodMan | 2019-05-07 21:35:15 UTC | #3

Also forgot to mention that some of these variables, and function are already defined in urho3d shaders. You will have to substitute them in your shader.

-------------------------

