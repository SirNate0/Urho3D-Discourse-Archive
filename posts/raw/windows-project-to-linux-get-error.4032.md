spwork | 2018-02-21 19:32:31 UTC | #1

I put a windows project to linux and compile with a error:
SubscribeToEvent(E_INPUTFOCUS, [&](StringHash eventType, VariantMap & eventData)
	{
		BGMIsPlaying = eventData[InputFocus::P_FOCUS].GetBool();
		BGMSoundSource->SetEnabled(BGMIsPlaying);
	});

this is error message

    /home/zhangkai/Documents/trunk/Src/AudioManager.cpp: 在成员函数‘void AudioManager::Init()’中:
    /home/zhangkai/Documents/trunk/Src/AudioManager.cpp:43:3: 错误：no matching function for call to ‘AudioManager::SubscribeToEvent(const Urho3D::StringHash&, AudioManager::Init()::<lambda(Urho3D::StringHash, Urho3D::VariantMap&)>)’
      });
       ^
    In file included from /home/zhangkai/Documents/Urho3D-1.7/Build/include/Urho3D/AngelScript/../AngelScript/Script.h:26:0,
                     from /home/zhangkai/Documents/Urho3D-1.7/Build/include/Urho3D/AngelScript/APITemplates.h:26,
                     from /home/zhangkai/Documents/Urho3D-1.7/Build/include/Urho3D/Urho3DAll.h:28,
                     from /home/zhangkai/Documents/trunk/Src/AudioManager.h:2,
                     from /home/zhangkai/Documents/trunk/Src/AudioManager.cpp:1:
    /home/zhangkai/Documents/Urho3D-1.7/Build/include/Urho3D/AngelScript/../AngelScript/../Core/Object.h:110:10: 附注：candidate: void Urho3D::Object::SubscribeToEvent(Urho3D::StringHash, Urho3D::EventHandler*)
         void SubscribeToEvent(StringHash eventType, EventHandler* handler);
              ^~~~~~~~~~~~~~~~
    /home/zhangkai/Documents/Urho3D-1.7/Build/include/Urho3D/AngelScript/../AngelScript/../Core/Object.h:110:10: 附注：  no known conversion for argument 2 from ‘AudioManager::Init()::<lambda(Urho3D::StringHash, Urho3D::VariantMap&)>’ to ‘Urho3D::EventHandler*’
    /home/zhangkai/Documents/Urho3D-1.7/Build/include/Urho3D/AngelScript/../AngelScript/../Core/Object.h:112:10: 附注：candidate: void Urho3D::Object::SubscribeToEvent(Urho3D::Object*, Urho3D::StringHash, Urho3D::EventHandler*)
         void SubscribeToEvent(Object* sender, StringHash eventType, EventHandler* handler);
              ^~~~~~~~~~~~~~~~
    /home/zhangkai/Documents/Urho3D-1.7/Build/include/Urho3D/AngelScript/../AngelScript/../Core/Object.h:112:10: 附注： 备选需要 3 实参，但提供了 2 个
    make[2]: *** [CMakeFiles/Restaurant_Tycoon.dir/build.make:63：CMakeFiles/Restaurant_Tycoon.dir/AudioManager.cpp.o] 错误 1
    make[1]: *** [CMakeFiles/Makefile2:68：CMakeFiles/Restaurant_Tycoon.dir/all] 错误 2
    make: *** [Makefile:130：all] 错误 2

no known conversion for argument 2 from ‘AudioManager::Init()::<lambda(Urho3D::StringHash, Urho3D::VariantMap&)>’ to ‘Urho3D::EventHandler*’

in windows it will generate succeed

-------------------------

Eugene | 2018-02-21 19:40:01 UTC | #2

Are you sure that C++11 is turned on in your build tree?

-------------------------

spwork | 2018-02-21 19:39:57 UTC | #3

sorry,i forget open C++11

-------------------------

