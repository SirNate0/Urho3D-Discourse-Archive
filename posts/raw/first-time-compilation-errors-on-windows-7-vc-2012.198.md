umen | 2017-01-02 00:58:48 UTC | #1

Hello all 
i try to compile the engine with as it written in the docs without script support just the c++ engine  the sources are cloned from the git repository 
this is the cmake command i executed :
[code]cmake_vs2012.bat -DENABLE_ANGELSCRIPT=0 -DURHO3D_SAMPLES=1 -DURHO3D_TOOLS=1 -DURHO3D_EXTRAS=1 -DURHO3D_OPENGL=1 -DURHO3D_STATIC_RUNTIME=1[/code]

this is the cmake output :
[code]D:\dev\cpp\3d\git\urho3d\Urho3D>cmake -E chdir Build cmake  -G "Visual Studio 11" VERSION=11 -DENABLE_ANGELSCRIPT=0 -DURHO3D_SAMPLES=1 -DURHO3D_TOOLS=1 -DURHO3D_EXTRAS=1 -DUR
HO3D_OPENGL=1 -DURHO3D_STATIC_RUNTIME=1 ..\Source
-- The C compiler identification is MSVC 17.0.60610.1
-- The CXX compiler identification is MSVC 17.0.60610.1
-- Check for working C compiler using: Visual Studio 11
-- Check for working C compiler using: Visual Studio 11 -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler using: Visual Studio 11
-- Check for working CXX compiler using: Visual Studio 11 -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Found DirectX SDK: C:/Program Files (x86)/Microsoft DirectX SDK (June 2010)/Lib/x86/d3d9.lib C:/Program Files (x86)/Microsoft DirectX SDK (June 2010)/Include
-- Looking for include file stdint.h
-- Looking for include file stdint.h - found
-- Looking for include file wbemcli.h
-- Looking for include file wbemcli.h - found
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Failed
-- Performing Test COMPILER_HAS_DEPRECATED
-- Performing Test COMPILER_HAS_DEPRECATED - Success
-- Found Urho3D: as CMake target
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    ENABLE_ANGELSCRIPT

-- Build files have been written to: D:/dev/cpp/3d/git/urho3d/Urho3D/Build[/code]

when trying to compile im getting those errors: 
[code]Error	85	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(bool)' to 'void (__thiscall Urho3D::Octree::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	456	1	Urho3D
Error	86	error C2440: 'type cast' : cannot convert from 'bool (__thiscall Urho3D::Animatable::* )(void) const' to 'void (__thiscall Urho3D::Octree::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	457	1	Urho3D
Error	87	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(Urho3D::ObjectAnimation *)' to 'void (__thiscall Urho3D::Octree::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	458	1	Urho3D
Error	88	error C2440: 'type cast' : cannot convert from 'Urho3D::ObjectAnimation *(__thiscall Urho3D::Animatable::* )(void) const' to 'void (__thiscall Urho3D::Octree::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	459	1	Urho3D
Error	89	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,Urho3D::AttributeAnimation *,Urho3D::WrapMode,float)' to 'void (__thiscall Urho3D::Octree::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	460	1	Urho3D
Error	90	error C2440: 'type cast' : cannot convert from 'Urho3D::AttributeAnimation *(__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::Octree::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	461	1	Urho3D
Error	91	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,Urho3D::WrapMode)' to 'void (__thiscall Urho3D::Octree::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	462	1	Urho3D
Error	92	error C2440: 'type cast' : cannot convert from 'Urho3D::WrapMode (__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::Octree::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	463	1	Urho3D
Error	93	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,float)' to 'void (__thiscall Urho3D::Octree::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	464	1	Urho3D
Error	94	error C2440: 'type cast' : cannot convert from 'float (__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::Octree::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	465	1	Urho3D
Error	95	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(bool)' to 'void (__thiscall Urho3D::RigidBody::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	456	1	Urho3D
Error	96	error C2440: 'type cast' : cannot convert from 'bool (__thiscall Urho3D::Animatable::* )(void) const' to 'void (__thiscall Urho3D::RigidBody::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	457	1	Urho3D
Error	97	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(Urho3D::ObjectAnimation *)' to 'void (__thiscall Urho3D::RigidBody::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	458	1	Urho3D
Error	98	error C2440: 'type cast' : cannot convert from 'Urho3D::ObjectAnimation *(__thiscall Urho3D::Animatable::* )(void) const' to 'void (__thiscall Urho3D::RigidBody::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	459	1	Urho3D
Error	99	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,Urho3D::AttributeAnimation *,Urho3D::WrapMode,float)' to 'void (__thiscall Urho3D::RigidBody::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	460	1	Urho3D
Error	100	error C2440: 'type cast' : cannot convert from 'Urho3D::AttributeAnimation *(__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::RigidBody::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	461	1	Urho3D
Error	101	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,Urho3D::WrapMode)' to 'void (__thiscall Urho3D::RigidBody::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	462	1	Urho3D
Error	102	error C2440: 'type cast' : cannot convert from 'Urho3D::WrapMode (__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::RigidBody::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	463	1	Urho3D
Error	103	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,float)' to 'void (__thiscall Urho3D::RigidBody::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	464	1	Urho3D
Error	104	error C2440: 'type cast' : cannot convert from 'float (__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::RigidBody::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	465	1	Urho3D
Error	105	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(bool)' to 'void (__thiscall Urho3D::PhysicsWorld::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	456	1	Urho3D
Error	106	error C2440: 'type cast' : cannot convert from 'bool (__thiscall Urho3D::Animatable::* )(void) const' to 'void (__thiscall Urho3D::PhysicsWorld::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	457	1	Urho3D
Error	107	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(Urho3D::ObjectAnimation *)' to 'void (__thiscall Urho3D::PhysicsWorld::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	458	1	Urho3D
Error	108	error C2440: 'type cast' : cannot convert from 'Urho3D::ObjectAnimation *(__thiscall Urho3D::Animatable::* )(void) const' to 'void (__thiscall Urho3D::PhysicsWorld::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	459	1	Urho3D
Error	109	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,Urho3D::AttributeAnimation *,Urho3D::WrapMode,float)' to 'void (__thiscall Urho3D::PhysicsWorld::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	460	1	Urho3D
Error	110	error C2440: 'type cast' : cannot convert from 'Urho3D::AttributeAnimation *(__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::PhysicsWorld::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	461	1	Urho3D
Error	111	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,Urho3D::WrapMode)' to 'void (__thiscall Urho3D::PhysicsWorld::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	462	1	Urho3D
Error	112	error C2440: 'type cast' : cannot convert from 'Urho3D::WrapMode (__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::PhysicsWorld::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	463	1	Urho3D
Error	113	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,float)' to 'void (__thiscall Urho3D::PhysicsWorld::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	464	1	Urho3D
Error	114	error C2440: 'type cast' : cannot convert from 'float (__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::PhysicsWorld::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	465	1	Urho3D
Error	115	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(bool)' to 'void (__thiscall Urho3D::ScriptInstance::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	456	1	Urho3D
Error	116	error C2440: 'type cast' : cannot convert from 'bool (__thiscall Urho3D::Animatable::* )(void) const' to 'void (__thiscall Urho3D::ScriptInstance::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	457	1	Urho3D
Error	117	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(Urho3D::ObjectAnimation *)' to 'void (__thiscall Urho3D::ScriptInstance::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	458	1	Urho3D
Error	118	error C2440: 'type cast' : cannot convert from 'Urho3D::ObjectAnimation *(__thiscall Urho3D::Animatable::* )(void) const' to 'void (__thiscall Urho3D::ScriptInstance::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	459	1	Urho3D
Error	119	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,Urho3D::AttributeAnimation *,Urho3D::WrapMode,float)' to 'void (__thiscall Urho3D::ScriptInstance::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	460	1	Urho3D
Error	120	error C2440: 'type cast' : cannot convert from 'Urho3D::AttributeAnimation *(__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::ScriptInstance::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	461	1	Urho3D
Error	121	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,Urho3D::WrapMode)' to 'void (__thiscall Urho3D::ScriptInstance::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	462	1	Urho3D
Error	122	error C2440: 'type cast' : cannot convert from 'Urho3D::WrapMode (__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::ScriptInstance::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	463	1	Urho3D
Error	123	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,float)' to 'void (__thiscall Urho3D::ScriptInstance::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	464	1	Urho3D
Error	124	error C2440: 'type cast' : cannot convert from 'float (__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::ScriptInstance::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	465	1	Urho3D
Error	125	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(bool)' to 'void (__thiscall Urho3D::PhysicsWorld2D::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	456	1	Urho3D
Error	126	error C2440: 'type cast' : cannot convert from 'bool (__thiscall Urho3D::Animatable::* )(void) const' to 'void (__thiscall Urho3D::PhysicsWorld2D::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	457	1	Urho3D
Error	127	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(Urho3D::ObjectAnimation *)' to 'void (__thiscall Urho3D::PhysicsWorld2D::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	458	1	Urho3D
Error	128	error C2440: 'type cast' : cannot convert from 'Urho3D::ObjectAnimation *(__thiscall Urho3D::Animatable::* )(void) const' to 'void (__thiscall Urho3D::PhysicsWorld2D::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	459	1	Urho3D
Error	129	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,Urho3D::AttributeAnimation *,Urho3D::WrapMode,float)' to 'void (__thiscall Urho3D::PhysicsWorld2D::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	460	1	Urho3D
Error	130	error C2440: 'type cast' : cannot convert from 'Urho3D::AttributeAnimation *(__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::PhysicsWorld2D::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	461	1	Urho3D
Error	131	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,Urho3D::WrapMode)' to 'void (__thiscall Urho3D::PhysicsWorld2D::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	462	1	Urho3D
Error	132	error C2440: 'type cast' : cannot convert from 'Urho3D::WrapMode (__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::PhysicsWorld2D::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	463	1	Urho3D
Error	133	error C2440: 'type cast' : cannot convert from 'void (__thiscall Urho3D::Animatable::* )(const Urho3D::String &,float)' to 'void (__thiscall Urho3D::PhysicsWorld2D::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	464	1	Urho3D
Error	134	error C2440: 'type cast' : cannot convert from 'float (__thiscall Urho3D::Animatable::* )(const Urho3D::String &) const' to 'void (__thiscall Urho3D::PhysicsWorld2D::* )(void)'	d:\dev\cpp\3d\git\urho3d\urho3d\source\engine\script\APITemplates.h	465	1	Urho3D
Error	135	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\19_VehicleDemo\LINK	19_VehicleDemo
Error	136	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\18_CharacterDemo\LINK	18_CharacterDemo
Error	137	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\20_HugeObjectCount\LINK	20_HugeObjectCount
Error	138	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\21_AngelScriptIntegration\LINK	21_AngelScriptIntegration
Error	139	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\25_Urho2DParticle\LINK	25_Urho2DParticle
Error	140	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\26_ConsoleInput\LINK	26_ConsoleInput
Error	141	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\28_Urho2DPhysicsRope\LINK	28_Urho2DPhysicsRope
Error	142	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\27_Urho2DPhysics\LINK	27_Urho2DPhysics
Error	143	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\29_SoundSynthesis\LINK	29_SoundSynthesis
Error	144	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\14_SoundEffects\LINK	14_SoundEffects
Error	145	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\07_Billboards\LINK	07_Billboards
Error	146	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Tools\AssetImporter\LINK	AssetImporter
Error	147	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\01_HelloWorld\LINK	01_HelloWorld
Error	148	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\02_HelloGUI\LINK	02_HelloGUI
Error	149	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\03_Sprites\LINK	03_Sprites
Error	150	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\30_LightAnimation\LINK	30_LightAnimation
Error	151	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\04_StaticScene\LINK	04_StaticScene
Error	152	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\05_AnimatingScene\LINK	05_AnimatingScene
Error	153	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\08_Decals\LINK	08_Decals
Error	154	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\06_SkeletalAnimation\LINK	06_SkeletalAnimation
Error	155	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\09_MultipleViewports\LINK	09_MultipleViewports
Error	156	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Extras\OgreBatchConverter\LINK	OgreBatchConverter
Error	157	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Tools\PackageTool\LINK	PackageTool
Error	158	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\10_RenderToTexture\LINK	10_RenderToTexture
Error	159	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Tools\RampGenerator\LINK	RampGenerator
Error	160	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\12_PhysicsStressTest\LINK	12_PhysicsStressTest
Error	161	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\13_Ragdolls\LINK	13_Ragdolls
Error	162	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\23_Water\LINK	23_Water
Error	163	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Tools\ScriptCompiler\LINK	ScriptCompiler
Error	164	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\15_Navigation\LINK	15_Navigation
Error	165	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\16_Chat\LINK	16_Chat
Error	166	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Tools\Urho3DPlayer\LINK	Urho3DPlayer
Error	167	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Samples\17_SceneReplication\LINK	17_SceneReplication
Error	168	error LNK1104: cannot open file 'D:\dev\cpp\3d\git\urho3d\Urho3D\Lib\Urho3D_d.lib'	D:\dev\cpp\3d\git\urho3d\Urho3D\Build\Tools\OgreImporter\LINK	OgreImporter
[/code]

-------------------------

Mike | 2017-01-02 00:58:48 UTC | #2

Try replace -DENABLE_ANGELSCRIPT=0 by -DURHO3D_ANGELSCRIPT=0

-------------------------

cadaver | 2017-01-02 00:58:48 UTC | #3

The AngelScript bindings are just right now broken on MSVC. A fix will be committed soon.

EDIT: should be there now.

-------------------------

umen | 2017-01-02 00:58:48 UTC | #4

Thanks all working now on windows , I'm targeting using the engine as static lib without scripts support 
now I'm going to test on Mac targeting for iOS.
ok every thing is comping great on IOS 
but there is no mobile example , the examples run fine on iOS but are just as the windows without mobile event handling
i will start new forum thread on the subject   

p.s
can it be that the "Notify me when a reply is posted" not working in this forum ?

-------------------------

umen | 2017-01-02 00:58:48 UTC | #5

Question , 
i compile with those flags :
-DURHO3D_ANGELSCRIPT=0  -DURHO3D_STATIC_RUNTIME=1
but i need the player to be compiled also for using the editor ? 
and as i understand when setting -DURHO3D_ANGELSCRIPT=0 the player dosn't compile , so my question is 
how to compile the player also ?
Thanks

-------------------------

weitjong | 2017-01-02 00:58:49 UTC | #6

The Urho3DPlayer won't work without scripting support. It needs either AngelScript or Lua to play the scripts.

-------------------------

umen | 2017-01-02 00:58:49 UTC | #7

yeah i figure it out , but i mean in compilation stage , i want to be able to run my examples natively and also compile the player 
so what should i do ? -DURHO3D_ANGELSCRIPT=1 ?

did try to compile with: -DURHO3D_ANGELSCRIPT=1   but got cake errors , I'm using the latest sources 
[code]meirs-Mac-mini:Urho3D meiryanovich$ ./cmake_ios.sh -DURHO3D_ANGELSCRIPT=1 -DURHO3D_LOGGING=1  -DURHO3D_STATIC_RUNTIME=1
-- The C compiler identification is Clang 5.1.0
-- The CXX compiler identification is Clang 5.1.0
-- Looking for include file stdint.h
CMake Error at /opt/local/share/cmake-2.8/Modules/CMakeCInformation.cmake:37 (get_filename_component):
  get_filename_component called with incorrect number of arguments
Call Stack (most recent call first):
  CMakeLists.txt:3 (PROJECT)


CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Looking for include file stdint.h - not found
-- The ASM compiler identification is unknown
-- Found assembler: /usr/bin/cc
-- Warning: Did not find file Compiler/-ASM
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
CMake Error at /opt/local/share/cmake-2.8/Modules/CMakeCXXInformation.cmake:37 (get_filename_component):
  get_filename_component called with incorrect number of arguments
Call Stack (most recent call first):
  CMakeLists.txt:3 (PROJECT)


CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Failed
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
CMake Error at /opt/local/share/cmake-2.8/Modules/CMakeCXXInformation.cmake:37 (get_filename_component):
  get_filename_component called with incorrect number of arguments
Call Stack (most recent call first):
  CMakeLists.txt:3 (PROJECT)


CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Failed
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
CMake Error at /opt/local/share/cmake-2.8/Modules/CMakeCXXInformation.cmake:37 (get_filename_component):
  get_filename_component called with incorrect number of arguments
Call Stack (most recent call first):
  CMakeLists.txt:3 (PROJECT)


CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Failed
-- Performing Test COMPILER_HAS_DEPRECATED
CMake Error at /opt/local/share/cmake-2.8/Modules/CMakeCXXInformation.cmake:37 (get_filename_component):
  get_filename_component called with incorrect number of arguments
Call Stack (most recent call first):
  CMakeLists.txt:3 (PROJECT)


CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Performing Test COMPILER_HAS_DEPRECATED - Failed
-- Found Urho3D: as CMake target
-- Configuring incomplete, errors occurred!
[/code]


opened issue:
[url]https://github.com/urho3d/Urho3D/issues/308[/url]

-------------------------

weitjong | 2017-01-02 00:58:49 UTC | #8

The short answer: Build with -DURHO3D_ANGELSCRIPT=1
Actually that is the default, so you can just build without specifying the option, provided you have not manually set it to 0 in earlier CMake invokation. 

The issue with CMake and Xcode that you reported on GitHub issue has been commented and closed now. But may I suggest you in future not to hijack the thread for unrelated matter (although the thread is started by you also). This thread is for Win7 vc2012; your last post is for Xcode 5.1. I just want to make it easier for the next persons to find the posts/threads when they have similar issue. Cheers.

-------------------------

umen | 2017-01-02 00:58:49 UTC | #9

Yes you are right 
Next time I will open new thread for each subject 
Thanks for the fast response

-------------------------

cadaver | 2017-01-02 00:58:49 UTC | #10

To elaborate, the scripting is the highest level in the Urho3D library, which depends on everything else, but nothing depends on it. This means that you can compile the library with scripting to be able to run the editor etc., but when you make your own application that doesn't use scripting, you won't pay unnecessarily for it in executable size, because it won't be linked in if you don't use it. Naturally this is when you build Urho as static library, if you use a shared library then the scripting support will be built inside it if enabled, resulting in a larger DLL size.

-------------------------

