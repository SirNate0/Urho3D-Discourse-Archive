namic | 2017-01-02 01:08:55 UTC | #1

Is there an example for client-side prediction for Ninja Snow War?

-------------------------

Enhex | 2017-01-02 01:09:01 UTC | #2

No AFAIK.

I tried to implement CSP back when I started using Urho, but there were problems with overriding states.
After a discussion about it SetInterceptNetworkUpdate() was added:
[urho3d.github.io/documentation/H ... 3e45afa49b](http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_serializable.html#a28cff53160b712d452724f3e45afa49b)

I never got around to trying SetInterceptNetworkUpdate() since I'm preoccupied with other work, but if u want to give it a shot I made my CSP attempt available:
[github.com/Enhex/Urho3D-CSP](https://github.com/Enhex/Urho3D-CSP)

Note that it uses outdated version of Urho so it needs patching up.


CSP is something that is highly missing in Urho, it's a core requirement for most real-time multiplayer games.

-------------------------

