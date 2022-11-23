gabdab | 2017-01-02 01:06:27 UTC | #1

I can't get it to read xml scenes written on a text editor instead of exported by Editor.sh .
Is it a matter of indentation , end of lines symbol or else ?
Example :
[code]<?xml version="1.0"?>
<scene id="1">
	<attribute name="Name" value="" />
	<attribute name="Time Scale" value="1" />
	<attribute name="Smoothing Constant" value="50" />
	<attribute name="Snap Threshold" value="5" />
	<attribute name="Elapsed Time" value="0" />
	<attribute name="Next Replicated Node ID" value="1" />
	<attribute name="Next Replicated Component ID" value="3" />
	<attribute name="Next Local Node ID" value="16777217" />
	<attribute name="Next Local Component ID" value="16777217" />
	<attribute name="Variables" />
	<attribute name="Variable Names" value="" />
	<component type="Octree" id="1" />
	<component type="DebugRenderer" id="2" />
	<node id="16777216">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="" />
		<attribute name="Position" value="-466.80 19.97 485.52" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="0.33 0.57 0.33" />
		<attribute name="Variables" />
		<component type="StaticModel"id="16777216" />
			<attribute name="Model"value="Model;Models/test/Cone_062.mdl" />
			<attribute name="Material"value="Material;Materials/test/Grass.xml" />
		</component>
	</node>
</scene>[/code]

-------------------------

cadaver | 2017-01-02 01:06:27 UTC | #2

Indentation shouldn't be an issue, but your component has invalid XML syntax (early terminated element, even though there are elements inside, no space between attributes)

When edited to the following, it should load:

[code]
      <component type="StaticModel" id="16777216">
         <attribute name="Model" value="Model;Models/test/Cone_062.mdl" />
         <attribute name="Material" value="Material;Materials/test/Grass.xml" />
      </component>
[/code]

-------------------------

gabdab | 2017-01-02 01:06:27 UTC | #3

It works now , thanks .

-------------------------

