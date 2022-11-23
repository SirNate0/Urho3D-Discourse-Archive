PsychoCircuitry | 2019-11-11 01:51:22 UTC | #1

I had noticed that sometime after the 1.7 release the bloomhdr shader started looking awful, pixelated and not very "bloomy". I spent some time looking into it today and discovered the cause.

The bloom shader uses the passed in uniform variables for inverse size and offset. Documentation for renderpath says these uniforms are case sensitive to the render target name. Well apparently the cases don't match between the render targets and uniforms, so what was happening was just stacking pixelated textures with no blur.

The fix is simple, either capitalize the render target names in the render path xml or change the uniform definitions to lowercase.

I'm not sure what the preferred approach is as render targets seem to always be defined with lowercase names and uniforms always start c-uppercase.

This issue only occurred post 1.7 release.

Hope this is helpful to someone.

-------------------------

weitjong | 2019-11-11 04:41:01 UTC | #2

Could you raise this as a bug in our issue tracker. Thanks.

-------------------------

PsychoCircuitry | 2019-11-12 09:17:48 UTC | #3

Ok, posted to the issue tracker on GitHub.

Also, the ldr bloom shader is affected by this same issue.

-------------------------

Modanung | 2019-11-12 10:41:25 UTC | #4

https://github.com/urho3d/Urho3D/issues/2542

-------------------------

