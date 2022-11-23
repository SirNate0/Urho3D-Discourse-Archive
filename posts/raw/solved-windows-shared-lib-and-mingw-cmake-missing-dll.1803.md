ghidra | 2017-01-02 01:10:19 UTC | #1

I'm having some new issues compiling "my" project against urho as a shared library. To be clear URHO compiles just fine.
When I go to compile my project (as I have done in the past) i get a pop up error that says mingw is unable to locate Urho3D.dll.
The dll is in the urho build directory /bin
i also copy the dll to my projects bin directory (that has fixed the problem in the past)
URHO3D_HOME is set to the urho build director.

I was consulting Carnalis about this (i know he uses the same compile method) and he is NOT have the same problem as I (other than getting 2 pop up errors that do not keep him from compiling). So being as our setups are largely similar. I am confused as to what I could be possibly missing in my process.

Any help would be greatly appreciated.

-------------------------

jmiller | 2017-01-02 01:10:19 UTC | #2

I started seeing something like this one or two months ago.
In my project's cmake stage, two test compiles fail with dialog boxes:

(dialog)"cmTC_8f747.exe - System Error" "The program can't start because Urho3D_d.dll is missing from your computer."
-- Found Urho3D: urho/build/lib/libUrho3D_d.dll.a
(dialog)"cmTC_e9d9c.exe - System Error" "The program can't start because Urho3D_d.dll is missing from your computer."
-- Found Urho3D: urho/build/lib/libUrho3D_d.dll.a

My project still builds successfully, and Urho3D*.dll is automatically copied there (if there is a way to prevent this, it could be useful).


And this may be unrelated, but cmake seems to be creating invalid links. These target folders are in my ROOT, not bin/, and I'm running cmake from the build tree, passing ../ to cmake as the source tree.
$project/build/bin/CoreData => $project/bin/CoreData
$project/build/bin/Data => $project/bin/Data

I am changing the output directory:
set_output_directories(${CMAKE_BINARY_DIR}/.. RUNTIME PDB)

-------------------------

weitjong | 2017-01-02 01:10:19 UTC | #3

Since you did not paste the actual error message, it is not apparent to me at which stage the error occured. Is it during CMake configuration/generation stage? Or the build tree already got generated and error during actual build phase. I can only assume it is the former, since only CMake does popup error message thingy. If so, then your issue sounds like your project has outdated CMake modules from Urho3D project. Probably you have not setup mklink nor symlink when you created the initial structure of your project the first time, so your project only contains soft copies of the CMake modules at that time. And if so then do yourself a favor by learning how to use mklink or symlink properly and setup your project to use it and fix the problem once and for all. You can, of course,  just try to refresh your stale/outdated CMake modules (and toolchains) by simply making another hard copy operation. However, you have to remember to keep doing that frequently for the remaining of your project's life. Then again, I could be totally wrong about it because all these is just based on my assumption of what has happened. Urho3D is under very active development including its build system,  I can at least guarantee you that soft copies get stale very quickly.

Edit: I was referring to OP.

-------------------------

ghidra | 2017-01-02 01:10:19 UTC | #4

[quote]Is it during CMake configuration/generation stage? Or the build tree already got generated and error during actual build phase[/quote]
Urho3D built from source without a problem. Using cmake_mingw.bat %BUILDPATH% %BUILDFLAGS%

The problem occurs when trying to build my project, using urho as a shared library.
Before building my project, I am sym linking in the relevant cmake folders, and toolchains from the build folder to my project ( I only do that when updating urho just to be safe, and sure I have the right folders when building my project)

[quote]Since you did not paste the actual error message[/quote]
fair enough
After running the following command from my project directory:
[code]
cmake -G "MinGW Makefiles" .
[/code]
The error:
[code]
CMake Error at CMake/Modules/FindUrho3D.cmake:347 (message):
  Could NOT find compatible Urho3D library in Urho3D SDK installation or
  build tree.  Use URHO3D_HOME environment variable or build option to
  specify the location of the non-default SDK installation or build tree.
  Ensure the specified location contains the Urho3D library of the requested
  library type.  Change Dir: D:/MYPROJECT/CMakeFiles/CMakeTmp
[/code]

I am not versed enough referencing that line in FindUrho3D.cmake to know how exactly to trouble shoot it. Even though it seems like a very straight forward path to trace.

Also, all command prompt input is done in elevated mode.
[b]
SOLVED:
The problem was just solved, by my adding the %URHOBUILD%/bin directory directly to my path.. so there was no confusion in cmake finding the dll.[/b]
 
At this point, I guess if anyone is willing to just make clarify what I did wrong, or what step I am missing prior to my "brute force" fix I would be greatful.. Otherwise, all is well in my world, and thank you for your help.

-------------------------

weitjong | 2017-01-02 01:10:19 UTC | #5

It has been years since I migrated from MS Windows to Linux as my main host system, so my understanding of how it works may be rusty now. But this is what I have assumed when the FindUrho3D.cmake module was updated one or two months ago. The Urho3D.dll is copied automatically as part of the try_compile/run test to where the test binary resided. The idea is the when the test binary is being executed then Windows will at least "smart enough" to look for it in the system-wide DLL location AND the directory where the binary is located. If this assumption is wrong then all bets are off.

-------------------------

jmiller | 2017-01-02 01:10:19 UTC | #6

As I watch the cmake test builds in build/CMakeFiles/CMakeTmp...
as indicated by the error dialogs, I do not see the .dll appear there.

MS Win does search the PATH for shared libraries, but I did not choose to 'make install' Urho, if that is relevant..

and again: I still get successful builds.

I don't envy the doing of your cmake work, which has been invaluable.  :slight_smile:

-------------------------

weitjong | 2017-01-02 01:10:19 UTC | #7

One more thing. The assumption is made under the precondition that Urho3D and downstream project are built using "normal" Windows account, not Administrator or any other account with escalated privileges. I will not be surprise that under such privilege accounts, Windows will not just use any DLL it can find along its way and constraint itself to use just those setup in the PATH environment variable. To do the former will be just stupid and luckily at the very least MS developes are not that stupid.

Whether you install the Urho3D SDK or not, is not relevant in this case.

-------------------------

jmiller | 2017-01-02 01:10:20 UTC | #8

The error also occurs without elevated privileges... Same user account of course. UAC, being shoddy, is mostly a popup before certain operations and the sudden right to symlink.. and as far as I know: the rules for locating and executing binaries, the PATH, and most filesystem privileges should be the same in either case. Let me know if I can help further..

-------------------------

weitjong | 2017-01-02 01:10:20 UTC | #9

As far as I concern, there is nothing wrong with our implementation or otherwise the CI builds on AppVeyor would have failed in each run. The CI build is designed to perform two scaffolding tests, i.e. it performs tests with two downstream projects, one using Urho SDK and one using Urho build tree. The CI build covers both STATIC and SHARED cases. I could not think of anything else it could have gone wrong and causes your issue. Sorry.

BTW, the DLL must have been copied unless your module is outdated. See this. [github.com/urho3d/Urho3D/blob/m ... #L241-L247](https://github.com/urho3d/Urho3D/blob/master/CMake/Modules/FindUrho3D.cmake#L241-L247). Either that, or your CMake version is broken. I recall Ivank encountered some issues with the FindUrho3D module and logged a GitHub issue, but in the end the culprit was his CMake. So, probably you should not rule that out too for your case.

-------------------------

jmiller | 2017-01-02 01:10:20 UTC | #10

I get the same behavior with CMake 3.4.1 and CMake 3.5.0 RC-3. And the module is not outdated; it's symlinked to the master.
That this happens on at least two systems gives more opportunity to find it solved.

At least in our cases, it does not seem to be a real problem and builds can continue. Thanks for looking into it.

-------------------------

weitjong | 2017-01-02 01:10:21 UTC | #11

NP. One last shot. [support.microsoft.com/en-us/kb/2264107](https://support.microsoft.com/en-us/kb/2264107). Personally in my Windows 10, I don't have any issues with scaffolding test too. I am using normal Windows account that has been granted MKLINK privilege (nothing more nothing less). And I have not done anything to the CWDIllegalInDllSearch registry entry because I do not have any issues with it in the first place. I only know about this key and its existence a few minutes ago after a quick google search. But I think you guys should know better,  never take Windows advice from a Linux user :wink: .

-------------------------

