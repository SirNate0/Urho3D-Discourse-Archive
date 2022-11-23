practicing01 | 2017-01-02 01:09:35 UTC | #1

Hello, native compiles but I'm getting the following for android:

[code]
[  5%] Built target FreeType
[  6%] Built target JO
[  6%] Built target LZ4
[  6%] Built target PugiXml
[  6%] Built target rapidjson
[ 19%] Built target SDL
[ 19%] Built target StanHull
[ 19%] Built target STB
[ 24%] Built target AngelScript
[ 24%] Performing build step for 'buildvm'
Linking C executable minilua
/usr/bin/ld: cannot open output file minilua: Is a directory
collect2: error: ld returned 1 exit status
make[5]: *** [minilua] Error 1
make[4]: *** [CMakeFiles/minilua.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [Source/ThirdParty/LuaJIT/buildvm-prefix/src/buildvm-stamp/buildvm-build] Error 2
make[1]: *** [Source/ThirdParty/LuaJIT/CMakeFiles/buildvm.dir/all] Error 2
make: *** [all] Error 2

[/code]

-------------------------

weitjong | 2017-01-02 01:09:35 UTC | #2

Regenerate your build tree from scratch. There was a change on how minilua target being configured recently.

-------------------------

