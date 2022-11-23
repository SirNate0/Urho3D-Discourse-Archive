thebluefish | 2017-01-02 01:06:29 UTC | #1

I've noticed something odd with Urho3D and Visual Studio (2013 and 2015). When including the project in my solution, it recompiles every time I build my project. By default Visual Studio is supposed to rebuild only modified files. However the rebuild affects JSONFile.cpp and JSONValue.cpp only. I also tend to get the following build errors:

[code]
5>JSONFile.cpp
5>..\..\..\Source\Urho3D\Resource\JSONFile.cpp : fatal error C1041: cannot open program database 'd:\_projects\jrpgengine\dependencies\urho3d\build\source\urho3d\urho3d.dir\debug\vc120.pdb'; if multiple CL.EXE write to the same .PDB file, please use /FS
5>  JSONValue.cpp
5>..\..\..\Source\Urho3D\Resource\JSONValue.cpp : fatal error C1041: cannot open program database 'd:\_projects\jrpgengine\dependencies\urho3d\build\source\urho3d\urho3d.dir\debug\vc120.pdb'; if multiple CL.EXE write to the same .PDB file, please use /FS
5>  Generating Code...
[/code]

Again, only affecting JSONFile.cpp and JSONValue.cpp. I can't seem to trace the cause of these errors. Any ideas?

-------------------------

weitjong | 2017-01-02 01:06:29 UTC | #2

It sounds like this only happens on VS. I have never seen JSONFile and JSONValue classes being recompiled unnecessarily on my build using GCC. I have little clue on what could be the problem. Not particularly familiar with VS either.

-------------------------

thebluefish | 2017-01-02 01:06:29 UTC | #3

[quote="Sinoid"]Never seen the errors. But I do always get an annoying rapidjson has been changed changed prompt that triggers a recompilation of everything it touches. Never really thought much of it.[/quote]

Ah ok, it was rapidjson causing the issues. I removed the project from my build, and now the Urho3D JSON classes don't get unnecessarily recompiled anymore. Thanks again!

-------------------------

