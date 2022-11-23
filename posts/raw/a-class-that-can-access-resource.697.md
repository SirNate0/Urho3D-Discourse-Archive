vivienneanthony | 2017-01-02 01:02:10 UTC | #1

Hello

I would like to create a World class that I can use to create objects using various methods. I don't want to make it a component but still possible to accesss Urho3D so It can place objects among other things. I am placing the code. Do anyone have any suggestions.

Vivienne

[b]Usage[/b]
[code]/// Build world
    WorldBuild World;

    /// Plant rocks
    for(unsigned int i=0; i<20; i++)
    {

        /// Pick a random spot
        Spotx=rand()%10000;
        Spotz=rand()%10000;

        randomSpotx=((float)Spotx/100)-50.0f;
        randomSpotz=((float)Spotz/100)-50.0f;

        World.CreateObjectAlongPath(randomSpotx,randomSpotz, 20, 100.0f);
    }
[/code]
[b]WordBuild.h[/b]
[code]#ifndef WORLDBUILD_H
#define WORLDBUILD_H

using namespace Urho3D;


#define WorldOjectCollisionMapLimit  1000

/// Temporary structure
struct WorldOjectCollisionMap
{
    float size_x;
    float size_y;
    float size_z;
    float origin_x;
    float origin_y;
    float origin_z;
    int lod;
};

class WorldBuild : public Component
{

public:
/// Construct.
    WorldBuild();
    virtual ~WorldBuild();

    /// public
    int CreateObjectAlongPath(float x, float z, float length, float numberofobjects);
protected:

private:
    float ComputeDistance(int x1, int y1, int x2, int y2);

    /// Saved Collision Objects to 0
    int SaveCollisionObjects;

    /// Set world limit of objects to test for collision
    WorldOjectCollisionMap CollisionBounds[WorldOjectCollisionMapLimit];


};

#endif // WORLDBUILD_H
[/code]


[b]WorldBuild.cpp[/b]
[code]/// Headers and etc
#include "CoreEvents.h"
#include "Engine.h"
#include "ProcessUtils.h"
#include "Octree.h"
#include "Model.h"
#include "Material.h"
#include "ResourceCache.h"
#include "Graphics.h"

#include "AnimationController.h"
#include "Character.h"
#include "Context.h"
#include "MemoryBuffer.h"
#include "PhysicsEvents.h"
#include "PhysicsWorld.h"
#include "RigidBody.h"
#include "Scene.h"
#include "SceneEvents.h"
#include "Player.h"
#include "Renderer.h"
#include "UI.h"
#include "Node.h"
#include "CollisionShape.h"
#include "StaticModel.h"


#include <iostream>
#include <cmath>
#include <algorithm>
#include <utility>


using namespace std;


#define NORTH 1
#define NORTHEAST 2
#define EAST 3
#define SOUTHEAST 4
#define SOUTH  5
#define SOUTHWEST 6
#define WEST 7
#define NORTHWEST 8

using namespace std;

#include "WorldBuild.h"

WorldBuild::WorldBuild()
{
    //ctor
}

WorldBuild::~WorldBuild()
{
    //dtor
}

float  WorldBuild::ComputeDistance(int x1, int y1, int x2, int y2)
{
    float  xrange= x1-x2;
    float  yrange= y1-y2;

    return sqrt((xrange*xrange)+(yrange*yrange));
}

int WorldBuild::CreateObjectAlongPath(float x, float z, float length, float numberofobjects)
{
   /// Get Needed SubSystems
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();

    Scene * scene_;

    /// Need variables
    float lengthlimitdistance= length;


    float objectsalongpath=numberofobjects;
    float objectsdistance=lengthlimitdistance/objectsalongpath;
    float objectincrement=1;

    float origin_x=x;
    float origin_z=z;

    float difference_z=0.0f;
    float difference_x=0.0f;

    float position_x=0.0f;
    float position_z=0.0f;

    float newposition_x=0.0f;
    float newposition_z=0.0f;
    float olddistance=0.0f;

    srand (time(NULL));

    position_x=origin_x;
    position_z=origin_z;


    do
    {
        /// Pick a random directoin
        int direction=rand()%8+1;

        /// Select coordinate change based on random direction
        switch (direction)
        {
        case NORTH:
            difference_x=0;
            difference_z=1;
            break;
        case NORTHEAST:
            difference_x=1;
            difference_z=1;
            break;
        case EAST:
            difference_x=+1;
            difference_z=0;
            break;
        case SOUTHEAST:
            difference_x=1;
            difference_z=-1;
            break;
        case SOUTH:
            difference_x=0;
            difference_z=-1;
            break;
        case SOUTHWEST:
            difference_x=-1;
            difference_z=-1;
            break;
        case WEST:
            difference_x=-1;
            difference_z=0;
            break;
        case NORTHWEST:
            difference_x=-1;
            difference_z=1;
            break;
        }

        /// If distance less then current distance then while continue loop
        if(ComputeDistance(position_x+difference_x, origin_x, position_z+difference_z,origin_z)<olddistance)
        {
            continue;
        }
        else
        {
            /// Create a new position
            newposition_x=position_x+difference_x;
            newposition_z=position_z+difference_z;

            ///  Copy newposition to current positon
            position_x=newposition_x;
            position_z=newposition_z;

            /// Get distance
            olddistance=ComputeDistance(position_x, origin_x, position_z, origin_z);

            /// Try this method to use percentange
            if(olddistance/lengthlimitdistance>(objectsdistance*objectincrement)/lengthlimitdistance)
            {
                objectincrement++;
                cout << "Spot Found\r\n";

                /// Add a Rock to the seen - Rock Node
                Node * RockNode = scene_ -> CreateChild("RockNode");

                StaticModel * RockStaticModel = RockNode->CreateComponent<StaticModel>();



                RockStaticModel->SetModel(cache->GetResource<Model>("Resources/Models/Rock1.mdl"));
                RockStaticModel->ApplyMaterialList("Resources/Models/Rock1.txt");

                /// Create Nodes and COmponents
                RockStaticModel->SetCastShadows(true);

                BoundingBox  staticmodelbox = RockStaticModel->GetBoundingBox();
                Vector3  staticmodelboxcenter= staticmodelbox.HalfSize();


                /// Select a possible position to place a Rock
                Vector3 selectPosition=Vector3(position_x,terrain->GetHeight(Vector3(position_x,0.0f,position_z))+staticmodelboxcenter.y_,position_z);

                /// Save coordinates
                CollisionBounds[SaveCollisionObjects].size_x=staticmodelboxcenter.x_;
                CollisionBounds[SaveCollisionObjects].size_y=staticmodelboxcenter.y_;
                CollisionBounds[SaveCollisionObjects].size_z=staticmodelboxcenter.z_;
                CollisionBounds[SaveCollisionObjects].origin_x=position_x;
                CollisionBounds[SaveCollisionObjects].origin_z=terrain->GetHeight(Vector3(position_x,0.0f,position_z))+staticmodelboxcenter.y_;
                CollisionBounds[SaveCollisionObjects].origin_z=position_z;
                CollisionBounds[SaveCollisionObjects].lod=0;

                /// Save object
                SaveCollisionObjects++;

                /// Set Rock position
                RockNode->SetPosition(selectPosition);
                RockNode->SetRotation(Quaternion(Random(360),Vector3(0.0f,1.0f,0.0f)));
            }

            /// Output X, Y
            cout << position_x << " " << position_z << "\r\n";
        }
    }
    while(olddistance<=lengthlimitdistance);


    return 1;
}
[/code]

-------------------------

att | 2017-01-02 01:02:11 UTC | #2

You can consider subclass from Object.

-------------------------

vivienneanthony | 2017-01-02 01:02:11 UTC | #3

[quote="att"]You can consider subclass from Object.[/quote]

I have to look in the morning. I'm not sure how (It's late).

If anything, I would think it would be a subclass of the Procedural class I made. Anyway,  right now I just want to access it then have it able to access Urho3D.

-------------------------

vivienneanthony | 2017-01-02 01:02:12 UTC | #4

[quote="att"]You can consider subclass from Object.[/quote]

I tried the following code but getting this error.

[code]WorldBuild.h||In member function ?virtual Urho3D::ShortStringHash WorldBuild::GetBaseType() const?:|
WorldBuild.h|24|error: ?GetBaseTypeStatic? was not declared in this scope|
ExistenceClient.cpp|3816|error: no matching function for call to ?WorldBuild::WorldBuild()?|
ExistenceClient.cpp|3816|note: candidates are:|
WorldBuild.h|29|note: WorldBuild::WorldBuild(Urho3D::Context*)|
WorldBuild.h|29|note:   candidate expects 1 argument, 0 provided|
WorldBuild.h|21|note: WorldBuild::WorldBuild(const WorldBuild&)|
WorldBuild.h|21|note:   candidate expects 1 argument, 0 provided|
||=== Build finished: 7 errors, 3 warnings ===|
[/code]

WorldBuild.h
[code]#ifndef WORLDBUILD_H
#define WORLDBUILD_H

using namespace Urho3D;


#define WorldOjectCollisionMapLimit  1000

/// Temporary structure
struct WorldOjectCollisionMap
{
    float size_x;
    float size_y;
    float size_z;
    float origin_x;
    float origin_y;
    float origin_z;
    int lod;
};

class WorldBuild
{
    /// Define subclass
    OBJECT(WorldBuild)

public:

    /// Construct.
    WorldBuild(Context* context);
    virtual ~WorldBuild();

    /// Register object factory and attributes.
    static void RegisterObject(Context* context);

    /// public
    int CreateObjectAlongPath(float x, float z, float length, float numberofobjects);

protected:

private:
    float ComputeDistance(int x1, int y1, int x2, int y2);

    /// Saved Collision Objects to 0
    int SaveCollisionObjects;

    /// Set world limit of objects to test for collision
    WorldOjectCollisionMap CollisionBounds[WorldOjectCollisionMapLimit];
};

#endif // WORLDBUILD_H
[/code]

WorldBuild.cpp
[code]/// Headers and etc
#include "CoreEvents.h"
#include "Engine.h"
#include "ProcessUtils.h"
#include "Octree.h"
#include "Model.h"
#include "Material.h"
#include "ResourceCache.h"
#include "Graphics.h"

#include "AnimationController.h"
#include "Character.h"
#include "Context.h"
#include "MemoryBuffer.h"
#include "PhysicsEvents.h"
#include "PhysicsWorld.h"
#include "RigidBody.h"
#include "Scene.h"
#include "SceneEvents.h"
#include "Player.h"
#include "Renderer.h"
#include "UI.h"
#include "Node.h"
#include "CollisionShape.h"
#include "StaticModel.h"

#include <iostream>
#include <cmath>
#include <algorithm>
#include <utility>
#include "WorldBuild.h"

using namespace std;

#define NORTH 1
#define NORTHEAST 2
#define EAST 3
#define SOUTHEAST 4
#define SOUTH  5
#define SOUTHWEST 6
#define WEST 7
#define NORTHWEST 8

WorldBuild::WorldBuild(Context* context)
{
    //ctor
}

WorldBuild::~WorldBuild()
{
    //dtor
}

void WorldBuild::RegisterObject(Context* context)
{
    context->RegisterFactory<WorldBuild>();
}

float  WorldBuild::ComputeDistance(int x1, int y1, int x2, int y2)
{
    float  xrange= x1-x2;
    float  yrange= y1-y2;

    return sqrt((xrange*xrange)+(yrange*yrange));
}

int WorldBuild::CreateObjectAlongPath(float x, float z, float length, float numberofobjects)
{
    /// Get Needed SubSystems
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();

    Scene * scene_;

    /// Need variables
    float lengthlimitdistance= length;


    float objectsalongpath=numberofobjects;
    float objectsdistance=lengthlimitdistance/objectsalongpath;
    float objectincrement=1;

    float origin_x=x;
    float origin_z=z;

    float difference_z=0.0f;
    float difference_x=0.0f;

    float position_x=0.0f;
    float position_z=0.0f;

    float newposition_x=0.0f;
    float newposition_z=0.0f;
    float olddistance=0.0f;

    srand (time(NULL));

    position_x=origin_x;
    position_z=origin_z;


    do
    {
        /// Pick a random directoin
        int direction=rand()%8+1;

        /// Select coordinate change based on random direction
        switch (direction)
        {
        case NORTH:
            difference_x=0;
            difference_z=1;
            break;
        case NORTHEAST:
            difference_x=1;
            difference_z=1;
            break;
        case EAST:
            difference_x=+1;
            difference_z=0;
            break;
        case SOUTHEAST:
            difference_x=1;
            difference_z=-1;
            break;
        case SOUTH:
            difference_x=0;
            difference_z=-1;
            break;
        case SOUTHWEST:
            difference_x=-1;
            difference_z=-1;
            break;
        case WEST:
            difference_x=-1;
            difference_z=0;
            break;
        case NORTHWEST:
            difference_x=-1;
            difference_z=1;
            break;
        }

        /// If distance less then current distance then while continue loop
        if(ComputeDistance(position_x+difference_x, origin_x, position_z+difference_z,origin_z)<olddistance)
        {
            continue;
        }
        else
        {
            /// Create a new position
            newposition_x=position_x+difference_x;
            newposition_z=position_z+difference_z;

            ///  Copy newposition to current positon
            position_x=newposition_x;
            position_z=newposition_z;

            /// Get distance
            olddistance=ComputeDistance(position_x, origin_x, position_z, origin_z);

            /// Try this method to use percentange
            if(olddistance/lengthlimitdistance>(objectsdistance*objectincrement)/lengthlimitdistance)
            {
                objectincrement++;
                cout << "Spot Found\r\n";

                /// Add a Rock to the seen - Rock Node
                Node * RockNode = scene_ -> CreateChild("RockNode");

                StaticModel * RockStaticModel = RockNode->CreateComponent<StaticModel>();



                RockStaticModel->SetModel(cache->GetResource<Model>("Resources/Models/Rock1.mdl"));
                RockStaticModel->ApplyMaterialList("Resources/Models/Rock1.txt");

                /// Create Nodes and COmponents
                RockStaticModel->SetCastShadows(true);

                BoundingBox  staticmodelbox = RockStaticModel->GetBoundingBox();
                Vector3  staticmodelboxcenter= staticmodelbox.HalfSize();


                /// Select a possible position to place a Rock
                Vector3 selectPosition=Vector3(position_x,terrain->GetHeight(Vector3(position_x,0.0f,position_z))+staticmodelboxcenter.y_,position_z);

                /// Save coordinates
                CollisionBounds[SaveCollisionObjects].size_x=staticmodelboxcenter.x_;
                CollisionBounds[SaveCollisionObjects].size_y=staticmodelboxcenter.y_;
                CollisionBounds[SaveCollisionObjects].size_z=staticmodelboxcenter.z_;
                CollisionBounds[SaveCollisionObjects].origin_x=position_x;
                CollisionBounds[SaveCollisionObjects].origin_z=terrain->GetHeight(Vector3(position_x,0.0f,position_z))+staticmodelboxcenter.y_;
                CollisionBounds[SaveCollisionObjects].origin_z=position_z;
                CollisionBounds[SaveCollisionObjects].lod=0;

                /// Save object
                SaveCollisionObjects++;

                /// Set Rock position
                RockNode->SetPosition(selectPosition);
                RockNode->SetRotation(Quaternion(Random(360),Vector3(0.0f,1.0f,0.0f)));
            }

            /// Output X, Y
            cout << position_x << " " << position_z << "\r\n";
        }
    }
    while(olddistance<=lengthlimitdistance);


    return 1;
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:02:12 UTC | #5

I changed the follow and get this error.

[code]Error
/media/home2/vivienne/Existence/Source/ExistenceApps/ExistenceClient/WorldBuild.cpp||In member function ?int WorldBuild::CreateObjectAlongPath(float, float, float, float)?:|
/media/home2/vivienne/Existence/Source/ExistenceApps/ExistenceClient/WorldBuild.cpp|85|error: invalid use of incomplete type ?struct Urho3D::Terrain?|
/media/home2/vivienne/Existence/Source/Engine/Physics/CollisionShape.h|45|error: forward declaration of ?struct Urho3D::Terrain?|
/media/home2/vivienne/Existence/Source/ExistenceApps/ExistenceClient/WorldBuild.cpp|196|error: invalid use of incomplete type ?struct Urho3D::Terrain?|
/media/home2/vivienne/Existence/Source/Engine/Physics/CollisionShape.h|45|error: forward declaration of ?struct Urho3D::Terrain?|
/media/home2/vivienne/Existence/Source/ExistenceApps/ExistenceClient/WorldBuild.cpp|203|error: invalid use of incomplete type ?struct Urho3D::Terrain?|
/media/home2/vivienne/Existence/Source/Engine/Physics/CollisionShape.h|45|error: forward declaration of ?struct Urho3D::Terrain?|
/media/home2/vivienne/Existence/Source/Engine/Scene/Node.h||In member function ?T* Urho3D::Node::GetComponent() const [with T = Urho3D::Terrain]?:|
/media/home2/vivienne/Existence/Source/ExistenceApps/ExistenceClient/WorldBuild.cpp:83|59|instantiated from here|
/media/home2/vivienne/Existence/Source/Engine/Scene/Node.h|492|error: incomplete type ?Urho3D::Terrain? used in nested name specifier|
||=== Build finished: 7 errors, 0 warnings ===|[/code]

In WorldBuild.cpp
[code]/// Try to get the node information;
    Scene * scene_;

    Node* terrainNode = scene_->GetChild("Terrain",true);

    Terrain* terrain = terrainNode->GetComponent<Terrain>();

    Terrain->GetHeight(Vector3(0.0f,0.0f,0.0f));
[/code]

WorldBuild.h[code]
class WorldBuild :public Component
{
    /// Define subclass
    OBJECT(WorldBuild)

public:

    /// Construct.
    WorldBuild(Context* context);
    virtual ~WorldBuild();

    /// Register object factory and attributes.
    static void RegisterObject(Context* context);[/code]




WorldBuild.cpp
[code]
WorldBuild::WorldBuild(Context* context):Component(context)
{
    //ctor
}

WorldBuild::~WorldBuild()
{
    //dtor
}

/// Register a object
void WorldBuild::RegisterObject(Context* context)
{
    context->RegisterFactory<WorldBuild>();
}[/code]

-------------------------

vivienneanthony | 2017-01-02 01:02:12 UTC | #6

Worldbuild is a component subclass but looking for it to  juust be a object sublass not component based.

-------------------------

vivienneanthony | 2017-01-02 01:02:12 UTC | #7

The code was fixed. It's a component.

The problem I have is with one line like seriously. The last line specifically. It's creating the latter debug segmentation fault. I used the same exact code to get the scene in a Character:LogicComponent basically 

[code]   /// Try to get the node information;
    Scene * scene_;

    scene_ = this -> GetScene();

    Node* terrainNode = scene_ ->GetChild("Terrain",true);
[/code]

Error Debug
[code]Debugger name and version: GNU gdb (Ubuntu/Linaro 7.4-2012.04-0ubuntu2.1) 7.4-2012.04
Child process PID: 26395
Program received signal SIGSEGV, Segmentation fault.
In Urho3D::Node::GetChild(Urho3D::StringHash, bool) const [clone .constprop.86] () ()
Debugger finished with status 0
[/code]


I also tried creating a component to the scene like.

[code]WorldBuild * WorldBuildObjects = scene_-> CreateComponent<WorldBuild>();[/code]

That didn't work.

-------------------------

att | 2017-01-02 01:02:12 UTC | #8

Do you called WorldBuild::RegisterObject(context); somewhere ?
And I think WorldBuild should subclass from Object like this,
class WorldBuild : public Object
{
     OBJECT(WorldBuild);

-------------------------

vivienneanthony | 2017-01-02 01:02:13 UTC | #9

[quote="att"]Do you called WorldBuild::RegisterObject(context); somewhere ?
And I think WorldBuild should subclass from Object like this,
class WorldBuild : public Object
{
     OBJECT(WorldBuild);[/quote]


I do. I got it to work with someone help. They seen a "Da!" moment line of code I forgot to add.

The way I got it to work is as a class as a logic component. It's not what I intended. Basically I have to create a WorldBuild node in the scene then attach the logic component. I can use functions inside the class to populate the scene.  Afterward removing the WorldBuild node.

Not exactly what I want but it works.

[code]/// Build world
    Node * WorldObjectNode = scene_-> CreateChild("WorldBuildNode");
    WorldBuild * WorldBuildObjects = WorldObjectNode  -> CreateComponent<WorldBuild>();


    /// Plant rocks
    for(unsigned int i=0; i<40; i++)
    {

        /// Pick a random spot
        Spotx=rand()%10000;
        Spotz=rand()%10000;

        randomSpotx=((float)Spotx/100)-50.0f;
        randomSpotz=((float)Spotz/100)-50.0f;

        WorldBuildObjects -> CreateObjectAlongPath(randomSpotx,randomSpotz, 50.0f,3);
    }
[/code]

-------------------------

att | 2017-01-02 01:02:13 UTC | #10

I see,
You can subclass WorldBuild from Object,  like UI, Graphics etc..Then you can register WorldBuild as a Subsystem or just a variable . Not need to create a node to create a WorldBuild.

-------------------------

vivienneanthony | 2017-01-02 01:02:13 UTC | #11

[quote="att"]I see,
You can subclass WorldBuild from Object,  like UI, Graphics etc..Then you can register WorldBuild as a Subsystem or just a variable . Not need to create a node to create a WorldBuild.[/quote]

I have to look at the code again to see how. It doesn't seem clear to me.  So, when I can take a deeper look I will.

-------------------------

