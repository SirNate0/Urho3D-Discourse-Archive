WangKai | 2020-11-11 15:20:19 UTC | #1

**Parameter File** (XML) of a 2D texture should be stored as the dependency of the texture.

Currently, if we change the parameter file, the texture will not be reloaded applying the changes of its paramaters. E.g. when we change the filter mode in the `test_texture.xml`, the `test_texture.png` won't be reloaded with the new filter mode.

Currently, 3D/Cube/2DArray textures have this feature, but 2D texture does not.

I have tested adding the following code to `Texture2D`, it seems working correctly. I remember Parameter file ability was added by @Eugene, so I think it's better to ask you first.

```c++
if (loadParameters_)
{
    auto* cache = GetSubsystem<ResourceCache>();
    String xmlName = ReplaceExtension(GetName(), ".xml");
    cache->StoreResourceDependency(this, xmlName);
}
```

Best regards.

-------------------------

WangKai | 2020-11-12 03:10:56 UTC | #2

I also find an issue with `void Texture::SetParameters(const XMLElement& element)` -

The logic in this function is that if some key/value is configured in the XML, this property of the texture will be set to the new value, if the property is not configured, it will not be toughed. i.e. default value is used.

e.g.-
```c++
if (name == "border") // if this property is configured
    SetBorderColor(paramElem.GetColor("color")); // new value is set
```

A simple case to show this issue is that we delete a property from the XML file, the texture's property value (sampler state) will remain the same and the old value is applied later rather than the default one.

-------------------------

SirNate0 | 2020-11-12 15:40:57 UTC | #3

I feel that the present behavior is correct. If you set the parameters and don't include a particular parameter, it should leave the texture with whatever parameter it had, which you had already set before in code or with a different XMLElement. 

Though if you think it should default to resetting to defaults I don't think that's unreasonable, it's possible it's the more intuitive behavior. I like the approach I proposed as it seems more flexible, but I personally won't be using it, so if you think it should be the other way I wouldn't object.

-------------------------

WangKai | 2020-11-12 15:47:27 UTC | #4

Hi SirNate0,

The issue with current `SetParameters` happens when reloading of the XML files. If the new version of the XML removed certain property, the property will NOT be reset to default, instead, the value in the XML file of last revision will be kept.

Edit: just think about use this in an editor, when we change the property of the texture, it won't always appear correctly, which is problematic.

-------------------------

WangKai | 2020-11-14 07:51:34 UTC | #5

I guess I misunderstood the original code. In Texture2DArray/TextureCude/Texture3D, the resources configured in an XML parameter file are added as dependencies, not the XML parameter file itself. I think we should not use the parameter files for reloading. We still need more work to if we want to edit textures in tools.

-------------------------

Eugene | 2020-11-14 07:56:49 UTC | #6

In all other textures the XML file itself is a “texture resource”. Whereas actual textures are dependencies.

In Texture2D situation is opposite. However, why do you think we shouldn’t use parameters for reloading?

-------------------------

WangKai | 2020-11-14 08:08:09 UTC | #7

Hi Eugene,

As I mentioned in previous lines, we need extra method to handle the reloading of the parameter file to apply all the properties of texture changes. 

In tools, if we are editing a Texture2D, we know when it is dirty, we can just apply all the properties and save them in parameter files if any property is different from its default value(though get default values are hacky).

-------------------------

WangKai | 2020-11-14 08:12:58 UTC | #8

Additionally, the fact is that none of the texture types have made the parameter file as their dependency. If we can solve all issues, we need to add the parameter file in their dependency for them all.

-------------------------

Eugene | 2020-11-14 08:19:18 UTC | #9

[quote="WangKai, post:8, topic:6520"]
Additionally, the fact is that none of the texture types have made the parameter file as their dependency.
[/quote]
None of other texture types _have_ parameter file. Of course they don’t make it “dependency”. Texture2DArray, Texture3D and TextureCube *are* XML files, they don’t depend on it. Resource doesn’t depend on itself.

-------------------------

WangKai | 2020-11-14 08:23:14 UTC | #10

Oh, yes you are right. The XML file for other texture types are resource itself. So we only need to solve problem for Texture2D.

-------------------------

Eugene | 2020-11-14 08:25:53 UTC | #11

Problem with partial parameter update may still persist in other texture types tho. It may be necessary to reset optional parameters somewhere if they aren’t set in file

-------------------------

WangKai | 2020-11-14 08:34:24 UTC | #12

I don't have a clear answer yet how to achieve this in a clean way.
1. notify resource if it is just loading or reloading?
2. intercept reloading from editor and call extra interface?
3. Do we need a `Reset` function for resources?

-------------------------

Eugene | 2020-11-14 08:37:10 UTC | #13

I didn’t check how it works in practice, but the place that loads parameters is responsible for resetting parameters that aren’t set. I mean, I expect it to be responsible.

-------------------------

WangKai | 2020-11-14 09:10:21 UTC | #14

What if we set a parameter which is supported by the parameter file but not configured to its default value? I don't see any overload of this. Typically, the GPU resources of the texture will always be recreated afterwards, no matter if a certain parameter is dirty or not.

something like:
if "border" is find in parameter_file:
    SetBorderColor(border_color_read)
else:
    SetBorderColor(default_border_color)

The issue I see with it is that we did not define default values explicitly, maybe we should.

-------------------------

