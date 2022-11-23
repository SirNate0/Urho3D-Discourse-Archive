glebedev | 2018-07-02 14:07:19 UTC | #1

I would like to make a component that takes an animation asset as an input and plays it on the animated model from the same node. It's a pain in the bottom to start all animations from the code. I would prefer to set animations on environment animated object in the editor.

Any cons?

-------------------------

johnnycable | 2018-07-02 18:13:34 UTC | #2

https://discourse.urho3d.io/t/problem-to-load-scene-from-xml-scene-replication/4173/5?u=johnnycable

Basicly you end up with s.t. like this:

    <?xml version="1.0"?>
    <scene id="1">
    	<attribute name="Name" value="" />
    	<attribute name="Time Scale" value="1" />
    	<attribute name="Smoothing Constant" value="50" />
    	<attribute name="Snap Threshold" value="5" />
    	<attribute name="Elapsed Time" value="6.67375" />
    	<attribute name="Next Replicated Node ID" value="15" />
    	<attribute name="Next Replicated Component ID" value="14" />
    	<attribute name="Next Local Node ID" value="16777223" />
    	<attribute name="Next Local Component ID" value="16777228" />
    	<attribute name="Variables" />
    	<attribute name="Variable Names" value="" />
    	<component type="PhysicsWorld" id="1" />
    	<component type="Octree" id="2" />
    	<component type="DebugRenderer" id="3" />
    	<node id="2">
    		<attribute name="Is Enabled" value="true" />
    		<attribute name="Name" value="Zone" />
    		<attribute name="Tags" />
    		<attribute name="Position" value="0 0 0" />
    		<attribute name="Rotation" value="1 0 0 0" />
    		<attribute name="Scale" value="1 1 1" />
    		<attribute name="Variables" />
    		<component type="Zone" id="4">
    			<attribute name="Bounding Box Min" value="-1000 -1000 -1000" />
    			<attribute name="Bounding Box Max" value="1000 1000 1000" />
    			<attribute name="Ambient Color" value="0.25 0.25 0.25 1" />
    		</component>
    	</node>
    	<node id="11">
    		<attribute name="Is Enabled" value="true" />
    		<attribute name="Name" value="Camera" />
    		<attribute name="Tags" />
    		<attribute name="Position" value="7.49446 -6.90148 -4.7805" />
    		<attribute name="Rotation" value="0.782767 -0.482461 -0.211214 0.331504" />
    		<attribute name="Scale" value="1 1 1" />
    		<attribute name="Variables" />
    		<component type="Camera" id="20">
    			<attribute name="Aspect Ratio" value="1.33333" />
    		</component>
    	</node>
    	<node id="3">
    		<attribute name="Is Enabled" value="true" />
    		<attribute name="Name" value="Spot" />
    		<attribute name="Tags" />
    		<attribute name="Position" value="7.48113 -6.50764 -5.34367" />
    		<attribute name="Rotation" value="0.844623 -0.46194 -0.191342 0.191342" />
    		<attribute name="Scale" value="1 1 1" />
    		<attribute name="Variables" />
    		<node id="12">
    			<attribute name="Is Enabled" value="true" />
    			<attribute name="Name" value="LightAdjust" />
    			<attribute name="Tags" />
    			<attribute name="Position" value="0 0 0" />
    			<attribute name="Rotation" value="0.707107 0 0 0" />
    			<attribute name="Scale" value="1 1 1" />
    			<attribute name="Variables" />
    			<component type="Light" id="10">
    				<attribute name="Light Shape Texture" value="TextureCube;" />
    			</component>
    		</node>
    	</node>
    	<node id="4">
    		<attribute name="Is Enabled" value="true" />
    		<attribute name="Name" value="Point" />
    		<attribute name="Tags" />
    		<attribute name="Position" value="0 6 -0" />
    		<attribute name="Rotation" value="1 0 0 0" />
    		<attribute name="Scale" value="1 1 1" />
    		<attribute name="Variables" />
    		<component type="Light" id="11">
    			<attribute name="Light Shape Texture" value="TextureCube;" />
    		</component>
    	</node>
    	<node id="5">
    		<attribute name="Is Enabled" value="true" />
    		<attribute name="Name" value="Sun" />
    		<attribute name="Tags" />
    		<attribute name="Position" value="0 0 -6" />
    		<attribute name="Rotation" value="1 0 0 0" />
    		<attribute name="Scale" value="1 1 1" />
    		<attribute name="Variables" />
    		<node id="13">
    			<attribute name="Is Enabled" value="true" />
    			<attribute name="Name" value="LightAdjust" />
    			<attribute name="Tags" />
    			<attribute name="Position" value="0 0 0" />
    			<attribute name="Rotation" value="-4.37114e-08 0 -1 0" />
    			<attribute name="Scale" value="1 1 1" />
    			<attribute name="Variables" />
    			<component type="Light" id="12">
    				<attribute name="Light Type" value="Directional" />
    			</component>
    		</node>
    	</node>
    	<node id="14">
    		<attribute name="Is Enabled" value="true" />
    		<attribute name="Name" value="Model" />
    		<attribute name="Tags" />
    		<attribute name="Position" value="0 0 0" />
    		<attribute name="Rotation" value="1 0 0 0" />
    		<attribute name="Scale" value="1 1 1" />
    		<attribute name="Variables" />
    		<component type="AnimatedModel" id="13">
    			<attribute name="Model" value="Model;Models/Model.mdl" />
    			<attribute name="Material" value="Material;Materials/Material.xml" />
    			<attribute name="Bone Animation Enabled">
    				<variant type="Bool" value="true" />
    				<variant type="Bool" value="true" />
    				<variant type="Bool" value="true" />
    				<variant type="Bool" value="true" />
    				<variant type="Bool" value="true" />
    				<variant type="Bool" value="true" />
    			</attribute>
    			<attribute name="Animation States">
    				<variant type="Int" value="1" />
    				<variant type="ResourceRef" value="Animation;Models/Armature.ani" />
    				<variant type="String" value="Bone" />
    				<variant type="Bool" value="true" />
    				<variant type="Float" value="1" />
    				<variant type="Float" value="0.6336" />
    				<variant type="Int" value="0" />
    			</attribute>
    		</component>
    		<node id="16777222">
    			<attribute name="Is Enabled" value="true" />
    			<attribute name="Name" value="Bone" />
    			<attribute name="Tags" />
    			<attribute name="Position" value="0 0 -0" />
    			<attribute name="Rotation" value="1 2.18557e-08 -0 0" />
    			<attribute name="Scale" value="1 1 1" />
    			<attribute name="Variables" />
    			<node id="16777221">
    				<attribute name="Is Enabled" value="true" />
    				<attribute name="Name" value="Bone.004" />
    				<attribute name="Tags" />
    				<attribute name="Position" value="0 0.5 -0" />
    				<attribute name="Rotation" value="0.981606 -0 -2.59522e-08 -0.190919" />
    				<attribute name="Scale" value="1 1 1" />
    				<attribute name="Variables" />
    				<node id="16777220">
    					<attribute name="Is Enabled" value="true" />
    					<attribute name="Name" value="Bone.002" />
    					<attribute name="Tags" />
    					<attribute name="Position" value="2.498e-16 0.5 -4.44089e-16" />
    					<attribute name="Rotation" value="1 -2.63201e-17 -1.56121e-17 -7.84399e-25" />
    					<attribute name="Scale" value="1 1 1" />
    					<attribute name="Variables" />
    					<node id="16777219">
    						<attribute name="Is Enabled" value="true" />
    						<attribute name="Name" value="Bone.006" />
    						<attribute name="Tags" />
    						<attribute name="Position" value="-1.31349e-08 0.5 -9.40819e-16" />
    						<attribute name="Rotation" value="1 -2.63201e-17 -1.56121e-17 -7.84399e-25" />
    						<attribute name="Scale" value="1 1 1" />
    						<attribute name="Variables" />
    						<node id="16777218">
    							<attribute name="Is Enabled" value="true" />
    							<attribute name="Name" value="Bone.003" />
    							<attribute name="Tags" />
    							<attribute name="Position" value="2.62697e-08 0.5 -2.16781e-15" />
    							<attribute name="Rotation" value="0.925886 1.74873e-15 -5.13559e-08 -0.377803" />
    							<attribute name="Scale" value="1 1 1" />
    							<attribute name="Variables" />
    							<node id="16777217">
    								<attribute name="Is Enabled" value="true" />
    								<attribute name="Name" value="Bone.007" />
    								<attribute name="Tags" />
    								<attribute name="Position" value="-9.29396e-08 0.5 1.83952e-14" />
    								<attribute name="Rotation" value="1 -5.264e-17 1.0528e-16 1.4018e-08" />
    								<attribute name="Scale" value="1 1 1" />
    								<attribute name="Variables" />
    							</node>
    						</node>
    					</node>
    				</node>
    			</node>
    		</node>
    	</node>
    </scene>

that  you can finally prune to:

    	<node id="14">
    		<attribute name="Is Enabled" value="true" />
    		<attribute name="Name" value="Animation" />
    		<attribute name="Tags" />
    		<attribute name="Position" value="0 0 0" />
    		<attribute name="Rotation" value="1 0 0 0" />
    		<attribute name="Scale" value="1 1 1" />
    		<attribute name="Variables" />
    		<node id="15">
    			<attribute name="Is Enabled" value="true" />
    			<attribute name="Name" value="Model" />
    			<attribute name="Tags" />
    			<attribute name="Position" value="0 0 0" />
    			<attribute name="Rotation" value="1 0 0 0" />
    			<attribute name="Scale" value="1 1 1" />
    			<attribute name="Variables" />
    			<component type="AnimatedModel" id="16">
    				<attribute name="Model" value="Model;Models/Model.mdl" />
    				<attribute name="Material" value="Material;Materials/Material.xml" />
    				<attribute name="Animation States">
    					<variant type="Int" value="0" />
    				</attribute>
    			</component>
    		</node>
    	</node>

and this more or less accounts for a default 'empty' animation scene you can tweak to what you want.
If I'm not mistaken. Did that some time ago...

-------------------------

glebedev | 2018-07-02 20:07:06 UTC | #3

It would be nice to set it up from the editor...

-------------------------

johnnycable | 2018-07-03 11:03:39 UTC | #4

That's what I tried in the beginning. You can dump the scene from the editor in the same way as I described. But I had to let go as I'm on Os X and editor doesn't work... and I had to resort to examples.
Not sure about it, but I think you can load character demo AS example specifically in the editor and do the same...

-------------------------

