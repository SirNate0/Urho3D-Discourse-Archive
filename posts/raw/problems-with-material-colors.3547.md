nergal | 2017-09-09 11:47:19 UTC | #1

I want to have blocks of basic colors specified with RGB(A). But I can't get it to work. The colors seems to be distorted.
I use the material technique:

> Techniques/NoTextureVCol.xml

And I set the material for each block as follows:
> SharedPtr<Material> m = model->GetMaterial()->Clone();
> // color contains the specific block color.
> m->SetShaderParameter("MatDiffColor",Vector4(color.x_/255.0f, color.y_/255.0f, color.z_/255.0f, 1.0f));
> model->SetMaterial(m);

The result becomes like this (the physic-blocks):
http://www.giphy.com/gifs/l1J9ByXXGAVQc8eLC
I want the blocks to have the same colors as the original blocks in the world. But as seen the blocks are multicolored and not one color.

What am I missing here?

-------------------------

1vanK | 2017-09-09 16:20:33 UTC | #2

Use you standat Box.mdl or own model? May be in model no vertex colors? Try "NoTexture" technique instead

-------------------------

nergal | 2017-09-09 16:20:19 UTC | #3

I'm using the standard asset "Models/Box.mdl". It worked with using the NoTexture tech. Many thanks!

-------------------------

