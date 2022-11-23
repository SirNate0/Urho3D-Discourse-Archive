Cpl.Bator | 2020-09-20 00:15:30 UTC | #1

hi, when i generate the urho lib with visual studio 2017 , and when i install it into "program files"  GLEW and IK are not copied into thirdparty include. And when i copy manualy glew and ik , the error in my project is :

> fatal error C1083: Cannot open file include : 'ik/config.h' : No such file or directory

config.h is not generated.

-------------------------

weitjong | 2020-09-20 01:16:39 UTC | #2

How did you do the “install”? If it is via the “install” built-in target then it should work out of the box.

-------------------------

Cpl.Bator | 2020-09-20 10:27:55 UTC | #3

yes , via the install target inside visual studio inspector ( generate from vs ), and yes, i have the admin right , and i dont change the install path.

-------------------------

weitjong | 2020-09-20 11:26:51 UTC | #4

I see. But does it cause any problem in the first place before you manually trying to “add” things into the installed location. We intentionally do not expose all the 3rd-party libs to the library users. Those not are considered as internal/private implementation detail. It means you can only interact with them via Urho3D public API.

-------------------------

Cpl.Bator | 2020-09-20 13:51:48 UTC | #5

yes, it cause a problem , if i dont move it  , i have this error :

> urho3d\include\urho3d\graphics\opengl\oglgraphicsimpl.h(39): fatal error C1083: Cannot open file include : 'GLEW/glew.h' : No such file or directory

-------------------------

weitjong | 2020-09-20 15:16:46 UTC | #6

I just looked at the code and it seems you are right that "glew.h" should be exposed to the library user for the platforms that need it. It is an easy fix.

EDIT: it is fixed in master branch now.

-------------------------

Cpl.Bator | 2020-09-20 15:17:22 UTC | #7

Thank you sir. happy to help you.

-------------------------

