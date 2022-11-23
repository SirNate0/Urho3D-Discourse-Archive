Taymindis | 2017-11-19 09:16:13 UTC | #1

I need a high Level Documentation about urho3D sprite and node.

I've seen some example that need Node, some not needed.
There are a lot of sprite type
Sprite,
Sprite2D
StaticSprite2D.

Sprite2D  < getCache Image?
Node spriteNode = scene->createChild() 
spriteNode->setPosition ? can't staticSprite do that?

staticSprite2D->setSprite(sprite2D);  << what sprite set sprite?

I can't really understand every one are sprite, but role are different

-------------------------

weitjong | 2017-11-19 10:01:47 UTC | #2

Unfortunately our documentation is quite sparse. We only have class references auto-generated from Doxygen comments. In the past we didn't support 2D graphics, so all the drawable classes were known to be worked for 3D only. When the 2D graphics support is added, it introduced another set of 2D drawables classes and they have "2D" suffix added to their class name. So, we have `StaticSprite2D` and `AnimatedSprite2D` drawable component for 2D. They serve a similar role as `StaticModel` and `AnimatedModel` drawable component in 3D.

The `Sprite2D` and also the `SpriteSheet2D` are resources to be loaded containing the sprite texture. They are not drawable component where you attach to a node.

Lastly the `Sprite` class has nothing to do with 2D graphics at all. It was created long before the 2D graphics support. This class is just one of the UI-element subclass. Useful for drawing HUD in the game UI.

Here are some of the docs you may find it useful:
https://urho3d.github.io/documentation/HEAD/_urho2_d.html#Urho2D_Sprites
https://urho3d.github.io/documentation/HEAD/_u_i.html#UI_Sprites

HTH.

-------------------------

