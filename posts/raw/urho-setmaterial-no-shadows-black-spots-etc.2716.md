Jimmy781 | 2017-01-17 20:32:09 UTC | #1

Hey guys , is there any way to set a material so that all sides are always have the same color / light . 

obj.SetMaterial(Material.FromImage("test_icon.jpg")); 

This one looks good from the top view but from the sides , it looks darker / black . At first i thought it was the light position

obj.SetMaterial(cache.GetMaterial("Materials/Stone.xml"));

However this is the inverse , it looks good from the sides , but the top part appears black / very dark 

This is the stone.xml 

    <material>
        <technique name="Techniques/DiffNormalPacked.xml" quality="1" />
        <technique name="Techniques/Diff.xml" quality="0" />
        <texture unit="diffuse" name="Textures/StoneDiffuse.dds" />
        <texture unit="normal" name="Textures/StoneDiffuse.dds" />
        <parameter name="MatSpecColor" value="0.3 0.3 0.3 70" />
    </material>


Is there any way to fix that ?

-------------------------

Eugene | 2017-01-17 21:26:15 UTC | #2

Use unlit techniques?

-------------------------

GoogleBot42 | 2017-01-17 22:51:35 UTC | #3

You can use unlit techniques like eugene said but I don't think you will be able to have a normal map because I think normal mapping requires lighting to make the object look 3D.

-------------------------

GoogleBot42 | 2017-01-17 22:54:06 UTC | #4

You are probably looking for using: [code]<technique name="Techniques/DiffUnlit.xml" />[/code]

-------------------------

