itisscan | 2017-01-02 01:11:26 UTC | #1

I can't build Urho3d project under the Visual Studio 2015 Update 1 (Version 14.0.24720.0 D14REL). 

I have tried built the Urho3D-1.5 release source code, and the latest code from "Master" branch. 

I get the following error in output window -

[code]1>C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(171,5): error MSB6006: "cmd.exe" exited with code -1073741515.
1>       Done executing task "CustomBuild" -- FAILED.
1>     1>
1>Done building target "CustomBuild" in project "Urho3D.vcxproj" -- FAILED.
1>
1>Build FAILED.[/code]

The full output can see here - [url]http://pastebin.com/iwrURe5B[/url]

Also I have tried to install VS2015 without Update 1. Then I couldn't open Urho3D solution at all, i got error like this - "this project is incompatible with this version of visual studio 2015".

I use Windows 7 64 bit and generate project through cmake2015.bat with command [code]>cmake_vs2015.bat build -DURHO3D_DATABASE_ODBC=1[/code]

Any suggestions how I can fix it ? 

Thanks.

-------------------------

1vanK | 2017-01-02 01:11:26 UTC | #2

> Also I have tried to install VS2015 without Update 1. Then I couldn't open Urho3D solution at all, i got error like this - "this project is incompatible with this version of visual studio 2015".

u need remove build dir and cmake again with another version of VS

-------------------------

itisscan | 2017-01-02 01:11:26 UTC | #3

[quote="1vanK"]> Also I have tried to install VS2015 without Update 1. Then I couldn't open Urho3D solution at all, i got error like this - "this project is incompatible with this version of visual studio 2015".

u need remove build dir and cmake again with another version of VS[/quote]

Ok, i will try it. 

I think there was my stupid mistake, I simply forgot run cmake for another version of VS.

-------------------------

itisscan | 2017-01-02 01:11:28 UTC | #4

I reinstalled Visual Studio 2015 without Update 1.

Then I have successfully built Urho3D lib. (I pulled the latest source from 'Master' branch)

Now when I try to build samples I get 'unresolved external symbol' error -

[code]
Error	LNK2001	unresolved external symbol "__declspec(dllimport) public: static class std::locale::id std::codecvt<char16_t,char,struct _Mbstatet>::id" (__imp_?id@?$codecvt@_SDU_Mbstatet@@@std@@2V0locale@2@A)	33_Urho2DSpriterAnimation	D:\Programming\Projects\GameEconomics\Source\Github\Urho3D-master\build_1\Source\Samples\33_Urho2DSpriterAnimation\Urho3D_d.lib(nanodbc.obj)	1
[/code]

Can see that nanodbc project causes the error.

I have found out that is bug in vs2015.

I will post the issue on nanodbc project.

-------------------------

weitjong | 2017-01-02 01:11:28 UTC | #5

Before you jump to that conclusion, it may be worth a try to build the nanodbc library as a standlone using its own build system. Things were much simpler last year when we first integrate nanodbc library into Urho3D. Now it seems the project has acquired some traction and contributions from other devs. In the past their CMakeLists.txt (or they didn't have one before, cannot remember now) was simpler, and we actually just use our own version of the CMakeLists.txt calling our own macros. That CMakeLists.txt has not been updated much since then. Thus, I won't rule out the possibility that the root cause of your problem is with us (with our integration). Best is if you could ascertain the root cause before filing a bug to any of the project, if possible.

-------------------------

itisscan | 2017-01-02 01:11:28 UTC | #6

[quote="weitjong"]Before you jump to that conclusion, it may be worth a try to build the nanodbc library as a standlone using its own build system. Things were much simpler last year when we first integrate nanodbc library into Urho3D. Now it seems the project has acquired some traction and contributions from other devs. In the past their CMakeLists.txt (or they didn't have one before, cannot remember now) was simpler, and we actually just use our own version of the CMakeLists.txt calling our own macros. That CMakeLists.txt has not been updated much since then. Thus, I won't rule out the possibility that the root cause of your problem is with us (with our integration). Best is if you could ascertain the root cause before filing a bug to any of the project, if possible.[/quote]

I have built nanodbc lib under vs2015 as a standalone using its own build system. The result is the same. I get the 'unresolved external symbol' error - 

[code]
Error	LNK2001	unresolved external symbol "__declspec(dllimport) public: static class std::locale::id std::codecvt<char16_t,char,struct _Mbstatet>::id" (__imp_?id@?$codecvt@_SDU_Mbstatet@@@std@@2V0locale@2@A)	example_northwind	D:\nanodbc-master\build\examples\nanodbc.lib(nanodbc.obj)	1
[/code]

Thanks for the tip. I agree it makes sense to identify the main cause before filing a bug.

-------------------------

weitjong | 2017-01-02 01:11:37 UTC | #7

Could you retry again. I have attempted a fix by re implementing the VS2015 workaround for the linker error. IMHO, this is a regression issue on nanodbc side. i.e. their workaround code was overwritten by subsequent enhancement. After you have verified that the fix works (connection to database and query a field with text conversion, etc) then probably I can submit my patch to nanodbc upstream. Thanks.

-------------------------

christianclavet | 2017-01-02 01:11:38 UTC | #8

HI, I've had theses kinds of problems with VS2015 everytime I wanted [b][u]to have it build in 64bits[/u][/b]. I've changed the command line[b] cmake_vs2015.bat[/b] to this:

[code]@%~dp0\cmake_generic.bat %* -VS=14 -DURHO3D_64BIT=1[/code]
Then I change the options from the CMAKE GUI and rebuild.
Does it build without the ODBC option? I've not tried this one.

-------------------------

weitjong | 2017-01-02 01:11:38 UTC | #9

[quote="christianclavet"]HI, I've had theses kinds of problems with VS2015 everytime I wanted [b][u]to have it build in 64bits[/u][/b]. I've changed the command line[b] cmake_vs2015.bat[/b] to this:

[code]@%~dp0\cmake_generic.bat %* -VS=14 -DURHO3D_64BIT=1[/code]
Then I change the options from the CMAKE GUI and rebuild.
Does it build without the ODBC option? I've not tried this one.[/quote]

I think you have to be more specific than that. I/we don't have problem with VS2015 64-bit in general.

-------------------------

christianclavet | 2017-01-02 01:11:39 UTC | #10

It's only a issue I have with MSVC (2015 in particuliar). The details are from this thread here: [url]http://discourse.urho3d.io/t/solved-building-urho3d-on-windows-10-using-msvc-2015/1446/1[/url]
This thread described problem seem to apply more to the ODBC option. Not the 64bit option.

-------------------------

weitjong | 2017-01-02 01:11:39 UTC | #11

Yes, they are totally different issue. As for your 64-bit VS issue, I thought I have explained it in that thread. It is how CMake generator for VS works and there is nothing we can help it. It happens to any VS, not just VS2015. The key things to remember:
[ol][li]CMake does not allow changes of compiler and/or generator after the build tree has been generated.[/li]
[li]CMake has different generators for 32-bit and 64-bit for each version of VS because MSVC compiler is not multilib-capable.[/li][/ol]
If you use cmake-gui all the way then when CMake prompted to choose a generator to use, choose one carefully. If you use CMake CLI all the way then pass the URHO3D_64BIT build option properly during the initial configuration. Changing this cache value after the fact is asking for trouble when using VS.

-------------------------

itisscan | 2017-01-02 01:11:40 UTC | #12

[quote="weitjong"]Could you retry again. I have attempted a fix by re implementing the VS2015 workaround for the linker error. IMHO, this is a regression issue on nanodbc side. i.e. their workaround code was overwritten by subsequent enhancement. After you have verified that the fix works (connection to database and query a field with text conversion, etc) then probably I can submit my patch to nanodbc upstream. Thanks.[/quote]

I have successfully built the latest code from Master branch under VS2015, but it seems that nanodbc v2.12.2 does not solve issue that I described there - [url]http://discourse.urho3d.io/t/select-text-from-database-returns-wrong-value/1906/1[/url]  .

I still get wrong value if text size is > 1024.

-------------------------

weitjong | 2017-01-02 01:11:40 UTC | #13

That's too bad. Until you can confirm everything is working fine, I think I will hold to submit my patch upstream. Do let me know if @lexicalunit has fixed your other issue and I will make another pull afterwards.

-------------------------

