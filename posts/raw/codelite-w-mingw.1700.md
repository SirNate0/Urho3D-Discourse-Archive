thebluefish | 2017-01-02 01:09:34 UTC | #1

Wanted to document this somewhere.

We had recently added cmake_codelite.bat and cmake_codelite.sh to Urho3D. These will allow you to generate CodeLite projects for Urho3D trivially. I have tested these and verified them to work with MinGW64 on Windows 7 x64 and Windows 10 x64. Urho3D 1.5 won't build Assimp this way, but everything works in HEAD. There is one caveat though, all of the projects generated may be affected by a bug in the CMake CodeLite generator that incorrectly calculates the number of CPU cores on the system. This will add the switch "-j 0" which will cause the compiler to stop, but removing the switch allows Urho3D to compile fine.

Here is a batch script that generates the CodeLite project and automatically strips these switches. It could be improved to scan the directory for all project files, but currently only affects the Urho3D project (samples and documentation need to be manually edited out):

[code]
:: Build Urho3D
setlocal
::call %cd%/Urho3D/cmake_generic.bat %* -G "CodeLite - MinGW Makefiles" :: For Urho3D versions that don't include cmake_codelite.bat
call %cd%/Urho3D/cmake_codelite.bat %*
call GOTO :FIX_PROJECT
GOTO:eof

:FIX_PROJECT
:: CD to build directory
set current_working_directory=%cd%
cd %1

:: Fix CMake bug - https://cmake.org/Bug/view.php?id=15054
:: Requires MinGW
sed -i "s/-j 0//g" Urho3D.project

:: CD back to working directory
cd %current_working_directory%
GOTO:eof
[/code]

-------------------------

weitjong | 2017-01-02 01:09:35 UTC | #2

Thanks for sharing it. You may want to know that on the Linux side, we actually have a "hook" to fix this sort of problems caused by CMake. The generic script calls a post_cmake() function defined in .bash_helper.sh to fix whatever it needs fixing. I think the same thing can be done on the Windows side as well.

-------------------------

thebluefish | 2017-01-02 01:09:35 UTC | #3

Really? I'm trying to finally tackle CMake this weekend, so I'll look at that and see what I can do with it while I'm at it.

-------------------------

