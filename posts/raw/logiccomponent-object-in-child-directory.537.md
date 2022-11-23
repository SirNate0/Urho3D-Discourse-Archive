empirer64 | 2017-01-02 01:01:14 UTC | #1

Hello,
I need a advice. I have a Application inherited object in the project root directory (./MainWindow.h) and a LogicComponent inherited object in the child directory (./HUD/HUD.h). The problem is that I can not compile it because when I try to HUD::RegisterObject(Context* context) in the MainWindow then the compiler says: 
[code]undefined reference to `HUD::RegisterObject(Urho3D::Context*)'[/code]
But when I move the HUD.h and HUD.cpp files into the project root directory then it compiles without errors and I can run it. Maybe the problem is in the CMakeLists.txt, because I am using Kdevelop and it automaticaly creates empty CMakeLists.txt files in the child directories (I am a Cmake n00b).

-------------------------

empirer64 | 2017-01-02 01:01:16 UTC | #2

Ok, maybe I should write it more simple. What I need is to to put a LogicComponent object into project subdirectory, but when I do this I get a error: 
[code]/Source/MainWindow.cpp:97: undefined reference to `HUD::RegisterObject(Urho3D::Context*)'[/code]
Can anybody please help me ?  :cry:

-------------------------

weitjong | 2017-01-02 01:01:16 UTC | #3

Your suspicion is correct. This is CMake build script (CMakeLists.txt) configuration problem. I think you will get better support in CMake forum or KDevelop froum (if they have one) for such basic question.

I have never used KDevelop before, so I don't know for sure why it does that (creating empty CMakeLists.txt in the subdir) but perhaps it wants to accommodate CMake's scoping concept. If you look at Urho3D build scripts, you will also observe we use this concept. The Source directory has a main CMakeLists.txt with each subdir also has its own child CMakeLists.txt which only takes care of project configuration for its own scope in the subdir.

Back to your issue. I think there are two ways to solve it.
[ol][li] More advance. Use the scoping. Configure the empty CMakeLists.txt in the subdir and then add the child CMakeLists.txt into the parent CMakeLists.txt in your project's main Source dir by using CMake's add_subdirectory() command.[/li]
[li] For simple project. Just configure your main CMakeLists.txt to "see" the source and header files in the "HUD" subdir by including them manually when you call CMake's add_executable() command. You probably also need to configure your header search path to include "HUD". See CMake's include_directories() command.[/li][/ol]
Now, if you use our Urho3D-CMake-common.cmake module then you can use our macro define_source_files() in conjunction with setup_executable() to do that. By default the former just "globs" C++ implementation and header files without taking subdirs into considerations. But you can pass extra arguments to change this behavior. And the latter macro uses the found source files to setup the executable target. Unfortunately we don't have any documentation pages on this. So you will have to study the macro itself and read the comments yourself on how to use it. You may want to refer to Source/Engine/Graphics/CMakeLists.txt as an example. This example kinds of doing both of the above :slight_smile: which is not exactly what you need but I hope you get the idea. Note the macro does not take care of the header search path, so it still needs to be done by yourself if it is required.

-------------------------

empirer64 | 2017-01-02 01:01:17 UTC | #4

Thank you for your answer. I will try that.

-------------------------

