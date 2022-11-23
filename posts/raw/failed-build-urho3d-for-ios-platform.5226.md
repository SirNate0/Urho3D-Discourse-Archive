att | 2019-06-11 04:51:14 UTC | #1

I download the latest Urho3D engine code, and build it for iOS, but the SDL and SLikeNet can not build. 
I build it on Xcode 10.2.1

blowing is the log,

> Blockquote
In file included from /Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/src/SDL_hints.c:23:
In file included from /Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/include/SDL_hints.h:42:
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:454:49: error: unknown type name 'wchar_t'
extern DECLSPEC size_t SDLCALL SDL_wcslen(const wchar_t *wstr);
                                                ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:455:66: error: unknown type name 'wchar_t'
extern DECLSPEC size_t SDLCALL SDL_wcslcpy(SDL_OUT_Z_CAP(maxlen) wchar_t *dst, const wchar_t *src, size_t maxlen);
                                                                 ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:455:86: error: unknown type name 'wchar_t'
extern DECLSPEC size_t SDLCALL SDL_wcslcpy(SDL_OUT_Z_CAP(maxlen) wchar_t *dst, const wchar_t *src, size_t maxlen);
                                                                                     ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:456:68: error: unknown type name 'wchar_t'
extern DECLSPEC size_t SDLCALL SDL_wcslcat(SDL_INOUT_Z_CAP(maxlen) wchar_t *dst, const wchar_t *src, size_t maxlen);
                                                                   ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:456:88: error: unknown type name 'wchar_t'
extern DECLSPEC size_t SDLCALL SDL_wcslcat(SDL_INOUT_Z_CAP(maxlen) wchar_t *dst, const wchar_t *src, size_t maxlen);
                                                                                       ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:457:46: error: unknown type name 'wchar_t'
extern DECLSPEC int SDLCALL SDL_wcscmp(const wchar_t *str1, const wchar_t *str2);
                                             ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:457:67: error: unknown type name 'wchar_t'
extern DECLSPEC int SDLCALL SDL_wcscmp(const wchar_t *str1, const wchar_t *str2);
                                                                  ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:493:76: error: unknown type name 'va_list'
extern DECLSPEC int SDLCALL SDL_vsscanf(const char *text, const char *fmt, va_list ap);
                                                                           ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:495:109: error: unknown type name 'va_list'
extern DECLSPEC int SDLCALL SDL_vsnprintf(SDL_OUT_Z_CAP(maxlen) char *text, size_t maxlen, const char *fmt, va_list ap);
                                                                                                            ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/src/SDL_hints.c:76:59: error: use of undeclared identifier 'NULL'
                hint->value = value ? SDL_strdup(value) : NULL;
                                                          ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/src/SDL_hints.c:89:47: error: use of undeclared identifier 'NULL'
    hint->value = value ? SDL_strdup(value) : NULL;
                                              ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/src/SDL_hints.c:91:23: error: use of undeclared identifier 'NULL'
    hint->callbacks = NULL;
                      ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/src/SDL_hints.c:174:23: error: use of undeclared identifier 'NULL'
        hint->value = NULL;
                      ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/src/SDL_hints.c:176:27: error: use of undeclared identifier 'NULL'
        hint->callbacks = NULL;
                          ^
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SDL/src/SDL_hints.c:198:20: error: use of undeclared identifier 'NULL'
            prev = NULL;
                   ^
15 errors generated.

In file included from /Users/att/Work/SDK/Urho3D/Source/ThirdParty/SLikeNet/Source/src/SuperFastHash.cpp:23:
/Users/att/Work/SDK/Urho3D/Source/ThirdParty/SLikeNet/Source/include/slikenet/linux_adapter.h:17:10: fatal error: 'winsock2.h' file not found
#include "winsock2.h"
         ^~~~~~~~~~~~
1 error generated.

> Blockquote

-------------------------

att | 2019-06-11 05:32:29 UTC | #2

Found the problem, need latest cmake.

-------------------------

weitjong | 2019-06-11 05:40:12 UTC | #3

Sorry to hear that. We are still testing our CI build using Xcode 9.4 and it seems to be fine with that version. I will probably bump Travis CI to use Xcode 10.2 later of the week to see if I can reproduce the issue.

-------------------------

weitjong | 2019-06-11 05:53:28 UTC | #4

Ok. Still I think it is time we bump the version.

-------------------------

