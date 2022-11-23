xDarkShadowKnightx | 2017-01-02 01:00:05 UTC | #1

For whatever reason my server sets all new clients ip's to 0.0.0.0:0 after one of the clients disconnects. Here's a screen shot of this [gyazo.com/56435597d1cd69086ccde9b24aa26685](http://gyazo.com/56435597d1cd69086ccde9b24aa26685), this is a problem extending from my original issue posted here on github [url]https://github.com/urho3d/Urho3D/issues/424[/url] (sorry if this counts as double posting, but I'm thinking more people will see this here). This issue does not occur with the example script 17_SceneReplication.as (the connections always keep there ip and port)

Thank you for any help! This has been a really frustrating problem!

Edit: It seems that if I disconnect right after I connect the server logs the right ip and port as disconnecting, but if I wait a few seconds it says 0.0.0.0:0 disconnected

-------------------------

cadaver | 2017-01-02 01:00:06 UTC | #2

I will reply to here too.

This does not mean that the server loses IP/port of a connection during the time the client is connected, or assigns zero IP to new connections. The nonzero IP/ports in the "connected" log print are the right ones. However, the zero IP's you are seeing in the "disconnected" log prints are the cases when the kNet networking library has sometimes already destroyed a network socket upon disconnection, in which case the line will show a zero IP/port.

-------------------------

