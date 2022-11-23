8Observer8 | 2021-02-18 14:02:18 UTC | #1

If [STATIC does not want to work for me](https://discourse.urho3d.io/t/how-to-set-up-urho3d-static-mingw-in-qt-creator-ide/6714) then I will try to build to SHARED. I found this option in CMake: ![image|330x15](upload://cQ3aZ1P7OFtC21g3DMVchcs1UKD.png) 

Now my config file looks like this now:

![image|319x323](upload://iOD4pwzeA1mnaBlH6fhog3KSPnf.png) 

![image|309x272](upload://7CSNw4lOC2H2I2I1la0Qn79nkR9.png) 


![image|527x302](upload://6fNKDBjhkPIr6GE3I3C6N6OavpL.png) 

![image|301x303](upload://jDplSsQMOuf5NcNX0RtVnuytCqh.png) 

![image|553x303](upload://4Wpeife8MQ8HoehZo3XLKR9o6HA.png) 

![image|514x200](upload://xJz1TjCX3MGTDqibhrs9Ckr6uNO.png) 

But I got these errors:

```
[ 87%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/TileMap2D.cpp.obj
[ 88%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/TileMapDefs2D.cpp.obj
[ 88%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/TileMapLayer2D.cpp.obj
[ 88%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/TmxFile2D.cpp.obj
[ 88%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/Urho2D.cpp.obj
[ 88%] Linking CXX shared library ..\..\bin\Urho3D.dll
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xcf9): undefined reference to `_imp__send@16'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x159b): undefined reference to `_imp__setsockopt@20'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x1a00): undefined reference to `_imp__getnameinfo@28'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x1dcb): undefined reference to `_imp__closesocket@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x22af): undefined reference to `_imp__select@20'../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x22ca): undefined reference to `__WSAFDIsSet@8'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x2335): undefined reference to `_imp__select@20'../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x2aed): undefined reference to `_imp__recv@16'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x403f): undefined reference to `_imp__setsockopt@20'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x4061): undefined reference to `_imp__shutdown@8'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x408b): undefined reference to `_imp__ioctlsocket@12'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x40be): undefined reference to `_imp__closesocket@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x45c3): undefined reference to `_imp__accept@12'../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x45dc): undefined reference to `_imp__ntohl@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x4638): undefined reference to `_imp__closesocket@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x4800): undefined reference to `_imp__getsockname@12'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x4838): undefined reference to `_imp__setsockopt@20'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x87b6): undefined reference to `_imp__ntohl@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0x8ac8): undefined reference to `_imp__ntohs@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xa3dd): undefined reference to `_imp__ntohs@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xa407): undefined reference to `_imp__ntohl@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xb1ac): undefined reference to `_imp__getaddrinfo@16'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xb20f): undefined reference to `_imp__freeaddrinfo@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xb22e): undefined reference to `_imp__htons@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xb253): undefined reference to `_imp__socket@12'../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xb2a0): undefined reference to `_imp__connect@12'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xb340): undefined reference to `_imp__getsockname@12'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xb449): undefined reference to `_imp__freeaddrinfo@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xb4b2): undefined reference to `_imp__closesocket@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xb51a): undefined reference to `_imp__closesocket@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xb578): undefined reference to `_imp__closesocket@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xb77c): undefined reference to `_imp__WSACleanup@0'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xb7bc): undefined reference to `_imp__WSAStartup@8'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xbf22): undefined reference to `_imp__socket@12'../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xbf5e): undefined reference to `_imp__setsockopt@20'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xbfa3): undefined reference to `_imp__bind@12'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xbfc6): undefined reference to `_imp__listen@8'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xbff1): undefined reference to `_imp__getsockname@12'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xc10c): undefined reference to `_imp__ntohs@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xc16d): undefined reference to `_imp__htonl@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xc185): undefined reference to `_imp__htons@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xc4c8): undefined reference to `_imp__closesocket@4'
../ThirdParty/Civetweb/libCivetweb.a(civetweb.c.obj):civetweb.c:(.text+0xc79d): undefined reference to `_imp__closesocket@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x1c2): undefined reference to `_imp__WSAGetLastError@0'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x1e5): undefined reference to `_imp__gethostname@8'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x1f6): undefined reference to `_imp__gethostbyname@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x279): undefined reference to `_imp__getaddrinfo@16'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x2a7): undefined reference to `_imp__freeaddrinfo@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x2de): undefined reference to `_imp__WSAStartup@8'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x304): undefined reference to `_imp__gethostname@8'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x5f6): undefined reference to `_imp__getaddrinfo@16'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x621): undefined reference to `_imp__socket@12'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x66d): undefined reference to `_imp__bind@12'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x688): undefined reference to `_imp__freeaddrinfo@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x6b0): undefined reference to `_imp__ntohs@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x7c1): undefined reference to `_imp__setsockopt@20'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x7dd): undefined reference to `_imp__listen@8'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x801): undefined reference to `_imp__ntohs@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x835): undefined reference to `_imp__closesocket@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x847): undefined reference to `_imp__freeaddrinfo@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x867): undefined reference to `_imp__closesocket@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0xe7a): undefined reference to `_imp__WSAGetLastError@0'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x10a5): undefined reference to `_imp__WSACleanup@0'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x1fe4): undefined reference to `_imp__getaddrinfo@16'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x2027): undefined reference to `_imp__WSASocketA@24'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x2072): undefined reference to `_imp__WSAConnect@28'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x208d): undefined reference to `_imp__freeaddrinfo@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x20ca): undefined reference to `_imp__getsockname@12'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x210f): undefined reference to `_imp__getpeername@12'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x229a): undefined reference to `_imp__closesocket@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x22ac): undefined reference to `_imp__freeaddrinfo@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x2307): undefined reference to `_imp__ntohs@4'
../ThirdParty/kNet/libkNet.a(Network.cpp.obj):Network.cpp:(.text+0x2346): undefined reference to `_imp__ntohs@4'
../ThirdParty/kNet/libkNet.a(NetworkServer.cpp.obj):NetworkServer.cpp:(.text+0xd6a): undefined reference to `_imp__ntohs@4'
../ThirdParty/kNet/libkNet.a(NetworkServer.cpp.obj):NetworkServer.cpp:(.text+0xed6): undefined reference to `_imp__accept@12'
../ThirdParty/kNet/libkNet.a(NetworkServer.cpp.obj):NetworkServer.cpp:(.text+0xf05): undefined reference to `_imp__ntohs@4'
../ThirdParty/kNet/libkNet.a(NetworkServer.cpp.obj):NetworkServer.cpp:(.text+0xfe7): undefined reference to `_imp__getsockname@12'
../ThirdParty/kNet/libkNet.a(NetworkServer.cpp.obj):NetworkServer.cpp:(.text+0x1134): undefined reference to `_imp__closesocket@4'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x42c): undefined reference to `_imp__WSACreateEvent@0'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x483): undefined reference to `_imp__WSACloseEvent@4'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x4db): undefined reference to `_imp__setsockopt@20'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x51b): undefined reference to `_imp__setsockopt@20'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x56b): undefined reference to `_imp__getsockopt@20'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x5cb): undefined reference to `_imp__getsockopt@20'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x79e): undefined reference to `_imp__shutdown@8'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x8a9): undefined reference to `_imp__shutdown@8'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x8b8): undefined reference to `_imp__closesocket@4'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x9bb): undefined reference to `_imp__WSAResetEvent@4'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0xa06): undefined reference to `_imp__WSARecv@28'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0xafb): undefined reference to `_imp__WSARecvFrom@36'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0xc8c): undefined reference to `_imp__recv@16'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0xd1e): undefined reference to `_imp__recvfrom@24'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0xd42): undefined reference to `_imp__ntohs@4'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0xe28): undefined reference to `_imp__WSAGetOverlappedResult@20'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0xfce): undefined reference to `_imp__ioctlsocket@12'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x104f): undefined reference to `_imp__select@20'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x10c7): undefined reference to `_imp__send@16'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x113f): undefined reference to `_imp__sendto@24'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x122a): undefined reference to `_imp__WSAGetOverlappedResult@20'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x12fb): undefined reference to `_imp__WSAGetOverlappedResult@20'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x1402): undefined reference to `_imp__WSAResetEvent@4'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x144a): undefined reference to `_imp__WSASend@28'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x14c3): undefined reference to `_imp__WSASendTo@36'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x1549): undefined reference to `_imp__WSASetEvent@4'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x15dc): undefined reference to `_imp__setsockopt@20'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x1e96): undefined reference to `_imp__setsockopt@20'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x1f20): undefined reference to `_imp__htons@4'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x1fbb): undefined reference to `_imp__getpeername@12'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x1fdf): undefined reference to `_imp__ntohs@4'
../ThirdParty/kNet/libkNet.a(Socket.cpp.obj):Socket.cpp:(.text+0x202e): undefined reference to `_imp__getsockname@12'
../ThirdParty/kNet/libkNet.a(W32Event.cpp.obj):W32Event.cpp:(.text+0x25): undefined reference to `_imp__WSACreateEvent@0'
../ThirdParty/kNet/libkNet.a(W32Event.cpp.obj):W32Event.cpp:(.text+0x4e): undefined reference to `_imp__WSACreateEvent@0'
../ThirdParty/kNet/libkNet.a(W32Event.cpp.obj):W32Event.cpp:(.text+0x6e): undefined reference to `_imp__WSACloseEvent@4'../ThirdParty/kNet/libkNet.a(W32Event.cpp.obj):W32Event.cpp:(.text+0xaf): undefined reference to `_imp__WSAResetEvent@4'../ThirdParty/kNet/libkNet.a(W32Event.cpp.obj):W32Event.cpp:(.text+0xdf): undefined reference to `_imp__WSASetEvent@4'
../ThirdParty/kNet/libkNet.a(W32Event.cpp.obj):W32Event.cpp:(.text+0x132): undefined reference to `_imp__WSAWaitForMultipleEvents@20'
../ThirdParty/kNet/libkNet.a(W32Event.cpp.obj):W32Event.cpp:(.text+0x182): undefined reference to `_imp__WSAWaitForMultipleEvents@20'
../ThirdParty/kNet/libkNet.a(W32Event.cpp.obj):W32Event.cpp:(.text+0x1d2): undefined reference to `_imp__WSAWaitForMultipleEvents@20'
../ThirdParty/kNet/libkNet.a(W32EventArray.cpp.obj):W32EventArray.cpp:(.text+0x88): undefined reference to `_imp__WSAWaitForMultipleEvents@20'
collect2.exe: error: ld returned 1 exit status
mingw32-make[2]: *** [Source\Urho3D\CMakeFiles\Urho3D.dir\build.make:4009: bin/Urho3D.dll] Error 1
mingw32-make[1]: *** [CMakeFiles\Makefile2:1322: Source/Urho3D/CMakeFiles/Urho3D.dir/all] Error 2
mingw32-make: *** [Makefile:170: all] Error 2
```

-------------------------

Eugene | 2021-02-17 14:11:10 UTC | #2

The best advice I can come up with is to delete MinGW and never use it because [it is officially retarded compiler that fails to build well-formed code](https://github.com/electronicarts/EASTL/pull/413).

It's not your first MinGW issue, it's not your last, and if you keep using MinGW, you will have to deal with them mostly on your own. MinGW has its own good sides (being compact, for example), but it doesn't justify amount of issues it creates for any _real_ project with multiple dependecies and compilcated code.

-------------------------

SirNate0 | 2021-02-17 15:21:14 UTC | #3

Ensure that it is trying to link the winsock2 library. To do that you can try `make VERBOSE=1` as the command instead of just `make`. See here for a similar error: 
https://stackoverflow.com/questions/2033608/mingw-linker-error-winsock

-------------------------

S.L.C | 2021-02-17 15:35:45 UTC | #4

somehow, somewhere, someone is not linking to `wsock32 ws2_32` or something like that.

@Eugene while I understand your frustration. You have to understand that if you criticize MinGW you criticize GCC and MSVC together. Because MinGW is torn somewhere between them. GCC being string makes MinGW retain some of that and MSVC being retarded and compiling just about anything that looks like a series of characters makes MinGW loose some of that strictness in order to maintain compatibility. If you've written some (non-platform-related) c++ on MSVC and then try to compile it on GCC you'd understand what I mean.

At this point, I'm pretty positive his whole environment is a bit messed up. I'm deducing that from previous posts. God knows what MinGW distribution he's using and god knows what procedure he's using. A bunch of pictures don't prove anything.

And at this point I blame some of the issues on Urho as well. A cluster fk of third-party dependencies, each using their own style, versions and approach of dealing CMake's build-system. Each adding their own libraries and and compiler flags and god knows what.

And I'm not even sure why `ws2_32` is not linked against by either SLikeNet or Civetweb.

This is more than just a MinGW issue. Let's not try to blame it on that.

EDIT:

And if you're about to reply "*oh, but msvc doesn't compile bad code*". Try to compile this on MSVC and then GCC/MinGW, and see who succeeds:
```cpp
#include <memory>

template < class T, class A = std::allocator< T > > struct Test {
    bool mB{};
    bool Foo();
};

template < class T, class A = std::allocator< T > >
inline bool Test< T, A >::Foo() { return mB; }
```
And then see what's wrong with it.

That was just one example. I can definitely come up with more.

-------------------------

SirNate0 | 2021-02-17 16:03:28 UTC | #5

I suspect your build tree is messed up. In UrhoCommon.cmake there is the following to link that library. I would suggest starting over from a clean build tree and hoping that fixes the issue.
```
macro (define_dependency_libs TARGET)

...

    # ThirdParty/Civetweb external dependency
    if (${TARGET} MATCHES Civetweb|Urho3D)
        if (WIN32)
            list (APPEND LIBS ws2_32)
        endif ()
    endif ()
```

-------------------------

Eugene | 2021-02-17 17:00:06 UTC | #6

[quote="S.L.C, post:4, topic:6718"]
You have to understand that if you criticize MinGW you criticize GCC and MSVC together
[/quote]
How exactly this derivation is made? I criticize MinGW because it is MinGW who cannot pass _argument_ to _function_ without messing up. Sure, fresh MSVC releases have bugs too. But MinGW has more bugs (or just inconsitencies and weird behaviors), perhaps by the order of magnitude, or two.

I may be overly expressive here, but I'm just tired. Tired of _countless_ MinGW fuckups. 9 of 10 times I see weird build error in CI, it's MinGW.

It means something that [3rd parties](https://github.com/embree/embree) say "we support MSVC, GCC and Clang. MinGW? Nah, we don't support *that*"

-------------------------

S.L.C | 2021-02-17 17:08:58 UTC | #7

[quote="Eugene, post:6, topic:6718"]
...Tired of *countless* MinGW fuckups. 9 of 10 times I see weird build error in CI, it’s MinGW.
[/quote]

[quote="Eugene, post:6, topic:6718"]
...“we support MSVC, GCC and Clang. MinGW? Nah, we don’t support *that* ”
[/quote]

You just explained your frustration and took the blame away from MinGW at the same time.

I'm just done here. This is pointless.

-------------------------

1vanK | 2021-02-17 17:30:19 UTC | #8

[quote="Eugene, post:6, topic:6718"]
Tired of *countless* MinGW fuckups. 9 of 10 times I see weird build error in CI, it’s MinGW.
[/quote]

This is because a small percentage of people use MinGW as the main compiler on their machine. I don't use MinGW because it compiles incredibly slowly, but it is needed as an alternative to proprietary VS

-------------------------

Eugene | 2021-02-17 17:37:19 UTC | #9

[quote="S.L.C, post:7, topic:6718"]
You just explained your frustration and took the blame away from MinGW at the same time.
[/quote]
Okay, I can elaborate. 3rd parties often don’t bother supporting MinGW properly because of unacceptable rate of *compiler* defects (I have encountered *three* only this year).

So yeah, this is kind of vicious cycle. MinGW is bad compiler, therefore it has little users and is not properly supported, and therefore it keeps being bad compiler. Which is sad, but it doesn’t excuse MinGW.

Sorry for off topic, this was the last message in my whining

-------------------------

WangKai | 2021-02-18 07:34:44 UTC | #10

~~I wonder which version of Urho are you using?~~ I would recommand to try the `master` branch from github.

-------------------------

8Observer8 | 2021-02-18 10:39:06 UTC | #11

[quote="WangKai, post:10, topic:6718"]
I wonder which version of Urho are you using?
[/quote]
Sorry that I did not write it
- Urho3D 1.7.1
- MinGW 8.1.0

[quote="WangKai, post:10, topic:6718"]
I would recommand to try the `master` branch from github.
[/quote]
I tried to build to the STATIC version with settings from my first post. I have only one error in the `RakNetSocket2.cpp`: ![image|296x17](upload://ipeiaC6K7ABzlLQ4TFXk72jaS27.png) 

My .pro file:

```
CONFIG += c++11

INCLUDEPATH += "C:\Users\8Observer8\Downloads\Urho3D-master\dist\include\Urho3D\ThirdParty"

INCLUDEPATH += "C:\Users\8Observer8\Downloads\Urho3D-master\dist\include"
LIBS += -L"C:\Users\8Observer8\Downloads\Urho3D-master\dist\lib"
LIBS += -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -lSetupapi -ladvapi32 -lwinmm -limm32 -lversion -lws2_32 -ldbghelp -lopengl32

SOURCES += \
    main.cpp
```

-------------------------

8Observer8 | 2021-02-18 10:59:38 UTC | #12

[quote="8Observer8, post:11, topic:6718"]
I tried to build to the STATIC version with settings from my first post. I have only one error in the `RakNetSocket2.cpp` : ![image|296x17](upload://ipeiaC6K7ABzlLQ4TFXk72jaS27)
[/quote]
I tried to google this error and I find the solution here: https://stackoverflow.com/questions/10972794/undefined-reference-to-getadaptersaddresses20-but-i-included-liphlpapi

I just added this key: `-liphlpapi`

```
CONFIG += c++11

INCLUDEPATH += "C:\Users\8Observer8\Downloads\Urho3D-master\dist\include\Urho3D\ThirdParty"

INCLUDEPATH += "C:\Users\8Observer8\Downloads\Urho3D-master\dist\include"
LIBS += -L"C:\Users\8Observer8\Downloads\Urho3D-master\dist\lib"
LIBS += -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -lSetupapi -ladvapi32 -lwinmm -limm32 -lversion -lws2_32 -ldbghelp -lopengl32 -liphlpapi

SOURCES += \
    main.cpp
```

@WangKai thank you that recommend to use the `mater` branch. It is a solution for STATIC build. Maybe I will try to build the SHARED version later.

-------------------------

8Observer8 | 2021-02-18 12:29:56 UTC | #13

I tried to build the SHARED version from the `master` branch. It was build good. Samples was built and they works. But my example was crashed without any messages:

![image|690x90](upload://hygqLhIrBatcbty7LbiaAHNXtb7.png) 

The STATIC version from the `master` branch and the pre-built SHARED 1.7.1 versions work and they enough for me.

-------------------------

SirNate0 | 2021-02-18 13:09:55 UTC | #14

Run it with the debugger so it can see where it crashes. My tentative guess is that it can't find a dll that it needs.

-------------------------

8Observer8 | 2021-02-18 14:01:45 UTC | #15

Yes, you are right. I copied `Urho3D.dll` to the `debug` folder. It works. Thanks!

-------------------------

8Observer8 | 2021-02-19 11:21:32 UTC | #16

Why the pre-build `Urho 1.7.1 SHARED` version works without copying `Urho3D.dll` to exe directory?

Is it a bad practice to copy the `Urho3D.dll` library to the `C:\Windows\System` directory? Because sometime I delete all the Debug/Release directories using this command: `for /d /r . %d in (Debug Release) do @if exist "%d" echo "%d" && rd /s/q "%d"` When I make a lot of examples I must copy `Urho3D.dll` every time. `Urho3D.dll` requires 18 MB and it is big for my laptop.

-------------------------

S.L.C | 2021-02-19 12:46:06 UTC | #17

[quote="8Observer8, post:16, topic:6718"]
Is it a bad practice to copy the `Urho3D.dll` library to the `C:\Windows\System` directory?
[/quote]

Yes. Very bad practice.

You can place the DLL in a common folder then [modify](https://docs.alfresco.com/4.2/tasks/fot-addpath.html) the system `Path` environment variable to include that common path. 

The executable should be able to find the required dependencies based on the search paths.

When that's a bit intrusive (*and it is*) most of the times people just create a command line file that adjusts the working directory or search paths only for the duration of the launch of a program. Not affecting other applications on the same machine.

-------------------------

