noals | 2017-01-02 01:11:27 UTC | #1

hi,

i try to make my own class and functions but i don't know how to initialise scene, cache or others nodes within it so that when i use my function in the main.cpp, it use the nodes already set.
could someone tell me how to do that please ?
here is the function i'm trying to make.

[code]
void Module::addRandomModule(Scene* scene, ResourceCache* cache, int m_id)
{

    const char* moduleX;

    //XML
    tinyxml2::XMLDocument modules;
    modules.Parse("Data/Scripts/Modules.xml");
    if(modules.LoadFile("Data/Scripts/Modules.xml") == tinyxml2::XML_NO_ERROR)
    {
        tinyxml2::XMLNode* root = modules.FirstChild();
        tinyxml2::XMLElement* infos = root->FirstChildElement("infos");
        infos->QueryIntAttribute("count", &modulesCount);
        int randomLine = chooseRandomLine(modulesCount);

        std::string module = ("module");
        {
            std::ostringstream ss;
            ss<<randomLine;
            std::string s(ss.str());
            module.append(s);
        }
        moduleX = module.c_str();

        tinyxml2::XMLElement* randomModule = root->FirstChildElement(moduleX);
        randomModule->QueryIntAttribute("type", &m_type); //moduletype);
        randomModule->QueryIntAttribute("exits", &m_exits);
           
        m_path = randomModule->Attribute("path");
        m_texturepath = randomModule->Attribute("texturepath");
    }

    std::string moduleName = ("");
    {
        std::ostringstream ss;
        ss<<m_id<<moduleX;
        std::string s(ss.str());
        moduleName.append(s);
    }
    m_name = moduleName.c_str();


    moduleNode=scene->CreateChild(m_name); 
    moduleNode->SetPosition(Vector3(0,0,0));
    AnimatedModel* moduleObject=moduleNode->CreateComponent<AnimatedModel>();
    moduleObject->SetModel(cache->GetResource<Model>(m_path));
    moduleObject->SetMaterial(cache->GetResource<Material>(m_texturepath));

}
[/code]



the class WIP :
[spoiler]module.h
[code]
#ifndef MODULE_H
#define MODULE_H

#include <Urho3D/Math/Vector3.h>
using namespace Urho3D;

class Module
{
    private:
    int m_id;
    const char* m_name;
    int m_type;
    int m_exits;
    const char* m_path;
    const char* m_texturepath;

    public:
    Module(); //constructeur
    ~Module(); //destructeur

    void addRandomModule(Scene* scene, ResourceCache* cache, int m_id);
    int getType(void);
    int getExits(void);

    void setPosition(Vector3 modulePos);
};

#endif[/code]

module.cpp
[code]
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/InputEvents.h>

#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Resource/XMLFile.h>
#include <Urho3D/IO/Log.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/UI/Button.h>
#include <Urho3D/UI/UIEvents.h>
#include <Urho3D/UI/Window.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Scene/SceneEvents.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/Geometry.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Graphics/DebugRenderer.h>
#include <Urho3D/Graphics/Octree.h>
#include <Urho3D/Graphics/Light.h>
#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Graphics/StaticModel.h>
#include <Urho3D/Graphics/AnimatedModel.h>
#include <Urho3D/Graphics/Material.h>
#include <Urho3D/Graphics/Skybox.h>
#include <Urho3D/UI/Window.h>
#include <Urho3D/Math/Vector3.h>


#include <string>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <time.h>



//my stuff
#include "tinyxml2.h"
#include "fonctions.h"
#include "Module.h"

int modulesCount;

Module::Module() //constructeur qui initialise
{
    int m_id; // = 0;
    const char* m_name;
    int m_type; // = 0;
    int m_exits; // = 0;
    const char* m_path; // = "";
    const char* m_texturepath; // = "";
}

Module::~Module() //destructeur
{

}

void Module::addRandomModule(Scene* scene, ResourceCache* cache, int m_id)
{

    const char* moduleX;

    //XML
    tinyxml2::XMLDocument modules;
    modules.Parse("Data/Scripts/Modules.xml");
    if(modules.LoadFile("Data/Scripts/Modules.xml") == tinyxml2::XML_NO_ERROR)
    {
        tinyxml2::XMLNode* root = modules.FirstChild();
        tinyxml2::XMLElement* infos = root->FirstChildElement("infos");
        infos->QueryIntAttribute("count", &modulesCount);
        int randomLine = chooseRandomLine(modulesCount);

        std::string module = ("module");
        {
            std::ostringstream ss;
            ss<<randomLine;
            std::string s(ss.str());
            module.append(s);
        }
        moduleX = module.c_str();

        tinyxml2::XMLElement* randomModule = root->FirstChildElement(moduleX);
        randomModule->QueryIntAttribute("type", &m_type); //moduletype);
        randomModule->QueryIntAttribute("exits", &m_exits);
           
        m_path = randomModule->Attribute("path");
        m_texturepath = randomModule->Attribute("texturepath");
    }

    std::string moduleName = ("");
    {
        std::ostringstream ss;
        ss<<m_id<<moduleX;
        std::string s(ss.str());
        moduleName.append(s);
    }
    m_name = moduleName.c_str();

    moduleNode=scene->CreateChild(m_name); 
    moduleNode->SetPosition(Vector3(0,0,0));
    AnimatedModel* moduleObject=moduleNode->CreateComponent<AnimatedModel>();
    moduleObject->SetModel(cache->GetResource<Model>(m_path));
    moduleObject->SetMaterial(cache->GetResource<Material>(m_texturepath));

}

int Module::getType(void)
{
    return m_type;
}

int Module::getExits(void)
{
    return m_exits;
}

void Module::setPosition(Vector3 modulePos)
{

}[/code][/spoiler]

-------------------------

noals | 2017-01-02 01:11:27 UTC | #2

i'm sorry, i didn't mean to troll or something, the code for that is kinda ok in my previous post. it just missed the initialisation of the moduleNode but i have some crash problems, it drives me a little crazy.
problems with initialisation to null and stuff like that, i never had to use it before and surprisingly, all my stuff worked fine before so i have a little hard time initialising everything fine. ><

-------------------------

Modanung | 2017-01-02 01:11:27 UTC | #3

Initializing member values in the constructor head is preferable over redefining them in the constructor body:
[code]Module::Module() : //constructeur qui initialise
    m_id{0},
    m_name{},
    m_type{0},
    m_exits{0},
    m_path{""},
    m_texturepath{""}
{
}[/code]

Rather than creating an empty [b]de[/b]structor, don't write one at all. (From Stroustrup's Tour of C++)

-------------------------

noals | 2017-01-02 01:11:28 UTC | #4

[quote]Initializing member values in the constructor head is preferable over redefining them in the constructor body[/quote]
thx but what is the difference ? is the access method still the same ?

here i'm struggling trying to use GetWorldPosition() in my own getPosition() but i didn't even defined a position to begin with in my class... >< i hate classes.

-------------------------

Modanung | 2017-01-02 01:11:28 UTC | #5

[quote="noals"]thx but what is the difference ? is the access method still the same ?[/quote]
The way you had set up the statements in the constructor, with data types mentioned, they were being redefined. This means a temporary object with the same name is created that is deleted at the end of the constructor's body, causing ambiguity. This is obviously not what you want in this case.
Just leaving out the data types and removing the slashes would have been enough, but initializing them this way is less error prone. [url=http://stackoverflow.com/a/18222927/3618748]Why?[/url]

-------------------------

noals | 2017-01-02 01:11:29 UTC | #6

thx for the link. i have the book actually (i guess i will check the whole chapter later) but i never really paid attention to memory allocation.

about the temporary object, you're right, the modules are to build a dungeon, i won't change them while running of later for fun but that's not my priority.
if i can do my class properly, next i already need to do another one that will represent each exits for each random modules, and then i will need to stock them and be able to update their list or whatever. ^^;

-------------------------

noals | 2017-01-02 01:11:29 UTC | #7

[quote="Modanung"]Initializing member values in the constructor head is preferable over redefining them in the constructor body:
[code]Module::Module() : //constructeur qui initialise
    m_id{0},
    m_name{};
    m_type{0},
    m_exits{0},
    m_path{""},
    m_texturepath{""}
}
}[/code]

Rather than creating an empty [b]de[/b]structor, don't write one at all. (From Stroustrup's Tour of C++)[/quote]

it seem i can't use your method, it don't compile because it don't use c++11.
and the other method compile but my application crash and i don't understand the message of the debugger. it seem i'm missing a file but i wonder why it would need it all of a sudden lol
[quote]Program received signal SIGSEGV, Segmentation fault.
0x00007ffff6990742 in _IO_vfscanf_internal (s=s@entry=0x7fffffffd460, 
    format=format@entry=0xe7b39c "%d", argptr=argptr@entry=0x7fffffffd588, 
    errp=errp@entry=0x0) at vfscanf.c:1857
1857	vfscanf.c: Aucun fichier ou dossier de ce type.
[/quote]

could you help me correct my class please ? or do you know how i can set my compiler to not have this problem ? i installed the build-essential packet on ubuntu and use make to compile, i think i need to add a -std=c++11 or -std=gnu++11 option somewhere but i don't know where.

module.h
[code]
#ifndef MODULE_H
#define MODULE_H

#include <Urho3D/Math/Vector3.h>
using namespace Urho3D;

class Module
{
    private:
    Node* m_node;
    int m_id;
    const char* m_name;
    int m_type;
    int m_exits;
    const char* m_path;
    const char* m_texturepath;
    Vector3 m_position;

    public:
    Module(); //constructeur

    void addRandomModule(Scene* scene, ResourceCache* cache, int m_id);
    int getType(void);
    int getExits(void);

    Vector3 getPosition();
    void setPosition(Vector3 position);
};

#endif
[/code]


module.cpp
[code]
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/InputEvents.h>

#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Resource/XMLFile.h>
#include <Urho3D/IO/Log.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/UI/Button.h>
#include <Urho3D/UI/UIEvents.h>
#include <Urho3D/UI/Window.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Scene/SceneEvents.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/Geometry.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Graphics/DebugRenderer.h>
#include <Urho3D/Graphics/Octree.h>
#include <Urho3D/Graphics/Light.h>
#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Graphics/StaticModel.h>
#include <Urho3D/Graphics/AnimatedModel.h>
#include <Urho3D/Graphics/Material.h>
#include <Urho3D/Graphics/Skybox.h>
#include <Urho3D/UI/Window.h>
#include <Urho3D/Math/Vector3.h>


#include <string>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <time.h>



//my stuff
#include "tinyxml2.h"
#include "fonctions.h"
#include "Module.h"

int modulesCount; //setting file class ?

Module::Module()//constructeur qui initialise,  cant use list without c++11
{
    Node* m_node;
    int m_id=0;
    const char* m_name="";
    int m_type=0;
    int m_exits=0;
    const char* m_path="";
    const char* m_texturepath="";
    Vector3 m_position(0, 0, 0);
}

void Module::addRandomModule(Scene* scene, ResourceCache* cache, int m_id)
{

    const char* moduleX;

    //XML
    tinyxml2::XMLDocument modules;
    modules.Parse("Data/Scripts/Modules.xml");
    if(modules.LoadFile("Data/Scripts/Modules.xml") == tinyxml2::XML_NO_ERROR)
    {
        tinyxml2::XMLNode* root = modules.FirstChild();
        tinyxml2::XMLElement* infos = root->FirstChildElement("infos");
        infos->QueryIntAttribute("count", &modulesCount);
        int randomLine = chooseRandomLine(modulesCount);

        std::string module = ("module");
        {
            std::ostringstream ss;
            ss<<randomLine;
            std::string s(ss.str());
            module.append(s);
        }
        moduleX = module.c_str();

        tinyxml2::XMLElement* randomModule = root->FirstChildElement(moduleX);
        randomModule->QueryIntAttribute("type", &m_type); //moduletype);
        randomModule->QueryIntAttribute("exits", &m_exits);
           
        m_path = randomModule->Attribute("path");
        m_texturepath = randomModule->Attribute("texturepath");
    }

    std::string moduleName = ("");
    {
        std::ostringstream ss;
        ss<<m_id<<moduleX;
        std::string s(ss.str());
        moduleName.append(s);
    }
    m_name = moduleName.c_str();


    m_node=scene->CreateChild(m_name);
    m_node->SetPosition(m_position);
    AnimatedModel* moduleObject=m_node->CreateComponent<AnimatedModel>();
    moduleObject->SetModel(cache->GetResource<Model>(m_path));
    moduleObject->SetMaterial(cache->GetResource<Material>(m_texturepath));

}

int Module::getType(void)
{
    return m_type;
}

int Module::getExits(void)
{
    return m_exits;
}

void Module::setPosition(Vector3 position)
{
    m_node->SetPosition(position);
}

Vector3 Module::getPosition(void)
{
    return m_node->GetWorldPosition();
}
[/code]


and i tryed to use it like that in the main.cpp
[code]
Module* module1;
module1->addRandomModule(my_scene, cache, 1);
module1->setPosition(Vector3(0,0,0));
[/code]

-------------------------

noals | 2017-01-02 01:11:31 UTC | #8

nevermind, i will try using struct and reorganising my code. i kinda want to do everything at the same time but i lack methodology here.

-------------------------

Dave82 | 2017-01-02 01:11:31 UTC | #9

[quote]"hx but what is the difference ? is the access method still the same ?"[/quote]

The other problem with that is faster to initialize a variable rather than initialize it and then assign a value to it inside the constructor.Constructor allows you to initilize member variables by a specific value in one go (e.g it is lot faster).

[quote]it seem i can't use your method, it don't compile because it don't use c++11.
and the other method compile but my application crash and i don't understand the message of the debugger. it seem i'm missing a file but i wonder why it would need it all of a sudden lol[/quote]

Thats nothing to do with c++ 11. class member initialization was always part of c++. The problem is Modanung made a mistake by using curly brackets after the variables and not round brackets.
This should work :
[code]Module::Module() : //constructeur qui initialise
    m_id(0),
    m_name(),
    m_type(0),
    m_exits(0),
    m_path(0),
    m_texturepath(0)
}
{[/code]


Also is there a reason you use const char* for strings ? Why not just use Urho's String ? You could also create classes derived from LogicComponent so you can easily access the scene or the component's node or all the SubSystems inside the component

-------------------------

Modanung | 2017-01-02 01:11:31 UTC | #10

[quote="Dave82"]The problem is Modanung made a mistake by using curly brackets after the variables and not round brackets.[/quote]
[url=https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#es23-prefer-the--initializer-syntax]C++ Core Guidelines[/url]

-------------------------

Dave82 | 2017-01-02 01:11:31 UTC | #11

[quote="Modanung"][quote="Dave82"]The problem is Modanung made a mistake by using curly brackets after the variables and not round brackets.[/quote]
[url=https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#es23-prefer-the--initializer-syntax]C++ Core Guidelines[/url][/quote]

You can't initialize variables with {} in a constructor

This is OK
[code]SomeClass::SomeClass():
     member1(0),
     member2(123),
     stringMemebr("something")
{
}[/code]

This is worong :
[code]SomeClass::SomeClass():
     member1{0},
     member2{123},
     stringMemebr{"something"}
{
}[/code]

-------------------------

Modanung | 2017-01-02 01:11:31 UTC | #12

Try it

-------------------------

Dave82 | 2017-01-02 01:11:32 UTC | #13

[quote="Modanung"]Try it[/quote]

Tried it , it doesn't work...

-------------------------

Modanung | 2017-01-02 01:11:32 UTC | #14

[quote="Dave82"]Tried it , it doesn't work...[/quote]
Update something

-------------------------

Dave82 | 2017-01-02 01:11:32 UTC | #15

[quote="Modanung"][quote="Dave82"]Tried it , it doesn't work...[/quote]
Update something[/quote]


Thats nothing to do with updating... it just doesn't work.I used hundreds of open source c++ libraries , and not a single one used {} for member initializing.
From the other hand you first post doesn't even make sense :

[quote]Module::Module() : //constructeur qui initialise
    m_id{0},
    m_name{};
    m_type{0},
    m_exits{0},
    m_path{""},
    m_texturepath{""}
}
}[/quote]
You used the {} at the end facing the same direction thus you opening another scope and never close them, so that's i'm dead certain won't work.Also notice the ; and , mixed in the parameter list... That code won't compile on any compiler

-------------------------

Modanung | 2017-01-02 01:11:32 UTC | #16

[quote="Dave82"]You used the {} at the end facing the same direction thus you opening another scope and never close them, so that's i'm dead certain won't work.Also notice the ; and , mixed in the parameter list... That code won't compile on any compiler[/quote]
You're right about the typos, and round brackets do work just fine... it's just that Stroustrup advises to use curly brackets, even in the constructor's head because "The rules for {} initialization are simpler, more general, less ambiguous, and safer than for other forms of initialization.". It works fine for me, and it takes a while for veterans to adapt.

-------------------------

Dave82 | 2017-01-02 01:11:32 UTC | #17

[quote="Modanung"][quote="Dave82"]You used the {} at the end facing the same direction thus you opening another scope and never close them, so that's i'm dead certain won't work.Also notice the ; and , mixed in the parameter list... That code won't compile on any compiler[/quote]
You're right about the typos, and round brackets do work just fine... it's just that Stroustrup advises to use curly brackets, even in the constructor's head because "The rules for {} initialization are simpler, more general, less ambiguous, and safer than for other forms of initialization.". It works fine for me, and it takes a while for veterans to adapt.[/quote]

May i ask which compiler you use ? i NEVER EVER saw any newer or older libraries ever used curly brackets in initializing... and just tried in any possible way it won't compile...

-------------------------

Modanung | 2017-01-02 01:11:32 UTC | #18

[quote="Dave82"]May i ask which compiler you use?[/quote]
gcc 5.2.1
And you?

-------------------------

Dave82 | 2017-01-02 01:11:32 UTC | #19

Ok as i see the Initializer lists are c++ 11 features.

-------------------------

Dave82 | 2017-01-02 01:11:32 UTC | #20

[quote="Modanung"]
And you?[/quote]

visual c++ 2008 and 2010 (but mostly 2008)

-------------------------

Modanung | 2017-01-02 01:11:32 UTC | #21

Which makes me wonder what reasons you (both) have to not use c++11 in 2016. Old VS?
I only started programming two years ago and never wrote code with a before-11 standard.

-------------------------

Dave82 | 2017-01-02 01:11:32 UTC | #22

[quote="Modanung"]Which makes me wonder what reasons you (both) have to not use c++11 in 2016.[/quote]

Good question.To be honest i don't see any real adventages of c++ 11 right now. But i will switch to vs 2015 once i buy a new PC. On this system i have everything i need and the workflow i use works perfectly for years.So why change. Using vs 2015 would be practical only because has all in one solution for all popular platforms (even android).I just don't want to change my compiler to have c++ 11 features right now.If urho changes to c++ 11 i will change too , but till then it's all fine like it is

Also my OS is 5 years old and my hdd is filled with crap :smiley:, so it would take a month to backup and save everything... i'm not in the mood to do that right now

-------------------------

Modanung | 2017-01-02 01:11:32 UTC | #23

[quote="Dave82"]To be honest i don't see any real adventages of c++ 11 right now.[/quote]
How about being able to compile code that was written using newly introduced features? :slight_smile:

And I guess IDE is a personal preference, but I loathe VS and prefer [url=http://www.qt.io/download/]QtCreator[/url] for many reasons.
Since your OS 5 years old... why not give Linux a try instead of turning you machine into a [url=https://en.wikipedia.org/wiki/Telescreen]telescreen[/url]?

-------------------------

Dave82 | 2017-01-02 01:11:32 UTC | #24

[quote="Modanung"][quote="Dave82"]To be honest i don't see any real adventages of c++ 11 right now.[/quote]
How about being able to compile code that was written using newly introduced features? :slight_smile:

And I guess IDE is a personal preference, but I loathe VS and prefer [url=http://www.qt.io/download/]QtCreator[/url] for many reasons.[/quote]

Yeah it is a personal taste.I'm kinda guy who like to focus more on programming side.I used CodeBlocks , Eclipse , NEtbeans , CodeLite , but non of them comes close to VS.
To tell you the truth Eclipse was the worst editor i ever tried in my life.I can't even imagine how could people actually use that... editor ? It has so many glitches that you need 2 months to find workarounds to even start to work with and the gui design is absolute disgrace... (after googleing around i saw i'm not the only one who thinks that way).Net beans is bit better but has same flaws , I like Code blocks almost as VS but it has (had ? i didn't used it in a while) some annoying problems i don't like (doesn't show definition and declarations of classes , shows member functions on both. and -> operators , etc)

-------------------------

Modanung | 2017-01-02 01:11:32 UTC | #25

[quote="Dave82"]shows member functions on both. and -> operators[/quote]
Well, it should, right? As long as they are public.
I though VS had a lot of extra features I didn't need, which made the UI and shortkeys needlessly cluttered. In QtCreator I never missed a feature and it doesn't suffer from platform-lock.

-------------------------

Dave82 | 2017-01-02 01:11:32 UTC | #26

[quote="Modanung"][quote="Dave82"]shows member functions on both. and -> operators[/quote]
Well, it should, right? As long as they are public.[/quote]

the -> should work only on pointers and . only for stack variables. Well i'm just too picky but in some situations could be confusing.You press the -> operatort on an external variable you don't know it's not a pointer , it will still list it's functions .You select the function and you are confident you did it right , but the code won't compile because the variable does not have an overloaded member 'operator ->"... It's not a must have feature , but if MS could do it why CodeBlocks not ?

[quote]I though VS had a lot of extra features I didn't need, which made the UI and shortkeys needlessly cluttered. In QtCreator I never missed a feature and it doesn't suffer from platform-lock.[/quote]
Yes.Since VS tries to be out of the box one click solution. But VS is no longer tied to Windows only. the 2015 became an all in one tool for all possible platforms.
[visualstudio.com/en-us/feat ... nt-vs.aspx](https://www.visualstudio.com/en-us/features/mobile-app-development-vs.aspx)

-------------------------

Modanung | 2017-01-02 01:11:33 UTC | #27

Ah, even for non-pointers -> would show the object's members? Yea, that should not be.

-------------------------

noals | 2017-01-02 01:11:33 UTC | #28

[quote="Dave82"]Also is there a reason you use const char* for strings ? Why not just use Urho's String ? You could also create classes derived from LogicComponent so you can easily access the scene or the component's node or all the SubSystems inside the component[/quote]
at some point it was convenient for some conversion but yes, i need to use string.
i tryed to use structs, programming functions after functions to see if there was a problem and at some point, the debugger showed me that my "string" wasn't returned fully by the const char*. i will check that tomorrow.

[quote="Dave82"]Ok as i see the Initializer lists are c++ 11 features.[/quote]
yep.

[quote="Modanung"]Which makes me wonder what reasons you (both) have to not use c++11 in 2016. Old VS?
I only started programming two years ago and never wrote code with a before-11 standard.[/quote]
i tryed codeblock and visual studio before but i use linux (ubuntu) for programming here. i just followed few tutorials to know how to compile c++ code, installing some basic packages apparently and i use gedit (kind of notepad) to code. i didn't know there was some kind of c++ updates.

-------------------------

Modanung | 2017-01-02 01:11:33 UTC | #29

[quote="Dave82"]But VS is no longer tied to Windows only[/quote]
You may be able to compile for other platforms. But VS still requires windows to run and be used. It is therefore not a cross-platform program; it suffers from [url=https://en.wikipedia.org/wiki/Vendor_lock-in]platform lock[/url].

[quote="noals"]...and i use gedit (kind of notepad) to code.[/quote]
Wow, coding without code completion? That's oldskool-hardcore, dude. :stuck_out_tongue:
Seriously: [i]sudo apt-get install qtcreator[/i]
Or search for QtCreator in the software center. You won't regret it.

-------------------------

noals | 2017-01-02 01:11:33 UTC | #30

[quote="Modanung"]Wow, coding without code completion? That's oldskool-hardcore, dude. :stuck_out_tongue:
Seriously: sudo apt-get install qtcreator
Or search for QtCreator in the software center. You won't regret it.[/quote]
it's not that hard but yeah, code completion could be helpfull.

[quote="noals"][quote="Dave82"]Also is there a reason you use const char* for strings ? Why not just use Urho's String ? You could also create classes derived from LogicComponent so you can easily access the scene or the component's node or all the SubSystems inside the component[/quote]
at some point it was convenient for some conversion but yes, i need to use string.
i tryed to use structs, programming functions after functions to see if there was a problem and at some point, the debugger showed me that my "string" wasn't returned fully by the const char*. i will check that tomorrow.[/quote]
after verification, const char* help me because i don't need to convert between urho3D::String, std::string and const char*, i use const char* because it kinda fits everywhere but it's also my actual problem because it seem const char* return my value but return it with a random length, could you tell me why or help me fix that ?

for exemple, i made my struct :
[code]
typedef struct Module
{
    int m_id;
    const char* m_name; 
    int m_type;
    int m_exits;
    const char* m_path;
    const char* m_texturepath;
    Vector3 m_position;
} Module ;[/code]
then i get a path from a xml with this line: (i use tinyxml2, i can't use urho3D::String here)
[code]
module.m_path = randomModule->Attribute("path");[/code]
then i load the module : (where i need a urho3D::String but it's almost ^^; working with const char* and don't with std::string)
[code]
m_Object->SetModel(cache->GetResource<Model>(module.m_path));[/code]
and sometime, i verify my values with urho3D::Text and i convert everything in one urho3D::String.
[code]
        std::string str = (""); 
        {
            std::ostringstream ss;
            ss<<" moduleXMLcount = "<<moduleXMLcount
              <<"\n randomModule = "<<randomModule;
                //<<"\n type = "<<moduleType
                //<<"\n exits = "<<exits
                //<<"\n path = "<<module1.m_path;
                //<<"\n texturepath = "<<moduleTexturePath

            std::string s(ss.str());
            str.append(s);    //str.append(s.substr(0,60));
        }

        String s(str.c_str(),str.size());[/code]

i would be happy if i can get it working with const char* actually, i didn't took the time to do some conversion functions yet but maybe that's the time to do it lol.

-------------------------

Dave82 | 2017-01-02 01:11:33 UTC | #31

[quote="noals"][quote="Modanung"]Wow, coding without code completion? That's oldskool-hardcore, dude. :stuck_out_tongue:
Seriously: sudo apt-get install qtcreator
Or search for QtCreator in the software center. You won't regret it.[/quote]
it's not that hard but yeah, code completion could be helpfull.

[quote="noals"][quote="Dave82"]Also is there a reason you use const char* for strings ? Why not just use Urho's String ? You could also create classes derived from LogicComponent so you can easily access the scene or the component's node or all the SubSystems inside the component[/quote]
at some point it was convenient for some conversion but yes, i need to use string.
i tryed to use structs, programming functions after functions to see if there was a problem and at some point, the debugger showed me that my "string" wasn't returned fully by the const char*. i will check that tomorrow.[/quote]
after verification, const char* help me because i don't need to convert between urho3D::String, std::string and const char*, i use const char* because it kinda fits everywhere but it's also my actual problem because it seem const char* return my value but return it with a random length, could you tell me why or help me fix that ?

for exemple, i made my struct :
[code]
typedef struct Module
{
    int m_id;
    const char* m_name; 
    int m_type;
    int m_exits;
    const char* m_path;
    const char* m_texturepath;
    Vector3 m_position;
} Module ;[/code]
then i get a path from a xml with this line: (i use tinyxml2, i can't use urho3D::String here)
[code]
module.m_path = randomModule->Attribute("path");[/code]
then i load the module : (where i need a urho3D::String but it's almost ^^; working with const char* and don't with std::string)
[code]
m_Object->SetModel(cache->GetResource<Model>(module.m_path));[/code]
and sometime, i verify my values with urho3D::Text and i convert everything in one urho3D::String.
[code]
        std::string str = (""); 
        {
            std::ostringstream ss;
            ss<<" moduleXMLcount = "<<moduleXMLcount
              <<"\n randomModule = "<<randomModule;
                //<<"\n type = "<<moduleType
                //<<"\n exits = "<<exits
                //<<"\n path = "<<module1.m_path;
                //<<"\n texturepath = "<<moduleTexturePath

            std::string s(ss.str());
            str.append(s);    //str.append(s.substr(0,60));
        }

        String s(str.c_str(),str.size());[/code]

i would be happy if i can get it working with const char* actually, i didn't took the time to do some conversion functions yet but maybe that's the time to do it lol.[/quote]


I still can't get why are you forcing the const char * so badly ? It's the most inconvenient way of storing a string.Urho has a string class which can actually return a valid nullterminated c string (myString.CString()) and you can build std string form it anytime you need it.And you could ask yourself "Do i REALLY need std::string ? Do i need so many string types ?". If the reason you use std::string just to build a stringstream
 with the << operator , thats not really valid reason. You can do that with Urho string too.
[code]Urho3D::String str;
str += " moduleXMLcount = ";
str += moduleXMLcount;
str += "\n randomModule = ";
str += randomModule;
str +=  "\n type = ";
str += moduleType;
str +=  "\n exits = ";
str += exits;
str += "\n path = ";
str += module1.m_path;
str +=  "\n texturepath = " + moduleTexturePath;[/code]

[quote]it seem const char* return my value but return it with a random length[/quote]
just a guess but thats because probably it's not null terminated ?

-------------------------

noals | 2017-01-02 01:11:33 UTC | #32

[quote="Dave82"]just a guess but thats because probably it's not null terminated ?[/quote]
yes, i just read a little about it, i didn't know it was like that with char.

so i tryed std::string and it seem to go well.
[code]
using namespace Urho3D;

String string2urhoString(std::string stdstring)
{
    String urString(stdstring.c_str(),stdstring.size());
    return urString;
}
[/code]

but now, i already have a problem with the module node. (it never end ><)
i guess it's not updated as i expected. i will try other things.
here is my project if you want to take a look :
[s000.tinyupload.com/index.php?fi ... 8104735121](http://s000.tinyupload.com/index.php?file_id=29900913548104735121)

this version crash, you can double slash those line in the main.cpp to avoid that :
[code]        camNode->LookAt(m_node->GetWorldPosition());  //target to begin with ///////////////////////////////////[/code]
[code]                camNode->LookAt(m_node->GetWorldPosition()); //look at room////////////////////////////[/code]

-------------------------

noals | 2017-01-02 01:11:34 UTC | #33

kinda found out. i don't even need to use the node, i just can use :
[quote]camNode->LookAt(module.m_position);[/quote]

-------------------------

noals | 2017-01-02 01:11:48 UTC | #34

i still can't get it to work properly, or i forgot something again, i don't know, it drives me crazy.

i made a class for my modules. here is the Room class i try to use : (i wasnt sure about your constructor method so i tryed the other one.)

in my [b]Module.h[/b]
[code]
class Room
{
    public:
    int type;
    int exit;
    std::string path;
    std::string texturepath;
    Vector3 position;
    Vector3 rotation; //direction in urho, did i need to change bone orientation in blender ?
    
    Room();
    void loadRoom(int id, Scene* scene, ResourceCache* cache);
};
[/code]

in my [b]Module.cpp[/b]
[code]
Counts XMLcounts;


Room::Room()
{
    //default values
    type=0;
    exit=0;
    path="";
    texturepath="";
    position=Vector3(0,0,0);
    rotation=Vector3(0,0,0);  //direction in urho, did i need to change bone orientation in blender ?
}
void Room::loadRoom(int id, Scene* scene, ResourceCache* cache)
{

    int roomNbr = chooseRandomNbr(XMLcounts.room_count);
    std::string roomX = stringInt("room",roomNbr);
    const char* RoomX = roomX.c_str(); //roomX in const char* for tinyxml

    Room room; 
    
    tinyxml2::XMLDocument modules;
    modules.Parse("Data/Scripts/Modules.xml");

    if(modules.LoadFile("Data/Scripts/Modules.xml") == tinyxml2::XML_NO_ERROR)
    {
        tinyxml2::XMLNode* root = modules.FirstChild();
        tinyxml2::XMLElement* randomModule = root->FirstChildElement(RoomX);  //need const char*
        randomModule->QueryIntAttribute("exits", &room.exit);    
        room.path = randomModule->Attribute("path");
        room.texturepath = randomModule->Attribute("texturepath");
    }

    std::string roomName = stringInt("module",id); //room's scene child name
    String room_name = string2urhoString(roomName); //converted to urho string

    String room_path = string2urhoString(room.path);
    String room_texturepath = string2urhoString(room.texturepath);

    Node* r_node;
    r_node=scene->CreateChild(room_name);
    r_node->SetWorldPosition(room.position);  // ATTENTION i need SetPos func for my class
    r_node->SetWorldDirection(room.rotation);  //   !!!
    AnimatedModel* r_Object=r_node->CreateComponent<AnimatedModel>();
    r_Object->SetModel(cache->GetResource<Model>(room_path));
    r_Object->SetMaterial(cache->GetResource<Material>(room_texturepath));
}
[/code]

and that should load a room.
the crazy thing is that it actually load it since the log say so.
[quote]
[Sun Apr 10 17:24:20 2016] DEBUG: Loading resource Models/rooms/room2.mdl
[Sun Apr 10 17:24:20 2016] DEBUG: Loading resource Models/rooms/vert.xml
[Sun Apr 10 17:24:20 2016] DEBUG: Loading resource Techniques/Diff.xml
[Sun Apr 10 17:24:20 2016] DEBUG: Loading resource Models/rooms/Grid.jpg
[/quote]
but it doesn't show in the viewport.

my room should load at the (0,0,0) position.
the camera point to this same position.
[code]
        camNode=my_scene->CreateChild("camNode");
        Camera* camObject=camNode->CreateComponent<Camera>();
        camObject->SetFarClip(2000);
	camNode->SetWorldPosition(Vector3(20,20,20));
        camTarget=my_scene->GetChild("module0");
        camNode->LookAt(Vector3(0,0,0)); //camTarget->GetPosition());  //target to begin with
[/code]
and is updated the same way as well in the handleupdate "[b]camNode->LookAt(Vector3(0,0,0));[/b]"
there are light around so i don't think it is a light problem either.

its maybe a texture problem but i didn't have this problem before so i'm lost.

any ideas why my model doesn't show in the viewport ?

-------------------------

Modanung | 2017-01-02 01:11:49 UTC | #35

[quote="noals"]any ideas why my model doesn't show in the viewport ?[/quote]
Does the model show up in the editor?

-------------------------

noals | 2017-01-02 01:11:49 UTC | #36

yes. i didn't tested them all but i made them all exactly the same way.
they show up in the editor and they also show up in a previous compiled version of my app where models just show up fine.
i also tested with a .png since i had doubt about the .jpg (just took it on google for testing purpose) but it didn't worked either.

the bin --> [s000.tinyupload.com/index.php?fi ... 7466881380](http://s000.tinyupload.com/index.php?file_id=49564613567466881380)

-------------------------

noals | 2017-01-02 01:11:49 UTC | #37

dunno, it's weird, i'm trying things to understand the problem but i don't get it.

i though my class was the problem but if i just try to load my model normaly, it is the same result, it doesn't show up.
[code]
//////////////////////
////    MODULE    ////
//////////////////////

    //MODULE_COUNT=0;
    //room->loadRoom(MODULE_COUNT, my_scene, cache); //abstract room
    //MODULE_COUNT=1;

        Node* r_node;
    r_node=my_scene->CreateChild("test");
    r_node->SetWorldPosition(Vector3(0,0,0));  // ATTENTION i need SetPos func for my class
    r_node->SetWorldDirection(Vector3(0,0,0));  //   !!!
    AnimatedModel* r_Object=r_node->CreateComponent<AnimatedModel>();
    r_Object->SetModel(cache->GetResource<Model>("Models/rooms/room0.mdl"));
    r_Object->SetMaterial(cache->GetResource<Material>("Models/rooms/vert.xml"));

//////////////////////
////    CAMERA    ////
//////////////////////
    camNode=my_scene->CreateChild("camNode");
    Camera* camObject=camNode->CreateComponent<Camera>();
    camObject->SetFarClip(2000);
    camNode->SetWorldPosition(Vector3(20,20,20));
    camTarget=my_scene->GetChild("module0");
    camNode->LookAt(Vector3(0,0,0)); //camTarget->GetPosition());  //target to begin with
[/code]

through i just tested again to be sure with my other bin, no problems with the models.
[url=http://www.hostingpics.net/viewer.php?id=608255modeltest.png][img]http://img15.hostingpics.net/pics/608255modeltest.png[/img][/url]

here is my project (data and coredata are in the previous post link)
[s000.tinyupload.com/index.php?fi ... 5388380872](http://s000.tinyupload.com/index.php?file_id=94843756085388380872)

-------------------------

Modanung | 2017-01-02 01:11:50 UTC | #38

I am at a loss.

To reset a node's rotation I think it's best to use SetRotation(Quaternion::IDENTITY), btw. I noticed some exclamation marks there. :wink:

-------------------------

noals | 2017-01-02 01:11:51 UTC | #39

yeah, it's very frustrating to me. that maybe do a month i'm stuck on this random loading and each time i code it differently to make it better, i encountered another problem i can't solve right away if i can solve it at all. ><
i will just restart from crash step by step and see if i forgot something or whatever, again...

at first i put SetRotation in my code but i was surprised it needed quaternion so i just put SetDirection since it used Vector3 and i'm not familiar with quaternion yet but i will check those later. 
i also need to check the bones's rotation in each model since i set those the same way in blender  so for example the front exit bone and a the back exit bone of a model will have the same rotation instead of 0? and 180?.

-------------------------

noals | 2017-01-02 01:11:51 UTC | #40

i think i found out, i have this in the middle of my main, i guess i made a mistake while copy/pasting things.
[code]
class MyApp : public Application
{
public:
[/code]
not sure how it was able to compile.

-------------------------

Modanung | 2017-01-02 01:11:51 UTC | #41

[quote="noals"]yeah, it's very frustrating to me. that maybe do a month i'm stuck on this random loading and each time i code it differently to make it better, i encountered another problem i can't solve right away if i can solve it at all. ><
i will just restart from crash step by step and see if i forgot something or whatever, again...[/quote]
Welcome to the world of programming; it's all part of the process. :slight_smile:

[quote="noals"]at first i put SetRotation in my code but i was surprised it needed quaternion so i just put SetDirection since it used Vector3 and i'm not familiar with quaternion yet but i will check those later.[/quote]
You don't need to fully understand quaternions to use them. The most important things to know about them are:
- How to construct them; Quaternion(float angle, Vector3 axis) or Quaternion(float x, float y, float z) in most cases.
- They can be multiplied with a Vector3 to rotate that vector
- Quaternion::IDENTITY equals no rotation

SetDirection() is meant to be used with non-zero values and is like a simpler LookAt() function. Oh and you might like to know there's a Vector3::ZERO which is equal to Vector3(0.0f, 0.0f, 0.0f).

-------------------------

noals | 2017-01-02 01:11:51 UTC | #42

[quote="Modanung"]
Welcome to the world of programming; it's all part of the process. :slight_smile:
[/quote]
it's hell ! it still doesn't work after erasing the weird second "[b]class projet : public Application { public:[/b]".
with my class or just in the main, nothing shows up.
[code]

        MODULE_COUNT=0;
        room->loadRoom(MODULE_COUNT, my_scene, cache);  //abstract room
        MODULE_COUNT=1;

            
            r_node=my_scene->CreateChild("whatever");
            r_node->SetWorldPosition(Vector3::ZERO);  // ATTENTION i need SetPos func for my class
            //r_node->SetWorldDirection(room.rotation);  //   !!!
            AnimatedModel* r_Object=r_node->CreateComponent<AnimatedModel>();
            r_Object->SetModel(cache->GetResource<Model>("Models/rooms/room0.mdl"));
            r_Object->SetMaterial(cache->GetResource<Material>("Models/rooms/vert.xml"));

[/code]


[quote="Modanung"]
- How to construct them; Quaternion(float angle, Vector3 axis) or Quaternion(float x, float y, float z) in most cases.
- They can be multiplied with a Vector3 to rotate that vector
- Quaternion::IDENTITY equals no rotation

SetDirection() is meant to be used with non-zero values and is like a simpler LookAt() function. Oh and you might like to know there's a Vector3::ZERO which is equal to Vector3(0.0f, 0.0f, 0.0f).
[/quote]

thx, that's good to know.


anyway, i'm stuck.
it's frustrating because my next step is to stock bone's positions and i know how to do it already but it's kinda pointless if nothing show up on screen. ><
dunno, i will start from scratch again, testing and testing step by step again next time because i don't see the problem here, i start thinking the world of programming doesn't want me to continue lol.

-------------------------

noals | 2017-01-02 01:11:54 UTC | #43

the problem seems to be from  :
[code]AnimatedModel* r_Object=r_node->CreateComponent<AnimatedModel>();[/code]

i don't know why because i used it previously and i think it was working fine since i made a backup of the main.cpp at this time, but it doesn't seem to work anymore.
no problem with StaticModel but my model doesn't show up as a AnimatedModel and i need it to be an AnimatedModel because i will need bones informations while rendering.

any idea ? an include i forgot or something in Data or CoreData maybe ?


[code]
//engine
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/Graphics/Graphics.h>

#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Scene/SceneEvents.h>
#include <Urho3D/Graphics/Octree.h>
#include <Urho3D/Graphics/DebugRenderer.h>
#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/Viewport.h>
#include <Urho3D/Graphics/Renderer.h>

#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Graphics/StaticModel.h>
#include <Urho3D/Graphics/AnimatedModel.h>
#include <Urho3D/Graphics/Material.h>

#include <Urho3D/Graphics/Light.h>

#include <Urho3D/Core/CoreEvents.h>

//my class
#include "Modules.h"

using namespace Urho3D;

class projet : public Application
{

    URHO3D_OBJECT(projet, Application)

public:

////______________________
////    DEFINITION    


    SharedPtr<Scene> my_scene;

    //about camera
    SharedPtr<Node> camNode;

    //about modules
    SharedPtr<Node> roomNode;

    projet(Context* context) : Application(context)
    {
    }

    virtual void Setup()
    {
        engineParameters_["FullScreen"]=false;
        engineParameters_["WindowWidth"]=1280;
        engineParameters_["WindowHeight"]=720;
        engineParameters_["WindowResizable"]=true;
    }

    virtual void Start()
    {

        ResourceCache* cache=GetSubsystem<ResourceCache>();

        my_scene=new Scene(context_);
        my_scene->CreateComponent<Octree>();
        my_scene->CreateComponent<DebugRenderer>();

////___________________
////    MODULES    


        roomNode=my_scene->CreateChild("room0");
        roomNode->SetPosition(Vector3::ZERO);
        //StaticModel* roomObject=roomNode->CreateComponent<StaticModel>();
        AnimatedModel* roomObject=roomNode->CreateComponent<AnimatedModel>();
        roomObject->SetModel(cache->GetResource<Model>("Models/room0.mdl"));
        roomObject->SetMaterial(cache->GetResource<Material>("Materials/blank.xml"));


////_________________
////    LIGHT    





////__________________
////    CAMERA        


        camNode=my_scene->CreateChild("camNode");
        Camera* camObject=camNode->CreateComponent<Camera>();
        camObject->SetFarClip(2000);
	camNode->SetWorldPosition(Vector3(20,20,20));
	camNode->LookAt(Vector3::ZERO);

        //camera light
        {
            Light* light=camNode->CreateComponent<Light>();
            light->SetLightType(LIGHT_POINT);
            light->SetRange(25);
            light->SetBrightness(2.0);
            light->SetColor(Color(.8,1,.8,1.0));
        }

////__________________
////    RENDER    


        Renderer* renderer=GetSubsystem<Renderer>();
        SharedPtr<Viewport> viewport(new Viewport(context_,my_scene,camNode->GetComponent<Camera>()));
        renderer->SetViewport(0,viewport);


////__________________
////    EVENTS    


    //SubscribeToEvent(E_BEGINFRAME,URHO3D_HANDLER(projet,HandleBeginFrame));
    //SubscribeToEvent(E_KEYDOWN,URHO3D_HANDLER(projet,HandleKeyDown));
    //SubscribeToEvent(E_UIMOUSECLICK,URHO3D_HANDLER(projet,HandleControlClicked));
        SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(projet, HandleUpdate));
    //SubscribeToEvent(E_POSTUPDATE,URHO3D_HANDLER(projet,HandlePostUpdate));
    //SubscribeToEvent(E_RENDERUPDATE,URHO3D_HANDLER(projet,HandleRenderUpdate));
    //SubscribeToEvent(E_POSTRENDERUPDATE,URHO3D_HANDLER(projet,HandlePostRenderUpdate));
    //SubscribeToEvent(E_ENDFRAME,URHO3D_HANDLER(projet,HandleEndFrame));
        SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(projet, HandleKeyDown));
    }

    virtual void Stop()
    {
    }


////________


    void HandleUpdate(StringHash eventType,VariantMap& eventData)
    {
        float timeStep=eventData[Update::P_TIMESTEP].GetFloat();
	float MOVE_SPEED=50.0f;
        Input* input=GetSubsystem<Input>();

	if(input->GetQualifierDown(1))  // 1 is shift, 2 is ctrl, 4 is alt
            MOVE_SPEED*=4;

        if(input->GetKeyDown('D')) //rotate sens inverse horizontal
            camNode->Translate(Vector3(1,0, 0)*MOVE_SPEED*timeStep);
        if(input->GetKeyDown('Q')) //sens montre horizontal
            camNode->Translate(Vector3(-1,0,0)*MOVE_SPEED*timeStep);
        if(input->GetKeyDown('Z')) //zoom avant
            camNode->Translate(Vector3(0,0,1)*MOVE_SPEED*timeStep);
        if(input->GetKeyDown('S')) //zoom arriere
            camNode->Translate(Vector3(0,0,-1)*MOVE_SPEED*timeStep);
	if(input->GetKeyDown('E')) //rotate sens inverse vertical
            camNode->Translate(Vector3(0,1,0)*MOVE_SPEED*timeStep);
        if(input->GetKeyDown('A')) //sens montre vertical
            camNode->Translate(Vector3(0,-1,0)*MOVE_SPEED*timeStep);

	if(!GetSubsystem<Input>()->IsMouseGrabbed())
	{
	    IntVector2 mouseMove=input->GetMouseMove();
	    
	    if(mouseMove.x_>-2000000000&&mouseMove.y_>-2000000000)
            {
		camNode->LookAt(Vector3::ZERO); //look at 0,0,0
            }
	}

    }



////________


    void HandleKeyDown(StringHash eventType, VariantMap& eventData)
    {
        using namespace KeyDown;

        Graphics* graphics=GetSubsystem<Graphics>();
        int key = eventData[P_KEY].GetInt();

        if (key == KEY_ESC) //ESC to quit
        {
            engine_->Exit();
        }
        else if(key == KEY_TAB) //TAB to toggle mouse cursor
        {
            GetSubsystem<Input>()->SetMouseVisible(!GetSubsystem<Input>()->IsMouseVisible());
            GetSubsystem<Input>()->SetMouseGrabbed(!GetSubsystem<Input>()->IsMouseGrabbed()); 
        }
	else if(key == 'W') //W for fullscreen
	{
	    graphics->ToggleFullscreen();
	}
        else if(key == 'I')
        {
            //GetSubsystem<UI>()->menu->ShowPopup ();
        }
    }


////________


};
URHO3D_DEFINE_APPLICATION_MAIN(projet)

[/code]

-------------------------

noals | 2017-01-02 01:11:55 UTC | #44

i don't get it, its pissing me off.
last time i had this problem, it was because of the exporter in blender but it was solved by checking the "weight" box
[topic1960-10.html](http://discourse.urho3d.io/t/solved-how-do-i-get-a-bone-position/1873/1)
what the hell could it be this time ?

my cleaned project : [s000.tinyupload.com/index.php?fi ... 3697051604](http://s000.tinyupload.com/index.php?file_id=07546520393697051604)
the blend file : [s000.tinyupload.com/index.php?fi ... 6661436406](http://s000.tinyupload.com/index.php?file_id=95424891716661436406)

with static model : (but i can't get bone position)
[url=http://www.hostingpics.net/viewer.php?id=498534staticModelworks.png][img]http://img15.hostingpics.net/pics/498534staticModelworks.png[/img][/url]

with animated model : (i get the pos but it doesn't show up)
[url=http://www.hostingpics.net/viewer.php?id=657210animatedmodelnotwork.png][img]http://img15.hostingpics.net/pics/657210animatedmodelnotwork.png[/img][/url]

-------------------------

Dave82 | 2017-01-02 01:11:55 UTC | #45

That position doesn't seem correct.(it is extremely small 0.000000171143 , you can use 0.0) Is your model positioned at 0,0,0 ? And are your bones in in the viewport ? If not , it is possible that your Animated model's skeleton isn't updated at first frame so it's bounding box isn't updated as well and it is culled by the engine.

try 

[code]yourAnimatedModel->SetUpdateInvisible(true);[/code]

-------------------------

Modanung | 2017-01-02 01:11:55 UTC | #46

I see the room0 object in Blender doesn't have an armature modifier. This may be causing problems since the model is exported as having a skeleton.
Select room0 and then the armature, then hit Ctrl+P and select (Armature Deform) [b]With Automatic Weights[/b]. Then export and try again.

-------------------------

noals | 2017-01-02 01:11:55 UTC | #47

[quote="Modanung"]I see the room0 object in Blender doesn't have an armature modifier. This may be causing problems since the model is exported as having a skeleton.
Select room0 and then the armature, then hit Ctrl+P and select (Armature Deform) [b]With Automatic Weights[/b]. Then export and try again.[/quote]
yep, it works, thx a lot but that's weird since i didn't needed it in the other topic. anyway, at least i can continue.

[quote="Dave82"]That position doesn't seem correct.(it is extremely small 0.000000171143 , you can use 0.0) Is your model positioned at 0,0,0 ? And are your bones in in the viewport ? If not , it is possible that your Animated model's skeleton isn't updated at first frame so it's bounding box isn't updated as well and it is culled by the engine.

try 

[code]yourAnimatedModel->SetUpdateInvisible(true);[/code][/quote]
it isn't the pos of the model, it is the pos.x_ of a bone. it was just for testing. i was surprised at first by those numbers since i though the blender and urho3d scaling was kinda similar but i tested it before and the position is as expected if i load something else there.

thx anyway.

[url=http://www.hostingpics.net/viewer.php?id=581688workingbonepos.png][img]http://img15.hostingpics.net/pics/581688workingbonepos.png[/img][/url]

-------------------------

Modanung | 2017-01-02 01:11:55 UTC | #48

[quote="noals"]yep, it works, thx a lot but that's weird since i didn't needed it in the other topic. anyway, at least i can continue.[/quote]
Glad to hear that solved the problem. It seems like it wasn't the world of programming as such that was giving you a hard time. :wink: 
Maybe the [i]Force missing elements[/i] checkbox would have an effect in this case too. Could it have been checked in the other case?

-------------------------

noals | 2017-01-02 01:11:56 UTC | #49

[quote="Modanung"][quote="noals"]yep, it works, thx a lot but that's weird since i didn't needed it in the other topic. anyway, at least i can continue.[/quote]
Glad to hear that solved the problem. It seems like it wasn't the world of programming as such that was giving you a hard time. :wink: 
Maybe the [i]Force missing elements[/i] checkbox would have an effect in this case too. Could it have been checked in the other case?[/quote]
no, i don't recall having checked the [i]force missing elements[/i] ever to export and i only selected the model and the armature just to set the armature as parent since it was the only thing needed at this time.

-------------------------

