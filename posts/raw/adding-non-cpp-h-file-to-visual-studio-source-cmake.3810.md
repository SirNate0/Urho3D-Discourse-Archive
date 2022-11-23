TrevorCash | 2017-12-01 18:33:54 UTC | #1

Hello everyone,

I want to include a generic file as part of my visual studio source.  Specifically Urho3D.natvis.

The following cmake line does not seem to work:

> define_source_files (Urho3D.natvis)

The file is right alongside all the other .cpp and .h files.  is there some macro I am missing?

Thanks - Trevor

-------------------------

weitjong | 2017-12-02 16:37:26 UTC | #2

The purpose of `define_source_files()` macro is to collect the C/C++ source code and header files under the current scope and use that information to populate the CMake variables. You should not call the macro the second time or in the manner you posted above. Instead, you should adjust the macro arguments as necessary when you have non-common extension source/header files to be included in the one-and-only call to this macro (per scope). However, you should not use it to include non source/header files. But nothing prevent you from calling the CMake provided command directly to add other files as source for a CMake target. Probably you will have to set the source properties of this other files too, if you do that, or else CMake might complain it does not know what to do with it.

-------------------------

TrevorCash | 2017-12-05 23:55:13 UTC | #3

Thanks weitjong,

Adding this after my single call to define_source_files() seems to do the trick:
> 
> if(MSVC)
> 	#add a natvis file for better debug support in visual studio.
> 	set(SOURCE_FILES ${SOURCE_FILES} Urho3D.natvis)
> endif(MSVC)

-------------------------

