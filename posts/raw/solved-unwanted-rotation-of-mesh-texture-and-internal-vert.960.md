vivienneanthony | 2017-01-02 01:04:27 UTC | #1

Hello

1. Do anyone know why I get a weird rotation in a mesh and texture? Check the last photo. [imgur.com/a/kkK5S](http://imgur.com/a/kkK5S)
2. If I wanted to do dust clouds effects like 3:23 in [youtube.com/watch?v=IqD2UImoIGU](https://www.youtube.com/watch?v=IqD2UImoIGU).  Do anyone have any suggestions or examples?

I also took WorldBuild and made it a API to EnvironmentBuild. So technically, environment can be ground or space(possible implementation). I also added about 20 different console commands and wouldn't mind recommendations of more like turning on object name information, octree, and collision highlight. (etc etc)

Vivienne

Diff.xml file for the whole scene (Everything else is procedural generated-I just have the rocks turned off for now) 

[code]
<?xml version="1.0"?>
<scene>

		<node id="11">
			<attribute name="Is Enabled" value="true" />
			<attribute name="Name" value="alienhub1" />
			<attribute name="Position" value="-67.9287 58.7 -101.57" />
			<attribute name="Rotation" value="1 0 0 0" />
			<attribute name="Scale" value="1 1 1" />
			<attribute name="Variables" />
			<component type="StaticModel" id="1038">
				<attribute name="Model" value="Model;Models/alienhub1.mdl" />
				<attribute name="Material" value="Material;Materials/alienhub1surface.xml;Materials/alienhub1ball.xml;Materials/alienhub1grill.xml" />
			</component>
			<component type="RigidBody" id="1039">
				<attribute name="Physics Position" value="-67.9287 58.7 -101.57" />
				<attribute name="Angular Factor" value="0 0 0" />
				<attribute name="Collision Event Mode" value="Always" />
			</component>
			<component type="CollisionShape" id="1040">
				<attribute name="Offset Position" value="5.96046e-07 1.61339 4.76837e-07" />
				<attribute name="LOD Level" value="1" />
			</component>
			<component type="GameObject" id="2090" />
		</node>
		<node id="12">
			<attribute name="Is Enabled" value="true" />
			<attribute name="Name" value="aliencommantenna1" />
			<attribute name="Position" value="27.8524 56.7604 -43.6167" />
			<attribute name="Rotation" value="1 0 0 0" />
			<attribute name="Scale" value="1 1 1" />
			<attribute name="Variables" />
			<component type="StaticModel" id="1041">
				<attribute name="Model" value="Model;Models/aliencommantenna1.mdl" />
				<attribute name="Material" value="Material;Materials/aliencommantenna1antenna.xml;Materials/aliencommantenna1surface.xml" />
				<attribute name="Cast Shadows" value="true" />
			</component>
			<component type="RigidBody" id="1042">
				<attribute name="Physics Position" value="27.8524 56.7604 -43.6167" />
				<attribute name="Angular Factor" value="0 0 0" />
				<attribute name="Collision Event Mode" value="Always" />
			</component>
			<component type="CollisionShape" id="1043">
				<attribute name="Shape Type" value="TriangleMesh" />
				<attribute name="Model" value="Model;Models/aliencommantenna1.mdl" />
				<attribute name="LOD Level" value="1" />
			</component>
			<component type="GameObject" id="1044" />
			<component type="GameObject" id="2091" />
		</node>
		<node id="13">
			<attribute name="Is Enabled" value="true" />
			<attribute name="Name" value="aliencommantenna3" />
			<attribute name="Position" value="8.96581 70.1164 -105.302" />
			<attribute name="Rotation" value="1 0 0 0" />
			<attribute name="Scale" value="1 1 1" />
			<attribute name="Variables" />
			<component type="StaticModel" id="1045">
				<attribute name="Model" value="Model;Models/aliencommantenna1.mdl" />
				<attribute name="Material" value="Material;Materials/aliencommantenna1antenna.xml;Materials/aliencommantenna1surface.xml" />
				<attribute name="Cast Shadows" value="true" />
			</component>
			<component type="RigidBody" id="1046">
				<attribute name="Physics Position" value="8.96581 70.1164 -105.302" />
				<attribute name="Angular Factor" value="0 0 0" />
				<attribute name="Collision Event Mode" value="Always" />
			</component>
			<component type="CollisionShape" id="1047">
				<attribute name="Shape Type" value="TriangleMesh" />
				<attribute name="Model" value="Model;Models/aliencommantenna1.mdl" />
				<attribute name="LOD Level" value="1" />
			</component>
			<component type="GameObject" id="1048" />
			<component type="GameObject" id="2092" />
		</node>
		<node id="14">
			<attribute name="Is Enabled" value="true" />
			<attribute name="Name" value="aliencommantenna2" />
			<attribute name="Position" value="16.6735 67.8509 -83.9448" />
			<attribute name="Rotation" value="1 0 0 0" />
			<attribute name="Scale" value="1 1 1" />
			<attribute name="Variables" />
			<component type="StaticModel" id="1049">
				<attribute name="Model" value="Model;Models/aliencommantenna1.mdl" />
				<attribute name="Material" value="Material;Materials/aliencommantenna1antenna.xml;Materials/aliencommantenna1surface.xml" />
				<attribute name="Cast Shadows" value="true" />
			</component>
			<component type="RigidBody" id="1050">
				<attribute name="Physics Position" value="16.6735 67.8509 -83.9448" />
				<attribute name="Angular Factor" value="0 0 0" />
				<attribute name="Collision Event Mode" value="Always" />
			</component>
			<component type="CollisionShape" id="1051">
				<attribute name="Shape Type" value="TriangleMesh" />
				<attribute name="Model" value="Model;Models/aliencommantenna1.mdl" />
				<attribute name="LOD Level" value="1" />
			</component>
			<component type="GameObject" id="1052" />
			<component type="GameObject" id="2093" />
		</node>
		<node id="15">
			<attribute name="Is Enabled" value="true" />
			<attribute name="Name" value="aliencommantenna6" />
			<attribute name="Position" value="-28.0511 57.85 -118.615" />
			<attribute name="Rotation" value="1 0 0 0" />
			<attribute name="Scale" value="1 1 1" />
			<attribute name="Variables" />
			<component type="StaticModel" id="1053">
				<attribute name="Model" value="Model;Models/aliencommantenna1.mdl" />
				<attribute name="Material" value="Material;Materials/aliencommantenna1antenna.xml;Materials/aliencommantenna1surface.xml" />
				<attribute name="Cast Shadows" value="true" />
			</component>
			<component type="RigidBody" id="1054">
				<attribute name="Physics Position" value="-28.0511 57.85 -118.615" />
				<attribute name="Angular Factor" value="0 0 0" />
				<attribute name="Collision Event Mode" value="Always" />
			</component>
			<component type="CollisionShape" id="1055">
				<attribute name="Shape Type" value="TriangleMesh" />
				<attribute name="Model" value="Model;Models/aliencommantenna1.mdl" />
				<attribute name="LOD Level" value="1" />
			</component>
			<component type="GameObject" id="1056" />
			<component type="GameObject" id="2094" />
		</node>

	<node id="18">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="randomnacelle1" />
		<attribute name="Position" value="-259.144 24 55.4767" />
		<attribute name="Rotation" value="0 -0.2 0.5 -0.2" />
		<attribute name="Scale" value="10 10 10" />
		<attribute name="Variables" />
		<component type="StaticModel" id="2107">
			<attribute name="Model" value="Model;Models/randomnacelle1.mdl" />
			<attribute name="Material" value="Material;Materials/RandomNacelle1Surface2.xml;Materials/RandomNacelle1Surface1.xml;Materials/RandomNacelle1Glass.xml;Materials/RandomNacelle1WarpCore.xml;Materials/RandomNacelle1Metal1.xml;Materials/RandomNacelle1Bussard2.xml;Materials/RandomNacelle1Bussard1.xml" />
			<attribute name="Cast Shadows" value="true" />
		</component>
		<component type="RigidBody" id="2108">
			<attribute name="Physics Rotation" value="0 -0.348155 0.870388 -0.348155" />
			<attribute name="Physics Position" value="-259.144 24 55.4767" />
			<attribute name="Angular Factor" value="0 0 0" />
			<attribute name="Collision Event Mode" value="Always" />
		</component>
		<component type="CollisionShape" id="2109">
			<attribute name="Shape Type" value="ConvexHull" />
			<attribute name="Model" value="Model;Models/randomnacelle1.mdl" />
			<attribute name="LOD Level" value="1" />
		</component>
		<component type="GameObject" id="2110" />
	</node>
</scene>[/code]

-------------------------

vivienneanthony | 2017-01-02 01:04:28 UTC | #2

I think I sorted the problem. Somehow when adding a object. It creates a node with the model and components with a node above it. I think.

How can I force a node to be created in the scene under root? Also should I set the scene root as the parent with set parent?

-------------------------

