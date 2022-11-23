devrich | 2017-01-02 01:02:54 UTC | #1

** I am using the "PhysicsStressTest.lua" script to test how things work **

Let's say I have multiple instances of a [i]Box.mdl[/i] model and I have set them all to use the [i]stoneSmall.xml[/i] material....

"Multiple as in anywhere from a couple hundred on up through as much as 5,000 individual models ( Boxes in this case )"

I figured out that I can use:

 [code]boxObject:GetMaterial(0):SetShaderParameter("MatDiffColor", Variant(Vector4(1,.8,0,1)))[/code]
 to change the XML parameters of a object's material.  But this applies to [u][i]ALL[/i][/u] instances of that particular material accross [i][u]ALL[/u][/i] objects in the scene.

Now let's say that I want to change their colors to be a different color on every box... How to do that?

Also.. if i end up having to use a different material XML file for every color then what would the performance hit be to having say 5,000 materials versus only 1 shared material ?

-------------------------

weitjong | 2017-01-02 01:02:55 UTC | #2

Just a thought. How about changing the color in a custom shader instead? Just use the shader parameter to "seed" the randomness.

-------------------------

hdunderscore | 2017-01-02 01:02:55 UTC | #3

You can Clone() a material: 
[urho3d.github.io/documentation/1 ... 017bc5e274](http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_material.html#af4a270694b5e998e19ff6e017bc5e274)

-------------------------

devrich | 2017-01-02 01:02:55 UTC | #4

[quote="weitjong"]Just a thought. How about changing the color in a custom shader instead? Just use the shader parameter to "seed" the randomness.[/quote]

I saw a extremely simular idea to what you are saying with the [i]31_AnimatedMaterials.lua[/i] Lua script example ( that was also where I found out about how to go about setting the shader parameter )

The problem was that when I changed that same shader parameter at runtime for each instance of the small box that I created; the entire cached material .XML was changed and thus changed all instances of that material in use.  If I had 50 small boxes then changed the color of the 51st box's material then all 50 existing small boxes would also change to that color.

Is there a setting somewhere for using a unique instance of geometry's material? ( or do i "have" to specify a "different" material .XML file for each object instance? )

@hd_ Thanks! I didn't notice the [i][u]Clone( )[/u][/i] function before; I tried using it but I don't think I know how to use it right as nothing I tried did anything.. is there an example ?

-------------------------

hdunderscore | 2017-01-02 01:02:55 UTC | #5

Here's an example snippet from something I'm working on:
[code]    Material@ mat = cache.GetResource("Material", "Materials/Mr0.xml");
    //for (int y = 0; y < 1; y++)
    int y = 0;
    {
        for (int z = 0; z < 11; z++)
        {
            for (int x = 0; x < 11; x++)
            {
                Node@ tp = Node();
                tp.scale = Vector3(0.5f, 0.5f, 0.5f);
                scene_.AddChild(tp);
                tp.position = Vector3(x, 1, z);
                StaticModel@ model = tp.CreateComponent("StaticModel");
                model.castShadows = true;
                model.model = cache.GetResource("Model", "Models/Sphere2.mdl");
                Material@ m = mat.Clone();
                model.material = m;
                float diff = z / 10.0f;
                float gloss = x / 10.0f;// 1.0f;
                float spec = 1;// z / 10.0f;// 1.0f;
                m.shaderParameters["MatDiffColor"] = Variant(Vector4(diff, diff, diff, 1.0f));
                m.shaderParameters["MatSpecColor"] = Variant(Vector4(spec, spec, spec, gloss));
            }
        }
    }[/code]

Loads a 'template' material, clones material for each StaticModel and varies some shader parameters for each.

-------------------------

devrich | 2017-01-02 01:02:55 UTC | #6

[quote="hd_"]Here's an example snippet from something I'm working on:
[code]...
...
    Material@ mat = cache.GetResource("Material", "Materials/Mr0.xml");
    Material@ m = mat.Clone();
    model.material = m;
...
...
[/code]

Loads a 'template' material, clones material for each StaticModel and varies some shader parameters for each.[/quote]

Awesome! I think we got it  :smiley: 

Those 3 lines of your code made complete sence to me but in Lua I don't know how ( or if we can, can we? ) to create a "local" variable of a specific class ( C++ you do [b][u]ClassName variableName[/u][/b] )


I tinkered around for a while with the Lua script and I ended up with:
[code]-- NOTE: This first line is required in order to "load in" the material -- otherwise you get a Nil reference error on the following lines
boxObject:SetMaterial(0,cache:GetResource("Material", "Materials/myMat.xml"))

    -- NOTE: If you remove thes following indented 2 lines then "ALL" of the objects with "Materials/myMat.xml" set to them will change their SetShaderParameter settings
    local mat = boxObject:GetMaterial(0):Clone(cache:GetResource("Material", "Materials/myMat.xml"))
    boxObject:SetMaterial(0,mat)

boxObject:GetMaterial(0):SetShaderParameter("MatDiffColor", Variant(Vector4((math.random(100)*.01),(math.random(100)*.01),(math.random(100)*.01),1)))[/code]

Many Thanks for your help there!!!  :smiley:

-------------------------

