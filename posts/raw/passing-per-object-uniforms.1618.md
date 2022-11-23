theak472009 | 2017-01-02 01:08:58 UTC | #1

Hello,
How would I go about passing per-object uniforms. I know there are constant buffers (ObjectVS, ObjectPS) but if I add a new uniform to the cbuffer
Example: 
cbuffer ObjectVS
{
  ...
  ...
#ifdef CONDITION
  float2 param;
#endif
  ...
}
How would I set "param" through code? Where would I have to call Graphics::SetShaderParameter (...) ?

Thanks.

-------------------------

ghidra | 2017-01-02 01:08:58 UTC | #2

One way I have done it, is to clone the material for each object I put it on (Which I cant claim is still valid, this code is a little bit old at this point)
In Anglescript...
[code]
Material@ bmat = cache.GetResource("Material", "Materials/mymat.xml");
Material@ rmat = bmat.Clone();

Color myCol = Color(Random(1.0f),Random(1.0f),Random(1.0f),1.0f);
rmat.shaderParameters["ObjectColor"]=Variant(myCol);//single quotes didnt work
[/code]

-------------------------

cadaver | 2017-01-02 01:09:00 UTC | #3

Currently the best way is indeed to clone a material. There was a branch dealing with per-object uniforms but it hasn't progressed to master, and related to the rendering internals it is actually roughly the same as using a different material, and slightly complicates things.

-------------------------

