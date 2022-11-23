TheComet | 2017-01-02 00:57:43 UTC | #1

Hi!

I tried building Urho3D on Win7 x64 using Visual Studio 2010, and am running into problems. I'll list in detail what I did.

[code](get version 1.23)
git clone https://github.com/urho3d/Urho3D.git
cd Urho3D
git checkout -b stable v1.23

(generate nmake makefiles)
mkdir build-vc10
cd build-vc10
cmake -G "NMake Makefiles" ..

(compile)
nmake

NOTE: This was done from inside the "Visual Studio Development Console 2010", which is basically the windows command prompt only with some extra local environment variables set up.[/code]

The first error I got was the following:

[img]http://i1.someimage.com/0yxqOvU.png[/img]

I edited CMakeLists.txt in the Urho3D root directory to disable precompiled headers and retried. Everything went fine until this next error popped up:

[img]http://i1.someimage.com/qWvZned.png[/img]

Does anyone know what's going on?

The library compiles fine on my linux machine using gcc 4.6.3

[EDIT] When running nmake again after the last error, I get the following, different error message:

[img]http://i1.someimage.com/VMsPaxW.png[/img]

-------------------------

cadaver | 2017-01-02 00:57:43 UTC | #2

Is there a specific reason you want to use version 1.23? I would actually recommend just using master (or at least 1.3) for more features and fixes.

I don't think out-of-source build, or using Urho as an external library is supported in 1.23 version yet, so you have to use the provided cmake_vs2010.bat file, which will setup an in-source build.

-------------------------

TheComet | 2017-01-02 00:57:43 UTC | #3

I tried compiling master, and the first issue with precompiled headers did not show up anymore. I am still getting the second error though.

Interestingly, if I generate Visual Studio solution files and compile it through the IDE, it successfully compiles everything, where as if I try to use nmake, it hangs at the second error.

I need to use nmake because I'm setting up a continuous integration server and the build process needs to be instantiated from the command line.

I also have a question regarding static/dynamic configurations: If I specify -DCMAKE_BUILD_TYPE=Debug and -DURHO3D_LIB_TYPE=Shared, this should build the debug version of a shared lib version, right?

-------------------------

cadaver | 2017-01-02 00:57:44 UTC | #4

I have not tested "NMake Makefiles" generator at all, it's possible there's a bug either in our CMake script, or in the generator, in relation to precompiled headers.

I suggest that you use the "Visual Studio 10" generator like you would if compiling manually with VS, but then invoke MSBuild to build the Urho solution automatically. The VS generator includes both debug & release configs into the solution file, but you can choose the config when running MSBuild, eg.

MSBuild Urho3D.sln /p:Configuration=Debug

-------------------------

carlomaker | 2017-01-02 00:57:44 UTC | #5

I use without problem  cmake 2.8.12.1 with vs2010 ( cmake_vs2010.bat)

-------------------------

alexrass | 2017-01-02 00:57:47 UTC | #6

For build Urho3D by NMake, need disable precompiled header in Assimp.
Easy way:
patch for file Urho3D\Source\ThirdParty\Assimp\CMakeLists.txt

[code]@@ -701,10 +701,16 @@ SET( CONTRIB_FILES
 	# Necessary to show the headers in the project when using the VC++ generator:

 	${Boost_SRCS}

 )

 

 if (MSVC)

+	if (CMAKE_BUILD_TOOL STREQUAL "nmake")

+		set(NMAKE TRUE)

+	endif ()

+endif ()

+

+if (MSVC AND NOT NMAKE)

     foreach(FILE ${SOURCE_FILES})

         if (${FILE} MATCHES "[A-Za-z0-9 _/]*[.]cpp")

             if (${FILE} MATCHES "AssimpPCH.cpp$")

                 set_source_files_properties(${FILE} PROPERTIES COMPILE_FLAGS "/YcAssimpPCH.h")

             else ()

[/code]

-------------------------

