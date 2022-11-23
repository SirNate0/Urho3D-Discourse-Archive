NemesisFS | 2017-01-02 00:59:29 UTC | #1

Hi,


after a while I picked my project up again and so far have made some progress with this awesome eninge!
Doing so  I have encountered a few things that are bothering me.
The build system is still not very consistend with the cmake conventions which has resulted in some trouble for my project:
I want to use a CMakeLists.txt in my project-root but when I do this the executable is always put out to $CMAKE_SOURCE_DIR/../Bin. I havent found a way to work around this, I guess its comes beacuse the Urho3D CMakeLists.txt resides in its Source Folder instead of the project root. Also quite confusing is the use of the macrof for setup_main_executable as those seem to do quite a lot of stuff which should be done by the using project itself like setting the exe type, modifying the includes&libraries etc. I`d much prefer a solution where the FindUrho3D.cmake sets the variables needed for setting up the executable (Urho3D_INCLUDE_DIRS and Urho3D_LIBRARIES, see [url]http://www.cmake.org/Wiki/CMake:How_To_Find_Libraries#Writing_find_modules[/url] and [url]http://www.cmake.org/Wiki/CMake/Tutorials/How_to_create_a_ProjectConfig.cmake_file[/url]) and leaving that work to the project developer.

Regarding the logging I find it strange that, if you use Urho3D as a library you cant change the loglevel that was set when compiling and also the convenience macros like LOG_DEBUG wont work as they are disabled during compile time.

Greetings,
NemesisFS

-------------------------

weitjong | 2017-01-02 00:59:29 UTC | #2

As the main maintainer of the build scripts, this is getting old to me. I think I have explained the rationale why we moved the CMakeLists.txt from root to the Source directory in the previous discussion threads. I have also explained why we need to make certain assumption on our project structure so we can write concise and reusable macros for all our targets in our project in a cross-platform manner.

If you just want to use Urho3D as an external library in your own project then you don't have to use our macros, if you think it does too many things than what you need. You don't have to use Urho3D-CMake-common module even for that matter, if you want the full control on how to setup your own project.

Back to your issues.
[ol]
[li] The location of runtime output directory is set in line 332 of Urho3D-CMake-common module.
[code]set_output_directories (${PROJECT_ROOT_DIR}/${PLATFORM_PREFIX}Bin RUNTIME PDB)[/code]You can modify this location as you see fit, however, you will be on your own to make the build scripts work for all the Urho3D supported platforms afterward. There are other build scripts down the road that expect/assume the location of the output directory as per originally designed, so you may have to change those scripts as well.

[/li]
[li] The setup_main_executable macro doing too many things. This is a rather strange complain. It is just a macro. The things that it does need to be carried out one way or another for each target. Without the macro(s), we will have to repeat the similar commands all over the places for each of our internal target. Besides, with the macros, we only need to change one place for any bug fixes or enhancement. Again, you don't have to use it. You can always just use the original commands provided by the CMake to setup your target, if that works best for you.

[/li]
[li] I agree our scripts do not follow the convention out there. As you may already know we don't force our user to install Urho3D library into a local filesystem in order to use it as external library. Or otherwise we could shorten the FindUrho3D module size by half. We could remove away those cross platform logic too to make it 100% conformant with the CMake's Wiki. The question is, why we want to do that?

It reminds me of a story about a farmer, and his son, and a donkey. We cannot keep everyone happy. Having said that, if you think you can do it better then you can submit your changes as pull request.[/li][/ol]
I have no comment on the logging issue as I failed to reproduce the problem. I am able to call logging macros in my test external project. Ensure your project has defined the "URHO3D_LOGGING" compiler definition. I can change the logging level in runtime also as per documentation.

-------------------------

NemesisFS | 2017-01-02 00:59:31 UTC | #3

Thanks for your reply.
1. I didnt find the location to change the output, I will use that now. Would it be possible to use the  EXECUTABLE_OUTPUT_PATH variable in that location instead (and maybe also the references) or does something speak against this?
2. Could you tell me where the FindUrho3D.cmake saves the include dirs needed for compiling against Urho3D? The libraries are set in URHO3D_LIBRARIES but I cannot find the includes...
3. It looks like I lack knowledge of the build process of urho. From an uninformed standpoint it just looks unnecessary as cmake is designed to support cross platform builds. When I undestand the build process better I hope my confusion cleared up or im able to supply patches so that I can help instead of only criticising.

Also you were right about the logging problem that solved itself for now, I set some variables wrong.

-------------------------

weitjong | 2017-01-02 00:59:33 UTC | #4

[ol]
[li] You can find the references easily using git grep command.
[code]$ git grep '${PROJECT_ROOT_DIR}'
Docs/CMakeLists.txt:            COMMAND ${PROJECT_ROOT_DIR}/Bin/ScriptCompiler -dumpapi ScriptAPI.dox AngelScriptAPI.h
Docs/CMakeLists.txt:        file (GLOB PKGS RELATIVE ${PROJECT_ROOT_DIR}/Source/Engine/LuaScript/pkgs ${PROJECT_ROOT_DIR}/Source/Engine/LuaScript/pkgs/*.pkg)
Docs/CMakeLists.txt:        file (WRITE ${PROJECT_ROOT_DIR}/Bin/LuaPkgToDox.txt ${PKGLIST})
Docs/CMakeLists.txt:            COMMAND ${PROJECT_ROOT_DIR}/Bin/tolua++ -L ToDoxHook.lua -P -o ${CMAKE_CURRENT_SOURCE_DIR}/LuaScriptAPI.dox ${PROJECT_ROOT_DIR}/Bin/LuaPkgToDox.tx
Docs/CMakeLists.txt:            WORKING_DIRECTORY ${PROJECT_ROOT_DIR}/Source/Engine/LuaScript/pkgs
Source/CMake/Modules/FindUrho3D.cmake:    set (URHO3D_HOME ${PROJECT_ROOT_DIR} CACHE PATH "Path to Urho3D project root tree" FORCE)
Source/CMake/Modules/Urho3D-CMake-common.cmake:set_output_directories (${PROJECT_ROOT_DIR}/${PLATFORM_PREFIX}Bin RUNTIME PDB)
Source/CMake/Modules/Urho3D-CMake-common.cmake:        list (APPEND SOURCE_FILES ${PROJECT_ROOT_DIR}/Source/ThirdParty/SDL/src/main/android/SDL_android_main.c)
Source/CMake/Modules/Urho3D-CMake-common.cmake:        set (RESOURCE_FILES ${PROJECT_ROOT_DIR}/Bin/CoreData ${PROJECT_ROOT_DIR}/Bin/Data)
Source/CMakeLists.txt:file (GLOB APP_SCRIPTS ${PROJECT_ROOT_DIR}/Bin/${SCRIPT_PATTERN})
Source/CMakeLists.txt:install (DIRECTORY ${PROJECT_ROOT_DIR}/Bin/CoreData ${PROJECT_ROOT_DIR}/Bin/Data DESTINATION ${DEST_RUNTIME_DIR} ${DEST_PERMISSIONS})
Source/CMakeLists.txt:install (DIRECTORY ${PROJECT_ROOT_DIR}/Source/CMake/ DESTINATION ${DEST_SHARE_DIR}/CMake ${DEST_PERMISSIONS})    # Note: the trailing slash is significant
Source/CMakeLists.txt:file (GLOB CMAKE_SCRIPTS ${PROJECT_ROOT_DIR}/${SCRIPT_PATTERN})
Source/CMakeLists.txt:set (CPACK_RESOURCE_FILE_LICENSE ${PROJECT_ROOT_DIR}/License.txt)
Source/Engine/CMakeLists.txt:    set (OUTPUT_PATH ${PROJECT_ROOT_DIR}/${PLATFORM_PREFIX}Lib)     # ${PLATFORM_PREFIX} is empty for native build
Source/Engine/LuaScript/CMakeLists.txt:    execute_process (COMMAND ${PROJECT_ROOT_DIR}/Bin/tolua++ -v RESULT_VARIABLE TOLUA_EXIT_CODE OUTPUT_QUIET ERROR_QUIET)
Source/Engine/LuaScript/CMakeLists.txt:        COMMAND ${PROJECT_ROOT_DIR}/Bin/tolua++ -L ToCppHook.lua -o ${CMAKE_CURRENT_BINARY_DIR}/${GEN_CPP_FILE} ${NAME}
Source/ThirdParty/LuaJIT/CMakeLists.txt:    execute_process (COMMAND ${PROJECT_ROOT_DIR}/Bin/${BUILDVM_X} RESULT_VARIABLE BUILDVM_EXIT_CODE OUTPUT_QUIET ERROR_QUIET)
Source/ThirdParty/LuaJIT/CMakeLists.txt:        file (WRITE ${PROJECT_ROOT_DIR}/Bin/${BUILDVM_X}-arch.txt ${TARGET_TESTARCH})
Source/ThirdParty/LuaJIT/CMakeLists.txt:    file (GLOB VARIANT_ARCHS ${PROJECT_ROOT_DIR}/Bin/buildvm-*-arch.txt)
Source/ThirdParty/LuaJIT/CMakeLists.txt:        COMMAND ${PROJECT_ROOT_DIR}/Bin/${BUILDVM_X} -m ${mode} -o ${GEN_SRC} ${ARGN}
Source/ThirdParty/LuaJIT/CMakeLists.txt:    set (LUAJIT_DEP_DIR ${PROJECT_ROOT_DIR}/Bin/Data/LuaScripts/jit)
Source/ThirdParty/LuaJIT/CMakeLists.txt-buildvm.in:    COMMAND ${PROJECT_ROOT_DIR}/Bin/minilua ${DASM} ${DASM_FLAGS} -o ${GEN_ARCH_H} ${DASM_DASC}
Source/ThirdParty/LuaJIT/DetectTargetArchitecture.cmake:            "To recover from this error, remove this file (generated by Android build script when LuaJIT is enabled) in ${
(END)[/code]As you can see there are only two occurrences of '${PROJECT_ROOT_DIR}/${PLATFORM_PREFIX}'. One for the Bin and one for the Lib. Once set, CMake is smart enough to handle the rest. In my last post, I was more worry about the scripts which referencing the tools. The tools are usually built natively even though we are cross-compiling to target a different platform. So they are always expected to be found in '${PROJECT_ROOT_DIR}/Bin' directory regardless of the platform. Thus you need to adjust the tool location accordingly for those scripts if you change the RUNTIME output location. Using a single variable EXECUTABLE_OUTPUT_PATH may not work when your platform-specific output directory is different than the native output directory.

[/li]
[li] Using git grep again. I think it is clear in which variable it is saved. [code]$ git grep INCLUDE Source/CMake/Modules/FindUrho3D.cmake
Source/CMake/Modules/FindUrho3D.cmake:#  URHO3D_INCLUDE_DIRS
Source/CMake/Modules/FindUrho3D.cmake:        set (URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE})
Source/CMake/Modules/FindUrho3D.cmake:            list (APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR})     # Note: variable change to list context after this
Source/CMake/Modules/FindUrho3D.cmake:            list (APPEND URHO3D_INCLUDE_DIRS ${URHO3D_HOME}/Source/ThirdParty/${DIR})
Source/CMake/Modules/FindUrho3D.cmake:        list (APPEND URHO3D_INCLUDE_DIRS ${BINARY_DIR}/Engine)
Source/CMake/Modules/FindUrho3D.cmake:    find_path (URHO3D_INCLUDE_DIRS Urho3D.h PATHS ${URHO3D_INC_SEARCH_PATH} PATH_SUFFIXES ${PATH_SUFFIX})
Source/CMake/Modules/FindUrho3D.cmake:    if (URHO3D_INCLUDE_DIRS)
Source/CMake/Modules/FindUrho3D.cmake:        set (BASE_DIR ${URHO3D_INCLUDE_DIRS})
Source/CMake/Modules/FindUrho3D.cmake:            list (APPEND URHO3D_INCLUDE_DIRS ${BASE_DIR}/${DIR})     # Note: variable change to list context after this, so we need BASE_DIR
Source/CMake/Modules/FindUrho3D.cmake:if (URHO3D_INCLUDE_DIRS AND URHO3D_LIBRARIES)
Source/CMake/Modules/FindUrho3D.cmake:    FIND_PACKAGE_MESSAGE (Urho3D ${FOUND_MESSAGE} "[${URHO3D_LIBRARIES}][${URHO3D_INCLUDE_DIRS}]")
Source/CMake/Modules/FindUrho3D.cmake:mark_as_advanced (URHO3D_INCLUDE_DIRS URHO3D_LIBRARIES URHO3D_SOURCE_TREE)
(END)
[/code] Remember this module works in two modes (Urho3D build tree detection mode or Urho3D SDK installation mode). The first part of the grep result shows how the include directory is appended using URHO3D_HOME build tree. The second part shows how it is obtained using CMake's find_path command to find the installed Urho3D SDK in a filesystem. You may want to check how the build scripts perform the install operation for the include directory in order to see the full picture.[/li][/ol]

-------------------------

