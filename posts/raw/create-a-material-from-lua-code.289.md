robertotena | 2017-01-02 00:59:24 UTC | #1

Hello, I'd like to create a custom material from Lua code instead of loading it from the ResourceCache, but I just don't find a proper way.

I tried to modify a previously loaded one via 'SetShaderParameter', but it seems to modify the material to nullify its previous effects (I wouldn't recommend this option, anyway, as it is a cached resource):

[code]
local node = scene:CreateChild('CustomNode')
local component = node:CreateComponent('CustomGeometry')

component:DefineVertex(Vector3(-1.2, 1.2, 0))
component:DefineVertex(Vector3(-1, 1.2, 0))
component:DefineVertex(Vector3(-1.2, -1, 0))

component.material = cache:GetResource('Material', 'Materials/RedUnlit.xml')

component.material:SetShaderParameter('MatDiffColor', Vector4(0, 1, 0, 1)) -- to make it green, for example

component:Commit()

[/code]

I was trying to create it manually, but if I do 
[code]
local material = Material()
[/code]

the engine crashes. I guess it is because they must be created via resource factory, but how? I read in the docs about the global CreateObject method, but it does not seems to work, either. A little example would be very much appreciated!

-------------------------

friesencr | 2017-01-02 00:59:24 UTC | #2

The engine should never crash (within reason) from script usage.  You should report a bug.

-------------------------

cadaver | 2017-01-02 00:59:25 UTC | #3

I'd put it this way that the engine should never crash, except in Lua bindings :slight_smile: They are rather unsafe as due to performance reasons type checks and even null checks need to be left out (use CMake option -DURHO3D_SAFE_LUA=1 to enable the checks, but it'll be slower) so something as simple as forgetting to use : instead of . will easily crash.

In this case I believe you're being hit by the memory allocation behavior and interaction with the C++ side reference counting. To allocate an object that will be put into a C++ SharedPtr (in this case, the drawable component has a SharedPtr for holding the material) you should use the new() function instead of just constructing the object. This is explained on the "Lua scripting" documentation page.

So the usage of creating a material and applying it to an object would go like this:

[code]
        local mat = Material:new()
        mat:SetShaderParameter("MatDiffColor", Variant(Vector4(Random(1.0), Random(1.0), Random(1.0), 1.0)))
        component.material = mat
[/code]

-------------------------

aster2013 | 2017-01-02 00:59:25 UTC | #4

cadaver is right.

-------------------------

robertotena | 2017-01-02 00:59:25 UTC | #5

Great, it works, thank you! :slight_smile:

And now that I'm able to create materials... I wanted to set a technique but I'm having problems:

First I tried to do the same as with the material:

[code]
local tech = Technique:new()
[/code]
But its result is the message error:
attempt to call method 'new' (a nil value)

Could it be because the constructor is not exposed? [github.com/urho3d/Urho3D/blob/m ... hnique.pkg](https://github.com/urho3d/Urho3D/blob/master/Source/Engine/LuaScript/pkgs/Graphics/Technique.pkg)

Later, I tried to load it directly from the resource cache:
[code]
local tech = cache:GetResource('Techinque', 'Techniques/NoTextureOverlay.xml')
[/code]
But the error message is:
Could not load unknown resource type 94E6

In the end, to make it work as I wanted, I loaded a material with a technique, and retrieved the technique from there:

[code]
  component.material = Material:new()
  component.material:SetShaderParameter('MatDiffColor', Variant(Vector4(1.0 , 1.0, 1.0, 1.0)))

  local loadedMaterial = cache:GetResource('Material', 'Materials/RedUnlit.xml')
  component.material:SetNumTechniques(1)
  component.material:SetTechnique(0, loadedMaterial:GetTechnique(0))
[/code]

What did I miss in order to create or load a custom Technique? Was this behavior expected?

-------------------------

robertotena | 2017-01-02 00:59:25 UTC | #6

Nevermind... there was a typo  :blush: 

[code]
local tech = cache:GetResource('Techinque', 'Techniques/NoTextureOverlay.xml')
[/code]

must be

[code]
local tech = cache:GetResource('Technique', 'Techniques/NoTextureOverlay.xml')
[/code]

sorry for the waste, and thank you again

-------------------------

