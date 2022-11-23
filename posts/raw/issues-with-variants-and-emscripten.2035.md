godan | 2017-01-02 01:12:27 UTC | #1

I'm working on a project that makes heavy use of passing Variants (and VariantVectors) in and out of functions. Everything was going ok until I started targeting Emscripten (which is an essential target). I have a number of questions, but here is a very simple case that has confounded me:

Ok, so I want to construct a Variant of type Double and double check it with some console output:

[code]
Variant varA = Variant(1.0);
URHO3D_LOGINFO("varA value: " + varA.ToString() + ", type: " + varA.GetTypeName(varA.GetType()));
[/code]

Running this in Chrome, gives the expected results:
[img]https://dl.dropboxusercontent.com/u/69779082/EmDebugSingleConstruction.PNG[/img]
So far so good. Now, I create two variants, one after the other:

[code]
Variant varA = Variant(1.0);
Variant varB = Variant(2.0);

URHO3D_LOGINFO("varA value: " + varA.ToString() + ", type: " + varA.GetTypeName(varA.GetType()));
URHO3D_LOGINFO("varB value: " + varB.ToString() + ", type: " + varB.GetTypeName(varB.GetType()));
[/code]

This is gives us the following console output:

[img]https://dl.dropboxusercontent.com/u/69779082/EmDebugJustConstruction.PNG[/img]

Notice that the second variant is now not being create correctly. Or at least, the output is not correct. This seems very wrong.

Ok, one more. I create the two variants and push them to a VariantVector and display the results:

[code]
Variant varA = Variant(1.0);
Variant varB = Variant(2.0);

URHO3D_LOGINFO("varA value: " + varA.ToString() + ", type: " + varA.GetTypeName(varA.GetType()));
URHO3D_LOGINFO("varB value: " + varB.ToString() + ", type: " + varB.GetTypeName(varB.GetType()));

VariantVector varVector;
varVector.Push(varA); varVector.Push(varB);

URHO3D_LOGINFO("vec value at 0: " + varVector[0].ToString() + ", type: " + varVector[0].GetTypeName(varVector[0].GetType()));
URHO3D_LOGINFO("vec value at 1: " + varVector[1].ToString() + ", type: " + varVector[1].GetTypeName(varVector[1].GetType()));
[/code]

And here is the result:

[img]https://dl.dropboxusercontent.com/u/69779082/EmDebugWithVector.PNG[/img]

Notice that now, the *first* variant is not correct.

Please help!

-------------------------

godan | 2017-01-02 01:12:27 UTC | #2

Huh, so with Floats, all is well... Is that expected?

-------------------------

fcroce | 2017-01-02 01:12:27 UTC | #3

Hi,

have you tested with "EM_ASM_" ?

[code]

        Variant varA = Variant(1.0);
        Variant varB = Variant(2.0);

        EM_ASM_(
            {
                Module.print("varA value: " + Pointer_stringify($0) + ", type: " + Pointer_stringify($1));
                Module.print("varB value: " + Pointer_stringify($2) + ", type: " + Pointer_stringify($3));
            },

            varA.ToString().CString(),
            varA.GetTypeName(varA.GetType()).CString(),

            varB.ToString().CString(),
            varB.GetTypeName(varB.GetType()).CString()
        );

[/code]

OUTPUT:

varA value: 1, type: Double
varB value: 2, type: Double


you get the same result even if you split the output in 2 "EM_ASM_" calls.

Possibly a bug on URHO3D_LOGINFO ? no idea :slight_smile:

-------------------------

cadaver | 2017-01-02 01:12:28 UTC | #4

The double is stored in a slightly nasty manner. VariantValue is a union of 4 floats, ints, or void ptrs. When a double is stored, this structure is reinterpret-casted as a double (practically, stored in the first 2 floats). In Emscripten this might not work as expected. Potentially more compatible but slower way would be to heap-allocate storage for a double and store the pointer into the void ptr part of the union.

-------------------------

cadaver | 2017-01-02 01:12:28 UTC | #5

Can't reproduce the issue myself, using Firefox & Emscripten 1.36.0. Note that calling the static function Variant::GetTypeName(VariantType) as if it is a member function is confusing, you could just do varA.GetTypeName();

-------------------------

