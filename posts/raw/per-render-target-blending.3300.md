sabotage3d | 2017-07-01 21:30:06 UTC | #1

I am trying to implement OIT in Urho3D and I need to do different blending for each target. What I am not sure if I am doing it correctly. Currently I added two new blending modes reveal and composite. This is the relevant code from the paper.

    glDepthMask(GL_FALSE);
    glEnable(GL_BLEND);
    // Accum Target 
    glBlendFunci(0, GL_ONE, GL_ONE);
    // Reveal Target
    glBlendFunci(1, GL_ZERO, GL_ONE_MINUS_SRC_ALPHA);

    // Composite the quad
    glBlendFunc(GL_ONE_MINUS_SRC_ALPHA, GL_SRC_ALPHA);

I have matched the above OpenGL code in Urho3d with two new blending modes reveal and composite. But instead of glBlendFunci I am using glBlendFunc the default in Urho3D.
In my technique I have the code below:

    <pass name="oit_accum" depthtest="always" depthwrite="false" blend="add" /> 
    <pass name="oit_reveal" depthtest="always" depthwrite="false" blend="reveal" /> 

In my renderpath I have:

    <command type="quad" tag="OIT_copy" enabled="true" vs="OIT_copy" ps="OIT_copy" blend="composite" output="viewport">

Would that be enough to get these blending modes working? Is Per-Render Target Blending currently supported at all?

-------------------------

sabotage3d | 2017-07-06 00:01:21 UTC | #2

Are passes with different blending supported? I can't get the correct blending. Do I need to render each to separate quad?
My passes are currently.

    <command type="scenepass" pass="oit_accum" vertexlights="true" metadata="gbuffer" >
        <output index="0" name="diffuse" />
    </command>
    <command type="scenepass" pass="oit_reveal" vertexlights="true" metadata="gbuffer">
        <output index="1" name="emissive" />
    </command>

-------------------------

