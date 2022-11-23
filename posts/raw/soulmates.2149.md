1vanK | 2017-01-02 01:13:28 UTC | #1

Repo: [github.com/1vanK/Soulmates](https://github.com/1vanK/Soulmates)

Video: [youtube.com/watch?v=2WAyRhZph9I](http://www.youtube.com/watch?v=2WAyRhZph9I)

[url=http://savepic.ru/10783187.htm][img]http://savepic.ru/10783187m.png[/img][/url]

P.s. The game is absolutely free, but you can vote for it [steamcommunity.com/sharedfiles/f ... =734916470](http://steamcommunity.com/sharedfiles/filedetails/?id=734916470)

-------------------------

MikeDX | 2017-01-02 01:13:44 UTC | #2

I'd love to play this (and your fishy game) but neither want to compile on my mac

I've edited CMakeLists.txt appropriately, but some C++ weirdness prevents it from working:
[code]
Mikes-MacBook-Air:FlappyUrho mike$ make
[ 16%] Building CXX object CMakeFiles/FlappyUrho.dir/BarrierLogic.cpp.o
/Users/mike/FlappyUrho/BarrierLogic.cpp:19:16: error: 
      expected ';' at end of declaration
    Vector3 pos{node_->GetPosition()};
               ^
               ;
1 error generated.
make[2]: *** [CMakeFiles/FlappyUrho.dir/BarrierLogic.cpp.o] Error 1
make[1]: *** [CMakeFiles/FlappyUrho.dir/all] Error 2
make: *** [all] Error 2

[/code]

Soulmates generates a lot more errors

Is this some difference between visual C++ and gcc / llvm ?

-------------------------

1vanK | 2017-01-02 01:13:44 UTC | #3

> Vector3 pos{node_->GetPosition()};

It's not my code :) I never use this initialization. Perhaps you are using Modanung's fork

-------------------------

1vanK | 2017-01-02 01:13:44 UTC | #4

> Soulmates generates a lot more errors

U can open issue on github and show log. I try to fix it

[b]EDIT:[/b] Soulmates uses "String + int" in some places, so u need to use specific version of the engine

[github.com/1vanK/Soulmates/blob ... wnload.bat](https://github.com/1vanK/Soulmates/blob/master/Engine/1_Download.bat)
[code]
git clone https://github.com/Urho3D/Urho3D.git
cd Urho3D
git reset --hard 56ba0def78fa31e9420b53ffef910bad8a4cea34[/code]

-------------------------

MikeDX | 2017-01-02 01:13:44 UTC | #5

Sorry, it is late and not paying attention correctly! Yes, Flappy is [github.com/Modanung/FlappyUrho](https://github.com/Modanung/FlappyUrho)

However! Your Soulmates code also fails for me :frowning:

I think it's an issue with the C++ standard used, since some seem to be c++11 extension errors, but others are something else.

[code]
Mikes-MacBook-Air:GameSrc mike$ make
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/mike/Soulmates/GameSrc
[ 11%] Building CXX object CMakeFiles/Soulmates.dir/BoardLogic.cpp.o
In file included from /Users/mike/Soulmates/GameSrc/BoardLogic.cpp:1:
In file included from /Users/mike/Soulmates/GameSrc/BoardLogic.h:7:
/Users/mikeg/Soulmates/GameSrc/Global.h:24:22: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    int soundVolume_ = DEFAULT_VOLUME;
                     ^
/Users/mike/Soulmates/GameSrc/Global.h:26:22: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    int musicVolume_ = DEFAULT_VOLUME;
                     ^
/Users/mike/Soulmates/GameSrc/Global.h:29:19: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    Scene* scene_ = nullptr;
                  ^
/Users/mike/Soulmates/GameSrc/Global.h:31:22: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    Node* boardNode_ = nullptr;
                     ^
/Users/mike/Soulmates/GameSrc/Global.h:39:26: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    GameState gameState_ = GS_START_MENU;
                         ^
/Users/mike/Soulmates/GameSrc/Global.h:42:32: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    GameState neededGameState_ = GS_START_MENU;
                               ^
In file included from /Users/mike/Soulmates/GameSrc/BoardLogic.cpp:1:
/Users/mike/Soulmates/GameSrc/BoardLogic.h:47:16: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    int width_ = DEFAULT_BOARD_WIDTH;
               ^
/Users/mike/Soulmates/GameSrc/BoardLogic.h:48:17: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    int height_ = DEFAULT_BOARD_HEIGHT;
                ^
/Users/mike/Soulmates/GameSrc/BoardLogic.h:49:20: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    int numColors_ = DEFAULT_NUM_COLORS;
                   ^
/Users/mike/Soulmates/GameSrc/BoardLogic.h:50:28: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    int initialPopulation_ = DEFAULT_POPULATION;
                           ^
/Users/mike/Soulmates/GameSrc/BoardLogic.h:51:21: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    int lineLength_ = DEFAULT_LINE_LENGTH;
                    ^
/Users/mike/Soulmates/GameSrc/BoardLogic.h:52:20: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    bool diagonal_ = DEFAULT_DIAGONAL;
                   ^
/Users/mike/Soulmates/GameSrc/BoardLogic.h:55:16: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    int score_ = 0;
               ^
/Users/mike/Soulmates/GameSrc/BoardLogic.h:58:27: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    bool needBreakUpdate_ = false;
                          ^
/Users/mike/Soulmates/GameSrc/BoardLogic.h:82:25: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    Node* selectedUnit_ = nullptr;
                        ^
In file included from /Users/mike/Soulmates/GameSrc/BoardLogic.cpp:2:
/Users/mike/Soulmates/GameSrc/UnitAnimator.h:23:24: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    float removeTimer_ = 0.0f;
                       ^
In file included from /Users/mike/Soulmates/GameSrc/BoardLogic.cpp:5:
/Users/mike/Soulmates/GameSrc/UIManager.h:31:28: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    MyButton* musicButton_ = nullptr;
                           ^
/Users/mike/Soulmates/GameSrc/UIManager.h:32:28: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    MyButton* soundButton_ = nullptr;
                           ^
/Users/mike/Soulmates/GameSrc/UIManager.h:73:24: warning: 
      in-class initialization of non-static data member is a
      C++11 extension [-Wc++11-extensions]
    float showedScore_ = 0.0f;
                       ^
/Users/mike/Soulmates/GameSrc/BoardLogic.cpp:8:42: error: 
      expected ';' after top level declarator
static const Color colors[MAX_NUM_COLORS]
                                         ^
                                         ;
/Users/mike/Soulmates/GameSrc/BoardLogic.cpp:215:5: warning: 
      'auto' type specifier is a C++11 extension
      [-Wc++11-extensions]
    auto staticModel = selectedUnit_->GetComponent<Stat...
    ^
/Users/mike/Soulmates/GameSrc/BoardLogic.cpp:216:5: warning: 
      'auto' type specifier is a C++11 extension
      [-Wc++11-extensions]
    auto material = staticModel->GetMaterial(0);
    ^
/Users/mike/Soulmates/GameSrc/BoardLogic.cpp:270:9: warning: 
      'auto' type specifier is a C++11 extension
      [-Wc++11-extensions]
        auto staticModel = selectedUnit_->GetComponent<...
        ^
/Users/mike/Soulmates/GameSrc/BoardLogic.cpp:271:9: warning: 
      'auto' type specifier is a C++11 extension
      [-Wc++11-extensions]
        auto material = staticModel->GetMaterial(0);
        ^
/Users/mike/Soulmates/GameSrc/BoardLogic.cpp:277:5: warning: 
      'auto' type specifier is a C++11 extension
      [-Wc++11-extensions]
    auto staticModel = selectedUnit_->GetComponent<Stat...
    ^
/Users/mike/Soulmates/GameSrc/BoardLogic.cpp:278:5: warning: 
      'auto' type specifier is a C++11 extension
      [-Wc++11-extensions]
    auto material = staticModel->GetMaterial(0);
    ^
/Users/mike/Soulmates/GameSrc/BoardLogic.cpp:491:12: error: 
      use of undeclared identifier 'max'
    return max(width_, height_);
           ^
/Users/mike/Soulmates/GameSrc/BoardLogic.cpp:504:24: error: 
      invalid operands to binary expression ('Urho3D::String'
      and 'int')
    return String("w") + width_ + "h" + height_ +
           ~~~~~~~~~~~ ^ ~~~~~~
/Users/mike/Urho3D/include/Urho3D/AngelScript/../Container/Str.h:230:12: note: 
      candidate function not viable: no known conversion from
      'int' to 'const Urho3D::String' for 1st argument
    String operator +(const String& rhs) const
           ^
/Users/mike/Urho3D/include/Urho3D/AngelScript/../Container/Str.h:241:12: note: 
      candidate function not viable: no known conversion from
      'int' to 'const char *' for 1st argument
    String operator +(const char* rhs) const
           ^
/Users/mike/Urho3D/include/Urho3D/AngelScript/../Container/Str.h:529:15: note: 
      candidate function not viable: no known conversion from
      'Urho3D::String' to 'const char *' for 1st argument
inline String operator +(const char* lhs, const String& rhs)
              ^
/Users/mike/Urho3D/include/Urho3D/AngelScript/../Container/Str.h:537:15: note: 
      candidate function not viable: no known conversion from
      'Urho3D::String' to 'const wchar_t *' for 1st argument
inline String operator +(const wchar_t* lhs, const String& rhs)
              ^
/Users/mike/Urho3D/include/Urho3D/ThirdParty/Bullet/LinearMath/btVector3.h:753:1: note: 
      candidate function not viable: no known conversion from
      'Urho3D::String' to 'const btVector3' for 1st argument
operator+(const btVector3& v1, const btVector3& v2) 
^
/Users/mike/Urho3D/include/Urho3D/ThirdParty/Bullet/LinearMath/btMatrix3x3.h:901:1: note: 
      candidate function not viable: no known conversion from
      'Urho3D::String' to 'const btMatrix3x3' for 1st argument
operator+(const btMatrix3x3& m1, const btMatrix3x3& m2)
^
/Users/mike/Urho3D/include/Urho3D/ThirdParty/Box2D/Common/b2Math.h:446:15: note: 
      candidate function not viable: no known conversion from
      'Urho3D::String' to 'const b2Vec2' for 1st argument
inline b2Vec2 operator + (const b2Vec2& a, const b2Vec2& b)
              ^
/Users/mike/Urho3D/include/Urho3D/ThirdParty/Box2D/Common/b2Math.h:485:15: note: 
      candidate function not viable: no known conversion from
      'Urho3D::String' to 'const b2Vec3' for 1st argument
inline b2Vec3 operator + (const b2Vec3& a, const b2Vec3& b)
              ^
/Users/mike/Urho3D/include/Urho3D/ThirdParty/Box2D/Common/b2Math.h:508:16: note: 
      candidate function not viable: no known conversion from
      'Urho3D::String' to 'const b2Mat22' for 1st argument
inline b2Mat22 operator + (const b2Mat22& A, const b2Mat22& B)
               ^
25 warnings and 3 errors generated.
make[2]: *** [CMakeFiles/Soulmates.dir/BoardLogic.cpp.o] Error 1
make[1]: *** [CMakeFiles/Soulmates.dir/all] Error 2
make: *** [all] Error 2
[/code]

-------------------------

MikeDX | 2017-01-02 01:13:44 UTC | #6

[quote="1vanK"]> Soulmates generates a lot more errors

U can open issue on github and show log. I try to fix it

[b]EDIT:[/b] Soulmates uses "String + int" in some places, so u need to use specific version of the engine

[github.com/1vanK/Soulmates/blob ... wnload.bat](https://github.com/1vanK/Soulmates/blob/master/Engine/1_Download.bat)
[code]
git clone https://github.com/Urho3D/Urho3D.git
cd Urho3D
git reset --hard 56ba0def78fa31e9420b53ffef910bad8a4cea34[/code][/quote]



Ah yes, I saw that. Maybe I will try to compile that commit overnight - it took a little while to compile the engine here.

-------------------------

1vanK | 2017-01-02 01:13:45 UTC | #7

Also u need enable c++11 in cmake, when u compile engine

-------------------------

MikeDX | 2017-01-02 01:13:45 UTC | #8

Adding 

[code]set (CMAKE_CXX_FLAGS "--std=gnu++11 ${CMAKE_CXX_FLAGS}")[/code] to the cmakelists.txt fixed the c11 problems, so thats half the battle

Tomorrow I shall compile Urho3D from that commit and see if the whole thing works!

Thanks for your help :slight_smile:

-------------------------

1vanK | 2017-01-02 01:13:45 UTC | #9

cmake has URHO3D_C++11 option (for game project also enable it)

EDIT: u can just replace "String + int" to "String + String(int)" in the pair of places and it should work

-------------------------

MikeDX | 2017-01-02 01:13:45 UTC | #10

[quote="1vanK"]cmake has URHO3D_C++11 option (for game project also enable it)[/quote]

Ah, excellent. that worked!

With some minor edits (missing max() function - weird) it almost compiled, but then the link failed 

[code]
Undefined symbols for architecture x86_64:
  "Urho3D::ToInt(Urho3D::String const&)", referenced from:
      Config::GetRecord(Urho3D::String) in Config.cpp.o
     (maybe you meant: __ZN6Urho3D5ToIntERKNS_6StringEi)
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
[/code]

But that's ok, I'm rebuilding the main lib now from that commit so hopefully I can play your game soon!

-------------------------

MikeDX | 2017-01-02 01:13:45 UTC | #11

I don't think it is my lucky day!

[code][100%] Building CXX object CMakeFiles/Soulmates.dir/Utils.cpp.o
Linking CXX executable bin/Soulmates
clang: warning: argument unused during compilation: '-pthread'
duplicate symbol _revision in:
    CMakeFiles/Soulmates.dir/BoardLogic.cpp.o
    CMakeFiles/Soulmates.dir/CameraLogic.cpp.o
duplicate symbol _revision in:
    CMakeFiles/Soulmates.dir/BoardLogic.cpp.o
    CMakeFiles/Soulmates.dir/Config.cpp.o
duplicate symbol _revision in:
    CMakeFiles/Soulmates.dir/BoardLogic.cpp.o
    CMakeFiles/Soulmates.dir/Game.cpp.o
duplicate symbol _revision in:
    CMakeFiles/Soulmates.dir/BoardLogic.cpp.o
    CMakeFiles/Soulmates.dir/Global.cpp.o
duplicate symbol _revision in:
    CMakeFiles/Soulmates.dir/BoardLogic.cpp.o
    CMakeFiles/Soulmates.dir/MyButton.cpp.o
duplicate symbol _revision in:
    CMakeFiles/Soulmates.dir/BoardLogic.cpp.o
    CMakeFiles/Soulmates.dir/UIManager.cpp.o
duplicate symbol _revision in:
    CMakeFiles/Soulmates.dir/BoardLogic.cpp.o
    CMakeFiles/Soulmates.dir/UnitAnimator.cpp.o
duplicate symbol _revision in:
    CMakeFiles/Soulmates.dir/BoardLogic.cpp.o
    CMakeFiles/Soulmates.dir/Utils.cpp.o
ld: 8 duplicate symbols for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [bin/Soulmates] Error 1
make[1]: *** [CMakeFiles/Soulmates.dir/all] Error 2
make: *** [all] Error 2
[/code]

It's late, I shall try again tomorrow :slight_smile:

-------------------------

