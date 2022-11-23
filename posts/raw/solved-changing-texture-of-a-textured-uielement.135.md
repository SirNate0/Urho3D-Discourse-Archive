Mike | 2017-01-02 00:58:18 UTC | #1

I'd like to know how to change texture applied onto an already textured UIElement.

For example in example #3 (Sprites), if I modify the texture like this:

[code]
        sprite.texture = decalTex
        sprite.texture = cache:GetResource("Texture2D, Textures/LogoLarge.png")
[/code]
Instead of applying the new texture, previous texture seems to be removed and the new one isn't applied.

-------------------------

cadaver | 2017-01-02 00:58:18 UTC | #2

You have a typo in your code.

[code]
sprite.texture = cache:GetResource("Texture2D", "Textures/LogoLarge.png")
[/code]
should work.

-------------------------

Mike | 2017-01-02 00:58:18 UTC | #3

Thanks and sorry for this one  :unamused:

-------------------------

