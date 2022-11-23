Spongie | 2017-01-02 01:02:45 UTC | #1

Hi!

I'm not super familiar with linking C++, but I've stumbled on a problem. When I try link the shared object (NOTE: using static build works fine!) using this:
 > g++ -I/usr/local/include/Urho3D -I/usr/local/include/Urho3D/ThirdParty -L/usr/local/lib64/Urho3D -lUrho3D -o urho3d_geometry_and_shader.bin urho3d_geometry_and_shader.cpp -lUrho3D -ldl -lpthread -lGL
/tmp/ccbaNWfo.o: In function `MyApp::CreateMaterial(Urho3D::Color const&)':
urho3d_geometry_and_shader.cpp:(.text._ZN5MyApp14CreateMaterialERKN6Urho3D5ColorE[_ZN5MyApp14CreateMaterialERKN6Urho3D5ColorE]+0x5a): undefined reference to `Urho3D::PASS_BASE'
collect2: error: ld returned 1 exit status

The offending line does this:
[code]pass = technique->CreatePass(PASS_BASE);[/code]

if I change it to
[code]pass = technique->CreatePass(StringHash("base"));[/code]
it will build just fine. When ever I use the PASS_* symbols it will fail to link due to undefined reference.

Looking at the shared object I can see the following BSS symbols:
0000000001339100 b Urho3D::PASS_ALPHA
00000000013390fc b Urho3D::PASS_LIGHT
0000000001339108 b Urho3D::PASS_SHADOW
00000000013390f8 b Urho3D::PASS_LITBASE
0000000001339110 b Urho3D::PASS_PREPASS
000000000133911c b Urho3D::PASS_REFRACT
000000000133910c b Urho3D::PASS_DEFERRED
0000000001339104 b Urho3D::PASS_LITALPHA
0000000001339114 b Urho3D::PASS_MATERIAL
0000000001339120 b Urho3D::PASS_POSTALPHA
0000000001339118 b Urho3D::PASS_POSTOPAQUE
00000000013390f4 b Urho3D::PASS_BASE

In GraphicsDefs.h we can see
[code]extern StringHash PASS_BASE;[/code]
and in GraphicsDefs.cpp
[code]StringHash PASS_BASE("base");[/code]
Looks good to me if extern does roughly the same thing in C++ as it does for C.

I checked the build logs, including library link, it includes GraphicsDefs.cpp.o so it should be good, it's there.

What am I messing up?

[b][color=#FF0000]EDIT:[/color][/b]
Turns out this has been added (or was it always there?) in the build " -fvisibility=hidden -fvisibility-inlines-hidden" and the extern symbol declarations now require the URHO3D_API.

-------------------------

