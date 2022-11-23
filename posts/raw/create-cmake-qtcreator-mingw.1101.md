umen | 2017-01-02 01:05:28 UTC | #1

Hello all 
lately im using QtCreator allot , and its great IDE light and fast ,
is there any change to create automatcly cmake_qtcreator.cmd generator ?
i tried to load project based on the cmakefile  the 
and gave it the parameters : 
-E chdir  G:\dev\cpp\3d\Urho3D\git\Urho3D-build-Qt-creator -G "MinGW Makefiles"
it does generate me the files but not loading in the Qtcreator

-------------------------

weitjong | 2017-01-02 01:05:28 UTC | #2

There is a thread about Qt-creator here sometime ago. [topic451.html](http://discourse.urho3d.io/t/guide-urho3d-debugging-in-qt-creator/452/1). Keep in mind that the thread is posted before 1.4 release. IMHO, there is no need for the cmake_qtcreator or something like that because:

[ol]
[li]CMake does not provide generator for Qt-creator.[/li]
[li]Qt-creator can open Makefile-based project and Code::Blocks project. Perhaps this is a strategy mistake from Qt developers.[/li][/ol]
So, long story short. Use cmake_codeblock.bat to configure and generate the build tree, then open the generated project in the build tree with Qt-creator.

-------------------------

weitjong | 2017-01-02 01:05:28 UTC | #3

Alternatively, I think you can also directly go to Qt-creator and instruct it to process the Urho3D (or your own project) main CMakeLists.txt. I write this based on my memory, so I could be wrong here.

-------------------------

umen | 2017-01-02 01:05:28 UTC | #4

Thanks for the quick replay , please see this : [topic1137.html](http://discourse.urho3d.io/t/how-to-see-all-sources-engine-and-examples-in-qtcreator/1102/1)
sorry about the duplication

-------------------------

GoogleBot42 | 2017-01-02 01:05:29 UTC | #5

[quote="weitjong"]Qt-creator can open Makefile-based project and Code::Blocks project. Perhaps this is a strategy mistake from Qt developers.[/quote]

Just a small correction.  Qt creator doesn't support makefiles but it does support cmake's CMakeLists.txt.

[quote="weitjong"]Alternatively, I think you can also directly go to Qt-creator and instruct it to process the Urho3D (or your own project) main CMakeLists.txt. I write this based on my memory, so I could be wrong here.[/quote]

I use qt creator (the only fast, lightweight nice looking C++ IDE available for linux IMO) and this is exactly what I do.  I just pass the CMakeLists.txt as an arg to starting qtcreator and it opens a prompt where you specify the build directory and any cmake args.  Unfortunately, this method doesn't allow you to use some of the autoconfiguration that Urho3D's sh files do for platforms like android.  Although, this should be able to be done directly in the cmake args.

-------------------------

