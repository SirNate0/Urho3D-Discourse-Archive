Firegorilla | 2017-01-02 00:59:50 UTC | #1

Hello,

I was wondering if there is any way to make lighting look more consistent on repeated objects. On this picture [img]http://i.imgur.com/Vt8zaFw.png[/img] you can clearly see where each wall tile begins and ends. Is there any way around it? (ignore the tiles, I fixed that).

Additionally, the walls and windows dont collide with the player in my program, but the floors do, and Im not sure why. Both have correctly placed collision maps, and the floors and walls use the same collision mask (Layer one, mask three, player component is default). I am completely stumped. One thing that may be important is that I have a physics raycaster that reads the node's names and displays them. The window tiles names get displayed, but the walls and floor do not. Here are the object XML files. This also happens when I load wall tiles from the object directly, so I am not sure that it is a level loading issue.

Wall:
[code]<?xml version="1.0"?>
<node id="3">
	<attribute name="Name" value="Wall" />
	<attribute name="Position" value="0 0 0" />
	<attribute name="Rotation" value="1 0 0 0" />
	<attribute name="Scale" value="1 1 1" />
	<attribute name="Variables" />
	<component type="StaticModel" id="7">
		<attribute name="Model" value="Model;Models/Wall.mdl" />
		<attribute name="Material" value="Material;Materials/Wall.xml" />
		<attribute name="Is Occluder" value="true" />
		<attribute name="Can Be Occluded" value="true" />
		<attribute name="Cast Shadows" value="true" />
		<attribute name="Draw Distance" value="0" />
		<attribute name="Shadow Distance" value="0" />
		<attribute name="LOD Bias" value="1" />
		<attribute name="Max Lights" value="0" />
		<attribute name="View Mask" value="-1" />
		<attribute name="Light Mask" value="-1" />
		<attribute name="Shadow Mask" value="-1" />
		<attribute name="Zone Mask" value="-1" />
	</component>
	<component type="CollisionShape" id="8">
		<attribute name="Shape Type" value="Box" />
		<attribute name="Size" value="2 3 0.4" />
		<attribute name="Offset Position" value="0 1.5 0" />
		<attribute name="Offset Rotation" value="1 0 0 0" />
		<attribute name="Collision Margin" value="0.01" />
		<attribute name="Model" value="Model;" />
		<attribute name="LOD Level" value="0" />
	</component>
	<component type="RigidBody" id="9">
		<attribute name="Physics Position" value="0 0 0" />
		<attribute name="Physics Rotation" value="1 0 0 0" />
		<attribute name="Mass" value="0" />
		<attribute name="Friction" value="100" />
		<attribute name="Restitution" value="0" />
		<attribute name="Linear Velocity" value="0 0 0" />
		<attribute name="Angular Velocity" value="0 0 0" />
		<attribute name="Linear Factor" value="1 1 1" />
		<attribute name="Angular Factor" value="1 1 1" />
		<attribute name="Linear Damping" value="0" />
		<attribute name="Angular Damping" value="0" />
		<attribute name="Linear Rest Threshold" value="0.01" />
		<attribute name="Angular Rest Threshold" value="1" />
		<attribute name="Collision Layer" value="1" />
		<attribute name="Collision Mask" value="3" />
		<attribute name="Collision Event Mode" value="When Active" />
		<attribute name="Use Gravity" value="False" />
		<attribute name="Is Kinematic" value="false" />
		<attribute name="Is Trigger" value="false" />
	</component>
</node>
[/code]

Window:
[code]<?xml version="1.0"?>
<node id="3">
	<attribute name="Name" value="WindowFrame" />
	<attribute name="Position" value="0 0 0" />
	<attribute name="Rotation" value="1 0 0 0" />
	<attribute name="Scale" value="1 1 1" />
	<attribute name="Variables" />
	<component type="StaticModel" id="7">
		<attribute name="Model" value="Model;Models/WindowFrame.mdl" />
		<attribute name="Material" value="Material;Materials/WindowFrame.xml" />
		<attribute name="Is Occluder" value="false" />
		<attribute name="Can Be Occluded" value="true" />
		<attribute name="Cast Shadows" value="true" />
		<attribute name="Draw Distance" value="0" />
		<attribute name="Shadow Distance" value="0" />
		<attribute name="LOD Bias" value="1" />
		<attribute name="Max Lights" value="0" />
		<attribute name="View Mask" value="-1" />
		<attribute name="Light Mask" value="-1" />
		<attribute name="Shadow Mask" value="-1" />
		<attribute name="Zone Mask" value="-1" />
	</component>
	<component type="CollisionShape" id="8">
		<attribute name="Shape Type" value="Box" />
		<attribute name="Size" value="2 3 0.4" />
		<attribute name="Offset Position" value="0 1.5 0" />
		<attribute name="Offset Rotation" value="1 0 0 0" />
		<attribute name="Collision Margin" value="0.01" />
		<attribute name="Model" value="Model;" />
		<attribute name="LOD Level" value="0" />
	</component>
	<component type="RigidBody" id="9">
		<attribute name="Physics Position" value="0 0 0" />
		<attribute name="Physics Rotation" value="1 0 0 0" />
		<attribute name="Mass" value="0" />
		<attribute name="Friction" value="0.5" />
		<attribute name="Restitution" value="0" />
		<attribute name="Linear Velocity" value="0 0 0" />
		<attribute name="Angular Velocity" value="0 0 0" />
		<attribute name="Linear Factor" value="1 1 1" />
		<attribute name="Angular Factor" value="1 1 1" />
		<attribute name="Linear Damping" value="0" />
		<attribute name="Angular Damping" value="0" />
		<attribute name="Linear Rest Threshold" value="0.01" />
		<attribute name="Angular Rest Threshold" value="1" />
		<attribute name="Collision Layer" value="2" />
		<attribute name="Collision Mask" value="3" />
		<attribute name="Collision Event Mode" value="When Active" />
		<attribute name="Use Gravity" value="false" />
		<attribute name="Is Kinematic" value="false" />
		<attribute name="Is Trigger" value="false" />
	</component>
	<node id="4">
		<attribute name="Name" value="WindowPane" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="StaticModel" id="7">
			<attribute name="Model" value="Model;Models/WindowPane.mdl" />
			<attribute name="Material" value="Material;Materials/WindowPane.xml" />
			<attribute name="Is Occluder" value="false" />
			<attribute name="Can Be Occluded" value="true" />
			<attribute name="Cast Shadows" value="true" />
			<attribute name="Draw Distance" value="0" />
			<attribute name="Shadow Distance" value="0" />
			<attribute name="LOD Bias" value="1" />
			<attribute name="Max Lights" value="0" />
			<attribute name="View Mask" value="-1" />
			<attribute name="Light Mask" value="-1" />
			<attribute name="Shadow Mask" value="-1" />
			<attribute name="Zone Mask" value="-1" />
		</component>
		<!-- <component type="CollisionShape" id="8">
			<attribute name="Shape Type" value="Box" />
			<attribute name="Size" value="2 3 0.2" />
			<attribute name="Offset Position" value="0 1.5 0" />
			<attribute name="Offset Rotation" value="1 0 0 0" />
			<attribute name="Collision Margin" value="0.01" />
			<attribute name="Model" value="Model;" />
			<attribute name="LOD Level" value="0" />
		</component>
		<component type="RigidBody" id="9">
			<attribute name="Physics Position" value="0 0 0" />
			<attribute name="Physics Rotation" value="1 0 0 0" />
			<attribute name="Mass" value="0.5" />
			<attribute name="Friction" value="0.5" />
			<attribute name="Restitution" value="0" />
			<attribute name="Linear Velocity" value="0 0 0" />
			<attribute name="Angular Velocity" value="0 0 0" />
			<attribute name="Linear Factor" value="1 1 1" />
			<attribute name="Angular Factor" value="1 1 1" />
			<attribute name="Linear Damping" value="0" />
			<attribute name="Angular Damping" value="0" />
			<attribute name="Linear Rest Threshold" value="0.01" />
			<attribute name="Angular Rest Threshold" value="1" />
			<attribute name="Collision Layer" value="2" />
			<attribute name="Collision Mask" value="3" />
			<attribute name="Collision Event Mode" value="When Active" />
			<attribute name="Use Gravity" value="true" />
			<attribute name="Is Kinematic" value="false" />
			<attribute name="Is Trigger" value="false" />
		</component> -->
	</node>
</node>
[/code]

Floor:
[code]<?xml version="1.0"?>
<node id="3">
	<attribute name="Name" value="Floor" />
	<attribute name="Position" value="0 0 0" />
	<attribute name="Rotation" value="1 0 0 0" />
	<attribute name="Scale" value="1 1 1" />
	<attribute name="Variables" />
	<component type="StaticModel" id="7">
		<attribute name="Model" value="Model;Models/Floor.mdl" />
		<attribute name="Material" value="Material;Materials/Floor.xml" />
		<attribute name="Is Occluder" value="true" />
		<attribute name="Can Be Occluded" value="true" />
		<attribute name="Cast Shadows" value="true" />
		<attribute name="Draw Distance" value="0" />
		<attribute name="Shadow Distance" value="0" />
		<attribute name="LOD Bias" value="1" />
		<attribute name="Max Lights" value="0" />
		<attribute name="View Mask" value="-1" />
		<attribute name="Light Mask" value="-1" />
		<attribute name="Shadow Mask" value="-1" />
		<attribute name="Zone Mask" value="-1" />
	</component>
	<component type="CollisionShape" id="8">
		<attribute name="Shape Type" value="Box" />
		<attribute name="Size" value="2 0.2 2" />
		<attribute name="Offset Position" value="0 -0.1 0" />
		<attribute name="Offset Rotation" value="1 0 0 0" />
		<attribute name="Collision Margin" value="0.01" />
		<attribute name="Model" value="Model;" />
		<attribute name="LOD Level" value="0" />
	</component>
	<component type="RigidBody" id="9">
		<attribute name="Physics Position" value="0 0 0" />
		<attribute name="Physics Rotation" value="1 0 0 0" />
		<attribute name="Mass" value="0" />
		<attribute name="Friction" value="100" />
		<attribute name="Restitution" value="0" />
		<attribute name="Linear Velocity" value="0 0 0" />
		<attribute name="Angular Velocity" value="0 0 0" />
		<attribute name="Linear Factor" value="1 1 1" />
		<attribute name="Angular Factor" value="1 1 1" />
		<attribute name="Linear Damping" value="0" />
		<attribute name="Angular Damping" value="0" />
		<attribute name="Linear Rest Threshold" value="0.01" />
		<attribute name="Angular Rest Threshold" value="1" />
		<attribute name="Collision Layer" value="1" />
		<attribute name="Collision Mask" value="3" />
		<attribute name="Collision Event Mode" value="When Active" />
		<attribute name="Use Gravity" value="False" />
		<attribute name="Is Kinematic" value="false" />
		<attribute name="Is Trigger" value="false" />
	</component>
</node>
[/code]

-------------------------

thebluefish | 2017-01-02 00:59:50 UTC | #2

Any chance you could upload the complete scene so that we can check it?

-------------------------

Firegorilla | 2017-01-02 00:59:50 UTC | #3

Sure. I used the scene's savexml function afterwards to see if it makes a difference, but I dont see any. here they are (too large to post directly):
Original: [pastebin.com/fWCxigrT](http://pastebin.com/fWCxigrT)
Resaved: [pastebin.com/k54Qdzqj](http://pastebin.com/k54Qdzqj)

-------------------------

Firegorilla | 2017-01-02 00:59:50 UTC | #4

Ive isolated it to being the mesh. The same lighting issue happens with the same mesh and a different material, but not on a different mesh with the same material. Here is the unconverted file.
[blendswap.com/blends/view/74895](http://www.blendswap.com/blends/view/74895)

-------------------------

AGreatFish | 2017-01-02 00:59:51 UTC | #5

Seems like your normals are off or something.
I would like to see the model, but the blendswap link gives me an error.

-------------------------

Firegorilla | 2017-01-02 00:59:51 UTC | #6

Yeah, they were, sort of. It turns out, I wanted flat shading instead of smooth. My bad. It looks better now.

-------------------------

friesencr | 2017-01-02 00:59:51 UTC | #7

I did the same thing with my tile wall thing.  My seams have really bad aliasing issues.

-------------------------

vivienneanthony | 2017-01-02 00:59:52 UTC | #8

[quote="Firegorilla"]Hello,

I was wondering if there is any way to make lighting look more consistent on repeated objects. On this picture [img]http://i.imgur.com/Vt8zaFw.png[/img] you can clearly see where each wall tile begins and ends. Is there any way around it? (ignore the tiles, I fixed that).

Additionally, the walls and windows dont collide with the player in my program, but the floors do, and Im not sure why. Both have correctly placed collision maps, and the floors and walls use the same collision mask (Layer one, mask three, player component is default). I am completely stumped. One thing that may be important is that I have a physics raycaster that reads the node's names and displays them. The window tiles names get displayed, but the walls and floor do not. Here are the object XML files. This also happens when I load wall tiles from the object directly, so I am not sure that it is a level loading issue.


[/code][/quote]

How did you fix the collisions?

-------------------------

Firegorilla | 2017-01-02 00:59:52 UTC | #9

The collisions werent really an issue. The problem was, I was translating the player component by the node, when I shouldve been using forces/impulses to push the rigidbody. the walls were so thing you could translate to the other side. I also used the settings from the demos, which made it handle better.

-------------------------

vivienneanthony | 2017-01-02 00:59:52 UTC | #10

[quote="Firegorilla"]The collisions werent really an issue. The problem was, I was translating the player component by the node, when I shouldve been using forces/impulses to push the rigidbody. the walls were so thing you could translate to the other side. I also used the settings from the demos, which made it handle better.[/quote]

Ah. I am uploading a video. I have to figure out a better way to texture terrain and also some lighting issues. Working on making a game based of Urho3D and my core code. Tweaking it with Blender, Urho3D editor, and Makehuman so far.

[youtube.com/watch?v=cBzGPRjmOvQ](https://www.youtube.com/watch?v=cBzGPRjmOvQ)

-------------------------

