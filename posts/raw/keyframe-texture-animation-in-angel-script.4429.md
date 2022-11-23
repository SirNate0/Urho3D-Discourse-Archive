berrymooor | 2018-08-01 11:38:01 UTC | #1

I want to animate the "Texture" property of material from BillboardSets, believing that there is such a way

        Material@ material = BillboardSet.material;  
        ValueAnimation@ TextureAnimation = ValueAnimation();

        TextureAnimation.SetKeyFrame(0.0f, Variant(ResourceRef("Texture2D", "icons1.png")));
        TextureAnimation.SetKeyFrame(1.0f, Variant(ResourceRef("Texture2D", "icons2.png")));
        TextureAnimation.SetKeyFrame(2.0f, Variant(ResourceRef("Texture2D", "icons3.png")));
        TextureAnimation.SetKeyFrame(3.0f, Variant(ResourceRef("Texture2D", "icons4.png")));
        TextureAnimation.SetKeyFrame(4.0f, Variant(ResourceRef("Texture2D", "icons1.png")));

        material.SetShaderParameterAnimation("Texture", TextureAnimation,WM_LOOP);

I think I do not correctly specify the parameter "Texture" in last line of code, maybe I need to specify something else...please help!

-------------------------

