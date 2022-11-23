spenland | 2019-12-12 17:37:58 UTC | #1

Since stb_perlin.h doesn't seem to be included in the third party list (it's listed but the file isn't there and the GitHub link is dead), I found the file on stb's GitHub and just copied it into my project folder.

I have this at the top of my class:

    #define STB_PERLIN_IMPLEMENTATION
    #include "stb_perlin.h"

I get access to the function I need "stb_perlin_noise3_seed" with autofill so it's seeing the function. But when I try to build I get this:

![errors|690x166](upload://nNxC4umHeAFaINJkynFK1LZshYu.png) 

Can anyone help? Is this stb_perlin.h file already included in Urho or something? If so how can I access it? I would think it would be #include <STB/stb_perlin.h>     but like I said, that file is not there.

Thanks for your help!

-------------------------

SirNate0 | 2019-12-12 18:51:50 UTC | #2

Did you put that in a header file? If so, you may have the implementation in multiple object files if you used that header in several cpp files. If that's the problem, just copy those two lines into a single .cpp file and leave only
```#include "stb_perlin.h"``` in the header.

Also, I'm not certain, but I think you would have needed 
```#include <Urho3D/ThirdParty/STB/stb_perlin.h>``` if Urho did include the perlin file, which it doesn't by default.

-------------------------

spenland | 2019-12-12 19:05:18 UTC | #3

Copying both to my cpp file and leaving the include in my header worked. I then removed the include in the header (since it's now in the cpp file) and that worked too.

I'm a little lost why I couldn't include it in my header file...but happy it works now :)

-------------------------

SirNate0 | 2019-12-12 19:32:18 UTC | #4

Glad you fixed it. As to why, including it in the header *with the define* told the library to include the implementation of the (not inline) functions at that point. Having that header then included in multiple cpp files resulted in multiple definitions/implementations of the same function. When compiled there where then multiple object files that contained the function, and then when the object files were linked into an executable the linker saw that there were multiple copies of _stb_perlin_noise3, for example, and since it can't tell which of them is the correct one it produces an error (you could, for instance, have multiple different functions with the same name but different effects. I'm guessing you can see why that would be problematic in linking the executable. This is a similar case, the functions just happen to be the same function)

-------------------------

