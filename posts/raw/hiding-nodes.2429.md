Sir_Nate | 2017-01-02 01:15:21 UTC | #1

I have map composed of various chunks (a node with geometry and collision data and children often with the same), which I want to hide once they are a certain distance away from the player (eventually unloading them, but some of them just making invisible). What is the best way to do this?

I've tried just using SetDeepEnabled(true), and in general it works, though I've had some problems with loosing prior enabled state (with children meant to be disabled becoming enabled when the containing chunk becomes visible). I was wondering if there was a better way to do it, though.

-------------------------

hdunderscore | 2017-01-03 00:26:33 UTC | #2

You used ResetDeepEnabled after and there was an issue? Were you doing other SetEnabled's in the meantime?

-------------------------

