Enhex | 2017-01-02 01:04:07 UTC | #1

Does Urho3D network non-LOCAL components which are attached to LOCAL nodes?

-------------------------

cadaver | 2017-01-02 01:04:07 UTC | #2

No. Actually a recent change has enforced so that you can't even create non-local components to local nodes, because if you were to do that on client, there would be possibility of ID conflict with server.

-------------------------

