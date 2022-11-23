vivienneanthony | 2017-01-02 00:59:51 UTC | #1

Hello

Is there something wrong with this? Basically, I setup the physics and Suzanne drops but goes through the terrain.

[code]<?xml version="1.0"?>
<scene id="1">
	<attribute name="Name" value="" />
	<attribute name="Time Scale" value="1" />
	<attribute name="Smoothing Constant" value="50" />
	<attribute name="Snap Threshold" value="5" />
	<attribute name="Elapsed Time" value="681.346" />
	<attribute name="Next Replicated Node ID" value="1" />
	<attribute name="Next Replicated Component ID" value="14354" />
	<attribute name="Next Local Node ID" value="16791596" />
	<attribute name="Next Local Component ID" value="16777299" />
	<attribute name="Variables" />
	<attribute name="Variable Names" value="" />
	<component type="Octree" id="1" />
	<component type="PhysicsWorld" id="2" />
	<component type="DebugRenderer" id="3" />
	<node id="16777413">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Terrain" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="Terrain" id="16777225">
			<attribute name="Height Map" value="Image;Textures/heightmap2.png" />
			<attribute name="Smooth Height Map" value="true" />
			<attribute name="Is Occluder" value="true" />
			<attribute name="Cast Shadows" value="true" />
		</component>
		<component type="RigidBody" id="16777280">
			<attribute name="Use Gravity" value="false" />
		</component>
		<component type="CollisionShape" id="16777281">
			<attribute name="Shape Type" value="Terrain" />
		</component>
	</node>
	<node id="16777281">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="lightElement" />
		<attribute name="Position" value="0 15.2658 0" />
		<attribute name="Rotation" value="0.985681 0.168619 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="Light" id="16777217">
			<attribute name="Light Type" value="Directional" />
			<attribute name="Specular Intensity" value="0" />
			<attribute name="Brightness Multiplier" value="0.4" />
			<attribute name="Cast Shadows" value="true" />
		</component>
	</node>
	<node id="16778902">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="camera" />
		<attribute name="Position" value="-13.2652 24.3692 43.1406" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="Camera" id="16777271">
			<attribute name="Aspect Ratio" value="1.78218" />
		</component>
	</node>
	<node id="16777283">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Zone" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="Zone" id="16777220">
			<attribute name="Bounding Box Min" value="-100 -100 -100" />
			<attribute name="Bounding Box Max" value="100 100 100" />
			<attribute name="Ambient Color" value="0.1 0.1 0.1 0" />
			<attribute name="Fog Color" value="0.7 0.9 0.98 1" />
			<attribute name="Fog Start" value="20" />
			<attribute name="Fog End" value="90" />
			<attribute name="Ambient Gradient" value="true" />
		</component>
	</node>
	<node id="16788712">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Suzanne" />
		<attribute name="Position" value="-13.2118 25.4879 58.0358" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777296">
			<attribute name="Model" value="Model;Models/Suzanne.mdl" />
			<attribute name="Material" value="Material;Materials/JoinedMaterial_#1.xml" />
			<attribute name="Can Be Occluded" value="false" />
		</component>
		<component type="RigidBody" id="16777297">
			<attribute name="Physics Position" value="-13.2118 25.4879 58.0358" />
			<attribute name="Mass" value="0.2" />
			<attribute name="Linear Velocity" value="0 -22.89 0" />
		</component>
		<component type="CollisionShape" id="16777298">
			<attribute name="Shape Type" value="TriangleMesh" />
			<attribute name="Model" value="Model;Models/Suzanne.mdl" />
		</component>
	</node>
</scene>[/code]

The XML file is at [sourceforge.net/projects/proteu ... es/Scenes/](https://sourceforge.net/projects/proteusgameengine/files/Existence/Bin/Resources/Scenes/) and the related resources.
Vivienne

-------------------------

vivienneanthony | 2017-01-02 00:59:52 UTC | #2

Screenshoots at

[sourceforge.net/projects/proteu ... creenshot/](https://sourceforge.net/projects/proteusgameengine/files/Existence/screenshot/)

-------------------------

