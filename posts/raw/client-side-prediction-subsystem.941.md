Enhex | 2017-01-02 01:04:17 UTC | #1

I made a client side prediction subsystem for Urho3D that doesn't conflict or modify Urho's Network subsystem.
[url=http://en.wikipedia.org/wiki/Client-side_prediction]Client side prediction[/url] lets the client predict the outcome of it's own input without waiting to receive it from the server, and thus eliminating the latency from round trip of the time it takes the input to arrive to the server, and the time it takes to the new state to be sent back to the client.

Source and instructions:
[github.com/Enhex/Urho3D-CSP](https://github.com/Enhex/Urho3D-CSP)

-------------------------

Enhex | 2017-08-21 19:34:31 UTC | #2

I've updated the subsystem to work with current Urho3D API.

Currently it doesn't do full game state rewinding, which means no physics re-stepping and such.
It's still useful to avoid input latency if you don't use physical movement, and want to prevent client cheating compared to client authority approach.

-------------------------

Lumak | 2018-04-16 21:07:38 UTC | #3

I'm trying to get a better understanding of the setup for this.  I know there's additional Controls data traffic in addition to what the Network already sends.  But my question is: does the client process the control input in the FixedUpdate() fn on both the server and client side or does it only do this on the server side for this prediction to work?

edit: I thought there was a more recent thread of this topic, and I don't think this is the one.

-------------------------

Enhex | 2018-04-16 21:07:59 UTC | #4

check out the example code.
In general this is how it works:

client:
- sample input, apply it, add it to the input buffer (for re-applying when predicting), and send it to the server.
- predict when an update is received from the server.

server:
- when an input message is received from a client, apply that input instantly.

BTW I'm in the middle of re-working the code, so the current `README.md` is outdated.

-------------------------

Lumak | 2018-04-16 21:16:22 UTC | #5

Ok, thanks. Looking forward to the update.

-------------------------

Enhex | 2018-04-25 13:35:27 UTC | #6

I got networked physics working. The code is still a mess.
I'm re-applying inputs every time a state snapshot is received by updating the physics world, so it's quite expensive.

Other approaches like this will probably work better:
https://gafferongames.com/post/networked_physics_in_virtual_reality/

-------------------------

