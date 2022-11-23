shipiz | 2017-09-20 19:29:21 UTC | #1

I have an issue with cmake generated XCode project. I have `Classes` folder which contains all source code organized into subfolders, the problem is that when i need to include a header i need to specify relative path i.e
```
Classes/
   MyApp.h
   scenes/
      MyScene.h
```
To include `MyScene.h` in `MyApp.h` i would have to use something like this `#include "scenes/MyScene.h"`. Now i know how to fix that in XCode alone, but regenerating project will remove my settings.

How would i need to modify `CMakeLists.txt` to properly add my `Classes` folder to user header search paths ?

-------------------------

weitjong | 2017-09-21 10:25:04 UTC | #2

Set below variable before calling `setup_main_executable()` macro. If you are not using our macro then you have to peek inside it to see how it is implemented. 

`
set (INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/Classes)
`

Adjust the path accordingly.

-------------------------

shipiz | 2017-09-21 10:29:03 UTC | #3

Thanks, tried it already,

This will add my source folder to Header Search Paths, but i'm still required to include my headers with relative path.
What i need to achieve is to populate User Header Search Paths with my source folder headers.

-------------------------

weitjong | 2017-09-21 10:39:33 UTC | #4

I am not sure what you try to achieve now. :slight_smile:

-------------------------

shipiz | 2017-09-21 10:49:37 UTC | #5

OK, basically

If header is located in `Source/scenes/MyScene.h` to include it it would look like this `#include "scenes/MyScene.h"` unless its in same folder.
What i want to achieve is to include it like this `#include "MyScene.h"` from anywhere.
Now to achieve this i have to add my headers to `User Header Search Paths` in XCode, which will basically flatten the structure.

Hope its clear now.

-------------------------

weitjong | 2017-09-21 11:29:06 UTC | #6

Kind of but I still don't get why you need it in the "User Search Path" to get it to work for your case. All our target are using the same approach I mentioned above and they have no issue with relative path. Also we do not control how CMake outputs our instruction in Xcode project file. If it uses "Header Search Path" then I don't think there is a way to tell it otherwise (vice versa). I could be wrong though.

-------------------------

