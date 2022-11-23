zedraken | 2017-08-19 15:56:22 UTC | #1

Hi,

I started to build the v1.7 in debug mode under Linux Fedora 23 64 bits with the following command line:

./cmake_generic.sh ../build -DCMAKE_BUILD_TYPE=debug -DCMAKE_INSTALL_PREFIX=/usr/local

All goes fine until I reach the step in which _AssetImporter_ is linked. Such operation fails and ends with the following errors:

> ../../ThirdParty/Assimp/libAssimp.a(zutil.c.o):(.bss+0x0): multiple definitions for "z_verbose"
../../../lib/libUrho3D.a(ftgzip.c.o):(.bss+0x0): first definition here

I algo get a multiple definition error message for "z_error".

However, if I build the release version, I do not get such errors and the build process successfully ends (the _AssetImporter_ is built).

Any idea on what is going on ? Or maybe is it a known error ?

I also compiled the git version (after a _git clone_ done today) and the same error occurs if I compile in debug mode.

Charles

-------------------------

cadaver | 2017-08-19 16:35:27 UTC | #2

There's zlib embedded in both assimp and freetype, and the z_verbose symbol would appear to clash. Didn't get this on a MinGW debug build though. For now the workaround would be, if you get hit by that issue, is to only compile AssetImporter in release mode. You can also configure the Urho build to skip tool building with CMake option -DURHO3D_TOOLS=0

-------------------------

cadaver | 2017-08-19 19:47:24 UTC | #3

This issue should be fixed in the master branch now.

-------------------------

weitjong | 2017-08-20 00:59:29 UTC | #4

This is really strange. I have no issue with this z_error thingy since the last time we quick fixed it in 2013. I use Fedora also but usually I use SHARED lib type. When I have time will try to reproduce it using 1.7 tag.

EDIT: it is reproduced. Both assimp and freetype are upgraded earlier this year. Unfortunately we only spotted this now. Only happens in STATIC DEBUG build config.

-------------------------

zedraken | 2017-08-20 03:36:31 UTC | #5

I checked for the latest modifications on the master branch and the _AssetImporter_ is successfully linked in debug mode.
Thanks !

-------------------------

