Lichi | 2017-01-02 01:01:33 UTC | #1

Hi, i have a problem, when i compile the project with codeblocks i get this error: unrecognized command line option '-static-libstdc++'.
Any solution?
Thanks :slight_smile:

-------------------------

weitjong | 2017-01-02 01:01:33 UTC | #2

Welcome to our forum.

Although we try to be as inclusive as possible, our build scripts may not able to support all the combinations of IDE/Compiler/Host-system out there. Code::Blocks project using UNIX Makefile with MinGW cross-compiler on Linux host system has been tested to build our project fine. So does the "standalone" MinGW compiler on Windows host system. I can only suspect that the MinGW compiler shipped by the Code::Blocks binary download is the culprit. If you quickly google the "mingw" and "static-libstdc++" as your search keyword then you will find others have encountered the same problem as you as well. One of the search result catches my attention: [mingw-w64.sourceforge.net/download.php](http://mingw-w64.sourceforge.net/download.php), then configure your Code::Blocks to use that toolchain. The TDM-GCC 4.81 may probably make the same 'mistake' as 4.71 in its handling of this compiler flag. So although it is more troublesome, if I were you I would go with standalone MinGW route.

HTH.

-------------------------

Lichi | 2017-01-02 01:01:33 UTC | #3

[quote="weitjong"]Welcome to our forum.

Although we try to be as inclusive as possible, our build scripts may not able to support all the combinations of IDE/Compiler/Host-system out there. Code::Blocks project using UNIX Makefile with MinGW cross-compiler on Linux host system has been tested to build our project fine. So does the "standalone" MinGW compiler on Windows host system. I can only suspect that the MinGW compiler shipped by the Code::Blocks binary download is the culprit. If you quickly google the "mingw" and "static-libstdc++" as your search keyword then you will find others have encountered the same problem as you as well. One of the search result catches my attention: [mingw-w64.sourceforge.net/download.php](http://mingw-w64.sourceforge.net/download.php), then configure your Code::Blocks to use that toolchain. The TDM-GCC 4.81 may probably make the same 'mistake' as 4.71 in its handling of this compiler flag. So although it is more troublesome, if I were you I would go with standalone MinGW route.

HTH.[/quote]

Thank you very much !! MingwW64 worked perfectly. : D

-------------------------

