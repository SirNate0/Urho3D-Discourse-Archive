GIMB4L | 2017-01-02 00:57:58 UTC | #1

Say I have a manager, and on a certain function call, I want to create an object on the C++ side, and return a pointer to script. It's fairly straightforward, but I ran into one hitch -- all script objects must inherit from Object which has Context as a parameter.

So when I tried to create a script object C++ side, I just called this->GetContext() and passed that context into the constructor of the new script object. I found out later that the object I created was promptly destroyed, which is probably due to context.

What's the proper way to make a script object C++ side?

-------------------------

Azalrion | 2017-01-02 00:57:58 UTC | #2

They don't inherit from Object they inherit from ScriptObject. When instantiated from the C++ side you should be using ScriptFile or ScriptInstance to instantiate the ScriptObjects. ScriptFiles are used for non-component Script Objects and Global Script Functions, and ScriptInstances are components that need to be added to a node.

So your script class would look like:

[code]class Foo : ScriptObject
{
}[/code]

And you'd use the following methods to instantiate and execute it:

[code]
    asIScriptObject* ScriptFile::CreateObject(const String& className);
    bool ScriptFile::Execute(asIScriptObject* object, const String& declaration, const VariantVector& parameters = Variant::emptyVariantVector, bool unprepare = true);
[/code]

[code]
    bool ScriptInstance::CreateObject(ScriptFile* scriptFile, const String& className);
    bool ScriptInstance::Execute(const String& declaration, const VariantVector& parameters = Variant::emptyVariantVector); //Optional ScriptInstance runs certain methods on start-up.
[/code]

More details can be found here: [urho3d.github.io/documentation/a00016.html](http://urho3d.github.io/documentation/a00016.html)

-------------------------

GIMB4L | 2017-01-02 00:57:58 UTC | #3

Got it, thanks.

-------------------------

GIMB4L | 2017-01-02 00:57:58 UTC | #4

WAIT

I think we're mistaken.

I have a class I have defined in C++. It inherits from Urho3D::Object. I want to be able to make instances of this C++ side, and pass them back to script. That's where I was having the context issue above.

-------------------------

weitjong | 2017-01-02 00:57:58 UTC | #5

I believe Alex has pointed you to the right direction. If you must declare your script object from C++ side instead of from script, I think what you need to do is to derive your component not from Urho3D::Object class but from Urho3D::ScriptInstance class. After creating the component object and attaching it to a node, your C++ function should be able to safely return a pointer to it to your script. I think in your script, you can also get script object back by using Node::GetScriptObject() API call. However, if what you are trying to achieve is an arbitrary object (i.e. not derived from Component class), so it cannot be attached to a node then I think you need to call AddRef() somewhere in your C++ function before returning that script object back to your script. And then you have to think of when is the appropriate time to decrease the reference count so your object would be destroyed in a timely manner.

-------------------------

Azalrion | 2017-01-02 00:57:58 UTC | #6

If you want classes defined in C++ usable in a script you need to also bind them to angelscript like Urho does in all the ...API.cpp files even if it does inherit from object as otherwise none of your custom methods will be available.

As for the deletion issue its probably being deleted as Weitjong says there is only a single reference and when your function falls out of scope its being deleted as I dont believe passing it to a script as part of the parameters adds a new reference as it treats it as a raw pointer and since it was created on the c++ side you need to do your lifecycle management there.

-------------------------

GIMB4L | 2017-01-02 00:57:58 UTC | #7

Ah, that makes sense. Thanks guys!

-------------------------

gasp | 2017-01-02 00:58:35 UTC | #8

i am trying to do exactly this :
[b]"If you want classes defined in C++ usable in a script you need to also bind them to angelscript like Urho does in all the ...API.cpp files even if it does inherit from object as otherwise none of your custom methods will be available."[/b]

i've created a "SimpleMath" class (h & cpp)
only 1 member "int  DoubleTheValue(int value);" who do a wonderfull :
[quote]
int  SimpleMath::DoubleTheValue(int value)
{
    return value * 2 ;
}
[/quote]
all compile fine, and the class work in the main cpp file 


In the main program (base on Urho3DPlayer.cpp) i've try the folowwing things :

My goal is to be able to call the "RegisterObjectMethod" Angel Script part who register the function for the script, somethings like :
[quote]
engine->RegisterObjectMethod("SimpleMath", "int  SimpleMath::DoubleTheValue(int value)", asMETHOD(SimpleMath, DoubleTheValue), asCALL_THISCALL);
[/quote]
the tricky part for me now is to be able to acces the engins script, like all the *API.cpp.

i've try something like that :
[quote]
Script *asEngine;
        context_->RegisterSubsystem(asEngine=new Script(context_));
[/quote]

but ... i must miss something :/
[quote]
asIScriptEngine* ScriptEngine=context_->GetSubsystem<asIScriptEngine>();
[/quote]
doesn"t work too ...
i've looking in the engine part where you register angel script part, nothing inherit, it ssem to be in the register script the trick to grab the Angel SCript instance to register it

i learn stuff but always somethings block me

-------------------------

cadaver | 2017-01-02 00:58:35 UTC | #9

You get the asIScriptEngine pointer from the Script subsystem.

[code]
    asIScriptEngine* engine = GetSubsystem<Script>()->GetScriptEngine();
[/code]

-------------------------

gasp | 2017-01-02 00:58:36 UTC | #10

thank you for the information, i get the following error :
[code]
D:\Developpement\testProject\Source\Urho3DPlayer.cpp:116:15: error: invalid use of incomplete type 'class asIScriptEngine'
         engine->RegisterObjectMethod("SimpleMath", "int  SimpleMath::DoubleTheValue(int value)", asMETHOD(SimpleMath, DoubleTheValue), asCALL_THISCALL);
               ^
In file included from D:\Developpement\testProject\Source\Urho3DPlayer.cpp:32:0:
D:/Developpement/Urho3D/Source/Engine/Script/ScriptFile.h:31:7: error: forward declaration of 'class asIScriptEngine'
 class asIScriptEngine;
[/code]

my code : 
[code]
void Urho3DPlayer::Start()
{

#ifdef ENABLE_ANGELSCRIPT
        // Instantiate and register the AngelScript subsystem
        context_->RegisterSubsystem(new Script(context_));
        asIScriptEngine* engine = GetSubsystem<Script>()->GetScriptEngine();
        engine->RegisterObjectMethod("SimpleMath", "int  SimpleMath::DoubleTheValue(int value)", asMETHOD(SimpleMath, DoubleTheValue), asCALL_THISCALL);

[/code]
i regulary from all my test get "error: invalid use of incomplete type 'class asIScriptEngine' "

-------------------------

GIMB4L | 2017-01-02 00:58:36 UTC | #11

You need to include the angelscript header file, or some other header which includes it.

-------------------------

gasp | 2017-01-02 00:58:36 UTC | #12

thanks you, it work, what i've done :

[code]

#include <angelscript.h>

String doubleTheNumber (int t){
        char buff[32];
        sprintf(buff, "%d", t*2);   // int => Char
        String ss(buff);
return ss;
}
[/code]
In the "void Urho3DPlayer::Start()" function : 
[code]
#ifdef ENABLE_ANGELSCRIPT
        // Instantiate and register the AngelScript subsystem
        context_->RegisterSubsystem(new Script(context_));
        asIScriptEngine* engine = GetSubsystem<Script>()->GetScriptEngine();
        engine->RegisterGlobalFunction("String doubleTheNumber (int t)", asFUNCTION(doubleTheNumber), asCALL_CDECL);
[/code]

and in the .as script : 
[code]
Print(testFunt(10));
[/code]
(next part is doing in the same with a class :p)
and you get 20 in the console :p

-------------------------

Azalrion | 2017-01-02 00:58:36 UTC | #13

[quote="GIMB4L"]You need to include the angelscript header file, or some other header which includes it.[/quote]

Just for the record so no one goes searching the angelscript.h file isn't included by the engine in any header files, its forward decl'd and included in the cpp files.

-------------------------

gasp | 2017-01-02 00:58:38 UTC | #14

Using a methode of a c++ class  in an Uhro3D angel script :
1st we create a sample class (.cpp & .h)
[u]SimpleMath.cpp:[/u]
[code]

#include "SimpleMath.h"

void SimpleMath::testSanRien(){
int i;
i=i+1;
}

//Double the Value !!!
Urho3D::String  SimpleMath::DoubleTheValue(int value)
{
  char buff[32];
  sprintf(buff, "%d", value*2);   // int => Char
  Urho3D::String ss(buff);
return ss;
}
[/code]
[u]SimpleMath.h file :[/u]
[code]



class SimpleMath
{
public:
    Urho3D::String DoubleTheValue(int value);
    void testSanRien();
private:
    int myPrivateValueNotUsedForNow(0);
};

[/code]


now in you'r [u]main.cpp[/u] file :
[code]
...

#include <angelscript.h>
#include "SimpleMath.h"
...
void Urho3DPlayer::Start()
{
    int r(0);
        // Instantiate and register the AngelScript subsystem
        context_->RegisterSubsystem(new Script(context_));
        asIScriptEngine* engine = GetSubsystem<Script>()->GetScriptEngine();
            //Register a global function
        engine->RegisterGlobalFunction("String doubleTheNumber (int t)", asFUNCTION(doubleTheNumber), asCALL_CDECL);
        assert( r >= 0 );
            // Registering the type "simplemath"
        engine->RegisterObjectType("simplemath", sizeof(SimpleMath), asOBJ_VALUE | asOBJ_POD | asOBJ_APP_CLASS_CAK);
        assert( r >= 0 );
            // Registering without argument
        engine->RegisterObjectMethod("simplemath", "void testSanRien()", asMETHOD(SimpleMath,testSanRien), asCALL_THISCALL);
        assert( r >= 0 );
            //With arguments
        engine->RegisterObjectMethod("simplemath", "String DoubleTheValue(int value)",asMETHODPR(SimpleMath, DoubleTheValue,(int),String), asCALL_THISCALL);
        assert( r >= 0 );

...

[/code]

and lastly in you'r .as scripts :

[code]
		//Global Function
	Print(doubleTheNumber (10));
		//With a class
	simplemath veryComplexMath;
		//Testing the value
	Print(veryComplexMath.DoubleTheValue(33));
[/code]

Now you can see the result in the console "20" and "66".

hope this had help someone, and i've not make alot of mistake

-------------------------

Azalrion | 2017-01-02 00:58:38 UTC | #15

Just be careful there you aren't actually assigning r to the return values of the angelscript binding calls and its not initialized so that assert would run all kinds of crazy on some compilers.

When binding simplemath you've used sizeof(StringHash) that should be sizeof(SimpleMath), it might not make a difference since we don't use AS garbage collector, I haven't looked to see the implications of the size specifications in the bindings.

asOBJ_POD you need to be careful with as well when declaring object types , it should only be used If the type doesn't require any special treatment, i.e. doesn't contain any pointers or other resource references that must be maintained.

Otherwise that it looks good, (oh you did copy the .cpp code instead of the header code into the simplemath.h example).

-------------------------

gasp | 2017-01-02 00:58:39 UTC | #16

thanks for all the remark, very instructive, once all i clear i will correct my post for reference

When declaring type "asOBJ_POD" seem to be medatory, if i don't set it i get : 
[quote]
"SimpleMath is missing behaviours"
"Invalid configuration. Verify the registered application interface
"Failed to compile script module"
[/quote]

correted the .h file

-------------------------

Azalrion | 2017-01-02 00:58:39 UTC | #17

[quote="gasp"]When declaring type "asOBJ_POD" seem to be medatory, if i don't set it i get : [/quote]

Yep in your case its needed because you're not declaring any constructors or destructors as part of the binding, so when it sees asOBJ_POD Angelscript will just use a default constructor, if you don't declare it you need to register the asBEHAVE (I think it is) for Ctors and Dtors.

Just one last thing I noticed, to use the assert properly it should be;

[code]
r = engine->RegisterObjectMethod("simplemath", "void testSanRien()", asMETHOD(SimpleMath,testSanRien), asCALL_THISCALL);
assert(r >= 0);
[/code]

Calling any angelscript RegisterXXX method returns an int value that is either 0 or less than 0 which then points to a specific error. So to catch the assert properly each time you call a register method you should be assigning r like above.

-------------------------

