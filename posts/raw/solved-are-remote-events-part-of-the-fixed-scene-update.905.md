Enhex | 2017-01-02 01:04:00 UTC | #1

When I send a remote event is it sent with the scene replication update to the client, so they're in sync?

-------------------------

cadaver | 2017-01-02 01:04:00 UTC | #2

EDIT: was posting incorrect info. Remote events and scene replication are both processed at the network tickrate that's set with Network::SetUpdateFps(). Scene replication update is sent first, followed by remote events queued up to that point. Though because part of that is ordered data, and part of it is unordered (things like position & velocity updates) some re-ordering may happen.

-------------------------

Enhex | 2017-01-02 01:04:01 UTC | #3

Are raw network messages also part of the tickrate update?

-------------------------

cadaver | 2017-01-02 01:04:02 UTC | #4

No. Raw messages will not be queued internally to Urho, but go directly to kNet. kNet will use its own queuing system, but generally you can assume they're sent immediately with the next UDP packet, if possible.

-------------------------

