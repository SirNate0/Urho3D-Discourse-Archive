throwawayerino | 2020-07-13 13:53:04 UTC | #1

# AUTOMATIC SNAKE DISPENSER
The only true way to fix a mice infestation is by shooting snakes at it! This is a neat little `PackageFile` I made to showcase this functionality and to experiment with player made objects.

https://imgur.com/OCCjjEz

https://imgur.com/zFSkKq9.png
* Radius: Specifies the size.x of the cylinder used for detection
* CooldownDuration: Time in seconds to wait until next launch. Please don't try setting it to zero
* ImpulseForce: The multiplier used when applying impulse to the snakes
* SnakeRagdollHolder: The Turret shoots ragdoll snakes. This can be a bit taxing on the computer, so you could group them into a node and clean them up periodically.
* TargetTag: Tag to use when searching for target nodes
* SnakeTag: Tag to add to each snake when fired

## The Turret in action:
https://imgur.com/g3IwB5x.gif

It can even handle movement in space (though not precisely):
https://imgur.com/k25BoLU

## Script Usage:
```
// Exact path may vary
cache.AddPackageFile("Data/Packages/SnakeTurret.pak");
Node@ turret = scene.CreateChild();
turret.LoadXML(cast<XMLFile>(cache.GetResource("XMLFile", "SnakeTurret/Objects/SnakeTurret.xml")).root);
turret.worldPosition = Vector3::ZERO;
```

## Things to consider:
* I don't like how it snaps in place. Might use an attribute animation to fix it
* Linear/Angular damping on the snakes might be too low.
* It makes no sound at all. Something to consider.

[Download SnakeTurret.pak (0.6MB, CRC32 4654A4A9)](https://files.catbox.moe/nc43jb.pak)
[Source code in .zip (0.5MB, CRC32 11AF0DA7)](https://files.catbox.moe/t82zrj.zip)
[Mega.nz backup](https://mega.nz/folder/prgGESJY#TnL5pC2HTORM16e_j34ZJg)

Everything inside is made by me.

-------------------------

Modanung | 2020-07-18 22:46:06 UTC | #2

Hehe, I think I might add the snake launching variant to my multi-mower concept (lawmower robot + home defence) if you don't mind. :laughing:
Everytime I go past one of those things I imagine some satirical commercial where it has machine guns popping out. They have names, like Ikea furniture: _Rocky_ is equipped with a catapult, _Tommy_ has typewriters and _Fido_ a beartrap. :slightly_smiling_face:

-------------------------

