franck22000 | 2017-01-02 01:07:32 UTC | #1

Hello Sinoid,

Any progress on this ? It would be nice to have geometry shader for DirectX11 :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:07:32 UTC | #2

>the Urho3D shaders use individual function arg inputs instead of the struct style inputs
Yes, this is pain sometimes.
Is it possibly in future to keep two versions of shaders in master with structs and without it, or maybe at all - rewrite all shaders for struct style input-output only ?

-------------------------

cadaver | 2017-01-02 01:07:33 UTC | #3

Two versions isn't a good idea for maintenance, rather we should just adjust the shaders to use structs. It should be relatively clean, as VS/PS source code are both in the same file. Only thing that needs verifying is that D3D9 & D3D11 should both work from the same source like before, but I don't think there should be a problem with that.

-------------------------

