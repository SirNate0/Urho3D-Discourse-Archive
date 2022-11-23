berrymooor | 2018-08-27 22:52:33 UTC | #1

Hi, maybe anyone knows how to attach PackageTool's .pak file to project and use resources from it in AngelScript? For example, textures...

-------------------------

weitjong | 2018-08-28 13:23:39 UTC | #2

There is no special instruction required for AngelScript. The API is the same. Build the "PackageTool" host tool and use it to package the resource dir into a *.pak file. The engine prefers to load relative path name, such as "CoreData", as a package than as a directory. Anyway, if you have "CoreData.pak" then you don't need "CoreData/" directory to be around.

For the bonus, you may also try to experiment with "URHO3D_PACKAGING" build option. Turn it on and the build system will automatically build the host tool mentioned above on the fly and use it to package all the resource dirs provided by the project in one go. However, currently this option does not work for Android Gradle build system (yet).

-------------------------

