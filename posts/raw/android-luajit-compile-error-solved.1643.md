practicing01 | 2017-01-02 01:09:11 UTC | #1

I've pulled the latest and am trying to compile android with luajit so I can use bitwise functions.  Thanks for any help.

Error:
[spoiler][code]
[  1%] Built target JO
[  1%] Built target LZ4
[  6%] Built target FreeType
[  6%] Built target rapidjson
[  6%] Built target PugiXml
[  6%] Built target StanHull
[  6%] Built target STB
[ 11%] Built target AngelScript
[ 12%] Built target buildvm
[ 13%] Built target toluapp
[ 13%] Built target Civetweb
[ 26%] Built target SDL
[ 27%] Built target Detour
[ 28%] Built target DetourCrowd
[ 28%] Built target DetourTileCache
[ 30%] Built target Recast
[ 33%] Built target kNet
[ 39%] Built target Box2D
[ 40%] Built target tolua++
[ 40%] Building ASM object Source/ThirdParty/LuaJIT/CMakeFiles/LuaJIT.dir/generated/lj_vm.s.o
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s: Assembler messages:
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:7: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:14: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:25: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:36: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:47: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:58: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:72: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:87: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:97: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:107: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:117: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:127: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:137: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:147: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:157: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:167: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:176: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:185: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:193: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:201: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:211: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:223: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:233: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:243: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:253: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:263: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:273: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:283: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:293: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:303: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:313: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:321: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:331: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:341: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:351: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:361: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:370: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:381: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:395: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:404: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:413: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:421: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:429: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:437: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:446: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:455: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:468: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:481: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:490: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:498: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:509: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:521: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:537: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:552: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:559: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:566: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:582: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:596: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:609: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:626: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:649: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:663: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:679: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:688: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:697: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:704: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:720: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:731: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:748: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:767: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:779: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:786: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:801: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:813: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:826: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:838: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:850: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:858: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:869: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:880: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:888: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:897: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:906: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:914: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:922: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:930: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:938: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:946: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:956: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:966: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:972: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:986: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:993: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1004: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1016: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1024: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1032: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1043: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1050: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1062: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1069: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1076: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1084: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1090: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1097: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1107: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1114: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1121: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1133: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1146: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1153: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1164: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1171: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1179: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1191: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1201: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1210: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1219: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1227: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1238: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1248: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1257: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1265: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1277: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1287: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1300: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1307: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1314: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1324: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1334: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1340: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1347: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1353: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1360: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1367: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1373: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1384: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1392: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1402: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1409: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1422: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1432: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1443: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1453: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1468: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1480: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1492: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1500: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1514: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1527: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1535: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1545: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1560: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1567: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1577: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1586: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1596: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1623: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1648: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1657: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1663: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1670: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1679: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1686: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1693: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1700: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1710: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1718: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1726: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1734: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1742: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1750: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1758: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1766: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1774: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1782: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1791: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1800: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1808: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1818: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1828: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1838: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1844: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1853: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1862: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1871: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1886: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1898: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1907: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1916: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1926: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1936: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1944: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1953: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1964: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1975: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1991: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:1998: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2012: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2025: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2038: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2051: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2061: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2071: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2083: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2095: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2107: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2117: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2126: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2133: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2140: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2151: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2162: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2173: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2184: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2194: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2201: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2208: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2220: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2231: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2242: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2250: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2257: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2269: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2276: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2287: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2294: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2306: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2324: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2336: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2342: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2354: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2360: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2372: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2378: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2390: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2404: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2411: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2418: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2426: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2434: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2440: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2448: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2474: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2489: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2507: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2516: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2523: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2538: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2551: Error: unrecognized symbol type ""
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2560: Error: junk at end of line, first unrecognized character is `,'
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2563: Error: junk at end of line, first unrecognized character is `,'
/home/practicing01/Desktop/Programming/Urho3D/android-Build/Source/ThirdParty/LuaJIT/generated/lj_vm.s:2617: Error: junk at end of line, first unrecognized character is `,'
make[2]: *** [Source/ThirdParty/LuaJIT/CMakeFiles/LuaJIT.dir/generated/lj_vm.s.o] Error 1
make[1]: *** [Source/ThirdParty/LuaJIT/CMakeFiles/LuaJIT.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 60%] Built target Bullet
make: *** [all] Error 2
[/code][/spoiler]

-------------------------

weitjong | 2017-01-02 01:09:12 UTC | #2

The Android-CI jobs for the last commit were all passed. In particular I have highlighted the relevant portion here: [travis-ci.org/urho3d/Urho3D/jobs/99144300#L1166](https://travis-ci.org/urho3d/Urho3D/jobs/99144300#L1166) for one of the CI job which uses the API level 19. I have never experienced this problem in Android build using amalgamated LuaJIT myself on my workstation with plenty of disk space and plenty of memory space and 8 logical cores with HT. Though once in a while I did see the same error (I think) on our Travis-CI build log. Usually a rerun of offending CI job would immediately pass the build test. On Travis-CI it appears to be an intermittent problem. I can only guess it was due to cosmic alignment.  :wink:  Or, most probably it was because our job stresses the worker VM to its edge already. In short, we have limited computing resources in the worker VM. We get what we asked for when we instruct it to build using the amalgamation of the compiler units for LuaJIT sub-library and to make it worse we also instruct it to spawn one more parallel build process that our free Travis-CI account is entitled for. We get away with it most of the time. Back to your problem. My recommendation for you is, nuke your current Android build tree and regenerate it from scratch but try not using URHO3D_LUAJIT_AMALG=1 first, and only after making sure you can get pass that then enable the amalgamated option. I am assuming you are using the amalgamated option in the first place, but if you are not then regenerate the build tree may sometimes also help especially you have indicated that you have it wrongly configured initially.

BTW, congrats with your new spidey game.

-------------------------

practicing01 | 2017-01-02 01:09:12 UTC | #3

It compiles with amalgamation off and "make -j1" (-j2 doesn't work even though I have 2 cores).  Thanks.

-------------------------

weitjong | 2017-01-02 01:09:14 UTC | #4

The compile error manifested itself today in the last RPI CI build [travis-ci.org/urho3d/Urho3D/job ... 9774#L1185](https://travis-ci.org/urho3d/Urho3D/jobs/100199774#L1185) This is a bogus build failure as a rerun of CI job would usually build successfully. I want to prevent this happen in the future. Could you tell me exactly which of these two actually helped in your case: turn off the amalgamated or reduce the number of parallel make worker process; or both. Thanks.

-------------------------

practicing01 | 2017-01-02 01:09:15 UTC | #5

Seems it just needs "make -j1", amalgamation compiled.

-------------------------

weitjong | 2017-01-02 01:09:15 UTC | #6

There is something fishy going on here. Our RPI CI jobs have been configured to run using 4 worker process (i.e. -j4 when using Makefile generator) and it caused the intermittent build failure. Mostly success but lately the frequency of failure increases for some reasons. I have experimented to reduce the number to 3 thinking that it should make the build more stable. To my surprise, 5 out of 6 RPI CI jobs failed the build test. It looks like the change actually aggravates the issue and makes it more reproducible instead. But why? I will open this as an issue in our issue tracker.

-------------------------

weitjong | 2017-01-02 01:09:21 UTC | #7

It turns out to be a regression issue caused by our recent changes in the master. The fix is now in. I believe you can now build with -j2 without any problems.

-------------------------

