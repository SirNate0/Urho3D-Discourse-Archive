practicing01 | 2017-01-02 01:03:51 UTC | #1

Edit: AnimatedSprite2D works.
[img]http://img.ctrlv.in/img/15/03/03/54f5b509a2d85.png[/img]

Hello, for my latest project I'm envisioning something along these lines: 
[spoiler][img]http://img.ctrlv.in/img/15/03/02/54f4b75843aea.jpg[/img][/spoiler]

How would I go about doing the character sprite?  It's 2d but it transforms in 3D.  On the irc channel it was suggested that I use billboards.  However, I don't see any methods for setting animations within the api docs.  Any ideas on how to achieve this would be greatly appreciated.  Thanks for your time.

-------------------------

ghidra | 2017-01-02 01:03:52 UTC | #2

The image isnt showing up.
I think i found it with google, but i'm still not sure what the desired effect is.

EDIT:
now the image shows up.  My confusion still stands :slight_smile:

-------------------------

thebluefish | 2017-01-02 01:03:53 UTC | #3

Based on the image, is sounds like you want to be able to position/rotate your sprite in 3D space?

-------------------------

GoogleBot42 | 2017-01-02 01:03:53 UTC | #4

I think you might be talking about the reflection of the rocks and the person onto the water....   :neutral_face:   I would find a way to represent objects at different heights (aka layers) and use a shader to combine the textures together keeping in mind how tall and far an object on a particular layer is from the water...  maybe the 3D water demo will shed some light.  IDK I don't really have any experience with shaders other than knowing what they are used for though.

-------------------------

thebluefish | 2017-01-02 01:03:53 UTC | #5

[quote="GoogleBot42"]I think you might be talking about the reflection of the rocks and the person onto the water....   :neutral_face:[/quote]

If that is the case, it might almost be better to draw it as part of the background. Completely static backgrounds like that can be baked into a single texture, or into individual tiles. Even using the tiles approach, that kind of rock would be its own tile so as to account for any lighting or other visual differences.

The character could be a simple shader that flips the sprite upside down and uses an alpha mask to stop it from appearing over anything but the water.

-------------------------

GoogleBot42 | 2017-01-02 01:03:53 UTC | #6

[quote="thebluefish"][quote="GoogleBot42"]I think you might be talking about the reflection of the rocks and the person onto the water....   :neutral_face:[/quote]

If that is the case, it might almost be better to draw it as part of the background. Completely static backgrounds like that can be baked into a single texture, or into individual tiles. Even using the tiles approach, that kind of rock would be its own tile so as to account for any lighting or other visual differences.

The character could be a simple shader that flips the sprite upside down and uses an alpha mask to stop it from appearing over anything but the water.[/quote]

True, but the player and other things will be moving around so not everything could be baked... I think think it would be less work just to do everything at runtime because some will have to be done at runtime anyway.  If this is a 2D game I think the performance will be good enough that baking is not needed.

-------------------------

practicing01 | 2017-01-02 01:03:53 UTC | #7

Fixed the link, it must have been removed.

No I didn't mean reflections.  I meant a 2d sprite in a 3d world.  In that game the characters where just that and they were affected by 3d transformations (translation, rotation, scale).

-------------------------

GoogleBot42 | 2017-01-02 01:03:54 UTC | #8

ohhhhh! That's actually pretty easy.   :slight_smile:  Just create a model that is a flat square (with four vertices), disable backside culling (so that both sides of the sprite are visible and the texture is flipped properly when turned around), and apply your texture.   :wink:

-------------------------

weitjong | 2017-01-02 01:03:54 UTC | #9

May be a short video is better in this case. Could it be actually low poly 3D models rendered in toon shader?

-------------------------

practicing01 | 2017-01-02 01:03:54 UTC | #10

This game was for the PlayStation 1, so no shaders, vidya: 

[spoiler][video]http://youtu.be/DU5e9J1jCx8?t=16m07s[/video][/spoiler]
[spoiler][video]http://youtu.be/DU5e9J1jCx8?t=22m47s[/video][/spoiler]

-------------------------

