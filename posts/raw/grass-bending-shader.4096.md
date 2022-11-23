smellymumbler | 2018-03-16 17:07:20 UTC | #1

Does anyone know how this thing works? 

https://twitter.com/Patrickd3/status/974284520328433666

Any article that could help me understand it?

-------------------------

Modanung | 2018-03-16 17:46:44 UTC | #2

[<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/812c006ebb824b0bdb8995d4f953fa79c882f9ae.jpg' alt=''>](https://twitter.com/Juicefoozle/status/974026650794020869)

Good luck! ;)

-------------------------

Sinoid | 2018-03-16 18:34:12 UTC | #3

He uses the direction from the `player` to the vertex to offset XZ and determines everything from the absolute distance to the surface of a sphere. The rest of the shader is controls, partially for tweaks and partially for fudging the curved look.

All of the gradients are unnecessary if designing by convention where the implied model-space gradient is a-ok (vertices are all in a unorm/snorm space on certain axes).

Everything else is just falloff control and other controls.

    float3 playerToVertex = vertexPosition - playerPosition;
    float3 directionFromPlayer = normalize(playerToVertex);
    float distanceFromSphere = abs(length(playerToVertex) - sphereRadius);
    
    float3 baseXZOffset = float3(directionFromPlayer.x, 0, directionFromPlayer.z) * distanceFromSphere;

    float gravityFactor = ... gravity determination here ...
    float bendinessFactor = ... bendiness/XZ determination here ...

    float3 vertexOffset = (baseXZOffset * bendinessFactor) - float3(0, distanceFromSphere * gravityFactor, 0);
    outputVertexPosition += vertexOffset;

-------------------------

