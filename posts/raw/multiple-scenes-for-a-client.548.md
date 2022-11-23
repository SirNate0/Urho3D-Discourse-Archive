OvermindDL1 | 2017-01-02 01:01:18 UTC | #1

I need to have a client receive more than one scene as they need to RTT to a texture from one to display it in another (portal type thing).  I seem to be having issues doing this by trying multiple cameras, is there an example anywhere?

-------------------------

friesencr | 2017-01-02 01:01:18 UTC | #2

there is an example included 10_RenderToTexture where another camera is projected onto a surface.

-------------------------

cadaver | 2017-01-02 01:01:18 UTC | #3

Having the client be in multiple scenes at the same time is not planned to be supported in networking. Supporting it would increase the complexity of the networking code and add overhead to the protocol as the scene that the messages are directed to should be identified. Of course if you want to hack this yourself, feel free to do so.

You could make a few hacks like having the RTT scene be a local scene, or make it render some part of the world that is normally not accessible.

-------------------------

OvermindDL1 | 2017-01-02 01:01:18 UTC | #4

[quote="friesencr"]there is an example included 10_RenderToTexture where another camera is projected onto a surface.[/quote]
Yep, that is easy to do, but not across a network it seems?

EDIT:  Ah, another response:
[quote="cadaver"]Having the client be in multiple scenes at the same time is not planned to be supported in networking. Supporting it would increase the complexity of the networking code and add overhead to the protocol as the scene that the messages are directed to should be identified. Of course if you want to hack this yourself, feel free to do so.

You could make a few hacks like having the RTT scene be a local scene, or make it render some part of the world that is normally not accessible.[/quote]
Thought of that, but it is a lot of data to build up, there will be players and so forth on the 'other side' that I will need to render as well, just a lot of state to handle, I am still trying to figure out how to wrap the world efficiently as well (need one side to wrap around to the other, 65kx65k levels that wrap specifically).  Just wanting 'nearby' scene data to the portal's camera, was planning to either shift the camera around to be equivalent distance to the portal as it is on the players side so it matches, and render a clipped area, or to render the far area clipped first, then clear the Z-buffer and render the near scene.  I am needing a 'things are larger on the inside then they are on the outside' type of thing, I did it with Ogre years ago, just trying to figure it out here the best way.

-------------------------

