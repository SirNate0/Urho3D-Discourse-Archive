George1 | 2017-09-19 03:34:06 UTC | #1

Hi, I'm trying to use version 1.7 from Git. 
I get the below error when building using VS2017 in Windows 10 64 bit.
The error seems to be from script compiler and nanodbc.

I used CMake to generate VS solution file.


Severity	Code	Description	Project	File	Line	Suppression State
Error	LNK2001	unresolved external symbol "public: static class std::locale::id std::codecvt<char16_t,char,struct _Mbstatet>::id" (?id@?$codecvt@_SDU_Mbstatet@@@std@@2V0locale@2@A)	ScriptCompiler	D:\Current Code\Urho3D-master\VS2017\Source\Tools\ScriptCompiler\Urho3D_d.lib(nanodbc.obj)	1	
Error	LNK1120	1 unresolved externals	ScriptCompiler	D:\Current Code\Urho3D-master\VS2017\bin\tool\ScriptCompiler.exe	1	
Error	MSB6006	"cmd.exe" exited with code 1.	RESOURCE_CHECK_2iiDm	C:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\Common7\IDE\VC\VCTargets\Microsoft.CppCommon.targets	171	
Error	LNK2001	unresolved external symbol "public: static class std::locale::id std::codecvt<char16_t,char,struct _Mbstatet>::id" (?id@?$codecvt@_SDU_Mbstatet@@@std@@2V0locale@2@A)	33_Urho2DSpriterAnimation	D:\Current Code\Urho3D-master\VS2017\Source\Samples\33_Urho2DSpriterAnimation\Urho3D_d.lib(nanodbc.obj)	1	
Error	LNK1120	1 unresolved externals	33_Urho2DSpriterAnimation	D:\Current Code\Urho3D-master\VS2017\bin\33_Urho2DSpriterAnimation_d.exe	1	
Error	LNK2001	unresolved external symbol "public: static class std::locale::id std::codecvt<char16_t,char,struct _Mbstatet>::id" (?id@?$codecvt@_SDU_Mbstatet@@@std@@2V0locale@2@A)	36_Urho2DTileMap	D:\Current Code\Urho3D-master\VS2017\Source\Samples\36_Urho2DTileMap\Urho3D_d.lib(nanodbc.obj)	1	
Error	LNK1120	1 unresolved externals	36_Urho2DTileMap	D:\Current Code\Urho3D-master\VS2017\bin\36_Urho2DTileMap_d.exe	1	
Error	LNK2001	unresolved external symbol "public: static class std::locale::id std::codecvt<char16_t,char,struct _Mbstatet>::id" (?id@?$codecvt@_SDU_Mbstatet@@@std@@2V0locale@2@A)	34_DynamicGeometry	D:\Current Code\Urho3D-master\VS2017\Source\Samples\34_DynamicGeometry\Urho3D_d.lib(nanodbc.obj)	1	
Error	LNK1120	1 unresolved externals	34_DynamicGeometry	D:\Current Code\Urho3D-master\VS2017\bin\34_DynamicGeometry_d.exe	1	
Error	LNK2001	unresolved external symbol "public: static class std::locale::id std::codecvt<char16_t,char,struct _Mbstatet>::id" (?id@?$codecvt@_SDU_Mbstatet@@@std@@2V0locale@2@A)	32_Urho2DConstraints	D:\Current Code\Urho3D-master\VS2017\Source\Samples\32_Urho2DConstraints\Urho3D_d.lib(nanodbc.obj)	1	
Error	LNK1120	1 unresolved externals	32_Urho2DConstraints	D:\Current Code\Urho3D-master\VS2017\bin\32_Urho2DConstraints_d.exe	1	
Error	LNK2001	unresolved external symbol "public: static class std::locale::id std::codecvt<char16_t,char,struct _Mbstatet>::id" (?id@?$codecvt@_SDU_Mbstatet@@@std@@2V0locale@2@A)	37_UIDrag	D:\Current Code\Urho3D-master\VS2017\Source\Samples\37_UIDrag\Urho3D_d.lib(nanodbc.obj)	1	
Error	LNK1120	1 unresolved externals	37_UIDrag	D:\Current Code\Urho3D-master\VS2017\bin\37_UIDrag_d.exe	1	
...

-------------------------

weitjong | 2017-09-19 05:50:12 UTC | #2

You should also show the steps you took to generate your build tree (solution file). When the build tree is corrupted, there is no harm to discard it and regenerate from scratch.

-------------------------

George1 | 2017-09-19 07:46:57 UTC | #3

Thanks,
I will re-download and try again with CMake gui.
I didn't have these error message in version 1.6.

Best regards

-------------------------

George1 | 2017-09-19 15:35:14 UTC | #4

Hi, I have redownload and have the same issue:
I found on the internet that 


Severity	Code	Description	Project	File	Line	Suppression State
Error	LNK2001	unresolved external symbol "public: static class std::locale::id std::codecvt<char16_t,char,struct _Mbstatet>::id" (?id@?$codecvt@_SDU_Mbstatet@@@std@@2V0locale@2@A)	ScriptCompiler	D:\Current Code\Urho3D-master\VS2017\Source\Tools\ScriptCompiler\Urho3D_d.lib(nanodbc.obj)	1	
Error	LNK1120	1 unresolved externals	ScriptCompiler	D:\Current Code\Urho3D-master\VS2017\bin\tool\ScriptCompiler.exe	1	
Error	MSB6006	"cmd.exe" exited with code 1.	RESOURCE_CHECK_A0qog	C:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\Common7\IDE\VC\VCTargets\Microsoft.CppCommon.targets	171	
Error	LNK2001	unresolved external symbol "public: static class std::locale::id std::codecvt<char16_t,char,struct _Mbstatet>::id" (?id@?$codecvt@_SDU_Mbstatet@@@std@@2V0locale@2@A)	33_Urho2DSpriterAnimation	D:\Current Code\Urho3D-master\VS2017\Source\Samples\33_Urho2DSpriterAnimation\Urho3D_d.lib(nanodbc.obj)	1	
Error	LNK1120	1 unresolved externals	33_Urho2DSpriterAnimation	D:\Current Code\Urho3D-master\VS2017\bin\33_Urho2DSpriterAnimation_d.exe	1	
Error	LNK2001	unresolved external symbol "public: static class std::locale::id std::codecvt<char16_t,char,struct _Mbstatet>::id" (?id@?$codecvt@_SDU_Mbstatet@@@std@@2V0locale@2@A)	35_SignedDistanceFieldText	D:\Current Code\Urho3D-master\VS2017\Source\Samples\35_SignedDistanceFieldText\Urho3D_d.lib(nanodbc.obj)	1	
...

Here the the CMake Gui config.
![image|523x500](upload://sitaW9hF52GWVnVUrmaKdgmSrXX.png)
![image|633x500](upload://spOvn4ePl2dzNqWd3qMNvWZC7VW.png)
![image|690x341](upload://qVoJddUQThktEP5Xy1wsVk1e0w6.png)

-------------------------

weitjong | 2017-09-20 01:22:26 UTC | #5

In that case it could be a bug then. Could you raise a new issue in our issue tracker or even better a PR if/when you figure out how to fix it. Personally I have not tried to use URHO3D_DATABASE_ODBC build option on Windows platform, so this code path may not be as tested as the other parts of our code base. Normally we use ODBC for sever side and that usually means Linux.

-------------------------

George1 | 2017-09-20 13:53:08 UTC | #6

Hi I have managed to build by adding 2 changes to the nanodbc.cpp file on line 211 and line 233.

Wherever you see _MSC_VER == 1900, change it to below.

_MSC_VER >= 1900

Best regards

-------------------------

weitjong | 2017-09-20 14:59:00 UTC | #7

I see the nanodbc team has already fixed this issue a few months ago, however, we have not pull from its upstream repository for quite some time now.

-------------------------

weitjong | 2017-09-23 13:08:42 UTC | #8

It appears the upstream also does not make any new release since the last time we sync with them. Nevertheless, I have synced with their master branch (with 9118e9c300f218629c83de3a9dcd0999ebbe711e as the last commit).

@George1 Please kindly retry to build Urho with ODBC enabled on VS2017 to see if it works out of the box for you now. Thanks.

-------------------------

George1 | 2017-09-23 14:07:14 UTC | #9

Hi weitjong,

It build fine with the new updated lib.

However, if you enable any of the below option in cmake the build will fail. Especially the Unicode option.

![image|690x52](upload://yRTKRNnx9y1bZ7JhVHcooDqUGUb.png)

Severity	Code	Description	Project	File	Line	Suppression State
Error	LNK2019	unresolved external symbol "public: __cdecl nanodbc::connection::connection(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > const &,long)" (??0connection@nanodbc@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@J@Z) referenced in function "public: __cdecl Urho3D::DbConnection::DbConnection(class Urho3D::Context *,class Urho3D::String const &)" (??0DbConnection@Urho3D@@QEAA@PEAVContext@1@AEBVString@1@@Z)	ScriptCompiler	D:\Current Code\Urho3D-master\VS2017\Source\Tools\ScriptCompiler\Urho3D_d.lib(ODBCConnection.obj)	1	
Error	LNK2019	unresolved external symbol "public: class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > __cdecl nanodbc::result::column_name(short)const " (?column_name@result@nanodbc@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@F@Z) referenced in function "public: class Urho3D::DbResult __cdecl Urho3D::DbConnection::Execute(class Urho3D::String const &,bool)" (?Execute@DbConnection@Urho3D@@QEAA?AVDbResult@2@AEBVString@2@_N@Z)	ScriptCompiler	D:\Current Code\Urho3D-master\VS2017\Source\Tools\ScriptCompiler\Urho3D_d.lib(ODBCConnection.obj)	1	
Error	LNK2019	unresolved external symbol "class nanodbc::result __cdecl nanodbc::execute(class nanodbc::connection &,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > const &,long,long)" (?execute@nanodbc@@YA?AVresult@1@AEAVconnection@1@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@JJ@Z) referenced in function "public: class Urho3D::DbResult __cdecl Urho3D::DbConnection::Execute(class Urho3D::String const &,bool)" (?Execute@DbConnection@Urho3D@@QEAA?AVDbResult@2@AEBVString@2@_N@Z)	ScriptCompiler	D:\Current Code\Urho3D-master\VS2017\Source\Tools\ScriptCompiler\Urho3D_d.lib(ODBCConnection.obj)	1	
Error	LNK2019	unresolved external symbol "public: class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > __cdecl nanodbc::result::get<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >(short)const " (??$get@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@result@nanodbc@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@F@Z) referenced in function "public: class Urho3D::DbResult __cdecl Urho3D::DbConnection::Execute(class Urho3D::String const &,bool)" (?Execute@DbConnection@Urho3D@@QEAA?AVDbResult@2@AEBVString@2@_N@Z)	ScriptCompiler	D:\Current Code\Urho3D-master\VS2017\Source\Tools\ScriptCompiler\Urho3D_d.lib(ODBCConnection.obj)	1	
Error	LNK1120	4 unresolved externals	ScriptCompiler	D:\Current Code\Urho3D-master\VS2017\bin\tool\ScriptCompiler.exe	1

-------------------------

weitjong | 2017-09-23 15:02:46 UTC | #10

I actually did not test those new options as well on my Linux host. Will check later tomorrow if It can be fixed and keep those options.

-------------------------

weitjong | 2017-09-24 04:04:29 UTC | #11

Just did a quick test on Linux. I got a GLIBC ABI mismatch linker error as described [here](https://gcc.gnu.org/onlinedocs/libstdc%2B%2B/manual/using_dual_abi.html) when enabling the UNICODE options, but no errors at all on the other two options. I did not spend more time to fix it though as it  is not related to your error, so fixing it now would not help anything. Also because we are currently just begin to refactor our code base and build system to C++11 standard, while nanodbc is already ahead of us in this matter. Perhaps, we should revisit these options again when we are ready. I will remove these build options for now.

-------------------------

George1 | 2017-09-24 08:05:00 UTC | #12

I'm fine without unicode option for now.
Great to see much progresses in the engine. You guys are doing a fantastic job.

Best regards

-------------------------

