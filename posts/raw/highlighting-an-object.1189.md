JulyForToday | 2017-01-02 01:05:59 UTC | #1

Okay, so I initially thought this would be something quick/easy to get working, but I keep running into problems.

What I want to do is have an object be highlighted while I mouse over it, like this:
[img]http://i.imgur.com/rFMFRNE.jpg[/img][img]http://i.imgur.com/hb7Yt19.jpg[/img]

The teapot is an instance of a Clickable class I created that derives from ScriptObject. When the cursor hovers over the teapot it shows text, and I want to modify the material to be noticeably highlighted. Once the cursor is no longer hovering over the object, the highlight should turn off, and the material return to it's original state.

I eventually want to do this with a shader, but I'm not that familiar with Urho's shader configuration (which is a little confusing), and can't quite figure out how to set that up (any suggestions on that would be appreciated). So in the meantime I thought I would just modify the material's color [url=http://urho3d.wikia.com/wiki/Customize_materials_(via_code)_%26_different_materials_per_model]like is done on the unofficial wiki[/url].

I can access the teapot's StaticModel, and I figured I would just get a reference to it's material using GetMaterial(), and then use GetShaderParamter() to get it's original diffuse color, save it to a variable, and then use SetShaderParameter() to modify the color. Then when the cursor stops hovering on the object I would use SetShaderParameter() again to restore the original color.

[b]The [url=http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_static_model.html#a2d417ab736ce45d119f02cf997c5289c]documentation for StaticModel[/url] clearly has a GetMaterial(), but I cannot seem to get it to work. I get an error message saying "No Matching Signatures to 'StaticModel::GetMaterial(const int)'. I'm passing a 0 as the index. I've tried declaring and passing it as a uint, and passing no argument (in case there was a default value). Same issue, not such function signature. I'm probably missing something simple here (like usual) but I can't see what it is.[/b]

Edit: And I am using Angelscript, which might have some bearing on this.

-------------------------

friesencr | 2017-01-02 01:05:59 UTC | #2

There is a script api reference in the Docs folder.

[github.com/urho3d/Urho3D/blob/m ... dox#L10883](https://github.com/urho3d/Urho3D/blob/master/Docs/ScriptAPI.dox#L10883)

-------------------------

JulyForToday | 2017-01-02 01:05:59 UTC | #3

Ah yes, it's been a while since I've worked with Urho in angelscript, and forgot about those differences in the ScriptAPI. I don't have the best memory in the world.  :confused: 

So I've been able to get it to work:
[code]
class Clickable : ScriptObject
{
	private Color originalColor;

	void EnableHighlight()
	{
		StaticModel@ model = node.GetComponent("StaticModel");
		Material@ mat = model.materials[0];			
		originalColor = mat.shaderParameters["MatDiffColor"].GetColor();
		Color col = Color(originalColor);
		col.r -= 0.5;
		col.g -= 0.1;
		col.b -= 0.5;
		mat.shaderParameters["MatDiffColor"] = Variant(col);
	}

	void DisableHighlightl()
	{
		StaticModel@ model = node.GetComponent("StaticModel");
		Material@ mat = model.materials[0];			
		mat.shaderParameters["MatDiffColor"] = Variant(originalColor);
	}
}
[/code]

I should have realized before, but doing it this way applies the change to the material, so every object that has the material will reflect the change. So had to tweak it like this:

[code]
class Clickable : ScriptObject
{
	private Material@ originalMaterial;

	void EnableHighlight()
	{
		StaticModel@ model = node.GetComponent("StaticModel");
		originalMaterial = model.materials[0];
		Material@ copyMaterial = originalMaterial.Clone();
		Color col = copyMaterial.shaderParameters["MatDiffColor"].GetColor();
		col.r -= 0.2;
		col.g -= 0.5;
		col.b -= 0.2;
		copyMaterial.shaderParameters["MatDiffColor"] = Variant(col);
		model.material = copyMaterial;
	}

	void DisableHighlightl()
	{
		StaticModel@ model = node.GetComponent("StaticModel");
		model.material = originalMaterial;
	}
}
[/code]

So any thoughts on how you would set up a shader to do this same sort of thing? I original thought it would be a matter of adding a second (custom) technique that does the highlighting to a material when EnableHightlight() is called, and then remove the technique when DisableHighlight() is called. But [url=http://urho3d.github.io/documentation/1.32/_materials.html]the documentation[/url] says multiple techniques are for LOD/quality purposes. So I'm not sure my idea is the best approach/proper way to do this.

-------------------------

