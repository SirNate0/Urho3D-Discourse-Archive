setzer22 | 2017-01-02 01:00:09 UTC | #1

[b]EDIT:[/b] I solved my problem so I'll share what I've learnt.

My goal was to do this:
[img]https://photos-4.dropbox.com/t/0/AACOBgxU5B-HjeD2GaHQuEj_RCtJWlrEMaB7MDXlZIY21g/12/25396264/png/1024x768/3/1409083200/0/2/urhoterrain.png/CM6p4IXKy8Euuzdt02XAEUlz25VUnHV79465TBl6-98[/img]

To do it I used a custom shader (which still needs a lot of fine tuning). Here's the pixel shader code (GLSL) for it:

[code] float cx = mod(vWorldPos.x,10);
    float cz = mod(vWorldPos.z,10);
    float e = 0.5;
    
    if(!((cx > 10.0-e && cx < 10.0+e) || (cz > 10.0-e && cz < 10.0+e)) ) {//inside a square
		float dist = max(abs(cx-5.0), abs(cz-5.0)) / 10.0;
		if(dist > 0.8) dist * 0.5;
	    gl_FragColor = vec4(0.0, 0.0, 0.0, dist);
	}
	else //outside a square
		gl_FragColor = normalize(vec4(1.0, 1.0, 1.0, 0.0));[/code]

So now, how do I render this on top of existing geometry? You have to modify the material's technique, or in case it's using more than one technique, modify them all. In my case, I renamed the TerrainBlend.xml technique file to TerrainBlend_CUSTOM.xml. Here's the content of the file:

[code]<technique vs="TerrainBlend" ps="TerrainBlend">

	<pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />  

	<pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" /> 
    <pass name="grid" vs ="TerrainBlend2" ps="TerrainBlend2" blend="alpha" />
</technique>[/code]

The content is the same as the original except the last pass which is named grid. In order for that to work I had to tell the viewport when and how to render this "grid" pass by the means of a RenderPath. To do so I added the line 
[code]<command type="scenepass" pass="grid" sort="backtofront" />[/code]
to the [b]end[/b] of the RenderPath file I wanted to use. I assume adding it at the end is important, as it's in the render path where the pass render order is decided, and not in the technique (Someone please confirm this). After this, I have set up the viewport with the custom RenderPath like this (in AngelScript):

[code]RenderPath@ renderPath = RenderPath();
	XMLFile@ xml = cache.GetResource("XMLFile","RenderPaths/Forward.xml");
	renderPath.Load(xml);
	Viewport@ viewport = Viewport(gameScene, cameraNodeBis.GetComponent("Camera"), renderPath);
    renderer.viewports[0] = viewport;[/code]

Of course I also had to modify the terrain material to point to the new technique (the custom one) instead of the old. I could also have duplicated the material like I did with the technique.

The result of all this is the screenshot above!



[b][u]Original post:[/u][/b]

[quote]Hello everyone!

First of all I'd like to say that I'm new to this community as I just started using urho3d yesterday and I'm impressed with this project. I'd like to contribute as I can, probably with a tutorial series and of course spreading the word! But for now, I'm still trying to learn the engine and I've come across this question:

I want to make a custom shader and render it after the main terrain pass (for the terrain shader) has been rendered in order to paint a grid on top of the terrain. I have successfully done this in Unity but I'm really lost on how do shaders work with Urho. As far as I can see there are three things that define a material:

[ul]
- The XML material file.
- The Technique.
- The HLSL/GLSL shader.
[/ul]

How do these relate? I can see that the material file defines both the properties for the shader and the technique for it. I assume the properties are accessible in the shader code. How can I access them from within the shader?

For the technique, I can see a list of passes like this one for example:
[code]<pass name="shadow" vs="Shadow" ps="Shadow" />[/code]

I suppose that vs and ps are the vertex and pixel shaders for the pass, and that the name on it refers to a shader in Bin/CoreData/Shaders, am I right? As for the name I have no clue so I'd like to ask what's it for as well.

Regarding the shader itself, I've also got several questions:

[ul]
- Am I forced to write both GLSL and HLSL shaders if I'm not planning on using Direct3D in my project? 
- I'm not planning on using any kind of lighging in my shader pass for now, as it's just a painted grid. Should I just omit those defines I keep finding at the start of each shader definition? I refer to things like PERPIXEL, SPOTLIGHT...
- I'd like to be able to pass an array of custom data to my shader as an attribute / property. Can I do this? I'm aware that for example that is impossible within unity and I had to pass that data as a texture. I'm also interested into changing that data on the fly efficiently. Is that possible? I'm not asking for a full answer, but some guides to aid my research would be really helpful.
[/ul]

This is all, any help will be much appreciated. 

Thank you![/quote]

-------------------------

friesencr | 2017-01-02 01:00:09 UTC | #2

You do not have to implement hlsl shaders.

The SPOTLIGHT, PERPIXEL are used in the LitSolid.glsl base.  If you want do not want lighting you should use Basic or Unlit instead of LitSolid.

Materials, RenderPath, and RenderPathCommand expose shaderParameters.  You can define your custom parameters there.

Sorry for being so brief.  Time is no friend of mine.

-------------------------

setzer22 | 2017-01-02 01:00:09 UTC | #3

[quote="friesencr"]You do not have to implement hlsl shaders.

The SPOTLIGHT, PERPIXEL are used in the LitSolid.glsl base.  If you want do not want lighting you should use Basic or Unlit instead of LitSolid.

Materials, RenderPath, and RenderPathCommand expose shaderParameters.  You can define your custom parameters there.

Sorry for being so brief.  Time is no friend of mine.[/quote]

Thank you, I'm begginning to understand how shaders work, and I've really read through the whole documentation on shaders. But it still feels like really overwhelming...

Instead of asking what I don't understand, which is a lot, I'll ask what my goal is to avoid falling into an XY problem. Some guidance on how to achieve that might help a lot.

What I want is: Given an existing material (the terrain one, for example), I want it to render a grid over the geometry using shaders. So all the terrain should be rendered normally, and after that an additional pass will be made, painting just a grid with transparent holes (and the geometry will be seen through those). The grid part is easy, I've already done that, and in fact modifying the TerrainBlend.glsl file has lead to almost the desired effect. What I want to do, though, is render the grid with alpha blending on a new pass after the TerrainBlend pass has been made. This would seem easy but when I see the technique description I don't even know where to begin:

[code]<technique vs="TerrainBlend" ps="TerrainBlend">
	<pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>[/code]

My naive approach was to add the line 

[code]<pass name="grid" vs="Grid" ps="Grid" />[/code]

The Grid shader does nothing special on the vertex shader (I copied it from unlit) and uses the world position to determine if it has to render the grid on a pixel during the fragment shader. The only problem is that the engine doesn't seem to even notice my pass. More importantly, when setting the pass name to "alpha", it draws the grid but doesn't do any alpha blending at all, so all the regions where the terrain should still be painted are instead rendered black.

I'm completely lost with this.

[b]EDIT:[/b] I figured it out! Now everything's working as I expected. I've also updated the original post with a description of what I did.

-------------------------

