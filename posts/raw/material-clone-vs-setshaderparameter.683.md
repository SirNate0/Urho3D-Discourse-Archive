ghidra | 2020-03-13 22:56:02 UTC | #1

First,
I am trying to send a Random() color to my materials ObjectColor Paramter.
However, with out Cloning the material, it seems I only get the last random value, so that all my objects get the same color.
Does that sound right? So to get a unique color for each object, I need to Clone the Material? If I have Hundred of objects, will that have a lot of overhead?

Second,
It appears as though in AngleScript ateast that there is no SetShaderParameter(), but there is SetShaderParameterAnimation(). So If I only want to set a unique color, i have to make a ValueAnimation Object, and set 2 keyfarmes to the same value. Does that sound right? What is the overhead for having hundreds of clones with hundreds of animations?

In summation, I solved getting a unique color on my material per obejct. But I feel like I am doing things a little hacky. When it feels like I should just be calling SetShaderParameter on just and instance of a material.

Thanks.

-------------------------

aster2013 | 2020-03-13 22:55:57 UTC | #2

Current you can use Mateiral::Clone to do such thing, but it it better to set per object's shader parameter. it override material's shader parameter.

for second. you can use shaderParameter['Name'] = value in AS Script.

-------------------------

ghidra | 2017-01-02 01:02:08 UTC | #3

Thank you.
With your suggestion I was able to just set the parameter straight with no need for the animated parameter (like so, for completion sake):

[code]
StaticModel@ box = node.CreateComponent("StaticModel");
box.model = cache.getResource("Model","Models/Box.mdl");

Material@ mat = cache.GetResource("Material","material/research/simple.xml");
Material@ cmat = mat.Clone();

Color cl = Color(Random(1.0f),Random(1.0f),Random(1.0f),1.0f);
cmat.ShaderParameter["ObjectColor"]=Variant(cl);

box.material = cmat;
[/code]

However, I seem to still need to clone it. I was uncertain what you meant by "set per object's shader parameter".

-------------------------

cadaver | 2017-01-02 01:02:08 UTC | #4

Per object shader parameters are not in master branch yet, though there's a feature branch for it.

In AngelScript many of the Set / Get functions do not exist as such but use properties or indexed properties instead. The difference to C++ can sometimes be confusing. So in AngelScript you'd do the following to edit material parameters:

[code]
material.shaderParameters["MatDiffColor"] = Variant(Color(1,1,1,1));
[/code]

-------------------------

