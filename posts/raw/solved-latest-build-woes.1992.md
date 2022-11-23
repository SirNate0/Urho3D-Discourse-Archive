ghidra | 2017-01-02 01:12:07 UTC | #1

I am able to build urho just fine.
However, on 1 of 3 different machines, I am unable to build my project.

[code]
In file included from /urho/Urho_BUILD/include/Urho3D/Engine/../Core/../Core/../Math/../Math/../Math/Quaternion.h:28:0,
                 from /urho/Urho_BUILD/include/Urho3D/Engine/../Core/../Core/../Math/../Math/Matrix4.h:25,
                 from /urho/Urho_BUILD/include/Urho3D/Engine/../Core/../Core/../Math/Matrix3x4.h:25,
                 from /urho/Urho_BUILD/include/Urho3D/Engine/../Core/../Core/Variant.h:29,
                 from /urho/Urho_BUILD/include/Urho3D/Engine/../Core/Object.h:26,
                 from /urho/Urho_BUILD/include/Urho3D/Engine/Engine.h:25,
                 from /urho/myurho_project/src/Main.cpp:2:
/apps/GCC/gcc-4.8.1/lib/gcc/x86_64-unknown-linux-gnu/4.8.1/include/emmintrin.h:31:3: error: #error "SSE2 instruction set not enabled"
 # error "SSE2 instruction set not enabled"
[/code]

It appears that its an SSE problem.
I've built with -DURHO_SSE=0, but that doesnt seem to change anything.
As well, I have noticed another weird output anomaly when building urho3D (unrelated maybe to the above issue). Using -DURHO3D_LIB_TYPE=SHARED, the cmake output shows:

[code]
Static Enabled = ON
Shared Enabled = OFF
[/code]

Something to that effect. Not sure if that is correct?

Anyway, how should I proceed in getting my project to compile on this outlyer machine?

-------------------------

rku | 2017-01-02 01:12:07 UTC | #2

[quote]Static Enabled = ON
Shared Enabled = OFF[/quote]
It is info on SDL, it is always built as static.

Have you tried building with -DURHO3D_SSE=1?

-------------------------

ghidra | 2017-01-02 01:12:07 UTC | #3

[quote]Have you tried building with -DURHO3D_SSE=1?[/quote]
I didn't consider that.
Just tried it, same error. 
I assume that the proc, or whataever configuration of this particular machine does not support it [SSE]. 
So how can I compile my project assuming SSE is disabled. Is there another set of instructions I need to consider?
[quote]It is info on SDL, it is always built as static.[/quote]
I did not know that about the SDL output. That makes more sense.

-------------------------

ghidra | 2017-01-02 01:12:07 UTC | #4

okay. Total user error.
A few things changed since I last updated urho to head.
notably.
[code]-DURHO3D_DEPLOYMENT_TARGET=core-avx-i[/code]
is now 
[code]-DURHO3D_DEPLOYMENT_TARGET=generic[/code]

and I needed to run cmake in my project as:

[code]cmake . -DURHO3D_DEPLOYMENT_TARGET=generic -DURHO3D_SSE=1[/code]

Just to force it incase, cause I'm paranoid.

-------------------------

