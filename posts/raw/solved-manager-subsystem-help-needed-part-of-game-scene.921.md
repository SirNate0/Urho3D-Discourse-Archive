vivienneanthony | 2017-01-02 01:04:06 UTC | #1

Hello.

Could someone help me figure out what's wrong. I am creating a Manager subsystem and it crashes when I do a a call for get   subsystem in a function.

Vivienne

Original Post
---------------
Do someone have  a suggestion? The client is working I'm making and I want to add some game elements. My initial thought was exploration which would work. I also been looking at adding some RPG element. I some RealMyst videos and that maybe that would be cool to do with a Scifi Star Trek and general SciFI(a lot) mashed up with some FPS.

The current code generates a scene with no goal and a person can roam around but I want to change that.

I am thinking of 

1) Adding to the Existence main app class some functions to load objects that can be used for interaction. Problem is the function list for that class would be too much over time.

or 
[b][color=#00BF00]
2) Creating a Manager  class subsystem that load scene and save objects like NPC'S and other objects from a XML(Diff) file which would tie will with the procedural generatlon and future networking.. Then maybe define functionality for objects inside the Node character/entity class on a individual basis. I'm assuming it will have to be a scene/world component like Renderer/UI etc aka Manager[/color]
[/b]
or

3) Do the above and also create a game Goal/Task Manager that handles goal aspects.

-------------------------

vivienneanthony | 2017-01-02 01:04:06 UTC | #2

I created the following code and it works correctly. In light, I'm thinking a function in my worldbuild to save extra objects in a xml(diff.xml scene file for example). Then use a function in the Manager to populate a scene with that file loading a xml. It's some extra step but if I want to set up networking it will be super helpful.

The software is crashing at the GetSubsystem line of Manager.cpp.


Manager.h
[code]#ifndef MANAGER_H
#define MANAGER_H


namespace Urho3D
{
class Geometry;
class Drawable;
class Light;
class Material;
class Pass;
class Technique;
class Octree;
class Graphics;
class RenderPath;
class RenderSurface;
class ResourceCache;
class Skeleton;
class OcclusionBuffer;
class Texture2D;
class TextureCube;
class View;
class Zone;
class Scene;


class URHO3D_API Manager : public Object
{
    OBJECT(Manager);
public:
    Manager(Context* context);

    int SetScene(Scene* scene);
    int AddObject(int type, const char * name, float x, float y, float z, const char *filename);

    virtual ~Manager();
protected:
private:
  /// Scene pointer.
    WeakPtr<Scene> scene_;
};
}
#endif // MANAGER_H

[/code]

Manager.cpp
[code]#include "Camera.h"
#include "ResourceCache.h"
#include "Renderer.h"
#include "Camera.h"
#include "Window.h"
#include "Button.h"
#include "LineEdit.h"
#include "UIElement.h"
#include "BoundingBox.h"
#include "UIEvents.h"
#include "DebugRenderer.h"
#include "File.h"
#include "FileSystem.h"
#include "XMLFile.h"
#include "XMLElement.h"
#include "Deserializer.h"
#include "Cursor.h"
#include "FileSystem.h"
#include "ListView.h"
#include "Console.h"
#include "RigidBody.h"
#include "CollisionShape.h"
#include "PhysicsWorld.h"
#include "Animation.h"
#include "AnimatedModel.h"
#include "AnimationController.h"
#include "Character.h"
#include "Terrain.h"
#include "EngineEvents.h"
#include "Zone.h"
#include "Log.h"
#include "Skybox.h"
#include "Sprite.h"
#include "StaticModelGroup.h"
#include "BillboardSet.h"
#include "Random.h"
#include "RenderPath.h"
#include "Color.h"
#include "Graphics.h"

///C/C++ related header files
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <locale>
#include <ctime>
#include <cmath>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <iostream>
#include <utility>
#include <algorithm>

/// Existence Header files
#include "GameStateHandler.h"
#include "Account.h"
#include "GameObject.h"
#include "WorldBuild.h"
#include "Manager.h"

#include "../../Engine/Procedural/RandomNumberGenerator.h"

#include "DebugNew.h"

Manager::Manager(Context* context) :
    Object(context)
{
    scene_=NULL;
}

Manager::~Manager()
{
    //dtor
}

int Manager::SetScene(Scene* scene)
{
    scene_=scene;
}

int Manager::AddObject(int type, const char * name, float x, float y, float z, const char *filename)
{
    /// Get Needed SubSystems
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();

    /// if no scene return 0
    if(!scene_)
    {
        return 0;
    }

    /// Get scene and terrain node
    Node* terrainNode = scene_->GetChild("GeneratedTerrainRule_Terrain",true);
    Terrain * terrain = terrainNode -> GetComponent<Terrain>();

    Vector3 terrainposition = terrainNode ->GetPosition();
    IntVector2 terrainsize = terrain->GetNumVertices();

    cout << terrainsize.ToString().CString() <<endl;
    cout << "test" << endl;

    return 1;
}


[/code]

-------------------------

vivienneanthony | 2017-01-02 01:04:06 UTC | #3

This is what the code is used in.
[code]
/// Routine for Console Environment related actions
int ExistenceClient::ConsoleActionBuild(const char * lineinput)
{

    /// get resources
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();
    Manager * manager_ = GetSubsystem<Manager>();

    /// string string leaving something comparable
    string argumentsstring = lineinput;
    string argument[40];

    /// create a idx
    int idx = 0;

    /// transfer to lowercase
    std::transform(argumentsstring.begin(), argumentsstring.end(), argumentsstring.begin(), ::tolower);

    /// copy string to stream
    stringstream ssin(argumentsstring);

    /// loop through arguments
    while (ssin.good() && idx < 10)
    {
        ssin >> argument[idx];
        ++idx;
    }

    /// parameters for debug related command
    if(argument[1]=="addobject")
    {
        /// Call the manager
       bool result=manager_-> AddObject(atoi(argument[2].c_str()),argument[3].c_str(), StringToFloat(argument[4]), StringToFloat(argument[5]), StringToFloat(argument[6]), argument[7].c_str());
    }


    return 1;
}

[/code]

-------------------------

thebluefish | 2017-01-02 01:04:07 UTC | #4

What's the error when it crashes?

-------------------------

vivienneanthony | 2017-01-02 01:04:07 UTC | #5

[quote="thebluefish"]What's the error when it crashes?[/quote]

I'm not home but when I am Ill post it.

The line I remember is 

Return context <-GetSystemSub

Either the manager API does not have the.context I think.

-------------------------

thebluefish | 2017-01-02 01:04:08 UTC | #6

In this line:
[code]
Manager * manager_ = GetSubsystem<Manager>();
[/code]

Can you verify that manager_ is a valid pointer? Also your other variable names indicate that you may meant to name it "manager" instead of "manager_". That could cause some issues if things aligned the right way.

-------------------------

codingmonkey | 2017-01-02 01:04:08 UTC | #7

I guess that need to make the static proc RegistryObject or RegistryFactory for your manager class

-------------------------

vivienneanthony | 2017-01-02 01:04:09 UTC | #8

Here is a screenshoot at the point of crash with the specific line.

[i.imgur.com/K5QBA9F.png](http://i.imgur.com/K5QBA9F.png)

-------------------------

vivienneanthony | 2017-01-02 01:04:09 UTC | #9

[quote="codingmonkey"]I guess that need to make the static proc RegistryObject or RegistryFactory for your manager class[/quote]

I shouldn't have to if its a subsystem. It's not fully registering I think. :-/

-------------------------

vivienneanthony | 2017-01-02 01:04:09 UTC | #10

This is complete. Going update Github with the code.

-------------------------

