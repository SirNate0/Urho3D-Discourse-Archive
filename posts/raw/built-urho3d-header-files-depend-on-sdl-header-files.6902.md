mohamed.chit | 2021-06-24 18:42:41 UTC | #1

Hi
I have used the script "dockerized" to use docker to build "Urho3D" for "android", I could have it as "aar", so far so good.
Now I would like to use statically built Urho3D libraries, the problem is, when I have in some C++ code, "#include" to some Urho3D file, the Urho3D header file does include "SDL/*" files.

I supposed that should not happen, SDL header files should not be visible (third party source code).

I copied the "include" folder of SDL from "Urho3D-master/Source/ThirdParty/SDL/include" and made it visible to Urho3D static library, yeas indeed, now Urho3D does see SDL but I got another problem.

now it complains about a missing SDL header file, which is "SDL_config.h"

I check Urho3D file tree, I found  "SDL_config.h.cmake", I dig into this file I find a very clear sentence in it, it says:
"// Modified by Yao Wei Tjong for Urho3D"

So the source code of the third party has been modified !

So how to get the generated version of this "SDL_config.h" for android?

if we depend on additional header files, why are not they included when dockerized.sh generated the static libraries and header files.

It would be great to have some feedback about this, how to fix this.

Best regards

-------------------------

SirNate0 | 2021-06-24 19:24:09 UTC | #2

I suspect that if you use the Build trees include folder it will have the generated SDL_config.h.
I.e. rather than
 `Urho3D-master/Source/ThirdParty/SDL/include` 
use
 `Urho3D-master/<BuildFolder>/include/Urho3D/ThirdParty/SDL`

Also, did you set up your project to use the library following the directions on https://urho3d.io/documentation/HEAD/_using_library.html, or are you trying to work it out on your own? It's been a while since I did an Android build, but assuming it's similar to the desktop one it should set up the include directories and such as expected if you use the CMake setup as directed. Even if you want to use your own, I would still recommend using the CMake build on a project for a desktop build, and then you can just copy the include paths you should be passing to the compiler from that.

-------------------------

mohamed.chit | 2021-06-24 19:41:07 UTC | #3

thanks for the reply.

as I mentioned, I have use "dockerized.sh" script, when it builds, we get the followins folders:


```
android
    - launcher-app
        - build
            - outputs
                - apk
                - logs
        - src
    - urho3d-lib
        - build
            - outputs
                - logs
                - aar
                    - urho3d-lib-debug.aar
                    - urho3d-lib-release.aar
        - src
```

I did not write the entire tree, but there are no any C++ header files anywhere.

inside the .aar, you find "include" folder for "Urho3D" header files, but no any header file for SDL.

The library was built, so I should be able to use it? should I build it from scratch using CMake? why we have dockerized.sh in this case?

I will keep trying thanks

-------------------------

SirNate0 | 2021-06-24 19:44:12 UTC | #4

I've never used the dockerized build, so someone else will have to help you with that. I thought it would be more similar, but the results look a fair bit different from what I get using CMake directly. But it may just be the directory structure, I don't know.

Sorry I can't help more.

-------------------------

weitjong | 2021-06-25 16:44:22 UTC | #5

There is more than one way to setup your project to use Urho3D library. The old way in the online documentation mentioned by SirNate0 does not work for Android build out of the box. For the android build, it is recommended to follow the new scaffolding instruction in the new website. However, the new doc is still work in progress.

Whether you use "dockerized build environment" or not, it is irrelevant. What relevant is how your project is structured. And, I would say you have got it all wrong or otherwise you would not have the header problem in your build.

About the marker `Modified by xxxx for Urho3D`, that's just Urho3D way to indicate the file has been changed locally in our subtree and we are forced to modify the upstream files in order to make them work with Urho3D, especially for SDL case is to make it build for all the platforms we support. You can try to build upstream SDL directly for Android or other platforms and you will understand how much work we have done for you. Don't just take it for granted or even complain without first doing your own homework!

-------------------------

mohamed.chit | 2021-06-25 18:49:03 UTC | #6


Thank you for the reply, If I had it all wrong, and I would not have the header problem in my build, could you please explain 
the following header files:



```
> Source/Urho3D/IO/NamedPipe.h            line:30                 #include <SDL/SDL_rwops.h>
> Source/Urho3D/IO/RWOpsWrapper.h         line:27                 #include <SDL/SDL_rwops.h>
> Source/Urho3D/Input/InputConstants.h    line:30                 #include <SDL/SDL_joystick.h>
> Source/Urho3D/Input/InputConstants.h    line:31                 #include <SDL/SDL_gamecontroller.h>
> Source/Urho3D/Input/InputConstants.h    line:32                 #include <SDL/SDL_keycode.h>
> Source/Urho3D/Input/InputConstants.h    line:33                 #include <SDL/SDL_mouse.h>
```

These are Urho3D header files, that we will include in projects, they explicitly publicly include "SDL" header files, in other words, if you would like to use Urho3D library, you MUST include the SDL header files with it.

And yet, the Urho3D team did modify SDL itself, and you get a problem with "SDL_config.h".


I am of course very thankful to Urho3D team, but I am just pointing to some things I have encountered during my usage of Urho3D.

Regards

-------------------------

weitjong | 2021-06-26 02:36:53 UTC | #7

What I meant was if you have “header search path” problem then your project is not correctly setup. The structure that you given in the earliest post already seems wrong to me. Most probably the content of the build scripts in your project also not entirely correct and lead to such header problem.

Rest assure that we have provided the Urho3D headers together with the necessary headers from the “exposed” sub-libraries. And, that includes headers from SDL. We purposely hide the other underlying sub-libraries as internal implementation detail. 

For Android platform, all the headers are packed inside the Urho3D AAR. So, the key is to use the right Gradle build script that could unpack those bits. We have provided Gradle build script that can perform such task automatically. Use it. It is in master branch only.

The new way for scaffolding a UrhoApp project is much better. It is truly cross-platform out of the box. Tested to work well on Android build too. I won’t give the link here first because the page is still under construction.

-------------------------

mohamed.chit | 2021-06-26 11:32:26 UTC | #8

Thank you again for the reply, the tree I showed above is tree structure inside "aar" file generated when using "dockerized.sh" script, it has nothing to do with the project structure that i am using.

For Android, Urho3D AAR generated from "dockerized.sh", does not contain "SDL" header files, and that is the problem I had, that was my original question, what to do? I copied "SDL" header files, it complained about "SDL_config.h".

Do you mean after generating AAR with "dockerized.sh", we must use some specific gradle file to include additional header files?

To be honest, I have solved this problem myself manually, by copying "SDL" header files, and un-comment in c++ code each line for "#include <SDL/SDL_config.h>", since I do not have "SDL_config.h" for android and I do not know how to generate it.
I could compile and it works.

looking forward for the page you have mentioned.

best regards

-------------------------

weitjong | 2021-06-26 14:00:18 UTC | #9

Are you using master branch? All our commit are being CI tested. The last few CI builds were successful. So, it could only mean the AAR is built correctly with the lib and header packed inside.

-------------------------

