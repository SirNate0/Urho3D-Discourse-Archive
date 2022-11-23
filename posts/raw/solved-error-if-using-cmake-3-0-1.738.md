alexrass | 2017-01-02 01:02:34 UTC | #1

[code]CMake Error: Error in cmake code at
/home/alex/projects/Urho3D/CMake/Modules/Urho3D-CMake-common.cmake:768:
Parse error.  Function missing ending ")".  Instead found bad character with text "[".
CMake Error at CMakeLists.txt:47 (include):
  include could not find load file:

    /home/alex/projects/Urho3D/CMake/Modules/Urho3D-CMake-common.cmake


CMake Error at Source/ThirdParty/FreeType/CMakeLists.txt:80 (setup_library):
  Unknown CMake command "setup_library".


-- Configuring incomplete, errors occurred![/code]

Google say it problem in CMake 3.0
I temporarily fix it, but i not sure this is correct or not

[quote]@@ -763,19 +763,19 @@ if (IOS)
     # TODO: can be removed when CMake minimum required has reached 2.8.12

     if (CMAKE_VERSION VERSION_LESS 2.8.12)

         # Due to a bug in the CMake/Xcode generator (prior to version 2.8.12) where it has wrongly assumed the IOS bundle structure to be the same as MacOSX bundle structure,

         # below temporary fix is required in order to solve the auto-linking issue when dependent libraries are changed

         add_custom_target (FIX_DEPEND_HELPER ALL

-            if [ ${CMAKE_BINARY_DIR}/CMakeScripts/XCODE_DEPEND_HELPER.make -nt ${CMAKE_BINARY_DIR}/CMakeScripts/.fixed-depend-helper ]\; then sed -i '' 's/\/Contents\/MacOS//g' ${CMAKE_BINARY_DIR}/CMakeScripts/XCODE_DEPEND_HELPER.make\; touch ${CMAKE_BINARY_DIR}/CMakeScripts/.fixed-depend-helper\; fi

+            "if [ ${CMAKE_BINARY_DIR}/CMakeScripts/XCODE_DEPEND_HELPER.make -nt ${CMAKE_BINARY_DIR}/CMakeScripts/.fixed-depend-helper ]\; then sed -i '' 's/\/Contents\/MacOS//g' ${CMAKE_BINARY_DIR}/CMakeScripts/XCODE_DEPEND_HELPER.make\; touch ${CMAKE_BINARY_DIR}/CMakeScripts/.fixed-depend-helper\; fi"

             COMMENT "Checking if the CMake/Xcode depend helper scripts need to be fixed")

     endif ()

 

     # Due to a bug in the CMake/Xcode generator (still exists in 3.1) that prevents iOS targets (library and bundle) to be installed correctly

     # (see [public.kitware.com/Bug/bug_relat ... dependency](http://public.kitware.com/Bug/bug_relationship_graph.php?bug_id=12506&graph=dependency)),

     # below temporary fix is required to work around the bug

     add_custom_target (FIX_INSTALL ALL

-        if [ ${CMAKE_BINARY_DIR}/CMakeScripts/install_postBuildPhase.makeDebug -nt ${CMAKE_BINARY_DIR}/CMakeScripts/.fixed-install ]\; then sed -i '' 's/EFFECTIVE_PLATFORM_NAME//g' ${CMAKE_BINARY_DIR}/CMakeScripts/install_postBuildPhase.make*\; touch ${CMAKE_BINARY_DIR}/CMakeScripts/.fixed-install\; fi

+        "if [ ${CMAKE_BINARY_DIR}/CMakeScripts/install_postBuildPhase.makeDebug -nt ${CMAKE_BINARY_DIR}/CMakeScripts/.fixed-install ]\; then sed -i '' 's/EFFECTIVE_PLATFORM_NAME//g' ${CMAKE_BINARY_DIR}/CMakeScripts/install_postBuildPhase.make*\; touch ${CMAKE_BINARY_DIR}/CMakeScripts/.fixed-install\; fi"

         COMMENT "Checking if the CMake/Xcode install scripts need to be fixed")

 endif ()

 

 # Macro for adjusting target output name by dropping _suffix from the target name

 macro (adjust_target_name)

[/quote]

-------------------------

weitjong | 2017-01-02 01:02:35 UTC | #2

This is a known bug in CMake 3.0. The regression bug is fixed since CMake 3.0.2. See [cmake.org/Bug/view.php?id=15092](http://www.cmake.org/Bug/view.php?id=15092)
Unfortunately the workaround to stringify the whole command as you suggested or the workaround just to stringify the brackets as sighted in their bug tracker does not work in our case. It only helps in allowing the faulty CMake parser to parse the command, however, the resultant command become an invalid one. This is the reason why we only use double quotes to stringify our arguments in our CMake rules sparingly and only when it is absolutely necessary, because CMake has a tendency to perform character escaping behind our back. And in this case the extra character escaping proves fatal to render the command becomes an invalid one.

Since this is a bug on CMake side and there are no known working workaround, I think we have to deal with this by asking user to upgrade their CMake to version 3.0.2 or above; or stays below 3.0.

-------------------------

weitjong | 2017-01-02 01:02:35 UTC | #3

Correction: The workaround to just stringify the brackets as sighted in CMake bug tracker actually works, despite on CMake 3.1 this workaround itself would produce yet another unrelated CMake warning. Anyways, I have decided to dumb down the post-CMake fix logic to avoid this CMake parsing error. The commit has been pushed in the master branch just now.

-------------------------

