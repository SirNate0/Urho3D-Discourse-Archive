cosar | 2018-11-07 23:48:55 UTC | #1

Hi,

I noticed that the Urho3D is using Shader Model 4.0 for DirectX 11. Is there any reason not to use Shader Model 5.0?

Thank you!

-------------------------

Sinoid | 2018-11-08 02:15:02 UTC | #2

None of the SM5 features are available in engine, so all you're missing from SM5 are intrinsic functions (lightning fast `rcp` being the most significant one) which are mostly still not present in GLSL which means you can't use them without writing slow versions for GL (or dumping it).

SM4 will also work on the 10_1 and 10_0 feature levels. If you force SM5 to be used then only DX11 feature levels 11_0 and onward will work.

If you really really want to, it's a pretty easy change. For GS/HS/DS I just up to SM5 when there's a Hull+Domain shader involved and otherwise leave it as SM4 ... though I still debate the advantages of fast rcp (and a few other DX only niceties), especially with DX10 hardware almost extinct.

---

TL;DR: you have to go into the renderer guts to get more of the significant gains that come with upping the min feature level than just another shader-model version - ie. structured buffers for instanced skeletal animation (doable but crippled on DX10), etc.

-------------------------

cosar | 2018-11-08 17:38:01 UTC | #3

Thank you for your answer!
I understand the desire to be compatible with as much hardware as possible, but in this case we are talking about cards produced for a couple of years almost 10 years ago. Whoever targets those, can still use DX9 (and even the need to support DX9 is debatable).

-------------------------

