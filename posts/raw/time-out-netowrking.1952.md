vivienneanthony | 2017-01-02 01:11:45 UTC | #1

Hello,

Question how do you increase the timeout of networking in Urho3D for debugging and testing? We want to debug the networking client-server aspect but a timeout limit of 1 minute is limiting?

Vivienne

[quote].... after 1 minute server makes client disconnect
[3:01:15 PM] ??????: or client is dicsonnected due to server is debugging
[3:01:57 PM] ??????: also there will be one issue
[3:02:05 PM] ??????: within performance
[3:02:23 PM] ??????: but i need to test it before say any conclusions
[3:03:16 PM] ??????: can you ask on the forum, how can set larger time out time in order to debug server or client ?
[/quote]

-------------------------

cadaver | 2017-01-02 01:11:45 UTC | #2

The disconnect timeout is a constant in kNet and not configurable, at least presently. See [github.com/juj/kNet/blob/master ... ection.cpp](https://github.com/juj/kNet/blob/master/src/MessageConnection.cpp)

-------------------------

