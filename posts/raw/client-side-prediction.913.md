Enhex | 2017-01-02 01:04:03 UTC | #1

I want to have client side prediction in Urho3D. Not having CSP means it's impossible to make real time multiplayer games with Urho3D over the internet (only Turn based / LAN games are possible).

I tried to implement it myself but I couldn't revert the replicated state to the CSP state.
My first attempt was to do it on fixed update, but nothing happened.
My second attempt was to send a net event and restore the CSP state when it arrives (should be in sync with the replication), but it kept jumping between the two states.
Is there a way to know when the state replication is done on the client-side, so I could revert it to the CSP state?

-------------------------

cadaver | 2017-01-02 01:04:03 UTC | #2

You could make Serializable::ReadLatestDataUpdate() and Serializable::ReadDeltaUpdate() send an event, for example. Make a pull request of it if it turns out nice and you want to share with the rest of the community.

-------------------------

