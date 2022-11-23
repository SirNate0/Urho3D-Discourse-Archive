Xero | 2017-01-02 00:58:36 UTC | #1

I am not able to light my whole scene. My scene's size is 60k x 60k in size I have a single point light with a light zone. In the editor my scene is completely lit but when loaded into my project it is not. I get black edges around the plane. Any ideas on how to fix this?

-------------------------

cadaver | 2017-01-02 00:58:37 UTC | #2

The obvious issue would be if your zone is not large enough to contain the whole scene; the ambient light outside any zone (default zone) is configurable in editor, but when running a standalone application, the initial value for the default zone's (Renderer::GetDefaultZone()) ambient light level is almost black.

If it's not that, can you share your scene, or some approximation of it (don't need to share the actual assets if you don't want to do that) that reproduces the bug?

-------------------------

Xero | 2017-01-02 00:58:37 UTC | #3

here is just a basic scene that replicates my issue, i have a very large lightzone:

[code]
<?xml version="1.0"?>
<scene id="1">
	<attribute name="Name" value="" />
	<attribute name="Time Scale" value="1" />
	<attribute name="Smoothing Constant" value="50" />
	<attribute name="Snap Threshold" value="5" />
	<attribute name="Elapsed Time" value="6762.51" />
	<attribute name="Next Replicated Node ID" value="427" />
	<attribute name="Next Replicated Component ID" value="66515" />
	<attribute name="Next Local Node ID" value="16842545" />
	<attribute name="Next Local Component ID" value="16777300" />
	<attribute name="Variables" />
	<attribute name="Variable Names" value="" />
	<component type="Octree" id="1" />
	<component type="PhysicsWorld" id="2" />
	<component type="DebugRenderer" id="3" />
	<node id="16818715">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="underwaterplane" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777262">
			<attribute name="Model" value="Model;Models/plane_test.mdl" />
			<attribute name="Material" value="Material;Materials/plane.xml" />
		</component>
	</node>
	<node id="16818717">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Skybox" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="Skybox" id="16777263">
			<attribute name="Model" value="Model;Models/Box.mdl" />
			<attribute name="Material" value="Material;Materials/Sky.xml" />
		</component>
	</node>
	<node id="16825636">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Light" />
		<attribute name="Position" value="0 1526.35 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="10 10 10" />
		<attribute name="Variables" />
		<component type="Light" id="16777274">
			<attribute name="Specular Intensity" value="0" />
			<attribute name="Range" value="99999" />
			<attribute name="Light Shape Texture" value="TextureCube;" />
			<attribute name="Shadow Intensity" value="0.3" />
			<attribute name="CSM Splits" value="1000 10 50 200" />
		</component>
		<component type="Zone" id="16777275">
			<attribute name="Bounding Box Min" value="-700000 -250000 -700000" />
			<attribute name="Bounding Box Max" value="700000 250000 700000" />
			<attribute name="Fog Start" value="0.1" />
			<attribute name="Fog End" value="100000" />
		</component>
	</node>
	<node id="16793358">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="WaterPlane" />
		<attribute name="Position" value="0 16 6.63495" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="60000 1 60000" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777247">
			<attribute name="Model" value="Model;Models/plane.mdl" />
			<attribute name="Material" value="Material;Materials/Water.xml" />
		</component>
	</node>
</scene>
[/code]
Just a note plane_test.mdl comes from an fbx file i made it is already scaled up to 60k by 60k

-------------------------

cadaver | 2017-01-02 00:58:37 UTC | #4

I don't see the scene behaving differently in editor and when loading it in the StaticScene sample & moving around. I used a camera farclip of 10000. The zone size should be fine.

That said, if the world unit is supposed to represent 1 meter, as in the Urho samples, you will run into float imprecision issues. If you want to construct a large world, you should make it in pieces (for example 1k x 1k), unload / load those pieces as you move around, and keep the visible world centered around the world origin (which means you'll have to "shift" the pieces when moving). See for example [forum.unity3d.com/threads/224509 ... -precision](http://forum.unity3d.com/threads/224509-large-world-floating-precision)

Also, to light a large scene in an uniform manner, a directional light may be more appropriate.

-------------------------

Xero | 2017-01-02 00:58:40 UTC | #5

so i figured out the solution to my problem. the issue was the far clip was too small so i increased it and it works

-------------------------

