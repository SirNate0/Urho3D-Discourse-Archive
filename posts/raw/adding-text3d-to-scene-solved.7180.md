csteaderman | 2022-02-01 19:20:17 UTC | #1

I am new to Urho3D, and 3D rendering in general. I am developing in UrhoSharp, although I don't believe that is my issue.

I have an existing scene, exported from Blender, to which I would like to add some text. I am unable to get the text to show up, no matter what I try.

So I took a step backward and am not trying to add a Text3D element to a scene using the Urho3D Editor. I am still unable to get the text to display. I assume that I am missing something very obvious, but of course I don't know what it is. I figure once I am able to display text via the Editor, I will be able to replicate this in my code.

Here is my most basic scene with a Light and Text3D. Please help me figure out how to get text display.

```
<?xml version="1.0"?>
<scene id="1">
	<attribute name="Name" value="" />
	<attribute name="Time Scale" value="1" />
	<attribute name="Smoothing Constant" value="50" />
	<attribute name="Snap Threshold" value="5" />
	<attribute name="Elapsed Time" value="0" />
	<attribute name="Next Replicated Node ID" value="1" />
	<attribute name="Next Replicated Component ID" value="6" />
	<attribute name="Next Local Node ID" value="16777218" />
	<attribute name="Next Local Component ID" value="16777240" />
	<attribute name="Variables" />
	<attribute name="Variable Names" value="" />
	<component type="Octree" id="1" />
	<component type="DebugRenderer" id="2" />
	<component type="Light" id="3">
		<attribute name="Light Type" value="Directional" />
	</component>
	<component type="Text3D" id="5">
		<attribute name="Font Size" value="120" />
		<attribute name="Text" value="Hello World!" />
		<attribute name="Color" value="0.5 0.5 0.5 0.5" />
		<attribute name="Top Left Color" value="0.5 0.5 0.5 0.5" />
		<attribute name="Top Right Color" value="0.5 0.5 0.5 0.5" />
		<attribute name="Bottom Left Color" value="0.5 0.5 0.5 0.5" />
		<attribute name="Bottom Right Color" value="0.5 0.5 0.5 0.5" />
		<attribute name="Stroke Thickness" value="10" />
	</component>
</scene>
```

Thanks,
Charlie

-------------------------

Eugene | 2022-02-01 18:20:41 UTC | #2

[quote="csteaderman, post:1, topic:7180"]
I assume that I am missing something very obvious,
[/quote]
Maybe the font itself?

-------------------------

SirNate0 | 2022-02-01 18:38:39 UTC | #3

Also try adding it to a node added to the scene. I'm not certain that drawables attached to the scene itself get drawn. (Or maybe they just don't have a transform or something, I forget exactly what the limitation is).

-------------------------

csteaderman | 2022-02-01 19:19:32 UTC | #4

Yes, that is the obvious think that I was missing! I made the assumption that a default font might be used in the absence of a specific font reference. Clearly my bad.

-------------------------

