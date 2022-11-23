CE184 | 2021-01-16 18:40:41 UTC | #1

MacOS, just ```git pull``` the newest Urho3D repo.
```
/Users/xxx/Documents/Urho3D_Projects/Urho3D/Source/ThirdParty/Assimp/contrib/zlib/gzlib.c:252:9: error: implicit declaration of function 'lseek' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
        LSEEK(state->fd, 0, SEEK_END);  /* so gzoffset() is correct */
        ^
/Users/xxx/Documents/Urho3D_Projects/Urho3D/Source/ThirdParty/Assimp/contrib/zlib/gzlib.c:14:17: note: expanded from macro 'LSEEK'
#  define LSEEK lseek
                ^
/Users/xxx/Documents/Urho3D_Projects/Urho3D/Source/ThirdParty/Assimp/contrib/zlib/gzlib.c:252:9: note: did you mean 'fseek'?
/Users/xxx/Documents/Urho3D_Projects/Urho3D/Source/ThirdParty/Assimp/contrib/zlib/gzlib.c:14:17: note: expanded from macro 'LSEEK'
#  define LSEEK lseek
                ^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdio.h:162:6: note: 'fseek' declared here
int      fseek(FILE *, long, int);
         ^
```

-------------------------

CE184 | 2021-01-16 20:02:10 UTC | #2

[This post (2014)](https://github.com/aerys/minko/issues/167#issuecomment-49554755) solved my problem.

add ```#include "unistd.h"``` to ```Assimp/contrib/zlib/gzguts.h```.

Not sure if it's the right way to do it, or is it just Assimp's problem. I didn't have this issue before.

-------------------------

