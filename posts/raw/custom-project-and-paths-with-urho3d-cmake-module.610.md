sabotage3d | 2017-01-02 01:01:39 UTC | #1

Hi ,
I am having some issues in larger projects where I would like to import Urho3d using its cmake common module .
It seems it has some paths hard-coded like CoreData and Data are always expected one level above where I would like to be able to set them to the same level as my source files. 

[code]  if (XCODE)
        set (RESOURCE_FILES ${PROJECT_ROOT_DIR}/Bin/CoreData ${PROJECT_ROOT_DIR}/Bin/Data)
        set_source_files_properties (${RESOURCE_FILES} PROPERTIES MACOSX_PACKAGE_LOCATION Resources)
        list (APPEND SOURCE_FILES ${RESOURCE_FILES})
    endif ()[/code]

I have also compiled Urho3D IOS static libraries to custom location which doesn't play nice with the Urho3d common module. Is there any workaround at the moment to set custom location for the headers and libraries ?
I am not entirely sure as well how to fit these macros into larger project is there a way to expand them so that I can tweak them accordingly ?

[code]# Define target name
set (TARGET_NAME PorjectName)

# Define source files
#define_source_files ()

# Setup target with resource copying
setup_main_executable ()[/code]

Thanks in advance,

Alex

-------------------------

weitjong | 2017-01-02 01:01:39 UTC | #2

[quote="sabotage3d"]It seems it has some paths hard-coded like CoreData and Data are always expected one level above where I would like to be able to set them to the same level as my source files.[/quote]
This has been discussed before in other thread. If you want to use Urho3D macros and modules then you have to structure your project to what it expects. Or you can tweak it to your heart content to suit your own project need. Currently Urho3D project structure has a project root dir which is the parent directory of the source tree (where the main CMakeLists.txt resides), the build tree(s), and all the other non-source subdirs (such as assets and docs). I suppose you have put your main CMakeLists.txt at the top level directory in your own project, so effectively making your top dir becoming the source tree as well and therefore the module get confused. If your own project structure differs from the module's current expectation/assumption then using our module as it is will hinder you more than actually helping you. Having said that, it occurs to me that a lot of you like to have your main CMakeLists.txt to be resided in the project root/top directory, so it may be time for another build script refactor.

[quote="sabotage3d"]I have also compiled Urho3D IOS static libraries to custom location which doesn't play nice with the Urho3d common module. Is there any workaround at the moment to set custom location for the headers and libraries ?[/quote]
In my opinion this has nothing to do with the Urho3D-CMake-common.cmake module, but with the FindUrho3D.cmake module. There is nothing magical about these modules. If you build the library into some custom location, how would it know where to find it? Currently the FindUrho3D module has two finding modes. 1) It finds the library using URHO3D_HOME environment variable. 2) It finds the library (SDK installation) using CMAKE_PREFIX_PATH environment variable (need to be provided when the library is not installed to the system-wide default destination such as "/usr/local" on Linux host). For the second mode to work, you need to use the documented SDK installation step to install the Urho3D library (and its header files) into a custom location of your choice.

-------------------------

sabotage3d | 2017-01-02 01:01:39 UTC | #3

Thank you weitjong,

I know that similar issues were discussed before. I wanted to check before I write my own Cmake script. Is it currently possible just to extract CMAKE_CXX_FLAGS, CMAKE_EXE_LINKER_FLAGS and any preprocessor macros depending on the platform from the Urho3d configuration script, that would be really useful.

-------------------------

weitjong | 2017-01-02 01:01:39 UTC | #4

[quote="sabotage3d"]Is it currently possible just to extract CMAKE_CXX_FLAGS, CMAKE_EXE_LINKER_FLAGS and any preprocessor macros depending on the platform from the Urho3d configuration script, that would be really useful.[/quote]
Yes, it is possible. See the updated section of this page relating to pkg-config. [urho3d.github.io/documentation/H ... hPkgConfig](http://urho3d.github.io/documentation/HEAD/_using_library.html#FromSDKWithPkgConfig).

-------------------------

sabotage3d | 2017-01-02 01:01:40 UTC | #5

I think Urho3d Cmake is already really good. For the libraries I have a custom build system for IOS that builds the libraries and combines all the archs into one static lib. All my libraries are in one folder called lib. 
Does it expects subfolders as it cannot them find them properly. Is there currently any flag that I can use to point it to these libs directly .

This is my libraries folder structure :
[code]lib/
libkNet.a
libUrho3D.a
libStanHull.a
libSTB.a
libSDL.a
libRecast.a
libPugiXml.a
libLZ4.a
libJO.a
libFreeType.a
libDetour.a
libCivetweb.a
libBullet.a
libBox2D.a
libAngelScript.a[/code]

It would be awesome if we can have a variable for where the Data folder resides. 

Thanks,
Alex

-------------------------

weitjong | 2017-01-02 01:01:40 UTC | #6

[quote="sabotage3d"]For the libraries I have a custom build system for IOS that builds the libraries and combines all the archs into one static lib.[/quote]
Have you tried our undocumented custom built-in target "Urho3D_universal" for iOS build? It is being used in our CI build to produce Mach-O universal binary already.

[quote="sabotage3d"]Does it expects subfolders as it cannot them find them properly. Is there currently any flag that I can use to point it to these libs directly.[/quote]
As the Urho3D library for native Mac OS X and iOS platform could be potentially installed in a same destination using the same location pointed by CMAKE_INSTALL_PREFIX, we have decided to install the library for the iOS platform under an extra subdir called "ios" to avoid the libs from overwriting each other. If you use our built-in target "install" for iOS build then you should find iOS lib is installed in something like: ${CMAKE_INSTALL_PREFIX}/lib/ios/libUrho3D.a. Since you are using your own custom build system, you don't have to follow this. But if so, you have to tweak the existing FindUrho3D CMake module to comment these lines out.
[code]if (IOS)
    set (CMAKE_LIBRARY_ARCHITECTURE ios)
endif ()[/code]

[quote="sabotage3d"]It would be awesome if we can have a variable for where the Data folder resides.[/quote]
Hey, I am also thinking about that idea as well as it will circumvent some of the difficulties we are facing. I think it is a good idea.

-------------------------

sabotage3d | 2017-01-02 01:01:41 UTC | #7

Thanks a lot weitjong,

One last suggestion if we can have URHO3D_LIB_SEARCH_PATH exposed as external variable or a new variable like in boost URHO3D_LIBRARYDIR would be great . Other than that I think Urho3d cmake script is near perfection for OSX and IOS at the moment. Last night I was able to override some of the macros in my cmake project which makes it quite modular and nice to work with .

-------------------------

weitjong | 2017-01-02 01:01:42 UTC | #8

[quote="sabotage3d"]One last suggestion if we can have URHO3D_LIB_SEARCH_PATH exposed as external variable or a new variable like in boost URHO3D_LIBRARYDIR would be great.[/quote]
If I understand it correctly, boost library has come up with BOOST_LIBRARYDIR and BOOST_INCLUDEDIR variable. Both of them can be replaced by a single variable CMAKE_PREFIX_PATH in my opinion. The prefix path is set to the parent directory where the "include" and the "lib" subdirs reside.

[quote="sabotage3d"]Last night I was able to override some of the macros in my cmake project which makes it quite modular and nice to work with .[/quote]
If you think your revision is generic and also useful for others then you may consider to share them. Slight off topic but I may attempt to perform a build system refactoring soon. So any inputs to make it better than now are welcome.

-------------------------

