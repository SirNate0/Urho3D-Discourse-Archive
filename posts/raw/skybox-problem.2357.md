itisscan | 2017-01-02 01:14:57 UTC | #1

In the scene i have node with SkyBox. When camera has big X,Y or Z values and is translated, then SkyBox has jitters. 
As X,Y or Z values are increased, the jitters become faster. 

I have captured it in Urho3d editor - [url]https://youtu.be/1AENHxsgg-4[/url]

At value > 10000 you can notice jitters.

Maybe someone already faced with this problem and can explain why so occurs and how can fix it?

Thanks.

-------------------------

cadaver | 2017-01-02 01:14:57 UTC | #2

The skybox positions itself to the camera position, and the camera position gets "subtracted" by the view matrix, bringing it back to origin, but with large numbers the math is not accurate.

This isn't easily solvable without engine changes since the engine doesn't expose a pure projection matrix, only combined viewProj.

-------------------------

Eugene | 2017-01-02 01:14:58 UTC | #3

[quote="itisscan"]
At value > 10000 you can notice jitters.
[/quote]
Since float have only 6 digits precision, at 10000 units you have only 0.01 unit precision.
If unit==meter, you will have ~5mm jittering of all your objects, not only skybox.

-------------------------

Eugene | 2017-01-02 01:14:59 UTC | #4

Specifically your problem can be easily fixed in Skybox shader:

from
[code]float3 worldPos = GetWorldPos(modelMatrix);
oPos = GetClipPos(worldPos);[/code]
to
[code]oPos = mul(float4(iPos.xyz, 0.0), cViewProj);[/code]

-------------------------

