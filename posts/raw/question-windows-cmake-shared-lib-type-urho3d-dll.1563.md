ghidra | 2017-01-02 01:08:32 UTC | #1

Nothing is broken. I just have some best practices questions.
I'm using Urho as a shared library, built with cmake.  here is my directory structure:

Dev
|--Urho3D (Source)
|--Urho_Build (Shared Library)
|--MyProject
|   |--bin
|   |   |--CoreData (aliased)
|   |   |--Data (aliased)
|   |   |--MyProject.exe
|   |   |--Urho3D.dll (aliased) <--------(method in question)
|   |--CMake (aliased)
|   |--Etc....

So, if I DO NOT have that Urho3D.dll in there with the exe, it will NOT launch.

Consulting the docs, it mentions in the third paragraph of the "Library Build" section install paths and CMAKE_INSTALL_PREFIX. As well mentions that DESTDIR (side note it is written as DESDIR and DESTDIR). Saying that DESTDIR is not relevant on windows. I rebuilt Urho setting the CMAKE_INSTALL_PREFIX to my build directory, but that didn't seem to make a difference. So, that's where I decided to just symlink it to my projects bin folder. But that's not mentioned in the docs...

Which leaves me wondering, what is the preferred method here? Or, did I miss something or misinterpret something from the docs?

-------------------------

Canardian | 2017-01-02 01:08:32 UTC | #2

You could also include the directory where Urho3D.dll is located in the PATH environment variable.
Another way would be to do a ChDir() from your application to the directory where the dll is located.

Here's some more info how dll's are located:
[msdn.microsoft.com/en-us/library/7d83bc18.aspx](https://msdn.microsoft.com/en-us/library/7d83bc18.aspx)

About best practices, I would prefer to do a ChDir() to a bin subdirectory in your application directory.
But I use always Urho3D as a static lib, so that my whole application is just one single exe, and the assets are in the exe too.
No installer needed, no runtime dlls needed (when using MinGW), and I'll make an online updater too which will patch the single exe.

-------------------------

jmiller | 2017-01-02 01:08:32 UTC | #3

To add some ideas for general reference..

On a dev system with several projects using the same master Urho library, I link Urho3D.dll and Urho3D_d.dll to a directory that's in my path.

[b]Link ShellExtension[/b] is great for making and explaining NTFS links.
[schinagl.priv.at/nt/hardlinkshel ... nsion.html](http://schinagl.priv.at/nt/hardlinkshellext/linkshellextension.html)

Maybe in most cases I would link the DLLs to each app's bin directory:
Shared libs there take precedence, so the app can use a specific Urho library.
It's easy to package for end-users: common file copies like with Explorer copy the link [i]targets[/i] by default. Many command-line tools like cp and xcopy offer a switch.
I've also linked CoreData for this behavior.

-------------------------

weitjong | 2017-01-02 01:08:32 UTC | #4

At the moment you have to pass similar build options used when building the Urho3D library to your own project using the Urho3D library. In this case you have to pass "-D URHO3D_LIB_TYPE=SHARED". Since release 1.5, we have added an automation step to auto-copy the Urho3D.dll or Urho3D_d.dll next to the target binary. In the near future we will change things a little bit more to bring in more automation so to avoid the downstream projects using Urho3D library have to repeat the build options used when building the library. But until then, I have just tested adding the above works.

-------------------------

ghidra | 2017-01-02 01:08:33 UTC | #5

[quote]
At the moment you have to pass similar build options used when building the Urho3D library to your own project using the Urho3D library.
[/quote]

At the risk of literally repeating what you just said...
Does this mean that when running cmake in my own project (MyProject in the case of this example), which currently I do like so (for mingw):

[code]
cmake -G "MinGW Makefiles"
[/code]

would be something like this?:

[code]
cmake -G "MinGW Makefiles" -D URHO3D_LIB_TYPE=SHARED
[/code]

-------------------------

weitjong | 2017-01-02 01:08:33 UTC | #6

Yes and No :slight_smile:  If you pull the latest master branch then the lib type should be now fully auto detected.

-------------------------

