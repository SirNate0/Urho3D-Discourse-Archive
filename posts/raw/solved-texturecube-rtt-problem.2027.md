jmiller | 2017-01-02 01:12:24 UTC | #1

For a few weeks, [url=http://discourse.urho3d.io/t/procsky/1168/1]ProcSky component[/url] is failing to render TextureCube faces.  [b]ghidra[/b] helped to narrow the problem.

Unlike RenderToTexture sample, I did not need to setup RenderSurfaces or new viewports or rendering camera.. just render quads. I think the problem is not in the shader.

Currently I am looking at this in particular (edited slightly for clarity):

[code]
  // Create a Skybox to draw to. Set its Material, Technique, and render size.
  skybox_ = node_->CreateComponent<Skybox>();
  Model* model(cache->GetResource<Model>("Models/Box.mdl"));
  skybox_->SetModel(model);
  SharedPtr<Material> skyboxMat(new Material(context_));
  skyboxMat->SetTechnique(0, cache->GetResource<Technique>("Techniques/DiffSkybox.xml"));
  skyboxMat->SetCullMode(CULL_NONE);
  skybox_->SetMaterial(skyboxMat);
  SetRenderSize(renderSize_);

ProcSky::SetRenderSize(unsigned size) {
  // Create a TextureCube and assign to the ProcSky material.
  SharedPtr<TextureCube> skyboxTexCube(new TextureCube(context_));
  skyboxTexCube->SetName("DiffProcSky");
  skyboxTexCube->SetSize(size, Graphics::GetRGBAFormat(), TEXTURE_RENDERTARGET);
  skyboxTexCube->SetFilterMode(FILTER_BILINEAR);
  skyboxTexCube->SetAddressMode(COORD_U, ADDRESS_CLAMP);
  skyboxTexCube->SetAddressMode(COORD_V, ADDRESS_CLAMP);
  skyboxTexCube->SetAddressMode(COORD_W, ADDRESS_CLAMP);
  GetSubsystem<ResourceCache>()->AddManualResource(skyboxTexCube);
  skybox_->GetMaterial()->SetTexture(TU_DIFFUSE, skyboxTexCube);
  renderSize_ = size;
}
[/code]

Full source [github.com/carnalis/ProcSky/blo ... ProcSky.cc](https://github.com/carnalis/ProcSky/blob/master/ProcSky.cc)

Maybe I was not using the proper way to accomplish RTT.
Maybe a recent change requires one of my own?
Only this recent commit stands out: [github.com/urho3d/Urho3D/commit ... 54913455c8](https://github.com/urho3d/Urho3D/commit/1ba0958fa70a4042bfbc84958a9b7b54913455c8)
Any advice is welcome.

-------------------------

Enhex | 2017-01-02 01:12:25 UTC | #2

Regular RenderSurface RTT works for me, so your problem might be related to your custom quad command and/or shaders.

-------------------------

jmiller | 2017-01-02 01:12:26 UTC | #3

My shader has not changed and I am pretty sure is not being run.

The commands have not changed:

[code]
  Renderer* renderer(GetSubsystem<Renderer>());
  rPath_ = renderer->GetViewport(0)->GetRenderPath();

  // Add custom quad commands to render path.
  for (unsigned i(0); i < MAX_CUBEMAP_FACES; ++i) {
    RenderPathCommand cmd;
    cmd.tag_ = "ProcSky";
    cmd.type_ = CMD_QUAD;
    cmd.sortMode_ = SORT_BACKTOFRONT;
    cmd.pass_ = "base";
    cmd.outputs_.Push(MakePair(String("DiffProcSky"), (CubeMapFace)i));
    cmd.textureNames_[0] = String::EMPTY; // have tried "viewport" and not setting it
    cmd.vertexShaderName_ = "ProcSky";
    cmd.vertexShaderDefines_ = String::EMPTY; // have tried not setting it
    cmd.pixelShaderName_ = "ProcSky";
    cmd.pixelShaderDefines_ = String::EMPTY; // have tried not setting it
    cmd.shaderParameters_ = atmoParams;
    cmd.shaderParameters_["InvViewRot"] = faceRotations_[i];
    cmd.enabled_ = true;
    rPath_->AddCommand(cmd);
  }
[/code]

RenderPath dump
[code]
INFO: Command 0 tag= type=clear enabled=1 pass= outputs=viewport/face=0
INFO: Command 1 tag= type=scenepass enabled=1 pass=base outputs=viewport/face=0
INFO: Command 2 tag= type=forwardlights enabled=1 pass=light outputs=viewport/face=0
INFO: Command 3 tag= type=scenepass enabled=1 pass=postopaque outputs=viewport/face=0
INFO: Command 4 tag= type=scenepass enabled=1 pass=refract outputs=viewport/face=0
INFO: Command 5 tag= type=scenepass enabled=1 pass=alpha outputs=viewport/face=0
INFO: Command 6 tag= type=scenepass enabled=1 pass=postalpha outputs=viewport/face=0
INFO: Command 7 tag=FXAA2 type=quad enabled=1 pass= vs=FXAA2 ps=FXAA2 texNames[0]=viewport outputs=viewport/face=0
INFO: Command 8 tag=ProcSky type=quad enabled=1 pass=base vs=ProcSky ps=ProcSky outputs=DiffProcSky/face=0
INFO: Command 9 tag=ProcSky type=quad enabled=1 pass=base vs=ProcSky ps=ProcSky outputs=DiffProcSky/face=1
INFO: Command 10 tag=ProcSky type=quad enabled=1 pass=base vs=ProcSky ps=ProcSky outputs=DiffProcSky/face=2
INFO: Command 11 tag=ProcSky type=quad enabled=1 pass=base vs=ProcSky ps=ProcSky outputs=DiffProcSky/face=3
INFO: Command 12 tag=ProcSky type=quad enabled=1 pass=base vs=ProcSky ps=ProcSky outputs=DiffProcSky/face=4
INFO: Command 13 tag=ProcSky type=quad enabled=1 pass=base vs=ProcSky ps=ProcSky outputs=DiffProcSky/face=5
[/code]
DiffProcSky output is attached to a normal Skybox.
At this point, maybe the easiest approach is to try to imitate RTT sample, where possible.

-------------------------

cadaver | 2017-01-02 01:12:27 UTC | #4

I didn't experience problems when I pulled your ProcSky code and used it against latest master. I just had to change the object definition to

  URHO3D_OBJECT(ProcSky, Component);

I used the 08_Decals sample and created ProcSky to the same node as the Zone component, and called Initialize() after defining the viewport. When I pumped up the Rayleigh the sky textures lit up and saving them also showed content. I tested OpenGL3 under VS2010.

In case you still have trouble, you may need to debug inside Urho, into the View class where the renderpath commands are being executed, and see what happens.

-------------------------

jmiller | 2017-01-02 01:12:29 UTC | #5

Thanks for your valuable help, Lasse.

I have now tried your procedure: using the repo shader and source in 08_Decals. I did not get your result, as odd as it seems.

I changed my mingw-w64 toolchain (thanks minipix) which allowed me to debug into DLLs again.
View::RenderQuad() is being called, values/params seem correct, at first glance.
That should eliminate source code, shader, scene file, and all data files on my end.
I changed video drivers on the small chance of a problem there.

My cmake config, for anyone interested
[spoiler][code]
cmake -G "MinGW Makefiles" -D CMAKE_BUILD_TYPE=Debug -D CMAKE_CXX_FLAGS_DEBUG="-g" -D CMAKE_CXX_FLAGS="-march=native -Wno-error=narrowing" -D MINGW_SYSROOT="C:/mingw/x86_64-w64-mingw32" -D URHO3D_C++11=1 -D URHO3D_ANGELSCRIPT=1 -D URHO3D_DOCS_QUIET=1 -D DOXYGEN_SKIP_DOT=1 -D URHO3D_LIB_TYPE=SHARED -D URHO3D_MKLINK=1 -D URHO3D_OPENGL=1 -D URHO3D_SAMPLES=1 -D URHO3D_URHO2D=0 -D URHO3D_LOGGING=1 -D URHO3D_TOOLS=0 "%SOURCE%"
[/code]
-Wno-error=narrowing so gcc doesn't die on Bullet[/spoiler]

So I'm now going around looking outside the boxes... Will post any conclusions. :slight_smile:


[b]edit:[/b] will look further into View and maybe Graphics, because the render time is noticeably much much smaller with this bug.

-------------------------

jmiller | 2017-01-02 01:12:29 UTC | #6

Found it.

OGLGraphics.cpp
[github.com/urho3d/Urho3D/commit ... b31d26cdf5](https://github.com/urho3d/Urho3D/commit/3f861d67dd684d4ca9dbdbdcdbd6dfe9ec701407#diff-878294995c200c1ad22be2b31d26cdf5)

There have been problems with [b]GL_TEXTURE_CUBE_MAP_SEAMLESS[/b] (OpenGL 3.2) on some hardware; e.g., GeForce 9800 GT, 9600 GM

In these cases the vertex shader falls back to software and aborts, leaving only black.

I have created an issue on GitHub: [github.com/urho3d/Urho3D/issues/1380](https://github.com/urho3d/Urho3D/issues/1380)

State of affairs:
Application developers can disable the extension in Urho's Graphics cpp implementations, and if they have fixes that are clean enough they can be PR'd.

-------------------------

