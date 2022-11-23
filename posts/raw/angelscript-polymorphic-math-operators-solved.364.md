ghidra | 2017-01-02 00:59:53 UTC | #1

Can I do math between types.
Vector multiplied by quaternion or matrix and return the resulting vector?

for example:

[code]
Vector3 _out = Vector3(0.0f,0.0f,-1.0f);
Vector3 _euler = Vector3(45.0f,45.0f,0.0f);
float _distance = 10.f;
Quaternion _rotation;
Vector3 _pos;

_rotation.FromEulerAngles(_euler.x,_euler.y,_euler.z);

_pos = (_out*_rotation)*_distance;
[/code]

It seems that I can rotate Nodes, but not nessisarily vectors.
And I'm not seeing anything under the Quaternion and Vector3 class information

or maybe something like

[code]
_pos = _out.rotate(_rotation);
_pos.scale(_distance);// or 
_pos.multiply(_distance);
[/code]


EDIT:
aaannnnnddd I found some stuff in 19_VehicleDemo.as
lines 194-221  HandlePostUpdate()

When i was trying it, before seeing that I was getting some errors:
"No matching operator that takes the types 'Vector3' and 'Quaternion' found"

-------------------------

cadaver | 2017-01-02 00:59:54 UTC | #2

The most needed cases of doing math between classes should work also in script. In some cases the C++ compiler may be smarter reordering the parameters as necessary than the AngelScript compiler, so in script you'd get an error of "no matching operator found" even if the same code works in C++. However, to apply rotation to a vector, the order of parameters is always:

vectorOut = quaternion * vectorIn
vectorOut = matrix * vectorIn

To check in more detail, the MathAPI.cpp file in the Source/Engine/Script directory tells exactly what operators are being registered for the math classes.

-------------------------

