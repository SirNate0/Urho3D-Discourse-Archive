ab4daa | 2019-04-30 13:44:11 UTC | #1

Hi,
I encountered shader parameter problem, maybe it is not the root cause, just want to share my observation and ask for comment.

The problem is when I port outline shader to 2nd scene, the outline is always enabled, but 1st scene works fine.
I eventually get to `Graphics::SetShaderParameter(StringHash param, bool value)` in D3D11Graphics.cpp.
It seems the "buffer" will be overwritten and overwritten during drawing batches and batches, so the initial value of the bool cbuffer is a dirty value.
![1-2|690x388](upload://t2IQXhxnkVCDnksKF6S2Bqkq85x.png) 

The code only set 1 byte while the cbuffer actually holds 4 bytes.
![2-2|690x388](upload://eF1tE97PFkUnMH6Wdt8KOsMuts1.png) 

A quick dirty fix can fix the problem on my side.
![%E5%9C%96%E7%89%87|678x159](upload://ArGrEzCOfyYlyMhI5eA6mxHLe5n.png) 

Not sure this is the right place to fix, any comment is welcome, thank you.

-------------------------

Leith | 2019-05-01 05:59:43 UTC | #2

Your compiler has a concept that a native boolean can be represented using a single byte in memory - this is a compiler optimization. When the parameter is sent to the shader, it uses a function provided by the underlying graphics api - in your case, DirectX. The translation of the native type to the shader type is meant to be handled by the local graphics api runtime. Any issues with transforming native system values to shader types, and particularly the primitives like bool, are likely to be driver issues, as this is outside of the scope of Urho3D - strictly speaking, urho uses graphics api to pass typed values, it's not Urho's fault if the shader is misinterpreting them. At least, if it is, I am very interested.

-------------------------

