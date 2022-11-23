Haukinger | 2020-06-22 20:04:36 UTC | #1

Hi there,

I'm on windows and my fragment shader does some raymarching. It writes to the frame buffer just fine, but I have no idea how I can write to another render target and how to read that from the application. I would like to get a buffer that for each pixel contains the world coordinates of the end point of the ray that produced the color of the pixel. I hoped that something along the line of fragData[1] = vec4(rayX, rayY, rayZ, 0.0) would do the job, but I either get index out of bounds or and empty bitmap or no rendered image at all.

Can you point me to documentation or an example?

-------------------------

ab4daa | 2020-06-23 03:15:54 UTC | #2

I think you could take a look at Deferred render path which output 4 targets(viewport, albedo, normal and depth) and use them in following render command.
https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/RenderPaths/Deferred.xml#L9

and its shader part(define DEFERRED)
https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/Shaders/HLSL/LitSolid.hlsl#L285

-------------------------

Haukinger | 2020-06-23 16:56:26 UTC | #3

Thanks a lot, I made progress. My render path is this now

    <renderpath>
      <rendertarget name="albedo" rtsizedivisor="1 1" format="rgba" />
      <command type="clear" color="0 0 0 0" output="viewport" />
      <command type="clear" color="0 0 0 0" output="albedo" />
      <command type="scenepass" pass="deferred" metadata="gbuffer">
        <output index="0" name="viewport" />
        <output index="1" name="albedo" />
      </command>
    </renderpath>

and the technique is

    <technique vs="MyShader" ps="MyShader" vsdefines="NOUV" psdefines="DEFERRED" >
        <pass name="deferred" />
    </technique>

and the shader writes to fragData[1] without visible errors, but also without visible results.

I've created a texture and assigned it to rendertarget 1, but whenever I do GetData on that texture, it's all zero. If I make the shader write the additional data to gl_FragColor (that is, fragData[0], isn't it?), the data looks good.

I've set the texture's usage to rendertarget, anything else I might be missing?

EDIT: I've added the texture to the resource cache, and suddenly it contains data :-)

-------------------------

