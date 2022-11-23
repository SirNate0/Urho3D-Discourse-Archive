reattiva | 2017-01-02 01:13:12 UTC | #1

Hello, I've tried to port the code of "Rasterized Voxel-based Dynamic Global Illumination" by Hawar Doghramachi:
[hd-prg.com/RVGlobalIllumination.html](http://hd-prg.com/RVGlobalIllumination.html)
It is only a port, all credits to the original author.
It is DirectX11 only, you can find it here:
[github.com/reattiva/Urho3D/tree/GI_work](https://github.com/reattiva/Urho3D/tree/GI_work)
The main code is here: .\Source\Work\WorkTests\SampleRVGI.cpp
The render path (Data/RVGI/RenderPaths/RVGI.xml) has a brief explanation of what it is doing.

It is still incomplete, has only one voxel grid (two in the original code) and there are some problems: random flickering (this can be solved with a temporal filter), light bleeding through walls, pixellated look... the original sample looks better.

It is so so, but what was implemented to make it work maybe can be useful (DirectX11 only):
geometry shaders, compute shaders, structured buffers (called ShaderBuffer) for reading (StructuredBuffer) and writing (RWStructuredBuffer) from compute and pixel shaders, compute command for the render path, manual unbinding of graphic resources (SRV, UAV, RT) (very useful), texture arrays as output (render targets) for pixel and compute shaders, null triangle command (this is similar to the quad command but can be instanced, it is useful to write to texture arrays), option to disable the stencil view (again, useful for writing to texture arrays), option to set a per-pass cull mode, per-command shaders parameters for scene pass commands, jumps and repetitions in the render path.

I've added some examples, they are in the same directory, see the selector in main.cpp.

Video: [webmshare.com/ww16j](http://webmshare.com/ww16j) (does not represent the quality of the original work)

-------------------------

franck22000 | 2017-01-02 01:13:12 UTC | #2

Very impressive amount of work done here :slight_smile: 

Are you planning to make some separate pull request for adding compute, geometry shaders supports and all new renderpath commands in Urho ? That would be awesome for everyone.

-------------------------

hdunderscore | 2017-01-02 01:13:13 UTC | #3

Screenshot?

-------------------------

codingmonkey | 2017-01-02 01:13:13 UTC | #4

Great work! It will be nice to see all this cool canges in master even without GI :slight_smile:

-------------------------

reattiva | 2017-01-02 01:13:14 UTC | #5

I'm not planning to do a pull request. It is DirectX11 only, the OpenGL (and script) part is totally missing and it probably requires OpenGl 4.3. Other users have already fully implemented geometry shaders. Also I cannot give support for these changes, and I don't want to dump it on the maintainers. Anyway, if you need help you can ask here.
This was already an old sample, a month ago I decided to tidying it up and organize it. Unfortunately now it is already too old for the master (Urho is very healthy). 
I'll post some images.

-------------------------

franck22000 | 2017-01-02 01:13:14 UTC | #6

If you are agree reattiva i can make some pull request based on your work to integrate Geometry shaders and compute shaders support in Urho for DX11 API only for now (Will try OpenGL implementation and left it for someone else if i can't do it). I have been asking Cadaver and he is agree on his side. 

Is it ok for you ?

-------------------------

reattiva | 2017-01-02 01:13:15 UTC | #7

franck, you don't even need to ask, it's 100% ok.
However let me be pedant, can you also support it? I don't want to push more work on Cadaver's shoulders. Maybe, a separate branch kept updated with the master by somebody else, could be better (but unknown and out of range for many users).
And please take a look at the code, my approach to problems was always hacky, a workaround with less effort possible (which is good if you want to merge time to time with the master branch). However some problems should have been solved in a more brave, organic and elegant way.
Be sure to ask Cadaver before starting to work on it, compute shaders could be really off scope.

-------------------------

cadaver | 2017-01-02 01:13:15 UTC | #8

The somewhat tricky thing with both geometry and compute is that at this point Urho itself requires them for absolutely nothing, there are no test cases / examples. Same could be said of e.g. texture arrays too, though.

In that sense they could be quite low-maintenance features, as most don't even notice or use them. But yes, definitely the hope is that once you contribute something, you practically know it best and it's certainly better if you also have time in the future to even out possible rough spots.

-------------------------

godan | 2017-01-02 01:13:21 UTC | #9

For what it's worth - I would *love* to see this functionality become part of Urho. My main use of the Urho is for fairly computationally intensive tasks, so the ability to farm some of that off to graphics card is very appealing.

-------------------------

dragonCASTjosh | 2017-01-02 01:13:21 UTC | #10

i think compute would allow allot of opportunity to optimize Urho under all API's that support it

-------------------------

codingmonkey | 2017-01-02 01:13:22 UTC | #11

Yes, gs and cs wery useful in some cases :slight_smile:

Riattivas's implement very nice/legant decision with introduce the ShaderKey, i suppose.

-------------------------

reattiva | 2017-01-02 01:13:22 UTC | #12

Actually, I've borrowed that from Boberfly's modern OpenGL branch.
But I wonder, how probable is a collision?
I've tested another way, more crude and clumsy but with no collision. 
We store the shaders pointers in a PODVector. For each new combination we store this PODVector in a list and we store the real shader program in another list (or create a struct for the two and use only one list). These two lists are kept in synch, so a PODVector and its corresponding program have the same index in the two lists.
When we search for an existing combination, we skim the list, find its index and use this index to get the program from the other list.
This can be slower than a simple map search, but for a hundred of combinations should still be comparable, I think.

[code]
    /// Shader programs search keys.
    Vector<PODVector<ShaderVariation*> > shaderProgramsKeys_;
    /// Shader programs.
    Vector<SharedPtr<ShaderProgram> > shaderPrograms_;


    PODVector<ShaderVariation*> key(3);
    key[0] = computeShader_ ? computeShader_ : vertexShader_;
    key[1] = pixelShader_;
    key[2] = geometryShader_;

    Vector<PODVector<ShaderVariation*> >::Iterator iKey = shaderProgramsKeys_.Find(key);
    if (iKey != shaderProgramsKeys_.End())
        shaderProgram_ = shaderPrograms_[iKey - shaderProgramsKeys_.Begin()];
    else
    {
        ShaderProgram* newProgram = new ShaderProgram(this, vertexShader_, pixelShader_, geometryShader_, computeShader_);
        shaderProgramsKeys_.Push(key);
        shaderPrograms_.Push(SharedPtr<ShaderProgram>(newProgram));
        shaderProgram_ = newProgram;
    }
[/code]

-------------------------

codingmonkey | 2017-03-28 02:23:19 UTC | #13

I think need desing the right arhetecture what take into account the future code changes in shader related part of urho. For example for future easy adding TES-shader. 
Alos you are right, I don't think what key search are dramaticaly slow or mostly impact on perfomance.

collisions:
In previous my trying i use some parts of your code for testing but part what placed in void Renderer::SetBatchShaders(Batch& batch, Technique* tech, bool allowShadows) works not well in my case, because it not take into account the shaders defenitions (auto pushed defs with vsi, gsi, psi) I suppose in most cases vsi= gsi (because vertex data flows from vs into gs, the same interpolators are used by both) but I decide to devide this into separated parts, for situation where GS-shader will have own unique auto-def.  

so my impl looks like this:

http://pastebin.com/Es5JVPY5

-------------------------

ab4daa | 2020-03-18 04:32:30 UTC | #14

Hello,

I want to have UAVs in shaders so trying to merge some codes from the repo.

Unfortunately after merge the smoke billboards in sample 07_Billboards becomes invisible.

GI_work repo has same problem.

Is it supposed to break the sample or some tweak should be done?

Thanks!

EDIT:
It's strange that if removing mushrooms and floors, the smoke is visible.
But once add back the mushrooms or floors the smoke becomes invisible.
So far have no idea what to check :sob:

EDIT2:
Got some luck with renderdoc, which points out size mismatch of some constant buffer in some vertex shaders.
When searching for existed constant buffer with same name, should check its size, too.
Because same cbuffer might be different size with different compile flag.

https://github.com/reattiva/Urho3D/blob/GI_work/Source/Urho3D/Graphics/Direct3D11/D3D11Graphics.cpp#L2259-L2268

In this case, it is the ObjectVS will have problem.(size is different depends on BILLBOARD)

https://github.com/reattiva/Urho3D/blob/GI_work/bin/CoreData/Shaders/HLSL/Uniforms.hlsl#L129-L138

-------------------------

