alexrass | 2017-01-02 00:58:05 UTC | #1

If compile Urho3D on windows with mingw, lib has name "libUrho3D.dll". 
For disable lib prefix set  prefix options in "Source/Engine/CMakeLists.txt":

[code]@@ -172,6 +172,9 @@
         get_target_property (LINK_LIBRARIES ${TARGET_NAME} LINK_LIBRARIES)
         target_link_libraries (${TARGET_NAME} LINK_PRIVATE ${LINK_LIBRARIES})
     endif ()
+	if (WIN32 AND NOT MSVC)
+		set_target_properties (${TARGET_NAME} PROPERTIES PREFIX "")
+	endif ()
 else ()
     set_target_properties (${TARGET_NAME} PROPERTIES LINK_LIBRARIES "")
 endif ()[/code]

-------------------------

weitjong | 2017-01-02 00:58:05 UTC | #2

Thanks for pointing this out. If I set that as is, I believe the setting would get applied when building for Windows platform using MinGW cross-compiler toolchain on a Linux host system as well. Also, does it have any implication with FindUrho3D CMake module on both Windows and Linux host/build systems?

-------------------------

alexrass | 2017-01-02 00:58:05 UTC | #3

This option affects to shared lib. 
FindUrho3D looking for an import library, I think it won't affect him. 
But with cross compilation I don't know...

-------------------------

weitjong | 2017-01-02 00:58:05 UTC | #4

Yup. I just did a quick check on the cross-compiling MinGW. It only affect the shared lib name. The import lib name stays the same. I will commit the changes soon.

-------------------------

alexrass | 2017-01-02 00:58:06 UTC | #5

May be need to add this option: "set (CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -static')". To remove mingw runtime from dll.
Total:
[code]
@@ -167,6 +167,10 @@
         get_target_property (LINK_LIBRARIES ${TARGET_NAME} LINK_LIBRARIES)
         target_link_libraries (${TARGET_NAME} LINK_PRIVATE ${LINK_LIBRARIES})
     endif ()
+	if (WIN32 AND NOT MSVC)
+		set_target_properties (${TARGET_NAME} PROPERTIES PREFIX "")
+		set (CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -static")        
+	endif ()
 else ()
     set_target_properties (${TARGET_NAME} PROPERTIES LINK_LIBRARIES "")
 endif ()
[/code]

-------------------------

weitjong | 2017-01-02 00:58:06 UTC | #6

The linker flags will be set globally as in other compiler flags for MinGW. I have committed the changes.

-------------------------

alexrass | 2017-01-02 00:58:06 UTC | #7

Ok. Windows way library naming )))

-------------------------

cadaver | 2017-01-02 00:58:06 UTC | #8

JTippetts has run into a problem with the naming change affecting static MinGW-built library ([github.com/urho3d/Urho3D/issues/223](https://github.com/urho3d/Urho3D/issues/223))

EDIT: I believe this is fixed now. Tested both a static & shared library build. The static build and shared build import library have lib-prefix, Urho3D.dll does not.

-------------------------

