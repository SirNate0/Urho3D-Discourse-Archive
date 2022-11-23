btschumy | 2020-06-16 21:07:38 UTC | #1

I am making slow progress moving an app I have written using Apple's SceneKit to Urho3D.

I'm having problems getting particle systems to do the same thing in Urho3D as I do in SceneKit.

The app is a visualization of our galaxy.  I use particle systems for the galactic bulge and the stars and duct that make up the disk.

This movie shows what the app looks like in SceneKit. 
http://www.otherwise.com/movies/OurGalaxy.mov

This shows where I'm currently at in Urho3D. 
http://www.otherwise.com/movies/OurGalaxyX.mov

I have several concerns (I can include any code upon request):

1. I don't seem to be able to change the color or alpha of the particle system.  In the SceneKit version I change these thing subtly on the fly as you pan around.  As far as I can tell the ParticleEffect class doesn't have a color property (although the documentation implies it does).

<particleemitter>
    <material name="MaterialName" />
    <updateinvisible enable="true|false" />
    <relative enable="true|false" />
    <scaled enable="true|false" />
    <sorted enable="true|false" />
    <emittertype value="sphere|box" />
    <emittersize value="x y z" />
    <emitterradius value="x" />
    <direction min="x1 y1 z1" max="x2 y2 z2" />
    <constantforce value="x y z" />
    <dampingforce value="x" />
    <activetime value="t" />
    <inactivetime value="t" />
    <interval min="t1" max="t2" />
    <emissionrate min="t1" max="t2" />
    <particlesize min="x1 y1" max="x2 y2" />
    <timetolive min="t1" max="t2" />
    <velocity min="x1" max="x2" />
    <rotation min="x1" max="x2" />
    <rotationspeed min="x1" max="x2" />
    <sizedelta add="x" mul="y" />
    <color value="r g b a" />
    <colorfade color="r g b a" time="t" />
    <texanim uv="u1 v1 u2 v2" time="t" />
</particleemitter>

I've tried setting the "color" tag in the xml, but it has no effect.  If this worked, I could change the color and alpha as needed.

2. If you look at the Urho3D movie, obviously there is something wrong with the drawing order or the merging of the galaxy node and the bulge particle system.  Any thoughts on that?

3. I also need to be able to change the alpha of the galaxy node on the fly.  Is that possible?

-------------------------

btschumy | 2020-06-16 22:31:33 UTC | #2

I did make progress on getting the coloring of the particle system working.  If I use DiffUnlitParticleAlpha.xml as the technique, then the color is used and I can get something close to what I need.  

I am still having problems with the particles flickering in and out as I pan around.  Sometimes the PS is drawn fully behind the galaxy node and sometimes fully in front of it.  Any thoughts on how to fix?  Both node are using the default drawing order.

-------------------------

Pencheff | 2020-06-16 22:35:46 UTC | #3

You can change the render order of the galaxy's material to be always on top of other objects  - https://discourse.urho3d.io/t/how-to-control-render-order/1240/4?u=pencheff

-------------------------

btschumy | 2020-06-17 13:56:42 UTC | #4

I don't want them to be always "on top" or "behind".  The galactic bulge is embedded in the disk of the galaxy.  Some parts need to be rendered in from and other parts behind.  I assume that if this were not a particle system, but say a textured ovoid, the two would be rendered correctly.  I will do that test in a bit to see.

-------------------------

btschumy | 2020-06-17 14:47:07 UTC | #5

Well, I'm not even able to get a solid object to display correctly.  Here is the galaxyNode's material.

    <?xml version="1.0"?>
    <material>
        <technique name="Techniques/DiffUnlitAlpha.xml" />
    	<texture unit="diffuse" name="Textures/Galaxy-North.dds" />
        <cull value = "none"/>
    </material>

Here is the galacticBulge's material:

    <?xml version="1.0" encoding="UTF-8" ?>
    <material>
        <technique name="Techniques/DiffUnlit.xml" />
        <texture unit="diffuse" name="Textures/SolidColor.jpg" />
        <cull value = "none"/>
    </material>
             
I am not using a particle system here and just want to see if I can display a sphere embedded in the disk of the galaxy.  The sphere flickers with various parts either being drawn or not as I pan the view around.

Surely there is some secret sauce to make this work.  Can anyone help?

Thanks.

-------------------------

SirNate0 | 2020-06-17 16:10:05 UTC | #6

It's a problem with using transparency. When it renders, whichever one is closer to the camera will render first (based on the origin of the nose, I think), so when they overlap like you suggested one ends up in front of the other. If you need some particles in front and some behind I would suggest just having two particle emitters, one with a higher priority than the Galaxy and one with a lower priority. The other option I can think of that might work is to make every single particle have it's own node, but that would probably be a lot slower. For your sphere, you can probably just force it to be drawn after the Galaxy and have the Galaxy write to the depth buffer (I don't remember whether transparent materials do that by default or not - I think maybe the alpha mask ones do but there normal ones don't).

-------------------------

btschumy | 2020-06-17 16:56:15 UTC | #7

Thanks for continuing to help me.

Even using a material without transparency, the sphere bisected by a plane doesn't draw correctly.  In some orientations the sphere disappears completely even though half is in front of the plane.

I an using this material for both plane and sphere:

<?xml version="1.0" encoding="UTF-8" ?>
<material>
    <technique name="Techniques/DiffUnlit.xml" />
    <texture unit="diffuse" name="Textures/SolidColor.jpg" />
    <cull value = "none"/>
</material>

I will try different Techniques, but I've tried a few already and none seem to work,

I'm obviously not a 3D game programmer, just a scientist.  Should this be that difficult?

How do you have the galaxy (or plane) write to the depth buffer?

Thanks.

-------------------------

SirNate0 | 2020-06-17 21:53:37 UTC | #8

Is the plane set as an occluder or something? (Which may or may not cause your problem, but in any case) I don't think what you describe should be happening. But also, I'm not sure that a completely empty material will actually do what you want (it may, but I'm not certain). In any case, when I tried with the following setup it worked fine, the sphere was always visible where it was in front of the plane and not visible where it was behind it.

*Materials/Unlit.xml*
```
<?xml version="1.0"?>
<material>
	<technique name="Techniques/NoTextureUnlit.xml" quality="0" loddistance="0" />
	<parameter name="UOffset" value="1 0 0 0" />
	<parameter name="VOffset" value="0 1 0 0" />
	<parameter name="MatDiffColor" value="0.2 0.5 1 1" />
	<parameter name="MatEmissiveColor" value="0 0 0" />
	<parameter name="MatEnvMapColor" value="1 1 1" />
	<parameter name="MatSpecColor" value="0 0 0 1" />
	<parameter name="Roughness" value="0.5" />
	<parameter name="Metallic" value="0" />
	<cull value="none" />
	<shadowcull value="none" />
	<fill value="solid" />
	<depthbias constant="0" slopescaled="0" />
	<alphatocoverage enable="false" />
	<lineantialias enable="false" />
	<renderorder value="128" />
	<occlusion enable="false" />
</material>
```

*Materials/Unlit2.xml*
```
<?xml version="1.0"?>
<material>
	<technique name="Techniques/NoTextureUnlit.xml" quality="0" loddistance="0" />
	<parameter name="UOffset" value="1 0 0 0" />
	<parameter name="VOffset" value="0 1 0 0" />
	<parameter name="MatDiffColor" value="1 0.5 0 1" />
	<parameter name="MatEmissiveColor" value="0 0 0" />
	<parameter name="MatEnvMapColor" value="1 1 1" />
	<parameter name="MatSpecColor" value="0 0 0 1" />
	<parameter name="Roughness" value="0.5" />
	<parameter name="Metallic" value="0" />
	<cull value="none" />
	<shadowcull value="none" />
	<fill value="solid" />
	<depthbias constant="0" slopescaled="0" />
	<alphatocoverage enable="false" />
	<lineantialias enable="false" />
	<renderorder value="128" />
	<occlusion enable="false" />
</material>
```

*Scene.xml*
```
<?xml version="1.0"?>
<scene id="1">
	<attribute name="Name" value="" />
	<attribute name="Time Scale" value="1" />
	<attribute name="Smoothing Constant" value="50" />
	<attribute name="Snap Threshold" value="5" />
	<attribute name="Elapsed Time" value="0" />
	<attribute name="Next Replicated Node ID" value="5" />
	<attribute name="Next Replicated Component ID" value="6" />
	<attribute name="Next Local Node ID" value="16777217" />
	<attribute name="Next Local Component ID" value="16777228" />
	<attribute name="Variables" />
	<attribute name="Variable Names" value="" />
	<component type="Octree" id="1" />
	<component type="DebugRenderer" id="2" />
	<node id="2">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="" />
		<attribute name="Tags" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="AnimatedModel" id="3">
			<attribute name="Model" value="Model;Models/Sphere.mdl" />
			<attribute name="Material" value="Material;Materials/Unlit.xml" />
			<attribute name="Animation States">
				<variant type="Int" value="0" />
			</attribute>
		</component>
	</node>
	<node id="3">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="" />
		<attribute name="Tags" />
		<attribute name="Position" value="0 3.35477 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="Light" id="4">
			<attribute name="Light Type" value="Directional" />
		</component>
	</node>
	<node id="4">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="" />
		<attribute name="Tags" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="10 10 10" />
		<attribute name="Variables" />
		<component type="StaticModel" id="5">
			<attribute name="Model" value="Model;Models/Plane.mdl" />
			<attribute name="Material" value="Material;Materials/Unlit2.xml" />
		</component>
	</node>
</scene>
```

-------------------------

btschumy | 2020-06-17 22:22:32 UTC | #9

I'll look at what you did tomorrow and see if I can use it.

I did get it working with a solid sphere embedded in the plane.  Turns out most of my issues were do to using the iPhone simulator rather than a real device.  I installed it on a real device in order to make a screen recording, and to my surprise it worked there.  On the simulator, chunks of the sphere would come and go as I viewer the scene from different perspectives.  

I still don't have it working with an actual particle system, but maybe I'll get it figure out tomorrow.  The particles are sometimes drawn with the transparent part as black and sometimes transparent, depending on the orientation.

-------------------------

btschumy | 2020-06-18 16:46:43 UTC | #10

I think I'm getting close.  It is the case that I need to turn on "depthwrite" for the galaxy image and turn it off for the particle system.  If I turn on "depthwrite" for the PS, the clear parts are drawn black in some orientations.

SirNate0 was correct that there is a problem with having part of the particle system above the plane and part below.  With that configuration the particle system flickers in and out depending on the orientation.  If I move the PS to be totally above the plane then it works in all orientations.

I would show my Techniques and ParticleEffects but using Preformatted Text doesn't seem to work.  The xml disappears in the rendered message.  SirNate, how do you do that?

So now the question is how to split the particle system with half above the galaxy and half below.  I need a dome shape and the only shapes for the emitter is sphere or box.

I don't really understand the emittersize and emitterradius elements in the particle effect file.  I have changed them to various values but they have no effect.  Right now I'm using a sphere and in the node I've attached the emitter to is scaled to make it ovoid (although it is not perfect).

Is there any way to get more control of the shape of the particle system?  How do I get half above and half below?

Here is what is is looking like currently:
www.otherwise.com/images/GalaxyX_Bulge.jpg

-------------------------

SirNate0 | 2020-06-18 18:37:22 UTC | #11

To get the xml to show use three backticks (\`\`\`) on either side of the code (line before and line after, or just one backtick to the left and right to do it \``inline`\`, and use a backslash \ before the \` to actually write backticks). Some sites also allow specifying the type of code for syntax highlighting by putting a label at the very start after the backticks (e.g. \`\`\`cpp for c++code). 

My suggestion to get it to appear in both sides would be too have one PS sphere rendered before the galaxy (not writing to the depth buffer). Then render the galaxy (if it's transparent you should then see some particles "behind" it). The Galaxy will write to the depth buffer (maybe using an alpha mask to get an oval shape). Lastly, render another sphere PS over the galaxy, testing against but not writing to the depth buffer to get the hemisphere "over" the galaxy.

There may be more ways to control the particle system (I think someone came up with code to use model vertices as an emitter), but over all I would describe Urho's particle system as pretty minimally featured. You may want to look into the integrations of the Spark particle engine, which may have more features.

-------------------------

btschumy | 2020-06-18 22:20:41 UTC | #12

Nate,

Thanks again for the help.  It looks like it just works if you set the RenderOrder to draw the bulge particle system after the galaxy.  The galaxy is writing to the depth buffer but the PS doesn't.  I don't seem to need the two particle systems, but maybe I'll find a flaw in this later.

Here is what I have:
http://www.otherwise.com/movies/OurGalaxyX_2.mov

 The bulge is a bit too much shaped like a capsule rather than a football, but maybe I can figure something out (or live with it).  

My next task is to try the particle systems for the dust and gas in the plane of the Galaxy.

-------------------------

