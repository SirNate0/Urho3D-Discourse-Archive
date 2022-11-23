noals | 2017-01-02 01:10:32 UTC | #1

hi,

i'm a beginner at programmation, i just try to organise my code for now with functions and classes before implementation, but i'm not sure the method i use with pugiXML is the right way to get what i want.
here is the XML part i wrote in my draft :

[code]
    //XML
    pugi::xml_document modulesList;
    pugi::xml_parse_result result = doc.load_file(XMLPath); //load XML
    if(!result)
    {
        ModulesNbr = modulesList.child("Infos")attribute("ModulesNbr").value(); //get module count
        moduleLine = chooseRandomLine(ModulesNbr, randomSeed)    //randomly select one
        
        
        for (moduleLine = modulesList.child("Module").attribute("Number").value()) //can it works ?
        {
            ModuleType = modulesList.child("Module").attribute("Type").value();  
       	  Exits = modulesList.child("Module").attribute("Exits").value();
    	     ModulePath = modulesList.child("Module").attribut("Path").value();
            ModuleTexturePath = modulesList.child("Module").attribut("TexturePath").value();
        }
    }
[/code]

basicaly, i want to load the xml file to get [u]the number of modules[/u] put in it  manually.
then i use a function to chose a number between 0 and the [u]number of modules[/u].

and then i want to get back all others values of the module N?[u]generated random value[/u] in the XML file.


would it work like that or should i use something else ?
what would be the best method ?

thx.

-------------------------

Enhex | 2017-01-02 01:10:32 UTC | #2

Try using xml_node::select_nodes() and xpath_node_set::size(). Haven't tried it myself.
Another way is to iterate over the siblings to get the their count.

For editing nodes look here: [pugixml.org/docs/manual.html#modify](http://pugixml.org/docs/manual.html#modify)

-------------------------

noals | 2017-01-02 01:10:33 UTC | #3

if for example, i have that in my xml.
[code]
<modules>
    <number = "1">
        <type = "corridor"></type>
        <exits = "2"></exits>
        <path = "model.mdl"></path>
        <texturepath = "texture.png"></texturepath>
    </number>
</modules>
[/code]

would it work with something like that ?

[code]
xml_node modules = doc.child("modules");
xml_node number = doc.child("number");     // ?

for( module.child_value("number") = 1)
{
    ModuleType = number.child_value("type")
    Exits = number.child_value("exits")
    ModulePath = number.child_value("path")
    ModuleTexturePath = number.child_value("texturepath")
}[/code]

i don't really understand how to use the functions you said.
[quote]xpath_node select_single_node(const char_t* query, xpath_variable_set* variables = 0) const;
xpath_node select_single_node(const xpath_query& query) const;
xpath_node_set select_nodes(const char_t* query, xpath_variable_set* variables = 0) const;
xpath_node_set select_nodes(const xpath_query& query) const;[/quote]
[quote]
xml_node child(const char_t* name) const;
xml_attribute attribute(const char_t* name) const;
xml_node next_sibling(const char_t* name) const;
xml_node previous_sibling(const char_t* name) const;
xml_node find_child_by_attribute(const char_t* name, const char_t* attr_name, const char_t* attr_value) const;
xml_node find_child_by_attribute(const char_t* attr_name, const char_t* attr_value) const;[/quote]

-------------------------

Enhex | 2017-01-02 01:10:33 UTC | #4

"number" is a child of "module", not the document's root node.

The XPath option seems too complicated, just count the nodes.

-------------------------

weitjong | 2017-01-02 01:10:33 UTC | #5

[quote="Enhex"]"number" is a child of "module", not the document's root node.

The XPath option seems too complicated, just count the nodes.[/quote]
I would agree with this statement if you do not know XPath before. It would be quicker I guess if you can achieve what you want to do using other ways. Convert the document into C++ data structure first and use the data structure as needed, for example. However, if you already know XPath then it is the most standard way to query an XML document, especially when the document itself is huge.

-------------------------

noals | 2017-01-02 01:10:33 UTC | #6

[quote]"number" is a child of "module", not the document's root node.[/quote]
how do i get the child of a child ?

[quote]just count the nodes.[/quote]
what do you mean ?

[quote]I would agree with this statement if you do not know XPath before. It would be quicker I guess if you can achieve what you want to do using other ways. Convert the document into C++ data structure first and use the data structure as needed, for example. However, if you already know XPath then it is the most standard way to query an XML document, especially when the document itself is huge.[/quote]
dunno, maybe i should write the xml file differently, i'm not really familiar with that either. something like that maybe :
[code]
<modules>
    <number = "1"> 1, 2, model.mdl, texture.png </number>
</modules>
[/code]
or i could maybe use a simple .txt file but i need to find some tutos about it as well anyway.
i just need to get few values from the chosen module in the external file, isn't there a simple method for that ?

i'm confused by all the type of stuff.

-------------------------

Enhex | 2017-01-02 01:10:34 UTC | #7

[quote]how do i get the child of a child ?[/quote]
You already posted code calling xml_node::child():
[code]xml_node modules = doc.child("modules");[/code]
modules is also a node, and you can call child() on it too.

[quote]what do you mean ?[/quote]
[en.wikipedia.org/wiki/Tree_(data_structure](https://en.wikipedia.org/wiki/Tree_(data_structure))
[w3schools.com/xml/xml_tree.asp](http://www.w3schools.com/xml/xml_tree.asp)

-------------------------

noals | 2017-01-02 01:10:34 UTC | #8

[quote]modules is also a node, and you can call child() on it too.[/quote]
so i can use that ?
[code]xml_node modules = doc.child("modules");
node_element number = modules.child("number");
int type = number.child_value("type");[/code]
what kind of node should i use for number ? is it the right one ? or maybe i could use a node from urdho3D ?

-------------------------

noals | 2017-01-02 01:10:37 UTC | #9

well, i tryed [url=http://urho3d.wikia.com/wiki/XML]the wiki example[/url] but it don't compile.

i made my xml like that :
[code]<xml>
<infos count="2"/>
<modules nbr="1" type="1" exits="2" path="Models/cor5x20x1/cor5x20x1.mdl" texturepath="Models/cor5x20x1/cor5x20x1.xml"/>
<modules nbr="2" type="2" exits="4" path="Models/room20x20x1/room20x20x1.mdl" texturepath="Models/room20x20x1/room20x20x1.xml"/>
</xml>[/code]

and tryed that :
[code]
        //XML
        pugi::xml_document modulesList;
        pugi::xml_parse_result result = modulesList.load_file("Scripts/modules.xml"); //load XML

        for(auto& c:modulesList.children())
        {
            for(pugi::xml_node& child:c.children())
            {
                std::string name(child.name());
                if(name=="infos")
                {
                    for(pugi::xml_attribute& attr:child.attributes())
                    {
                        if(std::string(attr.name()=="count"))
                        modulesCount = std::stoi(std::string(attr.value())); //get modules count
                    }
                }
            }
        }[/code]


[quote]/home/noname/Bureau/projet/main.cpp: In member function ?virtual void projet::Start()?:
/home/noname/Bureau/projet/main.cpp:109:19: error: ISO C++ forbids declaration of ?c? with no type [-fpermissive]
         for(auto& c:modulesList.children())
                   ^
/home/noname/Bureau/projet/main.cpp:109:21: error: range-based ?for? loops are not allowed in C++98 mode
         for(auto& c:modulesList.children())
                     ^
/home/noname/Bureau/projet/main.cpp:111:39: error: range-based ?for? loops are not allowed in C++98 mode
             for(pugi::xml_node& child:c.children())
                                       ^
/home/noname/Bureau/projet/main.cpp:111:41: error: request for member ?children? in ?c?, which is of non-class type ?int?
             for(pugi::xml_node& child:c.children())
                                         ^
/home/noname/Bureau/projet/main.cpp:116:51: error: range-based ?for? loops are not allowed in C++98 mode
                     for(pugi::xml_attribute& attr:child.attributes())
                                                   ^
/home/noname/Bureau/projet/main.cpp:118:60: error: no matching function for call to ?std::basic_string<char>::basic_string(bool)?
                         if(std::string(attr.name()=="count"))
                                                            ^
/home/noname/Bureau/projet/main.cpp:118:60: note: candidates are:
In file included from /usr/include/c++/4.8/string:52:0,
                 from /home/noname/Bureau/projet/main.cpp:32:
/usr/include/c++/4.8/bits/basic_string.h:532:9: note: template<class _InputIterator> std::basic_string<_CharT, _Traits, _Alloc>::basic_string(_InputIterator, _InputIterator, const _Alloc&)
         basic_string(_InputIterator __beg, _InputIterator __end,
         ^
/usr/include/c++/4.8/bits/basic_string.h:532:9: note:   template argument deduction/substitution failed:
/home/noname/Bureau/projet/main.cpp:118:60: note:   candidate expects 3 arguments, 1 provided
                         if(std::string(attr.name()=="count"))
                                                            ^
In file included from /usr/include/c++/4.8/string:53:0,
                 from /home/noname/Bureau/projet/main.cpp:32:
/usr/include/c++/4.8/bits/basic_string.tcc:219:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(std::basic_string<_CharT, _Traits, _Alloc>::size_type, _CharT, const _Alloc&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::basic_string<_CharT, _Traits, _Alloc>::size_type = long unsigned int]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:219:5: note:   candidate expects 3 arguments, 1 provided
/usr/include/c++/4.8/bits/basic_string.tcc:212:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const _CharT*, const _Alloc&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:212:5: note:   no known conversion for argument 1 from ?bool? to ?const char*?
/usr/include/c++/4.8/bits/basic_string.tcc:205:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const _CharT*, std::basic_string<_CharT, _Traits, _Alloc>::size_type, const _Alloc&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::basic_string<_CharT, _Traits, _Alloc>::size_type = long unsigned int]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:205:5: note:   candidate expects 3 arguments, 1 provided
/usr/include/c++/4.8/bits/basic_string.tcc:193:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const std::basic_string<_CharT, _Traits, _Alloc>&, std::basic_string<_CharT, _Traits, _Alloc>::size_type, std::basic_string<_CharT, _Traits, _Alloc>::size_type, const _Alloc&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::basic_string<_CharT, _Traits, _Alloc>::size_type = long unsigned int]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:193:5: note:   candidate expects 4 arguments, 1 provided
/usr/include/c++/4.8/bits/basic_string.tcc:183:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const std::basic_string<_CharT, _Traits, _Alloc>&, std::basic_string<_CharT, _Traits, _Alloc>::size_type, std::basic_string<_CharT, _Traits, _Alloc>::size_type) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::basic_string<_CharT, _Traits, _Alloc>::size_type = long unsigned int]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:183:5: note:   candidate expects 3 arguments, 1 provided
/usr/include/c++/4.8/bits/basic_string.tcc:169:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const std::basic_string<_CharT, _Traits, _Alloc>&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:169:5: note:   no known conversion for argument 1 from ?bool? to ?const std::basic_string<char>&?
/usr/include/c++/4.8/bits/basic_string.tcc:177:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const _Alloc&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:177:5: note:   no known conversion for argument 1 from ?bool? to ?const std::allocator<char>&?
In file included from /usr/include/c++/4.8/string:52:0,
                 from /home/noname/Bureau/projet/main.cpp:32:
/usr/include/c++/4.8/bits/basic_string.h:437:7: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string() [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>]
       basic_string()
       ^
/usr/include/c++/4.8/bits/basic_string.h:437:7: note:   candidate expects 0 arguments, 1 provided
/home/noname/Bureau/projet/main.cpp:119:40: error: ?stoi? is not a member of ?std?
                         modulesCount = std::stoi(std::string(attr.value())); //get modules count
                                        ^
make[2]: *** [CMakeFiles/projet.dir/main.cpp.o] Erreur 1
make[1]: *** [CMakeFiles/projet.dir/all] Erreur 2
make: *** [all] Erreur 2
[/quote]

-------------------------

noals | 2017-01-02 01:10:38 UTC | #10

ok, i think i figured out something checking the pugixml doc.

the xml file :
[code]
<xml>
<infos count="2"/>
<modules nbr="1" type="1" exits="2" path="Models/cor5x20x1/cor5x20x1.mdl" texturepath="Models/cor5x20x1/cor5x20x1.xml"/>
<modules nbr="2" type="2" exits="4" path="Models/room20x20x1/room20x20x1.mdl" texturepath="Models/room20x20x1/room20x20x1.xml"/>
</xml>[/code]

and this actually compile :
[code]
        pugi::xml_node infos = modulesList.child("infos");
	     pugi::xml_attribute count;
        count = infos.child_value("count");
[/code]
but since i wasn't able to render some text yet with urho3D, i can't verify if "count" really return the value i want.
i will try again to render some text and go back to xml after that.

-------------------------

gawag | 2017-01-02 01:10:38 UTC | #11

Oh! Whoopsie!

I just saw this thread and was going to post my wiki link but it was already found.
The reason it doesn't compile is due to the auto feature of C++11 being used. And possible also the new range based for loops. You seem to not have C++11 enabled or available.
Ha it even says "error: range-based ?for? loops are not allowed in C++98 mode".

I just edited the page and replaced the C++11 stuff with C++98 style code: [urho3d.wikia.com/wiki/XML](http://urho3d.wikia.com/wiki/XML)
(haven't tested that exact code but the loops itself work here. Write if there's an error, may have made typos.)

Also you seem to not have string included as the compiler complains about not finding std::stoi and it seems to be in string: [en.cppreference.com/w/cpp/string ... tring/stol](http://en.cppreference.com/w/cpp/string/basic_string/stol)
[code]#include <string>[/code]

Hope that helps.

Oh and about text output: Just use std::cout (or printf) to print to the console. If on windows you may need to set URHO3D_WIN32_CONSOLE in CMake when generating your project to get a console with output when starting your program.
You can also use the Urho logging feature via URHO3D_LOGDEBUG(text) which will print into the Urho log and onto the console.

-------------------------

noals | 2017-01-02 01:10:38 UTC | #12

it still don't compile and string was actually included the first time but wasn't recognized for some magical reasons.
i use ubuntu, i installed it just for programming so when you tell me about c++11, i guess i just installed an old packet; i just put "sudo apt-get install build-essential" following some tuto instruction.

here is my full main.cpp with the last try following your edited tuto :
you can scroll down to some //////////////////// to easely find the xml part.

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
#include <Urho3D/Graphics/Material.h>
#include <Urho3D/Graphics/Skybox.h>


#include <Urho3D/ThirdParty/PugiXml/pugixml.hpp>
#include <string>
#include <iostream>  //


using namespace Urho3D;
//using namespace std;

class projet : public Application
{

public:

    //DEFINITION
    SharedPtr<Scene> my_scene;
    SharedPtr<Node> corNode;
    SharedPtr<Node> roomNode;

    Node* camNode;

    int randomSeed;
    
    int modulesCount;
    int moduleNbr;

    //int moduleType;
    //int exits;
    //string modulePath;
    //string moduleTexturePath;

    projet(Context* context) : Application(context)
    {

    }

    virtual void Setup()
    {
	// See http://urho3d.github.io/documentation/1.32/_main_loop.html
	engineParameters_["FullScreen"]=false;
        engineParameters_["WindowWidth"]=1280;
        engineParameters_["WindowHeight"]=720;
        engineParameters_["WindowResizable"]=true;
    }

    virtual void Start()
    {

	//DEFINITION
	randomSeed = 35;


	// We will be needing to load resources.
        // All the resources used in this example comes with Urho3D.
        // If the engine can't find them, check the ResourcePrefixPath. <-- where ?
        ResourceCache* cache=GetSubsystem<ResourceCache>();

	// Let's setup a scene to render.
        my_scene=new Scene(context_);
        // Let the scene have an Octree component!
        my_scene->CreateComponent<Octree>();
        // Let's add an additional scene component for fun.
        my_scene->CreateComponent<DebugRenderer>();
	// what the hell ?!

	//menu=new Menu(context_);
	//GetSubsystem<Menu>()->GetRoot()->AddChild(menu);

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//XML
        pugi::xml_document modulesList;
        pugi::xml_parse_result result = modulesList.load_file("Scripts/modules.xml"); //load XML
        //if(!result)
        //{
	//std::cout<<"XML parsed with errors, attr value: ["<<modulesList.child("node").attribute("attr").value()<<"]\n";
        //std::cout<<"Error description: "<<result.description()<<"\n";
        //std::cout<<"Error offset: "<<result.offset<<" (error at [..."<<(result.offset)<<"]\n\n";
            //pugi::xml_node modules = modulesList.child("modules");  //don't compile
	//}
        
        for(pugi::xml_node_iterator it=modulesList.children().begin();
           it!=modulesList.children().end();it++)
        {
            pugi::xml_node& child=*it;

            std::string name(child.name());
            if(name=="infos")
            {
                for(pugi::xml_attribute_iterator it=child.attributes().begin();
                   it!=child.attributes().end();it++)
                {
                    pugi::xml_attribute& attr=*it;

                    if(std::string(attr.name()=="count"))
                    modulesCount = std::stoi(std::string(attr.value())); //get modules count
                }
            }
        }
        

        //pugi::xml_node infos = modulesList.child("infos");
	//pugi::xml_attribute count;
        //count = infos.child_value("count");

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/*
	text = new Text(context_);
	GetSubsystem<UI>()->GetRoot()->AddChild(text);
	text->SetText("This is a test.");
	text->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"),30);
	text->SetColor(Color(1.0f, 1.0f, 0.0f));
	text->SetHorizontalAlignment(HA_CENTER);
        text->SetVerticalAlignment(VA_CENTER);       

	Button* button = new Button(context_);
	// Note, must be part of the UI system before SetSize calls!
        GetSubsystem<UI>()->GetRoot()->AddChild(button);
        button->SetName("Button");
        button->SetStyle("Button");
        button->SetSize(32, 32);
        button->SetPosition(16, 16);

	// buttons don't have a text by itself, a text needs to be added as a child
	Text* t=new Text(context_);
	// setting a font is required
	t->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"),20);
	t->SetColor(Color(1.0f, 1.0f, 0.0f));
	t->SetHorizontalAlignment(HA_CENTER);
	t->SetVerticalAlignment(VA_CENTER);
	t->SetName("Text");
	t->SetText("Play");
	t->SetStyle("Text");
	button->AddChild(t);
*/


	// Let's put a room in there.
        roomNode=my_scene->CreateChild("room20x20x1");  //can i change it ?
        roomNode->SetPosition(Vector3(0,0,0));
        StaticModel* roomObject=roomNode->CreateComponent<StaticModel>();
        roomObject->SetModel(cache->GetResource<Model>("Models/room20x20x1/room20x20x1.mdl"));
        roomObject->SetMaterial(cache->GetResource<Material>("Models/room20x20x1/room20x20x1.xml"));
	//skeletonNode=roomObject->GetBone("exit1");
	//exitNode=my_scene->GetChild("exit1");
	

	//exitNode=roomNode->GetChild(0);

	/*
	// Let's put a corridor in there.
        corNode=my_scene->CreateChild("cor5x20x1");  //can i change it ?
        corNode->SetPosition(Vector3(0,5,0));
        StaticModel* corObject=corNode->CreateComponent<StaticModel>();
        corObject->SetModel(cache->GetResource<Model>("Models/cor5x20x1/cor5x20x1.mdl"));
        corObject->SetMaterial(cache->GetResource<Material>("Models/cor5x20x1/cor5x20x1.xml"));
	*/
	


	 // We need a camera from which the viewport can render.
        camNode=my_scene->CreateChild("camNode");
        Camera* camObject=camNode->CreateComponent<Camera>();
        camObject->SetFarClip(2000);
	camNode->SetWorldPosition(Vector3(20,20,20));
	camNode->LookAt(roomNode->GetWorldPosition());  //target cor to begin with
	
	//targetNode=my_scene->CreateChild("targetNode");
	//targetNode->SetWorldPosition(Vector3(0,0,0));

	// Create 6 lights
	{
            Node* lightNode=my_scene->CreateChild("Light1");  //  "their y is vertical"
            lightNode->SetPosition(Vector3(0,0,100));
            Light* lightObject=lightNode->CreateComponent<Light>();
            lightObject->SetLightType(LIGHT_POINT);
            lightObject->SetRange(200);
            lightObject->SetBrightness(2); //1.2
            lightObject->SetColor(Color(1,0.5,0.5,1));
            lightObject->SetCastShadows(true);
        }
        {
            Node* lightNode=my_scene->CreateChild("Light2"); 
            lightNode->SetPosition(Vector3(0,0,-100));
            Light* lightObject=lightNode->CreateComponent<Light>();
            lightObject->SetLightType(LIGHT_POINT);
            lightObject->SetRange(200);
            lightObject->SetBrightness(2);
            lightObject->SetColor(Color(1,0.5,0.5,1));
            lightObject->SetCastShadows(true);
        }
	{
            Node* lightNode=my_scene->CreateChild("Light3"); 
            lightNode->SetPosition(Vector3(100,0,0));
            Light* lightObject=lightNode->CreateComponent<Light>();
            lightObject->SetLightType(LIGHT_POINT);
            lightObject->SetRange(200);
            lightObject->SetBrightness(2); //1.2
            lightObject->SetColor(Color(0.5,0.5,1,1));
            lightObject->SetCastShadows(true);
        }
        {
            Node* lightNode=my_scene->CreateChild("Light4"); 
            lightNode->SetPosition(Vector3(-100,0,0));
            Light* lightObject=lightNode->CreateComponent<Light>();
            lightObject->SetLightType(LIGHT_POINT);
            lightObject->SetRange(200);
            lightObject->SetBrightness(2);
            lightObject->SetColor(Color(0.5,0.5,1,1));
            lightObject->SetCastShadows(true);
        }
	{
            Node* lightNode=my_scene->CreateChild("Light5"); 
            lightNode->SetPosition(Vector3(0,100,0));
            Light* lightObject=lightNode->CreateComponent<Light>();
            lightObject->SetLightType(LIGHT_POINT);
            lightObject->SetRange(200);
            lightObject->SetBrightness(2); //1.2
	    lightObject->SetColor(Color(0.5,1,0.5,1));
            lightObject->SetCastShadows(true);
        }
        {
            Node* lightNode=my_scene->CreateChild("Light6"); 
            lightNode->SetPosition(Vector3(0,-100,0));
            Light* lightObject=lightNode->CreateComponent<Light>();
            lightObject->SetLightType(LIGHT_POINT);
            lightObject->SetRange(200);
            lightObject->SetBrightness(2);
            lightObject->SetColor(Color(0.5,1,0.5,1));
            lightObject->SetCastShadows(true);
        } 



// Now we setup the viewport. Ofcourse, you can have more than one!
        Renderer* renderer=GetSubsystem<Renderer>();
        SharedPtr<Viewport> viewport(new Viewport(context_,my_scene,camNode->GetComponent<Camera>()));
        renderer->SetViewport(0,viewport);

// events
//SubscribeToEvent(E_BEGINFRAME,URHO3D_HANDLER(MyApp,HandleBeginFrame));
//SubscribeToEvent(E_KEYDOWN,URHO3D_HANDLER(MyApp,HandleKeyDown));
//SubscribeToEvent(E_UIMOUSECLICK,URHO3D_HANDLER(MyApp,HandleControlClicked));
	SubscribeToEvent(E_UPDATE,URHO3D_HANDLER(projet, HandleUpdate));
//SubscribeToEvent(E_POSTUPDATE,URHO3D_HANDLER(MyApp,HandlePostUpdate));
//SubscribeToEvent(E_RENDERUPDATE,URHO3D_HANDLER(MyApp,HandleRenderUpdate));
//SubscribeToEvent(E_POSTRENDERUPDATE,URHO3D_HANDLER(MyApp,HandlePostRenderUpdate));
//SubscribeToEvent(E_ENDFRAME,URHO3D_HANDLER(MyApp,HandleEndFrame));

        SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(projet, HandleKeyDown));

    }
    virtual void Stop()
    {

    }
	
//void HandleBeginFrame

    void HandleKeyDown(StringHash eventType, VariantMap& eventData)
    {

	Graphics* graphics=GetSubsystem<Graphics>();
        using namespace KeyDown;

        int key = eventData[P_KEY].GetInt();
        if (key == KEY_ESC)
            engine_->Exit();
        else if(key == KEY_TAB)
        {
            GetSubsystem<Input>()->SetMouseVisible(!GetSubsystem<Input>()->IsMouseVisible());
            GetSubsystem<Input>()->SetMouseGrabbed(!GetSubsystem<Input>()->IsMouseGrabbed());
	    //GetSubsystem<UI>()->menu->ShowPopup ();
        }
	else if(key == 'P')
	{
	    graphics->ToggleFullscreen();
	}
    }

//void HandleControlClicked(StringHash eventType, VariantMap& eventData)

    void HandleUpdate(StringHash eventType,VariantMap& eventData)
    {
	float timeStep=eventData[Update::P_TIMESTEP].GetFloat();

        //const float MOUSE_SENSITIVITY=0.1f;
	float MOVE_SPEED=50.0f;

        Input* input=GetSubsystem<Input>();

	if(input->GetQualifierDown(1))  // 1 is shift, 2 is ctrl, 4 is alt
            MOVE_SPEED*=10;
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
	//if(input->GetKeyDown('R')) //x
        //    targetNode->Translate(Vector3(1,0,0)*MOVE_SPEED*timeStep);

	if(!GetSubsystem<Input>()->IsMouseGrabbed())
	{
	    IntVector2 mouseMove=input->GetMouseMove();
	    
	    if(mouseMove.x_>-2000000000&&mouseMove.y_>-2000000000)
            {
		
		//camNode->LookAt(targetNode->GetWorldPosition());
                
		//targetPosX = targetNode->GetPosition().X;
		//targetPosY = targetNode->GetPosition().Y;
		//targetPosZ = targetNode->GetPosition().Z;

		//static float mousePosX = 40;
	        //static float mousePosY = 40;

                //mousePosX+=MOUSE_SENSITIVITY*mouseMove.x_;
                //mousePosY+=MOUSE_SENSITIVITY*mouseMove.y_;
                //mousePosY=Clamp(mousePosY,-90.0f,90.0f);
		camNode->LookAt(roomNode->GetWorldPosition()); //look at room
		// Reset rotation and set yaw and pitch again
		//camNode->Translate(Vector3(mouseMove.x_,0,0));
		//camNode->Translate(Vector3(-mouseMove.x_,0,0));
		//camNode->Translate(Vector3(0,0,mousePosY));
		//camNode->Translate(Vector3(0,0,-mousePosX));
		//camNode->Translate(Vector3(0,0,mousePosY));
                //camNode->Yaw(mousePosX);
                //camNode->Pitch(mousePosY);
		
		
            }
	}
	


    }


//void HandlePostUpdate
//void HandleRenderUpdate
//void HandlePostRenderUpdate
//void HandleEndFrame

};
URHO3D_DEFINE_APPLICATION_MAIN(projet)
[/code]

and the errors from the compiler
[quote]
/home/noname/Bureau/projet/main.cpp: In member function ?virtual void projet::Start()?:
/home/noname/Bureau/projet/main.cpp:123:56: error: no matching function for call to ?std::basic_string<char>::basic_string(bool)?
                     if(std::string(attr.name()=="count"))
                                                        ^
/home/noname/Bureau/projet/main.cpp:123:56: note: candidates are:
In file included from /usr/include/c++/4.8/string:52:0,
                 from /home/noname/Bureau/projet/main.cpp:32:
/usr/include/c++/4.8/bits/basic_string.h:532:9: note: template<class _InputIterator> std::basic_string<_CharT, _Traits, _Alloc>::basic_string(_InputIterator, _InputIterator, const _Alloc&)
         basic_string(_InputIterator __beg, _InputIterator __end,
         ^
/usr/include/c++/4.8/bits/basic_string.h:532:9: note:   template argument deduction/substitution failed:
/home/noname/Bureau/projet/main.cpp:123:56: note:   candidate expects 3 arguments, 1 provided
                     if(std::string(attr.name()=="count"))
                                                        ^
In file included from /usr/include/c++/4.8/string:53:0,
                 from /home/noname/Bureau/projet/main.cpp:32:
/usr/include/c++/4.8/bits/basic_string.tcc:219:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(std::basic_string<_CharT, _Traits, _Alloc>::size_type, _CharT, const _Alloc&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::basic_string<_CharT, _Traits, _Alloc>::size_type = long unsigned int]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:219:5: note:   candidate expects 3 arguments, 1 provided
/usr/include/c++/4.8/bits/basic_string.tcc:212:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const _CharT*, const _Alloc&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:212:5: note:   no known conversion for argument 1 from ?bool? to ?const char*?
/usr/include/c++/4.8/bits/basic_string.tcc:205:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const _CharT*, std::basic_string<_CharT, _Traits, _Alloc>::size_type, const _Alloc&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::basic_string<_CharT, _Traits, _Alloc>::size_type = long unsigned int]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:205:5: note:   candidate expects 3 arguments, 1 provided
/usr/include/c++/4.8/bits/basic_string.tcc:193:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const std::basic_string<_CharT, _Traits, _Alloc>&, std::basic_string<_CharT, _Traits, _Alloc>::size_type, std::basic_string<_CharT, _Traits, _Alloc>::size_type, const _Alloc&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::basic_string<_CharT, _Traits, _Alloc>::size_type = long unsigned int]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:193:5: note:   candidate expects 4 arguments, 1 provided
/usr/include/c++/4.8/bits/basic_string.tcc:183:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const std::basic_string<_CharT, _Traits, _Alloc>&, std::basic_string<_CharT, _Traits, _Alloc>::size_type, std::basic_string<_CharT, _Traits, _Alloc>::size_type) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::basic_string<_CharT, _Traits, _Alloc>::size_type = long unsigned int]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:183:5: note:   candidate expects 3 arguments, 1 provided
/usr/include/c++/4.8/bits/basic_string.tcc:169:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const std::basic_string<_CharT, _Traits, _Alloc>&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:169:5: note:   no known conversion for argument 1 from ?bool? to ?const std::basic_string<char>&?
/usr/include/c++/4.8/bits/basic_string.tcc:177:5: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string(const _Alloc&) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>]
     basic_string<_CharT, _Traits, _Alloc>::
     ^
/usr/include/c++/4.8/bits/basic_string.tcc:177:5: note:   no known conversion for argument 1 from ?bool? to ?const std::allocator<char>&?
In file included from /usr/include/c++/4.8/string:52:0,
                 from /home/noname/Bureau/projet/main.cpp:32:
/usr/include/c++/4.8/bits/basic_string.h:437:7: note: std::basic_string<_CharT, _Traits, _Alloc>::basic_string() [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>]
       basic_string()
       ^
/usr/include/c++/4.8/bits/basic_string.h:437:7: note:   candidate expects 0 arguments, 1 provided
/home/noname/Bureau/projet/main.cpp:124:36: error: ?stoi? is not a member of ?std?
                     modulesCount = std::stoi(std::string(attr.value())); //get modules count
                                    ^
make[2]: *** [CMakeFiles/projet.dir/main.cpp.o] Erreur 1
make[1]: *** [CMakeFiles/projet.dir/all] Erreur 2
make: *** [all] Erreur 2

[/quote]

i don't get it.

and wouldn't it work with this method ? 
[code]
pugi::xml_node infos = modulesList.child("infos");
pugi::xml_attribute count;
count = infos.child_value("count");
[/code]


i really need to get the text working in my program and i tryed at some point the URHO3D_LOGDEBUG(text) thing but had no result.
you can see my last text test in the code commented out (edit: through i guess i deleted the update part at some point), i tryed few tutos or examples but the result was the same, the only thing i got working was a kind of button through it was just a white square showing up on screen.

thx.


edit2: i edited a little mistake but the result is kinda the same.

-------------------------

gawag | 2017-01-02 01:10:39 UTC | #13

You can't just take a random part of the code and expect it to work  :slight_smile: 
Fixed your code with explanations:
[code]
        pugi::xml_document modulesList;
        pugi::xml_parse_result result = modulesList.load_file("Scripts/modules.xml"); //load XML
        //if(!result)
        //{
        //std::cout<<"XML parsed with errors, attr value: ["<<modulesList.child("node").attribute("attr").value()<<"]\n";
        //std::cout<<"Error description: "<<result.description()<<"\n";
        //std::cout<<"Error offset: "<<result.offset<<" (error at [..."<<(result.offset)<<"]\n\n";
        //pugi::xml_node modules = modulesList.child("modules");  //don't compile
        //}
       
        // here you had code to iterate over the childs of a XML node "c" which was not defined
        //for(pugi::xml_node_iterator it=modulesList.children().begin();
        //   it!=c.children().end();it++)
        // this code iterates over all topmost elements of the XML document, which you name "modulesList" and I in my example "doc"
        for(pugi::xml_node_iterator it=modulesList.children().begin();
            it!=modulesList.children().end();it++)
        {
            pugi::xml_node& child=*it;

            std::string name(child.name());
            if(name=="infos")
            {
                for(pugi::xml_attribute_iterator it=child.attributes().begin();
                   it!=child.attributes().end();it++)
                {
                    pugi::xml_attribute& attr=*it;

                    if(std::string(attr.name()=="count"))
                    modulesCount = std::stoi(std::string(attr.value())); //get modules count
                }
            }
        }
       
[/code]
Also the program may not find "Scripts/modules.xml", I guess it's "Data/Scripts/modules.xml" or something seen from the program executionable file (.exe on windows). The example code uses pugiXML directly without the Urho ressource system which looks in the Urho data paths. (Urho has an XML wrapper which probably uses the paths and may be better but I haven't used that yet)

Just added more comments to the example code to clarify stuff: [urho3d.wikia.com/wiki/XML](http://urho3d.wikia.com/wiki/XML)

[quote]
and wouldn't it work with this method ?

[code]
    pugi::xml_node infos = modulesList.child("infos");
    pugi::xml_attribute count;
    count = infos.child_value("count");
[/code]
[/quote]
That should work as well yes (after correctly loading the document). (At least it looks correct after their manual [pugixml.org/docs/manual.html](http://pugixml.org/docs/manual.html))
I had lists which I needed to iterate over, therefore the loops in my example.

[quote]
i really need to get the text working in my program and i tryed at some point the URHO3D_LOGDEBUG(text) thing but had no result.
[/quote]
Hm I just tested it and URHO3D_LOGDEBUG did really not print anything. I guess there are certain levels of how much output is actually printed and LOGDEBUG was too low. LOGINFO actually worked in my test:
[code]
URHO3D_LOGINFO("asdf urho log test text");
[/code]
The Urho3d.log looks like:
[code]
...
[Mon Mar 07 18:44:42 2016] INFO: Initialized renderer
[Mon Mar 07 18:44:42 2016] INFO: Set audio mode 44100 Hz stereo interpolated
[Mon Mar 07 18:44:42 2016] INFO: Initialized engine
[Mon Mar 07 18:44:42 2016] INFO: asdf urho log test text
[/code]

The Urho GUI is a bit tricky. That's one of the reasons I'm currently writing my own GUI system.
I had once the problem of not having set a font and then Urho did not display any text. Have you correctly set a font and style? (I'm not even sure if I'm doing that correctly)
[code]
    Text* t=new Text(context);
    t->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"),20);
    t->SetText("hello, world");
    t->SetStyle("Text");
[/code]

-------------------------

noals | 2017-01-02 01:10:40 UTC | #14

[quote="gawag"]You can't just take a random part of the code and expect it to work  :slight_smile: 
Fixed your code with explanations: [/quote]
you wrote the same thing as the code in my previous post so the result is the same through i tryed with a different path for the xml as you suggested.
and i don't understand why i have string error, i will ask another forum about it.
believing the compiler i could say it seem the data put don't fit the string template, it need a conversion or something but i guess it work for you so why wouldn't it work for me ?
or you use windows and the method doesn't work with GCC ? weird.

for the text, it compile fine but  it's not working either.
i even tryed different position for the "GetSubsystem<UI>()->GetRoot()->AddChild(text); " because in some tuto, they said it was revelant. (not sure it was about the text through)
[quote]
SharedPtr<Text> text;

text = new Text(context_);
text->SetText("This is a test.");
text->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"),30);
text->SetColor(Color(1.0f, 1.0f, 0.0f));
text->SetHorizontalAlignment(HA_CENTER);
text->SetVerticalAlignment(VA_TOP);
GetSubsystem<UI>()->GetRoot()->AddChild(text); 

[/quote]

sigh, it's annoying.
i started with irrlicht few years ago if you know it, things actually works fine with irrlicht but it lack good physics and others stuff so i was happy to find urho3D but it seem some things depend on luck with urho3D... i don't get it  and with all the sample examples wrote with some kind of framework around it, just the helloWorld is a pain already.


my environement variable are set like that :
[code]
export URHO3D_REPOSITORY=/home/noname/Documents/urho3D_1.5
export URHO3D_HOME=/home/noname/Documents/urho3D_build
[/code]
how do i set the URHO3D_PREFIX_PATH or change the engine parameter "ResourcePrefixPath" in the Setup method ? that's what is suggested in a wiki tuto and the only solution i can think of to maybe fix the text problem at least...

-------------------------

gawag | 2017-01-02 01:10:40 UTC | #15

[quote="noals"][quote="gawag"]You can't just take a random part of the code and expect it to work  :slight_smile: 
Fixed your code with explanations: [/quote]
you wrote the same thing as the code in my previous post so the result is the same through i tryed with a different path for the xml as you suggested.
and i don't understand why i have string error, i will ask another forum about it.
believing the compiler i could say it seem the data put don't fit the string template, it need a conversion or something but i guess it work for you so why wouldn't it work for me ?
or you use windows and the method doesn't work with GCC ? weird.[/quote]
You had an error because your "c" was not defined. You had copied an inner for loop out of an outer loop that defined that "c". So I tried fixed that by changing your code.

Oh I forgot about the string error, uhm. I'm on windows with GCC (MinGW).

That's an odd error. 
xml_attribute.name() and xml_attribute.value() should have the type "const char_t*" (after [pugixml.googlecode.com/svn-histo ... ibute.html](http://pugixml.googlecode.com/svn-history/r492/trunk/docs/html/classpugi_1_1xml__attribute.html)) but the compiler talks about a bool...
Try a "std::string((const char*)attr.name())". That explicit casting should work.

[quote="noals"]
for the text, it compile fine but  it's not working either.
i even tryed different position for the "GetSubsystem<UI>()->GetRoot()->AddChild(text); " because in some tuto, they said it was revelant. (not sure it was about the text through)
[/quote]

Hm, try this relative simple GUI code:
[code]
//In the class definition:
SharedPtr<Urho3D::Window> window;
Urho3D::Text* window_text;

// when creating the scene:
window=new Window(context_);
GetSubsystem<UI>()->GetRoot()->AddChild(window);
window->SetStyle("Window");
window->SetSize(600,70);
window->SetColor(Color(.0,.15,.3,.5));
window->SetAlignment(HA_LEFT,VA_TOP);

window_text=new Text(context_);
window_text->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"),14);
window_text->SetColor(Color(.8,.85,.9));
window_text->SetAlignment(HA_LEFT,VA_TOP);
window_text->SetText("Hello Urho!");
window->AddChild(window_text);
[/code]
This creates this window in the top left with a text: [i.imgur.com/R26Rdyn.jpg](http://i.imgur.com/R26Rdyn.jpg)
I'm using that normally to display various informations: [i.imgur.com/sPpJud5.jpg](http://i.imgur.com/sPpJud5.jpg)

[quote="noals"]
sigh, it's annoying.
i started with irrlicht few years ago if you know it, things actually works fine with irrlicht but it lack good physics and others stuff so i was happy to find urho3D but it seem some things depend on luck with urho3D... i don't get it  and with all the sample examples wrote with some kind of framework around it, just the helloWorld is a pain already.
[/quote]
That's why I started writing about it to explain stuff. Some things are really unintuitive and could be way better.
There are currently two possible bad and outdated first project examples that use a more minimalistic approach as the samples shipped with Urho:
[github.com/damu/UrhoSampleProject](https://github.com/damu/UrhoSampleProject)
[urho3d.wikia.com/wiki/First_Project](http://urho3d.wikia.com/wiki/First_Project)
I'm currently testing the UrhoSampleProject on my GitHub and after that the First Project code on the page. I guess I'll do a new First Project Article soon: [github.com/urho3d/Urho3D/wiki/First-Project](https://github.com/urho3d/Urho3D/wiki/First-Project) (currently empty)
Maybe even an article series like "Chapter 2: Adding simple Physics" "Chapter 3: Adding a character with animations to walk around" "Chapter 4: Adding Sound effects" ...
Whoa there's so much to do -.-

[quote="noals"]
my environement variable are set like that :
[code]
export URHO3D_REPOSITORY=/home/noname/Documents/urho3D_1.5
export URHO3D_HOME=/home/noname/Documents/urho3D_build
[/code]
how do i set the URHO3D_PREFIX_PATH or change the engine parameter "ResourcePrefixPath" in the Setup method ? that's what is suggested in a wiki tuto and the only solution i can think of to maybe fix the text problem at least...[/quote]
That should be unrelated to the text and other issues.
I'm not setting any path in my projects, so I guess that's not required (and I'm also not sure on how to do that). This may help if you really want to know that: [urho3d.github.io/documentation/1 ... _loop.html](http://urho3d.github.io/documentation/1.5/_main_loop.html)
Just tried that but it's not working like I did it.

-------------------------

noals | 2017-01-02 01:10:41 UTC | #16

[quote="gawag"]
That's an odd error. 
xml_attribute.name() and xml_attribute.value() should have the type "const char_t*" (after [pugixml.googlecode.com/svn-histo ... ibute.html](http://pugixml.googlecode.com/svn-history/r492/trunk/docs/html/classpugi_1_1xml__attribute.html)) but the compiler talks about a bool...
Try a "std::string((const char*)attr.name())". That explicit casting should work. [/quote]
it didn't work either.

[quote="gawag"]
Hm, try this relative simple GUI code: [/quote]
the window shows fine but still no text.


[quote="gawag"]
That's why I started writing about it to explain stuff. Some things are really unintuitive and could be way better.
There are currently two possible bad and outdated first project examples that use a more minimalistic approach as the samples shipped with Urho:
[github.com/damu/UrhoSampleProject](https://github.com/damu/UrhoSampleProject)
[urho3d.wikia.com/wiki/First_Project](http://urho3d.wikia.com/wiki/First_Project)
I'm currently testing the UrhoSampleProject on my GitHub and after that the First Project code on the page. I guess I'll do a new First Project Article soon: [github.com/urho3d/Urho3D/wiki/First-Project](https://github.com/urho3d/Urho3D/wiki/First-Project) (currently empty)
Maybe even an article series like "Chapter 2: Adding simple Physics" "Chapter 3: Adding a character with animations to walk around" "Chapter 4: Adding Sound effects" ...
Whoa there's so much to do -.- [/quote]
there is [url=http://darkdove.proboards.com/thread/30/urho-flow-1]this one too[/url] in the external tutorials on the wiki.
thx for the help anyway. even if i'm not an experienced programmer, usually i like to share my codes as well as examples when stuffs are done and working but here, it's just frustrating. maybe it have something to do with ubuntu or something.


could you compile [url=http://s000.tinyupload.com/index.php?file_id=82351543898966388003]my projet[/url] and try it please ? (there is just a main.cpp and the resources directories)
maybe it will work for you so at least i would know the problem doesn't come from the code but from ubuntu or cmake or whatever else.

-------------------------

gawag | 2017-01-02 01:10:41 UTC | #17

Still no text? That's odd.

I just randomly found how to do the path thing you asked for:
[code]engineParameters_["ResourcePrefixPaths"] = ";../share/Resources;../share/Urho3D/Resources";[/code]
It was in the example framework "Sample.inl".

I'll check out your code , thats a real mystery...
I kinda expect to run fine and be some Ubuntu/system issue. I tested Ubuntu before though and Urho worked fine. So let's see...

-------------------------

gawag | 2017-01-02 01:10:41 UTC | #18

Looks great!  :laughing:  [i.imgur.com/Gdp7b1L.jpg](http://i.imgur.com/Gdp7b1L.jpg)
The view can be rotated with Q, A, D and E and I can zoom with Z and Y.
I didn't change anything.

Edit: After clearing my data folder I couldn't see anything and the Urho log said:
[code]
[Tue Mar 08 04:01:19 2016] ERROR: Could not find resource Fonts/Anonymous Pro.ttf
[Tue Mar 08 04:01:19 2016] ERROR: Null font for Text
[Tue Mar 08 04:01:20 2016] ERROR: Could not find resource Shaders/HLSL/LitSolid.hlsl
[Tue Mar 08 04:01:20 2016] ERROR: Technique Techniques/Diff.xml has missing shaders
[Tue Mar 08 04:01:20 2016] ERROR: Could not find resource Shaders/HLSL/Basic.hlsl
[/code]

-------------------------

gawag | 2017-01-02 01:10:41 UTC | #19

I moved some of the default files into the folders so that it works: [s000.tinyupload.com/?file_id=085 ... 3494527147](http://s000.tinyupload.com/?file_id=08586134173494527147)
Haven't changed the code, just added data files. Some of the data files are not used, but it works like that for me.
Does that work on your system too? If not does the log say anything? How do you build that project?

-------------------------

thebluefish | 2017-01-02 01:10:43 UTC | #20

Might want to check that link :wink:

-------------------------

gawag | 2017-01-02 01:10:43 UTC | #21

oh what the hay... ohm....

fixed
Also I forgot to check if the XML code is working. I just checked the GUI and display. Checking...

Oh I'm getting the same errors... ohm...

-------------------------

gawag | 2017-01-02 01:10:43 UTC | #22

I managed to fix it: [i.imgur.com/64bV1DJ.jpg](http://i.imgur.com/64bV1DJ.jpg)

[code]
        pugi::xml_document modulesList;
        pugi::xml_parse_result result = modulesList.load_file("Data/Scripts/Modules.xml"); //load XML
        pugi::xml_node xml_root=modulesList.child("xml");  // the first child is (weirdly) the <xml> tag.

        // iterate over the child of the "<xml>" root node.
        for(pugi::xml_node_iterator it=xml_root.children().begin();
            it!=xml_root.children().end();it++)
        {
            pugi::xml_node& child=*it;

            std::string name(child.name());
std::cout<<"name: "<<name<<std::endl;
            if(name=="infos")
            {
                for(pugi::xml_attribute_iterator it=child.attributes().begin();
                   it!=child.attributes().end();it++)
                {
                    pugi::xml_attribute& attr=*it;
std::cout<<"attr: "<<attr.name()<<std::endl;

                    if(std::string((const char*)attr.name())=="count")
                        modulesCount = atoi(attr.value()); //get modules count
                }
            }
        }
std::cout<<"modulesCount: "<<modulesCount<<std::endl;
[/code]
std::stoi is actually a C++11 function. atoi is the older C possibility.

Works for me now.

(The "Device lost" message in the output appeared when I resized the Urho window for some reason but everything kept working fine. Maybe that's just a note.)

-------------------------

noals | 2017-01-02 01:10:45 UTC | #23

yes so i guess i just forgot to put the font in my ressources folder... ><
the text show fine, sometime i check the log but i guess i didn't checked at the good time, i wonder.

i have a "projet" directory on my bureau. with the console i run a little script:
[code]./cmake_generic.sh /home/noname/Bureau/projet_build -DURHO3D_SAMPLES=1 -DCMAKE_BUILD_TYPE=Debug[/code]
so it prepare the compilation in my "projet_build" directory.
then i delete the CoreData and Data shortcut from projet_build/bin and copy in it those from my projet folder with in it just what i need normally. ><
then in the console, i go to the projet_build folder and i use "make" (edit: or i just edit the main.cpp in my "projet" folder and use make directly)

[spoiler]i will try to see if my "count" return the value i want with the other method:
[code]
pugi::xml_node infos = modulesList.child("infos");
pugi::xml_attribute count;
count = infos.child_value("count");
[/code][/spoiler]
oh wait you beat me to it.
i will try your code for the xml so. it's almost 4am here, so i will do that tomorow. ^^;
oh and that's why the keys are set like this, i'm french so i have a azerty keyboad configuration through with tab you should be able to free the mouse too. and the light color represent the 3D axis ^^.

thx again for the help.

-------------------------

gawag | 2017-01-02 01:10:45 UTC | #24

[quote="noals"]
i have a "projet" directory on my bureau. with the console i run a little script:
[code]./cmake_generic.sh /home/noname/Bureau/projet_build -DURHO3D_SAMPLES=1 -DCMAKE_BUILD_TYPE=Debug[/code]
so it prepare the compilation in my "projet_build" directory.
[/quote]
Settings URHO3D_SAMPLES is only useful to tell the Urho build process if it should build the Urho samples ("01_HelloWorld", "02_HelloGUI",...). You can skip setting that as it isn't doing anything for your project.
See [urho3d.github.io/documentation/1 ... lding.html](http://urho3d.github.io/documentation/1.5/_building.html) for details on the build process.

-------------------------

noals | 2017-01-02 01:10:46 UTC | #25

the code compile fine but i have two others questions (i have tones of questions lol...) and i should be good to go.

1/ how do you enable the console ? i saw a build option to do that in the link you gave but it's only for windows and i'm sure i saw how to do that somewhere else but i don't remember where.

2/ how do i convert my int back into a string so i can append it to my text string and use [b]window_text->SetText(my_string);[/b]
checking some tutos, i think it should be something like that and i tryed different things with [b]char[/b] or other things but i wasn't able to compile with my tries:
[code]
        std::string str=("modulesCount = ");
        str.append(/*converstion of modulesCount into const char* ?*/);
        String s(str.c_str(),str.size());

      window_text->SetText(s);
[/code]

[quote]You can skip setting that as it isn't doing anything for your project.[/quote]
thx, i wasn't sure the sample option was needed or not.

-------------------------

gawag | 2017-01-02 01:10:46 UTC | #26

[quote="noals"]the code compile fine but i have two others questions (i have tones of questions lol...) and i should be good to go.

1/ how do you enable the console ? i saw a build option to do that in the link you gave but it's only for windows and i'm sure i saw how to do that somewhere else but i don't remember where.
[/quote]
Try starting your program from the terminal. There should be a visible output then. You can configure your IDE to start the program in a terminal. For example in CodeBlocks you set the "type" under "Build targets" in the project properties to "Console Application" (you may want to also uncheck "Pause when execution ends" there). In QtCreator the option is a checkbox and called "Run in terminal" in the projects run options.

[quote="noals"]
2/ how do i convert my int back into a string so i can append it to my text string and use [b]window_text->SetText(my_string);[/b]
checking some tutos, i think it should be something like that and i tryed different things with [b]char[/b] or other things but i wasn't able to compile with my tries:
[code]
        std::string str=("modulesCount = ");
        str.append(/*converstion of modulesCount into const char* ?*/);
        String s(str.c_str(),str.size());

      window_text->SetText(s);
[/code]
[/quote]
C++11 has std::to_string and std::stoi. In non C++11 the best option seems to be ostringstream: [stackoverflow.com/questions/5590 ... tring-in-c](http://stackoverflow.com/questions/5590381/easiest-way-to-convert-int-to-string-in-c).
Oh I'm actually using that to display my FPS:
[code]
std::string str="WASD, mouse and shift to move. T to toggle fill mode,\nG to toggle GUI, Tab to toggle mouse mode, Esc to quit.\n";
{
    std::ostringstream ss;
    ss<<1/timeStep;
    std::string s(ss.str());
    str.append(s.substr(0,6));  // limit the float value text length to 6 characters like "123.45" or "1.2345"
}
str.append(" FPS ");
String s(str.c_str(),str.size());  // convert std::string to Urho3D::String
window_text->SetText(s);         // set Urho3D::Text widget's text
[/code]

-------------------------

noals | 2017-01-02 01:10:47 UTC | #27

[quote="gawag"]
Try starting your program from the terminal. There should be a visible output then.[/quote]
ha yes, thx you, i will do that. i don't use an IDE, i just code with gedit. 

[quote="gawag"]
Oh I'm actually using that to display my FPS:
[/quote]
i didn't [b]#include <sstream>[/b] in my previous tries... ><

everything works fine now.
[url]http://s7.postimg.org/n7enmpda3/Capture_du_2016_03_09_18_32_21.png[/url]

thanks a lot for all your help.

-------------------------

noals | 2017-01-02 01:10:51 UTC | #28

hi, i encountered another little problem i don't really understand.

i changed a little my xml :
[code]
<xml>
<infos count="2"/>
<module1 type="1" exits="2" path="Models/cor5x20x1/cor5x20x1.mdl" texturepath="Models/cor5x20x1/cor5x20x1.xml"/>
<module2 type="2" exits="4" path="Models/room20x20x1/room20x20x1.mdl" texturepath="Models/room20x20x1/room20x20x1.xml"/>
</xml>
[/code]

and here is the code that compile fine but don't seem to return the values i want.
my string "module" actually return "module" + an int, module1 or module2 so it's not the problem.
[code]
            if(name==module) // "module" + randomLine 
            {
                for(pugi::xml_attribute_iterator it=child.attributes().begin();
                   it!=child.attributes().end();it++)
                {
                    pugi::xml_attribute& attr=*it;

                    if(std::string ((const char*)attr.name())=="type")
                    {
                        moduleType=std::atoi(attr.value());
                    }
                    if(std::string ((const char*)attr.name())=="exits")
                    {
                        exits=std::atoi(attr.value());
                    }
                    if(std::string ((const char*)attr.name())=="path")
                    {
                        modulePath=attr.value();
                    }
                    if(std::string ((const char*)attr.name())=="texturepath")
                    {
                        moduleTexturePath=attr.value();
                    }
                }
            }
[/code]
i didn't verified yet but moduleType and exits should works fine since they are int.
modulePath and moduleTexturePath are std:string so i though i didn't need to use std::atoi
i tryed the same conversion method as for the other or i just tryed :
[code]
        String mP(modulePath.c_str(),modulePath.size());
        String mTP(moduleTexturePath.c_str(),moduleTexturePath.size());[/code]
but they return nothing apparently.
what did i do wrong ?

[url=http://s000.tinyupload.com/index.php?file_id=07720525962192566728]my project files[/url]

thinking about t, i think it maybe have something to do with the "" because my string maybe return the value from the xml but since i want to use it directly to load a module, it don't work because it end up being :
[code]roomObject->SetModel(cache->GetResource<Model>(Models/room20x20x1/room20x20x1.mdl));[/code]
instead of :
[code]roomObject->SetModel(cache->GetResource<Model>("Models/room20x20x1/room20x20x1.mdl"));[/code]

i don't know, i'm a little confused.

-------------------------

noals | 2017-01-02 01:10:52 UTC | #29

bah, nvm. i will try to clean up my code a little because with all those conversion and string, it's a mess.
before i was able to return my moduleX string in the console so i know it worked but now with my tries, even that seem to return nothing.

there is something i will never understand through.
why every engine makes their own int, their own string and stuff like that ?
can't peoples just update the c++ library so everyone can use the same object ? sigh...

-------------------------

thebluefish | 2017-01-02 01:10:52 UTC | #30

[quote="noals"]there is something i will never understand through.
why every engine makes their own int, their own string and stuff like that ?
can't peoples just update the c++ library so everyone can use the same object ? sigh...[/quote]

Because of this:

[img]http://imgs.xkcd.com/comics/standards.png[/img]

That is, the current standards are kind of a pain in the ass. Not to mention things like Vector2/3/4, Matrix, Quaternion, etc... are not standard at all. On top of that, things such as int can vary in byte size, so they're usually standardized to fixed bit sizes (int_16, uint_32, etc...) in many libraries.

Luckily for things like String, we can convert to/from C-style strings much like most other libraries. That way, converting from one library to another usually involves something like:

[code]Urho3D::String ToUrho3D(lib2::String otherString) { return Urho3D::String(lib2String.c_str()); }[/code]

and many other formats are converted very similarly:

[code]Urho3D::Vector3 ToUrho3D(lib2::Vector3 otherVector) { return Urho3D::Vector3(otherVector.x, otherVector.y, otherVector.z); }[/code]

This allows each library to work with common data types in a way that works for them. If the STL is not able to handle a problem elegantly, it's easier to maintain your own implementation on top of that than rely on a non-standard "standard".

-------------------------

noals | 2017-01-02 01:10:52 UTC | #31

yeah, it's like a saying in france : "why makes things easier when we can make it complicated" ...
if int for example became obsolete because of 64 bit OS and stuff like that, people could just remplace int by int32 and int64, etc... so everyone use the same.
i'm really a beginner and i can't even get some values from an xml properly but i have a logical mind and sometime i think peoples didn't understand the concept of object oriented programmation.

anyway, i have work to do. i feel like i'm stepping from the little main.cpp to a more complexe project so i'm kinda satisfied to make some progress but it become harder fast, wish me courage. ^^;

-------------------------

