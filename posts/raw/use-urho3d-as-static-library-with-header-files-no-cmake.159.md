JoshuaBehrens | 2017-01-02 00:58:30 UTC | #1

Hey guys,

I m new to urho but I ll give it a shot. So I compiled the latest commit (because there are the 2Dphysics implemented). In forehand I tried to use a static build, but it had no 2D physics support. But now with the self-compiled version I m asking myself what are the right headers? I can't use the old from v1.31 and I can't see a pattern in the headers so I just copy from the latest commit(in the commit: everything in subdirectories; in the precompiled release: just header files in the main directory and some directories for the 3rd party headers). So how can I retrieve the right headers to use.

Thanks in advance.
- Joshua

-------------------------

friesencr | 2017-01-02 00:58:30 UTC | #2

sometimes i have to nuke the build folder.  give that a try.  the cmake caching system eludes me.

-------------------------

weitjong | 2017-01-02 00:58:30 UTC | #3

Whether you use binary packages from SourceForge which have the Urho3D library precompiled or you compile the Urho3D library yourself from the source code hosted in GitHub repo, eventually you have a few things that you need to setup in your project to link against the Urho3D library:
[ol]
[li]Set the location of Urho3D library[/li]
[li]Se the include directories[/li]
[li]Set the compiler flags and defines[/li][/ol]

If you are using CMake then you can use the provided FindUrho3D cmake module to setup these things automatically for your project (see [urho3d.github.io/documentation/a00004.html](http://urho3d.github.io/documentation/a00004.html)). If you are not using CMake then you can use pkg-config tool to configure these (it is also explained in the same documentation page). If you are configuring them by hand, you can also have a look at the Urho3D.pc file for the pkg-config to give you an idea what is needed.

-------------------------

JoshuaBehrens | 2017-01-02 00:58:31 UTC | #4

@weitjong: That is right. I already have the latest stable version working. But now I compiled the latest commit and I need to know where do I find the right headers (for the include directory). I m neither using CMake nor pkconfig for my project. I just have these libraries linked:
-lUrho3D -lopengl32 -lwinmm -lgdi32 -lws2_32 -lwsock32 -limm32 -lole32 -loleaut32 -luuid -lversion
and these defines:
-DUSE_OPENGL=1
and these include-dirs:
-IUrho3D -IUrho3D/Bullet -IUrho3D/kNet -IUrho3D/SDL -IUrho3D/AngelScript
and the precompiled stable version was working. So now I compiled it by myself and I m searching for the folder where the headers are for these include directories.

-------------------------

weitjong | 2017-01-02 00:58:31 UTC | #5

If I understand your two posts correctly, you are confused about the include directory structure between a source package (or from GitHub repo) and a binary package. In the source package, we include all the header files that are required to build the Urho3D library. While in the binary package, we only include the header files that are required by the Urho3D library user in their own project. That is, the latter does not include all the headers from the third party libraries, it only includes selected few that are directly being referenced by Urho3D own header files.

You can get the latest bleeding edge of Urho3D library and header files in two ways:
[ol]
[li] Get the latest source code from GitHub and build it. You can leave the build artifact in the Urho3D project root tree or install it. The 'install' built-in target will install the Urho3D library and the required header files into a your local file system. The FindUrho3D CMake module should be able to find them in both cases (in project root tree or in installed location).[/li]
[li] Get the latest snapshot binary package for your target platform. It only contains the library and the required header files (as if they are being installed from 'install' built-in target).[/li][/ol]
Since you are not using CMake, I suppose the second way is more suitable for you. You should be able to find the correct header files in the 'include' sub-dir after unzipping the package. I also strongly advice you to have a closer look on the Urho3D.pc file located in the 'lib/pkgconfig' sub-dir, although you are not using pkg-config tool. Below is some content snippet of that file for a 64-bit SHARED lib type. Note that the compiler defines are slightly different between using Urho3D STATIC and Urho3D SHARED lib type. For example, the Urho3D STATIC lib type always require -DURHO3D_STATIC_DEFINE being defined in order to build successfully. Also, note that the compiler flags set in Urho3D.pc in the Windows snapshot binary package found in SourceForge are meant for MinGW compiler (You can get a Urho3D.pc for MSVC if you can get someone with CMake and MSVC build the binary package for you).

[code]Libs:    -L${libdir} -lUrho3D -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lversion -luuid -lws2_32 -lwinmm -lopengl32

Cflags:  -DENABLE_SSE -DENABLE_FILEWATCHER -DENABLE_PROFILING -DENABLE_LOGGING -DUSE_OPENGL -DENABLE_ANGELSCRIPT -DENABLE_LUA  -Wno-invalid-offsetof -ffast-math -m64 -static -static-libstdc++ -static-libgcc  -I${includedir} -I${includedir}/Bullet -I${includedir}/kNet -I${includedir}/SDL -I${includedir}/AngelScript[/code]

Sorry for the long post. English is not my native language too. I tends to write long sentences to convey my short messages :slight_smile: .

-------------------------

JoshuaBehrens | 2017-01-02 00:58:31 UTC | #6

Thank you very much for your reply, you've helped us so much!

We were trying to use Urho3D as a static library, but not make use of CMake. Seeing as we're not used to it and we think it's an overkill to use for our project.

So how did we go about this?

We grabbed the latest master as a zip from the Github page, then run CMake so we could actually build the library (do note one developer is using visual studio and I am using  CodeBlocks).

Once we did this we had the static library but the header files were missing, we didn't know what to do. But as weitjong explained we just had to execute 'make install' (as administrator on Windows seeing as it places the files in C:\Program Files (x86)\Urho3D), once the install was done we could just copy paste the header files into our solution and link against the .lib file.

Thank you so much!

I tried to explain our solution so that if other people are having the same problem they will find this post.

tl;dr
just 'make install' (after compiling the static lib?)

-------------------------

Azalrion | 2017-01-02 00:58:31 UTC | #7

You can change the output of the install command by building the project files using:

[code]-DCMAKE_INSTALL_PREFIX="/path/to/install/dir"[/code]

this can relative for example I use:

[code]-DCMAKE_INSTALL_PREFIX="../Install"[/code]

Which installs to urho3d/Install.

-------------------------

weitjong | 2017-01-02 00:58:32 UTC | #8

Glad to hear that. You don't have to use "administrator" privilege to perform the install if the destination location is somewhere normal user has write permission. Use the CMake option as pointed out by Alex to specify the install location. BTW, I thought you guys don't use CMake at all. Next time perhaps you could be more specific in describing your issue.

-------------------------

JoshuaBehrens | 2017-01-02 00:58:33 UTC | #9

Sorry, I thought it was clear, that we used CMake to "compile" the library as there is no other easy way to generate the library.

-------------------------

