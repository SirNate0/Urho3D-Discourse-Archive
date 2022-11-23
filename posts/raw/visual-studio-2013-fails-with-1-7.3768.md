Pencheff | 2017-11-22 13:36:23 UTC | #1

Visual Studio 2013 build fails with multiple errors like this in Urho3D/Core/Variant.h:
[code]Error	1	error C2621: 'Urho3D::VariantValue::vector2_' : illegal union member; type 'Urho3D::Vector2' has a copy constructor
[/code]
Errors repeat for every member of the union VariantValue.

It seems after refactoring Variant in PR #2097 brakes the build with VS2013. Any ideas for a workaround ?

-------------------------

Eugene | 2017-11-22 13:51:52 UTC | #2

Use C++11-compatible compiler. I'm sorry, but you cannot use Visual Studio 2013 anymore.
To be precise, 1.7 must work perfectly. Any commits above 1.7 may not.

-------------------------

Pencheff | 2017-11-22 23:13:50 UTC | #3

Yeah sorry for the misleading title, I meant to update to 1.7 but pulled latest from master. It works fine with VS2017 and my gcc/clang build is fine too, just making sure it has been noticed. Thanks.

-------------------------

weitjong | 2017-11-23 06:04:18 UTC | #4

In that case I think we should remove the `cmake_vs2013.bat` file from master branch as well.

-------------------------

