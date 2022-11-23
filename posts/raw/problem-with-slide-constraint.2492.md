l19g2004 | 2017-01-02 01:15:47 UTC | #1

Hi guys,

i have a problem with some physical constraint between two rigid bodies. I have two boxes and one is above the other one. With gravity they fall down so far. Now i want to keep the distance between them in a specific range. In order to do this, i used the constraint entity to define this range between the rigid bodies. But in action, they get total out go control. I tried to change the rotations of the constrains but it does not help. 
Do you have some hints ?

Here is my scene:
[code]<?xml version="1.0"?>
<scene id="1">
	<attribute name="Name" value="" />
	<attribute name="Time Scale" value="1" />
	<attribute name="Smoothing Constant" value="50" />
	<attribute name="Snap Threshold" value="5" />
	<attribute name="Elapsed Time" value="391.392" />
	<attribute name="Next Replicated Node ID" value="1" />
	<attribute name="Next Replicated Component ID" value="7" />
	<attribute name="Next Local Node ID" value="16777229" />
	<attribute name="Next Local Component ID" value="16777326" />
	<attribute name="Variables" />
	<attribute name="Variable Names" value="" />
	<component type="Octree" id="1" />
	<component type="DebugRenderer" id="2" />
	<component type="PhysicsWorld" id="3" />
	<node id="16777217">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Top" />
		<attribute name="Tags" />
		<attribute name="Position" value="0 5 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777228">
			<attribute name="Model" value="Model;Models/Box.mdl" />
			<attribute name="Material" value="Material;Materials/Stone.xml" />
		</component>
		<component type="RigidBody" id="16777243">
			<attribute name="Physics Position" value="0 5 0" />
			<attribute name="Mass" value="1" />
			<attribute name="Linear Velocity" value="59.1207 -25.2133 -5.82021" />
			<attribute name="Angular Velocity" value="-3.99654 11.7038 53.2007" />
		</component>
		<component type="CollisionShape" id="16777274" />
		<component type="Constraint" id="16777277">
			<attribute name="Constraint Type" value="Slider" />
			<attribute name="Other Body Rotation" value="0.707107 0 0 0.707107" />
			<attribute name="Other Body NodeID" value="16777219" />
			<attribute name="High Limit" value="2 0" />
			<attribute name="Low Limit" value="-1 0" />
		</component>
	</node>
	<node id="16777219">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Down" />
		<attribute name="Tags" />
		<attribute name="Position" value="0 2 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777229">
			<attribute name="Model" value="Model;Models/Box.mdl" />
			<attribute name="Material" value="Material;Materials/Stone.xml" />
		</component>
		<component type="RigidBody" id="16777244">
			<attribute name="Physics Position" value="0 2 0" />
			<attribute name="Mass" value="1" />
		</component>
		<component type="CollisionShape" id="16777275" />
	</node>
	<node id="16777222">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Floor" />
		<attribute name="Tags" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="100 1 100" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777258">
			<attribute name="Model" value="Model;Models/Plane.mdl" />
			<attribute name="Material" value="Material;" />
		</component>
		<component type="RigidBody" id="16777259" />
		<component type="CollisionShape" id="16777276">
			<attribute name="Offset Position" value="0 -0.5 0" />
		</component>
	</node>
	<node id="16777223">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Light" />
		<attribute name="Tags" />
		<attribute name="Position" value="4 10 5" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="Light" id="16777260">
			<attribute name="Light Shape Texture" value="TextureCube;" />
			<attribute name="Cast Shadows" value="true" />
		</component>
	</node>
</scene>
[/code]

Best regards

-------------------------

Lumak | 2017-01-02 01:15:48 UTC | #2

I tested your scene, and after clearing out the linear and angular velocities that were set in your scene and other minor tweaks to just stabilize it, I have a sliding functionality.

[spoiler][code]
<?xml version="1.0"?>
<scene id="1">
	<attribute name="Name" value="" />
	<attribute name="Time Scale" value="1" />
	<attribute name="Smoothing Constant" value="50" />
	<attribute name="Snap Threshold" value="5" />
	<attribute name="Elapsed Time" value="26.954" />
	<attribute name="Next Replicated Node ID" value="1" />
	<attribute name="Next Replicated Component ID" value="7" />
	<attribute name="Next Local Node ID" value="16777230" />
	<attribute name="Next Local Component ID" value="16777338" />
	<attribute name="Variables" />
	<attribute name="Variable Names" value="" />
	<component type="Octree" id="1" />
	<component type="DebugRenderer" id="2" />
	<component type="PhysicsWorld" id="3" />
	<node id="16777217">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Top" />
		<attribute name="Tags" />
		<attribute name="Position" value="3.3088 2 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777228">
			<attribute name="Model" value="Model;Models/Box.mdl" />
			<attribute name="Material" value="Material;Materials/Stone.xml" />
		</component>
		<component type="RigidBody" id="16777243">
			<attribute name="Physics Position" value="3.31132 2 0" />
			<attribute name="Mass" value="1" />
			<attribute name="Linear Velocity" value="0.198712 -5.72205e-006 0" />
			<attribute name="Angular Factor" value="0 0 0" />
		</component>
		<component type="CollisionShape" id="16777274" />
		<component type="Constraint" id="16777277">
			<attribute name="Constraint Type" value="Slider" />
			<attribute name="Other Body NodeID" value="16777219" />
			<attribute name="High Limit" value="12 0" />
			<attribute name="Low Limit" value="3 0" />
		</component>
	</node>
	<node id="16777219">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Down" />
		<attribute name="Tags" />
		<attribute name="Position" value="0 2 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777229">
			<attribute name="Model" value="Model;Models/Box.mdl" />
			<attribute name="Material" value="Material;Materials/Stone.xml" />
		</component>
		<component type="RigidBody" id="16777244">
			<attribute name="Physics Position" value="0 2 0" />
		</component>
		<component type="CollisionShape" id="16777275" />
	</node>
	<node id="16777222">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Floor" />
		<attribute name="Tags" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="100 1 100" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777258">
			<attribute name="Model" value="Model;Models/Plane.mdl" />
			<attribute name="Material" value="Material;" />
		</component>
		<component type="RigidBody" id="16777259" />
		<component type="CollisionShape" id="16777276">
			<attribute name="Offset Position" value="0 -0.5 0" />
		</component>
	</node>
	<node id="16777223">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Light" />
		<attribute name="Tags" />
		<attribute name="Position" value="4 10 5" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="Light" id="16777260">
			<attribute name="Range" value="20" />
			<attribute name="Light Shape Texture" value="TextureCube;" />
			<attribute name="Cast Shadows" value="true" />
		</component>
	</node>
</scene>
[/code][/spoiler]

Move the box that's on the right towards the one on the left and you should see it repel (slide) away from it.  
I've looked at the Urho3d/Physics/Constraint.cpp and then looked at btSliderConstraint.cpp, and I'd say you'll need to access the methods defined in btSliderConstraint.h to get a full access to the slider feature.
Good luck.

-------------------------

