christianclavet | 2017-01-02 01:09:12 UTC | #1

Hi, I'm now able to build URHO3D without much trouble with the options I need. But I'm still in the early beginning with URHO...

I started recently with MSVC and CODELITE (Mingw32) to try to use the lib externally but it fail all the time. I come from the Irrlicht world, and I was used to use a library this way:
1. set the path of the include files and the compiled library file (.a or .lib) for the used library, in the compiler settings.
2. set the name of the library to the linker setting.
3. Use the "hello world" example and try to compile.

[b]Results:[/b]
[code]C:\WINDOWS\system32\cmd.exe /C C:/TDM-GCC-64/bin/mingw32-make.exe -j8 SHELL=cmd.exe -e -f  Makefile
"----------Building project:[ Test - Debug ]----------"
mingw32-make.exe[1]: Entering directory 'C:/Users/Public/Projets/Test'
mingw32-make.exe[1]: Leaving directory 'C:/Users/Public/Projets/Test'
mingw32-make.exe[1]: Entering directory 'C:/Users/Public/Projets/Test'
C:/TDM-GCC-64/bin/g++.exe  -c  "C:/Users/Public/Projets/Test/main.cpp" -g -O0 -Wall  -o ./Debug/main.cpp.o -I. -I../URHO/Codelite/Include -I../URHO/Codelite/Include/Audio -I../URHO/Codelite/Include/Container -I../URHO/Codelite/Include/Core -I../URHO/Codelite/Include/Database -I../URHO/Codelite/Include/Engine -I../URHO/Codelite/Include/Graphics -I../URHO/Codelite/Include/Input -I../URHO/Codelite/Include/IO -I../URHO/Codelite/Include/LuaScript -I../URHO/Codelite/Include/Math -I../URHO/Codelite/Include/Navigation -I../URHO/Codelite/Include/Network -I../URHO/Codelite/Include/Physics -I../URHO/Codelite/Include/Resource -I../URHO/Codelite/Include/Scene -I../URHO/Codelite/Include/Script -I../URHO/Codelite/Include/ThirdParty -I../URHO/Codelite/Include/ThirdParty/AngelScript -I../URHO/Codelite/Include/ThirdParty/Box2D -I../URHO/Codelite/Include/ThirdParty/Bullet -I../URHO/Codelite/Include/ThirdParty/Civetweb -I../URHO/Codelite/Include/ThirdParty/Detour -I../URHO/Codelite/Include/ThirdParty/DetourCrowd -I../URHO/Codelite/Include/ThirdParty/DetourTileCache -I../URHO/Codelite/Include/ThirdParty/freetype -I../URHO/Codelite/Include/ThirdParty/GLEW -I../URHO/Codelite/Include/ThirdParty/JO -I../URHO/Codelite/Include/ThirdParty/kNet -I../URHO/Codelite/Include/ThirdParty/libCpuId -I../URHO/Codelite/Include/ThirdParty/Lua -I../URHO/Codelite/Include/ThirdParty/LZ4 -I../URHO/Codelite/Include/ThirdParty/PugiXml -I../URHO/Codelite/Include/ThirdParty/rapidjson -I../URHO/Codelite/Include/ThirdParty/Recast -I../URHO/Codelite/Include/ThirdParty/SDL -I../URHO/Codelite/Include/ThirdParty/StanHull -I../URHO/Codelite/Include/ThirdParty/STB -I../URHO/Codelite/Include/ThirdParty/toluapp -I../URHO/Codelite/Include/UI -I../URHO/Codelite/Include/Urho2D
C:/Users/Public/Projets/Test/main.cpp:13:24: error: expected constructor, destructor, or type conversion before '(' token
 DEFINE_APPLICATION_MAIN(HelloWorld)
                        ^
C:/Users/Public/Projets/Test/main.cpp:20:6: error: 'HelloWorld' has not been declared
 void HelloWorld::Start()
      ^
C:/Users/Public/Projets/Test/main.cpp: In function 'void Start()':
C:/Users/Public/Projets/Test/main.cpp:23:5: error: 'Sample' has not been declared
     Sample::Start();
     ^
C:/Users/Public/Projets/Test/main.cpp:26:16: error: 'CreateText' was not declared in this scope
     CreateText();
                ^
C:/Users/Public/Projets/Test/main.cpp:31:23: error: 'SubscribeToEvents' was not declared in this scope
     SubscribeToEvents();
                       ^
C:/Users/Public/Projets/Test/main.cpp: At global scope:
C:/Users/Public/Projets/Test/main.cpp:34:6: error: 'HelloWorld' has not been declared
 void HelloWorld::CreateText()
      ^
C:/Users/Public/Projets/Test/main.cpp: In function 'void CreateText()':
C:/Users/Public/Projets/Test/main.cpp:36:5: error: 'ResourceCache' was not declared in this scope
     ResourceCache* cache = GetSubsystem<ResourceCache>();
     ^
C:/Users/Public/Projets/Test/main.cpp:36:5: note: suggested alternative:
In file included from ../URHO/Codelite/Include/Urho3D/Input/../UI/../UI/BorderImage.h:26:0,
                 from ../URHO/Codelite/Include/Urho3D/Input/../UI/Cursor.h:27,
                 from ../URHO/Codelite/Include/Urho3D/Input/Input.h:30,
                 from C:/Users/Public/Projets/Test/main.cpp:7:
../URHO/Codelite/Include/Urho3D/Input/../UI/../UI/../UI/UIElement.h:109:7: note:   'Urho3D::ResourceCache'
 class ResourceCache;
       ^
C:/Users/Public/Projets/Test/main.cpp:36:20: error: 'cache' was not declared in this scope
     ResourceCache* cache = GetSubsystem<ResourceCache>();
                    ^
C:/Users/Public/Projets/Test/main.cpp:36:28: error: 'GetSubsystem' was not declared in this scope
     ResourceCache* cache = GetSubsystem<ResourceCache>();
                            ^
C:/Users/Public/Projets/Test/main.cpp:36:56: error: expected primary-expression before ')' token
     ResourceCache* cache = GetSubsystem<ResourceCache>();
                                                        ^
C:/Users/Public/Projets/Test/main.cpp:39:5: error: 'SharedPtr' was not declared in this scope
     SharedPtr<Text> helloText(new Text(context_));
     ^
C:/Users/Public/Projets/Test/main.cpp:39:5: note: suggested alternative:
In file included from ../URHO/Codelite/Include/Urho3D/Core/../Core/../Core/Variant.h:26:0,
                 from ../URHO/Codelite/Include/Urho3D/Core/../Core/Object.h:26,
                 from ../URHO/Codelite/Include/Urho3D/Core/CoreEvents.h:25,
                 from C:/Users/Public/Projets/Test/main.cpp:4:
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Ptr.h:34:26: note:   'Urho3D::SharedPtr'
 template <class T> class SharedPtr
                          ^
C:/Users/Public/Projets/Test/main.cpp:39:15: error: 'Text' was not declared in this scope
     SharedPtr<Text> helloText(new Text(context_));
               ^
C:/Users/Public/Projets/Test/main.cpp:39:15: note: suggested alternative:
In file included from C:/Users/Public/Projets/Test/main.cpp:9:0:
../URHO/Codelite/Include/Urho3D/UI/Text.h:73:18: note:   'Urho3D::Text'
 class URHO3D_API Text : public UIElement
                  ^
C:/Users/Public/Projets/Test/main.cpp:39:35: error: expected type-specifier before 'Text'
     SharedPtr<Text> helloText(new Text(context_));
                                   ^
C:/Users/Public/Projets/Test/main.cpp:39:49: error: 'helloText' was not declared in this scope
     SharedPtr<Text> helloText(new Text(context_));
                                                 ^
C:/Users/Public/Projets/Test/main.cpp:45:43: error: 'Font' was not declared in this scope
     helloText->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 30);
                                           ^
C:/Users/Public/Projets/Test/main.cpp:45:43: note: suggested alternative:
In file included from C:/Users/Public/Projets/Test/main.cpp:6:0:
../URHO/Codelite/Include/Urho3D/UI/Font.h:46:18: note:   'Urho3D::Font'
 class URHO3D_API Font : public Resource
                  ^
C:/Users/Public/Projets/Test/main.cpp:46:47: error: 'Color' was not declared in this scope
     helloText->SetColor(Color(0.0f, 1.0f, 0.0f));
                                               ^
C:/Users/Public/Projets/Test/main.cpp:46:47: note: suggested alternative:
In file included from ../URHO/Codelite/Include/Urho3D/Core/../Core/../Core/Variant.h:27:0,
                 from ../URHO/Codelite/Include/Urho3D/Core/../Core/Object.h:26,
                 from ../URHO/Codelite/Include/Urho3D/Core/CoreEvents.h:25,
                 from C:/Users/Public/Projets/Test/main.cpp:4:
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Math/Color.h:36:18: note:   'Urho3D::Color'
 class URHO3D_API Color
                  ^
C:/Users/Public/Projets/Test/main.cpp:49:39: error: 'HA_CENTER' was not declared in this scope
     helloText->SetHorizontalAlignment(HA_CENTER);
                                       ^
C:/Users/Public/Projets/Test/main.cpp:49:39: note: suggested alternative:
In file included from ../URHO/Codelite/Include/Urho3D/Input/../UI/../UI/BorderImage.h:26:0,
                 from ../URHO/Codelite/Include/Urho3D/Input/../UI/Cursor.h:27,
                 from ../URHO/Codelite/Include/Urho3D/Input/Input.h:30,
                 from C:/Users/Public/Projets/Test/main.cpp:7:
../URHO/Codelite/Include/Urho3D/Input/../UI/../UI/../UI/UIElement.h:37:5: note:   'HA_CENTER'
     HA_CENTER,
     ^
C:/Users/Public/Projets/Test/main.cpp:50:37: error: 'VA_CENTER' was not declared in this scope
     helloText->SetVerticalAlignment(VA_CENTER);
                                     ^
C:/Users/Public/Projets/Test/main.cpp:50:37: note: suggested alternative:
In file included from ../URHO/Codelite/Include/Urho3D/Input/../UI/../UI/BorderImage.h:26:0,
                 from ../URHO/Codelite/Include/Urho3D/Input/../UI/Cursor.h:27,
                 from ../URHO/Codelite/Include/Urho3D/Input/Input.h:30,
                 from C:/Users/Public/Projets/Test/main.cpp:7:
../URHO/Codelite/Include/Urho3D/Input/../UI/../UI/../UI/UIElement.h:45:5: note:   'VA_CENTER'
     VA_CENTER,
     ^
C:/Users/Public/Projets/Test/main.cpp:53:18: error: 'UI' was not declared in this scope
     GetSubsystem<UI>()->GetRoot()->AddChild(helloText);
                  ^
C:/Users/Public/Projets/Test/main.cpp:53:18: note: suggested alternative:
In file included from C:/Users/Public/Projets/Test/main.cpp:10:0:
../URHO/Codelite/Include/Urho3D/UI/UI.h:43:18: note:   'Urho3D::UI'
 class URHO3D_API UI : public Object
                  ^
C:/Users/Public/Projets/Test/main.cpp:53:22: error: expected primary-expression before ')' token
     GetSubsystem<UI>()->GetRoot()->AddChild(helloText);
                      ^
C:/Users/Public/Projets/Test/main.cpp: At global scope:
C:/Users/Public/Projets/Test/main.cpp:56:6: error: 'HelloWorld' has not been declared
 void HelloWorld::SubscribeToEvents()
      ^
C:/Users/Public/Projets/Test/main.cpp: In function 'void SubscribeToEvents()':
C:/Users/Public/Projets/Test/main.cpp:59:22: error: 'E_UPDATE' was not declared in this scope
     SubscribeToEvent(E_UPDATE, HANDLER(HelloWorld, HandleUpdate));
                      ^
C:/Users/Public/Projets/Test/main.cpp:59:22: note: suggested alternative:
In file included from ../URHO/Codelite/Include/Urho3D/Core/CoreEvents.h:25:0,
                 from C:/Users/Public/Projets/Test/main.cpp:4:
../URHO/Codelite/Include/Urho3D/Core/CoreEvents.h:38:7: note:   'Urho3D::E_UPDATE'
 EVENT(E_UPDATE, Update)
       ^
../URHO/Codelite/Include/Urho3D/Core/../Core/Object.h:287:67: note: in definition of macro 'EVENT'
 #define EVENT(eventID, eventName) static const Urho3D::StringHash eventID(#eventName); namespace eventName
                                                                   ^
C:/Users/Public/Projets/Test/main.cpp:59:40: error: 'HelloWorld' was not declared in this scope
     SubscribeToEvent(E_UPDATE, HANDLER(HelloWorld, HandleUpdate));
                                        ^
../URHO/Codelite/Include/Urho3D/Core/../Core/Object.h:291:68: note: in definition of macro 'HANDLER'
 #define HANDLER(className, function) (new Urho3D::EventHandlerImpl<className>(this, &className::function))
                                                                    ^
../URHO/Codelite/Include/Urho3D/Core/../Core/Object.h:291:77: error: template argument 1 is invalid
 #define HANDLER(className, function) (new Urho3D::EventHandlerImpl<className>(this, &className::function))
                                                                             ^
C:/Users/Public/Projets/Test/main.cpp:59:32: note: in expansion of macro 'HANDLER'
     SubscribeToEvent(E_UPDATE, HANDLER(HelloWorld, HandleUpdate));
                                ^
../URHO/Codelite/Include/Urho3D/Core/../Core/Object.h:291:79: error: invalid use of 'this' in non-member function
 #define HANDLER(className, function) (new Urho3D::EventHandlerImpl<className>(this, &className::function))
                                                                               ^
C:/Users/Public/Projets/Test/main.cpp:59:32: note: in expansion of macro 'HANDLER'
     SubscribeToEvent(E_UPDATE, HANDLER(HelloWorld, HandleUpdate));
                                ^
C:/Users/Public/Projets/Test/main.cpp:59:40: error: 'HelloWorld' is not a class or namespace
     SubscribeToEvent(E_UPDATE, HANDLER(HelloWorld, HandleUpdate));
                                        ^
../URHO/Codelite/Include/Urho3D/Core/../Core/Object.h:291:86: note: in definition of macro 'HANDLER'
 #define HANDLER(className, function) (new Urho3D::EventHandlerImpl<className>(this, &className::function))
                                                                                      ^
C:/Users/Public/Projets/Test/main.cpp:59:65: error: 'SubscribeToEvent' was not declared in this scope
     SubscribeToEvent(E_UPDATE, HANDLER(HelloWorld, HandleUpdate));
                                                                 ^
C:/Users/Public/Projets/Test/main.cpp: At global scope:
C:/Users/Public/Projets/Test/main.cpp:62:6: error: 'HelloWorld' has not been declared
 void HelloWorld::HandleUpdate(StringHash eventType, VariantMap& eventData)
      ^
C:/Users/Public/Projets/Test/main.cpp:62:31: error: variable or field 'HandleUpdate' declared void
 void HelloWorld::HandleUpdate(StringHash eventType, VariantMap& eventData)
                               ^
C:/Users/Public/Projets/Test/main.cpp:62:31: error: 'StringHash' was not declared in this scope
C:/Users/Public/Projets/Test/main.cpp:62:31: note: suggested alternative:
In file included from ../URHO/Codelite/Include/Urho3D/Core/../Core/../Core/Variant.h:31:0,
                 from ../URHO/Codelite/Include/Urho3D/Core/../Core/Object.h:26,
                 from ../URHO/Codelite/Include/Urho3D/Core/CoreEvents.h:25,
                 from C:/Users/Public/Projets/Test/main.cpp:4:
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Math/StringHash.h:31:18: note:   'Urho3D::StringHash'
 class URHO3D_API StringHash
                  ^
C:/Users/Public/Projets/Test/main.cpp:62:53: error: 'VariantMap' was not declared in this scope
 void HelloWorld::HandleUpdate(StringHash eventType, VariantMap& eventData)
                                                     ^
C:/Users/Public/Projets/Test/main.cpp:62:53: note: suggested alternative:
In file included from ../URHO/Codelite/Include/Urho3D/Core/../Core/Object.h:26:0,
                 from ../URHO/Codelite/Include/Urho3D/Core/CoreEvents.h:25,
                 from C:/Users/Public/Projets/Test/main.cpp:4:
../URHO/Codelite/Include/Urho3D/Core/../Core/../Core/Variant.h:109:38: note:   'Urho3D::VariantMap'
 typedef HashMap<StringHash, Variant> VariantMap;
                                      ^
C:/Users/Public/Projets/Test/main.cpp:62:65: error: 'eventData' was not declared in this scope
 void HelloWorld::HandleUpdate(StringHash eventType, VariantMap& eventData)
                                                                 ^
mingw32-make.exe[1]: *** [Debug/main.cpp.o] Error 1
mingw32-make.exe: *** [All] Error 2
Test.mk:97: recipe for target 'Debug/main.cpp.o' failed
mingw32-make.exe[1]: Leaving directory 'C:/Users/Public/Projets/Test'
Makefile:4: recipe for target 'All' failed
====33 errors, 38 warnings====
[/code]

From the docs, it tell to use CMAKE to prepare something for the compilation. I'm really confused now.

Is there a way to use the URHO3D lib without having to use CMAKE to make our own workspace/project? Is there a tutorial somewhere, where I could use it the way I'm used to? I just want to create a new C++ project and use the features of URHO3D, I don't want to "patch" the helloworld file example to add my stuff.

-------------------------

Bluemoon | 2017-01-02 01:09:12 UTC | #2

[quote]
1. set the path of the include files and the compiled library file (.a or .lib) for the used library, in the compiler settings.
2. set the name of the library to the linker setting.
3. Use the "hello world" example and try to compile.
[/quote]

You can definitely use Urho3D library like this on codelite. It works for me so it should work for you too. And yes too, you can "use the URHO3D lib without having to use CMAKE" . But first are you intentionally using pre-1.5 Urho3d ?  because from the build log the MACROs lack the "URHO3D_" prefix that are present in the current version. If this is by choice then no problem :smiley: 

From all indication it seems that your include file path was not added properly. If you are using v1.4 or v1.5 you only need to include these two paths for Urho3D 
"${urho3d-installation-dir}/include" and "${urho3d-installation-dir}/include/Urho3D/ThirdParty" . For example my installation directory is "C:/Urho3D" so I only include 
"C:/Urho3D/include" and " C:/Urho3D/include/Urho3D/ThirdParty" .

All you have to do next from here is to include the necessary Urho3D based preprocessors ( like URHO3D_PROFILING, URHO3D_LOGGING etc) , add the library path and the libraries. That's just it

-------------------------

christianclavet | 2017-01-02 01:09:13 UTC | #3

Thanks!

What are required pre-processor for the "hello world" example? I don't remember using this before. I'm using 1.5.

NOTE: I think I've been able to make it compile. Now I think the linker don't find something (I've set the path and the lib but it look like the project doesnt find it)
C:\WINDOWS\system32\cmd.exe /C C:/TDM-GCC-64/bin/mingw32-make.exe -j8 SHELL=cmd.exe -e -f  Makefile
[code]"----------Building project:[ Test - Debug ]----------"
mingw32-make.exe[1]: Entering directory 'C:/Users/Public/Projets/Test'
C:/TDM-GCC-64/bin/g++.exe  -c  "C:/Users/Public/Projets/Test/main.cpp" -g -O0 -Wall  -o ./Debug/main.cpp.o -I. -I../URHO/Codelite/Include -I../URHO/Codelite/Include/Audio -I../URHO/Codelite/Include/Container -I../URHO/Codelite/Include/Core -I../URHO/Codelite/Include/Database -I../URHO/Codelite/Include/Engine -I../URHO/Codelite/Include/Graphics -I../URHO/Codelite/Include/Input -I../URHO/Codelite/Include/IO -I../URHO/Codelite/Include/LuaScript -I../URHO/Codelite/Include/Math -I../URHO/Codelite/Include/Navigation -I../URHO/Codelite/Include/Network -I../URHO/Codelite/Include/Physics -I../URHO/Codelite/Include/Resource -I../URHO/Codelite/Include/Scene -I../URHO/Codelite/Include/Script -I../URHO/Codelite/Include/ThirdParty -I../URHO/Codelite/Include/ThirdParty/AngelScript -I../URHO/Codelite/Include/ThirdParty/Box2D -I../URHO/Codelite/Include/ThirdParty/Bullet -I../URHO/Codelite/Include/ThirdParty/Civetweb -I../URHO/Codelite/Include/ThirdParty/Detour -I../URHO/Codelite/Include/ThirdParty/DetourCrowd -I../URHO/Codelite/Include/ThirdParty/DetourTileCache -I../URHO/Codelite/Include/ThirdParty/freetype -I../URHO/Codelite/Include/ThirdParty/GLEW -I../URHO/Codelite/Include/ThirdParty/JO -I../URHO/Codelite/Include/ThirdParty/kNet -I../URHO/Codelite/Include/ThirdParty/libCpuId -I../URHO/Codelite/Include/ThirdParty/Lua -I../URHO/Codelite/Include/ThirdParty/LZ4 -I../URHO/Codelite/Include/ThirdParty/PugiXml -I../URHO/Codelite/Include/ThirdParty/rapidjson -I../URHO/Codelite/Include/ThirdParty/Recast -I../URHO/Codelite/Include/ThirdParty/SDL -I../URHO/Codelite/Include/ThirdParty/StanHull -I../URHO/Codelite/Include/ThirdParty/STB -I../URHO/Codelite/Include/ThirdParty/toluapp -I../URHO/Codelite/Include/UI -I../URHO/Codelite/Include/Urho2D
C:/Users/Public/Projets/Test/main.cpp:23:9: warning: #pragma once in main file
 #pragma once
         ^
C:/TDM-GCC-64/bin/g++.exe -o ./Debug/Test @"Test.txt" -L../URHO/Codelite/lib  -lUrho3D
./Debug/main.cpp.o: In function `Sample::Sample(Urho3D::Context*)':
C:/Users/Public/Projets/Test/Sample.inl:50: undefined reference to `__imp__ZN6Urho3D11ApplicationC2EPNS_7ContextE'
./Debug/main.cpp.o: In function `Sample::Setup()':
C:/Users/Public/Projets/Test/Sample.inl:57: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:/Users/Public/Projets/Test/Sample.inl:58: undefined reference to `__imp__ZNK6Urho3D10FileSystem20GetAppPreferencesDirERKNS_6StringES3_'
C:/Users/Public/Projets/Test/Sample.inl:58: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:/Users/Public/Projets/Test/Sample.inl:59: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:/Users/Public/Projets/Test/Sample.inl:60: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/main.cpp.o: In function `Sample::Start()':
C:/Users/Public/Projets/Test/Sample.inl:65: undefined reference to `__imp__ZN6Urho3D11GetPlatformEv'
C:/Users/Public/Projets/Test/Sample.inl:65: undefined reference to `__imp__ZN6Urho3D11GetPlatformEv'
C:/Users/Public/Projets/Test/Sample.inl:70: undefined reference to `__imp__ZN6Urho3D6Object16SubscribeToEventENS_10StringHashEPNS_12EventHandlerE'
C:/Users/Public/Projets/Test/Sample.inl:82: undefined reference to `__imp__ZN6Urho3D6Object16SubscribeToEventENS_10StringHashEPNS_12EventHandlerE'
C:/Users/Public/Projets/Test/Sample.inl:84: undefined reference to `__imp__ZN6Urho3D6Object16SubscribeToEventENS_10StringHashEPNS_12EventHandlerE'
./Debug/main.cpp.o: In function `Sample::Stop()':
C:/Users/Public/Projets/Test/Sample.inl:89: undefined reference to `__imp__ZN6Urho3D6Engine13DumpResourcesEb'
./Debug/main.cpp.o: In function `Sample::InitTouchInput()':
C:/Users/Public/Projets/Test/Sample.inl:103: undefined reference to `__imp__ZN6Urho3D7XMLFileC1EPNS_7ContextE'
C:/Users/Public/Projets/Test/Sample.inl:104: undefined reference to `__imp__ZN6Urho3D7XMLFile10FromStringERKNS_6StringE'
C:/Users/Public/Projets/Test/Sample.inl:105: undefined reference to `__imp__ZN6Urho3D7XMLFile5PatchEPS0_'
C:/Users/Public/Projets/Test/Sample.inl:107: undefined reference to `__imp__ZN6Urho3D5Input17AddScreenJoystickEPNS_7XMLFileES2_'
C:/Users/Public/Projets/Test/Sample.inl:108: undefined reference to `__imp__ZN6Urho3D5Input24SetScreenJoystickVisibleEib'
./Debug/main.cpp.o: In function `Sample::SetLogoVisible(bool)':
C:/Users/Public/Projets/Test/Sample.inl:114: undefined reference to `__imp__ZN6Urho3D9UIElement10SetVisibleEb'
./Debug/main.cpp.o: In function `Sample::CreateLogo()':
C:/Users/Public/Projets/Test/Sample.inl:127: undefined reference to `__imp__ZN6Urho3D6String5EMPTYE'
C:/Users/Public/Projets/Test/Sample.inl:130: undefined reference to `__imp__ZN6Urho3D6Sprite10SetTextureEPNS_7TextureE'
C:/Users/Public/Projets/Test/Sample.inl:136: undefined reference to `__imp__ZN6Urho3D6Sprite8SetScaleEf'
C:/Users/Public/Projets/Test/Sample.inl:139: undefined reference to `__imp__ZN6Urho3D9UIElement7SetSizeEii'
C:/Users/Public/Projets/Test/Sample.inl:142: undefined reference to `__imp__ZN6Urho3D6Sprite10SetHotSpotEii'
C:/Users/Public/Projets/Test/Sample.inl:145: undefined reference to `__imp__ZN6Urho3D9UIElement12SetAlignmentENS_19HorizontalAlignmentENS_17VerticalAlignmentE'
C:/Users/Public/Projets/Test/Sample.inl:148: undefined reference to `__imp__ZN6Urho3D9UIElement10SetOpacityEf'
C:/Users/Public/Projets/Test/Sample.inl:151: undefined reference to `__imp__ZN6Urho3D9UIElement11SetPriorityEi'
./Debug/main.cpp.o: In function `Sample::SetWindowTitleAndIcon()':
C:/Users/Public/Projets/Test/Sample.inl:159: undefined reference to `__imp__ZN6Urho3D8Graphics13SetWindowIconEPNS_5ImageE'
C:/Users/Public/Projets/Test/Sample.inl:160: undefined reference to `__imp__ZN6Urho3D8Graphics14SetWindowTitleERKNS_6StringE'
./Debug/main.cpp.o: In function `Sample::CreateConsoleAndDebugHud()':
C:/Users/Public/Projets/Test/Sample.inl:170: undefined reference to `__imp__ZN6Urho3D6Engine13CreateConsoleEv'
C:/Users/Public/Projets/Test/Sample.inl:171: undefined reference to `__imp__ZN6Urho3D7Console15SetDefaultStyleEPNS_7XMLFileE'
C:/Users/Public/Projets/Test/Sample.inl:172: undefined reference to `__imp__ZN6Urho3D9UIElement10SetOpacityEf'
C:/Users/Public/Projets/Test/Sample.inl:175: undefined reference to `__imp__ZN6Urho3D6Engine14CreateDebugHudEv'
C:/Users/Public/Projets/Test/Sample.inl:176: undefined reference to `__imp__ZN6Urho3D8DebugHud15SetDefaultStyleEPNS_7XMLFileE'
./Debug/main.cpp.o: In function `Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
C:/Users/Public/Projets/Test/Sample.inl:189: undefined reference to `__imp__ZNK6Urho3D7Console9IsVisibleEv'
C:/Users/Public/Projets/Test/Sample.inl:190: undefined reference to `__imp__ZN6Urho3D7Console10SetVisibleEb'
C:/Users/Public/Projets/Test/Sample.inl:192: undefined reference to `__imp__ZN6Urho3D6Engine4ExitEv'
C:/Users/Public/Projets/Test/Sample.inl:197: undefined reference to `__imp__ZN6Urho3D7Console6ToggleEv'
C:/Users/Public/Projets/Test/Sample.inl:201: undefined reference to `__imp__ZN6Urho3D8DebugHud9ToggleAllEv'
C:/Users/Public/Projets/Test/Sample.inl:218: undefined reference to `__imp__ZN6Urho3D5Input17AddScreenJoystickEPNS_7XMLFileES2_'
C:/Users/Public/Projets/Test/Sample.inl:221: undefined reference to `__imp__ZN6Urho3D5Input24SetScreenJoystickVisibleEib'
C:/Users/Public/Projets/Test/Sample.inl:231: undefined reference to `__imp__ZN6Urho3D8Renderer17SetTextureQualityEi'
C:/Users/Public/Projets/Test/Sample.inl:241: undefined reference to `__imp__ZN6Urho3D8Renderer18SetMaterialQualityEi'
C:/Users/Public/Projets/Test/Sample.inl:246: undefined reference to `__imp__ZN6Urho3D8Renderer19SetSpecularLightingEb'
C:/Users/Public/Projets/Test/Sample.inl:250: undefined reference to `__imp__ZN6Urho3D8Renderer14SetDrawShadowsEb'
C:/Users/Public/Projets/Test/Sample.inl:259: undefined reference to `__imp__ZN6Urho3D8Renderer16SetShadowMapSizeEi'
C:/Users/Public/Projets/Test/Sample.inl:269: undefined reference to `__imp__ZN6Urho3D8Renderer16SetShadowQualityEi'
C:/Users/Public/Projets/Test/Sample.inl:277: undefined reference to `__imp__ZN6Urho3D8Renderer23SetMaxOccluderTrianglesEi'
C:/Users/Public/Projets/Test/Sample.inl:282: undefined reference to `__imp__ZN6Urho3D8Renderer20SetDynamicInstancingEb'
C:/Users/Public/Projets/Test/Sample.inl:288: undefined reference to `__imp__ZN6Urho3D5ImageC1EPNS_7ContextE'
C:/Users/Public/Projets/Test/Sample.inl:289: undefined reference to `__imp__ZN6Urho3D8Graphics14TakeScreenShotERNS_5ImageE'
C:/Users/Public/Projets/Test/Sample.inl:292: undefined reference to `__imp__ZN6Urho3D4Time12GetTimeStampEv'
C:/Users/Public/Projets/Test/Sample.inl:292: undefined reference to `__imp__ZNK6Urho3D6String8ReplacedEccb'
C:/Users/Public/Projets/Test/Sample.inl:292: undefined reference to `__imp__ZNK6Urho3D6String8ReplacedEccb'
C:/Users/Public/Projets/Test/Sample.inl:292: undefined reference to `__imp__ZNK6Urho3D6String8ReplacedEccb'
C:/Users/Public/Projets/Test/Sample.inl:291: undefined reference to `__imp__ZNK6Urho3D10FileSystem13GetProgramDirEv'
C:/Users/Public/Projets/Test/Sample.inl:292: undefined reference to `__imp__ZNK6Urho3D5Image7SavePNGERKNS_6StringE'
C:/Users/Public/Projets/Test/Sample.inl:288: undefined reference to `__imp__ZN6Urho3D5ImageD1Ev'
C:/Users/Public/Projets/Test/Sample.inl:288: undefined reference to `__imp__ZN6Urho3D5ImageD1Ev'
./Debug/main.cpp.o: In function `Sample::HandleSceneUpdate(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
C:/Users/Public/Projets/Test/Sample.inl:305: undefined reference to `__imp__ZNK6Urho3D5Input8GetTouchEj'
C:/Users/Public/Projets/Test/Sample.inl:319: undefined reference to `__imp__ZN6Urho3D4Node11SetRotationERKNS_10QuaternionE'
C:/Users/Public/Projets/Test/Sample.inl:326: undefined reference to `__imp__ZN6Urho3D9UIElement11SetPositionERKNS_10IntVector2E'
./Debug/main.cpp.o: In function `Sample::HandleTouchBegin(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
C:/Users/Public/Projets/Test/Sample.inl:337: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:/Users/Public/Projets/Test/Sample.inl:337: undefined reference to `__imp__ZN6Urho3D6Object20UnsubscribeFromEventENS_10StringHashE'
./Debug/main.cpp.o: In function `__static_initialization_and_destruction_0':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Input/../Input/InputEvents.h:36: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Input/../Input/InputEvents.h:38: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Input/../Input/InputEvents.h:39: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Input/../Input/InputEvents.h:40: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Input/../Input/InputEvents.h:44: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/main.cpp.o:C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Input/../Input/InputEvents.h:46: more undefined references to `__imp__ZN6Urho3D10StringHashC1EPKc' follow
./Debug/main.cpp.o: In function `Urho3D::String::String()':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Str.h:50: undefined reference to `__imp__ZN6Urho3D6String7endZeroE'
./Debug/main.cpp.o: In function `Urho3D::String::String(Urho3D::String const&)':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Str.h:58: undefined reference to `__imp__ZN6Urho3D6String7endZeroE'
./Debug/main.cpp.o: In function `Urho3D::String::String(char const*)':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Str.h:67: undefined reference to `__imp__ZN6Urho3D6String7endZeroE'
./Debug/main.cpp.o: In function `Urho3D::String::operator=(Urho3D::String const&)':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Str.h:158: undefined reference to `__imp__ZN6Urho3D6String6ResizeEj'
./Debug/main.cpp.o: In function `Urho3D::String::operator=(char const*)':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Str.h:168: undefined reference to `__imp__ZN6Urho3D6String6ResizeEj'
./Debug/main.cpp.o: In function `Urho3D::String::operator+(Urho3D::String const&) const':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Str.h:233: undefined reference to `__imp__ZN6Urho3D6String6ResizeEj'
./Debug/main.cpp.o: In function `Urho3D::String::operator+(char const*) const':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Str.h:245: undefined reference to `__imp__ZN6Urho3D6String6ResizeEj'
./Debug/main.cpp.o: In function `Urho3D::Quaternion::Quaternion(float, float, float)':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Math/Quaternion.h:85: undefined reference to `__imp__ZN6Urho3D10Quaternion15FromEulerAnglesEfff'
./Debug/main.cpp.o: In function `Urho3D::Variant::Variant(Urho3D::Variant const&)':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Core/Variant.h:415: undefined reference to `__imp__ZN6Urho3D7VariantaSERKS0_'
./Debug/main.cpp.o: In function `Urho3D::Variant::~Variant()':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Core/Variant.h:421: undefined reference to `__imp__ZN6Urho3D7Variant7SetTypeENS_11VariantTypeE'
./Debug/main.cpp.o: In function `Urho3D::Variant::operator=(bool)':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Core/Variant.h:460: undefined reference to `__imp__ZN6Urho3D7Variant7SetTypeENS_11VariantTypeE'
./Debug/main.cpp.o: In function `Urho3D::Variant::operator=(Urho3D::String const&)':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Core/Variant.h:524: undefined reference to `__imp__ZN6Urho3D7Variant7SetTypeENS_11VariantTypeE'
./Debug/main.cpp.o: In function `Urho3D::Object::GetBaseTypeStatic()':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/../Core/../Core/Object.h:50: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/main.cpp.o: In function `Urho3D::EventHandler::EventHandler(Urho3D::Object*)':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/../Core/../Core/Object.h:194: undefined reference to `__imp__ZTVN6Urho3D12EventHandlerE'
./Debug/main.cpp.o: In function `Urho3D::EventHandler::EventHandler(Urho3D::Object*, void*)':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/../Core/../Core/Object.h:203: undefined reference to `__imp__ZTVN6Urho3D12EventHandlerE'
./Debug/main.cpp.o: In function `Urho3D::EventHandler::~EventHandler()':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/../Core/../Core/Object.h:209: undefined reference to `__imp__ZTVN6Urho3D12EventHandlerE'
./Debug/main.cpp.o: In function `Urho3D::Application::GetTypeStatic()':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/Application.h:37: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/main.cpp.o: In function `Sample::GetTypeStatic()':
C:/Users/Public/Projets/Test/Sample.h:54: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/main.cpp.o: In function `Sample::GetScreenJoystickPatchString() const':
C:/Users/Public/Projets/Test/Sample.h:69: undefined reference to `__imp__ZN6Urho3D6String5EMPTYE'
./Debug/main.cpp.o: In function `Urho3D::Camera::GetTypeStatic()':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Graphics/Camera.h:46: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/main.cpp.o: In function `Urho3D::Console::GetTypeStatic()':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/Console.h:44: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/main.cpp.o: In function `Urho3D::Image::GetTypeStatic()':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/UI/../Resource/Image.h:92: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/main.cpp.o: In function `Urho3D::XMLFile::GetTypeStatic()':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/UI/../UI/../UI/../Resource/XMLFile.h:43: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/main.cpp.o: In function `Urho3D::DebugHud::GetTypeStatic()':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/DebugHud.h:45: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/main.cpp.o:C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/IO/FileSystem.h:44: more undefined references to `__imp__ZN6Urho3D10StringHashC1EPKc' follow
./Debug/main.cpp.o: In function `Urho3D::Application::~Application()':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/Application.h:35: undefined reference to `__imp__ZTVN6Urho3D11ApplicationE'
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/Application.h:35: undefined reference to `__imp__ZN6Urho3D6ObjectD2Ev'
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/Application.h:35: undefined reference to `__imp__ZN6Urho3D6ObjectD2Ev'
./Debug/main.cpp.o: In function `Urho3D::Application::~Application()':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/Application.h:35: undefined reference to `__imp__ZTVN6Urho3D11ApplicationE'
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/Application.h:35: undefined reference to `__imp__ZN6Urho3D6ObjectD2Ev'
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/Application.h:35: undefined reference to `__imp__ZN6Urho3D6ObjectD2Ev'
./Debug/main.cpp.o: In function `Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>::~HashMap()':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/HashMap.h:246: undefined reference to `__imp__ZN6Urho3D21AllocatorUninitializeEPNS_14AllocatorBlockE'
./Debug/main.cpp.o: In function `Urho3D::FileSystem* Urho3D::Object::GetSubsystem<Urho3D::FileSystem>() const':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/../Core/../Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/main.cpp.o: In function `Urho3D::Input* Urho3D::Object::GetSubsystem<Urho3D::Input>() const':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/../Core/../Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/main.cpp.o: In function `Urho3D::ResourceCache* Urho3D::Object::GetSubsystem<Urho3D::ResourceCache>() const':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/../Core/../Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/main.cpp.o: In function `Urho3D::XMLFile* Urho3D::ResourceCache::GetResource<Urho3D::XMLFile>(Urho3D::String const&, bool)':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Resource/ResourceCache.h:257: undefined reference to `__imp__ZN6Urho3D13ResourceCache11GetResourceENS_10StringHashERKNS_6StringEb'
./Debug/main.cpp.o: In function `Urho3D::Texture2D* Urho3D::ResourceCache::GetResource<Urho3D::Texture2D>(Urho3D::String const&, bool)':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Resource/ResourceCache.h:257: undefined reference to `__imp__ZN6Urho3D13ResourceCache11GetResourceENS_10StringHashERKNS_6StringEb'
./Debug/main.cpp.o: In function `Urho3D::UI* Urho3D::Object::GetSubsystem<Urho3D::UI>() const':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/../Core/../Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/main.cpp.o: In function `Urho3D::Sprite* Urho3D::UIElement::CreateChild<Urho3D::Sprite>(Urho3D::String const&, unsigned int)':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/UI/../UI/../UI/UIElement.h:713: undefined reference to `__imp__ZN6Urho3D9UIElement11CreateChildENS_10StringHashERKNS_6StringEj'
./Debug/main.cpp.o: In function `Urho3D::Graphics* Urho3D::Object::GetSubsystem<Urho3D::Graphics>() const':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/../Core/../Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/main.cpp.o: In function `Urho3D::Image* Urho3D::ResourceCache::GetResource<Urho3D::Image>(Urho3D::String const&, bool)':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Resource/ResourceCache.h:257: undefined reference to `__imp__ZN6Urho3D13ResourceCache11GetResourceENS_10StringHashERKNS_6StringEb'
./Debug/main.cpp.o: In function `Urho3D::Console* Urho3D::Object::GetSubsystem<Urho3D::Console>() const':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/../Core/../Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/main.cpp.o: In function `Urho3D::DebugHud* Urho3D::Object::GetSubsystem<Urho3D::DebugHud>() const':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/../Core/../Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/main.cpp.o: In function `Urho3D::Renderer* Urho3D::Object::GetSubsystem<Urho3D::Renderer>() const':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Engine/../Core/../Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/main.cpp.o: In function `Urho3D::Camera* Urho3D::Node::GetComponent<Urho3D::Camera>(bool) const':
C:\Users\Public\Projets\Test/../URHO/Codelite/Include/Urho3D/Scene/../Scene/Node.h:654: undefined reference to `__imp__ZNK6Urho3D4Node12GetComponentENS_10StringHashEb'
./Debug/main.cpp.o: In function `Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>::Clear()':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/HashMap.h:428: undefined reference to `__imp__ZN6Urho3D8HashBase9ResetPtrsEv'
./Debug/main.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Engine>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/main.cpp.o: In function `Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>::FreeNode(Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>::Node*)':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/HashMap.h:699: undefined reference to `__imp__ZN6Urho3D13AllocatorFreeEPNS_14AllocatorBlockEPv'
./Debug/main.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Sprite>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/main.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Scene>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/main.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Node>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/main.cpp.o: In function `Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>::InsertNode(Urho3D::StringHash const&, Urho3D::Variant const&, bool)':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/HashMap.h:602: undefined reference to `__imp__ZN6Urho3D8HashBase15AllocateBucketsEjj'
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/HashMap.h:614: undefined reference to `__imp__ZN6Urho3D7VariantaSERKS0_'
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/HashMap.h:626: undefined reference to `__imp__ZN6Urho3D8HashBase15AllocateBucketsEjj'
./Debug/main.cpp.o: In function `Urho3D::SharedPtr<Urho3D::XMLFile>::AddRef()':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Ptr.h:182: undefined reference to `__imp__ZN6Urho3D10RefCounted6AddRefEv'
./Debug/main.cpp.o: In function `Urho3D::SharedPtr<Urho3D::XMLFile>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/main.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Sprite>::AddRef()':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/Ptr.h:182: undefined reference to `__imp__ZN6Urho3D10RefCounted6AddRefEv'
./Debug/main.cpp.o: In function `Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>::ReserveNode(Urho3D::StringHash const&, Urho3D::Variant const&)':
C:/Users/Public/Projets/URHO/Codelite/Include/Urho3D/Container/HashMap.h:690: undefined reference to `__imp__ZN6Urho3D16AllocatorReserveEPNS_14AllocatorBlockE'
../URHO/Codelite/lib/libUrho3D.a(Timer.cpp.obj):Timer.cpp:(.text+0x1c): undefined reference to `__imp_timeEndPeriod'
../URHO/Codelite/lib/libUrho3D.a(Timer.cpp.obj):Timer.cpp:(.text+0x8a): undefined reference to `__imp_timeGetTime'
../URHO/Codelite/lib/libUrho3D.a(Timer.cpp.obj):Timer.cpp:(.text+0x11a): undefined reference to `__imp_timeBeginPeriod'
../URHO/Codelite/lib/libUrho3D.a(Timer.cpp.obj):Timer.cpp:(.text+0x126): undefined reference to `__imp_timeEndPeriod'
../URHO/Codelite/lib/libUrho3D.a(Timer.cpp.obj):Timer.cpp:(.text+0x13a): undefined reference to `__imp_timeGetTime'
../URHO/Codelite/lib/libUrho3D.a(Timer.cpp.obj):Timer.cpp:(.text+0x163): undefined reference to `__imp_timeGetTime'
../URHO/Codelite/lib/libUrho3D.a(Timer.cpp.obj):Timer.cpp:(.text+0x38a): undefined reference to `__imp_timeGetTime'
../URHO/Codelite/lib/libUrho3D.a(Timer.cpp.obj):Timer.cpp:(.text+0x3ad): undefined reference to `__imp_timeGetTime'
../URHO/Codelite/lib/libUrho3D.a(Timer.cpp.obj):Timer.cpp:(.text+0x3da): undefined reference to `__imp_timeGetTime'
../URHO/Codelite/lib/libUrho3D.a(Timer.cpp.obj):Timer.cpp:(.text+0x444): more undefined references to `__imp_timeGetTime' follow
../URHO/Codelite/lib/libUrho3D.a(SDL_windowswindow.c.obj):SDL_windowswindow.c:(.text+0xa4f): undefined reference to `__imp_CreateDCW'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowswindow.c.obj):SDL_windowswindow.c:(.text+0xa68): undefined reference to `__imp_SetDeviceGammaRamp'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowswindow.c.obj):SDL_windowswindow.c:(.text+0xa77): undefined reference to `__imp_DeleteDC'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowswindow.c.obj):SDL_windowswindow.c:(.text+0xabf): undefined reference to `__imp_CreateDCW'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowswindow.c.obj):SDL_windowswindow.c:(.text+0xad8): undefined reference to `__imp_GetDeviceGammaRamp'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowswindow.c.obj):SDL_windowswindow.c:(.text+0xae7): undefined reference to `__imp_DeleteDC'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsshape.c.obj):SDL_windowsshape.c:(.text+0x41): undefined reference to `__imp_CreateRectRgn'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsshape.c.obj):SDL_windowsshape.c:(.text+0x5e): undefined reference to `__imp_CombineRgn'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsshape.c.obj):SDL_windowsshape.c:(.text+0x6f): undefined reference to `__imp_DeleteObject'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsopengl.c.obj):SDL_windowsopengl.c:(.text+0x1a4): undefined reference to `__imp_ChoosePixelFormat'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsopengl.c.obj):SDL_windowsopengl.c:(.text+0x1b2): undefined reference to `__imp_SetPixelFormat'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsopengl.c.obj):SDL_windowsopengl.c:(.text+0x4f5): undefined reference to `__imp_DescribePixelFormat'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsopengl.c.obj):SDL_windowsopengl.c:(.text+0x76b): undefined reference to `__imp_SetPixelFormat'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsopengl.c.obj):SDL_windowsopengl.c:(.text+0xa7f): undefined reference to `__imp_ChoosePixelFormat'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsopengl.c.obj):SDL_windowsopengl.c:(.text+0xa8d): undefined reference to `__imp_SetPixelFormat'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsopengl.c.obj):SDL_windowsopengl.c:(.text+0x102e): undefined reference to `__imp_SwapBuffers'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsopengl.c.obj):SDL_windowsopengl.c:(.text+0x1098): undefined reference to `__imp_GetPixelFormat'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsopengl.c.obj):SDL_windowsopengl.c:(.text+0x10be): undefined reference to `__imp_DescribePixelFormat'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsopengl.c.obj):SDL_windowsopengl.c:(.text+0x10cc): undefined reference to `__imp_SetPixelFormat'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmouse.c.obj):SDL_windowsmouse.c:(.text+0x2e8): undefined reference to `__imp_CreateDIBSection'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmouse.c.obj):SDL_windowsmouse.c:(.text+0x30a): undefined reference to `__imp_CreateBitmap'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmouse.c.obj):SDL_windowsmouse.c:(.text+0x354): undefined reference to `__imp_DeleteObject'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmodes.c.obj):SDL_windowsmodes.c:(.text+0x1cd): undefined reference to `__imp_CreateDCW'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmodes.c.obj):SDL_windowsmodes.c:(.text+0x1e0): undefined reference to `__imp_GetDeviceCaps'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmodes.c.obj):SDL_windowsmodes.c:(.text+0x27d): undefined reference to `__imp_CreateCompatibleBitmap'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmodes.c.obj):SDL_windowsmodes.c:(.text+0x296): undefined reference to `__imp_GetDIBits'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmodes.c.obj):SDL_windowsmodes.c:(.text+0x2e0): undefined reference to `__imp_DeleteObject'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmodes.c.obj):SDL_windowsmodes.c:(.text+0x2e9): undefined reference to `__imp_DeleteDC'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmessagebox.c.obj):SDL_windowsmessagebox.c:(.text+0x35b): undefined reference to `__imp_CreateCompatibleDC'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmessagebox.c.obj):SDL_windowsmessagebox.c:(.text+0x44b): undefined reference to `__imp_CreateFontIndirectW'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmessagebox.c.obj):SDL_windowsmessagebox.c:(.text+0x457): undefined reference to `__imp_SelectObject'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmessagebox.c.obj):SDL_windowsmessagebox.c:(.text+0x463): undefined reference to `__imp_GetTextMetricsW'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmessagebox.c.obj):SDL_windowsmessagebox.c:(.text+0x4e7): undefined reference to `__imp_DeleteDC'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsmessagebox.c.obj):SDL_windowsmessagebox.c:(.text+0x650): undefined reference to `__imp_GetDeviceCaps'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0xf6): undefined reference to `ImmGetIMEFileNameA'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x144): undefined reference to `ImmGetContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x167): undefined reference to `ImmReleaseContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x1d4): undefined reference to `ImmGetCompositionStringW'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x1ec): undefined reference to `ImmGetCompositionStringW'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x462): undefined reference to `ImmGetIMEFileNameA'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x579): undefined reference to `GetFileVersionInfoSizeA'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x5a5): undefined reference to `GetFileVersionInfoA'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x5cf): undefined reference to `VerQueryValueA'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x87c): undefined reference to `__imp_SysFreeString'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0xa0e): undefined reference to `ImmGetContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0xa30): undefined reference to `ImmNotifyIME'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0xa4d): undefined reference to `ImmNotifyIME'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0xa59): undefined reference to `ImmReleaseContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0xa9a): undefined reference to `ImmSetCompositionStringW'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0xc53): undefined reference to `ImmAssociateContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0xca3): undefined reference to `__imp_CoCreateInstance'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0xd6d): undefined reference to `ImmGetContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0xd7c): undefined reference to `ImmReleaseContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0xde8): undefined reference to `__imp_CoCreateInstance'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x12dd): undefined reference to `ImmAssociateContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x148a): undefined reference to `ImmAssociateContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x1626): undefined reference to `ImmGetContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x1672): undefined reference to `ImmReleaseContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x17a3): undefined reference to `ImmGetContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x17c4): undefined reference to `ImmGetCandidateListW'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x17d9): undefined reference to `ImmReleaseContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x186e): undefined reference to `ImmAssociateContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x187b): undefined reference to `ImmAssociateContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x18ed): undefined reference to `ImmGetContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x1988): undefined reference to `ImmReleaseContext'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x19d4): undefined reference to `ImmGetCandidateListW'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x1d46): undefined reference to `__imp_SysFreeString'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x1e3b): undefined reference to `__imp_SysFreeString'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x1fe4): undefined reference to `__imp_CreateCompatibleDC'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x1ffc): undefined reference to `__imp_DeleteDC'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x203e): undefined reference to `__imp_CreatePen'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x2060): undefined reference to `__imp_CreateSolidBrush'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x2148): undefined reference to `__imp_CreateFontW'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x214f): undefined reference to `__imp_SetBkMode'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x2173): undefined reference to `__imp_SelectObject'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x2211): undefined reference to `__imp_GetTextExtentPoint32W'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x22fd): undefined reference to `__imp_CreateDIBSection'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x236a): undefined reference to `__imp_Rectangle'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x23a1): undefined reference to `__imp_SetTextColor'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x252b): undefined reference to `__imp_ExtTextOutW'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x2644): undefined reference to `__imp_DeleteObject'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowskeyboard.c.obj):SDL_windowskeyboard.c:(.text+0x2655): undefined reference to `__imp_DeleteObject'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsframebuffer.c.obj):SDL_windowsframebuffer.c:(.text+0x35): undefined reference to `__imp_DeleteDC'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsframebuffer.c.obj):SDL_windowsframebuffer.c:(.text+0x40): undefined reference to `__imp_DeleteObject'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsframebuffer.c.obj):SDL_windowsframebuffer.c:(.text+0x80): undefined reference to `__imp_CreateCompatibleBitmap'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsframebuffer.c.obj):SDL_windowsframebuffer.c:(.text+0x97): undefined reference to `__imp_GetDIBits'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsframebuffer.c.obj):SDL_windowsframebuffer.c:(.text+0x162): undefined reference to `__imp_CreateCompatibleDC'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsframebuffer.c.obj):SDL_windowsframebuffer.c:(.text+0x18c): undefined reference to `__imp_CreateDIBSection'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsframebuffer.c.obj):SDL_windowsframebuffer.c:(.text+0x1af): undefined reference to `__imp_SelectObject'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsframebuffer.c.obj):SDL_windowsframebuffer.c:(.text+0x2b2): undefined reference to `__imp_BitBlt'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsframebuffer.c.obj):SDL_windowsframebuffer.c:(.text+0x2dc): undefined reference to `__imp_DeleteDC'
../URHO/Codelite/lib/libUrho3D.a(SDL_windowsframebuffer.c.obj):SDL_windowsframebuffer.c:(.text+0x2f3): undefined reference to `__imp_DeleteObject'
../URHO/Codelite/lib/libUrho3D.a(SDL_systimer.c.obj):SDL_systimer.c:(.text+0x2f): undefined reference to `__imp_timeBeginPeriod'
../URHO/Codelite/lib/libUrho3D.a(SDL_systimer.c.obj):SDL_systimer.c:(.text+0x35): undefined reference to `__imp_timeEndPeriod'
../URHO/Codelite/lib/libUrho3D.a(SDL_systimer.c.obj):SDL_systimer.c:(.text+0xd5): undefined reference to `__imp_timeGetTime'
../URHO/Codelite/lib/libUrho3D.a(SDL_systimer.c.obj):SDL_systimer.c:(.text+0x17a): undefined reference to `__imp_timeGetTime'
../URHO/Codelite/lib/libUrho3D.a(SDL_windows.c.obj):SDL_windows.c:(.text+0xdf): undefined reference to `__imp_CoInitializeEx'
../URHO/Codelite/lib/libUrho3D.a(SDL_windows.c.obj):SDL_windows.c:(.text+0x113): undefined reference to `__imp_CoUninitialize'
../URHO/Codelite/lib/libUrho3D.a(SDL_dxjoystick.c.obj):SDL_dxjoystick.c:(.text+0x21a0): undefined reference to `__imp_CoCreateInstance'
../URHO/Codelite/lib/libUrho3D.a(SDL_syshaptic.c.obj):SDL_syshaptic.c:(.text+0x1c42): undefined reference to `__imp_CoCreateInstance'
C:/TDM-GCC-64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.0/../../../../x86_64-w64-mingw32/lib/../lib/libmingw32.a(lib64_libmingw32_a-crt0_c.o): In function `main':
C:/crossdev/src/mingw-w64-v4-git/mingw-w64-crt/crt/crt0_c.c:18: undefined reference to `WinMain'
collect2.exe: error: ld returned 1 exit status
mingw32-make.exe[1]: *** [Debug/Test] Error 1
mingw32-make.exe: *** [All] Error 2
Test.mk:78: recipe for target 'Debug/Test' failed
mingw32-make.exe[1]: Leaving directory 'C:/Users/Public/Projets/Test'
Makefile:4: recipe for target 'All' failed
====238 errors, 1 warnings====[/code]

-------------------------

Bluemoon | 2017-01-02 01:09:13 UTC | #4

Generally the preprocessors are based on your build configuration; like if network component was built or if you are using opengl for rendering. The preprocessors for my current build are
[code]
URHO3D_FILEWATCHER
URHO3D_PROFILING
URHO3D_LOGGING
URHO3D_THREADING
URHO3D_STATIC_DEFINE
URHO3D_ANGELSCRIPT
URHO3D_NAVIGATION
URHO3D_NETWORK
URHO3D_PHYSICS
URHO3D_URHO2D
URHO3D_DATABASE
[/code]

you can still view the ones for your build by using a text editor to open the file "Urho3D.pc" which is found in "${urho3d-installation-dir}/lib/pkgconfig"

-------------------------

christianclavet | 2017-01-02 01:09:13 UTC | #5

Thanks. Found my preprocessors for my build here:
[code]URHO3D_64BIT
URHO3D_ANGELSCRIPT
URHO3D_OPENGL
URHO3D_FILEWATCHER
URHO3D_LOGGING
URHO3D_LUA
URHO3D_NAVIGATION
URHO3D_NETWORK
URHO3D_PACKAGING
URHO3D_PHYSICS
URHO3D_PROFILING
URHO3D_SSE
URHO3D_URHO2D[/code]
It now compile but the linker still fail. I used the same LIB that was created by CodeLite, not the one that was build by MSVC. Using the MINGW32 compiler with it. Since my project is Windows and Linux only, I prefer to use CodeLite.

Here is my current configuration:
[img]http://www.clavet.org/files/URHO/settingCompiler.jpg[/img]

-------------------------

Bluemoon | 2017-01-02 01:09:13 UTC | #6

Sorry I forgot to mention that the "Urho3D.pc" file can serve as a guide to use Urho3D as an external lib, just like your case. As seen from this file you also need to include the following libraries
[code]
user32
gdi32
winmm
imm32
ole32
oleaut32
version
uuid
ws2_32
opengl32
[/code]
NOTE: You don't necessarily have to state out Urho3D library as libUrho3D.a, simply entering it as "Urho3d" can do the job. opengl32 is included there because your build uses opengl on windows.


One more thing. Click the linker option field shown below :

[img]http://i.imgur.com/Nyc0bVD.png[/img]

This will bring out the linker options window, tick the checkboxes as show:

[img]http://i.imgur.com/lnL4hNq.png[/img]

-------------------------

christianclavet | 2017-01-02 01:09:14 UTC | #7

Thanks.

I've done this, tried to rebuild the project and still have linker errors. I will have to investigate more why is this happening.

-------------------------

Bluemoon | 2017-01-02 01:09:14 UTC | #8

Can you post the build log containing the error to assist me further

-------------------------

christianclavet | 2017-01-02 01:09:15 UTC | #9

HI, Here is the output on my Windows 10 system (Codelite V9.0 with Mingw as compiler)

[code]C:\WINDOWS\system32\cmd.exe /C C:/TDM-GCC-64/bin/mingw32-make.exe -j8 SHELL=cmd.exe -e -f  Makefile
"----------Building project:[ Test - Debug ]----------"
mingw32-make.exe[1]: Entering directory 'C:/Users/Public/Projets/Test'
C:/TDM-GCC-64/bin/g++.exe -o ./Debug/Test @"Test.txt" -LC:/Users/Public/Projets/URHO/Codelite/lib  -lUrho3D -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lversion -luuid -lws2_32 -lwinmm -lopengl32 -lUrho3D  -s -mwindows -s -mwindows
./Debug/HelloWorld.cpp.o: In function `Sample::Sample(Urho3D::Context*)':
C:/Users/Public/Projets/Test/Sample.inl:50: undefined reference to `__imp__ZN6Urho3D11ApplicationC2EPNS_7ContextE'
./Debug/HelloWorld.cpp.o: In function `Sample::Setup()':
C:/Users/Public/Projets/Test/Sample.inl:57: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:/Users/Public/Projets/Test/Sample.inl:58: undefined reference to `__imp__ZNK6Urho3D10FileSystem20GetAppPreferencesDirERKNS_6StringES3_'
C:/Users/Public/Projets/Test/Sample.inl:58: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:/Users/Public/Projets/Test/Sample.inl:59: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:/Users/Public/Projets/Test/Sample.inl:60: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o: In function `Sample::Start()':
C:/Users/Public/Projets/Test/Sample.inl:65: undefined reference to `__imp__ZN6Urho3D11GetPlatformEv'
C:/Users/Public/Projets/Test/Sample.inl:65: undefined reference to `__imp__ZN6Urho3D11GetPlatformEv'
C:/Users/Public/Projets/Test/Sample.inl:70: undefined reference to `__imp__ZN6Urho3D6Object16SubscribeToEventENS_10StringHashEPNS_12EventHandlerE'
C:/Users/Public/Projets/Test/Sample.inl:82: undefined reference to `__imp__ZN6Urho3D6Object16SubscribeToEventENS_10StringHashEPNS_12EventHandlerE'
C:/Users/Public/Projets/Test/Sample.inl:84: undefined reference to `__imp__ZN6Urho3D6Object16SubscribeToEventENS_10StringHashEPNS_12EventHandlerE'
./Debug/HelloWorld.cpp.o: In function `Sample::Stop()':
C:/Users/Public/Projets/Test/Sample.inl:89: undefined reference to `__imp__ZN6Urho3D6Engine13DumpResourcesEb'
./Debug/HelloWorld.cpp.o: In function `Sample::InitTouchInput()':
C:/Users/Public/Projets/Test/Sample.inl:103: undefined reference to `__imp__ZN6Urho3D7XMLFileC1EPNS_7ContextE'
C:/Users/Public/Projets/Test/Sample.inl:104: undefined reference to `__imp__ZN6Urho3D7XMLFile10FromStringERKNS_6StringE'
C:/Users/Public/Projets/Test/Sample.inl:105: undefined reference to `__imp__ZN6Urho3D7XMLFile5PatchEPS0_'
C:/Users/Public/Projets/Test/Sample.inl:107: undefined reference to `__imp__ZN6Urho3D5Input17AddScreenJoystickEPNS_7XMLFileES2_'
C:/Users/Public/Projets/Test/Sample.inl:108: undefined reference to `__imp__ZN6Urho3D5Input24SetScreenJoystickVisibleEib'
./Debug/HelloWorld.cpp.o: In function `Sample::SetLogoVisible(bool)':
C:/Users/Public/Projets/Test/Sample.inl:114: undefined reference to `__imp__ZN6Urho3D9UIElement10SetVisibleEb'
./Debug/HelloWorld.cpp.o: In function `Sample::CreateLogo()':
C:/Users/Public/Projets/Test/Sample.inl:127: undefined reference to `__imp__ZN6Urho3D6String5EMPTYE'
C:/Users/Public/Projets/Test/Sample.inl:130: undefined reference to `__imp__ZN6Urho3D6Sprite10SetTextureEPNS_7TextureE'
C:/Users/Public/Projets/Test/Sample.inl:136: undefined reference to `__imp__ZN6Urho3D6Sprite8SetScaleEf'
C:/Users/Public/Projets/Test/Sample.inl:139: undefined reference to `__imp__ZN6Urho3D9UIElement7SetSizeEii'
C:/Users/Public/Projets/Test/Sample.inl:142: undefined reference to `__imp__ZN6Urho3D6Sprite10SetHotSpotEii'
C:/Users/Public/Projets/Test/Sample.inl:145: undefined reference to `__imp__ZN6Urho3D9UIElement12SetAlignmentENS_19HorizontalAlignmentENS_17VerticalAlignmentE'
C:/Users/Public/Projets/Test/Sample.inl:148: undefined reference to `__imp__ZN6Urho3D9UIElement10SetOpacityEf'
C:/Users/Public/Projets/Test/Sample.inl:151: undefined reference to `__imp__ZN6Urho3D9UIElement11SetPriorityEi'
./Debug/HelloWorld.cpp.o: In function `Sample::SetWindowTitleAndIcon()':
C:/Users/Public/Projets/Test/Sample.inl:159: undefined reference to `__imp__ZN6Urho3D8Graphics13SetWindowIconEPNS_5ImageE'
C:/Users/Public/Projets/Test/Sample.inl:160: undefined reference to `__imp__ZN6Urho3D8Graphics14SetWindowTitleERKNS_6StringE'
./Debug/HelloWorld.cpp.o: In function `Sample::CreateConsoleAndDebugHud()':
C:/Users/Public/Projets/Test/Sample.inl:170: undefined reference to `__imp__ZN6Urho3D6Engine13CreateConsoleEv'
C:/Users/Public/Projets/Test/Sample.inl:171: undefined reference to `__imp__ZN6Urho3D7Console15SetDefaultStyleEPNS_7XMLFileE'
C:/Users/Public/Projets/Test/Sample.inl:172: undefined reference to `__imp__ZN6Urho3D9UIElement10SetOpacityEf'
C:/Users/Public/Projets/Test/Sample.inl:175: undefined reference to `__imp__ZN6Urho3D6Engine14CreateDebugHudEv'
C:/Users/Public/Projets/Test/Sample.inl:176: undefined reference to `__imp__ZN6Urho3D8DebugHud15SetDefaultStyleEPNS_7XMLFileE'
./Debug/HelloWorld.cpp.o: In function `Sample::HandleKeyDown(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
C:/Users/Public/Projets/Test/Sample.inl:189: undefined reference to `__imp__ZNK6Urho3D7Console9IsVisibleEv'
C:/Users/Public/Projets/Test/Sample.inl:190: undefined reference to `__imp__ZN6Urho3D7Console10SetVisibleEb'
C:/Users/Public/Projets/Test/Sample.inl:192: undefined reference to `__imp__ZN6Urho3D6Engine4ExitEv'
C:/Users/Public/Projets/Test/Sample.inl:197: undefined reference to `__imp__ZN6Urho3D7Console6ToggleEv'
C:/Users/Public/Projets/Test/Sample.inl:201: undefined reference to `__imp__ZN6Urho3D8DebugHud9ToggleAllEv'
C:/Users/Public/Projets/Test/Sample.inl:218: undefined reference to `__imp__ZN6Urho3D5Input17AddScreenJoystickEPNS_7XMLFileES2_'
C:/Users/Public/Projets/Test/Sample.inl:221: undefined reference to `__imp__ZN6Urho3D5Input24SetScreenJoystickVisibleEib'
C:/Users/Public/Projets/Test/Sample.inl:231: undefined reference to `__imp__ZN6Urho3D8Renderer17SetTextureQualityEi'
C:/Users/Public/Projets/Test/Sample.inl:241: undefined reference to `__imp__ZN6Urho3D8Renderer18SetMaterialQualityEi'
C:/Users/Public/Projets/Test/Sample.inl:246: undefined reference to `__imp__ZN6Urho3D8Renderer19SetSpecularLightingEb'
C:/Users/Public/Projets/Test/Sample.inl:250: undefined reference to `__imp__ZN6Urho3D8Renderer14SetDrawShadowsEb'
C:/Users/Public/Projets/Test/Sample.inl:259: undefined reference to `__imp__ZN6Urho3D8Renderer16SetShadowMapSizeEi'
C:/Users/Public/Projets/Test/Sample.inl:269: undefined reference to `__imp__ZN6Urho3D8Renderer16SetShadowQualityEi'
C:/Users/Public/Projets/Test/Sample.inl:277: undefined reference to `__imp__ZN6Urho3D8Renderer23SetMaxOccluderTrianglesEi'
C:/Users/Public/Projets/Test/Sample.inl:282: undefined reference to `__imp__ZN6Urho3D8Renderer20SetDynamicInstancingEb'
C:/Users/Public/Projets/Test/Sample.inl:288: undefined reference to `__imp__ZN6Urho3D5ImageC1EPNS_7ContextE'
C:/Users/Public/Projets/Test/Sample.inl:289: undefined reference to `__imp__ZN6Urho3D8Graphics14TakeScreenShotERNS_5ImageE'
C:/Users/Public/Projets/Test/Sample.inl:292: undefined reference to `__imp__ZN6Urho3D4Time12GetTimeStampEv'
C:/Users/Public/Projets/Test/Sample.inl:292: undefined reference to `__imp__ZNK6Urho3D6String8ReplacedEccb'
C:/Users/Public/Projets/Test/Sample.inl:292: undefined reference to `__imp__ZNK6Urho3D6String8ReplacedEccb'
C:/Users/Public/Projets/Test/Sample.inl:292: undefined reference to `__imp__ZNK6Urho3D6String8ReplacedEccb'
C:/Users/Public/Projets/Test/Sample.inl:291: undefined reference to `__imp__ZNK6Urho3D10FileSystem13GetProgramDirEv'
C:/Users/Public/Projets/Test/Sample.inl:292: undefined reference to `__imp__ZNK6Urho3D5Image7SavePNGERKNS_6StringE'
C:/Users/Public/Projets/Test/Sample.inl:288: undefined reference to `__imp__ZN6Urho3D5ImageD1Ev'
C:/Users/Public/Projets/Test/Sample.inl:288: undefined reference to `__imp__ZN6Urho3D5ImageD1Ev'
./Debug/HelloWorld.cpp.o: In function `Sample::HandleSceneUpdate(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
C:/Users/Public/Projets/Test/Sample.inl:305: undefined reference to `__imp__ZNK6Urho3D5Input8GetTouchEj'
C:/Users/Public/Projets/Test/Sample.inl:319: undefined reference to `__imp__ZN6Urho3D4Node11SetRotationERKNS_10QuaternionE'
C:/Users/Public/Projets/Test/Sample.inl:326: undefined reference to `__imp__ZN6Urho3D9UIElement11SetPositionERKNS_10IntVector2E'
./Debug/HelloWorld.cpp.o: In function `Sample::HandleTouchBegin(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
C:/Users/Public/Projets/Test/Sample.inl:337: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:/Users/Public/Projets/Test/Sample.inl:337: undefined reference to `__imp__ZN6Urho3D6Object20UnsubscribeFromEventENS_10StringHashE'
./Debug/HelloWorld.cpp.o: In function `RunApplication()':
C:/Users/Public/Projets/Test/HelloWorld.cpp:38: undefined reference to `__imp__ZN6Urho3D7ContextC1Ev'
C:/Users/Public/Projets/Test/HelloWorld.cpp:38: undefined reference to `__imp__ZN6Urho3D11Application3RunEv'
./Debug/HelloWorld.cpp.o: In function `WinMain':
C:/Users/Public/Projets/Test/HelloWorld.cpp:38: undefined reference to `__imp__ZN6Urho3D14ParseArgumentsEPKw'
./Debug/HelloWorld.cpp.o: In function `HelloWorld::CreateText()':
C:/Users/Public/Projets/Test/HelloWorld.cpp:64: undefined reference to `__imp__ZN6Urho3D4TextC1EPNS_7ContextE'
C:/Users/Public/Projets/Test/HelloWorld.cpp:67: undefined reference to `__imp__ZN6Urho3D4Text7SetTextERKNS_6StringE'
C:/Users/Public/Projets/Test/HelloWorld.cpp:70: undefined reference to `__imp__ZN6Urho3D4Text7SetFontEPNS_4FontEi'
C:/Users/Public/Projets/Test/HelloWorld.cpp:71: undefined reference to `__imp__ZN6Urho3D9UIElement8SetColorERKNS_5ColorE'
C:/Users/Public/Projets/Test/HelloWorld.cpp:74: undefined reference to `__imp__ZN6Urho3D9UIElement22SetHorizontalAlignmentENS_19HorizontalAlignmentE'
C:/Users/Public/Projets/Test/HelloWorld.cpp:75: undefined reference to `__imp__ZN6Urho3D9UIElement20SetVerticalAlignmentENS_17VerticalAlignmentE'
C:/Users/Public/Projets/Test/HelloWorld.cpp:78: undefined reference to `__imp__ZN6Urho3D9UIElement8AddChildEPS0_'
./Debug/HelloWorld.cpp.o: In function `HelloWorld::SubscribeToEvents()':
C:/Users/Public/Projets/Test/HelloWorld.cpp:84: undefined reference to `__imp__ZN6Urho3D6Object16SubscribeToEventENS_10StringHashEPNS_12EventHandlerE'
./Debug/HelloWorld.cpp.o: In function `__static_initialization_and_destruction_0':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/CoreEvents.h:31: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/CoreEvents.h:33: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/CoreEvents.h:34: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/CoreEvents.h:38: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/CoreEvents.h:40: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o:C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/CoreEvents.h:44: more undefined references to `__imp__ZN6Urho3D10StringHashC1EPKc' follow
./Debug/HelloWorld.cpp.o: In function `Urho3D::String::String()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Str.h:50: undefined reference to `__imp__ZN6Urho3D6String7endZeroE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::String::String(Urho3D::String const&)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Str.h:58: undefined reference to `__imp__ZN6Urho3D6String7endZeroE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::String::String(char const*)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Str.h:67: undefined reference to `__imp__ZN6Urho3D6String7endZeroE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::String::operator=(Urho3D::String const&)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Str.h:158: undefined reference to `__imp__ZN6Urho3D6String6ResizeEj'
./Debug/HelloWorld.cpp.o: In function `Urho3D::String::operator=(char const*)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Str.h:168: undefined reference to `__imp__ZN6Urho3D6String6ResizeEj'
./Debug/HelloWorld.cpp.o: In function `Urho3D::String::operator+(Urho3D::String const&) const':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Str.h:233: undefined reference to `__imp__ZN6Urho3D6String6ResizeEj'
./Debug/HelloWorld.cpp.o: In function `Urho3D::String::operator+(char const*) const':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Str.h:245: undefined reference to `__imp__ZN6Urho3D6String6ResizeEj'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Quaternion::Quaternion(float, float, float)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Math/Quaternion.h:85: undefined reference to `__imp__ZN6Urho3D10Quaternion15FromEulerAnglesEfff'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Variant::Variant(Urho3D::Variant const&)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Variant.h:415: undefined reference to `__imp__ZN6Urho3D7VariantaSERKS0_'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Variant::~Variant()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Variant.h:421: undefined reference to `__imp__ZN6Urho3D7Variant7SetTypeENS_11VariantTypeE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Variant::operator=(bool)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Variant.h:460: undefined reference to `__imp__ZN6Urho3D7Variant7SetTypeENS_11VariantTypeE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Variant::operator=(Urho3D::String const&)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Variant.h:524: undefined reference to `__imp__ZN6Urho3D7Variant7SetTypeENS_11VariantTypeE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Object::GetBaseTypeStatic()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Object.h:50: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o: In function `Urho3D::EventHandler::EventHandler(Urho3D::Object*)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Object.h:194: undefined reference to `__imp__ZTVN6Urho3D12EventHandlerE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::EventHandler::EventHandler(Urho3D::Object*, void*)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Object.h:203: undefined reference to `__imp__ZTVN6Urho3D12EventHandlerE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::EventHandler::~EventHandler()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Object.h:209: undefined reference to `__imp__ZTVN6Urho3D12EventHandlerE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Font::GetTypeStatic()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/UI/Font.h:48: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Image::GetTypeStatic()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Resource/Image.h:92: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o: In function `Urho3D::XMLFile::GetTypeStatic()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Resource/XMLFile.h:43: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Input::GetTypeStatic()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Input/Input.h:136: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o: In function `Urho3D::UI::GetTypeStatic()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/UI/UI.h:45: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o:C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Engine/Application.h:37: more undefined references to `__imp__ZN6Urho3D10StringHashC1EPKc' follow
./Debug/HelloWorld.cpp.o: In function `Sample::GetScreenJoystickPatchString() const':
C:/Users/Public/Projets/Test/Sample.h:69: undefined reference to `__imp__ZN6Urho3D6String5EMPTYE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Camera::GetTypeStatic()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Graphics/Camera.h:46: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Console::GetTypeStatic()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Engine/Console.h:44: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o: In function `Urho3D::DebugHud::GetTypeStatic()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Engine/DebugHud.h:45: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o: In function `Urho3D::FileSystem::GetTypeStatic()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/IO/FileSystem.h:44: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Graphics::GetTypeStatic()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Graphics/OpenGL/OGLGraphics.h:79: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o:C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Graphics/Renderer.h:153: more undefined references to `__imp__ZN6Urho3D10StringHashC1EPKc' follow
./Debug/HelloWorld.cpp.o: In function `Urho3D::Application::~Application()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Engine/Application.h:35: undefined reference to `__imp__ZTVN6Urho3D11ApplicationE'
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Engine/Application.h:35: undefined reference to `__imp__ZN6Urho3D6ObjectD2Ev'
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Engine/Application.h:35: undefined reference to `__imp__ZN6Urho3D6ObjectD2Ev'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Application::~Application()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Engine/Application.h:35: undefined reference to `__imp__ZTVN6Urho3D11ApplicationE'
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Engine/Application.h:35: undefined reference to `__imp__ZN6Urho3D6ObjectD2Ev'
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Engine/Application.h:35: undefined reference to `__imp__ZN6Urho3D6ObjectD2Ev'
./Debug/HelloWorld.cpp.o: In function `HelloWorld::GetTypeStatic()':
C:/Users/Public/Projets/Test/HelloWorld.h:34: undefined reference to `__imp__ZN6Urho3D10StringHashC1EPKc'
./Debug/HelloWorld.cpp.o: In function `Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>::~HashMap()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/HashMap.h:246: undefined reference to `__imp__ZN6Urho3D21AllocatorUninitializeEPNS_14AllocatorBlockE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::FileSystem* Urho3D::Object::GetSubsystem<Urho3D::FileSystem>() const':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Input* Urho3D::Object::GetSubsystem<Urho3D::Input>() const':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::ResourceCache* Urho3D::Object::GetSubsystem<Urho3D::ResourceCache>() const':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::XMLFile* Urho3D::ResourceCache::GetResource<Urho3D::XMLFile>(Urho3D::String const&, bool)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Resource/ResourceCache.h:257: undefined reference to `__imp__ZN6Urho3D13ResourceCache11GetResourceENS_10StringHashERKNS_6StringEb'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Texture2D* Urho3D::ResourceCache::GetResource<Urho3D::Texture2D>(Urho3D::String const&, bool)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Resource/ResourceCache.h:257: undefined reference to `__imp__ZN6Urho3D13ResourceCache11GetResourceENS_10StringHashERKNS_6StringEb'
./Debug/HelloWorld.cpp.o: In function `Urho3D::UI* Urho3D::Object::GetSubsystem<Urho3D::UI>() const':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Sprite* Urho3D::UIElement::CreateChild<Urho3D::Sprite>(Urho3D::String const&, unsigned int)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/UI/UIElement.h:713: undefined reference to `__imp__ZN6Urho3D9UIElement11CreateChildENS_10StringHashERKNS_6StringEj'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Graphics* Urho3D::Object::GetSubsystem<Urho3D::Graphics>() const':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Image* Urho3D::ResourceCache::GetResource<Urho3D::Image>(Urho3D::String const&, bool)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Resource/ResourceCache.h:257: undefined reference to `__imp__ZN6Urho3D13ResourceCache11GetResourceENS_10StringHashERKNS_6StringEb'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Console* Urho3D::Object::GetSubsystem<Urho3D::Console>() const':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::DebugHud* Urho3D::Object::GetSubsystem<Urho3D::DebugHud>() const':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Renderer* Urho3D::Object::GetSubsystem<Urho3D::Renderer>() const':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Core/Object.h:130: undefined reference to `__imp__ZNK6Urho3D6Object12GetSubsystemENS_10StringHashE'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Camera* Urho3D::Node::GetComponent<Urho3D::Camera>(bool) const':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Scene/Node.h:654: undefined reference to `__imp__ZNK6Urho3D4Node12GetComponentENS_10StringHashEb'
./Debug/HelloWorld.cpp.o: In function `Urho3D::Font* Urho3D::ResourceCache::GetResource<Urho3D::Font>(Urho3D::String const&, bool)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Resource/ResourceCache.h:257: undefined reference to `__imp__ZN6Urho3D13ResourceCache11GetResourceENS_10StringHashERKNS_6StringEb'
./Debug/HelloWorld.cpp.o: In function `Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>::Clear()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/HashMap.h:428: undefined reference to `__imp__ZN6Urho3D8HashBase9ResetPtrsEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Engine>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>::FreeNode(Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>::Node*)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/HashMap.h:699: undefined reference to `__imp__ZN6Urho3D13AllocatorFreeEPNS_14AllocatorBlockEPv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Sprite>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Scene>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Node>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>::InsertNode(Urho3D::StringHash const&, Urho3D::Variant const&, bool)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/HashMap.h:602: undefined reference to `__imp__ZN6Urho3D8HashBase15AllocateBucketsEjj'
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/HashMap.h:614: undefined reference to `__imp__ZN6Urho3D7VariantaSERKS0_'
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/HashMap.h:626: undefined reference to `__imp__ZN6Urho3D8HashBase15AllocateBucketsEjj'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<Urho3D::XMLFile>::AddRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:182: undefined reference to `__imp__ZN6Urho3D10RefCounted6AddRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<Urho3D::XMLFile>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Sprite>::AddRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:182: undefined reference to `__imp__ZN6Urho3D10RefCounted6AddRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Context>::AddRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:182: undefined reference to `__imp__ZN6Urho3D10RefCounted6AddRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Context>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<HelloWorld>::AddRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:182: undefined reference to `__imp__ZN6Urho3D10RefCounted6AddRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<HelloWorld>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Text>::AddRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:182: undefined reference to `__imp__ZN6Urho3D10RefCounted6AddRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::SharedPtr<Urho3D::Text>::ReleaseRef()':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/Ptr.h:190: undefined reference to `__imp__ZN6Urho3D10RefCounted10ReleaseRefEv'
./Debug/HelloWorld.cpp.o: In function `Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>::ReserveNode(Urho3D::StringHash const&, Urho3D::Variant const&)':
C:/Users/Public/Projets/URHO/Codelite/include/Urho3D/Container/HashMap.h:690: undefined reference to `__imp__ZN6Urho3D16AllocatorReserveEPNS_14AllocatorBlockE'
collect2.exe: error: ld returned 1 exit status
mingw32-make.exe[1]: *** [Debug/Test] Error 1
mingw32-make.exe: *** [All] Error 2
Test.mk:79: recipe for target 'Debug/Test' failed
mingw32-make.exe[1]: Leaving directory 'C:/Users/Public/Projets/Test'
Makefile:4: recipe for target 'All' failed
====151 errors, 0 warnings====
[/code]

I've done a build of Urho3D on Linux mint, and tried to do the same thing:
1. Take the Hello World example files (including the samples.h, sample.inl)
2. Create a separate project, add theses files and try to remake the example from the new project (in a new workspace).

Results are almost identical, got tons of "undefined references" coming out also. So there is something that I'm doing totally wrong. I've got URHO3D building from source on each system fine and all example are running.
As of note, when I only compile a file, there is no error. Theses errors come out only in the linking process.

The library that is referenced in the new project was created with the same IDE/Compiler. So there should be no problems using it, I really don't know what I'm doing wrong.

-------------------------

Bluemoon | 2017-01-02 01:09:15 UTC | #10

To be honest, I can't really see why there should be problem during linking. I'm a bit confused

-------------------------

weitjong | 2017-01-02 01:09:15 UTC | #11

I think you should be clear that if you are not using our CMake build system then you are largely on your own. Our build system has been tested to work equally well across all the target platforms supported by Urho3D. But it is one choice if you don't want to use it and do it the hard way. I am intrigue to find out how difficult it is myself without our CMake build system and I just did that experiment. It all worked out for me. I am using the latest branch.

[ol][li] Build the SHARED Urho3D library using Release build configuration with MinGW-W64 and leave it in the build tree without installation. Using STATIC or other build configuration should not make much differences.[/li]
[li] Go to the Urho3D Samples/01_HelloWorld directory and key in this:[/li][/ol]
[code]/usr/bin/x86_64-w64-mingw32-c++ -o HelloWorld.exe HelloWorld.cpp -O3 -DNDEBUG -I.. -I/home/weitjong/ClionProjects/urho3d/mingw-Build/include -I/home/weitjong/ClionProjects/urho3d/mingw-Build/include/Urho3D/ThirdParty -L/home/weitjong/ClionProjects/urho3d/mingw-Build/lib -lUrho3D.dll -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lversion -luuid -lws2_32 -lwinmm -lopengl32[/code]
Naturally you have to adapt the include search path to match yours, and you gonna need more adaptation for more complex samples. Good luck with your attempt.

-------------------------

christianclavet | 2017-01-02 01:09:18 UTC | #12

Hi. I've partially solved the problem.

The linker errors still happen on windows, and from the messages, it look like the the urho.a library has something.

I've redone all this process on Linux Mint 17.1 with CodeLite 9.07 and compilation is working, and the linker errors were due to the fact that the dependancy libraries were not specified. I've checked the[b] Source/Urho3D/urho3d.pc[/b] file from the generated project to find all the related info and was able to input the required libs. It now compile and build on Linux Mint.

Still don't work on Windows. I've done a rebuild of Urho in case the lib was broken, and I will have to investigate more. But this work fine on Linux Mint.
I will try to update in the weekend if I find a solution.

-------------------------

weitjong | 2017-01-02 01:09:19 UTC | #13

That's good to hear. I just want to add that currently the generated Urho3D.pc file is not entirely correct. There are at least two things we could improve.

[ol][li] I think it still erroneously exposes some of the compiler defines that are really required only when building the library and not when using the library.[/li]
[li] The linker flags are erroneously prepared as if user would always want to link against the library statically, i.e. we actually need less linker flags when linking dynamically.[/li][/ol]
When I have time I may make this improvement to the Urho3D.pc file generation in the near future.

Now, when you use our CMake build system then the above planned change will not affect you much. It also will not affect you much when you use the pkg-config tool (which reads the Urho3D.pc file) correctly in your own build system, you just need to update this Urho3D.pc file accordingly. But if you just reference the content of Urho3D.pc file and use the defines/flags or what have you into your own build system then you are bound to forever keep them up to date by yourself manually.

-------------------------

esak | 2017-01-02 01:09:21 UTC | #14

I would also like to use codelite, but on the mac. But I cannot figure out how to set it up.
Could you (those that are using codelite) please explain the different steps to set it up?
Can I build Urho3D in codelite also? Now I have built it through cmake/xcode.

-------------------------

christianclavet | 2017-01-02 01:10:43 UTC | #15

Hi!

I'm still unable to use URHO as a lib on Windows. My progress has been stopped for months now. I'm programming as a hobby and am not a real programmer (with all the knowledge that come with it). I'm able to compile from source, and use the URHO3D examples. I just want to have a single project using URHO as a lib. 

Has someone been able to make it work on windows and share a sample project? I could use this then as a base to start my own project.

I would like to use URHO as a lib the way I used Irrlicht (I used Irrlicht before).

The best for me would be to:
- Take the binary distribution (Sourceforge): [urlhttps://sourceforge.net/projects/urho3d/files/Urho3D/1.5/Urho3D-1.5-Windows-64bit-STATIC.zip/download[/url] (Windows 64bit STATIC)
- Create a new project (Codelite, codeblock or MSVC)
- Set the project to use URHO3D as a lib, and start coding (For example reusing the code from the HELLOWORLD example for a start, then expanding it with my own code.) Would use this "hello world" as a template for each project I would do with URHO.

I've been able to make it work for Linux, but no way to create this on Windows. My "big" PC is using Windows 10, so I'm doing most of the work on this one.

If someone has been able to do this, I would really appreciate if you can share the projects from any of thoses (Codelite, codeblock or MSVC). I really want to get started with this awesome game engine!

Thanks!

-------------------------

thebluefish | 2017-01-02 01:10:43 UTC | #16

Codelite project (filename: bluEdit.project):
[code]
<?xml version="1.0" encoding="UTF-8"?>
<CodeLite_Project Name="bluEdit" InternalType="Console">
  <Plugins>
    <Plugin Name="qmake">
      <![CDATA[00010001N0005Debug000000000000]]>
    </Plugin>
    <Plugin Name="CMakePlugin">
      <![CDATA[[{
  "name": "Debug",
  "enabled": false,
  "buildDirectory": "build",
  "sourceDirectory": "$(ProjectPath)",
  "generator": "",
  "buildType": "",
  "arguments": [],
  "parentProject": ""
 }, {
  "name": "Release",
  "enabled": false,
  "buildDirectory": "build",
  "sourceDirectory": "$(ProjectPath)",
  "generator": "",
  "buildType": "",
  "arguments": [],
  "parentProject": ""
 }]]]>
    </Plugin>
  </Plugins>
  <Description/>
  <Dependencies/>
  <VirtualDirectory Name="src">
    <File Name="src/main.h"/>
    <File Name="src/main.cpp"/>
    <VirtualDirectory Name="Editor">
      <File Name="src/Editor/EditorState.cpp"/>
      <File Name="src/Editor/EditorState.h"/>
      <File Name="src/Editor/EditorAPI.cpp"/>
      <File Name="src/Editor/EditorAPI.h"/>
      <File Name="src/Editor/EditorEvents.h"/>
      <File Name="src/Editor/ProjectHandler.h"/>
      <File Name="src/Editor/ProjectHandler.cpp"/>
      <File Name="src/Editor/StyleEditor.h"/>
      <File Name="src/Editor/StyleEditor.cpp"/>
    </VirtualDirectory>
  </VirtualDirectory>
  <Dependencies Name="Release"/>
  <Dependencies Name="Debug">
    <Project Name="libblu"/>
    <Project Name="blu"/>
  </Dependencies>
  <Settings Type="Executable">
    <GlobalSettings>
      <Compiler Options="-std=c++11" C_Options="" Assembler="">
        <IncludePath Value="./src"/>
        <IncludePath Value="../blu/src"/>
        <IncludePath Value="../blu/src/ThirdParty"/>
        <IncludePath Value="../../Build/Urho3D/include"/>
        <IncludePath Value="../../Build/Urho3D/include/Urho3D/ThirdParty"/>
        <Preprocessor Value="WIN32"/>
        <Preprocessor Value="_WINDOWS"/>
        <Preprocessor Value="_DEBUG"/>
        <Preprocessor Value="URHO3D_SSE"/>
        <Preprocessor Value="URHO3D_MINIDUMPS"/>
        <Preprocessor Value="URHO3D_FILEWATCHER"/>
        <Preprocessor Value="URHO3D_PROFILING"/>
        <Preprocessor Value="URHO3D_LOGGING"/>
        <Preprocessor Value="URHO3D_OPENGL"/>
        <Preprocessor Value="GLEW_STATIC"/>
        <Preprocessor Value="URHO3D_ANGELSCRIPT"/>
        <Preprocessor Value="URHO3D_NAVIGATION"/>
        <Preprocessor Value="URHO3D_NETWORK"/>
        <Preprocessor Value="URHO3D_PHYSICS"/>
        <Preprocessor Value="URHO3D_URHO2D"/>
        <Preprocessor Value="URHO3D_STATIC_DEFINE"/>
        <Preprocessor Value="_CRT_SECURE_NO_WARNINGS"/>
      </Compiler>
      <Linker Options="-mwindows">
        <LibraryPath Value="."/>
        <LibraryPath Value="../../Build/Urho3D/lib"/>
        <LibraryPath Value="../blu/lib"/>
        <Library Value="libUrho3D_d"/>
        <Library Value="libblu_d"/>
        <Library Value="user32"/>
        <Library Value="gdi32"/>
        <Library Value="winmm"/>
        <Library Value="imm32"/>
        <Library Value="ole32"/>
        <Library Value="oleaut32"/>
        <Library Value="version"/>
        <Library Value="uuid"/>
        <Library Value="ws2_32"/>
        <Library Value="winmm"/>
        <Library Value="opengl32"/>
      </Linker>
      <ResourceCompiler Options=""/>
    </GlobalSettings>
    <Configuration Name="Debug" CompilerType="gnu g++" DebuggerType="GNU gdb debugger" Type="Executable" BuildCmpWithGlobalSettings="append" BuildLnkWithGlobalSettings="append" BuildResWithGlobalSettings="append">
      <Compiler Options="-g;-O0;-std=c++11;-Wall" C_Options="-g;-O0;-Wall" Assembler="" Required="yes" PreCompiledHeader="" PCHInCommandLine="no" PCHFlags="" PCHFlagsPolicy="0">
        <IncludePath Value="."/>
      </Compiler>
      <Linker Options="" Required="yes"/>
      <ResourceCompiler Options="" Required="no"/>
      <General OutputFile="../../bin/Debug/$(ProjectName)" IntermediateDirectory="./obj/Debug" Command="../../bin/Debug/$(ProjectName)" CommandArguments="" UseSeparateDebugArgs="no" DebugArguments="" WorkingDirectory="../../bin/Debug/" PauseExecWhenProcTerminates="yes" IsGUIProgram="yes" IsEnabled="yes"/>
      <Environment EnvVarSetName="&lt;Use Defaults&gt;" DbgSetName="&lt;Use Defaults&gt;">
        <![CDATA[]]>
      </Environment>
      <Debugger IsRemote="no" RemoteHostName="" RemoteHostPort="" DebuggerPath="" IsExtended="no">
        <DebuggerSearchPaths/>
        <PostConnectCommands/>
        <StartupCommands/>
      </Debugger>
      <PreBuild/>
      <PostBuild/>
      <CustomBuild Enabled="no">
        <RebuildCommand/>
        <CleanCommand/>
        <BuildCommand/>
        <PreprocessFileCommand/>
        <SingleFileCommand/>
        <MakefileGenerationCommand/>
        <ThirdPartyToolName>None</ThirdPartyToolName>
        <WorkingDirectory/>
      </CustomBuild>
      <AdditionalRules>
        <CustomPostBuild/>
        <CustomPreBuild/>
      </AdditionalRules>
      <Completion EnableCpp11="no" EnableCpp14="no">
        <ClangCmpFlagsC/>
        <ClangCmpFlags/>
        <ClangPP/>
        <SearchPaths/>
      </Completion>
    </Configuration>
    <Configuration Name="Release" CompilerType="gnu g++" DebuggerType="GNU gdb debugger" Type="Executable" BuildCmpWithGlobalSettings="append" BuildLnkWithGlobalSettings="append" BuildResWithGlobalSettings="append">
      <Compiler Options="-O2;-Wall" C_Options="-O2;-Wall" Assembler="" Required="yes" PreCompiledHeader="" PCHInCommandLine="no" PCHFlags="" PCHFlagsPolicy="0">
        <IncludePath Value="."/>
        <Preprocessor Value="NDEBUG"/>
      </Compiler>
      <Linker Options="" Required="yes"/>
      <ResourceCompiler Options="" Required="no"/>
      <General OutputFile="$(IntermediateDirectory)/$(ProjectName)" IntermediateDirectory="./Release" Command="./$(ProjectName)" CommandArguments="" UseSeparateDebugArgs="no" DebugArguments="" WorkingDirectory="$(IntermediateDirectory)" PauseExecWhenProcTerminates="yes" IsGUIProgram="no" IsEnabled="yes"/>
      <Environment EnvVarSetName="&lt;Use Defaults&gt;" DbgSetName="&lt;Use Defaults&gt;">
        <![CDATA[]]>
      </Environment>
      <Debugger IsRemote="no" RemoteHostName="" RemoteHostPort="" DebuggerPath="" IsExtended="no">
        <DebuggerSearchPaths/>
        <PostConnectCommands/>
        <StartupCommands/>
      </Debugger>
      <PreBuild/>
      <PostBuild/>
      <CustomBuild Enabled="no">
        <RebuildCommand/>
        <CleanCommand/>
        <BuildCommand/>
        <PreprocessFileCommand/>
        <SingleFileCommand/>
        <MakefileGenerationCommand/>
        <ThirdPartyToolName>None</ThirdPartyToolName>
        <WorkingDirectory/>
      </CustomBuild>
      <AdditionalRules>
        <CustomPostBuild/>
        <CustomPreBuild/>
      </AdditionalRules>
      <Completion EnableCpp11="no" EnableCpp14="no">
        <ClangCmpFlagsC/>
        <ClangCmpFlags/>
        <ClangPP/>
        <SearchPaths/>
      </Completion>
    </Configuration>
  </Settings>
</CodeLite_Project>
[/code]

There's a full VS2013 project here: [github.com/thebluefish/IndiesvsGamers](https://github.com/thebluefish/IndiesvsGamers)

Everything uses relative paths. The general process for me, with this, looks like:

- Download Urho3D source
- Move into Project/Dependencies/Urho3D
- Run Project/Dependencies/Build_Urho3D.bat
- Build the Urho3D project

Then the projects should compile and run.

-------------------------

jmiller | 2017-01-02 01:10:49 UTC | #17

Bonjour Christian,

Regarding the linking errors with undefined references..
[code]"mingw-w64-crt/crt/crt0_c.c:18: undefined reference to `WinMain'[/code] does appear in [url=https://www.google.com/search?q="mingw-w64-crt%2Fcrt%2Fcrt0_c.c%3A18%3A+undefined+reference+to+%60WinMain%27"]web search[/url] ...

Maybe an issue related to the compiler? mingw-w64s have had bugs now and then, some obscure, and I've had to change/update my revision to resolve them a few times already.
[sourceforge.net/projects/mingw-w ... daily/5.x/](http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/dongsheng-daily/5.x/)

If you do reconsider cmake makefiles, at least people are more familiar with them and maybe linking is less trouble..

And to intercept the most common mingw linker error,
My own project adds (in cmake parlance)  set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -static-libgcc -static-libstdc++")

-------------------------

AReichl | 2017-01-02 01:10:49 UTC | #18

Hi christianclavet  ( we know each other from the Irrlicht forum ),

well - i had no trouble using Urho3D the same way as Irrlicht ( only tried it with Visual Studio by now ).

try this ( 'D:\Develop.etc\Urho3D\trunk\' is my directory for Urho3D ):

include paths:
----------------
D:\Develop.etc\Urho3D\trunk\Build.VS2015\include
D:\Develop.etc\Urho3D\trunk\Build.VS2015\include\Urho3D\ThirdParty
D:\Develop.etc\Urho3D\trunk\Build.VS2015\include\Urho3D\ThirdParty\Bullet
D:\Develop.etc\Urho3D\trunk\Source\Samples

lib path:
----------
D:\Develop.etc\Urho3D\trunk\Build.VS2015\lib

preprocessor options:
-------------------------
WIN32;
_WINDOWS;
_DEBUG;
URHO3D_MINIDUMPS;
URHO3D_WIN32_CONSOLE;
URHO3D_FILEWATCHER;
URHO3D_PROFILING;
URHO3D_LOGGING;
URHO3D_THREADING;
URHO3D_ANGELSCRIPT;
URHO3D_NAVIGATION;
URHO3D_NETWORK;
URHO3D_PHYSICS;
URHO3D_URHO2D;
URHO3D_CXX11;
_CRT_SECURE_NO_WARNINGS;
HAVE_STDINT_H;
CMAKE_INTDIR="Debug";
%(PreprocessorDefinitions)

I dont't know if you need all the above options, but i copied them just in case.

And just because i am here, i have another question:
in OpenGL the texture coordinates are flipped - how is this handled in Urho3D; automatically in the lib or in shaders?

-------------------------

cadaver | 2017-01-02 01:10:49 UTC | #19

Regarding the UV coordinates (that would have been much more visible in its own thread though): 

Where it matters, there is automatical code in Urho3D to handle the UV addressing difference. Practically it mostly matters only when rendering to a texture; the rendering is automatically flipped on OpenGL. Meshes' UV coordinates don't need to change. Some shader math related to postprocessing and screen-coords to UV conversion also needs taking this into account, it's done in the included base GLSL code.

-------------------------

christianclavet | 2017-01-02 01:10:54 UTC | #20

Hi! Thanks everybody! (Especially [b][u]thebluefish[/u][/b]!) I was able to get some hints from your project and make one. I reused the HelloGUI example as a start. Now it compile, link and build in MSVC (I was not able to get it to work for CODELITE yet.)
Here is a link to my "template project" ([url]http://www.clavet.org/files/URHO/TemplateMSVC.zip[/url] 94,02Mb)
This is a complete project in done MSVC Community 2015 edition that has all the required files. You can open it in MSVC and compile. You don't need any other files to start. This is only using the HelloGUI sample. But for what I need this is a perfect start for a template. I've set also the path to be relative and the URHO libs and include files are all there. The libs are static.

I reused my version of URHO, rebuilded it from source in 32bit with theses option :
URHO3D_SSE
URHO3D_WIN32_CONSOLE
URHO3D_FILEWATCHER
URHO3D_PROFILING
URHO3D_LOGGING
URHO3D_OPENGL
URHO3D_ANGELSCRIPT
URHO3D_LUA
URHO3D_NAVIGATION
URHO3D_NETWORK
URHO3D_PHYSICS
URHO3D_URHO2D
URHO3D_STATIC_DEFINE
URHO3D_CPP11

- Generated the debug and release libs for it.
- Started the "template" solution with a project of the same name. 
- Took the source files from the hello gui sample
- created a "3rdParty" folder with the include and lib folder from urho3d msvc build
- Set the paths appropriately
- Took the info for the link libraries inside [b][u]thebluefish[/u][/b] MSVC project and pasted there. Removing the extra stuff that was not needed.
- Set minor things for release and debug

Now the project compile fine and build on Windows using MSVC community 2015 edition.

Most of the issues seem to have come from this:
- link libraries informations send to the linker. Only the list taken from [b][u]thebluefish[/u][/b] worked. Before I was able to compile, but was not able to link.
[b]EDIT:[/b] Rebuild the libs as 64bits, and re-tested in the project. Changed to x64 and it worked. The file in the link is updated with the 64bit version.
Here are the parameters that work for me[i] (Release use Urho3d.lib, debug use Urho3d_d.lib)[/i]
[code]kernel32.lib
user32.lib
gdi32.lib
winspool.lib
shell32.lib
ole32.lib
oleaut32.lib
uuid.lib
comdlg32.lib
advapi32.lib
Urho3D.lib
winmm.lib
imm32.lib
version.lib
ws2_32.lib
dbghelp.lib
opengl32.lib[/code]

[b]EDIT2:[/b] Since I've seen it work, I was able to make the same type of work for a CODELITE project (MINGW compiler (TDM-GCC-64))
Interpreting the data in the Urho3D.pc file was invaluable. Just not 100% sure the project is 64bit. Tryied to -m64 flag on the linker and it was not accepted.

Here is a link to my "template project" 
   - MSVC Community Edition 2015 ([url]http://www.clavet.org/files/URHO/TemplateMSVC.zip[/url] 94,02Mb)
   - Codelite 9.13 with (MINGW compiler (TDM-GCC-64)) ([url]http://www.clavet.org/files/URHO/Template_Codelite.zip[/url] 36,02Mb)

These "templates" only contain the hello gui example, that you can start if you have one of theses installed on Windows (MSVC 2015 or Codelite).
Urho is already compiled as a lib for thoses IDE`s and their projects are ready to compile.
I'll be ready now to start my own small projects and check more of URHO features. Thanks!

-------------------------

