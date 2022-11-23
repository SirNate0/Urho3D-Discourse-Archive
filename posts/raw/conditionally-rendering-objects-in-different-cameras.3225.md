darkirk | 2017-06-08 01:58:43 UTC | #1

I'm working on an FPS built on top of the CharacterDemo sample. One of the things that i'm trying to get rid of is the 3rd person body when i'm in the FPS camera. And, the inverse as well: getting rid of the FPS model when i'm in a third-person camera. A third-person camera can be networked or the player itself. 

How do you guys conditionally display certain objects in cameras?

-------------------------

Eugene | 2017-06-08 06:55:19 UTC | #2

I'd make simple script to enable/disable certian drawables and avoid bitmask tricks.

-------------------------

darkirk | 2017-06-08 14:20:42 UTC | #3

You mean: `if thirdPerson {  fpArms.SetVisible(false)  }`? But what about multiplayer?

-------------------------

slapin | 2017-06-08 14:27:18 UTC | #4

Well, if you run multiplayer clients on each player's PC, there's no problem - you just render 3rd person model for
all non-player models, right? and only have different logic on player model. Don't worry, nobody will see what you're doing over network, as you just don't let them by not providing such info.

-------------------------

