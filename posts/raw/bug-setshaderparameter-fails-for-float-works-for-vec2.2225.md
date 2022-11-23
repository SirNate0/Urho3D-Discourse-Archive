krstefan42 | 2017-01-02 01:14:02 UTC | #1

I just ran into this strange behavior. When I declare in my GLSL code (worldToTex is the only place this uniform is used in the shader):
[code]uniform float cHeightMapSize;

vec2 worldToTex(vec2 c) {
	c += vec2(cHeightMapSize*.5);
	c += vec2(.5);
	c /= cHeightMapSize;
	return c;
}[/code]
Use this as the XML material file:
[code]<material>
    <technique name="Techniques/Terrain.xml"/>
    <parameter name="HeightMapSize" value="2048." />
    <parameter name="TerrainDisplacement" value="16." />
</material>[/code]
And set it in the Lua script like this:
[code]renderMaterial:SetShaderParameter("HeightMapSize", Variant(2048.))[/code]
Nothing happens, I always get 0 for the value of the parameter.

But when I declare cHeightMapSize as a vec2 in the shader, initialize it to  value="2048. 2048."in the XML, and in Lua call SetShaderParameter with Variant(Vector2(2048.,2048.)), everything works as expected.  I can post the full code if necessary.

-------------------------

cadaver | 2017-01-02 01:14:02 UTC | #2

This is a problem with Lua numbers. I verified that creating a float uniform and assigning it in material XML works fine. However when you create a Variant in Lua that way, it actually ends up holding a double, which the shaders can't take. I believe I'll put in a check in Material::SetShaderParameter() that a double is automatically converted to a float.

-------------------------

cadaver | 2017-01-02 01:14:02 UTC | #3

Fixed in master branch.

-------------------------

weitjong | 2017-01-02 01:14:03 UTC | #4

I believe this is a general issue when boxing Lua's number into Urho's Variant. Number in Lua is implemented using double-precision floating-point number. So, when you construct a Variant as you have done, the Lua/C++ binding will use the constructor which takes a single double parameter. As this is a general issue, you may find the mismatch to manifest itself in other cases. IMHO, it is not possible to safe-guard this in all our API against this mismatch. What to do then? If I were you then I would explicitly use another constructor which take 2 parameter, the type and the number.

[code]Variant(const char* type, const char* value);   // For storing a numerical type into Variant , value could be just a number[/code]
Remember that Lua is a typeless language, so the second parameter could actually be passed with a number instead of string. Observe:

[code]test1 = Variant(0.123)
print(test1:GetTypeName())   // double
test2 = Variant("float", 0.123)
print(test2:GetTypeName())  // float[/code]

-------------------------

