Kanfor | 2017-01-02 01:10:11 UTC | #1

Hi.

If I send the same material to different models, when I change a shader of the material this affect to all models.
I just want change the material of a specifiq model.

I tested clone, addManualResource, but not work.

Is possible to make different materials with the same resource?

Thank you.

-------------------------

cadaver | 2017-01-02 01:10:11 UTC | #2

If you want per-object material changes, Clone() the material and make the changes to the clone. Note that in this case optimizations such as instancing can't be applied, instead each model using a unique material will be its own draw call.

There was a recent bug related to Clone() and shader parameter changes not working as expected, so I recommend to pull the latest master.

Shader is specified in technique / pass, so in this case you would also need to make a copy of the technique and make sure the original is not changed. Currently Technique doesn't have a Clone() function so I'd recommend pre-authoring the needed techniques with different shaders as actual files.

-------------------------

gawag | 2017-01-02 01:10:13 UTC | #3

This could be helpful: [urho3d.wikia.com/wiki/Customize_ ... _per_model](http://urho3d.wikia.com/wiki/Customize_materials_%28via_code%29_%26_different_materials_per_model)

-------------------------

cadaver | 2017-01-02 01:10:13 UTC | #4

Now also Technique::Clone() is implemented in the master branch, using that you can change the shader. However be aware of all the passes you need to change (e.g. forward lighting base pass, and per-pixel light pass, and optimized first light base pass)

-------------------------

Modanung | 2017-01-02 01:10:16 UTC | #5

I've been using [i]GetTempResource<Material>()[/i] for this. Is that dangerous or inefficient? Seems more direct in some cases.
I guess you may have a pointer lying around somewhere and then [i]Clone()[/i] would be more convenient.

-------------------------

cadaver | 2017-01-02 01:10:16 UTC | #6

GetTempResource() is not dangerous, but causes a reload from disk each time it's called, while Clone() would work in memory.

-------------------------

Modanung | 2017-01-02 01:10:16 UTC | #7

[quote="cadaver"]GetTempResource() is not dangerous, but causes a reload from disk each time it's called, while Clone() would work in memory.[/quote]
Check, thanks for clearing that up.

-------------------------

