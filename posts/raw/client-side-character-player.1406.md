Magnetoid | 2017-01-02 01:07:32 UTC | #1

I'm having some issues implementing the character controller for my FPS-like game. Specifically I have two questions:

1) How can I hide the player's model on the corresponding client? I want other players to see the model like normal (with animation and whatnot). The problem is that in first person view the player can see inside their body. Ideally, I'd just hide the head and make sure the neck hole cannot be seen.

2) How should the aiming animations work? The character needs to bend his back point his weapon up or down. This implies that the player's viewpoint moves slightly when they look up and down. Is that a bad idea? Another game that I looked at just fakes the animation at extreme angles and only really points +/-45 degrees. Bullets and things come out of the characters face instead of the weapon itself so accuracy is unaffected. I can't do that because my weapons are physical objects that have no connection to the player other than being held.

-------------------------

rasteron | 2017-01-02 01:07:32 UTC | #2

Hey Magnetoid, here's one quick solution for you to try: tweak your game camera node position by moving it a little bit forward from the head while maintaining the aimpoint position, so that your model's head is obscured by the camera.

You can check it out in NinjaSnowWar with something like this under UpdateCamera():

[code]
    Vector3 fpsminDist = aimPoint + dir * Vector3(0, 0, 6);
    Vector3 fpsDir = (maxDist - fpsminDist).Normalized();

    gameCameraNode.position = fpsminDist + fpsDir * rayDistance;
[/code]

Sample Video:

[video]https://www.youtube.com/watch?v=igfq6w_TORA[/video]


I think you could also use this for iron sight zoom/scope, but I have not tested it. It's not 99.9% accurate, but it gets the job done. :wink:

-------------------------

jmiller | 2017-01-02 01:07:32 UTC | #3

Hi,

*cadaver has a solution  :slight_smile:

-------------------------

cadaver | 2017-01-02 01:07:32 UTC | #4

Note that in the Urho default networking replication is one way only (authoritative server to client)

Clients are free to make their local changes which aren't pushed to the server. So you can use this to your advantage and make the client hide the locally controlled player mesh, without ill effects.

-------------------------

