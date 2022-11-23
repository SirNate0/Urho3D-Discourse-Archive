noals | 2017-01-02 01:12:17 UTC | #1

hi,

my project start to looks like something but i need to do some collision check
[url=http://www.hostingpics.net/viewer.php?id=901234cooltest3.png][img]http://img15.hostingpics.net/pics/901234cooltest3.png[/img][/url]

after checking the wiki, i think that for each of my module, i need to add this to get a precise bounding box
[code]
//add physic        dont forget to include RigidBody and CollisionShape
        RigidBody* m_Body=moduleNode->CreateComponent<RigidBody>();
        m_Body->SetMass(0);  //0 for static object
        m_Body->SetFriction(0.6);        // friction with other objects (like the ground)
//add collision shape
        CollisionShape* m_BBox=moduleNode->CreateComponent<CollisionShape>();      
        m_BBox->SetTriangleMesh(cache->GetResource<Model>(path));
[/code]
then i can use layers
[code]
m_body->SetCollisionLayer(2)
[/code]
but how do you do a collision check between two bounding box ? what must i use ?
so that if a module spawn on another, i change it or delete it or whatever.


and by the way, i have a little question :  is there a way to get  a list of all the scene child ?

thx

-------------------------

noals | 2017-01-02 01:12:17 UTC | #2

i found this page : [urho3d.github.io/documentation/1.5/_physics.html](http://urho3d.github.io/documentation/1.5/_physics.html) that direct me to [url=http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_rigid_body.html#ae8efeb02d37b545321b84f35ed355b34]GetCollidingBodies()[/url]

so i guess it could work with :
[code]
if(m_Body->GetCollidingBodies() != 0)  //or NULL ?
{
    //there is a collision with another module : do something.
}
else
{
    //there is no collision, the module can stay here.
}
[/code]

i will try that and see.

-------------------------

Nerrik | 2017-01-02 01:12:17 UTC | #3

in my project iam working with the E_NODECOLLISION event.
[code]
SubscribeToEvent(mynode, E_NODECOLLISION, HANDLER(objectevents, HandleObjectCollision)); //for every node that should trigger something on collision


void objectevents::HandleObjectCollision(StringHash eventT, VariantMap& eData)
{
RigidBody* body = static_cast<RigidBody*>(eData[P_BODY].GetPtr());
Component* comp;
comp=body->GetComponent("StaticModel");
Node* myobject;
myobject=comp->GetNode ();

......

}[/code]


I have a xml file looks like this to load and subscribe the events per level in a function:

[code]<?xml version="1.0"?>
<objects id="1">
    <object type="object" id="churchentry" visible="false" />
    <object type="event" do="oncollude" />
    <object type="do" do="teleport" value="-13.8625f, -265.351f, 251.486f" timer="0" />
  
 <object type="object" id="churchentry2" visible="false" />
    <object type="event" do="oncollude" />
    <object type="do" do="teleport" value="-10.1958f, 47.8538f, -100.748f" timer="0" />
</objects>[/code]

-------------------------

noals | 2017-01-02 01:12:17 UTC | #4

your method seems a bit complicated to me but thx anyway. i didn't tryed anything yet, i will check it out later, the SubscribeToEvent could be usefull.

-------------------------

Nerrik | 2017-01-02 01:12:17 UTC | #5

[quote="noals"]your method seems a bit complicated to me but thx anyway. i didn't tryed anything yet, i will check it out later, the SubscribeToEvent could be usefull.[/quote]

yep i try to don't hardcode too much in my game, so i need this xml solution. You can do it with urho node variables too, or just hardcode it :wink:

and yep you will need SubscribeToEvent.

You can also only subscribe your mainchar and look with what he collude. (setting variables or names to the nodes to choose the trigger), but then your objects don't interact between each other

-------------------------

jmiller | 2017-06-29 08:03:36 UTC | #6

[quote="noals"]and by the way, i have a little question :  is there a way to get  a list of all the scene child ?[/quote]

Hi,
Scene::GetChildren() is one way.
Here is a quick and dirty recursive print method, copypasta untested, Using Urho head revision... should not be too different for 1.5.
[url=http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_scene.html]Scene[/url] is a type of Node, so this works with both types.

[details=Code][code]
decl:
void PrintTree(Urho3D::Node* node, unsigned level = 0);

void SceneManager::PrintTree(Node* node, unsigned level /* = 0 */) {
  // if you do not like spam
  // if (node->HasComponent<TerrainPatch>()) return;

  String s('+', level); // indentation
  s += "<" + node->GetName() + ">" + " pos:" + String(node->GetPosition());

  URHO3D_LOGRAW(s + '\n'); // opt. URHO3D_LOGINFO etc.

  if (!node->GetChildren().Empty()) {
    const Vector<SharedPtr<Node>> children(node->GetChildren()); // pre-C++11 needs a space: <SharedPtr<Node> >
    for (unsigned i = 0; i < children.Size(); ++i) {
      PrintTree(children[i], level + 1);
    }
  }
}
[/code][/details]

-------------------------

noals | 2017-01-02 01:12:18 UTC | #7

[quote="Nerrik"]

yep i try to don't hardcode too much in my game, so i need this xml solution. You can do it with urho node variables too, or just hardcode it :wink:

and yep you will need SubscribeToEvent.

You can also only subscribe your mainchar and look with what he collude. (setting variables or names to the nodes to choose the trigger), but then your objects don't interact between each other[/quote]
i also use xml, i code so that when it is compiled, you can just change the modules at your liking with the xml. (or other things later)
[code]<room0 exits="4" path="Models/room0.mdl" texturepath="Materials/blank.xml"/>[/code]
i didn't do a character yet but i know i will at least need 3 physics layer because i think modules side by side would return a collision==true;

[quote="carnalis"]

Hi,
Scene::GetChildren() is one way.
Here is a quick and dirty recursive print method, copypasta untested, Using Urho head revision... should not be too different for 1.5.
[url=http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_scene.html]Scene[/url] is a type of Node, so this works with both types.

[spoiler][code]
decl:
void PrintTree(Urho3D::Node* node, unsigned level = 0);

void SceneManager::PrintTree(Node* node, unsigned level /* = 0 */) {
  // if you do not like spam
  // if (node->HasComponent<TerrainPatch>()) return;

  String s('+', level); // indentation
  s += "<" + node->GetName() + ">" + " pos:" + String(node->GetPosition());

  URHO3D_LOGRAW(s + '\n'); // opt. URHO3D_LOGINFO etc.

  if (!node->GetChildren().Empty()) {
    const Vector<SharedPtr<Node>> children(node->GetChildren()); // pre-C++11 needs a space: <SharedPtr<Node> >
    for (unsigned i = 0; i < children.Size(); ++i) {
      PrintTree(children[i], level + 1);
    }
  }
}
[/code][/spoiler][/quote]
ah ok, so you can make a vector of children and incremente until your pointer is* empty when you get them from the scene. thx, that's good to know. (edit: i reread and the node method too is good to know ^^)
*edit 2 ><

i go do some tries, i also need to check the physic demo to see what #include i need, etc...

-------------------------

noals | 2017-01-02 01:12:18 UTC | #8

another question, is it possible to change the color of the collision layer when i render it ? how should i do ?
in the physic example, you can use the SPACE key to see the physic stuff so i put different layers for the first module and the others module but i can't see the difference when rendering.

[url=http://www.hostingpics.net/viewer.php?id=646635physicstuff.png][img]http://img15.hostingpics.net/pics/646635physicstuff.png[/img][/url]

-------------------------

Nerrik | 2017-01-02 01:12:18 UTC | #9

[quote]i didn't do a character yet but i know i will at least need 3 physics layer because i think modules side by side would return a collision==true;[/quote]

there is also an NodeCollisionEnd event, to handle double collisions if you mean that. (with an "lastcollision" array or something like this).

-------------------------

noals | 2017-01-02 01:12:18 UTC | #10

i saw that in the doc : [url]http://urho3d.github.io/documentation/1.5/_event_list.html[/url]
[quote]
NodeCollisionEnd

    Body : RigidBody pointer
    OtherNode : Node pointer
    OtherBody : RigidBody pointer
    Trigger : bool

[/quote]

so if the two RigidBody are side by side, i can define them as "false" so they will not be seen as colliding ?
yes i would need that, thx.
but how do i use it ?
[quote](with an "lastcollision" array or something like this)[/quote] ?
i'm lost already lol.


i put the m_Body on the same layer and i will try that tomorrow :
[code]        c_light=scene->CreateChild("collision_light");
        c_light->SetPosition(Vector3(position.x_, position.y_+1, position.z_));
        {
            Light* Elight=e_light->CreateComponent<Light>();
            Elight->SetLightType(LIGHT_POINT);
            Elight->SetRange(2);

            if(m_Body->GetCollidingBodies() != 0)  //or NULL ?
            {
                //there is a collision with another module : do something.
                Elight->SetBrightness(2.0);
                Elight->SetColor(Color(1.0,0.5,0.1,1.0));
            }
            else
            {
                //there is no collision, the module can stay here.
                Elight->SetBrightness(2.0);
                Elight->SetColor(Color(.0,.0,1.0,1.0));
            }
        }[/code]
i should see an orange or a blue light if it work at all.

-------------------------

noals | 2017-01-02 01:12:20 UTC | #11

ok, i just understood that i need to check the somethingEvents.h in the source with the [url=http://urho3d.github.io/documentation/1.5/_event_list.html]documentation[/url] to see what's going on but it's still confusing to me.
[code]
SubscribeToEvent(mynode, E_NODECOLLISION, HANDLER(objectevents, HandleObjectCollision)); //for every node that should trigger something on collision

void objectevents::HandleObjectCollision(StringHash eventT, VariantMap& eData)
{
RigidBody* body = static_cast<RigidBody*>(eData[P_BODY].GetPtr());[/code]

[b]mynode[/b] ? why are you able to put it in the [b]SubscribeToEvent()[/b] ?
can i name [b]HandleObjectCollision[/b] as i want ?
and so, [b]eData[P_BODY].GetPtr()[/b] point to what excatly ?

-------------------------

Nerrik | 2017-06-29 08:05:29 UTC | #12

[quote="noals"]
ok, i just understood that i need to check the somethingEvents.h in the source with the [url=http://urho3d.github.io/documentation/1.5/_event_list.html]documentation[/url] to see what's going on but it's still confusing to me.
```
SubscribeToEvent(mynode, E_NODECOLLISION, HANDLER(objectevents, HandleObjectCollision)); //for every node that should trigger something on collision

void objectevents::HandleObjectCollision(StringHash eventT, VariantMap& eData)
{
RigidBody* body = static_cast<RigidBody*>(eData[P_BODY].GetPtr());
```

[b]mynode[/b] ? why are you able to put it in the [b]SubscribeToEvent()[/b] ?
can i name [b]HandleObjectCollision[/b] as i want ?
and so, [b]eData[P_BODY].GetPtr()[/b] point to what excatly ?
[/quote]

first of all, there was some 1.5 changes:

[code]SubscribeToEvent(mynode, E_NODECOLLISION, HANDLER(objectevents, HandleObjectCollision)); [/code]

should be written:

[code]SubscribeToEvent(mynode, E_NODECOLLISION, URHO3D_HANDLER(objectevents, HandleObjectCollision));[/code]


[b]mynode[/b] ? why are you able to put it in the [b]SubscribeToEvent()[/b] ?

if it has a RigidBody and a CollisionShape, you'll can set this event on every node you want.

can i name [b]HandleObjectCollision[/b] as i want ?
yes (Also different notes to different functions)

and so, [b]eData[P_BODY].GetPtr()[/b] point to what excatly ?

to the RigidBody of the collision target. (node rbody that get colluded by something)

-------------------------

Nerrik | 2017-01-02 01:12:20 UTC | #13

[code]
URHO3D_EVENT(E_NODECOLLISION, NodeCollision)
{
    URHO3D_PARAM(P_BODY, Body);                    // RigidBody pointer
    URHO3D_PARAM(P_OTHERNODE, OtherNode);          // Node pointer
    URHO3D_PARAM(P_OTHERBODY, OtherBody);          // RigidBody pointer
    URHO3D_PARAM(P_TRIGGER, Trigger);              // bool
    URHO3D_PARAM(P_CONTACTS, Contacts);            // Buffer containing position (Vector3), normal (Vector3), distance (float), impulse (float) for each contact
}
[/code]

-------------------------

jmiller | 2017-06-29 08:05:51 UTC | #14

[quote="noals"]
```
SubscribeToEvent(mynode, E_NODECOLLISION, HANDLER(objectevents, HandleObjectCollision)); //for every node that should trigger something on collision
```
[b]mynode[/b] ? why are you able to put it in the [b]SubscribeToEvent()[/b] ?
[/quote]

[url=http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_object.html#ac9ea95ee6f24e7fbeede16ba149dbc2d]This class method[/url] is described in the docs, events subsection [b]Sending events through another object[/b]
[urho3d.github.io/documentation/H ... therObject](http://urho3d.github.io/documentation/HEAD/_events.html#Events_AnotherObject)
[urho3d.github.io/documentation/1 ... therObject](http://urho3d.github.io/documentation/1.5/_events.html#Events_AnotherObject) (1.5 - same)

I think that section could be clearer by giving an example of the method.

-------------------------

noals | 2017-01-02 01:12:22 UTC | #15

this [code]SubscribeToEvent(mynode, E_NODECOLLISION, HANDLER(objectevents, HandleObjectCollision))
[/code]
is actually : [code]SubscribeToEvent(mynode, P_BODY, P_OTHERNODE, P_OTHERBODY, P_TRIGGER, P_CONTACTS, HANDLER(objectevents, HandleObjectCollision))[/code]
and im starting to get the idea but i will need to test things up anyway. 

[quote]This class method is described in the docs, events subsection Sending events through another object[/quote]
yes, that's what i meant. i wasn't able to find it in the doc at this time, thx.
i though we were able to put whatever we wanted in the function somehow.

yeah an exemple would be nice through i will still try the other thing again later as well
[quote]GetCollidingBodies (PODVector< RigidBody * > &result) const[/quote]

i'm rethinking my whole code now, i need a better organisation.

-------------------------

Nerrik | 2017-06-29 08:08:33 UTC | #16

come home from a party and iam drunk, but have extended the 11_Physics (1.5) sample a little bit...just search for "//itsnew" replace the code and watch in to the log (F1)

[details=11_Physics.h ]
```
//
// Copyright (c) 2008-2015 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

#pragma once

#include "Sample.h"

namespace Urho3D
{

class Node;
class Scene;

}
    using namespace NodeCollision; //itsnew
/// Physics example.
/// This sample demonstrates:
///     - Creating both static and moving physics objects to a scene
///     - Displaying physics debug geometry
///     - Using the Skybox component for setting up an unmoving sky
///     - Saving a scene to a file and loading it to restore a previous state
class Physics : public Sample
{
    URHO3D_OBJECT(Physics, Sample);

public:
    /// Construct.
    Physics(Context* context);

    /// Setup after engine initialization and before running the main loop.
    virtual void Start();

protected:
    /// Return XML patch instructions for screen joystick layout for a specific sample app, if any.
    virtual String GetScreenJoystickPatchString() const { return
        "<patch>"
        "    <remove sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/attribute[@name='Is Visible']\" />"
        "    <replace sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Spawn</replace>"
        "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]\">"
        "        <element type=\"Text\">"
        "            <attribute name=\"Name\" value=\"MouseButtonBinding\" />"
        "            <attribute name=\"Text\" value=\"LEFT\" />"
        "        </element>"
        "    </add>"
        "    <remove sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/attribute[@name='Is Visible']\" />"
        "    <replace sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Debug</replace>"
        "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]\">"
        "        <element type=\"Text\">"
        "            <attribute name=\"Name\" value=\"KeyBinding\" />"
        "            <attribute name=\"Text\" value=\"SPACE\" />"
        "        </element>"
        "    </add>"
        "</patch>";
    }

private:
    /// Construct the scene content.
    void CreateScene();
    /// Construct an instruction text to the UI.
    void CreateInstructions();
    /// Set up a viewport for displaying the scene.
    void SetupViewport();
    /// Subscribe to application-wide logic update and post-render update events.
    void SubscribeToEvents();
    /// Read input and moves the camera.
    void MoveCamera(float timeStep);
    /// Spawn a physics object from the camera position.
    void SpawnObject();
    /// Handle the logic update event.
    void HandleUpdate(StringHash eventType, VariantMap& eventData);
    /// Handle the post-render update event.
    void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData);
    void HandleObjectCollision(StringHash eventType, VariantMap& eventData); //itsnew
    /// Flag for drawing debug geometry.
    bool drawDebug_;
};
```
[/details]

[details=11_Physics.cpp]
```
//
// Copyright (c) 2008-2015 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/DebugRenderer.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/Light.h>
#include <Urho3D/Graphics/Material.h>
#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Graphics/Octree.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Graphics/Skybox.h>
#include <Urho3D/Graphics/Zone.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/IO/File.h>
#include <Urho3D/IO/FileSystem.h>
#include <Urho3D/Physics/CollisionShape.h>
#include <Urho3D/Physics/PhysicsWorld.h>
#include <Urho3D/Physics/RigidBody.h>
#include <Urho3D/Physics/PhysicsEvents.h> //itsnew
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/IO/Log.h> //itsnew
#include "Physics.h"

#include <Urho3D/DebugNew.h>

URHO3D_DEFINE_APPLICATION_MAIN(Physics)


Physics::Physics(Context* context) :
    Sample(context),
    drawDebug_(false)
{
}

void Physics::Start()
{
    // Execute base class startup
    Sample::Start();

    // Create the scene content
    CreateScene();

    // Create the UI content
    CreateInstructions();

    // Setup the viewport for displaying the scene
    SetupViewport();

    // Hook up to the frame update and render post-update events
    SubscribeToEvents();
}

void Physics::CreateScene()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();

    scene_ = new Scene(context_);

    // Create octree, use default volume (-1000, -1000, -1000) to (1000, 1000, 1000)
    // Create a physics simulation world with default parameters, which will update at 60fps. Like the Octree must
    // exist before creating drawable components, the PhysicsWorld must exist before creating physics components.
    // Finally, create a DebugRenderer component so that we can draw physics debug geometry
    scene_->CreateComponent<Octree>();
    scene_->CreateComponent<PhysicsWorld>();
    scene_->CreateComponent<DebugRenderer>();

    // Create a Zone component for ambient lighting & fog control
    Node* zoneNode = scene_->CreateChild("Zone");
    Zone* zone = zoneNode->CreateComponent<Zone>();
    zone->SetBoundingBox(BoundingBox(-1000.0f, 1000.0f));
    zone->SetAmbientColor(Color(0.15f, 0.15f, 0.15f));
    zone->SetFogColor(Color(1.0f, 1.0f, 1.0f));
    zone->SetFogStart(300.0f);
    zone->SetFogEnd(500.0f);

    // Create a directional light to the world. Enable cascaded shadows on it
    Node* lightNode = scene_->CreateChild("DirectionalLight");
    lightNode->SetDirection(Vector3(0.6f, -1.0f, 0.8f));
    Light* light = lightNode->CreateComponent<Light>();
    light->SetLightType(LIGHT_DIRECTIONAL);
    light->SetCastShadows(true);
    light->SetShadowBias(BiasParameters(0.00025f, 0.5f));
    // Set cascade splits at 10, 50 and 200 world units, fade shadows out at 80% of maximum shadow distance
    light->SetShadowCascade(CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f));

    // Create skybox. The Skybox component is used like StaticModel, but it will be always located at the camera, giving the
    // illusion of the box planes being far away. Use just the ordinary Box model and a suitable material, whose shader will
    // generate the necessary 3D texture coordinates for cube mapping
    Node* skyNode = scene_->CreateChild("Sky");
    skyNode->SetScale(500.0f); // The scale actually does not matter
    Skybox* skybox = skyNode->CreateComponent<Skybox>();
    skybox->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
    skybox->SetMaterial(cache->GetResource<Material>("Materials/Skybox.xml"));

    {
        // Create a floor object, 1000 x 1000 world units. Adjust position so that the ground is at zero Y
        Node* floorNode = scene_->CreateChild("Floor");
        floorNode->SetPosition(Vector3(0.0f, -0.5f, 0.0f));
        floorNode->SetScale(Vector3(1000.0f, 1.0f, 1000.0f));
        StaticModel* floorObject = floorNode->CreateComponent<StaticModel>();
        floorObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
        floorObject->SetMaterial(cache->GetResource<Material>("Materials/StoneTiled.xml"));

        // Make the floor physical by adding RigidBody and CollisionShape components. The RigidBody's default
        // parameters make the object static (zero mass.) Note that a CollisionShape by itself will not participate
        // in the physics simulation
        /*RigidBody* body = */floorNode->CreateComponent<RigidBody>();
        CollisionShape* shape = floorNode->CreateComponent<CollisionShape>();
        // Set a box shape of size 1 x 1 x 1 for collision. The shape will be scaled with the scene node scale, so the
        // rendering and physics representation sizes should match (the box model is also 1 x 1 x 1.)
        shape->SetBox(Vector3::ONE);
    }

    {
        // Create a pyramid of movable physics objects
        for (int y = 0; y < 8; ++y)
        {
            for (int x = -y; x <= y; ++x)
            {
                int z=0;
                String MyBoxname = "x:" + (String)float(x) + ", y:" + (String)-(float(y + 8.0f))+", z:" + (String)float(z); //itsnew - generate a unique name (starting position)
                Node* boxNode = scene_->CreateChild(MyBoxname); //itsnew
                boxNode->SetPosition(Vector3((float)x, -(float)y + 8.0f, 0.0f));
                StaticModel* boxObject = boxNode->CreateComponent<StaticModel>();
                boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
                boxObject->SetMaterial(cache->GetResource<Material>("Materials/StoneEnvMapSmall.xml"));
                boxObject->SetCastShadows(true);

                // Create RigidBody and CollisionShape components like above. Give the RigidBody mass to make it movable
                // and also adjust friction. The actual mass is not important; only the mass ratios between colliding
                // objects are significant
                RigidBody* body = boxNode->CreateComponent<RigidBody>();
                body->SetMass(1.0f);
                body->SetFriction(0.75f);
                CollisionShape* shape = boxNode->CreateComponent<CollisionShape>();
                shape->SetBox(Vector3::ONE);
                SubscribeToEvent(boxNode, E_NODECOLLISION, URHO3D_HANDLER(Physics, HandleObjectCollision)); //itsnew
            }
        }
    }

    // Create the camera. Set far clip to match the fog. Note: now we actually create the camera node outside the scene, because
    // we want it to be unaffected by scene load / save
    cameraNode_ = new Node(context_);
    Camera* camera = cameraNode_->CreateComponent<Camera>();
    camera->SetFarClip(500.0f);

    // Set an initial position for the camera scene node above the floor
    cameraNode_->SetPosition(Vector3(0.0f, 5.0f, -20.0f));
}

void Physics::CreateInstructions()
{

    ResourceCache* cache = GetSubsystem<ResourceCache>();
    UI* ui = GetSubsystem<UI>();

    // Construct new Text object, set string to display and font to use
    Text* instructionText = ui->GetRoot()->CreateChild<Text>();
    instructionText->SetText(
        "Use WASD keys and mouse/touch to move\n"
        "LMB to spawn physics objects\n"
        "F5 to save scene, F7 to load\n"
        "Space to toggle physics debug geometry"
    );
    instructionText->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 15);
    // The text has multiple rows. Center them in relation to each other
    instructionText->SetTextAlignment(HA_CENTER);

    // Position the text relative to the screen center
    instructionText->SetHorizontalAlignment(HA_CENTER);
    instructionText->SetVerticalAlignment(VA_CENTER);
    instructionText->SetPosition(0, ui->GetRoot()->GetHeight() / 4);
}

void Physics::SetupViewport()
{
    Renderer* renderer = GetSubsystem<Renderer>();

    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);
}

void Physics::SubscribeToEvents()
{
    // Subscribe HandleUpdate() function for processing update events
    SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(Physics, HandleUpdate));

    // Subscribe HandlePostRenderUpdate() function for processing the post-render update event, during which we request
    // debug geometry
    SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(Physics, HandlePostRenderUpdate));
}

void Physics::MoveCamera(float timeStep)
{
    // Do not move if the UI has a focused element (the console)
    if (GetSubsystem<UI>()->GetFocusElement())
        return;

    Input* input = GetSubsystem<Input>();

    // Movement speed as world units per second
    const float MOVE_SPEED = 20.0f;
    // Mouse sensitivity as degrees per pixel
    const float MOUSE_SENSITIVITY = 0.1f;

    // Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
    IntVector2 mouseMove = input->GetMouseMove();
    yaw_ += MOUSE_SENSITIVITY * mouseMove.x_;
    pitch_ += MOUSE_SENSITIVITY * mouseMove.y_;
    pitch_ = Clamp(pitch_, -90.0f, 90.0f);

    // Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
    cameraNode_->SetRotation(Quaternion(pitch_, yaw_, 0.0f));

    // Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
    if (input->GetKeyDown('W'))
        cameraNode_->Translate(Vector3::FORWARD * MOVE_SPEED * timeStep);
    if (input->GetKeyDown('S'))
        cameraNode_->Translate(Vector3::BACK * MOVE_SPEED * timeStep);
    if (input->GetKeyDown('A'))
        cameraNode_->Translate(Vector3::LEFT * MOVE_SPEED * timeStep);
    if (input->GetKeyDown('D'))
        cameraNode_->Translate(Vector3::RIGHT * MOVE_SPEED * timeStep);

    // "Shoot" a physics object with left mousebutton
    if (input->GetMouseButtonPress(MOUSEB_LEFT))
        SpawnObject();

    // Check for loading/saving the scene. Save the scene to the file Data/Scenes/Physics.xml relative to the executable
    // directory
    if (input->GetKeyPress(KEY_F5))
    {
        File saveFile(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Scenes/Physics.xml", FILE_WRITE);
        scene_->SaveXML(saveFile);
    }
    if (input->GetKeyPress(KEY_F7))
    {
        File loadFile(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Scenes/Physics.xml", FILE_READ);
        scene_->LoadXML(loadFile);
    }

    // Toggle physics debug geometry with space
    if (input->GetKeyPress(KEY_SPACE))
        drawDebug_ = !drawDebug_;
}

void Physics::SpawnObject()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();

    // Create a smaller box at camera position
    Node* boxNode = scene_->CreateChild("SmallBox");
    boxNode->SetPosition(cameraNode_->GetPosition());
    boxNode->SetRotation(cameraNode_->GetRotation());
    boxNode->SetScale(0.25f);
    StaticModel* boxObject = boxNode->CreateComponent<StaticModel>();
    boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
    boxObject->SetMaterial(cache->GetResource<Material>("Materials/StoneEnvMapSmall.xml"));
    boxObject->SetCastShadows(true);

    // Create physics components, use a smaller mass also
    RigidBody* body = boxNode->CreateComponent<RigidBody>();
    body->SetMass(0.25f);
    body->SetFriction(0.75f);
    CollisionShape* shape = boxNode->CreateComponent<CollisionShape>();
    shape->SetBox(Vector3::ONE);

    const float OBJECT_VELOCITY = 10.0f;

    // Set initial velocity for the RigidBody based on camera forward vector. Add also a slight up component
    // to overcome gravity better
    body->SetLinearVelocity(cameraNode_->GetRotation() * Vector3(0.0f, 0.25f, 1.0f) * OBJECT_VELOCITY);
}

void Physics::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    using namespace Update;

    // Take the frame time step, which is stored as a float
    float timeStep = eventData[P_TIMESTEP].GetFloat();

    // Move the camera, scale movement with time step
    MoveCamera(timeStep);
}

void Physics::HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
    // If draw debug mode is enabled, draw physics debug geometry. Use depth test to make the result easier to interpret
    if (drawDebug_)
        scene_->GetComponent<PhysicsWorld>()->DrawDebugGeometry(true);
}


//itsnew all now.......


void Physics::HandleObjectCollision(StringHash eventT, VariantMap& eData)
{

RigidBody* body = static_cast<RigidBody*>(eData[P_BODY].GetPtr());
Component* comp;
comp=body->GetComponent("StaticModel");
Node* myobject;
myobject=comp->GetNode ();
String nodename=myobject->GetName();


Node* otherNode = static_cast<Node*>(eData[P_OTHERNODE].GetPtr());
String othernodename=otherNode->GetName();

URHO3D_LOGRAW("\n nodename: " + nodename + " collude with: " + othernodename);


}
```
[/details]

its no rockedsience...

-------------------------

noals | 2017-01-02 01:12:32 UTC | #17

it took me some time but i rewrited my stuff and i tryed your method to see what it actually does but it doesn't seem to return anything at all.
i just got this message in the terminal :
[quote]warning btCollisionDispatcher::needsCollision: static-static collision!
[/quote]
i guess i need a static-static collision test but that don't help me much at this point.
what should i use ?

the code i tryed :
[code]
        SubscribeToEvent(E_NODECOLLISION, URHO3D_HANDLER(projet, HandleCollisionUpdate)); //collision test  

    void HandleCollisionUpdate(StringHash eventType, VariantMap& eventData)
    {

        RigidBody* body = static_cast<RigidBody*>(eventData[P_BODY].GetPtr());
        Component* comp;
        comp=body->GetComponent("AnimatedModel");
        Node* myobject;
        myobject=comp->GetNode ();
        String nodename=myobject->GetName();


        Node* otherNode = static_cast<Node*>(eventData[P_OTHERNODE].GetPtr());
        String othernodename=otherNode->GetName();

        URHO3D_LOGRAW("\n nodename: " + nodename + " collide with: " + othernodename);
    }
[/code]

[url=http://www.hostingpics.net/viewer.php?id=605187collisiontest.png][img]http://img15.hostingpics.net/pics/605187collisiontest.png[/img][/url]

-------------------------

Nerrik | 2017-01-02 01:12:32 UTC | #18

you dont give the SubscribeToEvent a node.
SubscribeToEvent(E_NODECOLLISION, URHO3D_HANDLER(projet, HandleCollisionUpdate)); //collision test  



but you have set this event to a specific node  that should send this event on a collision (with whatever)

nodes: [url]http://urho3d.github.io/documentation/1.3/class_urho3_d_1_1_node.html[/url]

SubscribeToEvent([b]boxNode[/b], E_NODECOLLISION, URHO3D_HANDLER(Physics, HandleObjectCollision)); //itsnew

this nodes also should have a rigidbody: [url]http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_rigid_body.html[/url]
and a collisionshape: [url]http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_collision_shape.html[/url]

AND

    void HandleCollisionUpdate(StringHash eventType, VariantMap& eventData)
 normaly it should be wirtten: 
    void YOURCLASSNAME::HandleCollisionUpdate(StringHash eventType, VariantMap& eventData)

so 

SubscribeToEvent([b]boxNode[/b], E_NODECOLLISION, URHO3D_HANDLER(YOURCLASSNAME, HandleObjectCollision)); //itsnew

can point to the right class and function(void)

-------------------------

noals | 2017-01-02 01:12:32 UTC | #19

ok, sorry if i'm annoying but be rassured that i am as much or even more annoyed than you could be.
this shit doesn't really make sense to me when trying to include it in my code so i will describe what i understand and what i don't plus my actual problem in hope you will can enlight me.

first of all, i have my urho3D main class that represent my project :
[code]
class projet : public Application
{
    URHO3D_OBJECT(projet, Application)
[/code]
and within the virtual void Start(), i have the SubscribeToEvent stuff including :
[code]
        SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(projet, HandleUpdate));
        SubscribeToEvent(E_POSTRENDERUPDATE,URHO3D_HANDLER(projet,HandlePostRenderUpdate));     
        SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(projet, HandleKeyDown));[/code]
so no problem here.

then, i have a "Dungeon" class in separates files that use  r_Rooms (for random rooms), r_Cors (for random corridors), r_Juncs (for random junctions) and Module classes to build the dungeon.
example, the first loaded module :
[code]
Dungeon::Dungeon(int MODULE_MAX, Scene* scene, ResourceCache* cache)
{
   MODULE_COUNT = 0;
   roomJuncSwitch = 0;

   while(MODULE_COUNT<MODULE_MAX)
   {
       if(mainExitList.size()==0)
       {
            room_p = new r_Rooms(); //i start with a room
            module_p = new Module(MODULE_COUNT, room_p->type, room_p->std_name, 
                                  room_p->exits, room_p->path, room_p->texturepath,
                                  scene, cache);
            
            for(int x=0;x<module_p->exitList.size();x++)
            {
                mainExitList.push_back(module_p->exitList[x]);
            }       

            temp_Body = module_p->m_Body;  
            MODULE_COUNT++;
        }
        else
        {
[/code]
each module object have its Node, AnimatedModel, RigidBody and CollisionShape that i can access with the pointer [b]module_p->[/b] and that should be this node that is collision tested for each loaded module..
so i need to put the subscribeToEvent stuff within my class i guess but that's where i don't really get it.

if i want to make a fonction within my class, first i declare it as a public member :
[code]void testCollision(Node* whatever);[/code]
and then, in the .cpp, i can define what the function does :
[code]
void Dungeon::testCollision(Node* whatever)
{
    collisionTest(whatever);
}[/code]

but here, i guess i should have something like this in my class.h public member :
[code]SubscribeToEvent(Node* m_Node, E_NODECOLLISION, URHO3D_HANDLER(projet, HandleObjectCollision));[/code]
but i also guess it won't work if it isn't define in the projet class so i'm not sure how to use it
and for the function :
[code]void Dungeon(?)::HandleCollisionUpdate(StringHash eventType, VariantMap& eventData)
    {

        RigidBody* body = static_cast<RigidBody*>(eventData[P_BODY].GetPtr());
        Component* comp;
        comp=body->GetComponent("AnimatedModel");
        Node* myobject;
        myobject=comp->GetNode ();
        String nodename=myobject->GetName();[/code]
i guess i have to put it in my class.cpp somehow but since it's a function definition, can i put it in the constructor of my class ?
anyway, i kinda understand a few things but with this method i'm lost, i don't know where to put what because i don't need it in the main.cpp and the way the function is defined just confuse me.

you have the main.cpp,  the class.h and the class.cpp.    what do you write in each stuff for an event to work ?

-------------------------

Dave82 | 2017-01-02 01:12:32 UTC | #20

Thats because you doing it wrong.Are you trying to make a wrapper or i can't really understand what are you trying to do ? :confused: 

You don't have SubscribeToEvent in your class because its not derived from Urho3D::Object... Here are few advices :

Get rid of these Module , Dungeon and other classes you try to implement.You don't need them. Urho doesn't work this way. Follow the rules that the developers provided.In this case Component based programming.
Instead of creating a Dungeon and other external classes , you should use Urho3d::Node and add your collision body , AnimatedModel etc components to it. Define a Corridor , and Dungeon components derived from Urho3D::LogicComponent. Now you have a valid Urho Object that can properly subscribed to events , collision checks and network updates.

-------------------------

noals | 2017-01-02 01:12:32 UTC | #21

i use nodes and pointers, in my module class :

[b].h[/b]
[code]
class Module
{
    public:
    Node* m_Node;
    AnimatedModel* m_Object;
    RigidBody* m_Body;
    CollisionShape* m_BBox;
    Node* light;    

    ExitList exitList;

    Module (int m_COUNT, 
            int type, std::string std_name, int exits, String path, String texturepath,
            Scene* scene, ResourceCache* cache);
            
    private:
};
[/code]

[b].cpp[/b]
[code]
Module::Module(int m_COUNT, 
               int type, std::string std_name, int exits, String path, String texturepath, 
               Scene* scene, ResourceCache* cache)
{

    
    std::string std_sceneName = IntString(m_COUNT, std_name);
    String sceneName = string2urhoString(std_sceneName);
    //m_Node = new Node();
    m_Node = scene->CreateChild(sceneName);
    m_Node->SetWorldPosition(Vector3::ZERO);   //room.position          
    m_Node->SetWorldRotation(Quaternion::IDENTITY);   //room.rotation (1,0,0,0) 
    
    //m_Object = new AnimatedModel();    
    m_Object=m_Node->CreateComponent<AnimatedModel>();
    m_Object->SetModel(cache->GetResource<Model>(path));
    m_Object->SetMaterial(cache->GetResource<Material>(texturepath));
    
//add physic  
    //m_Body = new RigidBody();          
    m_Body = m_Node->CreateComponent<RigidBody>();
    m_Body->SetMass(0);  //0 for static object
    m_Body->SetFriction(0.6);        // friction with other objects (like the ground)
    m_Body->SetCollisionLayer(1);
//add collision shape
    //m_BBox = new CollisionShape();
    m_BBox = m_Node->CreateComponent<CollisionShape>();
    m_BBox->SetTriangleMesh(cache->GetResource<Model>(path));   

//etc....[/code]

the Module constructor use infos from the "rooms", "cors" and "juncs" that return infos from a .xml, like the "path" to load the model.
i simplified my code so it doesn't have X time the same function repeated again and again and i needed to separate the code this way because i needed a before rendering step and a while rendering step plus the differentiation of each module type "rooms", "cors", etc... so i can chose which one i want.

basicaly, what i had in mind after seeing the GetCollidingBody() function was to make a vector of RigidBody pointer from previously loaded module so i can compare the last loaded module rigidbody with the vector and return true or whatever if there is a collision, but already the GetCollidingBody() is a void function so i don't know how to use it either. i need to check the source to see what's going on i think.

few month ago, i wasn't able to initialize class members properly. now i kinda understand classes but i didn't learned about derived one yet.
i guess it's maybe the time to do that.

-------------------------

Dave82 | 2017-01-02 01:12:32 UTC | #22

Well i HIGHLY RECOMMEND to look up some c++ tutorials and books and practice few months before you jump into Urho3d... It is completely abstract and relies on polymorphism and other "design standards" that i don't think it could be understand by trial and error... Once again you don't need the Module and Corridor and other classes ! It's not that is unnecessary but it won't work ! It is absolutely against the whole c++ Urho Component based programming concept. Try it as  i suggested in my previous post.Use Nodes for Modules and create components for Corridors and other stuff... That's the ONLY way it will ever work.

If you using your own classes which are not derived form Urho3D::Object , it breaks the OOP rules of the engine.You can't access the Urho context from outside. 

But if i were you i would start reading/watching some c++ tutorials first because this way it will take ages to take a leap forward 
Regards

-------------------------

noals | 2017-01-02 01:12:32 UTC | #23

well, i ask for a collision test method and i get a whole framework.

you're telling me the whole urho3D concept is about object, component and the kind.
in the doc, there is only that kinda :
[url]http://urho3d.github.io/documentation/1.4/_object_types.html[/url]
and in the wiki as a "latest activity" :
[url]http://urho3d.wikia.com/wiki/Creating_your_own_C%2B%2B_components[/url]
those are not for beginner like me when i check some .cpp in the source as examples, can't i use bullet or something directly ?

there is no way to actually test if 2 RigidBody are colliding not having to write a whole urho3D object or whatever ?!  :angry:

-------------------------

noals | 2017-01-02 01:12:33 UTC | #24

i will try to use bullet directly with its library.

from urho i can get the bullet collision shape
[code]btCollisionShape * 	GetCollisionShape () const
 	Return Bullet collision shape. [/code]

with bullet, i can create a btCollisionObject and assign it the collision shape
[code]setCollisionShape (btCollisionShape *collisionShape)[/code]

then i should be able somehow to test the collision with contactTest() or contactPairTest() from bullet
what annoy me is that it seem i will still need to use simulation steps while it isn't really needed yet for my need but i will see how it goes anyway.

-------------------------

noals | 2017-01-02 01:12:34 UTC | #25

well...

i get a Program received signal SIGSEGV, Segmentation fault because of the second line :
[code]
    bt_BBox = m_BBox->GetCollisionShape();  //urho BBox to bullet BBox (collision shape)
    bt_CollisionObj->setCollisionShape(bt_BBox); //bullet collision object
[/code]

and i don't know what argument is needed to get a PhysicsWorld pointer
[code]
    PhysicsWorld* urhoPhysics = scene->GetComponent<PhysicsWorld>( ??? );
[/code]


how come physic in engines is never user friendly ?
and how come there is no understandable tutorial about urho custom objects and components while it seem to be the base of the engine ?



edit: bah, i guess i will just use bullet as it come and won't use urho3D physic at all. it will be simplier, i saw i can use .obj from blender to bullet so that should be ok.

-------------------------

Dave82 | 2017-01-02 01:12:34 UTC | #26

[quote]how come physic in engines is never user friendly ?
and how come there is no understandable tutorial about urho custom objects and components while it seem to be the base of the engine ?[/quote]

I never saw an engine where using Physics is easier than Urho.
Object oriented  and component based programming are [b]NOT[/b] Urho features but c++ and other OOP language features.You can't expect form anyone here to explain you the basics of c++.
The tutorials are extremely straightforward and explain the engine usage very well.

[quote]edit: bah, i guess i will just use bullet as it come and won't use urho3D physic at all. it will be simplier, i saw i can use .obj from blender to bullet so that should be ok.[/quote]
That's bad idea ! Don't use the engine's lower layer if you're not a experienced programmer.After few days your code will turn into an unreadable spagetti and no one can help you afterewards.

-------------------------

noals | 2017-01-02 01:12:34 UTC | #27

i would like to try as you say but i don't really know what i must do exaclty.

when i check [url=http://www.tutorialspoint.com/cplusplus/cpp_inheritance.htm]HERE[/url], it doesn't seem very hard to me to derive a class (and i kinda understand the custom component thing) but which class must i derive from ?
must i do some kind of Node, Component, LogicComponent, AnimatedModel ? i'm confused.

and then, that's when i derive the class that i must add the SubscribeToEvent ? i'm confused by the organisation/hierarchy of it all.

-------------------------

Nerrik | 2017-01-02 01:12:34 UTC | #28

you can look into the characterdemo(or other samples with more than one class) source how to implement a new class as a urho3d logiccomponent. In the characterdemo it is the "Character" class. 


[quote]and then, that's when i derive the class that i must add the SubscribeToEvent ? i'm confused by the organisation/hierarchy of it all.[/quote]

You dont have to subscribe your event into an diffrent class. You can do it in every class you want. (it only has to be a "urho3d class")

-------------------------

noals | 2017-01-02 01:12:34 UTC | #29

ok, now i kinda see what i must do but the how seems more difficult to me.
from what i understand, i should end up adding the logic component to my module node and so urho should do the collision check for me as long as i can define the component well.
example :
[code]m_Node -> CreateComponent<CollisionTester>();[/code]
or i could even do a new urho Object for my rooms, corridors, modules, ... but it seems even harder.

this is a new level of abstraction to me.
i'm puzzled by how things are initialized, i need to get into it and try things, i will surely have more questions about it later.

-------------------------

Nerrik | 2017-01-02 01:12:34 UTC | #30

[quote]from what i understand, i should end up adding the logic component to my module node and so urho should do the collision check for me as long as i can define the component well.[/quote]

thats right (if you call up the function with the SubscribeToEvent command from your CollisionTester class in the mainclass - one time)

-------------------------

TheComet | 2017-01-02 01:12:34 UTC | #31

[quote="noals"]i'm puzzled by how things are initialized, i need to get into it and try things, i will surely have more questions about it later.[/quote]

During start-up, all components that can be instantiated are registered to the context object. The best way to learn about this mechanism is by writing your own component. Example:

[code]class MyComponent : public Urho3D::Component {
public:
    MyComponent(Urho3D::Context* context) : Component(context) {}

    static void RegisterObject(Urho3D::Context* context)
    {
        context->RegisterFactory<MyComponent>("Custom Component");
    }
};[/code]

If you were to try and execute the following code without registering your component:
[code]node_ = CreateComponent<MyComponent>();[/code]

then Urho3D would not know how to create "MyComponent". It will return a default component that does nothing instead of instantiating MyComponent (or it might return NULL, I'm not sure any more).

You have to first register your component once:
[code]// Do this once
MyComponent::RegisterObject(context_);[/code]

And now CreateComponent<MyComponent>(); will do what you expect it to do.

You can look in Object.h:241 to see how it is implemented.

-------------------------

noals | 2017-01-02 01:12:35 UTC | #32

i have a little question.

i use the Ragdolls sample as example.
in the CreateRagdoll.cpp:115, there is that :
[code]void CreateRagdoll::CreateRagdollBone(const String& boneName, ShapeType type, const Vector3& size, const Vector3& position,
    const Quaternion& rotation)
{
    // Find the correct child scene node recursively
    Node* boneNode = node_->GetChild(boneName, true);[/code]
[b]node_[/b] is actually the node on which the ragdoll is created right ?
the same node the custom component is assigned to with :
[code]protected:
    /// Handle node being assigned.
    virtual void OnNodeSet(Node* node);[/code]

i guess it is that but since i don't see it being initialized, i wonder where it come from.
this [b]node_[/b] is a member of what originally ?

-------------------------

cadaver | 2017-01-02 01:12:35 UTC | #33

It's a member of the Component base class, and has been initialized when the component was created to the node.

-------------------------

noals | 2017-01-02 01:12:36 UTC | #34

[quote="cadaver"]It's a member of the Component base class, and has been initialized when the component was created to the node.[/quote]
[code]
    /// Scene node.
    Node* node_;
    /// Unique ID within the scene.
    unsigned id_;
    /// Network update queued flag.
    bool networkUpdate_;
    /// Enabled flag.
    bool enabled_;
[/code]

thx, that's great.

-------------------------

noals | 2017-01-02 01:12:38 UTC | #35

the dumb question of the day.

i initialized my component like that :
[code]
        Node* m_Node = my_scene->CreateChild("Test");
        m_Node->CreateComponent<Module>();
[/code]

but then, how do i use component's functions that are public member ?
can i make a pointer of a component or something ?

-------------------------

cadaver | 2017-01-02 01:12:38 UTC | #36

To retrieve a component for calling its functions, it's easiest to use the template overload of GetComponent:

[code]
Module* module = m_Node->GetComponent<Module>();
module->MyFunction();
[/code]

-------------------------

noals | 2017-01-02 01:12:38 UTC | #37

ok thx.

-------------------------

noals | 2017-01-02 01:12:38 UTC | #38

well, i'm at the same point.
[quote]warning btCollisionDispatcher::needsCollision: static-static collision![/quote]
why shouldn't i be able to do some static-static collision check ? did i miss something ?
[code]
//add physic         
    RigidBody* m_Body = node_->CreateComponent<RigidBody>();
    m_Body->SetMass(0);  //0 for static object
[/code]


my component is made like that :

CreateModule.h
[code]
#pragma once

#include <Urho3D/Physics/CollisionShape.h>
#include "ModuleInfos.h"

using namespace Urho3D;

/// Custom component (that creates a ragdoll upon collision.)
class Module : public Component
{
    URHO3D_OBJECT(Module, Component);
    
public:
    /// Construct.
    Module(Context* context);

    //ExitList exitList;
	
    void createRoom(Scene* scene, ResourceCache* cache);
    void createCor(Scene* scene, ResourceCache* cache);
    void createJunc(Scene* scene, ResourceCache* cache);

	
    
protected:
    /// Handle node being assigned.
    virtual void OnNodeSet(Node* node);
    
private:
    /// Handle scene node's physics collision.
    void OnCollisionEvent(StringHash eventType, VariantMap& eventData);
    

//to load different modules type infos
    r_Rooms* room_p;
    r_Cors* cor_p;
    r_Juncs* junc_p;
};
[/code]

CreateModule.cpp
[code]

#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/Graphics/Graphics.h>

#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Math/Vector3.h>
#include <Urho3D/Math/Quaternion.h>
#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Graphics/AnimatedModel.h>
#include <Urho3D/Graphics/Material.h>
#include <string>
#include <vector>

#include "fonctions.h"
#include "conversions.h"
#include "Counts.h"
#include "Exit.h"

#include "tinyxml2.h"
#include <Urho3D/IO/Log.h>
#include <Urho3D/DebugNew.h>

//physic
#include <Urho3D/Physics/CollisionShape.h>
//#include <Urho3D/Physics/PhysicsWorld.h>
#include <Urho3D/Physics/RigidBody.h>
#include <Urho3D/Physics/PhysicsEvents.h>


#include "CreateModule.h"
#include "ModuleInfos.h"


using namespace Urho3D;



Module::Module(Context* context) :
    Component(context)
{
}

void Module::createRoom(Scene* scene, ResourceCache* cache)
{
    room_p = new r_Rooms();
	
    std::string std_sceneName = IntString(id_, room_p->std_name);
    String sceneName = string2urhoString(std_sceneName);

    node_ = scene->CreateChild(sceneName);
    node_->SetWorldPosition(Vector3::ZERO);   //room.position          
    node_->SetWorldRotation(Quaternion::IDENTITY);   //room.rotation (1,0,0,0) 
    
    //m_Object = new AnimatedModel();    
    AnimatedModel* m_Object = node_->CreateComponent<AnimatedModel>();
    m_Object->SetModel(cache->GetResource<Model>(room_p->path));
    m_Object->SetMaterial(cache->GetResource<Material>(room_p->texturepath));
    
//add physic          
    RigidBody* m_Body = node_->CreateComponent<RigidBody>();
    m_Body->SetMass(0);  //0 for static object
    m_Body->SetFriction(0.6);        // friction with other objects (like the ground)
    m_Body->SetCollisionLayer(1);
//add collision shape
    CollisionShape* m_BBox = node_->CreateComponent<CollisionShape>();
    m_BBox->SetTriangleMesh(cache->GetResource<Model>(room_p->path));


//add light
    Node* light=node_->CreateChild("m_light");
    light->SetPosition(Vector3(0, 5, 0));
    {
        Light* Mlight=light->CreateComponent<Light>();
        Mlight->SetLightType(LIGHT_POINT);
        Mlight->SetRange(20);
        Mlight->SetBrightness(1.0);
        Mlight->SetColor(Color(.8,.8,.8,1.0));
    }

}

void Module::createCor(Scene* scene, ResourceCache* cache)
{
   //same thing...
}

void Module::createJunc(Scene* scene, ResourceCache* cache)
{
   //same thing...
}

//protected
void Module::OnNodeSet(Node* node)
{
    // If the node pointer is non-null, this component has been created into a scene node. Subscribe to physics collisions that concern this scene node
    if (node)
    {
        SubscribeToEvent(node, E_NODECOLLISION, URHO3D_HANDLER(Module, OnCollisionEvent)); 
    }
}

//private
void Module::OnCollisionEvent(StringHash eventType, VariantMap& eventData)
{
    using namespace NodeCollision;

    // Get the other colliding body
    RigidBody* otherBody = static_cast<RigidBody*>(eventData[P_OTHERBODY].GetPtr());

    if (otherBody)
    {

        URHO3D_LOGINFO("collide"); 

        // Finally remove self from the scene node. Note that this must be the last operation performed in the function
        //Remove();  ??
    }
}
[/code]

-------------------------

Lumak | 2017-01-02 01:12:39 UTC | #39

[quote="noals"]well, i'm at the same point.
[quote]warning btCollisionDispatcher::needsCollision: static-static collision![/quote]
why shouldn't i be able to do some static-static collision check ? did i miss something ?
[/quote]

There shouldn't be a static-static collision check in Bullet, as you don't expect static geometries to move.  That is the point of static objects.

If you're trying to place objects randomly in the scene, what I'd suggest is that you set the mass of > 0 so you can get a collision call back and rely on dynamic-static collision callback.  And once it's placed properly in the world [b]then[/b] set the mass back to 0.

-------------------------

noals | 2017-01-02 01:12:39 UTC | #40

i think i misunderstood the warning message :
[quote]warning btCollisionDispatcher::needsCollision: static-static collision![/quote]

i fast checked the bullet forum and it seems that the collision actually happen and bullet just warn me that it is a collision between 2 static models. (and that's what i want here)

but if the collision happens, then i don't understand urho3D again because this part of code don't do what i expect it to do :

[code]

void Module::OnCollisionEvent(StringHash eventType, VariantMap& eventData)
{
    using namespace NodeCollision;

    // Get the other colliding body
    RigidBody* otherBody = static_cast<RigidBody*>(eventData[P_OTHERBODY].GetPtr());

    if (otherBody)
    {
        URHO3D_LOGINFO("collide");
    }
}
[/code]

it doesn't show "collide" in my log.

-------------------------

noals | 2017-01-02 01:12:39 UTC | #41

[quote="Lumak"][quote="noals"]well, i'm at the same point.
[quote]warning btCollisionDispatcher::needsCollision: static-static collision![/quote]
why shouldn't i be able to do some static-static collision check ? did i miss something ?
[/quote]

There shouldn't be a static-static collision check in Bullet, as you don't expect static geometries to move.  That is the point of static objects.

If you're trying to place objects randomly in the scene, what I'd suggest is that you set the mass of > 0 so you can get a collision call back and rely on dynamic-static collision callback.  And once it's placed properly in the world [b]then[/b] set the mass back to 0.[/quote]

we posted at the same time. ^^;

i though about this solution while thinking about my problem but you're right,  i don't want my module to move. i will check about call back, i'm not familiar with this either.

-------------------------

Lumak | 2017-01-02 01:12:39 UTC | #42

The warning:
			printf("warning btCollisionDispatcher::needsCollision: static-static collision!\n");


is reported in bullet's code, specifiacally in: 
                    bool	btCollisionDispatcher::needsCollision(const btCollisionObject* body0,const btCollisionObject* body1) - in btCollisionDispatcher.cpp

And because of it, it never reports back to Urho.  There are two choices to your solution: 1) write static-static collision dispatcher as complained in btCollisionDispatcher.cpp 2) temporarily assign some mass to a placing object.

-------------------------

Lumak | 2017-01-02 01:12:39 UTC | #43

Ha, you posted your conclusion as I was typing another response.

I think you're on the right track now. good luck!

-------------------------

noals | 2017-01-02 01:12:39 UTC | #44

still doesn't work, dunno what's wrong with my code.
this doesn't do anything :
[code]
void Module::OnCollisionEvent(StringHash eventType, VariantMap& eventData)
{
    using namespace NodeCollision;
    RigidBody* otherBody = static_cast<RigidBody*>(eventData[P_OTHERBODY].GetPtr());

    if (otherBody->GetMass() > 0.0f)
    {
        URHO3D_LOGINFO("collide");
        Light* light;
        light = node_->GetComponent<Light>();
        light->SetColor(Color(.8,.4,.4,1.0));
    }
}
[/code]

and i set my RigidBody like that so my modules are non-static but they don't move either.
[code]
    m_Body->SetMass(1);  //0 for static object
	m_Body->SetUseGravity(false);
	m_Body->SetTrigger(true);	 //In trigger mode collisions are reported but do not apply forces. 
[/code]

and my component is registered in my main.cpp
[code]
    projet(Context* context) : Application(context)
    {
        context->RegisterFactory<Module>();
    }
[/code]

-------------------------

noals | 2017-01-02 01:12:40 UTC | #45

the component doesn't even work at all.

[code]
void Module::OnNodeSet(Node* node)
{
    // If the node pointer is non-null, this component has been created into a scene node. Subscribe to physics collisions that concern this scene node
    if (node)
    {
        SubscribeToEvent(node, E_NODECOLLISIONSTART, URHO3D_HANDLER(Module, OnCollisionEvent));
        URHO3D_LOGINFO("node set");
    }
}
[/code]
this actually return me "node set" in the log but that's all this fucking component can do !
in my main.cpp, if i try to move the node with the component on it with SetWorldPosition(), nothing move at all.

i'm losing my time with this shit.  :imp: 
how da fuck do this shit work really ?!

main
[spoiler][code]//engine
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

#include <Urho3D/Math/Vector3.h>

#include <Urho3D/UI/Window.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/IO/Log.h>

//my class
#include "CreateModule.[code][/code]h"
#include "Exit.h"
#include "Counts.h"

//include
#include <string>
#include <iostream>
#include <sstream>

//physic
#include <Urho3D/Physics/PhysicsWorld.h>
#include <Urho3D/Physics/PhysicsEvents.h>



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

    //physic
    bool drawDebug_;

    //about text
    Window* window;
    Text* text;

    projet(Context* context) : Application(context)
    {
// Register an object factory for our custom CreateRagdoll component so that we can create them to scene nodes
        context->RegisterFactory<Module>();
        //context->RegisterFactory<Exit>();
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
//physic

        my_scene->CreateComponent<PhysicsWorld>(); 



////___________________
////    MODULES    
        
        //Dungeon dungeon(100, my_scene, cache);
        
        Node* m_Node = my_scene->CreateChild("Test");
        m_Node->CreateComponent<Module>();
        Module* m_comp = m_Node->GetComponent<Module>();
        m_comp->createRoom(my_scene, cache);

        Node* m_Node2 = my_scene->CreateChild("Test2");
        m_Node2->CreateComponent<Module>();
        Module* m_comp2 = m_Node2->GetComponent<Module>();
        m_comp2->createCor(my_scene, cache);
        m_comp2->SetWorldPosition(Vector3(0,2,0)); //i tryed with the node as well
        


        URHO3D_LOGINFO("test_main"); 





////__________________
////    CAMERA        

using namespace Urho3D;
        camNode=my_scene->CreateChild("camNode");
        Camera* camObject=camNode->CreateComponent<Camera>();
        camObject->SetFarClip(2000);
	camNode->SetWorldPosition(Vector3(0,20,-20));     //x =blender y //y =blender z hauteur //z =blender x profondeur
	camNode->LookAt(Vector3::ZERO);

        //camera light
        {
            Light* light=camNode->CreateComponent<Light>();
            light->SetLightType(LIGHT_POINT);
            light->SetRange(25);
            light->SetBrightness(2.0);
            light->SetColor(Color(.8,1,.8,1.0));
        }

////________________
////    TEXT    


        std::string str = (""); 
        {
            std::ostringstream ss;
            ss;
              //<<" module count = "<<dungeon.MODULE_COUNT
              //<<"\n free exit = "<<dungeon.mainExitList.size();

            std::string s(ss.str());
            str.append(s/*.substr(0,60)*/);
        }
        String s(str.c_str(),str.size());

        window=new Window(context_);
        GetSubsystem<UI>()->GetRoot()->AddChild(window);
        window->SetStyle("Window");
        window->SetSize(500,200);
        window->SetColor(Color(.0,.15,.3,.5));
        window->SetAlignment(HA_LEFT,VA_TOP);

        text=new Text(context_);
        text->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"),14);
        text->SetColor(Color(.8,.85,.9));
        text->SetAlignment(HA_LEFT,VA_TOP);
        text->SetText(s); //s
        window->AddChild(text);


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
        SubscribeToEvent(E_POSTRENDERUPDATE,URHO3D_HANDLER(projet,HandlePostRenderUpdate));     
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
        if (input->GetKeyPress(KEY_SPACE)) // Toggle physics debug geometry with space
            drawDebug_ = !drawDebug_;

	if(!GetSubsystem<Input>()->IsMouseGrabbed())
	{
	    IntVector2 mouseMove=input->GetMouseMove();
	    
	    if(mouseMove.x_>-2000000000&&mouseMove.y_>-2000000000)
            {
		camNode->LookAt(Vector3::ZERO); //look at 0,0,0
            }
	}
            


    }
////_______


////________

    void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
    {
    // If draw debug mode is enabled, draw physics debug geometry. Use depth test to make the result easier to interpret
        if (drawDebug_)
            my_scene->GetComponent<PhysicsWorld>()->DrawDebugGeometry(true);
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
[/code][/spoiler]

comp.h
[spoiler][code]//
// Copyright (c) 2008-2015 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

#pragma once

#include <Urho3D/Physics/CollisionShape.h>
#include "ModuleInfos.h"

using namespace Urho3D;

/// Custom component (that creates a ragdoll upon collision.)
class Module : public Component
{
    URHO3D_OBJECT(Module, Component);
    
public:
    /// Construct.
    Module(Context* context);
	
    void createRoom(Scene* scene, ResourceCache* cache);
    void createCor(Scene* scene, ResourceCache* cache);
    void createJunc(Scene* scene, ResourceCache* cache);

	int type;
	int exits;
	
    
protected:
    /// Handle node being assigned.
    virtual void OnNodeSet(Node* node);
    
private:
    /// Handle scene node's physics collision.
    void OnCollisionEvent(StringHash eventType, VariantMap& eventData);
    
/*    
    /// Make a bone physical by adding RigidBody and CollisionShape components.
    void CreateRagdollBone(const String& boneName, ShapeType type, const Vector3& size, const Vector3& position, const Quaternion& rotation);
    /// Join two bones with a Constraint component.
    void CreateRagdollConstraint(const String& boneName, const String& parentName, ConstraintType type, const Vector3& axis, const Vector3& parentAxis, const Vector2& highLimit, const Vector2& lowLimit, bool disableCollision = true);
*/
    
//to load different modules type infos
    r_Rooms* room_p;
    r_Cors* cor_p;
    r_Juncs* junc_p;
};[/code][/spoiler]

comp.cpp
[spoiler][code]//
// Copyright (c) 2008-2015 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/Graphics/Graphics.h>

#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Math/Vector3.h>
#include <Urho3D/Math/Quaternion.h>
#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Graphics/AnimatedModel.h>
#include <Urho3D/Graphics/Material.h>
#include <string>
#include <vector>

#include "fonctions.h"
#include "conversions.h"
#include "Counts.h"
#include "Exit.h"

#include "tinyxml2.h"
#include <Urho3D/IO/Log.h>
#include <Urho3D/DebugNew.h>

//physic
#include <Urho3D/Physics/CollisionShape.h>
//#include <Urho3D/Physics/PhysicsWorld.h>
#include <Urho3D/Physics/RigidBody.h>
#include <Urho3D/Physics/PhysicsEvents.h>


#include "CreateModule.h"
#include "ModuleInfos.h"
//#include "CreateExit.h"

using namespace Urho3D;


Module::Module(Context* context) :
    Component(context),
	type(0),
	exits(0)
{
	//context->RegisterFactory<Exit>();
}

void Module::createRoom(Scene* scene, ResourceCache* cache)
{
    room_p = new r_Rooms();
	type = 0;
	exits = room_p->exits;
	
    std::string std_sceneName = IntString(id_, room_p->std_name);
    String sceneName = string2urhoString(std_sceneName);

    node_ = scene->CreateChild(sceneName);
    node_->SetWorldPosition(Vector3::ZERO);   //room.position          
    node_->SetWorldRotation(Quaternion::IDENTITY);   //room.rotation (1,0,0,0) 
    
    //m_Object = new AnimatedModel();    
    AnimatedModel* m_Object = node_->CreateComponent<AnimatedModel>();
    m_Object->SetModel(cache->GetResource<Model>(room_p->path));
    m_Object->SetMaterial(cache->GetResource<Material>(room_p->texturepath));
    
//add physic          
    RigidBody* m_Body = node_->CreateComponent<RigidBody>();
    m_Body->SetMass(1);  //0 for static object
    m_Body->SetUseGravity(false);
    m_Body->SetTrigger(true);
    m_Body->SetFriction(0.6);        // friction with other objects (like the ground)
    m_Body->SetCollisionLayer(1);

//add collision shape
    CollisionShape* m_BBox = node_->CreateComponent<CollisionShape>();
    m_BBox->SetTriangleMesh(cache->GetResource<Model>(room_p->path));

//add light
    Node* light=node_->CreateChild("m_light");
    light->SetPosition(Vector3(0, 5, 0));
    {
        Light* Mlight=light->CreateComponent<Light>();
        Mlight->SetLightType(LIGHT_POINT);
        Mlight->SetRange(20);
        Mlight->SetBrightness(1.0);
        Mlight->SetColor(Color(.8,.8,.8,1.0));
    }
/*
    for(int x=0; x<exits; x++)
    {
		
		std::string std_exitName = stringInt("exit",x);
        String name = string2urhoString(std_exitName);
		
        Node* exitNode = node_->GetChild(name, true);
		exitNode->CreateComponent<Exit>();
		
		
		//make a vector there ?
		
		Exit* tempExit = exitNode->GetComponent<Exit>();
		tempExit->type = 0;

		
		
		exit.type=room_p->type;
        exit.position = exit.e_Node->GetWorldPosition();
        exit.module_pos = Vector3::ZERO;
        exitList.push_back(exit);            
    }
	*/
}

void Module::createCor(Scene* scene, ResourceCache* cache)
{
    cor_p = new r_Cors();
	type = 1;
	exits = cor_p->exits;
	
    std::string std_sceneName = IntString(id_, cor_p->std_name);
    String sceneName = string2urhoString(std_sceneName);

    node_ = scene->CreateChild(sceneName);
    node_->SetWorldPosition(Vector3::ZERO);   //room.position          
    node_->SetWorldRotation(Quaternion::IDENTITY);   //room.rotation (1,0,0,0) 
    
    //m_Object = new AnimatedModel();    
    AnimatedModel* m_Object = node_->CreateComponent<AnimatedModel>();
    m_Object->SetModel(cache->GetResource<Model>(cor_p->path));
    m_Object->SetMaterial(cache->GetResource<Material>(cor_p->texturepath));
    
//add physic          
    RigidBody* m_Body = node_->CreateComponent<RigidBody>();
    m_Body->SetMass(1);  //0 for static object
    m_Body->SetUseGravity(false);
    m_Body->SetTrigger(true);
    m_Body->SetFriction(0.6);        // friction with other objects (like the ground)
    m_Body->SetCollisionLayer(1);

//add collision shape
    CollisionShape* m_BBox = node_->CreateComponent<CollisionShape>();
    m_BBox->SetTriangleMesh(cache->GetResource<Model>(cor_p->path));

//add light
    Node* light=node_->CreateChild("m_light");
    light->SetPosition(Vector3(0, 5, 0));
    {
        Light* Mlight=light->CreateComponent<Light>();
        Mlight->SetLightType(LIGHT_POINT);
        Mlight->SetRange(20);
        Mlight->SetBrightness(1.0);
        Mlight->SetColor(Color(.8,.8,.8,1.0));
    }
/*
    for(int x=0; x<cor_p->exits; x++)
    {
        Exit tempExit;    

        std::string std_exitName = stringInt("exit",x);
        exit.name = string2urhoString(std_exitName);
        exit.type=cor_p->type;
        exit.e_Node = node_->GetChild(exit.name, true);
        exit.position = exit.e_Node->GetWorldPosition();
        exit.module_pos = Vector3::ZERO;
        exitList.push_back(exit);            
    }*/
}

void Module::createJunc(Scene* scene, ResourceCache* cache)
{
    junc_p = new r_Juncs();
	type = 2;
	exits = junc_p->exits;
	
	std::string std_sceneName = IntString(id_, junc_p->std_name);
    String sceneName = string2urhoString(std_sceneName);

    node_ = scene->CreateChild(sceneName);
    node_->SetWorldPosition(Vector3::ZERO);   //room.position          
    node_->SetWorldRotation(Quaternion::IDENTITY);   //room.rotation (1,0,0,0) 
    
    //m_Object = new AnimatedModel();    
    AnimatedModel* m_Object = node_->CreateComponent<AnimatedModel>();
    m_Object->SetModel(cache->GetResource<Model>(junc_p->path));
    m_Object->SetMaterial(cache->GetResource<Material>(junc_p->texturepath));
    
//add physic          
    RigidBody* m_Body = node_->CreateComponent<RigidBody>();
    m_Body->SetMass(1);  //0 for static object
    m_Body->SetUseGravity(false);
    m_Body->SetTrigger(true);
    m_Body->SetFriction(0.6);        // friction with other objects (like the ground)
    m_Body->SetCollisionLayer(1);

//add collision shape
    CollisionShape* m_BBox = node_->CreateComponent<CollisionShape>();
    m_BBox->SetTriangleMesh(cache->GetResource<Model>(junc_p->path));

//add light
    Node* light=node_->CreateChild("m_light");
    light->SetPosition(Vector3(0, 5, 0));
    {
        Light* Mlight=light->CreateComponent<Light>();
        Mlight->SetLightType(LIGHT_POINT);
        Mlight->SetRange(20);
        Mlight->SetBrightness(1.0);
        Mlight->SetColor(Color(.8,.8,.8,1.0));
    }
/*
    for(int x=0; x<junc_p->exits; x++)
    {
        Exit tempExit;    

        std::string std_exitName = stringInt("exit",x);
        exit.name = string2urhoString(std_exitName);
        exit.type=junc_p->type;
        exit.e_Node = node_->GetChild(exit.name, true);
        exit.position = exit.e_Node->GetWorldPosition();
        exit.module_pos = Vector3::ZERO;
        exitList.push_back(exit);            
    }*/
}

//protected
void Module::OnNodeSet(Node* node)
{
    // If the node pointer is non-null, this component has been created into a scene node. Subscribe to physics collisions that concern this scene node
    if (node)
    {
        SubscribeToEvent(node, E_NODECOLLISIONSTART, URHO3D_HANDLER(Module, OnCollisionEvent));
        URHO3D_LOGINFO("node set");
    }
}

//private
void Module::OnCollisionEvent(StringHash eventType, VariantMap& eventData)
{
    using namespace NodeCollision;

    // Get the other colliding body
    RigidBody* otherBody = static_cast<RigidBody*>(eventData[P_OTHERBODY].GetPtr());

    //Node* otherNode = static_cast<Node*>(eventData[P_OTHERNODE].GetPtr());

    if (otherBody->GetMass() > 0.0f)
    {

        URHO3D_LOGINFO("collide");
        Light* light;
        light = node_->GetComponent<Light>();
        light->SetColor(Color(.8,.4,.4,1.0));

    //m_Body->SetMass(1);  //0 for static object
	//m_Body->SetUseGravity(false);
	//m_Body->SetTrigger(true);		
		
        // Finally remove self from the scene node. Note that this must be the last operation performed in the function
        //Remove();  
    }
}[/code][/spoiler]

-------------------------

noals | 2017-01-02 01:12:40 UTC | #46

i will try with a logic component.

edit: or not, because i shouldn't need real time to set my module's position at the beginning of my app.

dunno what to do.

-------------------------

Lumak | 2017-01-02 01:12:40 UTC | #47

Alright, there are a couple of things you can try.
First, remove setting up the body as a trigger, i.e. m_Body->SetTrigger(true); <-- comment this out.
Second, there are other collision events you can register for.  Try these: E_PHYSICSCOLLISION, E_NODECOLLISION.[b]E_PHYSICSCOLLISION[/b] event is ongoing, meaning that as long as there is a collision occurring you'll get an event callbck - it doesn't stop with just an initial collision call like E_NODECOLLISIONSTART.
Third, remove any conditionals in your OnCollisionEvent() function and just log what's coming in.
Lastly, I highly recommend working with Urho3D/Samples for starters.  Add bits of your code to test just to learn how things work. It might end up saving you weeks of trouble.

Good luck!

-------------------------

noals | 2017-01-02 01:12:40 UTC | #48

what about the component update ?
all this is pointless if my component doesn't even follow the node it is attached to.
the advantage for me with this component thing is that i can move it and rotate it using the node.

really, there should be templates examples for component, logic component, object with their essential requirements. (or not essential as a plus, for common usages, but commented as such !)
here instead of 3 clear examples, i have to deal with 41 of them kinda... 



[quote]First, remove setting up the body as a trigger, i.e. m_Body->SetTrigger(true); <-- comment this out.[/quote]
why ? 
i want my module as static in the physic world but i need them as non-static to test collision so i set them with :
[quote]SetUseGravity (bool enable)
 	Set whether gravity is applied to rigid body. [/quote]
and
[quote]SetTrigger (bool enable)
 	Set rigid body trigger mode. In trigger mode collisions are reported but do not apply forces. [/quote]
and when the collision check is done, i can make them static again and disable the trigger mode so the physic doesn't mess up with my modules's position when i'm placing them.

-------------------------

Lumak | 2017-01-02 01:12:41 UTC | #49

You'll get a better understanding of Urho3D physic, components, and callbacks by looking at 11_Physics demo.  

Try adding a subscription to E_NODECOLLISIONSTART and see how that works.  Then try PHYSICSCOLLISION.  Then try setting SetTrigger() and see what happens.

If you can observe those behaviors, my bet is you can fix what's wrong with yours.

-------------------------

Dave82 | 2017-01-02 01:12:41 UTC | #50

[quote]what about the component update ?
all this is pointless if my component doesn't even follow the node it is attached to.
the advantage for me with this component thing is that i can move it and rotate it using the node.[/quote]

Components doesn't have transforms , nodes do ! How do you expect your Module component to move in 3d space ? It's not a transformable entity it is just a component ! you expect to move based on what exacly ?

[quote]i'm losing my time with this shit.  
how da fuck do this shit work really ?![/quote]

Well, how about learning the basics first as i previously suggested ? I think Urho3d's structure is extremely well designed and could be understand in no time if you first learn c++ and Component based programming.
If you stuck with trivial things like how to add components to nodes , imagine how confusing it will be once you get into game logic programming and other nasty stuff which requires good understanding of c++ ?

[quote]this actually return me "node set" in the log but that's all this fucking component can do !
in my main.cpp, if i try to move the node with the component on it with SetWorldPosition(), nothing move at all.[/quote]

The code you posted doesn't make sense to me at all. How about using Nodes for modules.Create one component called (lets say) Element.In this Element component's Start() function add you necessary urho components AnimatedModel , Light , RigidBody etc. If you need extra parameters and functions just implement it to Element component. You can override Update() or FixedUpdate() etc in your Element and do per frame updates there. Other things i want to point out is : 
your code is so overcomplicated for such a simple task you want to achive.By simplifying the code i can garantee you could get the same effect with only 10-15 lines of code...

[code]void Module::createRoom(Scene* scene, ResourceCache* cache)[/code]
Your module is a component.It is unnecessary to pass the cache and scene pointers because those are already part of your Component.Use GetScene() anywehre in you Module to get the scene and use GetSubsystem<Urho3D::Cache>() to get the cache

[code]room_p = new r_Rooms();[/code]
You dynamically allocate memory but you never delete them in you code , thus you extremely leaking memory. Do you understand how dynamic memory allocation/deallocation works in c++ ?

[code]std::string std_sceneName[/code]

You still using std::string and i already stated that it is a bad idea.It's trivial to link against the stdlib on linux and windows but on other platforms may not be that simple.Also if you try to compile your game on a system that does not implement the std::string you're doomed. Same goes for std::vector. Urho3d has it's own Vector and String containers that the developers can guarantee will compile on every platform they support.If you use std:: i don't think they can guarantee anything. Urho's string and vector work exacly the same way as the std:: containers.

[code]exitNode->CreateComponent<Exit>();   
Exit* tempExit = exitNode->GetComponent<Exit>();[/code]
Whats wrong with 
[code]Exit* tempExit = exitNode->CreateComponent<Exit>();[/code] 


[code]exit.position = exit.e_Node->GetWorldPosition();
exit.module_pos = Vector3::ZERO;
exitList.push_back(exit);[/code]
This doesn't make any sense.Why you need a separate component for this ? I would suggest you could use node->SetVar() GetVar() for parameters like these.Or simply implement them in the Element component i suggested.

-------------------------

noals | 2017-01-02 01:12:41 UTC | #51

first, i want things done. then, i optimize my code or whatever.

my first step is having my maze generated without problems, and to do so, i need a collision check.
i don't really need the whole physical simulation right now, i just need something that tell me when two modules are colliding, that's all.

you guys told me to use events.
from there already it became a mess because i didn't know about events and i wanted it to work in my class and not in the main.cpp and then you told me about components, etc...

so right now, i will test some events in my main.cpp and see how it goes.

-------------------------

noals | 2017-01-02 01:12:41 UTC | #52

so here is my try :

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

#include <Urho3D/Math/Vector3.h>

#include <Urho3D/UI/Window.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/UI/UI.h>

//my class
#include "Modules.h"
#include "Exit.h"
#include "Counts.h"

//include
#include <string>
#include <iostream>
#include <sstream>

//just for testing
#include "conversions.h"
#include "fonctions.h"
#include <Urho3D/IO/Log.h>

//physic
#include <Urho3D/Physics/CollisionShape.h>//test
#include <Urho3D/Physics/PhysicsWorld.h>
#include <Urho3D/Physics/RigidBody.h>//test
#include <Urho3D/Physics/PhysicsEvents.h>



using namespace NodeCollision;
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

    //physic
    bool drawDebug_;

    //about text
    Window* window;
    Text* text;

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
//physic
        my_scene->CreateComponent<PhysicsWorld>();


////___________________
////    MODULES    

        
        //Dungeon dungeon(600, my_scene, cache);


    Node* m_Node = my_scene->CreateChild("1");
    m_Node->SetWorldPosition(Vector3::ZERO);   //room.position          
    m_Node->SetWorldRotation(Quaternion::IDENTITY);   //room.rotation (1,0,0,0) 
     
    AnimatedModel* m_Object=m_Node->CreateComponent<AnimatedModel>();
    m_Object->SetModel(cache->GetResource<Model>("Models/room0.mdl"));
    m_Object->SetMaterial(cache->GetResource<Material>("Materials/blank.xml"));
              
    RigidBody* m_Body = m_Node->CreateComponent<RigidBody>();
    m_Body->SetMass(0);  //0 for static object
    //m_Body->SetUseGravity(false);
    //m_Body->SetTrigger(true);
    m_Body->SetFriction(0.6);        // friction with other objects (like the ground)
    m_Body->SetCollisionLayer(1);

    CollisionShape* m_BBox = m_Node->CreateComponent<CollisionShape>();
    m_BBox->SetTriangleMesh(cache->GetResource<Model>("Models/room0.mdl"));
        
    Node* light=m_Node->CreateChild("m_light");
    light->SetPosition(Vector3(0, 5, 0));
    {
        Light* Mlight=light->CreateComponent<Light>();
        Mlight->SetLightType(LIGHT_POINT);
        Mlight->SetRange(20);
        Mlight->SetBrightness(1.0);
        Mlight->SetColor(Color(.8,.8,.8,1.0));
    }


    Node* m_Node2 = my_scene->CreateChild("2");
    m_Node2->SetWorldPosition(Vector3(0,3,0));   //room.position          
    m_Node2->SetWorldRotation(Quaternion::IDENTITY);   //room.rotation (1,0,0,0) 
     
    AnimatedModel* m_Object2=m_Node2->CreateComponent<AnimatedModel>();
    m_Object2->SetModel(cache->GetResource<Model>("Models/cor0.mdl"));
    m_Object2->SetMaterial(cache->GetResource<Material>("Materials/blank.xml"));
              
    RigidBody* m_Body2 = m_Node2->CreateComponent<RigidBody>();
    m_Body2->SetMass(1);  //0 for static object
    //m_Body2->SetUseGravity(false);
    //m_Body2->SetTrigger(true);
    m_Body2->SetFriction(0.6);        // friction with other objects (like the ground)
    m_Body2->SetCollisionLayer(1);

    CollisionShape* m_BBox2 = m_Node2->CreateComponent<CollisionShape>();
    m_BBox2->SetTriangleMesh(cache->GetResource<Model>("Models/cor0.mdl"));



////__________________
////    CAMERA        


        camNode=my_scene->CreateChild("camNode");
        Camera* camObject=camNode->CreateComponent<Camera>();
        camObject->SetFarClip(2000);
	camNode->SetWorldPosition(Vector3(0,20,-20));     //x =blender y //y =blender z hauteur //z =blender x profondeur
	camNode->LookAt(Vector3::ZERO);

        //camera light
        {
            Light* light=camNode->CreateComponent<Light>();
            light->SetLightType(LIGHT_POINT);
            light->SetRange(25);
            light->SetBrightness(2.0);
            light->SetColor(Color(.8,1,.8,1.0));
        }

////________________
////    TEXT    


        std::string str = (""); 
        {
            std::ostringstream ss;
            ss;
              //<<" module count = "<<dungeon.MODULE_COUNT
              //<<"\n free exit = "<<dungeon.mainExitList.size();

            std::string s(ss.str());
            str.append(s/*.substr(0,60)*/);
        }
        String s(str.c_str(),str.size());

        window=new Window(context_);
        GetSubsystem<UI>()->GetRoot()->AddChild(window);
        window->SetStyle("Window");
        window->SetSize(500,200);
        window->SetColor(Color(.0,.15,.3,.5));
        window->SetAlignment(HA_LEFT,VA_TOP);

        text=new Text(context_);
        text->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"),14);
        text->SetColor(Color(.8,.85,.9));
        text->SetAlignment(HA_LEFT,VA_TOP);
        text->SetText(s); //s
        window->AddChild(text);


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

        SubscribeToEvent(m_Node, E_NODECOLLISION, URHO3D_HANDLER(projet, OnNodeCollisionEvent));
        SubscribeToEvent(E_PHYSICSCOLLISION, URHO3D_HANDLER(projet, OnCollisionEvent));

    //SubscribeToEvent(E_RENDERUPDATE,URHO3D_HANDLER(projet,HandleRenderUpdate));
        SubscribeToEvent(E_POSTRENDERUPDATE,URHO3D_HANDLER(projet,HandlePostRenderUpdate));     
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
        if (input->GetKeyPress(KEY_SPACE)) // Toggle physics debug geometry with space
            drawDebug_ = !drawDebug_;

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


    void OnNodeCollisionEvent(StringHash eventType, VariantMap& eventData)
    {
        URHO3D_LOGINFO("OnNodeCollisionEvent");
    }


    void OnCollisionEvent(StringHash eventType, VariantMap& eventData)
    {
        //RigidBody* body = static_cast<RigidBody*>(eventData[P_BODY].GetPtr());
        URHO3D_LOGINFO("OnCollisionEvent");
    }

////________

    void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
    {
    // If draw debug mode is enabled, draw physics debug geometry. Use depth test to make the result easier to interpret
        if (drawDebug_)
            my_scene->GetComponent<PhysicsWorld>()->DrawDebugGeometry(true);
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


it load my 2 test module, and the second module just fall through the first one.

1/ why the physic simulation isn't working at all ? i have a static and a non-static, i guess the non-static should somehow bounce on the static no ?
2/ and why none of my events return a thing in the log ?

-------------------------

noals | 2017-01-02 01:12:42 UTC | #53

at least, i was able to get something working and so i found out what my problem is.
[code] m_BBox->SetTriangleMesh(cache->GetResource<Model>("Models/room0.mdl"));[/code]

if i set my collision shape as a box, it work like a charm but it doesn't do anything with SetTriangleMesh and my custom shape.
i recall having see something about it somewhere, i through it was in the API but doesn't seem so or it was edited while i was trying stuff.
it was saying that the SetTriangleMesh thing is not activated by default or something and i don't remember what it was saying to fix it.

so, how can i make my room0.mdl well recognized by the physic engine ?

-------------------------

noals | 2017-01-02 01:12:42 UTC | #54

found out, it was in the wiki.

[quote]Note: triangle mesh on triangle mesh collisions are disabled per default. See PhysicsWorld::SetInternalEdge(bool enable) [urho3d.github.io/documentation/1 ... world.html](http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_physics_world.html). [/quote]
im using windows right now, i program with ubuntu but i will test it next time in hope it will work at last... ><

-------------------------

noals | 2017-01-02 01:12:45 UTC | #55

[code]
        PhysicsWorld* physicWorld = my_scene->CreateComponent<PhysicsWorld>();
        physicWorld->SetInternalEdge(true);
[/code]
doesn't work either. i'm kinda losing hope...
is there another method to get .mdl collision shapes well recognized by the engine ?
could it be a .mdl issue ? a setting in blender, i wonder.

-------------------------

noals | 2017-01-02 01:12:47 UTC | #56

i'm a bit disappointed but convex hulls seems to work so i will try with that.

[quote="Dave82"]Components doesn't have transforms , nodes do ! How do you expect your Module component to move in 3d space ? It's not a transformable entity it is just a component ! you expect to move based on what exacly ?[/quote]
yes, i'm trying to derive from Node but it confuse me more than ever.

[quote="Dave82"]your code is so overcomplicated for such a simple task you want to achive.By simplifying the code i can garantee you could get the same effect with only 10-15 lines of code...[/quote]
i would like to know how to do that, each time i try a different thing but it end up a mess anyway.
i use std::string because it is needed for tinyxml2. i had difficulties using PugiXML, tinyxml2 was more convenient to me.
and then, there is all the mess around.

the xml (so i can change modules not having to recompile)
[spoiler][code]<xml>

<infos room_count="3" cor_count="4" junc_count="3" toLoad="100"/>

<room0 exits="4" path="Models/room0.mdl" texturepath="Materials/blank.xml"/>
<room1 exits="4" path="Models/room1.mdl" texturepath="Materials/blank.xml"/>
<room2 exits="4" path="Models/room2.mdl" texturepath="Materials/blank.xml"/>

<cor0 exits="2" path="Models/cor0.mdl" texturepath="Materials/blank.xml"/>
<cor1 exits="2" path="Models/cor1.mdl" texturepath="Materials/blank.xml"/>
<cor2 exits="2" path="Models/cor2.mdl" texturepath="Materials/blank.xml"/>
<cor3 exits="2" path="Models/cor3.mdl" texturepath="Materials/blank.xml"/>

<junc0 exits="4" path="Models/junc0.mdl" texturepath="Materials/blank.xml"/>
<junc1 exits="3" path="Models/junc1.mdl" texturepath="Materials/blank.xml"/>
<junc2 exits="3" path="Models/junc2.mdl" texturepath="Materials/blank.xml"/>

</xml>[/code][/spoiler]

a class to check the number of modules by type and the number of module i will want to load. (i need to add some code if a value is 0 or the app will crash)
[spoiler][code]xmlCounts::xmlCounts()
{

    tinyxml2::XMLDocument modules;
    modules.Parse("Data/Scripts/Modules.xml");
    if(modules.LoadFile("Data/Scripts/Modules.xml") == tinyxml2::XML_NO_ERROR)
    {
        tinyxml2::XMLNode* root = modules.FirstChild();
        tinyxml2::XMLElement* infos = root->FirstChildElement("infos");
        infos->QueryIntAttribute("room_count", &room);
        infos->QueryIntAttribute("cor_count", &cor);
        infos->QueryIntAttribute("junc_count", &junc);
        infos->QueryIntAttribute("toLoad", &toLoad);
    }

}[/code][/spoiler]

then i use xml again to get module infos
[spoiler][code]r_Rooms::r_Rooms()
{

    xmlCounts m_counts;
    
    type=0;
    int roomNbr = chooseRandomNbr(m_counts.room);
    std::string std_name = stringInt("room",roomNbr);
    const char* ROOMX = std_name.c_str(); //std::string to const char*
        
    tinyxml2::XMLDocument modulesXML;
    modulesXML.Parse("Data/Scripts/Modules.xml");
    if(modulesXML.LoadFile("Data/Scripts/Modules.xml") == tinyxml2::XML_NO_ERROR)
    {
            tinyxml2::XMLNode* root = modulesXML.FirstChild();
            tinyxml2::XMLElement* roomXML = root->FirstChildElement(ROOMX);
            roomXML->QueryIntAttribute("exits", &exits);
            std::string std_path = roomXML->Attribute("path");                
            std::string std_texturepath = roomXML->Attribute("texturepath");
            path = string2urhoString(std_path); //to urho String
            texturepath = string2urhoString(std_texturepath); //to urho String
             
    }
}[/code][/spoiler]

and then, i need something to create a urho node with a module with AnimatedModel, a vector of child node or something with its exits (bones that i get position from) and its RigidBody and CollisionShape so i can register it with a collision event to test collision and move it at will when i build the dungeon.
how would you do that because i don't know how to organise it for the best.

[quote="Dave82"]Do you understand how dynamic memory allocation/deallocation works in c++ ?[/quote]
yes a little. i know i don't free the memory where i should.. ^^;

[quote="Dave82"]This doesn't make any sense.Why you need a separate component for this ? I would suggest you could use node->SetVar() GetVar() for parameters like these.Or simply implement them in the Element component i suggested.[/quote]
basicaly, one exit is a child node that represent a bone of the module. i use those to get my exits positions to calculate modules placement when i build the dungeon.


anyway, thx for your patience, any help is appreciated, it's just that i tryed a few things before and each time i was kinda stuck at physic so it's very frustrating for me as i'm kinda very close to exceed this limit.

-------------------------

noals | 2017-01-02 01:12:49 UTC | #57

it's with convex hulls but it works at last.
just added this component :

OnCollision.h
[code]
#pragma once

using namespace Urho3D;

class OnCollision : public Component
{
    URHO3D_OBJECT(OnCollision, Component);
    
public:
    OnCollision(Context* context);

protected:
    /// Handle node being assigned.
    virtual void OnNodeSet(Node* node);
    
private:
    /// Handle scene node's physics collision.
    void OnCollisionEvent(StringHash eventType, VariantMap& eventData);
};
[/code]

OnCollision.cpp
[code]
#include "OnCollision.h"

using namespace Urho3D;

OnCollision::OnCollision(Context* context) :
    Component(context)
{

}


//protected
void OnCollision::OnNodeSet(Node* node)
{
    // If the node pointer is non-null, this component has been created into a scene node. Subscribe to physics collisions that concern this scene node
    if (node)
    {
        SubscribeToEvent(node, E_NODECOLLISIONSTART, URHO3D_HANDLER(OnCollision, OnCollisionEvent));
        URHO3D_LOGINFO("node set");
    }
}

//private
void OnCollision::OnCollisionEvent(StringHash eventType, VariantMap& eventData)
{
    using namespace NodeCollision;

    // Get the other colliding body
    RigidBody* otherBody = static_cast<RigidBody*>(eventData[P_OTHERBODY].GetPtr());

        URHO3D_LOGINFO("collide");
		
        // Finally remove self from the scene node. Note that this must be the last operation performed in the function
        //Remove();  
}
[/code]

log
[quote]
[Sun Jun 12 06:19:47 2016] INFO: Opened log file Urho3D.log
[Sun Jun 12 06:19:47 2016] INFO: Created 3 worker threads
[Sun Jun 12 06:19:47 2016] INFO: Added resource path /home/noname/Bureau/projet_build/bin/Data/
[Sun Jun 12 06:19:47 2016] INFO: Added resource path /home/noname/Bureau/projet_build/bin/CoreData/
[Sun Jun 12 06:19:47 2016] DEBUG: Skipped autoload path 'Autoload' as it does not exist, check the documentation on how to set the 'resource prefix path'
[Sun Jun 12 06:19:47 2016] INFO: Set screen mode 1280x720 windowed resizable
[Sun Jun 12 06:19:47 2016] INFO: Initialized input
[Sun Jun 12 06:19:47 2016] INFO: Initialized user interface
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource Textures/Ramp.png
[Sun Jun 12 06:19:47 2016] DEBUG: Loading temporary resource Textures/Ramp.xml
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource Textures/Spot.png
[Sun Jun 12 06:19:47 2016] DEBUG: Loading temporary resource Textures/Spot.xml
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource Techniques/NoTexture.xml
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource RenderPaths/Forward.xml
[Sun Jun 12 06:19:47 2016] INFO: Initialized renderer
[Sun Jun 12 06:19:47 2016] ERROR: Could not initialize audio output
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource UI/MessageBox.xml
[Sun Jun 12 06:19:47 2016] DEBUG: Loading UI layout UI/MessageBox.xml
[Sun Jun 12 06:19:47 2016] INFO: Initialized engine
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource Models/room2.mdl        <---- first model
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource Materials/blank.xml
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource Techniques/Diff.xml
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource Textures/grid_8x8.png
[Sun Jun 12 06:19:47 2016] INFO: node set        <---- 
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource Models/cor1.mdl        <---- second model
[Sun Jun 12 06:19:47 2016] INFO: node set        <---- 
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource Fonts/Anonymous Pro.ttf
[Sun Jun 12 06:19:47 2016] DEBUG: Font face Anonymous Pro (14pt) has 624 glyphs
[Sun Jun 12 06:19:47 2016] DEBUG: Reloading shaders
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource Shaders/GLSL/LitSolid.glsl
[Sun Jun 12 06:19:47 2016] DEBUG: Compiled vertex shader LitSolid(PERPIXEL POINTLIGHT SKINNED)
[Sun Jun 12 06:19:47 2016] DEBUG: Compiled pixel shader LitSolid(AMBIENT DIFFMAP PERPIXEL POINTLIGHT SPECULAR)
[Sun Jun 12 06:19:47 2016] DEBUG: Linked vertex shader LitSolid(PERPIXEL POINTLIGHT SKINNED) and pixel shader LitSolid(AMBIENT DIFFMAP PERPIXEL POINTLIGHT SPECULAR)
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource Shaders/GLSL/Stencil.glsl
[Sun Jun 12 06:19:47 2016] DEBUG: Compiled vertex shader Stencil()
[Sun Jun 12 06:19:47 2016] DEBUG: Compiled pixel shader Stencil()
[Sun Jun 12 06:19:47 2016] DEBUG: Linked vertex shader Stencil() and pixel shader Stencil()
[Sun Jun 12 06:19:47 2016] DEBUG: Compiled pixel shader LitSolid(DIFFMAP PERPIXEL POINTLIGHT SPECULAR)
[Sun Jun 12 06:19:47 2016] DEBUG: Linked vertex shader LitSolid(PERPIXEL POINTLIGHT SKINNED) and pixel shader LitSolid(DIFFMAP PERPIXEL POINTLIGHT SPECULAR)
[Sun Jun 12 06:19:47 2016] DEBUG: Loading resource Shaders/GLSL/Basic.glsl
[Sun Jun 12 06:19:47 2016] DEBUG: Compiled vertex shader Basic(VERTEXCOLOR)
[Sun Jun 12 06:19:47 2016] DEBUG: Compiled pixel shader Basic(VERTEXCOLOR)
[Sun Jun 12 06:19:47 2016] DEBUG: Linked vertex shader Basic(VERTEXCOLOR) and pixel shader Basic(VERTEXCOLOR)
[Sun Jun 12 06:19:47 2016] INFO: OnCollisionEvent
[Sun Jun 12 06:19:47 2016] INFO: collide        <---- 
[Sun Jun 12 06:19:47 2016] INFO: collide        <---- 
[Sun Jun 12 06:19:47 2016] INFO: OnCollisionEvent
[Sun Jun 12 06:19:47 2016] INFO: OnCollisionEvent
[Sun Jun 12 06:19:47 2016] INFO: OnCollisionEvent
[Sun Jun 12 06:19:47 2016] INFO: OnCollisionEvent
[Sun Jun 12 06:19:47 2016] INFO: OnCollisionEvent
[Sun Jun 12 06:19:47 2016] INFO: OnCollisionEvent
[Sun Jun 12 06:19:47 2016] INFO: OnCollisionEvent
[Sun Jun 12 06:19:47 2016] INFO: OnCollisionEvent
[Sun Jun 12 06:19:47 2016] INFO: OnCollisionEvent
[Sun Jun 12 06:19:47 2016] INFO: OnCollisionEvent
etc...
[/quote]

now, i just need to find a way to avoid collision between module that are next to each other but it shouldn't be too hard now that i understand the events better :
[code]
URHO3D_EVENT(E_NODECOLLISION, NodeCollision)
{
    URHO3D_PARAM(P_BODY, Body);                    // RigidBody pointer
    URHO3D_PARAM(P_OTHERNODE, OtherNode);          // Node pointer
    URHO3D_PARAM(P_OTHERBODY, OtherBody);          // RigidBody pointer
    URHO3D_PARAM(P_TRIGGER, Trigger);              // bool
    URHO3D_PARAM(P_CONTACTS, Contacts);            // Buffer containing position (Vector3), normal (Vector3), distance (float), impulse (float) for each contact
}
[/code]

thx.

-------------------------

