Mike | 2017-01-02 00:57:34 UTC | #1

To render a model from both side, for example make a plane visible from upside & downside:

Lua:
[code]
-- Single material
object.material:SetCullMode(CULL_NONE)

-- For accessing/modifying multiple materials:
object:ApplyMaterialList("Materials/Asset.txt")
local i=0
while object:GetMaterial(i) ~= nil do
	object:GetMaterial(i):SetCullMode(CULL_NONE)
	i=i+1
end
[/code]

AngelScript:
[code]
// Single material
object.material.cullMode = CULL_NONE;

//For accessing/modifying multiple materials:
object.ApplyMaterialList("Models/Asset.txt");
uint i = 0;
while (object.materials[i] !is null)
{
    object.materials[i].cullMode = CULL_NONE;
    i=i+1;
}
[/code]

Editor:
- open the Material editor for your material to edit by clicking "Edit" in Material inspector (right panel) > Material
- then modify Cull mode (at the botom)from CCW (default) to None

-------------------------

