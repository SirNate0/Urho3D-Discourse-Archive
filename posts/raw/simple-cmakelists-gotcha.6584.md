vmost | 2020-11-30 01:08:54 UTC | #1

If you are messing around with CMakeLists for your project, you might try this:
```
project (myapp 
            DESCRIPTION "messing around with Urho3D"
            LANGUAGES CXX)
```

But then you will get the error
```
CMake Error at CMake/Modules/CheckCompilerToolchain.cmake:194 (message):
  Could not check compiler toolchain as it does not handle '-E -dM' compiler
  flags correctly
```

It's because specifying the languages explicitly means they won't be implicitly found... and you need C.

Solution:
```
project (myapp 
            DESCRIPTION "messing around with Urho3D"
            LANGUAGES C CXX)
```

-------------------------

