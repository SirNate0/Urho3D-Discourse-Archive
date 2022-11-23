codewalkerdan | 2022-09-25 04:07:40 UTC | #1

It started as a learning experience in putting enTT on top of Urho3D as a learning experience, but now it has become a full fledged project to work on. The name i have no idea yet ;P.

After the recreation of the Character Demo using ECS was done I wanted to add bullet's character controller to the systems of the game and so far I am satisfied with the results

https://www.youtube.com/watch?v=Wcgl9K4pvP4

This video has an issue in that the changes in direction are a bit abrupt   (specially up and down the stairs) so after some tests I decided to add an optional lerp when copying data from components to nodes (position and rotation) to make a smoother movement. I will make another video of that later.

Now it was time to add raycasting with entities that will allow me to identify items such as weapons that a player can pick or equip.

https://www.youtube.com/watch?v=KRXy3fMd9os

-------------------------

