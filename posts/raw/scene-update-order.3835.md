nergal | 2017-12-11 15:39:49 UTC | #1

I'm looking at the Sample 18 demo (character controller) and I'm wondering about the reason for updating char controls before physic updates and then after physics update the camera. Why not handle it in a single update (camera update in HandleUpdate)?

    // Subscribe to Update event for setting the character controls before physics simulation
    SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(CharacterDemo, HandleUpdate));

    // Subscribe to PostUpdate event for updating the camera position after physics simulation
    SubscribeToEvent(E_POSTUPDATE, URHO3D_HANDLER(CharacterDemo, HandlePostUpdate));

-------------------------

SirNate0 | 2017-12-11 18:02:46 UTC | #2

Without having the code in front of me, I would guess that it is because the physics update is responsible for setting the player's position and orientation, and the camera position and orientation is based on that. If both are done in the one update event, the camera position would be based on the last frames arrangement, instead of on the one that was just called, which probably updated the position and orientation of the player. That would potentially lead to a laggy feel in the camera, where camera position and orientation are a frame behind the player's.

-------------------------

