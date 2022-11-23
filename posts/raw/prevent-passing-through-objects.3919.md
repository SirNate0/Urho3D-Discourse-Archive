davidpox | 2018-01-07 04:50:09 UTC | #1

Hi all, 

Quick question. I have the following : A player. The player is a model with a rigidbody and a collision shape. 
: 4 Walls, a floor & ceiling, each with rigidbodies and collisionshapes. 

Question: How do I stop the player from being able to pass through the walls/floor/ceiling? I can do the simple method to check if they're out of bounds and then change their position back but that isn't as fluid and doesn't work perfectly sometimes. 

If I remember correctly, In Unity it was possible to alter the Rigidbodies somehow, and it would cause the body to stop as soon as it hits another one. I was wondering if it was possible in Urho too. 
I played around with rigidbodies a slight bit and a way for me to stop going through walls but as soon as I touch another rigidbody, it applies a force to my player that causes them to float away. 

Many thanks for the help!

-------------------------

TrevorCash | 2018-01-07 05:40:58 UTC | #2

Sample 18 has a custom component called "Character" that handles the interactions for a player:
https://github.com/urho3d/Urho3D/tree/master/Source/Samples/18_CharacterDemo

-------------------------

