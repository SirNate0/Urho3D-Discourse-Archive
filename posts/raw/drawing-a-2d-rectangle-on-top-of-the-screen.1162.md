setzer22 | 2017-01-02 01:05:48 UTC | #1

What's the best way do draw a 2D rectangle on the screen, as if it was an UI element but without having to use UIElements. I'm talking about something like the selection rectangle typically found on RTS games.

I thought about using Urho2D with a sepparate camera drawing a second "pass" which would be rendered on top of the scene, but I'm not familiar enough with Urho's rendering pipeline so I'm not sure how (or even if I can) achieve that behaviour.

Any other ideas?

-------------------------

Mike | 2017-01-02 01:05:48 UTC | #2

This [url=http://discourse.urho3d.io/t/how-to-layer-scenes/740/1]thread[/url] should help.

-------------------------

setzer22 | 2017-01-02 01:05:49 UTC | #3

Thanks Mike, that's actually what I was trying to do, without knowing exactly how (even though I came pretty close  :stuck_out_tongue:).

I'm having problems in accomplishing the same thing in the editor. Somehow it's not working properly there, probably because of the way the editor sets up its viewport, but I'm not really sure. Loading the scene normally works just fine.

-------------------------

