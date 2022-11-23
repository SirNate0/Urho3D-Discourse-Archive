TheComet | 2019-08-03 18:47:13 UTC | #1

I'm just wondering, it seems like Urho3D isn't very secure, network wise. If I were to make a publicly available server clients can connect to, MIDM attacks and worse seems possible. It's UDP, you could send a client a packet to create a script component to gain remote code execution, for example.

What are some techniques to secure a connection to a public game server?

-------------------------

dertom | 2019-08-03 20:16:00 UTC | #2

There is a similar [post](https://discourse.urho3d.io/t/slikenet-libcat-security/5300) with some hints. Maybe that helps you bit

-------------------------

dertom | 2019-08-04 10:26:23 UTC | #4

I find the danger more real than not. Just go to some open WIFI and there you are. The man in the middle is at least the guy how offers the free wifi and if that is not setup well enough it might(?) be possible to sniff the traffic (I guess, not an expert though)....
Ok, about executing scripts on the client via udp?!? That would only be possible if you have some kind of message-type that executes its payload,no? 

Still, I think as an online developer you should have to secure personal data and credentials at all costs. 
@TheComet Have a look at  this PR. Maybe this gets you at a better starting point: 
* SLikeNet libcat security: https://github.com/urho3d/Urho3D/pull/2464

Very optional:
Also have a look at the [civetweb-update-branch](https://github.com/urho3d/Urho3D/tree/civetweb-update) in which @Miegamicis is adding https support. Maybe you could manage the critical data via https and a dedicated 'lobby'.webserver, which would handle logins/account data and such and create then some kind of session-token for login in to the server-connection once you want to start a game.... The uncritical game-data transmissions would then still be unencrypted...make this sense?

-------------------------

TheComet | 2019-08-05 06:34:17 UTC | #5

> With respect to creating a remote script instance? What script? The attacker would need to find a way to upload an arbitrary script to the server, then instantiate it remotely.

He wouldn't need to upload it to the server if he is the man in the middle. You could send the client a required resource via [Scene::AddRequiredPackage()](https://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_scene.html#adb229515c3873cb6dbafe3ac58ab2053) and then instanciate it.

It would be entirely possible to write a malicious urho application that sits in the middle of a server/client connection and "filters" the scene.

The core issue is: The client has no way of verifying whether the network packets it's receiving are actually from the server.

If the server and client were to cryptographically sign every network packet using previously exchanged public keys, I think it would mitigate all of my concerns.

I see in the PR @dertom linked, SLikeNet libcat does what I need.

-------------------------

