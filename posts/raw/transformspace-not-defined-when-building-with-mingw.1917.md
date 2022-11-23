godan | 2017-01-02 01:11:28 UTC | #1

For some reason, MinGW (actually gcc on MinGW) throws an error when I compile the following code:

[code]GetNode()->RotateAround(Vector3(0,0,0), Quaternion(0.005f, Vector3::UP), TransformSpace::TS_WORLD); [/code]

In particular, it claims that "TransformSpace" is not a class or namespace. Removing that argument from the function lets the code compile and run. However, I do need that parameter. Am I missing something? That syntax works fine on VS, and even emscripten...

-------------------------

weitjong | 2017-01-02 01:11:29 UTC | #2

As you said, MinGW is GCC on *Windows*. So, it basically is a derivative of GCC compiler toolchain. The "TransformSpace" is only an enumerator.  Using it as a nested namespace specifier requires C++11 standard to be enabled. Since we do not enabled that standard by default, all GCC (including MinGW) would complain about it. Clang (including Emscripten), on the other hand, does the next sensible thing, allowing it but giving a warning about it. Both GCC and Clang allows user to choose which C++ standards you want to use. I don't think I need to say anything about the MSVC.

Just use 'TS_WORLD' as parameter to the method without any specifier.

-------------------------

