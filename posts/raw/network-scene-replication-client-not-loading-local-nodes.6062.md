Bambofy | 2020-04-02 20:59:24 UTC | #1

Hi,

I'm writing a multiplayer game and i'm using scene replication to network everything. I've got a bug where when the client joins the server, none of the LOCAL nodes in the scene file loaded by the server, are loaded by the client.

The client only loads the REPLICATED scene nodes, and non of the LOCAL nodes defined in the scene file?

Here are the logs of my Client and Server applications.

SERVER_LOG.txt
>     [Thu Apr  2 21:51:43 2020] INFO: Opened log file SERVER_LOG.txt
>     [Thu Apr  2 21:51:43 2020] INFO: Started server on port 25565
>     [Thu Apr  2 21:51:43 2020] INFO: Loading scene from Scenes/City.xml
>     [Thu Apr  2 21:51:43 2020] INFO: Building dynamic navigation mesh...
>     [Thu Apr  2 21:51:43 2020] INFO: Complete!
>     [Thu Apr  2 21:51:43 2020] INFO: Creating entity HP_PACK
>     [Thu Apr  2 21:51:43 2020] INFO: Creating entity ENT_PISTOL
>     [Thu Apr  2 21:51:43 2020] INFO: Creating entity ENT_TANK
>     [Thu Apr  2 21:51:45 2020] INFO: Client 127.0.0.1:56111 connected
>     [Thu Apr  2 21:51:45 2020] INFO: Creating entity PLAYER_ENTITY
>     [Thu Apr  2 21:51:45 2020] INFO: Added Flashlight to the weapon belt
>     [Thu Apr  2 21:51:45 2020] INFO: Added Crowbar to the weapon belt
>     [Thu Apr  2 21:51:48 2020] INFO: Client 127.0.0.1:56111 disconnected
>     [Thu Apr  2 21:51:49 2020] INFO: Stopped server


CLIENT_LOG.txt:
>     [Thu Apr  2 21:51:45 2020] INFO: Opened log file CLIENT_LOG.txt
>     [Thu Apr  2 21:51:45 2020] INFO: Initializing client connection...
>     [Thu Apr  2 21:51:45 2020] INFO: Connecting to server 127.0.0.1:25565, Client: 127.0.0.1:56111
>     [Thu Apr  2 21:51:45 2020] INFO: Connected to server!
>     [Thu Apr  2 21:51:45 2020] INFO: Loading scene from Scenes/City.xml
>     [Thu Apr  2 21:51:45 2020] INFO: Weapon added to belt: Flashlight
>     [Thu Apr  2 21:51:45 2020] INFO: Weapon added to belt: Crowbar
>     [Thu Apr  2 21:51:45 2020] ERROR: No Octree component in scene, drawable will not render

Here is the scene file i'm having trouble with, it contains 2 nodes, 1 local and 1 replicated, only the replicated node is loaded by the client?

    <?xml version="1.0"?>

    <scene id="1">

        <attribute name="Name" value="" />

        <attribute name="Time Scale" value="1" />

        <attribute name="Smoothing Constant" value="50" />

        <attribute name="Snap Threshold" value="5" />

        <attribute name="Elapsed Time" value="0" />

        <attribute name="Next Replicated Node ID" value="1" />

        <attribute name="Next Replicated Component ID" value="1" />

        <attribute name="Next Local Node ID" value="16777218" />

        <attribute name="Next Local Component ID" value="16777240" />

        <attribute name="Variables" />

        <attribute name="Variable Names" value="" />

        <component type="Octree" id="1" />

        <component type="DebugRenderer" id="2" />

        <component type="Zone" id="3" />

        <component type="PhysicsWorld" id="7" />

        <component type="Skybox" id="9">

            <attribute name="Model" value="Model;Models/Box.mdl" />

            <attribute name="Material" value="Material;Materials/Skybox.xml" />

        </component>

        <node id="16777218">

            <attribute name="Is Enabled" value="true" />

            <attribute name="Name" value="" />

            <attribute name="Tags" />

            <attribute name="Position" value="-17.2457 -19.3131 36.8148" />

            <attribute name="Rotation" value="1 0 0 0" />

            <attribute name="Scale" value="1 1 1" />

            <attribute name="Variables" />

            <component type="StaticModel" id="16777240">

                <attribute name="Model" value="Model;Simple_Apocolypse/UrhoMDL/SA_Bld_OfficeGrey_02.fbx.mdl" />

                <attribute name="Material" value="Material;Simple_Apocolypse/Urho/Materials/DEFAULT.xml;Simple_Apocolypse/Urho/Materials/DEFAULT.xml" />

            </component>

        </node>

        <node id="3">

            <attribute name="Is Enabled" value="true" />

            <attribute name="Name" value="" />

            <attribute name="Tags" />

            <attribute name="Position" value="0 -1.43321 0" />

            <attribute name="Rotation" value="1 0 0 0" />

            <attribute name="Scale" value="10 10 10" />

            <attribute name="Variables" />

            <component type="StaticModel" id="10">

                <attribute name="Model" value="Model;Models/Plane.mdl" />

                <attribute name="Material" value="Material;Materials/StoneTiled.xml" />

            </component>

            <component type="CollisionShape" id="11">

                <attribute name="Shape Type" value="ConvexHull" />

                <attribute name="Model" value="Model;Models/Plane.mdl" />

            </component>

            <component type="RigidBody" id="12">

                <attribute name="Physics Position" value="0 -1.43321 0" />

                <attribute name="Use Gravity" value="false" />

                <attribute name="Is Kinematic" value="true" />

            </component>

        </node>

        <node id="16777221">

            <attribute name="Is Enabled" value="true" />

            <attribute name="Name" value="" />

            <attribute name="Tags" />

            <attribute name="Position" value="0.0141136 1.47894 -0.111718" />

            <attribute name="Rotation" value="1 0 0 0" />

            <attribute name="Scale" value="1 1 1" />

            <attribute name="Variables" />

            <component type="Light" id="16777265">

                <attribute name="Light Shape Texture" value="TextureCube;" />

            </component>

        </node>

    </scene>

-------------------------

Bambofy | 2020-04-05 01:54:34 UTC | #2

Found the fix, it was because the Scene.XML file had the octree root component as nodeid="1" which means its a replicated component, when it should be >116777000

https://github.com/urho3d/Urho3D/issues/2616#issuecomment-608368333

-------------------------

