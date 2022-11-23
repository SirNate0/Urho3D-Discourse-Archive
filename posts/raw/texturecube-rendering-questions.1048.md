jmiller | 2017-01-02 01:05:03 UTC | #1

I've been working on implementing a procedural sky I'd like to share when completed (maybe a tutorial), but being a noob at some of this, I'm still missing some thing(s).

A technique I'm currently using uses multiple cubemaps as layers - sky, sunlight, sun, etc. The faces are rendered by quad to named rendertargets ('auxiliary views' with no camera/scene), which should be sampled later by 'inner' cubes. Then I have a Skybox sample that and render to the camera/scene view.

The problem seems to be that nothing is rendered to the quads.

Here's part of the setup for one cube.

[code]
texCube_.SetSize(128, Graphics::GetRGBAFormat(), TEXTURE_RENDERTARGET);
String name = "texcube";
String textureName = "viewport"; // other cubes use named rendertargets

for (unsigned i = 0; i < MAX_CUBEMAP_FACES; ++i) {
  RenderTargetInfo rti;
  rti.name = name + String(i);
  rti.tag_ = name;
  rti.filtered_ = true;
  rti.persistent_ = true;
  rti.size_ = Vector2(128, 128);
  rti.format_ = Graphics::GetRGBAFormat();
  renderPath->AddRenderTarget(rti);

  RenderPathCommand rpc;
  rpc.tag_ = name;
  rpc.type_ = CMD_QUAD;
  rpc.pass_ = "base";
  rpc.vertexShadername = "renderface";
  rpc.pixelShadername = "renderface";
  rpc.outputNames_.Push(name + String(i));

  if (textureName != "viewport") {
    textureName += String(i); // sequential 
  }
  rpc.textureNames_[TU_DIFFUSE] = textureName;
  renderPath->AddCommand(rpc);

  RenderSurface* surf = texCube_.GetRenderSurface((CubeMapFace)i);
  SharedPtr<Viewport> vp(new Viewport(context_, NULL, NULL, renderPath));
  surf->SetViewport(0, vp);

  surf->SetUpdateMode(SURFACE_UPDATEALWAYS); // manual later
//etc
}
[/code]

Grateful for any advice.

-------------------------

cadaver | 2017-01-02 01:05:03 UTC | #2

The renderpath doesn't currently support rendering a QUAD command to a named texture cubemap face (only 2D textures), so right now you should actually setup the individual cubemap faces as true auxiliary views (similar to the RenderToTexture example) with their own renderpaths, in which case a specific face of the cubemap is referred to as the "viewport" final target surface. This is inconvenient, so the possibility should be added.

Note also that if you want the renderpath to find the named texture you have explicitly created in the code, you must add it to the resource cache as a manual resource. This is not necessary if it's the "viewport" target surface we're talking about, as that is specified by the Viewport.

-------------------------

cadaver | 2017-01-02 01:05:04 UTC | #3

I'm working on a branch "renderpath-cubemap" which improves the flexibility of the renderpath. Using that branch, renderpaths can define cubemap rendertargets, can refer to programmatically created rendertarget textures stored as manual resources (by name) and can set the output face in commands. I cannot guarantee 100% that it will  be merged before next release, as it carries a risk of breaking something.

Using this branch, you could setup a dynamic skybox as follows (AngelScript example, this just demonstrates CLEAR commands for all faces added in the current renderpath, but any command should naturally work)

[code]
    TextureCube@ texCube = TextureCube();
    texCube.name = "DynamicSky";
    cache.AddManualResource(texCube); // To allow the texture to be found by View to use as a rendertarget
    texCube.SetSize(256, GetRGBAFormat(), TEXTURE_RENDERTARGET);
    skybox.materials[0].textures[0] = texCube;

    for (int i = 0; i < 6; ++i)
    {
        RenderPathCommand cmd;
        cmd.type = CMD_CLEAR;
        cmd.clearFlags = CLEAR_COLOR;
        cmd.clearColor = Color(Random(), Random(), Random());
        cmd.SetOutput(0, "DynamicSky", CubeMapFace(i)); // This is a new function, sets output name and face at the same time
        renderer.viewports[0].renderPath.InsertCommand(i, cmd);
    }
[/code]

Alternatively you could setup the dynamic sky render purely in renderpath xml (this requires a sky material that actually does not set the diffuse texture, as it's set globally for the postopaque pass, but that's somewhat unreliable so I wouldn't necessarily recommend it)

[code]
<renderpath>
    <rendertarget name="sky" cubemap="true" size="128 128" format="rgb" />
    <command type="clear" output="sky" face="0" color="1 0 0 1" />
    <command type="clear" output="sky" face="1" color="0 1 0 1" />
    <command type="clear" output="sky" face="2" color="0 0 1 1" />
    <command type="clear" output="sky" face="3" color="1 1 0 1" />
    <command type="clear" output="sky" face="4" color="0 1 1 1" />
    <command type="clear" output="sky" face="5" color="1 0 1 1" />
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque">
        <texture unit="diffuse" name="sky" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>
[/code]

-------------------------

jmiller | 2017-01-02 01:05:04 UTC | #4

Yet another feature added before we can even start simple workarounds.  :slight_smile:   Much appreciated, as well as your explanations.
Already using the branch so I expect to be doing some testing.

-------------------------

cadaver | 2017-01-02 01:05:05 UTC | #5

The branch has been merged to the master, as there were other RenderPath fixes and shader changes as well, so just need testing.

-------------------------

jmiller | 2017-01-02 01:05:16 UTC | #6

Maybe a lost cause, but worth asking if at a glance someone can see how this could be setup in Urho?
[github.com/pyalot/WebGL-City-SS ... master/sky](https://github.com/pyalot/WebGL-City-SSAO/tree/master/sky)
cubemap impl [github.com/pyalot/WebGL-City-SS ... cubemap.js](https://github.com/pyalot/WebGL-City-SSAO/blob/master/glee/cubemap.js)

I have multiple TextureCubes, some of different size, whose faces are rendered by a bunch of quad commands in 'base' pass. For performance, these would be updated manually.
One cube is assigned to the Material of a normal Skybox rendered in the postopaque scenepass.

Here is an orthographic with 'clear' colors used
[url=http://ctrlv.in/579081][img]http://img.ctrlv.in/img/15/05/25/5562a6d03ed68.jpg[/img][/url]

Seems that the renders are not scaled to the destination textures (which I guess is expected - only viewport?).

-------------------------

cadaver | 2017-01-02 01:05:16 UTC | #7

Can you show the renderpath you have now?

-------------------------

jmiller | 2017-01-02 01:05:17 UTC | #8

I'm generating the renderpath commands programmatically as shown below; here is a dump.
0-6 are the standard Forward.
(The image in my last post is with command outputs set to the 'display' texcube)

[code]
0 tag= type=CMD_CLEAR pass= vs= ps= vsd= psd= texNames[0]= outputs=viewport/face=0
1 tag= type=CMD_SCENEPASS pass=base vs= ps= vsd= psd= texNames[0]= outputs=viewport/face=0
2 tag= type=CMD_FORWARDLIGHTS pass=light vs= ps= vsd= psd= texNames[0]= outputs=viewport/face=0
3 tag= type=CMD_SCENEPASS pass=postopaque vs= ps= vsd= psd= texNames[0]= outputs=viewport/face=0
4 tag= type=CMD_SCENEPASS pass=refract vs= ps= vsd= psd= texNames[0]= outputs=viewport/face=0
5 tag= type=CMD_SCENEPASS pass=alpha vs= ps= vsd= psd= texNames[0]= outputs=viewport/face=0
6 tag= type=CMD_SCENEPASS pass=postalpha vs= ps= vsd= psd= texNames[0]= outputs=viewport/face=0
7 tag=clear type=CMD_CLEAR pass=base vs= ps= vsd= psd= texNames[0]= outputs=display/face=0
8 tag=display type=CMD_QUAD pass=base vs=display ps=display vsd= psd= texNames[0]= outputs=display/face=0
10 tag=clear type=CMD_CLEAR pass=base vs= ps= vsd= psd= texNames[0]= outputs=display/face=1
11 tag=display type=CMD_QUAD pass=base vs=display ps=display vsd= psd= texNames[0]= outputs=display/face=1
13 tag=clear type=CMD_CLEAR pass=base vs= ps= vsd= psd= texNames[0]= outputs=display/face=2
14 tag=display type=CMD_QUAD pass=base vs=display ps=display vsd= psd= texNames[0]= outputs=display/face=2
...
113 tag=diffuse_sun type=CMD_QUAD pass=base vs=cubemap_convolve ps=cubemap_convolve vsd= psd= texNames[0]=level3 outputs=diffuse_sun/face=5
[/code]


[code]
// ... AddManualResource(texCube)...

for (unsigned i = 0; i < MAX_CUBEMAP_FACES; ++i) {
  // [conditionally add clear command]

  RenderPathCommand cmd;
  cmd.tag_ = name_;
  cmd.type_ = CMD_QUAD;
  cmd.sortMode_ = SORT_BACKTOFRONT;
  cmd.pass_ = "base";
  cmd.vertexShaderName_ = params["vs"].GetString();
  cmd.pixelShaderName_ = params["ps"].GetString();
  Vector<String> outputs = params["outputs"].GetString().Split(';');
  for (auto j = outputs.Begin(); j != outputs.End(); ++j) {
    if (!(*j).Empty()) { cmd.outputs_.Push(MakePair(*j, (CubeMapFace)i)); }
  }
  cmd.textureNames_[TU_DIFFUSE] = params["textures"].GetString();
  cmd.shaderParameters_ = shaderParameters_;
  cmd.enabled_ = true;
  rPath_->AddCommand(cmd); // main renderpath
}
[/code]

-------------------------

cadaver | 2017-01-02 01:05:17 UTC | #9

Thanks. Will have to check the viewport size determination logic, or if that can't be easily fixed, allow viewport to be set explicitly in renderpath commands.

-------------------------

cadaver | 2017-01-02 01:05:18 UTC | #10

There was a bug; the backbuffer's viewport was being used even when rendering to some other rendertarget. Should be fixed in the master branch now. It was undetectable as long as the other texture was smaller or equal in size to the backbuffer.

-------------------------

jmiller | 2017-01-02 01:05:18 UTC | #11

I updated but do not notice a change from the posted image.

Also, if I declare RenderTargets with or without AddManualResource, all outputs are black, even clears:
[code]rti.name_ = name_;
rti.cubemap_ = true;
rti.filtered_ = filtered;
rti.persistent_ = persistent;
rti.size_ = Vector2(size, size);
rti.format_ = Graphics::GetRGBAFormat();[/code]

[code]RenderTarget 0 name=display format=6408 size=128 enabled=1 cubemap=1 filtered=1 persistent=1
RenderTarget 1 name=irradiance_sun format=6408 size=128 enabled=1 cubemap=1 filtered=0 persistent=1
RenderTarget 2 name=level1 format=6408 size=64 enabled=1 cubemap=1 filtered=0 persistent=1
RenderTarget 3 name=level2 format=6408 size=32 enabled=1 cubemap=1 filtered=0 persistent=1
RenderTarget 4 name=level3 format=6408 size=16 enabled=1 cubemap=1 filtered=0 persistent=1
RenderTarget 5 name=diffuse_sun format=6408 size=16 enabled=1 cubemap=1 filtered=1 persistent=1
[/code]

-------------------------

cadaver | 2017-01-02 01:05:18 UTC | #12

Can you post some sort of complete or mostly complete test application that shows the problem? Doesn't need your custom shaders, just using clear commands should be enough to showcase the problem.

-------------------------

jmiller | 2017-01-02 01:05:20 UTC | #13

Thanks, your PM shed some light on things.
Using MRT scales to only the first target - noted (I don't need MRT, just used to see the textures at all).

The shaders seem to be only writing the clear and test colors, but I can hunt down uniform problems myself.

The main question I still have is how the cubemaps can be drawn "over" each other with alpha, when only a couple actually do any sampling.

-------------------------

cadaver | 2017-01-02 01:05:20 UTC | #14

To sample the previous passes' cubemaps, set them as texture inputs in quad commands outputting to another cubemap.

As there currently is no blend mode for the QUAD command, you need to set all needed inputs (for one cubemap target) at once and do the blending manually in shader. That will probably be better for performance than hardware blending via multipass, if you're able to do that. However adding blendmode to quads should not be hard.

-------------------------

cadaver | 2017-01-02 01:05:22 UTC | #15

Blend mode has been added to QUAD commands in the renderpath (default = replace).

-------------------------

jmiller | 2017-01-02 01:05:22 UTC | #16

Wow, this is convenient - thanks again. I think we can say Urho3D has excellent cubemap support  :sunglasses:

-------------------------

