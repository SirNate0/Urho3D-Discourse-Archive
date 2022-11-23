setzer22 | 2017-01-02 01:02:42 UTC | #1

Hello everyone!

I've got problems with registering integer class variables into the script API. I have this class:

[code]
class UnitStats : public LogicComponent { 
	OBJECT(UnitStats)  
private:
        ...
public:
        ...
    String unitName;
	int HP;
	int moveRange;
	int attackRange;
	int minAttackRange;
        ...

   void BindScriptMethods(asIScriptEngine *engine) {
       ...
       r = engine->RegisterObjectProperty("String", "String unitName", asOFFSET(UnitStats,unitName)); 
       assert(r >= 0) ;
       r = engine->RegisterObjectProperty("int", "int HP", asOFFSET(UnitStats,HP)); 
       assert(r >= 0) ;
       ...
   }
};
[/code]

As you can see I'm registering an int  and a String variables, the String object property is properly defined and works, but somehow the int one is giving me trouble.

The code compiles just fine but crashes on execution. The RegisterObjectProperty method makes some kind of invalid memory access.

This is the gdb's backtrace:
[code]
Program received signal SIGSEGV, Segmentation fault.
0x0000000000ef93a0 in asCString::AddressOf (this=0x8)
    at URHO3D_HOME/Source/ThirdParty/AngelScript/source/as_string.cpp:114
114		if( length <= 11 )
(gdb) backtrace
#0  0x0000000000ef93a0 in asCString::AddressOf (this=0x8)
    at URHO3D_HOME/Source/ThirdParty/AngelScript/source/as_string.cpp:114
#1  0x0000000000c169fb in asCScriptEngine::RegisterObjectProperty (this=0x18e1fb0, obj=0x10ce793 "int", declaration=0x10ccd0b "int HP", 
    byteOffset=168) at URHO3D_HOME/Source/ThirdParty/AngelScript/source/as_scriptengine.cpp:1452
#2  0x00000000007f37cf in UnitStats::BindScriptMethods (engine=0x18e1fb0)
    at PROJECT_HOME/Source/Components/Unit/Stats/UnitStats.cpp:49
#3  0x00000000008087a3 in CustomComponents::BindScriptMethods (engine=0x18e1fb0)
    at PROJECT_HOME/Source/CustomPlayer/CustomComponents.cpp:39
#4  0x00000000008076da in MainApplication::Start (this=0x16ab4a0)
    at PROJECT_HOME/Source/CustomPlayer/MainApplication.cpp:67
#5  0x0000000000b4be3f in Urho3D::Application::Run (this=0x16ab4a0)
    at URHO3D_HOME/Source/Engine/Engine/Application.cpp:77
#6  0x000000000080730c in RunApplication () at PROJECT_HOMESource/CustomPlayer/MainApplication.cpp:42
#7  0x00007ffff696c040 in __libc_start_main () from /usr/lib/libc.so.6
#8  0x00000000007ee0bf in _start ()
[/code]
I've omitted paths for your convenience, don't mind those URHO3D_HOME/PROJECT_HOME lines.

There's not much more I can say about it, note that I've just copied the example from AngelScript's documentation: [url]http://www.angelcode.com/angelscript/sdk/docs/manual/doc_reg_objprop.html[/url]

The obvious workaround is define getter/setter functions and register those. I'm pretty sure that would work as I've, at least used the "int" data type before while registering methods. Nevertheless I'd like to avoid doing that so the interface is the same on AS and C++.

I don't get why this isn't working. Any clues?

Thanks!

[b]EDIT[/b] Also, as another (remotely-possible-)relevant fact all those class fields are being registered as component attributes as well.

-------------------------

