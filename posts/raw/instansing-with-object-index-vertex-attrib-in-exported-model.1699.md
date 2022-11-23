codingmonkey | 2017-01-02 01:09:33 UTC | #1

Hi folks!
I want to share with community with a new exporter's ability.
It use ObjectIndex vertex attrib to separate objects from each other in one solid VB. 
there is simple example of using

[video]https://www.youtube.com/watch?v=qd-UZc-7paw[/video]

exporter : [github.com/MonkeyFirst/Urho3D-B ... exPaint4Ch](https://github.com/MonkeyFirst/Urho3D-Blender/tree/VertexPaint4Ch)
example : [github.com/MonkeyFirst/urho3d-s ... -instances](https://github.com/MonkeyFirst/urho3d-staticmodel-instances)

-------------------------

sabotage3d | 2017-01-02 01:09:34 UTC | #2

Pretty cool. Similar to what I am doing at the moment for mobile instancing.

-------------------------

codingmonkey | 2017-01-02 01:09:34 UTC | #3

Yes, probably it may be very cheap batching for mobile devices.

>Similar to what I am doing at the moment for mobile instancing.
did you store matrixes for instances in uniforms ? you use mat4 or vec4*3 ?

-------------------------

sabotage3d | 2017-01-02 01:09:34 UTC | #4

I am using position and quaternion. Sending it as an array to the shader. I will soon release my code just want to make it more usable.

-------------------------

