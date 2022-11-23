codingmonkey | 2017-01-02 01:06:40 UTC | #1

[url=http://savepic.net/7193448.htm][img]http://savepic.net/7193448m.png[/img][/url]

if you have two objects and both have triangulated colliders
1. plane 
2. box 
collision in this case not working, box are falling through plane
Is this a problem or standard behavior of physics?
i'm do not remember but I guessing what in unity this works property.
there are some options for continues collisions for tiny objects

-------------------------

szamq | 2017-01-02 01:06:40 UTC | #2

Triangle mesh from bullet physics library can be only static, it won't work properly if mass is other than zero. Use convex hull instead

-------------------------

codingmonkey | 2017-01-02 01:06:40 UTC | #3

Oh, thanks  [b]szamq[/b].
I don't knowed about this.

Did you looked on convex hull debug line? it's looked little wierd, no?

-------------------------

sabotage3d | 2017-01-02 01:06:40 UTC | #4

Triangle mesh should work for active objects. Can you provide a simple example scene ?

-------------------------

friesencr | 2017-01-02 01:06:40 UTC | #5

I can't remember if the vertex buffer has to be dynamic for it to work.  My brain is mush.

-------------------------

codingmonkey | 2017-01-02 01:06:40 UTC | #6

>Can you provide a simple example scene ?
The scene is very simple. Floor and box both CollisionShape = TriangleMesh. And if I change type collider for one of them to other it's work fine, but not TriangleMesh with TriangleMesh;

[spoiler][code]
<?xml version="1.0"?>
<scene id="1">
	<attribute name="Name" value="" />
	<attribute name="Time Scale" value="1" />
	<attribute name="Smoothing Constant" value="50" />
	<attribute name="Snap Threshold" value="5" />
	<attribute name="Elapsed Time" value="8.62167" />
	<attribute name="Next Replicated Node ID" value="1" />
	<attribute name="Next Replicated Component ID" value="4" />
	<attribute name="Next Local Node ID" value="16777246" />
	<attribute name="Next Local Component ID" value="16777504" />
	<attribute name="Variables" />
	<attribute name="Variable Names" value="" />
	<component type="Octree" id="1" />
	<component type="DebugRenderer" id="2" />
	<component type="PhysicsWorld" id="3" />
	<node id="16777217">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="ground" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="100 100 100" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777228">
			<attribute name="Model" value="Model;Models/Plane.mdl" />
			<attribute name="Material" value="Material;Materials/Stone.xml" />
		</component>
		<component type="RigidBody" id="16777243" />
		<component type="CollisionShape" id="16777244">
			<attribute name="Shape Type" value="TriangleMesh" />
			<attribute name="Model" value="Model;Models/Plane.mdl" />
		</component>
	</node>
	<node id="16777219">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="playerNode" />
		<attribute name="Position" value="-8.28655e-013 1.04 -1.39907e-006" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="RigidBody" id="16777245">
			<attribute name="Physics Position" value="-8.68875e-013 1.04 -1.38647e-006" />
			<attribute name="Mass" value="1" />
			<attribute name="Angular Factor" value="0 0 0" />
		</component>
		<component type="CollisionShape" id="16777246">
			<attribute name="Shape Type" value="Capsule" />
			<attribute name="Size" value="1 2 1" />
		</component>
		<node id="16777225">
			<attribute name="Is Enabled" value="true" />
			<attribute name="Name" value="cameraNode" />
			<attribute name="Position" value="0 0.238122 0" />
			<attribute name="Rotation" value="1 0 0 0" />
			<attribute name="Scale" value="1 1 1" />
			<attribute name="Variables" />
			<component type="Camera" id="16777272">
				<attribute name="Far Clip" value="110.01" />
				<attribute name="Aspect Ratio" value="1.77778" />
			</component>
		</node>
	</node>
	<node id="16777221">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="lights" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<node id="16777222">
			<attribute name="Is Enabled" value="true" />
			<attribute name="Name" value="light1" />
			<attribute name="Position" value="0 4.33886 0" />
			<attribute name="Rotation" value="1 0 0 0" />
			<attribute name="Scale" value="1 1 1" />
			<attribute name="Variables" />
			<component type="Light" id="16777242">
				<attribute name="Light Shape Texture" value="TextureCube;" />
			</component>
		</node>
	</node>
	<node id="16777228">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="123" />
		<attribute name="Position" value="4.41798 8.34563 4.1454" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777297">
			<attribute name="Model" value="Model;Models/Box.mdl" />
			<attribute name="Material" value="Material;" />
		</component>
		<component type="RigidBody" id="16777298">
			<attribute name="Physics Position" value="4.41798 8.34563 4.1454" />
			<attribute name="Mass" value="1" />
		</component>
		<component type="CollisionShape" id="16777299">
			<attribute name="Shape Type" value="TriangleMesh" />
			<attribute name="Model" value="Model;Models/Box.mdl" />
			<attribute name="LOD Level" value="1" />
		</component>
	</node>
</scene>

[/code][/spoiler]

-------------------------

