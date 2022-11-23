berrymooor | 2018-07-11 15:00:14 UTC | #1

Hi, is there a right way to animate a material texture of BillboardSet with AngelScript's SetKeyFrame contruction?
Somewhere I saw something like that:

    ValueAnimation@ TextureAnimation = ValueAnimation();
    TextureAnimation.SetKeyFrame(0.0f, Variant(cache.GetResource("Texture2D", "sprite1.png")));
    TextureAnimation.SetKeyFrame(1.0f, Variant(cache.GetResource("Texture2D", "sprite2.png")));
    TextureAnimation.SetKeyFrame(2.0f, Variant(cache.GetResource("Texture2D", "sprite3.png")));
    TextureAnimation.SetKeyFrame(3.0f, Variant(cache.GetResource("Texture2D", "sprite4.png")));
    TextureAnimation.SetKeyFrame(4.0f, Variant(cache.GetResource("Texture2D", "sprite2.png")));

but it's not working...

-------------------------

1vanK | 2018-07-11 19:18:27 UTC | #2

try
```
TextureAnimation.SetKeyFrame(0.0f, Variant(ResourceRef("Texture2D", "...")));
```

-------------------------

