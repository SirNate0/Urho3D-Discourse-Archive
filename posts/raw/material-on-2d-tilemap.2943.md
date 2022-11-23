napard | 2017-03-22 23:37:18 UTC | #1

I'd like to "tint" several specific elements in a TileMap2D to reuse tiles. Is it possible to apply a custom material when drawing the tilemap or setting a tile? Is there any example about this? Any hint would be much appreciated.

-------------------------

napard | 2017-03-25 05:20:12 UTC | #2

Well, I think I will not get any answer on this. But finally I understand that it is possible to apply a custom material to a specific sprite in the tilemap, so, Which technique should I use to add a tinted effect on a tile? Where is the info about materials/techniques use cases? Where do I find documentation on material parameters and their effect? I haven't found any useful on the examples nor in the docs...

I really need help with this guys.
Thanks.

-------------------------

1vanK | 2017-03-25 09:11:15 UTC | #3

> Where is the info about materials/techniques use cases?

 https://urho3d.github.io/documentation/HEAD/_materials.html
 
To change material color:
1) clone material to make it unique
2) material->SetShaderParameter("MatDiffColor", Color::RED);
 https://github.com/1vanK/Urho3DOutlineSelectionExample/blob/master/Game.cpp

-------------------------

Mike | 2017-03-26 02:49:24 UTC | #4

Theoretically, you could use sprite.color (like we do in sample #32 when tinting the grabbed sprite in red). For exemple:

>  sprite.color = Color(0, 0, 1); // Blue tint
>  sprite.color = Color(0, 1, 0); // Grey tint

These will work, however other combinations (including pure red) don't and I have no clue why.

-------------------------

napard | 2017-03-25 17:17:22 UTC | #6

> Theoretically, you could use sprite.color (like we do in sample #32 when tinting the grabbed sprite in red).

That's what I need. Thanks!!

-------------------------

